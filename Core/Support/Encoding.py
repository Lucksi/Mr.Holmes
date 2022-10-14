# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2022 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0 


import base64
from time import sleep
from Core.Support import Font
from Core.Support import Language
import os

filename = Language.Translation.Get_Language()
filename

class Encoder:

    @staticmethod
    def Encode(report):
        quest = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                        filename, "Default", "Encode", "None") +  Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if quest == 1:
            EncodedFile = report.replace(".txt",".mh")
            f = open(report,"r+")
            reader = f.read()
            f.close()
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "ENCODING...")
            sleep(3)
            encodingString = reader.encode("utf-8")
            Base64_Byte = base64.b64encode(encodingString)
            FinalString = Base64_Byte.decode("utf-8")
            f = open(EncodedFile,"w+",encoding="utf-8")
            f.write(FinalString)
            f.close()
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "ENCODED REPORT: {}".format(FinalString))
            Message = FinalString
            Message1 = Message.encode("utf-8")
            Message3 = base64.b64decode(Message1)
            Message4 = Message3.decode("utf-8")
            #print(Message4)
            os.remove(report)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "ENCODING FINISHED")
        else:
            pass