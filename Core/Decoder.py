# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
from time import sleep
from Core.Support import Font
from Core.Support import Language
from Core.Support import Clear
from Core.Support import Banner_Selector as banner
from Core.Support import Encoding

filename = Language.Translation.Get_Language()
filename

class Menu:
    
    @staticmethod
    def Banner(Mode):
        Clear.Screen.Clear()
        Folder = "Banners/Decode"
        banner.Random.Get_Banner(Folder, Mode)

    @staticmethod
    def Main(username,Mode):
        Menu.Banner(Mode)
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "INFO:" + "[{}]".format(Font.Color.GREEN + Language.Translation.Translate_Language(filename,"Decoding","Explanation","None") + Font.Color.WHITE))
        folder = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                        filename, "Decoding", "Folder", "None").format(Font.Color.GREEN + username + Font.Color.WHITE)  + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
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
        if folder == 1 or folder == 4:
            choice = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                        filename, "Decoding", "Type", "None").format(username)  + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            username= username.replace(" ","_")
            if choice == 1:
                report = username
            elif choice == 2:
                report = "Recap"
            else:
                exit()
        else:
            report = username
        if secondFold == "True":
            Report = "GUI/Reports/{}/{}/{}".format(fold,username,report)
        else:
            Report = "GUI/Reports/{}/{}".format(fold,report)
        option = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                        filename, "Decoding", "Options", "None")+ Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if option == 1:
            report = Report + ".txt" 
            Encoding.Encoder.Encode(report)
        elif option == 2:
            report = Report + ".mh" 
            Encoding.Encoder.Decode(report)
        inp = input(Language.Translation.Translate_Language(
                        filename, "Default", "Continue", "None"))