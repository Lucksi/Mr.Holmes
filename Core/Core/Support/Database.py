# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import socket
from Core.Support import Font
from Core.Support import Language
from time import sleep
from configparser import ConfigParser


class Controller:

    @staticmethod
    def Gui():
        Config_file = "Configuration/Configuration.ini"
        filename = Language.Translation.Get_Language()
        filename
        print(Font.Color.BLUE + "\n[I]" +
              Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Database", "Active", "None"))
        Parser = ConfigParser()
        Parser.read(Config_file)
        mode = Parser["Settings"]["Database"]
        if mode == "True":
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 1))
            host = s.getsockname()[0]
            if (os.name != "nt"):
                if os.getuid() == 0:
                    os.system("php -S" + host +
                              ":5001 -t GUI >/dev/null 2>&1 &")
                    Req = True
                else:
                    Req = False
            else:
                os.system("START /B php -S " + host +
                          ":5001 -t GUI 2>NUL >NUL")
                Req = True

            link = host
        else:
            if (os.name != "nt"):
                if os.getuid() == 0:
                    os.system("php -S 127.0.0.1:5001 -t GUI >/dev/null 2>&1 &")
                    Req = True
                else:
                    Req = False

            else:
                os.system("START /B php -S 127.0.0.1:5001 -t GUI 2>NUL >NUL")
                Req = True
            link = "127.0.0.1"
        if Req:
            sleep(3)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Database", "Link", "None") + "http://{}:5001".format(link))
            inp = input(Font.Color.WHITE + Language.Translation.Translate_Language(
                filename, "Database", "Quit", "None"))
            if (os.name != "nt"):
                os.system("killall  php > /dev/null 2>&1")
            else:
                os.system("taskkill /F /IM php.exe 2>NUL >NUL")
            print(Font.Color.BLUE + "\n[I]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Database", "Stop", "None"))
            sleep(2)
            print(Font.Color.BLUE +
                  "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Database", "Del_Token", "None"))
            Token = "GUI/Session/Token.txt"
            Temp = "GUI/Graphs/Temp.txt"
            Temp2 = Temp.replace("Temp","TempEncode")
            if os.path.isfile(Token):
                os.remove(Token)
            else:
                print(Font.Color.BLUE + "\n[I]" +
                      Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Database", "Token", "None"))
            if os.path.isfile(Temp):
                os.remove(Temp)
            else:
                pass
            if os.path.isfile(Temp2):
                os.remove(Temp2)
            else:
                pass
            sleep(3)
        else:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Database", "NoRoot", "None"))
            print(Font.Color.WHITE + Language.Translation.Translate_Language(filename,
                  "Default", "Continue", "None"))
            inp = input()
