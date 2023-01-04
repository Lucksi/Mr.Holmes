# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2022-2023 Lucksi <lukege287@gmail.com>
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
    def Decode(report):
        if os.path.isfile(report):
            quest = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                            filename, "Decoding", "Decode", "None") +  Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if quest == 1:
                EncodedFile = report.replace(".mh",".txt")
                f = open(report,"r+",encoding="utf-8")
                reader = f.read()
                f.close()
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "DECODING...")
                sleep(3)
                encodingString = reader.encode("utf-8")
                Base64_Byte = base64.b64decode(encodingString)
                FinalString = Base64_Byte.decode("utf-8")
                f = open(EncodedFile,"w+",encoding="utf-8")
                f.write(FinalString)
                f.close()
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "DECODED REPORT:\n{}".format(FinalString))
                os.remove(report)
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "DECODING FINISHED")
            else:
                pass
        else:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "FILE DOES NOT EXIST")

    @staticmethod
    def Encode(report):
        if os.path.isfile(report):
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
                f = open(EncodedFile,"w+",encoding="ascii")
                f.write(FinalString)
                f.close()
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "ENCODED REPORT:\n{}".format(FinalString))
                os.remove(report)
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "ENCODING FINISHED")
            else:
                pass
        else:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "FILE DOES NOT EXIST")
    
    @staticmethod
    def Main(report,setting):
        if setting == "Decode":
           Encoder.Decode(report)
        elif setting == "Encode":
            Encoder.Encode(report)
        else:
            pass