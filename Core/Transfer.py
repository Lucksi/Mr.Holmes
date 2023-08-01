# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import MrHolmes as holmes
from time import sleep
from Core.Support import Font
from Core.Support import Language
from Core.Support import Clear
from Core.Support import Banner_Selector as banner
from Core.Support import FileTransfer as FileT

filename = Language.Translation.Get_Language()
filename

class Menu:
    
    @staticmethod
    def Banner(Mode):
        Clear.Screen.Clear()
        Folder = "Banners/Transfer"
        banner.Random.Get_Banner(Folder, Mode)

    @staticmethod
    def Main(username,Mode):
        Menu.Banner(Mode)
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "INFO:" + "[{}]".format(Font.Color.GREEN + Language.Translation.Translate_Language(filename,"Transfer","Explanation","None") + Font.Color.WHITE) )
        folder = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                        filename, "Transfer", "Folder", "None").format(Font.Color.GREEN + username + Font.Color.WHITE)  + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if folder == 1:
            fold = "Usernames"
            secondFold = "True"
        elif folder == 2:
            fold = "Phone"
            secondFold = "True"
        elif folder == 3:
            fold = "Websites"
            secondFold = "True"
        elif folder == 4:
            fold = "People"
            secondFold = "True"
        elif folder == 5:
            fold = "E-Mail"
            secondFold = "False"
        elif folder == 6:
            fold = "Ports"
            secondFold = "False"
        elif folder == 7:
            fold = "PDF"
            secondFold = "Exception"
        elif folder == 8:
            fold = "Maps"
            secondFold = "True"
        elif folder == 9:
            fold = "Graphs"
            secondFold = "True"
        elif folder == 8:
            inp = input(Language.Translation.Translate_Language(
                        filename, "Configuration", "Main", "Exit"))
            holmes.Main.Menu(Mode)
        if folder == 1 or folder == 4:
            choice = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                        filename, "Decoding", "Type", "None").format(username)  + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            username= username.replace(" ","_")
            if choice == 1:
                report = username
                name2 = username
            elif choice == 2:
                report = "Recap"
                name2 = "Recap"
            else:
                exit()
        else:
            report = username
            name2 = username
        if secondFold == "True":
            if fold == "Graphs" or fold == "Maps":
                Report = "GUI/{}/{}/{}".format(fold,username,report)
            else:
               Report = "GUI/Reports/{}/{}/{}".format(fold,username,report)
        elif secondFold == "False":
            Report = "GUI/Reports/{}/{}".format(fold,report)
        else:
            Report = "GUI/PDF/{}".format(report)
        if secondFold != "Exception":
            option = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                        filename, "Transfer", "Type", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if option == 1:
                report = Report + ".txt"
                extension = ".txt"
                name = name2
            elif option == 2:
                report = Report + ".mh"
                extension = ".mh"
                name = name2
        else:
            report = Report + ".pdf"
            extension = ".pdf"
            name = username
        FileT.Transfer.File(report,name,extension)
        inp = input(Language.Translation.Translate_Language(
                        filename, "Default", "Continue", "None"))
