# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import urllib
import json
import requests
import shutil
from Core.Support import Font
from Core.Support import Creds
from Core.Support import FileTransfer
from Core.Support import Headers
from Core.Support.Phone import Numbers
from Core import E_Mail as Mail
from Core.Support import Proxies
from Core.Support import Requests_Search
from Core.Support import Clear
from Core.Support.Websites import Scanner
from Core.Support.Person import Scraper
from Core.Support import Dorks
from Core.Support import Logs
from Core.Support import Banner_Selector as banner
from Core.Support import Language
from Core.Support import DateFormat
from Core.Support import Map
from Core.Support import Notification
from Core.Support import Encoding
from Core.Support import ApiCheck as Api
from time import sleep
from datetime import datetime

filename = Language.Translation.Get_Language()
filename

Type = "Web"


class Web:

    @staticmethod
    def Profiles(username,report):
        choice = int(input(
            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "choice", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            http_proxy = Proxies.proxy.final_proxis
            http_proxy2 = Proxies.proxy.choice3
            source = "http://ip-api.com/json/" + http_proxy2
            access = urllib.request.urlopen(source)
            try:
                content = access.read()
                final = json.loads(content)
                identity = Language.Translation.Translate_Language(
                    filename, "Default", "ProxyLoc", "None").format(final["regionName"], final["country"])
            except Exception as e:
                print("SOMETHING WENT WRONG SORRY")
                http_proxy = None
                http_proxy2 = str(http_proxy)
                identity = "None"

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
        print(Font.Color.WHITE + "----------------------------------------------------------INSTAGRAM------------------------------------------------------------------\n" + Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "CHECKING FIRST 20 INSTAGRAM PROFILES THAT CONTAINS: {}".format(username))
        username_2 = username.split(".", 1)[0]
        try:
            Scraper.Search.Instagram(report, username, http_proxy, "None", "None", "None", "None", "None","Websites")
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "SOMETHING WENT WRONG" + str(e))
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "CHECKING FIRST 20 INSTAGRAM PROFILE FOR: {}".format(username_2))
        sleep(5)
        try:
            Scraper.Search.Instagram(report, username_2, http_proxy, "None", "None", "None", "None", username,"Websites")
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "SOMETHING WENT WRONG" + str(e))
        print(Font.Color.WHITE + "---------------------------------------------------------TWITTER---------------------------------------------------------------------\n" + Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "CHECKING FIRST 20 TWITTER PROFILES THAT CONTAINS: {}".format(username))
        try:
            Scraper.Search.Twitter(report, username, http_proxy, "None", "None","None","Websites")
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "SOMETHING WENT WRONG" + str(e))
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "CHECKING FIRST 20 TWITTER PROFILES FOR: {}".format(username_2))
        sleep(5)
        try:
            Scraper.Search.Twitter(report, username_2, http_proxy, "None", "None",username,"Websites")
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "SOMETHING WENT WRONG" + str(e))
        print(Font.Color.WHITE + "---------------------------------------------------------TIKTOK---------------------------------------------------------------------\n" + Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "CHECKING FIRST 20 TIKTOK PROFILES THAT CONTAINS: {}".format(username))
        try:
            Scraper.Search.TikTok(report, username, http_proxy, "None", "None","Websites")
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "SOMETHING WENT WRONG" + str(e))
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "CHECKING FIRST 20 TIKTOK PROFILES FOR: {}".format(username_2))
        sleep(5)
        try:
            Scraper.Search.TikTok(report, username_2, http_proxy, "None",username,"Websites")
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "SOMETHING WENT WRONG" + str(e))
        print(Font.Color.WHITE + "---------------------------------------------------------GIT-HUB---------------------------------------------------------------------\n" + Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "CHECKING FIRST 20 TWITTER PROFILES THAT CONTAINS: {}".format(username))
        try:
            Scraper.Search.Github(report, username, http_proxy, "None","None","Websites")
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "SOMETHING WENT WRONG" + str(e))
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "CHECKING FIRST 20 GIT-HUB PROFILES FOR: {}".format(username_2))
        sleep(5)
        try:
            Scraper.Search.Github(report, username_2, http_proxy, "None",username,"Websites")
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "SOMETHING WENT WRONG" + str(e))
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Robots") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            Web.Robots(username, report)
        else:
            choice = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Ports") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                Web.Ports(username, report)
            else:
                choice = int(input(
                    Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Traceroute") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                Web.trace(username, report)

    @staticmethod
    def Ports(username, report):
        f = open(report, "a")
        f.write(Language.Translation.Translate_Language(
            filename, "Report", "Website", "Ports"))
        f.close()
        Scanner.Port.Scan(username, report)
        choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Traceroute") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            Web.trace(username, report)

    @staticmethod
    def Banner(Mode):
        Clear.Screen.Clear()
        Folder = "Banners/Websites"
        banner.Random.Get_Banner(Folder, Mode)

    @staticmethod
    def Reputation(username, report):
        subject = "DOMAIN/WEBSITE/IP"
        data = "Site_lists/Websites/Lookup.json"
        f = open(report, "a")
        f.write(Language.Translation.Translate_Language(
            filename, "Report", "Website", "Malicious"))
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Website", "Default", "Research").format(username))
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
              Language.Translation.Translate_Language(filename, "Default", "Proxy", "None") .format(http_proxy2))
        if identity != "None":
            print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + identity)
        else:
            pass
        folder = "Websites"
        Logs.Log.Checker(username, folder)
        successfull = []
        successfullName = []
        ScraperSites = []
        Writable = False
        json_file = "GUI/Reports/Websites/{}/{}.json".format(
            username, username)
        json_file2 = "GUI/Reports/Websites/{}/{}.json".format(
            username, "Name")
        f = open(data,)
        data = json.loads(f.read())
        for sites in data:
            for data1 in sites:
                name = sites[data1]["name"]
                site1 = sites[data1]["url"].replace("{}", username)
                site2 = sites[data1]["url2"].replace("{}", username)
                error = sites[data1]["Error"]
                main = sites[data1]["main"]
                is_scrapable = sites[data1]["Scrapable"]
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + "TRYING ON: {} ".format(name))
                try:
                    Requests_Search.Search.search(error, report, site1, site2, http_proxy, sites, data1, username,
                                                  subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main, json_file, json_file2)
                except Exception as e:
                    print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                    http_proxy = None
                    try:
                        Requests_Search.Search.search(error, report, site1, site2, http_proxy, sites, data1, username,
                                                      subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main, json_file, json_file2)
                    except Exception as e:
                        print(
                            Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Site_Error", "None"))

            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "TotFound", "None").format(subject, username))

            if len(successfull):
                for names in successfull:
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + names)
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Website", "Default", "Unsecure").format(username))
            else:
                print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Website", "Default", "Secure").format(username))
                f = open(report, "a")
                f.write(Language.Translation.Translate_Language(
                    filename, "Report", "Website", "Safe"))
                f.close()
            consultFile = "Site_lists/Websites/Consult.json"
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Website", "Default", "Info"))
            f = open(consultFile,)
            data = json.loads(f.read())
            for sites in data:
                for data1 in sites:
                    site1 = sites[data1]["url"].replace("{}", username)
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + site1)
            f = open(report, "a")
            f.write(Language.Translation.Translate_Language(
                filename, "Report", "Website", "Info"))
            for sites in data:
                for data1 in sites:
                    site1 = sites[data1]["url"].replace("{}", username)
                    f.write(site1+"\n")
            f.close()
            choice = int(input(
                    Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Soc") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                    Web.Profiles(username, report)
            else:
                choice = int(input(
                    Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Robots") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if choice == 1:
                    Web.Robots(username, report)
                else:
                    choice = int(input(
                        Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Ports") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if choice == 1:
                        Web.Ports(username, report)
                    else:
                        choice = int(input(
                            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Traceroute") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                        if choice == 1:
                            Web.trace(username, report)

    @staticmethod
    def Robots(username, report):
        headers = Headers.Get.classic()
        name = "Site_lists/Websites/Robots.json"
        f = open(name,)
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "DOWNLOADING {} Robots.txt".format(username))
        choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "choice", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            http_proxy = Proxies.proxy.final_proxis
            http_proxy2 = Proxies.proxy.choice3
            source = "http://ip-api.com/json/" + http_proxy2
            access = urllib.request.urlopen(source)
            content = access.read()
            final = json.loads(content)
            identity = Language.Translation.Translate_Language(
                filename, "Default", "ProxyLoc", "None").format(final["regionName"], final["country"])
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
        robot = "GUI/Reports/Websites/Robots/" + username + "_robots.txt"
        final = json.loads(f.read())
        for sites in final:
            try:
                url = sites["Robots"]["url"].replace("{}", username)
                dork = requests.get(
                    url, headers=headers, proxies=http_proxy, timeout=None, allow_redirects=True)
                if dork.status_code == 200:
                    open(robot, 'wb').write(dork.content)
                    print(Font.Color.YELLOW +
                          "[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Default", "Robots").format(robot))
                    print(dork.text)
                else:
                    print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(filename, "Website", "Default", "NoRobots").format(username))
            except Exception as e:
                try:
                    print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                    url = sites["Robots"]["url"].replace("{}", username)
                    dork = requests.get(
                        url, headers=headers, proxies=None, timeout=None, allow_redirects=True)
                    if dork.status_code == 200:
                        open(robot, 'wb').write(dork.content)
                        print(Font.Color.YELLOW +
                              "[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Default", "Robots").format(robot))
                        print(dork.text)
                    else:
                        print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                              Language.Translation.Translate_Language(filename, "Website", "Default", "NoRobots").format(username))
                except Exception as e:
                    print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(filename, "Website", "Default", "NoRobots").format(username))

        choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Ports") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            Web.Ports(username, report)
        else:
            choice = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Traceroute") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                Web.trace(username, report)
            else:
                pass

    @staticmethod
    def trace(username, report):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Website", "Default", "Traceroute").format(username))
        if os.name == "nt":
            command = ("tracert " + username)
        else:
            command = ("traceroute " + username)
        proces = os.popen(command)
        results = str(proces.read())
        print(results)
        f = open(report, "a")
        f.write("\n\nTRACEROUTE SEQUENCE:" + "\r\n")
        f.write(results)
        f.close()

    @staticmethod
    def google_dork(username, number, num, email, email2):
        report = "GUI/Reports/Websites/Dorks/{}_dorks.txt".format(username)
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Dorks", "Remove", "None").format(username))
        else:
            pass
        nomefile = "Site_lists/Websites/Google_dorks.txt"
        Type = "GOOGLE"
        Dorks.Search.dork(username, report, nomefile, Type)
        Web.yandex_dork(username, report)
        if number == True:
            f = open(report, "a")
            f.write("\nGENERATING LINK FOR {} PHONE NUMBER {}...\n".format(
                username, num))
            f.close()
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Website", "Default", "Phone").format(username, num))
            phonen = "Site_lists/Websites/ExtraDorks.txt"
            f = open(phonen, "r")
            for sites in f:
                site = sites.rstrip("\n")
                site = site.replace("{}", num)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + site)
                f = open(report, "a")
                f.write(site + "\n")
                f.close()
                sleep(2)
            f.close()
        if email == True:
            f = open(report, "a")
            f.write("\nGENERATING LINK FOR {} EMAIL {}...\n".format(
                username, email2))
            f.close()
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Website", "Default", "Email").format(username, email2))
            f = open(phonen, "r")
            for sites in f:
                site = sites.rstrip("\n")
                site = site.replace("{}", email2)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + site)
                f = open(report, "a")
                f.write(site + "\n")
                f.close()
                sleep(2)
            f.close()
        else:
            pass
        report = "GUI/Reports/Websites/{}/{}.txt".format(username, username)
        choice = int(input(
            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Repu") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            Web.Reputation(username, report)
        else:
            choice = int(input(
                    Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Soc") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                    Web.Profiles(username, report)
            else:
                choice = int(input(
                    Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Robots") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if choice == 1:
                    Web.Robots(username, report)
                else:
                    choice = int(input(
                        Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Ports") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if choice == 1:
                        Web.Ports(username, report)
                    else:
                        choice = int(input(
                            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Traceroute") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                        if choice == 1:
                            Web.trace(username, report)

    @staticmethod
    def yandex_dork(username, report):
        nomefile = "Site_lists/Websites/Yandex_dorks.txt"
        Type = "YANDEX"
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def whois_lookup(username, report, Mode):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Website", "Default", "Whois").format(username))
        sleep(2)
        Key = Api.Check.WhoIs()
        Key
        if Key == "None":
            if (os.name != "nt"):
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Website", "Parameters", "KeyNoFound"))
                command = ("whois " + username)
                proces = os.popen(command)
                results = str(proces.read())
                final = results + command
                print(Font.Color.WHITE + results)
                f = open(report, "a")
                f.write("\nWEBSITE DATA:" + "\r\n")
                f.write(results)
                f.close()
                num = None
                number = False
                em = None
                email2 = None
                email = False
            else:
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Website", "Default", "NoWhois"))
                num = None
                number = False
                email = None
                email2 = None
        else:
            try:
                print(Font.Color.GREEN + "[+]" +
                      Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Parameters", "KeyFound"))
                Key2 = str(Key)
                source = "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={}&domainName={}&outputFormat=JSON".format(
                    Key2, username)
                access = urllib.request.urlopen(source)
                reader = access.read()
                final = json.loads(reader)
                created = "CREATION-DATE: " + \
                    final["WhoisRecord"]["createdDate"]
                modified = "UPDATE-DATE: " + \
                    final["WhoisRecord"]["updatedDate"]
                expired = "EXPIRED-DATE: " + \
                    final["WhoisRecord"]["expiresDate"]
                domain = "DOMAIN: " + \
                    final["WhoisRecord"]["registrant"]["name"]
                organization = "ORGANIZATION: " + \
                    final["WhoisRecord"]["registrant"]["organization"]
                nation = "NATION: " + \
                    final["WhoisRecord"]["registrant"]["country"]
                nationCode = "NATION-CODE: " + \
                    final["WhoisRecord"]["registrant"]["countryCode"]
                if "state"  in final["WhoisRecord"]["registrant"]:
                    state = "STATE: " + final["WhoisRecord"]["registrant"]["state"]
                else:
                    state = "STATE: NONE"
                if "city" in final["WhoisRecord"]["registrant"]:
                    city = "CITY: " + final["WhoisRecord"]["registrant"]["city"]
                    city2 = str(final["WhoisRecord"]["registrant"]["city"])
                else:
                    city = "CITY: NONE"
                if "street1" in  final["WhoisRecord"]["registrant"]:
                    street = "STREET: " + \
                        final["WhoisRecord"]["registrant"]["street1"].replace("\n"," ")
                    if ".com" in street:
                        street2 = str(final["WhoisRecord"]["registrant"]["street1"].replace("\n"," ").split(".com",1)[1])
                    else:
                        street2 = str(final["WhoisRecord"]["registrant"]["street1"].replace("\n"," "))
                else:
                    street = "STREET: NONE"
                if "email" in final["WhoisRecord"]["registrant"]:
                    email = "EMAIL: " + final["WhoisRecord"]["registrant"]["email"]
                    email2 = final["WhoisRecord"]["registrant"]["email"]
                else:
                    email = "EMAIL: NONE"
                    email2 = ""
                if "telephone" in final["WhoisRecord"]["registrant"]:
                    telephone = "TELEPHONE: " + \
                        final["WhoisRecord"]["registrant"]["telephone"]
                    telephone2 = final["WhoisRecord"]["registrant"]["telephone"]
                else:
                    telephone = "TELEPHONE: NONE"
                    telephone2 = ""
                if "street1" in final["WhoisRecord"]["registrant"] and "city" in final["WhoisRecord"]["registrant"]:                
                    link = "https://www.google.com/maps/place/{} {}".format(
                    street2, city2)
                else:
                    link = "None"
                sleep(2)
                print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE + created)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + modified)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + expired)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + domain)
                print(Font.Color.YELLOW + "[v]" +
                      Font.Color.WHITE + organization)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + nation)
                print(Font.Color.YELLOW + "[v]" +
                      Font.Color.WHITE + nationCode)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + state)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + city)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + street)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + email)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + telephone)
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Default", "Maps"))
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + link)
                f = open(report, "a")
                f.write("\nWEBSITE DATA:" + "\r\n")
                f.write(created + "\r\n")
                f.write(modified + "\r\n")
                f.write(expired + "\r\n")
                f.write(domain + "\r\n")
                f.write(organization + "\r\n")
                f.write(nation + "\r\n")
                f.write(nationCode + "\r\n")
                f.write(state + "\r\n")
                f.write(city + "\r\n")
                f.write(street + "\r\n")
                f.write(email + "\r\n")
                f.write(telephone + "\r\n")
                f.close()
                try:
                    link_json = "https://nominatim.openstreetmap.org/search?q={}+{}&format=json".format(
                        street2, city2).replace(" ", "%20")
                    get_Coords = urllib.request.urlopen(link_json)
                    Reader = get_Coords.read()
                    parser = json.loads(Reader)
                    for value in parser:
                        Lat = value["lat"]
                        Lon = value["lon"]
                    report_Coordinates = "GUI/Reports/Websites/Coordinates/Street_Geolocation/" + \
                        username + ".json"
                    data = {
                        "Geolocation": {
                            "Latitude": Lat,
                            "Longitude": Lon
                        }
                    }
                    print(
                        Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Default", "Geo"))
                    sleep(2)
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                          "LATITUDE:" + Font.Color.GREEN + " {}".format(Lat))
                    sleep(2)
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                          "LONGITUDE:" + Font.Color.GREEN + " {}".format(Lon))
                    with open(report_Coordinates, "w", encoding="utf-8") as output:
                        json.dump(data, output, ensure_ascii=False, indent=4)
                    Map.Creation.mapWeb(report_Coordinates, Lat, Lon, username)
                except Exception as e:
                    f = str(e)
                    print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(filename, "Website", "Default", "NoGeo") + f)
                num = telephone2
                if num != "":
                    number = True
                    sc = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Parameters", "PhoneFound").format(
                        num) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if sc == 1:
                        folder = "GUI/Reports/Websites/{}/{}".format(
                            username, num)
                        if os.path.exists(folder):
                            shutil.rmtree(folder)
                        os.mkdir(folder)
                        report2 = folder + "/{}.txt".format(num)
                        f = open(report2, "w")
                        f.write("\nPHONE NUMBER DATA:\n")
                        f.close()
                        code = 0
                        try:
                            Numbers.Phony.Number(
                                num, report2, code, Mode, Type, username)
                        except Exception as e:
                            print("SOMETHING WENT WRONG")
                    else:
                        pass
                else:
                    print(Font.Color.RED +
                          "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Parameters", "PhoneNotFound"))
                    number = False
                if email2 != "":
                    email = True
                    sc = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Parameters", "EmailFound").format(
                        email2) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if sc == 1:
                        folder = folder = "GUI/Reports/Websites/{}/{}".format(
                                username, email2)
                        os.mkdir(folder)
                        report2 = folder + "/{}.txt".format(email2)
                        try:
                            Mail.Mail_search.Lookup(email2,report2)
                        except Exception as e:
                                print("SOMETHING WENT WRONG")
                    else:
                        pass
                else:
                    print(Font.Color.RED +
                          "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Parameters", "EmailNotFound"))
                    email = False
            except Exception as e:
                print(str(e))
                num = None
                number = False
                email = False
                email2 = None
                print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Website", "Parameters", "Error"))
                command = ("whois " + username)
                proces = os.popen(command)
                results = str(proces.read())
                final = results + command
                print(Font.Color.WHITE + results)
                f = open(report, "a")
                f.write("\nWEBSITE DATA:" + "\r\n")
                f.write(results)
                f.close()
            print(Font.Color.GREEN +
                  "\n[+]" + Font.Color.WHITE + "GETTING REPUTATION RATING...")
            try:
                source = "https://domain-reputation.whoisxmlapi.com/api/v2?apiKey={}&domainName={}".format(
                    Key2, username)
                access = urllib.request.urlopen(source)
                reader = access.read()
                final = json.loads(reader)
                repu = final["reputationScore"]
                tests = final["testResults"]
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "REPUTATION RATING: {}".format(repu))
                f = open(report, "a")
                f.write("\n\nREPUTATION RATING: {}\r\n".format(repu))
                for test1 in tests:
                    print(Font.Color.GREEN +
                          "\n[+]" + Font.Color.WHITE + "TEST-NAME: {}".format(test1["test"]))
                    print(Font.Color.YELLOW +
                          "[v]" + Font.Color.WHITE + "TEST-CODE: {}".format(test1["testCode"]))
                    print(Font.Color.GREEN +
                          "[+]" + Font.Color.WHITE + "WARNING LISTS FOR TEST: {}".format(test1["test"]))
                    f.write("TEST-NAME: {}".format(test1["test"]) + "\r\n")
                    f.write("TEST-CODE: {}".format(test1["testCode"]) + "\r\n")
                    f.write("TEST-NAME: {}".format(test1["test"]) + "\r\n")
                    f.write("WARNING LISTS FOR TEST: {}".format(
                        test1["test"]) + "\r\n")
                    for warning1 in test1["warnings"]:
                        print(Font.Color.YELLOW +
                              "[v]" + Font.Color.WHITE + "DESCRIPTION: {}".format(warning1["warningDescription"]))
                        print(Font.Color.YELLOW +
                              "[v]" + Font.Color.WHITE + "CODE: {}".format(warning1["warningCode"]))
                        f.write("DESCRIPTION: {}".format(
                            warning1["warningDescription"]) + "\r\n")
                        f.write("CODE: {}".format(
                            warning1["warningCode"]) + "\r\n")
                    f.close()
            except Exception as e:
                pass
        choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Dorks", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            Web.google_dork(username, number, num,email,email2)
        else:
            choice = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Repu") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                Web.Reputation(username, report)
            else:
                choice = int(input(
                    Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Soc") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if choice == 1:
                    Web.Profiles(username, report)
                else:
                    choice = int(input(
                        Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Robots") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if choice == 1:
                        Web.Robots(username, report)
                    else:
                        choice = int(input(
                            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Ports") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                        if choice == 1:
                            Web.Ports(username, report)
                        else:
                            choice = int(input(
                                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Traceroute") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                            if choice == 1:
                                Web.trace(username, report)

    @staticmethod
    def search(username, Mode):
        os.system("cls" if os.name == "nt" else "clear")
        Web.Banner(Mode)
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "INFO:" + "[{}]".format(Font.Color.GREEN + Language.Translation.Translate_Language(filename,"Website","Default","Explanation") + Font.Color.WHITE) )
        folder = "GUI/Reports/Websites/" + username + "/"
        if os.path.isdir(folder):
            shutil.rmtree(folder)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        os.mkdir(folder)
        report = "GUI/Reports/Websites/{}/{}.txt".format(username, username)
        report_Ip = "GUI/Reports/Websites/Coordinates/Ip_Geolocation/" + username + ".json"
        now = datetime.now()
        dataformat = DateFormat.Get.Format()
        dt_string = now.strftime(dataformat)
        Date = "Date: " + str(dt_string)
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Website", "Default", "Search").format(username))
        sleep(3)
        source = "http://ip-api.com/json/" + username
        access = urllib.request.urlopen(source)
        content = access.read()
        final = json.loads(content)
        status = final["status"]
        if status != "fail":
            ip = "IP: " + final["query"]
            country = "NATION: " + final["country"]
            country_code = "NATION-CODE: " + final["countryCode"]
            region = "REGION-CODE: " + final["region"]
            regionName = "REGION-NAME: " + final["regionName"]
            city = "CITY: " + final["city"]
            timezone = "TIMEZONE: " + final["timezone"]
            isp = "ISP: " + final["isp"]
            org = "ORG: " + final["org"]
            asp = "AS: " + final["as"]
            lat2 = str(final["lat"])
            final_lat = "LAT: {}".format(lat2)
            lon2 = str(final["lon"])
            final_lon = "LONG: {}".format(lon2)
            zip_data = "ZIP/POSTAL-CODE: " + final["zip"]
            link = "https://www.google.com/maps/place/{},{}".format(lat2, lon2)
            print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE + ip)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + country)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + country_code)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + region)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + regionName)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + city)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + timezone)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + isp)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + org)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + asp)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + final_lat)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + final_lon)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + zip_data)
            print(Font.Color.GREEN +
                  "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Default", "Maps"))
            sleep(2)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + link)
            f = open(report, "a")
            f.write(Language.Translation.Translate_Language(
                filename, "Report", "Default", "Date").format(Date) + "\r\n")
            f.write(ip + "\r\n")
            f.write(country + "\r\n")
            f.write(country_code + "\r\n")
            f.write(region + "\r\n")
            f.write(regionName + "\r\n")
            f.write(city + "\r\n")
            f.write(timezone + "\r\n")
            f.write(isp + "\r\n")
            f.write(org + "\r\n")
            f.write(asp + "\r\n")
            f.write(final_lat + "\r\n")
            f.write(final_lon + "\r\n")
            f.write(zip_data + "\r\n")
            f.close()
            data = {
                "Geolocation": {
                    "Latitude": lat2.replace(" ", "%20"),
                    "Longitude": lon2.replace(" ", "%20")
                }
            }

            with open(report_Ip, "w", encoding='utf-8') as outupt:
                json.dump(data, outupt, ensure_ascii=False, indent=4)
            Map.Creation.mapWeb(report_Ip, lat2, lon2, username)
        else:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Website", "Default", "NoResponse"))
        choice = int(input(
            Font.Color.BLUE + " \n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Whois") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            Web.whois_lookup(username, report, Mode)
        else:
            num = None
            number = False
            email = False
            email2 = False
            choice = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Dorks", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                Web.google_dork(username, number, num,email,email2)
            else:
                choice = int(input(
                    Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Repu") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if choice == 1:
                    Web.Reputation(username, report)
                else:
                    choice = int(input(
                        Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Soc") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if choice == 1:
                        Web.Profiles(username, report)
                    else:
                        choice = int(input(
                            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Robots") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                        if choice == 1:
                            Web.Robots(username, report)
                        else:
                            choice = int(input(
                                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Ports") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                            if choice == 1:
                                Web.Ports(username, report)
                            else:
                                choice = int(input(
                                    Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Questions", "Traceroute") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                                if choice == 1:
                                    Web.trace(username, report)

        f = open(report, "a")
        f.write(Language.Translation.Translate_Language(
            filename, "Report", "Default", "By"))
        f.close()
        print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
              report)
        Notification.Notifier.Start(Mode)
        Creds.Sender.mail(report, username)
        choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Transfer", "Question", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            FileTransfer.Transfer.File(report, username, ".txt")
        Encoding.Encoder.Encode(report)
        inp = input(Language.Translation.Translate_Language(
            filename, "Default", "Continue", "None"))
