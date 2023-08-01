# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import base64
import socket
from time import sleep
from Core.Support import Font
from Core.Support import Language
import pyqrcode
import shutil

filename = Language.Translation.Get_Language()
filename

class Transfer:

    @staticmethod
    def File(report,name,extension):
        if os.path.exists(report):
            new = "Transfer/{}{}".format(name,extension)
            shutil.copyfile(report,new)
            temp = "Transfer/file.txt"
            f = open(temp,"w")
            f.write(name + extension)
            f.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 1))
            host = s.getsockname()[0]
            if (os.name != "nt"):
                wan = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Transfer","Wan","None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if wan == 1:
                    wanToken = "True"
                    passw = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Transfer","Pwd","None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if passw == 1:
                        password = str(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Transfer","PwdIns","None")  + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                        while password == "" or len(password) < 8:
                            password = str(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename,"Transfer","PwdIns","None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                        encodingString = password.encode("utf-8")
                        Base64_Byte = base64.b64encode(encodingString)
                        passwordEncoded = Base64_Byte.decode("utf-8")
                        print(Font.Color.GREEN + "\n[+]"+ Font.Color.WHITE + "ENCODED PASSCODE: {}".format(Font.Color.GREEN + passwordEncoded + Font.Color.WHITE))
                        f = open("Transfer/Logpass.txt","w+",encoding="ascii")
                        f.write(passwordEncoded)
                        f.close()
                else:
                    wanToken = "False"
            if (os.name != "nt"):
                if os.getuid() == 0:
                    os.system("php -S" + host +
                                ":5000 -t Transfer >/dev/null 2>&1 &")
                    Req = True
                    if wan == 1:
                        os.system("php -S 127.0.0.1:5000 -t Transfer >/dev/null 2>&1 &")
                        wanop = os.popen("Core/Support/Tunnel/Starter.sh 5000")
                        wanlink = str(wanop.read()).replace(", proto :","")
                        link = wanlink
                        if link == "":
                            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "SOMETHING WENT WRONG CANNOT FIND TUNNEL LINK")
                            wan = 2
                            link = "http://" + host +":5000"
                    else:
                        link = "http://" + host +":5000"
                else:
                    Req = False
        
            else:
                os.system("START /B php -S " + host +
                            ":5000 -t Transfer 2>NUL >NUL")
                Req = True

            if Req:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                        filename, "Transfer", "Generation", "None"))
                sleep(3)
                if wan == 1:
                    url = pyqrcode.create(link,version=9)
                    url.eps('QRCodes/QR.png', scale=10)
                else:
                    url = pyqrcode.create(link,version=4)
                    url.eps('QRCodes/QR.png', scale=8)
                print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                        filename, "Transfer", "Location", "None"))
                print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                    Language.Translation.Translate_Language(filename, "Database", "Link", "None").replace("DATABASE","FILE-TRANSFER") + "{}".format(Font.Color.GREEN + link + Font.Color.WHITE))
                inp = input(Font.Color.WHITE + Language.Translation.Translate_Language(
                    filename, "Database", "Quit", "None"))
                os.remove(new)
                os.remove(temp)
                os.remove("QRCodes/QR.png")
                if wanToken == "True":
                    if os.path.exists("Transfer/Logpass.txt"):
                        os.remove("Transfer/Logpass.txt")
                if (os.name != "nt"):
                    os.system("killall  php > /dev/null 2>&1")
                    if wan == 1:
                        os.system("killall ngrok > /dev/null 2>&1")
                else:
                    os.system("taskkill /F /IM php.exe 2>NUL >NUL")
                print(Font.Color.BLUE + "\n[I]" +
                    Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Database", "Stop", "None").replace("DATABASE","FILE-TRANSFER"))
                sleep(2)
            else:
                 print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Database", "NoRoot", "None").replace("DATABASE","FILE-TRANSFER"))
        else:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE DOES NOT EXIST")
