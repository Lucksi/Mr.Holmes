# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import os
import urllib
import json
from datetime import datetime
from Core.Support.Phone import Numbers
from Core.Support import Font
from Core.Support import Creds
from Core.Support import Proxies
from Core.Support import Requests_Search
from Core.Support import Clear
from Core.Support import Dorks
from Core.Support import Logs
from Core.Support import Banner_Selector as banner
from Core.Support import Language
from time import sleep

filename = Language.Translation.Get_Language()
filename


class Phone_search:

    @staticmethod
    def Banner():
        Clear.Screen.Clear()
        Folder = "Banners/Phone"
        banner.Random.Get_Banner(Folder)

    @staticmethod
    def Google_dork(username):
        report = "GUI/Reports/Phone/Dorks/{}_dorks.txt".format(username)
        nomefile = "Site_lists/Phone/Google_dorks.txt"
        fingerprints = "Site_lists/Phone/Fingerprints.txt"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Dorks", "Remove", "None").format(username))
        else:
            pass
        Type = "GOOGLE"
        Dorks.Search.dork(username, report, nomefile, Type)
        f = open(report, "a")
        f.write(Language.Translation.Translate_Language(filename, "Report", "Phone", "FingerPrints"))
        f.close()
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Phone", "FingerPrints", "None"))
        sleep(3)
        f = open(fingerprints, "r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", username)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + site)
            f = open(report, "a")
            f.write(site + "\n")
            sleep(2)
        f.close()
        f.close()

    @staticmethod
    def Yandex_dork(username):
        report = "GUI/Reports/Phone/Dorks/{}_dorks.txt".format(username)
        nomefile = "Site_lists/Phone/Yandex_dorks.txt"
        fingerprints = "Site_lists/Phone/Yandex_Fingerprints.txt"
        Type = "YANDEX"
        Dorks.Search.dork(username, report, nomefile, Type)
        f = open(report, "a")
        f.write(Language.Translation.Translate_Language(filename, "Report", "Phone", "FingerPrints"))
        f.close()
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Phone", "FingerPrints", "None"))
        sleep(3)
        f = open(fingerprints, "r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", username)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + site)
            f = open(report, "a")
            f.write(site + "\n")
            sleep(2)
        f.close()
        f.close()

    @staticmethod
    def lookup(username, report):
        f = open(report, "a")
        f.write("\nPHONE NUMBER FOUND ON:\n")
        f.close()
        f = open("Temp/Phone/Code.txt", "r", newline=None)
        nation = f.read().rstrip("\n")
        f.close()
        if nation == "US":
            data = "Site_lists/Phone/Lookup/USA_phone.json"
            country = "UNITED-STATES"
            token = True
        elif nation == "IT":
            data = "Site_lists/Phone/Lookup/ITA_phone.json"
            country = "ITALY"
            token = True
        elif nation == "DE":
            data = "Site_lists/Phone/Lookup/DEU_phone.json"
            country = "GERMANY"
            token = True
        elif nation == "FR":
            data = "Site_lists/Phone/Lookup/FRA_phone.json"
            country = "FRANCE"
            token = True
        elif nation == "RO":
            data = "Site_lists/Phone/Lookup/ROU_phone.json"
            country = "ROMANIA"
            token = True
        elif nation == "CH":
            data = "Site_lists/Phone/Lookup/SWIS_phone.json"
            country = "SWITZERLAND"
            token = True
        else:
            token = True
            data = "Site_lists/Phone/Lookup/Undefined.json"
            country = "UNDEFINED"
        number = str(username)
        os.remove("Temp/Phone/Code.txt")
        subject = "PHONE-NUMBER"
        print(Font.Color.YELLOW + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Phone", "Country", "None").format(country))
        if token:
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Phone", "Search", "None").format(number))

            sc = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "choice", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if sc == 1:
                http_proxy = Proxies.proxy.final_proxis
                http_proxy2 = Proxies.proxy.choice3
                source = "http://ip-api.com/json/" + http_proxy2
                access = urllib.request.urlopen(source)
                content = access.read()
                final = json.loads(content)
                identity = Language.Translation.Translate_Language(filename, "Default", "ProxyLoc", "None").format(
                    final["regionName"], final["country"])
            else:
                http_proxy = None
                http_proxy2 = str(http_proxy)
                identity = "None"
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Proxy", "None").format(http_proxy2))
            if identity != "None":
                print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + identity)
            else:
                pass
            folder = "Phone"
            Logs.Log.Checker(username, folder)
            successfull = []
            successfullName = []
            ScraperSites = []
            Writable = True
            f = open(data,)
            data = json.loads(f.read())
            for sites in data:
                for data1 in sites:
                    name = sites[data1]["name"]
                    if name == "CarteTelefonae":
                        username = username.replace("40", "")
                    site1 = sites[data1]["url"].replace("{}", username)
                    site2 = sites[data1]["url2"].replace("{}", username)
                    main = sites[data1]["main"]
                    error = sites[data1]["Error"]
                    is_scrapable = sites[data1]["Scrapable"]
                    print(
                        Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Attempt", "None").format(name))
                    try:
                        Requests_Search.Search.search(error, report, site1, site2, http_proxy, sites, data1, username,
                                                      subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main)
                    except Exception as e:
                        print(
                            Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                        http_proxy = None
                        try:
                            Requests_Search.Search.search(error, report, site1, site2, http_proxy, sites, data1, username,
                                                          subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Site_Error", "None"))
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "TotFound", "None").format(subject, username))

            if len(successfull):
                for names in successfull:
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + names)
            else:
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                    filename, "Phone", "NotFound", "None"))

        else:
            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE +
                  "OPS LOOKS LIKE THERE IS NO LOOKUP FILE FOR NOW..SKIPPING")

        sleep(3)
        dork = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Dorks", "None") +
                   Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if dork == 1:
            Phone_search.Google_dork(username)
            Phone_search.Yandex_dork(username)
        else:
            pass

    @staticmethod
    def searcher(username):
        Phone_search.Banner()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        Date = "Date: " + str(dt_string)
        report = "GUI/Reports/Phone/" + username + ".txt"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        f = open(report, "w")
        f.write(Language.Translation.Translate_Language(filename, "Report", "Default", "Date").format(Date) + "\n")
        f.close()
        num = username
        code = 1
        Numbers.Phony.Number(num, report, code)
        Phone_search.lookup(username, report)
        print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
              os.getcwd() + "/" + report)
        f = open(report, "a")
        f.write(Language.Translation.Translate_Language(filename, "Report", "Default", "By"))
        f.close()
        Creds.Sender.mail(report, username)
