# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0 

import os
import sys
from Core.Support import Useragent
from Core.Support import Proxies
from Core.Support import Language
from Core.Support import Font
from time import sleep

filename = Language.Translation.Get_Language()
filename

class Options:

    @staticmethod
    def Printing():
        agent = Useragent.Select.agent
        http_proxy = Proxies.proxy.choice3
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "USERAGENT:[{}]".format(Font.Color.GREEN + agent + Font.Color.WHITE))
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "PROXY-IP:[{}]".format(Font.Color.GREEN + http_proxy + Font.Color.WHITE))
    
    @staticmethod
    def View():
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Session", "Printing", "None"))
        sleep(2)
        Options.Printing()
        choice = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Session", "Question", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            inp = input(Font.Color.GREEN + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Session", "Changed", "None"))
            python = sys.executable
            try:
                os.execl(python, python, *sys.argv)
            except Exception as e:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
        else:
            pass
        inp = input(Font.Color.GREEN + "\n[I]" + Font.Color.WHITE + "PRESS ENTER TO CONTINUE")