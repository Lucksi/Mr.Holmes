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
                if os.getuid() == 0:
                    os.system("php -S" + host +
                                ":5000 -t Transfer >/dev/null 2>&1 &")
                    Req = True
                  
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
                if (os.name != "nt"):
                    os.system("killall  php > /dev/null 2>&1")
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
