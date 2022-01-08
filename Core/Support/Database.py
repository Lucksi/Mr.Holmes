# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import os
import socket
from Core.Support import Font
from time import sleep
from configparser import ConfigParser


class Controller:

    @staticmethod
    def Gui():
        Config_file = "Configuration/Configuration.ini"
        print(Font.Color.BLUE + "\n[I]" +
              Font.Color.WHITE + "ACTIVATING DATABASE...")
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
                              ":200 -t GUI >/dev/null 2>&1 &")
                    Req = True
                else:
                    Req = False
            else:
                os.system("START /B php -S " + host +
                          ":200 -t GUI 2>NUL >NUL")
                Req = True

            link = host
        else:
            if (os.name != "nt"):
                if os.getuid() == 0:
                    os.system("php -S 127.0.0.1:200 -t GUI >/dev/null 2>&1 &")
                    Req = True
                else:
                    Req = False

            else:
                os.system("START /B php -S 127.0.0.1:200 -t GUI 2>NUL >NUL")
                Req = True
            link = "127.0.0.1"
        if Req :
                sleep(3)
                print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                      "DATABASE STARTED ON http://{}:200".format(link))
                inp = input("\nPRESS ENTER TO STOP ")
                if (os.name != "nt"):
                    os.system("killall  php > /dev/null 2>&1")
                else:
                    os.system("taskkill /F /IM php.exe 2>NUL >NUL")
                print(Font.Color.BLUE + "\n[I]" +
                      Font.Color.WHITE + "STOPPING DATABASE...")
                sleep(2)
                print(Font.Color.BLUE +
                      "\n[I]" + Font.Color.WHITE + "DELETING TOKEN SESSION FILE...")
                Token = "GUI/Session/Token.txt"
                if os.path.isfile(Token):
                    os.remove(Token)
                else:
                    print(Font.Color.BLUE + "\n[I]" +
                          Font.Color.WHITE + "TOKEN NOT FOUND...")
                sleep(3)
        else:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                          "YOU MUST BE ROOT FOR ACTIVATING THE DATABASE")
            print(Font.Color.WHITE + "\nPRESS ENTER TO CONTINUE..")
            inp = input()
