# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import os
import getpass
import MrHolmes as holmes
from Core.Support import Font
from configparser import ConfigParser
from Core.Support import Clear

dest = "Configuration"
nomefile = "Configuration.ini"

class Config:

    @staticmethod
    def Banner():
        Clear.Screen.Clear()
        f = open("Banners/Banner5.txt")
        banner = f.read()
        f.close()
        print(Font.Color.GREEN + banner)

    @staticmethod
    def modify_recipient():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR RECIPIENT EMAIL?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                recipient = str(input(
                    Font.Color.WHITE + "\nINSERT THE EMAIL-RECIPIENT(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while recipient == "":
                    recipient = str(input(
                        Font.Color.RED + "\n[!]" + Font.Color.WHITE + "INSERT AN EMAIL-RECIPIENT(INSERT NONE FOR QUITTING)" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if recipient == "None":
                    out = input("\nRECIPIENT-EMAIL NOT CHANGED PRESS ENTER TO EXIT")
                    os.chdir("../")
                else:
                    Parser.set("Smtp","Email",recipient)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nEMAIL CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_password():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR RECIPIENT-EMAIL-PASSWORD?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                passw = getpass.getpass(
                    Font.Color.WHITE + "\nINSERT THE PASSWORD-RECIPIENT(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                while passw == "":
                    passw = getpass.getpass(
                        Font.Color.RED + "\n[!]" + Font.Color.WHITE + "INSERT THE PASSWORD-RECIPIENT(INSERT NONE FOR QUITTING)" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                if passw == "None":
                    out = input("\nRECIPIENT-PASSWORD NOT CHANGED PRESS ENTER TO EXIT")
                    os.chdir("../")
                else:
                    Parser.set("Smtp","Password",passw)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nPASSWORD CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_destination():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR DESTINATION-EMAIL?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                destination = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR DESTINATION-MAIL(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while destination == "":
                   destination = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR DESTINATION-MAIL(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if destination == "None":
                    out = input("\nDESTINATION-MAIL NOT CHANGED PRESS ENTER TO EXIT")
                    os.chdir("../")
                else:
                    Parser.set("Smtp","Destination",destination)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nEMAIL CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_port():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR SERVER-PORT?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                port = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR SERVER-PORT(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while port == "":
                   port = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR SERVER-PORT(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if port == "None":
                    out = input("\nSERVER-PORT NOT CHANGED PRESS ENTER TO EXIT")
                    os.chdir("../")
                else:
                    Parser.set("Smtp","Destination",port)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nPORT CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_server():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR SMTP-SERVER?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                server = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR SMTP-SERVER(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while server == "":
                    server = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR SMTP-SERVER(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if server == "None":
                    out = input("\nSMTP-SERVER NOT CHANGED PRESS ENTER TO EXIT")
                    os.chdir("../")
                else:
                    Parser.set("Smtp","Server",server)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nSMTP-SERVER CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")
    
    @staticmethod
    def modify_path():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR UPDATE-PATH?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile:
                Parser = ConfigParser()
                Parser.read(nomefile)
                path = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR UPDATE-PATH(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while path == "":
                    path = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR UPDATE-PATH(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if path == "None":
                    out = input("\nUPDATE-PATH NOT CHANGED PRESS ENTER TO EXIT")
                    os.chdir("../")
                else:
                    Parser.set("Settings","Path",path)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nUPDATE-PATH CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_update_pass():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR UPDATE-PASSWORD?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile:
                Parser = ConfigParser()
                Parser.read(nomefile)
                passw = getpass.getpass(
                        Font.Color.WHITE + "\nINSERT YOUR UPDATE-PASSWORD(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                while passw == "":
                    passw = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR UPDATE-PASSWORD(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if passw == "None":
                    out = input("\nUPDATE-PASSWORD NOT CHANGED PRESS ENTER TO EXIT")
                    os.chdir("../")
                else:
                    Parser.set("Settings","Password",passw)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                        print("\nUPDATE-PASSWORD CHANGED SUCCESSFULLY")
                        out = input("\nPRESS ENTER TO EXIT")
                        os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_key():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR WHO-IS-XMLAPI-KEY?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                key = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR API-KEY(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while key == "":
                    key = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR API-KEY" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if key == "None":
                    out = input("\nAPI-KEY NOT CHANGED PRESS ENTER TO EXIT")
                    os.chdir("../")
                else:
                    Parser.set("Settings","Path",key)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nAPI-KEY CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")
    
    @staticmethod
    def modify_proxy():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR PROXY-LIST-PATH?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                proxy_path = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR PROXY-LIST-PATH(INSERT NONE FOR QUITTING)" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while proxy_path == "":
                    proxy_path = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR PROXY-LIST-PATH" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if proxy_path == "None":
                    out = input("\nPROXY-LIST NOT CHANGED PRESS ENTER TO EXIT")
                    os.chdir("../")
                else:
                    Parser.set("Settings","Proxy_List",proxy_path)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nPROXY-LIST CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")
    
    @staticmethod
    def modify_Log():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR LOG OPTION?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                Logs = int(input(
                        Font.Color.WHITE + "\nINSERT IF YOU WANT TO ENABLE LOGS FEATURE(1)YES(2)NO" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if Logs == 1:
                    Logs = "True"
                elif Logs == 2:
                    Logs = "False"
                else:
                    os.chdir("../")
                    Config.main()
                Parser.set("Settings","show_Logs",Logs)
                with open(nomefile, 'w') as configfile:
                    Parser.write(configfile)
                    print("\nLOGS OPTION CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")
    
    @staticmethod
    def modify_Database_Visibility():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR DATABSE SETTING?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                Data = int(input(
                        Font.Color.WHITE + "\nINSERT IF YOU WANT TO ENABLE YOUR DATABASE ON OTHER DEVICES(1)YES(2)NO" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if Data == 1:
                    Data = "True"
                elif Data == 2:
                    Data = "False"
                else:
                    os.chdir("../")
                    Config.main()
                Parser.set("Settings","Database",Data)
                with open(nomefile, 'w') as configfile:
                    Parser.write(configfile)
                    print("\nDATABASE OPTION CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def main():
        while True:
            Config.Banner()
            option = "\n(1)MODIFY-SENDER-MAIL\n(2)MODIFY-DESTINATION-MAIL\n(3)MODIFY-PASSWORD-MAIL\n(4)MODIFY-SMTP-SERVER\n(5)MODIFY-SMTP-PORT\n(6)MODIFY-UPDATE-PASSWORD\n(7)MODIFY-UPDATE-PATH\n(8)MODIFY-API-KEY\n(9)MODIFY-PROXY-LIST-PATH\n(10)MODIFY-LOGS\n(11)MODIFY-DATABASE\n(12)MAIN-MENU"
            options = str(option)
            print(Font.Color.GREEN + "[INSERT AN OPTION]")
            print(Font.Color.WHITE + options)
            sce = int(input(Font.Color.GREEN + "\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if sce == 1:
                Config.modify_recipient()
            elif sce == 2:
                Config.modify_destination()
            elif sce == 3:
                Config.modify_password()
            elif sce == 4:
                Config.modify_server()
            elif sce == 5:
                Config.modify_port()
            elif sce == 6:
                Config.modify_update_pass()
            elif sce == 7:
                Config.modify_path()
            elif sce == 8:
                Config.modify_key()
            elif sce == 9:
                Config.modify_proxy()
            elif sce == 10:
                Config.modify_Log()
            elif sce == 11:
                Config.modify_Database_Visibility()
            elif sce == 12:
                inp = input("PRESS ENTER TO CONTINUE...")
                holmes.Main.Menu()
            else:
                inp = input(Font.Color.RED + "[!]" + Font.Color.WHITE + "WRONG OPTION PRESS ENTER TO CONTINUE...")
                Config.main()