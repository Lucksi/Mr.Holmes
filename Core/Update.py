# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import configparser
import os
from configparser import ConfigParser
from Core.Support import Font

Conf_file = "Configuration/Configuration.ini"
Parser = ConfigParser()
Parser.read(Conf_file)

class Downloader:
    
    @staticmethod
    def Check_Creds():
        Attempts = 5
        Password = Parser["Settings"]["Password"]
        while Attempts>0:
            Pass = str(input(Font.Color.BLUE + "INSERT YOUR UPDATE PASSWORD YOU HAVE {} ATTEMPTS".format(Attempts)))
            while Pass == "":
                Pass = str(input(Font.Color.BLUE + "INSERT YOUR UPDATE PASSWORD YOU HAVE {} ATTEMPTS".format(Attempts)))
            if Pass == Password:
                Downloader.Update()
            else:
                Attempts = Attempts -1
                print(Font.Color.BLUE + "WRONG PASSWORD YOU HAVE {} ATTEMPTS".format(Attempts))
        inp = input("YOU HAVE {} ATTEMPTS PRESS ENTER TO CONTINUE".format(Attempts))
    
    @staticmethod
    def Update():
        Path = Parser["Settings"]["Path"]
        os.system("cd {}".format(Path))
        os.system("rename Mr.Holmes Mr.Holmes2")
        os.system("git clone https://github.com/Lucksi/Mr.Holmes 2>NUL >NUL")
        choice = int(input(Font.Color.WHITE + "\nWOULD YOU LIKE TO DELETE THE OLD FILES?(1)YES(2)NO\n\n"))
        if choice == 1:
            os.remove("Mr.Holmes")
            print(Font.Color.BLUE + "DELETING OLD MR.HOLMES FILES")
        else:
            print(Font.Color.BLUE + "KEEPING OLD MR.HOLMES FILES")
        inp = input(Font.Color.WHITE + "MR.HOLMES UPDATED CORRECTLY")
