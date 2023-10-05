# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2022-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0


import os
import json
import urllib
from Core.Support import Font
from Core.Support import Creds
from Core.Support import Proxies
from Core.Support.Person import Scraper
from Core.Support import Clear
from Core.Support import Dorks
from Core.Support import Logs
from Core.Support import Banner_Selector as banner
from Core.Support import Language
from Core.Support import DateFormat
from Core.Support import Notification
from Core.Support import Recap
from Core.Support import FileTransfer
from datetime import datetime
from time import sleep
from Core.Support import Encoding


filename = Language.Translation.Get_Language()
filename


class info:

    @staticmethod
    def Google_dork(username):
        report = "GUI/Reports/People/Dorks/{}_Dorks.txt".format(username)
        nomefile = "Site_lists/Username/Google_dorks.txt"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Dorks", "Remove", "None").format(username))
        else:
            pass
        Type = "GOOGLE"
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def Yandex_dork(username):
        report = "GUI/Reports/People/Dorks/{}_Dorks.txt".format(username)
        nomefile = "Site_lists/Username/Yandex_dorks.txt"
        Type = "YANDEX"
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def Banner(Mode):
        Clear.Screen.Clear()
        Folder = "Banners/Person"
        banner.Random.Get_Banner(Folder, Mode)

    @staticmethod
    def Search(username, Mode):
        username2 = username.replace(" ", "_")
        folder = "GUI/Reports/People/" + username2 + "/"
        report = folder + username2 + ".txt"
        report2 = folder + username2 + ".mh"
        link1 = folder + "Insta_Link.json"
        link2 = folder + "Twitter_Link.json"
        link3 = folder + "TikTok_Link.json"
        Recap1 = folder + "Recap.txt"
        Recap2 = folder + "Recap.mh"
        imagefold = "GUI/Reports/People/" + username2 + "/Profile_pics"
        InstagramParams = []
        TwitterParams = []
        PostLocations = []
        PostGpsCoordinates = []
        MostTags = []
        info.Banner(Mode)
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "INFO:" + "[{}]".format(Font.Color.GREEN + Language.Translation.Translate_Language(filename,"Username","Default","ExplanationP") + Font.Color.WHITE) )
        subject = "PERSON"
        now = datetime.now()
        dataformat = DateFormat.Get.Format()
        dt_string = now.strftime(dataformat)
        Date = "Date: " + str(dt_string)
        if os.path.exists(report):
            os.remove(report)
            if os.path.exists(Recap1):
                os.remove(Recap1)
            elif os.path.exists(Recap2):
                os.remove(Recap2)
            if os.path.exists(link1):
                os.remove(link1)
            if os.path.exists(link2):
                os.remove(link2)
            if os.path.exists(link3):
                os.remove(link3)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        elif os.path.exists(report2):
            os.remove(report2)
            if os.path.exists(Recap1):
                os.remove(Recap1)
            elif os.path.exists(Recap2):
                os.remove(Recap2)
            if os.path.exists(link1):
                os.remove(link1)
            if os.path.exists(link2):
                os.remove(link2)
            if os.path.exists(link3):
                os.remove(link3)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        else:
            os.mkdir(folder)
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
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        folder = "People"
        Logs.Log.Checker(username, folder)
        f = open(report, "a")
        f.write(Language.Translation.Translate_Language(
            filename, "Report", "Default", "Date").format(Date) + "\r\n")
        f.close()
        Scraper.Search.Instagram(report, username, http_proxy, InstagramParams,
                                 PostLocations, PostGpsCoordinates, imagefold, username2,"People")
        Scraper.Search.Twitter(report, username, http_proxy, TwitterParams,
                               imagefold, username2,"People")
        Scraper.Search.TikTok(
            report, username, http_proxy, imagefold, username2,"People")
        Scraper.Search.Github(report, username, http_proxy,imagefold, username2,"People")
        if PostGpsCoordinates == [] and PostLocations == []:
            pass
        else:
            n = 0
            print(Font.Color.GREEN +
                  "\n[+]" + Font.Color.WHITE + "GETTING LATEST POST GEOLOCATION:")
            f = open(report, "a")
            f.write("\nGETTING LATEST POST GEOLOCATION:\n")
            for Locations in PostGpsCoordinates:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Locations)
                f.write(Locations + "\n")
                n = n + 1
            f.close()
            
            print(Font.Color.GREEN +
                  "\n[+]" + Font.Color.WHITE + "GETTING LATEST PLACE VISITED:")
            f = open(report, "a")
            f.write("\nGETTING LATEST PLACE VISITED:\n")
            for Locations in PostLocations:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Locations)
                f.write(Locations+"\n")
            f.close()
        Recaps = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(
            filename, "Default", "Hypo", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if Recaps == 1:
            if len(InstagramParams):
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + "INSTAGRAM HYPOTHESIS")
                Recap.Stats.Hypotesys(InstagramParams, username, Recap1)
            if len(TwitterParams):
                print(Font.Color.GREEN + "\n[+]" +
                      Font.Color.WHITE + "TWITTER HYPOTHESIS")
                Recap.Stats.Hypotesys(TwitterParams, username, Recap1)
            Recap.Stats.Places(PostLocations,Recap1,InstagramParams,username,MostTags)
            if len(MostTags):
                print(Font.Color.GREEN +
                  "\n[+]" + Font.Color.WHITE + "GETTING POSSIBLE HOBBIES/INTERESTS:")
                f = open(Recap1, "a")
                f.write("\nGETTING POSSIBLE HOBBIES/INTERESTS:\n")
                sleep(3)
                for PossibleHobby in MostTags:
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + PossibleHobby)
                    f.write(PossibleHobby+"\n")
            Encoding.Encoder.Encode(Recap1)
        choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Dorks", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            info.Google_dork(username)
            info.Yandex_dork(username)
        Notification.Notifier.Start(Mode)
        Creds.Sender.mail(report, username)
        choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Transfer", "Question", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            FileTransfer.Transfer.File(report, username, ".txt")
        Encoding.Encoder.Encode(report)
        print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
              report)
        inp = input(Language.Translation.Translate_Language(
            filename, "Default", "Continue", "None"))
