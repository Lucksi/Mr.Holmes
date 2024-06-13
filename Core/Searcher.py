# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import urllib
import json
from Core.Support import Font
from Core.Support import Creds
from Core.Support import FileTransfer
from Core.Support import Proxies
from Core.Support import Requests_Search
from Core.Support.Username import Scraper
from Core.Support import Clear
from Core.Support import Dorks
from Core.Support import Logs
from Core.Support import Banner_Selector as banner
from Core.Support import Language
from Core.Support import Notification
from Core.Support import Recap
from Core.Support import DateFormat
from datetime import datetime
from Core.Support import Encoding
from Core.Support import Site_Counter as CO
from time import sleep

filename = Language.Translation.Get_Language()
filename

class MrHolmes:

    @staticmethod
    def Scraping(report, username, http_proxy,InstagramParams,PostLocations, PostGpsCoordinates,TwitterParams):
        os.chdir("GUI/Reports/Usernames/{}".format(username))
        if os.path.isdir("Profile_pics"):
            pass
        else:
            os.mkdir("Profile_pics")
        os.chdir("../../../../")
        #http_proxy = None
        try:
            Scraper.info.Instagram(report, username, http_proxy, InstagramParams,
                                 PostLocations, PostGpsCoordinates, "Usernames", username)
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "Something went wrong")
        try:
            Scraper.info.Twitter(report, username, http_proxy, TwitterParams,
                               "Usernames", username)
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "Something went wrong")
        try:
            Scraper.info.TikTok(report, username, http_proxy, "Usernames", username)
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "Something went wrong")
        
        try:
            Scraper.info.Github(
            report, username, http_proxy, "Usernames", username)
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "Something went wrong")

        try:
            Scraper.info.GitLab(
            report, username, http_proxy, "Usernames", username)
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "Something went wrong")
        
        try:
            Scraper.info.Ngl(
            report, username, http_proxy, "Usernames", username)
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "Something went wrong")
        try:
            Scraper.info.Tellonym(
                report, username, http_proxy, "Usernames", username)
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "Something went wrong")
        
        try:
            Scraper.info.Gravatar(
                report, username, http_proxy, "Usernames", username)
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "Something went wrong")

        try:
            Scraper.info.Joinroll(
            report, username, http_proxy, "Usernames", username)
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "Something went wrong")
        
        try:
            Scraper.info.Chess(
                report, username, http_proxy, "Usernames", username)
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "Something went wrong")
        
    
    @staticmethod
    def Controll(username, nomefile, identity, report, subject, successfull, ScraperSites, Writable, http_proxy2, successfullName, http_proxy, choice, Tags, MostTags):
        f = open(nomefile,)
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Default", "Proxy", "None").format(http_proxy2))
        if identity != "None":
            print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + identity)
        else:
            pass
        json_file = "GUI/Reports/Usernames/{}/{}.json".format(
            username, username)
        json_file2 = "GUI/Reports/Usernames/{}/{}.json".format(
            username, "Name")
        data = json.loads(f.read())
        for sites in data:
            for data1 in sites:
                site1 = sites[data1]["user"].replace("{}", username)
                site2 = sites[data1]["user2"].replace("{}", username)
                name = sites[data1]["name"]
                main = sites[data1]["main"]
                error = sites[data1]["Error"]
                exception_char = sites[data1]["exception"]
                is_scrapable = sites[data1]["Scrapable"]
                Tag = sites[data1]["Tag"]
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Attempt", "None") .format(name))
                for errors in exception_char:
                    if errors in username:
                        alert = "NOT-CORRECT"
                        break
                    else:
                        alert = "CORRECT"
                if alert == "NOT-CORRECT":
                    print(
                        Font.Color.YELLOW2 + "[U]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Not_Valid"))
                else:
                    try:
                        Requests_Search.Search.search(error, report, site1, site2, http_proxy, sites, data1, username,
                                                      subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main, json_file, json_file2, Tag, Tags, MostTags)
                    except Exception as e:
                        print(
                            Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                        http_proxy = None
                        try:
                            Requests_Search.Search.search(error, report, site1, site2, http_proxy, sites, data1, username,
                                                          subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main, json_file, json_file2, Tag, Tags, MostTags)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Site_Error", "None"))
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

    @staticmethod
    def Banner(Mode):
        Clear.Screen.Clear()
        Folder = "Banners/Username"
        banner.Random.Get_Banner(Folder, Mode)

    @staticmethod
    def Google_dork(username):
        report = "GUI/Reports/Usernames/Dorks/{}_Dorks.txt".format(username)
        nomefile = "Site_lists/Username/Google_dorks.txt"
        Type = "GOOGLE"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Dorks", "Remove", "None").format(username))
        else:
            pass
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def Yandex_dork(username):
        report = "GUI/Reports/Usernames/Dorks/{}_Dorks.txt".format(username)
        nomefile = "Site_lists/Username/Yandex_dorks.txt"
        Type = "YANDEX"
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def search(username, Mode):
        successfull = []
        successfullName = []
        ScraperSites = []
        Tags = []
        MostTags = []
        Writable = True
        MrHolmes.Banner(Mode)
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "INFO:" + "[{}]".format(Font.Color.GREEN + Language.Translation.Translate_Language(filename,"Username","Default","Explanation") + Font.Color.WHITE) )
        subject = "USERNAME"
        found = 0
        Percent = 0
        nomefile = "Site_lists/Username/site_list.json"
        folder = "GUI/Reports/Usernames/" + username + "/"
        report = folder + username + ".txt"
        report2 = folder + username + ".mh"
        Recap1 = folder + "Recap.txt"
        Recap2 = folder + "Recap.mh"
        InstagramParams = []
        TwitterParams = []
        PostLocations = []
        PostGpsCoordinates = []
        if os.path.exists(report):
            os.remove(report)
            if os.path.exists(folder + "Name.json"):
                os.remove(folder + "Name.json")
            if os.path.exists(report.replace(".txt", ".json")):    
                os.remove(report.replace(".txt", ".json"))
            if os.path.exists(Recap1):
                os.remove(Recap1)
            elif os.path.exists(Recap2):
                os.remove(Recap2)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        elif os.path.exists(report2):
            os.remove(report2)
            if os.path.exists(folder + "Name.json"):
                os.remove(folder + "Name.json")
            if os.path.exists(report.replace(".mh", ".json")):
                os.remove(report2.replace(".mh", ".json"))
            if os.path.exists(Recap1):
                os.remove(Recap1)
            elif os.path.exists(Recap2):
                os.remove(Recap2)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        else:
            os.mkdir(folder)
        now = datetime.now()
        dataformat = DateFormat.Get.Format()
        dt_string = now.strftime(dataformat)
        Date = "Date: " + str(dt_string)
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
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        folder = "Username"
        Logs.Log.Checker(username, folder)
        f = open(report, "a")
        f.write(Language.Translation.Translate_Language(
            filename, "Report", "Default", "Date").format(Date) + "\r\n")
        f.write(Language.Translation.Translate_Language(
            filename, "Report", "Username", "Found"))
        f.close()
        opt = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.GREEN + "[INSERT AN OPTION]:" +  Font.Color.WHITE + "\n(1)USERNAME-RESEARCH (SEARCH USERNAME ON DIFFERENT WEBSITES)\n(2)PROFILE-SCRAPING (SCRAPE USERNAME PROFILE DIRECTLY)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if opt == 1:
            i1 = CO.Counter.Site(nomefile)
            MrHolmes.Controll(username, nomefile, identity, report, subject,
                            successfull, ScraperSites, Writable, http_proxy2, successfullName, http_proxy, choice, Tags, MostTags)
            Nsfw = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Nsfw") +
                    Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if Nsfw == 1:
                nomefile = "Site_lists/Username/NSFW_site_list.json"
                i2 = CO.Counter.Site(nomefile)
                MrHolmes.Controll(username, nomefile, identity, report, subject,
                                successfull, ScraperSites, Writable, http_proxy2, successfullName, http_proxy, choice, Tags, MostTags)
                Count = i1 + i2
            else:
                Count = i1
                pass
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                Language.Translation.Translate_Language(filename, "Default", "TotFound", "None").format(subject, username))
            sleep(3)
            if len(successfull):
                for names in successfull:
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + names)
                    found = found + 1
                if len(ScraperSites):
                    os.chdir("GUI/Reports/Usernames/{}".format(username))
                    if os.path.isdir("Profile_pics"):
                        pass
                    else:
                        os.mkdir("Profile_pics")
                    os.chdir("../../../../")
                    choice = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Scraper") +
                                Font.Color.GREEN + "[*MR.HOLMES*]" + Font.Color.WHITE + "-->"))
                    if choice == 1:
                        ScrapeOp = "Positive"
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
                            print(Font.Color.GREEN +
                                "[+]" + Font.Color.WHITE + identity)
                        else:
                            pass

                        if "Instagram" in ScraperSites:
                            try:
                                Scraper.info.Instagram(
                                    report, username, http_proxy, InstagramParams, PostLocations, PostGpsCoordinates, "Usernames", username)
                            except ConnectionError:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Instagram(
                                    report, username, http_proxy, InstagramParams, PostLocations, PostGpsCoordinates, "Usernames", username)
                            except Exception as e:
                                pass
                        else:
                            pass

                        if "TikTok" in ScraperSites:
                            try:
                                Scraper.info.TikTok(
                                    report, username, http_proxy, "Usernames", username)
                            except ConnectionError:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.TikTok(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                pass
                        else:
                            pass

                        if "Disqus" in ScraperSites:
                            try:
                                Scraper.info.Disqus(
                                    report, username, http_proxy, "Usernames", username)
                            except ConnectionError:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Disqus(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                pass
                        else:
                            pass

                        if "Imgur" in ScraperSites:
                            try:
                                Scraper.info.Imgur(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Imgur(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass

                        if "Pr0gramm" in ScraperSites:
                            try:
                                Scraper.info.Pr0gramm(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Pr0gramm(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass

                        if "BinarySearch" in ScraperSites:
                            try:
                                Scraper.info.Binarysearch(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Binarysearch(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass

                        if "MixCloud" in ScraperSites:
                            try:
                                Scraper.info.MixCloud(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.MixCloud(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass

                        if "Twitter" in ScraperSites:
                            try:
                                Scraper.info.Twitter(
                                    report, username, http_proxy, TwitterParams, "Usernames", username)
                            except ConnectionError:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Twitter(
                                    report, username, http_proxy, TwitterParams, "Usernames", username)
                            except Exception as e:
                                print(str(e))
                                pass
                        else:
                            pass

                        if "DockerHub" in ScraperSites:
                            try:
                                Scraper.info.Dockerhub(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Dockerhub(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass

                        if "Kik" in ScraperSites:
                            try:
                                Scraper.info.Kik(report, username,
                                                http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Kik(report, username,
                                                http_proxy, "Usernames", username)
                        else:
                            pass

                        if "GitLab" in ScraperSites:
                            try:
                                Scraper.info.GitLab(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.GitLab(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass

                        if "Wattpad" in ScraperSites:
                            try:
                                Scraper.info.Wattpad(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Wattpad(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass

                        if "GitHub" in ScraperSites:
                            try:
                                Scraper.info.Github(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Github(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass

                        if "Gravatar" in ScraperSites:
                            try:
                                Scraper.info.Gravatar(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Gravatar(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass

                        if "Chess.com" in ScraperSites:
                            try:
                                Scraper.info.Chess(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Chess(
                                    report, username, http_proxy, "Usernames", username)

                        if "Minecraft" in ScraperSites:
                            try:
                                Scraper.info.Minecraft(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Minecraft(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass
                        
                        if "JoinRoll" in ScraperSites:
                            try:
                                Scraper.info.Joinroll(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Joinroll(
                                    report, username, http_proxy, "Usernames", username)

                        if "Ngl.link" in ScraperSites:
                            try:
                                Scraper.info.Ngl(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Ngl(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass

                        if "Tellonym" in ScraperSites:
                            try:
                                Scraper.info.Tellonym(
                                    report, username, http_proxy, "Usernames", username)
                            except Exception as e:
                                print(
                                    Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                                http_proxy = None
                                Scraper.info.Tellonym(
                                    report, username, http_proxy, "Usernames", username)
                        else:
                            pass
                    else:
                        ScrapeOp = "Negative"
                else:
                    print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                        Language.Translation.Translate_Language(filename, "Username", "Default", "NoScrape"))
                    ScrapeOp = "Negative"
            else:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                    Language.Translation.Translate_Language(filename, "Username", "Default", "NoFound").format(username))
                ScrapeOp = "Negative"
        else:
            MrHolmes.Scraping(report,username,http_proxy,InstagramParams,PostLocations, PostGpsCoordinates,TwitterParams)
        if PostGpsCoordinates == [] and PostLocations == []:
            pass
        else:
            n = 0
            print(Font.Color.GREEN +
                  "\n[+]" + Font.Color.WHITE + "GETTING LATEST POST GEOLOCATION")
            f = open(report, "a")
            f.write("\nGETTING LATEST POST GEOLOCATION:\n")
            for Locations in PostGpsCoordinates:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Locations)
                f.write(Locations+"\n")
                n = n + 1
            print(Font.Color.GREEN +
                  "\n[+]" + Font.Color.WHITE + "GETTING LATEST PLACE VISITED")
            f = open(report, "a")
            f.write("\nGETTING LATEST PLACE VISITED:\n")
            for Locations in PostLocations:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Locations)
                f.write(Locations+"\n")
            f.close()
        
        count = 1
        Recaps = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                filename, "Default", "Hypo", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if Recaps == 1:
            if opt == 1:
                Percent = found/Count*100
                Recap.Stats.Printer(username, found, Count, Percent, subject,
                                        Tags, InstagramParams, TwitterParams, ScraperSites, ScrapeOp, MostTags)
            else:
                if len(InstagramParams):
                    print(Font.Color.GREEN +
                        "\n[+]" + Font.Color.WHITE + "INSTAGRAM HYPOTHESIS")
                    Recap.Stats.Hypotesys(InstagramParams, username, Recap1)
                if len(TwitterParams):
                    print(Font.Color.GREEN + "\n[+]" +
                       Font.Color.WHITE + "TWITTER HYPOTHESIS")
                    Recap.Stats.Hypotesys(TwitterParams, username, Recap1)
            report = "GUI/Reports/Usernames/{}/Recap.txt".format(username)
            if len(PostLocations):
                Recap.Stats.Places(PostLocations,report,InstagramParams,username,MostTags)
            if len(MostTags):
                Hobby2 = MostTags
            else:
                if len(Tags):
                    Hobby2 = Tags
                else:
                    Hobby2 = "False"
            if Hobby2 != "False":
                print(Font.Color.GREEN +
                  "\n[+]" + Font.Color.WHITE + "GETTING POSSIBLE HOBBIES/INTERESTS:")
                f = open(report, "a")
                f.write("\nGETTING POSSIBLE HOBBIES/INTERESTS:\n")
                sleep(3)
                for PossibleHobby in Hobby2:
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + PossibleHobby)
                    f.write(PossibleHobby+"\n")
                f.close()
    
            Encoding.Encoder.Encode(report)
        else:
            pass
        if count == 1:
            choice = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Dorks", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                MrHolmes.Google_dork(username)
                MrHolmes.Yandex_dork(username)
            print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
                  report)
            report = "GUI/Reports/Usernames/{}/{}.txt".format(username,username)
            f = open(report, "a")
            f.write(Language.Translation.Translate_Language(
                filename, "Report", "Default", "By"))
            f.close()
            Notification.Notifier.Start(Mode)
            Creds.Sender.mail(report, username)
            choice = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Transfer", "Question", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            report = "GUI/Reports/Usernames/{}/{}.txt".format(username,username)
            if choice == 1:
                FileTransfer.Transfer.File(report, username, ".txt")
            Encoding.Encoder.Encode(report)
            print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
                  report)
            inp = input(Language.Translation.Translate_Language(
                        filename, "Default", "Continue", "None"))
