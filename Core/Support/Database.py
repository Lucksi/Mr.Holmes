# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import os
import MrHolmes as Holmes
import socket
from Core.Support import Font
from time import sleep
from configparser import ConfigParser

class Controller:
    
    @staticmethod
    def Gui():
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
        else :
            os.system("sudo php -S 127.0.0.1:200 -t GUI >/dev/null 2>&1 &")
            sleep(3)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "DATABASE STARTED ON http://127.0.0.1:200")
        inp = input("\nPRESS ENTER TO STOP ")
        os.system ("killall  php > /dev/null 2>&1")
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "STOPPING DATABASE...")
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "DELETING TOKEN SESSION FILE...")
        Token = "GUI/Session/Token.txt"
        if os.path.isfile(Token):
            os.remove(Token)
        else:
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "TOKEN NOT FOUND...")
        sleep(3)
        Holmes.Main()