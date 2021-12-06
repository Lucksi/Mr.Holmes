# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import os
import socket
from Core.Support import Font
from time import sleep
from configparser import ConfigParser

class Controller:
    
    @staticmethod
    def Gui():
        if os.name == "nt":
            inp = input(Font.Color.RED + "[!]" + Font.Color.WHITE + "SORRY BUT DATABASE IS'NT AVIABLE FOR WINDOWS AT THE MOMENT:(\n\nPRESS ENTER TO CONTINUE")
        else:
            Config_file = "Configuration/Configuration.ini"
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "ACTIVATING DATABASE...")
            Parser = ConfigParser()
            Parser.read(Config_file)
            mode = Parser["Settings"]["Database"]
            if mode == "True" :
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('8.8.8.8', 1))
                host = s.getsockname()[0]
                os.system("sudo php -S" + host + ":200 -t GUI >/dev/null 2>&1 &")
                sleep(3)
                print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "DATABASE STARTED ON http://{}:200".format(host))
            else:
                os.system("sudo php -S 127.0.0.1:200 -t GUI >/dev/null 2>&1 &")
                sleep(3)
                print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "DATABASE STARTED ON http://127.0.0.1:200")
            inp = input("\nPRESS ENTER TO STOP ")
            os.system ("killall  php > /dev/null 2>&1")
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "STOPPING DATABASE...")
            sleep(2)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "DELETING TOKEN SESSION FILE...")
            Token = "GUI/Session/Token.txt"
            if os.path.isfile(Token):
                os.remove(Token)
            else:
                print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "TOKEN NOT FOUND...")
            sleep(3)