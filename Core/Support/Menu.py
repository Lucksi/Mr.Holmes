# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import os
import random
from Core.Support import Font
from Core.Support import Clear
from Core import Searcher
from Core import config
from Core import Searcher_phone
from Core import Searcher_website
from Core import Port_Scanner
from Core import E_Mail
from Core import Update
from Core.Support import Database
from Core.Support import Agree
from Core.Support import Language


class Main:

    @staticmethod
    def Checker():
        if os.path.exists("Configuration/Agreement.txt"):
            pass
        else:
            Agree.One_time.Agreement()

    @staticmethod
    def banner(r):
        Clear.Screen.Clear()
        f = open("Version/Version.txt", "r", newline=None)
        for line in f:
            r = line.replace("\n", "")
        version = f.read() + r
        f.close()
        Quotes = ["Quotes1.txt", "Quotes4.txt", "Quotes3.txt", "Quotes7.txt",
                  "Quotes6.txt", "Quotes2.txt", "Quotes5.txt", "Quotes8.txt",
                  "Quotes9.txt", "Quotes10.txt", "Quotes11.txt", "Quotes12.txt",
                  "Quotes13.txt", "Quotes14.txt", "Quotes15.txt", "Quotes16.txt",
                  "Quotes17.txt", "Quotes18.txt", "Quotes19.txt", "Quotes20.txt"]
        choice = random.choice(Quotes)
        f = open("Quotes/" + choice, "r", newline=None)
        text = f.read()
        f.close()
        if os.name == "nt":
            u = "|\t\t\t    MR.HOLMES\t\t\t\t    |"
        else:
            u = "|\t\t\t   🇲​​​​​🇷​​​​​.🇭​​​​​🇴​​​​​🇱​​​​​🇲​​​​​🇪​​​​​🇸​​​​​\t\t\t    |"
        print(Font.Color.WHITE +
              "---------------------------------------------------------------------")
        print(Font.Color.WHITE + u)
        print(Font.Color.GREEN + text
              +
              Font.Color.WHITE + "| A COMPLETE OSINT TOOL:)      " + Font.Color.BANNER + "CODED BY LUCKSI" + Font.Color.RESET + Font.Color.WHITE + "                      |\n|                                                                   |")
        print(Font.Color.WHITE + "|[+]" + Font.Color.GREEN + "VERSION:" + version +
              Font.Color.WHITE + "                                           |")
        print(
            Font.Color.YELLOW + "|Instagram:lucks_022                                                |\n|EMAIL:lukege287@gmail.com                                          |\n|GIT-HUB:Lucksi                                                     |\n|Twitter:@Lucksi_22                                                 |\n|Linkedin:https://www.linkedin.com/in/Lucksi                        |")
        print(Font.Color.WHITE +
              "---------------------------------------------------------------------")

    @staticmethod
    def main():
        while True:
            try:
                Main.Checker()
                filename = Language.Translation.Get_Language()
                filename
                Main.banner(r=True)
                option = Language.Translation.Translate_Language(
                    filename, "Main", "Options", "None")
                options = str(option)
                print(Font.Color.GREEN +
                      Language.Translation.Translate_Language(filename, "Main", "Text", "None"))
                print(Font.Color.WHITE + options)
                sce = int(input(Font.Color.GREEN +
                          "\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if sce == 1:
                    print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(filename, "Main", "Alert", "None"))
                    username = str(input(
                        Font.Color.BLUE + "\n[+]" + Font.Color.WHITE +
                        Language.Translation.Translate_Language(filename, "Main", "Username", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    while username == "":
                        username = str(input(
                            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Username", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    Searcher.MrHolmes.search(username)

                elif sce == 2:
                    username = str(input(
                        Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Phone", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    while username == "":
                        username = str(input(
                            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Phone", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    Searcher_phone.Phone_search.searcher(username)

                elif sce == 3:
                    username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Site", "None") +
                                   Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    while username == "":
                        username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Site", "None") +
                                       Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    Searcher_website.Web.search(username)
                elif sce == 4:
                    config.Config.main()
                elif sce == 5:
                    Database.Controller.Gui()
                elif sce == 6:
                    if os.name == "nt":
                        Update.Downloader.Check_Creds()
                    else:
                        os.system("Core/./update.sh")
                elif sce == 7:
                    username = input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Port", "None") +
                                     Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                    while username == "":
                        username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Port", "None") +
                                       Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    Port_Scanner.Ports.Main(username)
                elif sce == 8:
                    username = input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Email", "None") +
                                     Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                    while username == "":
                        username = str(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Main", "Email", "None") +
                                       Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    E_Mail.Mail_search.Search(username)
                elif sce == 9:
                    print(Language.Translation.Translate_Language(
                        filename, "Main", "Exit", "None"))
                    exit()
                elif sce == 0:
                    Main.main()
                else:
                    print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(filename, "Default", "KeyError", "None"))
                    exit()
            except ValueError as e:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Default", "ValueError", "None") + "{}".format(str(e)))
                exit()
