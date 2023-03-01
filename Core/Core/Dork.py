# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2022-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
from Core.Support import Font
from Core.Support import Dorks
from Core.Support import FileTransfer
from Core.Support import Banner_Selector as banner
from Core.Support import Notification
from Core.Support import Language
from Core.Support import DateFormat
from Core.Support import Clear
from Core.Support import Creds
from datetime import datetime

filename = Language.Translation.Get_Language()
filename


class List:

    @staticmethod
    def Banner(Mode):
        Clear.Screen.Clear()
        Folder = "Banners/Dorks"
        banner.Random.Get_Banner(Folder, Mode)

    @staticmethod
    def GoogleDorks(report,phrase):
        nomefile = "Site_lists/Username/Google_dorks.txt"
        Type = "GOOGLE"
        Dorks.Search.Generator(Type,nomefile,report,phrase)

    
    @staticmethod
    def YandexDorks(report,phrase):
        Type = "YANDEX"
        nomefile = "Site_lists/Username/Yandex_dorks.txt"
        phrase = phrase.replace("+","%2B")
        Dorks.Search.Generator(Type,nomefile,report,phrase)


    @staticmethod
    def Main(username,Mode):
        List.Banner(Mode)
        now = datetime.now()
        dataformat = DateFormat.Get.Format()
        dt_string = now.strftime(dataformat)
        Date = "Date: " + str(dt_string)
        report = "GUI/Reports/Dorks/{}.txt".format(username)
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        add = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Question", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        while add == "" or add == 0:
            number = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "ParamN", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if add == 1:
            Start = 1
            Parameters = []
            number = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "ParamN", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            for i in range(number):
                param = str(input(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Param", "None").format(str(Start)) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while param == "":
                    param = str(input(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Param", "None").format(str(Start)) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Added", "None").format(Font.Color.GREEN + param + Font.Color.WHITE))
                Parameters.append("+"+param)
                Start = Start +1
            phrase = username + "".join(Parameters)
        else:
            phrase = username
        f = open(report, "a")
        f.write(Language.Translation.Translate_Language(
            filename, "Report", "Default", "Date").format(Date) + "\r\n")
        f.close()
        List.GoogleDorks(report,phrase)
        List.YandexDorks(report,phrase)
        f = open(report, "a")
        f.write(Language.Translation.Translate_Language(
                filename, "Report", "Default", "By"))
        f.close()
        Notification.Notifier.Start(Mode)
        Creds.Sender.mail(report, username)
        choice = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Transfer", "Question", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            FileTransfer.Transfer.File(report,username,".txt") 
        inp = input(Language.Translation.Translate_Language(
                        filename, "Default", "Continue", "None"))