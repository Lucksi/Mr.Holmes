# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import json
import random
import string
from datetime import datetime, timezone
from Core.Support import Font
from Core.Support import Language
from Core.Support import Headers
from Core.Support import Http
from Core.Support import Results

filename = Language.Translation.Get_Language()
filename

UNIQUE = ["Chess","Books","Pokemon","Lol/League of Legends","Minecraft","Roblox","Modelling","Anime","Shopping","Writing","Stories","OSU","ThemeForest","Meme","Python","Ruby","Npm","Health","Map","File-Sharing","Colors","Crypto","Speedrun","Steam","BitCoin","Playstation","Gallery","Chess.com","Badge"]
NOT_FOUND_CODES = (404, 410, 204)
# Status codes that mean "blocked / rate limited / broken": never a valid positive
BLOCKED_CODES = (401, 403, 429, 451, 500, 502, 503, 504)

# site name -> True if the site reports a random non-existent account as found
_control_cache = {}


def _detect(error, site, response):
    """Return True (found), False (not found) or None (cannot tell)."""
    code = response.status_code
    if code in BLOCKED_CODES:
        return None
    if error == "Status-Code":
        if code == 200:
            return True
        if code in NOT_FOUND_CODES:
            return False
        return None
    if code in NOT_FOUND_CODES:
        return False
    if code >= 400:
        return None
    if error == "Message":
        return site["text"] not in response.text
    if error == "Response-Url":
        return response.url.rstrip("/") != site["response"].rstrip("/")
    return None


def _random_username():
    return "mh" + "".join(random.choice(string.ascii_lowercase) for _ in range(14))


def _control_positive(error, site, name, http_proxy, headers):
    """Probe the site with an account that cannot exist. If it still looks
    'found', the site's rule is unreliable and the positive is discarded."""
    if name not in _control_cache:
        url = site["user2"].replace("{}", _random_username())
        try:
            response = Http.get(url, proxies=http_proxy, headers=headers, allow_redirects=True)
            _control_cache[name] = _detect(error, site, response)
        except Exception:
            _control_cache[name] = None
    return _control_cache[name]


def _headers_for(name):
    return Headers.Get.Twitter() if name == "Twitter" else Headers.Get.classic()


class Search:

    @staticmethod
    def headers_for(name):
        return _headers_for(name)

    @staticmethod
    def _found(f, site1, username, subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main, Tag, Tags, MostTags):
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Default", "Found", "None").format(subject, username))
        print(Font.Color.YELLOW +
              "[v]" + Font.Color.WHITE + "LINK: {}".format(site1))
        if Writable == True:
            f.write(site1 + "\r\n")
            print(Font.Color.BLUE +
                  "[I]" + Font.Color.WHITE + "TAGS:[{}]".format(Font.Color.GREEN + ",".join(Tag) + Font.Color.WHITE))
            if subject != "PHONE-NUMBER":
                for tags in Tag:
                    if tags in UNIQUE:
                        MostTags.append(tags)
                    if tags in Tags:
                        if tags not in MostTags:
                            MostTags.append(tags)
                    else:
                        Tags.append(tags)
        else:
            f.write("{}:{}\r\n".format(name, main))
        successfull.append(site1)
        successfullName.append(name)
        if is_scrapable == "True":
            ScraperSites.append(name)

    @staticmethod
    def search(error, report, site1, site2, http_proxy, sites, data1, username, subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main, json_file, json_file2, Tag, Tags, MostTags, response=None):
        site = sites[data1]
        headers = _headers_for(name)
        if response is None or isinstance(response, Exception):
            response = Http.get(site2, proxies=http_proxy, headers=headers, allow_redirects=True)
        result = _detect(error, site, response)
        confidence = None
        if result:
            control = _control_positive(error, site, name, http_proxy, headers)
            if control:
                result = None
                confidence = "unreliable-site"
            else:
                confidence = "high" if control is False else "medium"

        with open(report, "a") as f:
            if result:
                Search._found(f, site1, username, subject, successfull, name, successfullName,
                              is_scrapable, ScraperSites, Writable, main, Tag, Tags, MostTags)
                if confidence == "medium":
                    print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + "CONFIDENCE: MEDIUM (control check unavailable)")
            elif result is False:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Default", "NotFound", "None").format(subject, username))
            elif confidence == "unreliable-site":
                print(Font.Color.YELLOW2 + "[?]" + Font.Color.WHITE +
                      "INCONCLUSIVE: {} ALSO REPORTS A RANDOM NON-EXISTENT ACCOUNT AS FOUND (FALSE POSITIVE DISCARDED)".format(name))
            else:
                print(Font.Color.BLUE + "[N]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None") + " HTTP {}".format(response.status_code))

        Results.append(report, "accounts", {
            "site": name,
            "url": site1,
            "checked_url": site2,
            "method": error,
            "http_status": response.status_code,
            "final_url": response.url,
            "result": {True: "found", False: "not-found", None: "inconclusive"}[result],
            "confidence": confidence,
            "tags": Tag,
            "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        })

        with open(json_file2, "w") as d:
            json.dump({"Names": [{"name": element} for element in successfullName]}, d, indent=4)
        with open(json_file, "w") as d:
            json.dump({"List": [{"site": element} for element in successfull]}, d, indent=4)
