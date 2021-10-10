# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import os
from Core.Support import Font
from Core.Support import Clear
from Core.Support import Scanner
from Core.Support import Creds
from datetime import datetime

class Ports:
    
    @staticmethod
    def Banner():
        Clear.Screen.Clear()
        nomefile = "Banners/Banner7.txt"
        f = open(nomefile,"r")
        banner = f.read()
        f.close()
        print(Font.Color.GREEN + banner)
    
    @staticmethod
    def Main(username):
        Ports.Banner()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        Date = "Date: " + str(dt_string)
        report = "GUI/Reports/Ports/{}.txt".format(username)
        if os.path.exists(report):
            print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + "DELETING OLD {}.txt".format(username))
            os.remove(report)
        f = open(report, "a")
        f.write("SCANNING EXECUTED ON:\n" + Date + "\r\n")
        f.write("OPEN PORTS:\r\n")
        f.close()
        Scanner.Port.Scan(username,report)
        print(Font.Color.WHITE + "\nREPORT WRITTEN IN: " + os.getcwd() + "/" + report)
        f = open(report,"a")
        f.write("\nSCANNING EXECUTED WITH Mr.Holmes")
        f.close()
        Creds.Sender.mail(report, username)
