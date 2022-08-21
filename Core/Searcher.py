# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import urllib
import json
from Core.Support import Font
from Core.Support import Creds
from Core.Support import Proxies
from Core.Support import Requests_Search
from Core.Support.Username import Scraper
from Core.Support import Clear
from Core.Support import Dorks
from Core.Support import Logs
from Core.Support import Banner_Selector as banner
from Core.Support import Language
from Core.Support import Notification
from datetime import datetime
from time import sleep

filename = Language.Translation.Get_Language()
filename


class MrHolmes:

    @staticmethod
    def Controll(username, nomefile, identity, report, subject, successfull, ScraperSites, Writable, http_proxy2, successfullName, http_proxy, choice):
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
                                                      subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main, json_file, json_file2)
                    except Exception as e:
                        print(
                            Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                        http_proxy = None
                        try:
                            Requests_Search.Search.search(error, report, site1, site2, http_proxy, sites, data1, username,
                                                          subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main, json_file, json_file2)
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
    def Bing_dork(username):
        report = "GUI/Reports/Usernames/Dorks/Bing_{}_Dorks.txt".format(
            username)
        nomefile = "Site_lists/Username/Bing_dorks.txt"
        Type = "BING"
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def search(username, Mode):
        successfull = []
        successfullName = []
        ScraperSites = []
        Writable = True
        MrHolmes.Banner(Mode)
        subject = "USERNAME"
        nomefile = "Site_lists/Username/site_list.json"
        folder = "GUI/Reports/Usernames/" + username + "/"
        report = folder + username + ".txt"
        if os.path.exists(report):
            os.remove(report)
            os.remove(folder + "Name.json")
            os.remove(report.replace(".txt", ".json"))
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        else:
            os.mkdir(folder)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
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
        MrHolmes.Controll(username, nomefile, identity, report, subject,
                          successfull, ScraperSites, Writable, http_proxy2, successfullName, http_proxy, choice)
        Nsfw = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Nsfw") +
                   Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if Nsfw == 1:
            nomefile = "Site_lists/Username/NSFW_site_list.json"
            MrHolmes.Controll(username, nomefile, identity, report, subject,
                              successfull, ScraperSites, Writable, http_proxy2, successfullName, http_proxy, choice)
        else:
            pass
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Default", "TotFound", "None").format(subject, username))
        sleep(3)
        if len(successfull):
            for names in successfull:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + names)
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
                                report, username, http_proxy)
                        except ConnectionError:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Instagram(
                                report, username, http_proxy)
                        except Exception as e:
                            pass
                    else:
                        pass

                    if "TikTok" in ScraperSites:
                        try:
                            Scraper.info.TikTok(
                                report, username, http_proxy)
                        except ConnectionError:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.TikTok(
                                report, username, http_proxy)
                        except Exception as e:
                            pass
                    else:
                        pass

                    if "Disqus" in ScraperSites:
                        try:
                            Scraper.info.Disqus(
                                report, username, http_proxy)
                        except ConnectionError:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Disqus(
                                report, username, http_proxy)
                        except Exception as e:
                            pass
                    else:
                        pass

                    if "Imgur" in ScraperSites:
                        try:
                            Scraper.info.Imgur(report, username, http_proxy)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Imgur(report, username, http_proxy)
                    else:
                        pass

                    if "Pr0gramm" in ScraperSites:
                        try:
                            Scraper.info.Pr0gramm(report, username, http_proxy)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Pr0gramm(report, username, http_proxy)
                    else:
                        pass

                    if "BinarySearch" in ScraperSites:
                        try:
                            Scraper.info.Binarysearch(
                                report, username, http_proxy)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Binarysearch(
                                report, username, http_proxy)
                    else:
                        pass

                    if "MixCloud" in ScraperSites:
                        try:
                            Scraper.info.MixCloud(report, username, http_proxy)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.MixCloud(report, username, http_proxy)
                    else:
                        pass

                    if "Twitter" in ScraperSites:
                        try:
                            Scraper.info.Twitter(report, username, http_proxy)
                        except ConnectionError:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Twitter(report, username, http_proxy)
                        except Exception as e:
                            print(str(e))
                            pass
                    else:
                        pass

                    if "DockerHub" in ScraperSites:
                        try:
                            Scraper.info.Dockerhub(
                                report, username, http_proxy)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Dockerhub(
                                report, username, http_proxy)
                    else:
                        pass

                    if "Kik" in ScraperSites:
                        try:
                            Scraper.info.Kik(report, username, http_proxy)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Kik(report, username, http_proxy)
                    else:
                        pass

                    if "GitLab" in ScraperSites:
                        try:
                            Scraper.info.GitLab(report, username, http_proxy)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.GitLab(report, username, http_proxy)
                    else:
                        pass

                    if "Wattpad" in ScraperSites:
                        try:
                            Scraper.info.Wattpad(report, username, http_proxy)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Wattpad(report, username, http_proxy)
                    else:
                        pass

                    if "GitHub" in ScraperSites:
                        try:
                            Scraper.info.Github(report, username, http_proxy)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Github(report, username, http_proxy)
                    else:
                        pass

                    if "Minecraft" in ScraperSites:
                        try:
                            Scraper.info.Minecraft(
                                report, username, http_proxy)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Minecraft(
                                report, username, http_proxy)
                    else:
                        pass
                    
                    if "Ngl.link" in ScraperSites:
                        try:
                            Scraper.info.Ngl(
                                report, username, http_proxy)
                        except Exception as e:
                            print(
                                Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error1", "None"))
                            http_proxy = None
                            Scraper.info.Ngl(
                                report, username, http_proxy)
                    else:
                        pass
                else:
                    pass
            else:
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Username", "Default", "NoScrape") + "¯\_(ツ)_/¯")
        else:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Username", "Default", "NoFound") + "¯\_(ツ)_/¯".format(username))
        count = 1
        if count == 1:
            choice = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Dorks", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                MrHolmes.Google_dork(username)
                MrHolmes.Yandex_dork(username)
            print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
                  report)
            f = open(report, "a")
            f.write(Language.Translation.Translate_Language(
                filename, "Report", "Default", "By"))
            f.close()
            Notification.Notifier.Start(Mode)
            Creds.Sender.mail(report, username)
