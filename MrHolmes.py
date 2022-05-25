#!/usr/bin/python3
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import os
from Core.Support import Menu
from Core.Support import Font
from Core.Support import Language

filename = Language.Translation.Get_Language()
filename

class Main:

    @staticmethod
    def Controll_Display():
        Interface_file = "Display/Display.txt"
        if os.path.isfile(Interface_file):
            d = open(Interface_file,"r",newline=None)
            conf = d.read().strip("\n")
            d.close()
            if conf == "Desktop":
                pass
            elif conf == "Mobile":
                pass
            else:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + "LOOKS LIKE THERE IS AN INVALID OPTION ACCEPTED ONLY 'Desktop' OR 'Mobile' EXIT...")
                exit()
        else:
             print(Font.Color.RED + "[!]" + Font.Color.WHITE + "FILE HAS NOT BEEN FOUND {} EXIT...".format(Interface_file))
        return conf

    def Menu(Mode):
        Menu.Main.main(Mode)

if __name__ == "__main__":
    Mode = Main.Controll_Display()
    Mode
    try:
       Main.Menu(Mode)
    except KeyboardInterrupt:
        print(Font.Color.RED + "\n\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "KeyC", "None"))
        exit()
    except ModuleNotFoundError as Error:
        print(Font.Color.RED + "\n\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Internal", "None").format(str(Error)))
        exit()