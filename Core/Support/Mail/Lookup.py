# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0 

import json
import requests
from Core.Support import Font
from Core.Support import Language
from Core.Support import Headers
from time import sleep
import hashlib


filename = Language.Translation.Get_Language()
filename

headers = Headers.Get.classic()

class List:

    @staticmethod
    def Twitter(report,email,name):
        print(Font.Color.GREEN + "\n[+]"+ Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Check2", "None").format(email,name))
        url = "https://api.twitter.com/i/users/email_available.json?email={}".format(email)
        sleep(3)
        try:
            req = requests.get(url,headers=headers).text
            parser = json.loads(req)
            output = parser["taken"]
            if output == False:
                response = Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name)
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name))
            elif output == True:
                response = Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name))
            f = open(report,"a")
            f.write("\n"+ response)
            f.close()
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
    
    @staticmethod
    def Github(report,email,name):
        print(Font.Color.GREEN + "\n[+]"+ Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Check2", "None").format(email,name))
        url = "https://api.github.com/search/users?q={}+in:email%22".format(email)
        sleep(3)
        try:
            req = requests.get(url,headers=headers).text
            parser = json.loads(req)
            output = parser["total_count"]
            if output == 0:
                response = Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name)
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name))
            elif output == 1:
                response = Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name))
            elif output >1:
                response = Language.Translation.Translate_Language(filename, "Email", "MultipleRes", "None").format(name,(str(output)))
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +  Language.Translation.Translate_Language(filename, "Email", "MultipleRes", "None").format(name,str(output)))
            f = open(report,"a")
            f.write("\n"+ response)
            f.close()
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))

    @staticmethod
    def Gravatar(report,email,name):
        hashedemail= hashlib.md5(email.encode()).hexdigest()
        print(Font.Color.GREEN + "\n[+]"+ Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Check2", "None").format(email,name))
        url = "https://en.gravatar.com/{}.json".format(hashedemail)
        try:
            req = requests.get(url,headers=headers)
            if "User not found" in req.text:
                response = Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name)
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name))
            else:
                response = Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name))
            f = open(report,"a")
            f.write("\n"+ response)
            f.close()
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))

    @staticmethod
    def Imgur(report,email,name):
        print(Font.Color.GREEN + "\n[+]"+ Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Check2", "None").format(email,name))
        data ={
            "email": email
        }
        url = "https://imgur.com/signin/ajax_email_available"
        sleep(3)
        try:
            req = requests.post(url,headers=headers,data = data).text
            parser = json.loads(req)
            output = parser["data"]["available"]
            if output == True:
                response = Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name)
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name))
            elif output == False:
                response = Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name))
            f = open(report,"a")
            f.write("\n"+ response)
            f.close()
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
     
    @staticmethod
    def Main(report,email):
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Lookup", "None"))
        List.Twitter(report,email,"TWITTER")
        List.Github(report,email,"GITHUB")
        List.Gravatar(report,email,"GRAVATAR")
        List.Imgur(report,email,"IMGUR")
