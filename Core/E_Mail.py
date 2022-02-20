# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0


import os
import json
import MrHolmes as holmes
from Core.Support import Font
from Core.Support import Creds
from Core.Support import Clear
from Core.Support import Dorks
from Core.Support.Mail import Mail_Validator as mail
from Core.Support import Banner_Selector as banner
from Core.Support import Language
from time import sleep
from datetime import datetime

filename = Language.Translation.Get_Language()
filename

class Mail_search:

    @staticmethod
    def Banner():
        Clear.Screen.Clear()
        Folder = "Banners/E-Mail"
        banner.Random.Get_Banner(Folder)

    @staticmethod
    def Google_dork(username):
        report = "GUI/Reports/E-Mail/Dorks/{}_dorks.txt".format(username)
        nomefile = "Site_lists/E-Mail/Google_dorks.txt"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Remove", "None").format(username))
        else:
            pass
        Type = "GOOGLE"
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def Yandex_dork(username):
        report = "GUI/Reports/E-Mail/Dorks/{}_dorks.txt".format(username)
        nomefile = "Site_lists/E-Mail/Yandex_dorks.txt"
        Type = "YANDEX"
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def searcher(username, report):
        nomefile = "Temp/E-Mail/Code.txt"
        if os.path.isfile(nomefile):
            list_file = "Site_lists/E-Mail/Lists.json"
            reader = open(list_file,)
            data = json.loads(reader.read())
            for sites in data:
                for data1 in sites:
                    name = sites[data1]["name"]
                    url = sites[data1]["url"].replace("{}", username)
                    print(
                        Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Link", "None").format(name))
                    sleep(2)
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + url)
                    f = open(report, "a")
                    f.write("\nGENERATING {} LINK".format(name))
                    f.write("\n{}".format(url))
                f.close()
            f.close()
            os.remove(nomefile)
        else:
            holmes.Main.Menu()

    @staticmethod
    def Search(username):
        Mail_search.Banner()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        Date = "Date: " + str(dt_string)
        report = "GUI/Reports/E-Mail/" + username + ".txt"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        f = open(report, "w")
        f.write("SCANNING EXECUTED ON:\n" + Date + "\n")
        f.close()
        mail.Validator.Mail(username, report)
        Mail_search.searcher(username, report)
        choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Dorks", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            Mail_search.Google_dork(username)
            Mail_search.Yandex_dork(username)
        else:
            pass
        print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
              os.getcwd() + "/" + report)
        f = open(report, "a")
        f.write("\nSCANNING EXECUTED WITH Mr.Holmes")
        f.close()
        Creds.Sender.mail(report, username)
