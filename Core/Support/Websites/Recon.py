# Technical reconnaissance for a domain or IP: DNS, RDAP registration data,
# TLS certificate, certificate-transparency subdomains, HTTP security posture,
# technology fingerprint, security.txt, sitemap and Wayback Machine history.
# Every check is independent: a failing source never stops the others.

import ipaddress
import re
import socket
import ssl
from datetime import datetime, timezone

from Core.Support import Font
from Core.Support import Http
from Core.Support import Results

DOH = "https://cloudflare-dns.com/dns-query"
DNS_TYPES = ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "CAA", "SOA"]
SECURITY_HEADERS = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options",
                    "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy",
                    "Cross-Origin-Opener-Policy"]
TECH_HEADERS = ["Server", "X-Powered-By", "X-Generator", "X-AspNet-Version", "X-AspNetMvc-Version",
                "X-Drupal-Cache", "X-Shopify-Stage", "X-Vercel-Id", "X-Nf-Request-Id", "CF-Ray",
                "X-Amz-Cf-Id", "X-Served-By", "Via"]
TECH_SIGNATURES = {
    "WordPress": [r"/wp-content/", r"/wp-includes/"],
    "Drupal": [r"Drupal\.settings", r"/sites/default/files/"],
    "Joomla": [r"/media/jui/", r"Joomla!"],
    "Shopify": [r"cdn\.shopify\.com"],
    "Wix": [r"static\.wixstatic\.com"],
    "Squarespace": [r"static1\.squarespace\.com"],
    "Next.js": [r"/_next/static/", r"__NEXT_DATA__"],
    "Nuxt": [r"__NUXT__", r"/_nuxt/"],
    "Gatsby": [r"___gatsby"],
    "React": [r"data-reactroot", r"react-dom"],
    "Angular": [r"ng-version="],
    "Vue.js": [r"data-v-[0-9a-f]{8}"],
    "jQuery": [r"jquery[.-][0-9.]*(?:min\.)?js"],
    "Bootstrap": [r"bootstrap(?:\.min)?\.(?:css|js)"],
    "Google Analytics": [r"googletagmanager\.com/gtag", r"google-analytics\.com"],
    "Google Tag Manager": [r"googletagmanager\.com/gtm\.js"],
    "Cloudflare": [r"cdnjs\.cloudflare\.com", r"/cdn-cgi/"],
}
TECH_HEADER_HINTS = {"CF-Ray": "Cloudflare", "X-Vercel-Id": "Vercel", "X-Nf-Request-Id": "Netlify",
                     "X-Amz-Cf-Id": "Amazon CloudFront", "X-Shopify-Stage": "Shopify", "X-Drupal-Cache": "Drupal"}


def _say(label, value):
    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "{}: {}".format(label, value))


def _title(text):
    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + text)


def _warn(text):
    print(Font.Color.RED + "[!]" + Font.Color.WHITE + text)


def is_ip(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False


def normalize(target):
    target = target.strip().lower()
    target = re.sub(r"^[a-z]+://", "", target)
    return target.split("/")[0].split(":")[0]


# ---------- DNS ----------

def dns_query(name, rtype):
    data = Http.get_json(DOH, headers={"Accept": "application/dns-json"},
                         params={"name": name, "type": rtype})
    if not data or data.get("Status") != 0:
        return []
    return [a["data"] for a in data.get("Answer", []) if a.get("data")]


def dns_records(domain):
    records = {}
    for rtype in DNS_TYPES:
        values = dns_query(domain, rtype)
        if values:
            records[rtype] = values
    return records


# ---------- RDAP (registration metadata) ----------

def _vcard_name(entity):
    for item in (entity.get("vcardArray") or [None, []])[1]:
        if item and item[0] == "fn":
            return item[3]
    return None


def rdap(domain):
    data = Http.get_json("https://rdap.org/domain/{}".format(domain), allow_redirects=True)
    if not data:
        return {}
    info = {"handle": data.get("handle"), "status": data.get("status", []),
            "nameservers": [ns.get("ldhName") for ns in data.get("nameservers", [])],
            "dnssec": (data.get("secureDNS") or {}).get("delegationSigned")}
    for event in data.get("events", []):
        info[event.get("eventAction", "event")] = event.get("eventDate")
    for entity in data.get("entities", []):
        if "registrar" in entity.get("roles", []):
            info["registrar"] = _vcard_name(entity)
            for pid in entity.get("publicIds", []):
                info["registrar_iana_id"] = pid.get("identifier")
    return info


# ---------- TLS ----------

def tls_certificate(host, port=443):
    ctx = ssl.create_default_context()
    with socket.create_connection((host, port), timeout=8) as sock:
        with ctx.wrap_socket(sock, server_hostname=host) as tls:
            cert = tls.getpeercert()
            version = tls.version()
            cipher = tls.cipher()[0]
    flat = lambda seq: {k: v for part in seq for k, v in part}
    not_after = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
    return {"subject": flat(cert.get("subject", [])).get("commonName"),
            "issuer": flat(cert.get("issuer", [])).get("organizationName") or flat(cert.get("issuer", [])).get("commonName"),
            "valid_from": cert.get("notBefore"), "valid_until": cert.get("notAfter"),
            "days_left": (not_after - datetime.now(timezone.utc)).days,
            "san": [v for k, v in cert.get("subjectAltName", []) if k == "DNS"],
            "protocol": version, "cipher": cipher}


# ---------- Certificate transparency ----------

def ct_subdomains(domain):
    data = Http.get_json("https://crt.sh/", params={"q": "%." + domain, "output": "json"},
                         timeout=(8, 60))
    if data is None:
        return None
    names = set()
    for entry in data:
        for name in str(entry.get("name_value", "")).splitlines():
            name = name.strip().lower().lstrip("*.")
            if name.endswith("." + domain):
                names.add(name)
    return sorted(names)


# ---------- HTTP profile ----------

def http_profile(host):
    response = None
    for scheme in ("https", "http"):
        try:
            response = Http.get("{}://{}".format(scheme, host), allow_redirects=True)
            break
        except Exception:
            continue
    if response is None:
        return {}
    headers = response.headers
    html = response.text[:500000]
    title = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    generator = re.search(r'<meta[^>]+name=["\']generator["\'][^>]+content=["\']([^"\']+)', html, re.I)
    tech = set(TECH_HEADER_HINTS[h] for h in TECH_HEADER_HINTS if h in headers)
    for name, patterns in TECH_SIGNATURES.items():
        if any(re.search(p, html, re.I) for p in patterns):
            tech.add(name)
    if generator:
        tech.add(generator.group(1).strip())
    cookies = []
    for c in response.cookies:
        cookies.append({"name": c.name, "secure": c.secure,
                        "httponly": c.has_nonstandard_attr("HttpOnly") or c.has_nonstandard_attr("httponly"),
                        "samesite": c.get_nonstandard_attr("SameSite") or c.get_nonstandard_attr("samesite")})
    return {"final_url": response.url, "status": response.status_code,
            "redirects": [r.url for r in response.history],
            "title": title.group(1).strip()[:200] if title else None,
            "tech_headers": {h: headers[h] for h in TECH_HEADERS if h in headers},
            "technologies": sorted(tech),
            "security_headers_present": [h for h in SECURITY_HEADERS if h in headers],
            "security_headers_missing": [h for h in SECURITY_HEADERS if h not in headers],
            "cookies": cookies}


def security_txt(host):
    for path in ("/.well-known/security.txt", "/security.txt"):
        try:
            r = Http.get("https://{}{}".format(host, path), allow_redirects=True)
        except Exception:
            continue
        if r.status_code == 200 and "contact:" in r.text.lower():
            return {"url": r.url, "contact": re.findall(r"(?im)^contact:\s*(.+)$", r.text),
                    "policy": re.findall(r"(?im)^policy:\s*(.+)$", r.text)}
    return None


def sitemap(host):
    try:
        r = Http.get("https://{}/sitemap.xml".format(host), allow_redirects=True)
    except Exception:
        return None
    if r.status_code != 200 or "<loc>" not in r.text:
        return None
    locs = re.findall(r"<loc>\s*([^<]+?)\s*</loc>", r.text)
    return {"url": r.url, "entries": len(locs), "sample": locs[:20]}


# ---------- Wayback Machine ----------

def wayback(host):
    out = {}
    for label, params in (("first_snapshot", {"url": host, "timestamp": "19900101"}),
                          ("last_snapshot", {"url": host})):
        data = Http.get_json("https://archive.org/wayback/available", params=params)
        closest = ((data or {}).get("archived_snapshots") or {}).get("closest")
        if closest and closest.get("available"):
            out[label] = {"timestamp": closest.get("timestamp"), "url": closest.get("url")}
    return out


# ---------- Runner ----------

def run(target, report):
    host = normalize(target)
    results = {"target": host}
    lines = ["\nEXTENDED TECHNICAL RECON:"]

    if is_ip(host):
        _title("REVERSE DNS")
        try:
            results["reverse_dns"] = socket.gethostbyaddr(host)[0]
            _say("PTR", results["reverse_dns"])
        except (socket.herror, socket.gaierror, OSError):
            _warn("NO PTR RECORD")
    else:
        _title("DNS RECORDS")
        results["dns"] = dns_records(host)
        for rtype, values in results["dns"].items():
            for v in values:
                _say(rtype, v)
        if not results["dns"]:
            _warn("NO DNS DATA")

        _title("DOMAIN REGISTRATION (RDAP)")
        results["rdap"] = rdap(host)
        for k, v in results["rdap"].items():
            if v:
                _say(k.upper(), ", ".join(map(str, v)) if isinstance(v, list) else v)
        if not results["rdap"]:
            _warn("RDAP NOT AVAILABLE FOR THIS DOMAIN")

        _title("SUBDOMAINS FROM CERTIFICATE TRANSPARENCY (crt.sh)")
        subs = ct_subdomains(host)
        results["subdomains"] = subs
        if subs is None:
            _warn("crt.sh DID NOT RESPOND, TRY AGAIN LATER")
        else:
            _say("TOTAL", len(subs))
            for name in subs[:50]:
                _say("SUBDOMAIN", name)
            if len(subs) > 50:
                print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + "{} MORE IN THE REPORT".format(len(subs) - 50))

    _title("TLS CERTIFICATE")
    try:
        results["tls"] = tls_certificate(host)
        for k, v in results["tls"].items():
            _say(k.upper(), ", ".join(v[:15]) if isinstance(v, list) else v)
        if results["tls"]["days_left"] < 15:
            _warn("CERTIFICATE EXPIRES IN {} DAYS".format(results["tls"]["days_left"]))
    except Exception as e:
        results["tls"] = {"error": str(e)}
        _warn("TLS CHECK FAILED: {}".format(e))

    _title("HTTP PROFILE, SECURITY HEADERS AND TECHNOLOGIES")
    results["http"] = http_profile(host)
    http = results["http"]
    if http:
        _say("FINAL URL", http["final_url"])
        _say("STATUS", http["status"])
        _say("TITLE", http["title"])
        for h, v in http["tech_headers"].items():
            _say(h.upper(), v)
        _say("TECHNOLOGIES", ", ".join(http["technologies"]) or "NONE DETECTED")
        _say("SECURITY HEADERS PRESENT", ", ".join(http["security_headers_present"]) or "NONE")
        if http["security_headers_missing"]:
            _warn("SECURITY HEADERS MISSING: " + ", ".join(http["security_headers_missing"]))
        for c in http["cookies"]:
            flags = [f for f, ok in (("Secure", c["secure"]), ("HttpOnly", c["httponly"])) if not ok]
            if flags:
                _warn("COOKIE {} WITHOUT {}".format(c["name"], "/".join(flags)))
    else:
        _warn("WEBSITE DID NOT RESPOND OVER HTTP/HTTPS")

    _title("SECURITY.TXT AND SITEMAP")
    results["security_txt"] = security_txt(host)
    if results["security_txt"]:
        for c in results["security_txt"]["contact"]:
            _say("SECURITY CONTACT", c)
    else:
        _warn("NO SECURITY.TXT")
    results["sitemap"] = sitemap(host)
    if results["sitemap"]:
        _say("SITEMAP ENTRIES", results["sitemap"]["entries"])
    else:
        _warn("NO SITEMAP.XML")

    _title("WAYBACK MACHINE HISTORY")
    results["wayback"] = wayback(host)
    for k, v in results["wayback"].items():
        _say(k.upper().replace("_", " "), "{} {}".format(v["timestamp"], v["url"]))
    if not results["wayback"]:
        _warn("NO ARCHIVED SNAPSHOTS OR ARCHIVE.ORG UNAVAILABLE")

    for section, value in results.items():
        if section != "target" and value:
            lines.append("{}: {}".format(section.upper(), value))
    with open(report, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    Results.save(report, "recon", results)
    return results
