from Core.Support import Font
import os
import getpass
import MrHolmes as holmes

dest = "Configuration"


class Config:

    @staticmethod
    def modify_recipient():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR RECIPIENT EMAIL?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            nomefile = "Recipient.txt"
            if os.path.isfile(nomefile):
                f = open(nomefile, "w")
                recipient = str(input(
                    Font.Color.WHITE + "\nINSERT THE EMAIL-RECIPIENT" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while recipient == "":
                    recipient = str(input(
                        Font.Color.RED + "\n[!]" + Font.Color.WHITE + "INSERT AN EMAIL" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    f.write(recipient)
                    f.close()
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
            nomefile = "Password.txt"
            if os.path.isfile(nomefile):
                f = open(nomefile, "w")
                passw = getpass.getpass(
                    Font.Color.WHITE + "\nINSERT THE PASSWORD-RECIPIENT" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                while passw == "":
                    passw = getpass.getpass(
                        Font.Color.RED + "\n[!]" + Font.Color.WHITE + "INSERT A PASSWORD" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                else:
                    f.write(passw)
                    f.close()
                    print("\nPASSWORD CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_destination():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR DESTINATION-MAIL?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            nomefile = "Destination.txt"
            if os.path.isfile(nomefile):
                f = open(nomefile, "w")
                destination = str(input(
                    Font.Color.WHITE + "\nINSERT THE DESTINATION-MAIL" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while destination == "":
                    destination = str(input(
                        Font.Color.RED + "\n[!]" + Font.Color.WHITE + "INSERT AN EMAIL" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    f.write(destination)
                    f.close()
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
            nomefile = "Port.txt"
            if os.path.isfile(nomefile):
                f = open(nomefile, "w")
                port = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR SERVER-PORT" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while port == "":
                    port = str(input(
                        Font.Color.RED + "\n[!]" + Font.Color.WHITE + "INSERT YOUR SERVER-PORT" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    f.write(port)
                    f.close()
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
            nomefile = "Server.txt"
            if os.path.isfile(nomefile):
                f = open(nomefile, "w")
                server = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR SMTP-SERVER" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while server == "":
                    server = str(input(
                        Font.Color.RED + "\n[!]" + Font.Color.WHITE + "INSERT YOUR SMTP-SERVER" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    f.write(server)
                    f.close()
                    print("\nSERVER CHANGED SUCCESSFULLY")
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
            nomefile = "Update.txt"
            if os.path.isfile(nomefile):
                f = open(nomefile, "w")
                server = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR UPDATE-PATH" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while server == "":
                    server = str(input(
                        Font.Color.RED + "\n[!]" + Font.Color.WHITE + "INSERT YOUR UPDATE-PATH" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    f.write(server)
                    f.close()
                    print("\nPATH CHANGED SUCCESSFULLY")
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
            nomefile = "Pass_Update.txt"
            if os.path.isfile(nomefile):
                f = open(nomefile, "w")
                passw = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR UPDATE-PATH" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while passw == "":
                    passw = str(input(
                        Font.Color.RED + "\n[!]" + Font.Color.WHITE + "INSERT YOUR UPDATE-PATH" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    f.write(passw)
                    f.close()
                    print("\nPASSWORD CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def main():
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            f = open("Banners/Banner5.txt")
            banner = f.read()
            f.close()
            print(Font.Color.GREEN + banner)
            option = "(1)MODIFY-SENDER-MAIL\n(2)MODIFY-DESTINATION-MAIL\n(3)MODIFY-PASSWORD-MAIL\n(4)MODIFY-SMTP-SERVER\n(5)MODIFY-SMTP-PORT\n(6)MODIFY-UPDATE-PASSWORD\n(7)MODIFY-UPDATE-PATH\n(8)MAIN-MENU"
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
                inp = input("PRESS ENTER TO CONTINUE...")
                holmes.Main.main()
