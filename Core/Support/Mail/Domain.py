# Email domain intelligence: mail server records (MX, SPF, DMARC, MTA-STS),
# disposable/free provider detection and breach data from the official
# Have I Been Pwned API (per-account lookup only when an API key is configured).

import os
import re
import time
from configparser import ConfigParser
from urllib.parse import quote

from Core.Support import Font
from Core.Support import Http
from Core.Support import Results
from Core.Support.Websites import Recon

DISPOSABLE_URL = ("https://raw.githubusercontent.com/disposable-email-domains/"
                  "disposable-email-domains/master/disposable_email_blocklist.conf")
DISPOSABLE_CACHE = "Temp/E-Mail/disposable_domains.txt"
CACHE_DAYS = 7
HIBP = "https://haveibeenpwned.com/api/v3"
FREE_PROVIDERS = {"gmail.com", "googlemail.com", "outlook.com", "hotmail.com", "live.com", "msn.com",
                  "yahoo.com", "ymail.com", "icloud.com", "me.com", "mac.com", "aol.com", "gmx.com",
                  "gmx.net", "gmx.de", "web.de", "mail.com", "yandex.com", "yandex.ru", "mail.ru",
                  "proton.me", "protonmail.com", "pm.me", "tutanota.com", "tuta.io", "zoho.com",
                  "libero.it", "virgilio.it", "orange.fr", "laposte.net", "qq.com", "163.com"}


def _say(label, value):
    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "{}: {}".format(label, value))


def _warn(text):
    print(Font.Color.RED + "[!]" + Font.Color.WHITE + text)


def hibp_key():
    parser = ConfigParser()
    parser.read("Configuration/Configuration.ini")
    key = parser.get("Settings", "hibp_api_key", fallback="").strip()
    return key if key and key.lower() != "none" else None


def mail_records(domain):
    mx = sorted(Recon.dns_query(domain, "MX"), key=lambda r: int(r.split()[0]) if r.split()[0].isdigit() else 0)
    txt = [t.strip('"') for t in Recon.dns_query(domain, "TXT")]
    spf = [t for t in txt if t.lower().startswith("v=spf1")]
    dmarc = [t.strip('"') for t in Recon.dns_query("_dmarc." + domain, "TXT") if "v=DMARC1" in t]
    policy = re.search(r"\bp=(\w+)", dmarc[0]).group(1) if dmarc and re.search(r"\bp=(\w+)", dmarc[0]) else None
    mta_sts = [t.strip('"') for t in Recon.dns_query("_mta-sts." + domain, "TXT")]
    # RFC 7505 null MX ("0 .") means the domain explicitly refuses email
    accepts = any(r.split()[-1] != "." for r in mx)
    return {"mx": mx, "accepts_mail": accepts, "spf": spf, "dmarc": dmarc, "dmarc_policy": policy,
            "mta_sts": bool(mta_sts)}


def disposable_domains():
    fresh = os.path.isfile(DISPOSABLE_CACHE) and time.time() - os.path.getmtime(DISPOSABLE_CACHE) < CACHE_DAYS * 86400
    if not fresh:
        try:
            r = Http.get(DISPOSABLE_URL)
            if r.status_code == 200 and r.text.strip():
                os.makedirs(os.path.dirname(DISPOSABLE_CACHE), exist_ok=True)
                with open(DISPOSABLE_CACHE, "w", encoding="utf-8") as f:
                    f.write(r.text)
        except Exception:
            pass
    try:
        with open(DISPOSABLE_CACHE, encoding="utf-8") as f:
            return {line.strip().lower() for line in f if line.strip() and not line.startswith("#")}
    except OSError:
        return None


def domain_breaches(domain):
    data = Http.get_json("{}/breaches".format(HIBP), params={"domain": domain},
                         headers={"User-Agent": "Mr.Holmes"})
    if data is None:
        return None
    return [{"name": b.get("Name"), "date": b.get("BreachDate"), "accounts": b.get("PwnCount"),
             "data": b.get("DataClasses", [])} for b in data]


def account_breaches(email, key):
    r = Http.get("{}/breachedaccount/{}".format(HIBP, quote(email)),
                 params={"truncateResponse": "false"},
                 headers={"hibp-api-key": key, "User-Agent": "Mr.Holmes"})
    if r.status_code == 404:
        return []
    if r.status_code != 200:
        raise RuntimeError("HIBP HTTP {}".format(r.status_code))
    return [{"name": b.get("Name"), "date": b.get("BreachDate"), "data": b.get("DataClasses", [])}
            for b in r.json()]


def run(email, report):
    domain = email.rsplit("@", 1)[-1].strip().lower()
    results = {"email": email, "domain": domain}
    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "ANALYZING MAIL DOMAIN: {}".format(domain))

    results["records"] = mail_records(domain)
    rec = results["records"]
    for mx in rec["mx"]:
        _say("MX", mx)
    if not rec["accepts_mail"]:
        _warn("DOMAIN HAS NO MX RECORDS: IT CANNOT RECEIVE EMAIL")
    _say("SPF", rec["spf"][0] if rec["spf"] else "MISSING")
    _say("DMARC", rec["dmarc"][0] if rec["dmarc"] else "MISSING")
    if rec["dmarc_policy"] in (None, "none"):
        _warn("DMARC POLICY IS {}: DOMAIN CAN BE SPOOFED MORE EASILY".format(rec["dmarc_policy"] or "MISSING"))
    _say("MTA-STS", "ENABLED" if rec["mta_sts"] else "NOT CONFIGURED")

    disposable = disposable_domains()
    results["disposable"] = None if disposable is None else domain in disposable
    results["free_provider"] = domain in FREE_PROVIDERS
    _say("DISPOSABLE PROVIDER", "UNKNOWN (LIST UNAVAILABLE)" if disposable is None else results["disposable"])
    _say("FREE PROVIDER", results["free_provider"])

    if not results["free_provider"]:
        results["domain_breaches"] = domain_breaches(domain)
        if results["domain_breaches"] is None:
            _warn("HAVE I BEEN PWNED UNAVAILABLE")
        elif results["domain_breaches"]:
            for b in results["domain_breaches"]:
                _warn("DOMAIN BREACH: {} ({}) {} ACCOUNTS".format(b["name"], b["date"], b["accounts"]))
        else:
            _say("DOMAIN BREACHES", "NONE KNOWN")

    key = hibp_key()
    if key:
        try:
            results["account_breaches"] = account_breaches(email, key)
            if results["account_breaches"]:
                for b in results["account_breaches"]:
                    _warn("ACCOUNT IN BREACH: {} ({}) DATA: {}".format(b["name"], b["date"], ", ".join(b["data"])))
            else:
                _say("ACCOUNT BREACHES", "NONE KNOWN")
        except Exception as e:
            _warn("ACCOUNT BREACH CHECK FAILED: {}".format(e))
    else:
        print(Font.Color.BLUE + "[I]" + Font.Color.WHITE +
              "SET hibp_api_key IN Configuration/Configuration.ini TO CHECK THIS ACCOUNT AGAINST BREACHES")

    with open(report, "a", encoding="utf-8") as f:
        f.write("\nMAIL DOMAIN ANALYSIS:\n")
        for k, v in results.items():
            f.write("{}: {}\n".format(k.upper(), v))
    Results.save(report, "mail_domain", results)
    return results
