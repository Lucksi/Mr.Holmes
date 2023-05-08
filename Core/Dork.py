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
    def GoogleDorks(report,phrase,data,DorksList,between,seconddata):
        Type = "GOOGLE"
        Dorks.Search.Generator(Type,DorksList,report,phrase,data,between,seconddata)

    
    @staticmethod
    def YandexDorks(report,phrase,data,DorksList,between,seconddata):
        Type = "YANDEX"
        phrase = phrase.replace("+","%2B")
        Dorks.Search.Generator(Type,DorksList,report,phrase,data,between,seconddata)


    @staticmethod 
    def Main(username,Mode):
        List.Banner(Mode)
        now = datetime.now()
        dataformat = DateFormat.Get.Format()
        dt_string = now.strftime(dataformat)
        check = "False"
        between = "False"
        seconddata = "None"
        Date = "Date: " + str(dt_string)
        report = "GUI/Reports/Dorks/{}.txt".format(username)
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        type = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Choice2", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if(type == 1 or type == 4):
            DorksList = "Site_lists/Dorks/Usernames/Google_dorks.txt"
            DorksList2 = "Site_lists/Dorks/Usernames/Yandex_dorks.txt"
        elif(type == 2):
            DorksList = "Site_lists/Dorks/Phone/Google_dorks.txt"
            DorksList2 = "Site_lists/Dorks/Phone/Yandex_dorks.txt"
            DorksList3 = "Site_lists/Dorks/Phone/Fingerprints.txt"
            DorksList4 = "Site_lists/Dorks/Phone/Yandex_Fingerprints.txt"
        elif(type == 3):
            DorksList = "Site_lists/Dorks/Websites/Google_dorks.txt"
            DorksList2 = "Site_lists/Dorks/Websites/Yandex_dorks.txt"
        add = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Question", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        data = ""
        while add == "" or add == 0:
            number = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "ParamN", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if add == 1:
            Start = 1
            Parameters = []
            number = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "ParamN", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            for i in range(number):
                type = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Choice", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if type == 1:
                    if check == "False":
                        data = str(input(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Date", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Added2", "None").format(Font.Color.GREEN + data + Font.Color.WHITE))
                        event = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Event", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                        if event == 1:
                            data = "+before:{}".format(data)
                            data2 = "BEFORE"
                            check = "True"
                        elif event == 2:
                            data = "+after:{}".format(data)
                            data2 = "AFTER"
                            check = "True"
                        else:
                            pass
                    else:
                        print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "DATE ALREADY SEATTED CANNOT USE THIS OPTION")
                    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Added3", "None").format(Font.Color.GREEN + data2 + Font.Color.WHITE))
                elif type == 2 :
                    if check == "False":
                        after = str(input(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "After", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                        print(Font.Color.GREEN + "\n[+]"+ Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Added2", "None").format(Font.Color.GREEN + after + Font.Color.WHITE))
                        begin = str(input(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Dorks", "Before", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE+ Language.Translation.Translate_Language(filename, "Dorks", "Added2", "None").format(Font.Color.GREEN + begin + Font.Color.WHITE))
                        after = "+after:{}".format(after)
                        begin = "before:{}".format(begin)
                        data = after + "+" + begin
                        seconddata = after.replace(":","") +".."+begin.replace(":","")
                        between = "True"
                        check = "True"
                    else:
                       print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "DATE ALREADY SEATTED CANNOT USE THIS OPTION")
                else:
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
        if type == 2:
            List.GoogleDorks(report,phrase,data,DorksList,between="None",seconddata="None")
            List.GoogleDorks(report,phrase,data,DorksList3,between="None",seconddata="None")
            List.YandexDorks(report,phrase,data,DorksList2,between,seconddata)
            List.YandexDorks(report,phrase,data,DorksList4,between,seconddata)
        else:
            List.GoogleDorks(report,phrase,data,DorksList,between="None",seconddata="None")
            List.YandexDorks(report,phrase,data,DorksList2,between,seconddata)
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