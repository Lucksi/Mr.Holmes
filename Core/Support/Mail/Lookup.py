# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023-2024 Lucksi <lukege287@gmail.com>
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
    def Spotify(report,email,name):
        print(Font.Color.GREEN + "\n[+]"+ Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Check2", "None").format(email,name))
        url = "https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email={}".format(email)
        req = requests.get(url=url,headers=headers)
        sleep(3)
        if 'errors' in req.text:
            response = Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name))
        else:
            response = Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name)
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name))
        f = open(report,"a")
        f.write("\n"+ response)
        f.close()

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
    def Gmail(report,email,name):
        url = "https://mail.google.com/mail/gxlu?email={}".format(email)
        req = requests.get(url,headers)
        sleep(3)
        if 'Set-Cookie' in req.headers:
            response = Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name))
        else:
            response = Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name)
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name))
        f = open(report,"a")
        f.write("\n"+ response)
        f.close()
    
    @staticmethod
    def Github(report,email,name):
        Image = []
        username = []
        Link = []
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
                f = open(report,"a")
                f.write("\n"+ response)
                f.close()
            elif output == 1:
                response = Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name)
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name) + "\n")
                f = open(report,"a")
                f.write("\n"+ response)
                f.close()
            elif output >1:
                response = Language.Translation.Translate_Language(filename, "Email", "MultipleRes", "None").format(name,(str(output)))
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +  Language.Translation.Translate_Language(filename, "Email", "MultipleRes", "None").format(name,str(output)) + "\n")
                f = open(report,"a")
                f.write("\n"+ response)
                f.close()
            if output == 0:
                pass
            else:
                if output <= 20:
                    output = output
                else:
                    output = 20
            for i in range(output):
                usern = parser["items"][i]["login"]
                link = parser["items"][i]["html_url"]
                profile_pic = parser["items"][i]["avatar_url"]
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER FOUND: {}".format(Font.Color.WHITE + usern + Font.Color.WHITE))
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(Font.Color.WHITE + profile_pic + Font.Color.WHITE))
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}\n".format(Font.Color.WHITE + link + Font.Color.WHITE))
                f = open(report,"a")
                f.write("\nUSER FOUND: {}".format(usern))
                f.write("\nPROFILE-PIC: {}".format(profile_pic))
                f.write("\nLINK: {}\n".format(link))
                Image.append(profile_pic)
                username.append(usern)
                Link.append(link)
                f.close()
                if len(username):
                    json_file = "GUI/Reports/E-Mail/{}/Github.json".format(email)
                    f = open(json_file, "w")
                    f.write('''{
                                "List":[
                                ]
                            }''')
                    f.close()

                    i = 0
                    for image in Image:
                        data2 = {
                            "username": "{}".format(username[i]),
                            "site": "{}".format(Link[i]),
                            "image": "{}".format(image)
                        }
                        with open(json_file, 'r+') as file:
                            file_data = json.load(file)
                            file_data["List"].append(data2)
                            file.seek(0)
                            json.dump(file_data, file, indent=4)
                        i = i +1
                else:
                    pass
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))

    @staticmethod
    def Gravatar(report,email,name):
        Image = []
        username = []
        Link = []
        Names = []
        hashedemail= hashlib.md5(email.encode()).hexdigest()
        print(Font.Color.GREEN + "\n[+]"+ Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Check2", "None").format(email,name))
        url = "https://en.gravatar.com/{}.json".format(hashedemail)
        try:
            req = requests.get(url,headers=headers)
            if "User not found" in req.text:
                response = Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name)
                f = open(report,"a")
                f.write("\n"+ response)
                f.close()
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "FalseRes", "None").format(name))
            else:
                response = Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name)
                f = open(report,"a")
                f.write("\n"+ response)
                f.close()
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "TrueRes", "None").format(name))
                reader = req.text
                converted = json.loads(reader)
                hashid = converted["entry"][0]["hash"]
                user = converted["entry"][0]["preferredUsername"]
                link = converted["entry"][0]["profileUrl"]
                displayname = converted["entry"][0]["displayName"]
                profile_pic = converted["entry"][0]["thumbnailUrl"]
                if "aboutMe" in reader:
                    bio = converted["entry"][0]["aboutMe"]
                else:
                    bio = ""
                if "formatted" in reader:
                    name = converted["entry"][0]["name"]["formatted"]
                else:
                    name = "None"
                if "urls" in reader:
                    urls = converted["entry"][0]["urls"]
                else:
                    urls = "None"
                if "last_profile_edit" in reader:
                    modification = converted["entry"][0]["last_profile_edit"]
                else:
                    modification = "None"
                f = open(report, "a", encoding="utf-8")
                f.write("\nGRAVATAR DATA:\n")
                
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "HASH: {}".format(hashid))
                f.write("HASH: {}\r\n".format(hashid))
                
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USERNAME: {}".format(user))
                f.write("USERNAME: {}\r\n".format(user))
                
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "DISPLAY-NAME: {}".format(displayname))
                f.write("DISPLAY-NAME: {}\r\n".format(displayname))
                
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "NAME: {}".format(name))
                f.write("NAME: {}\r\n".format(name))
                
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "BIO: {}".format(bio))
                f.write("BIO: {}\r\n".format(bio))
                
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "UPADTED ON: {}".format(modification))
                f.write("UPDATED-ON: {}\r\n".format(modification))
                i = 1
                if urls != "None":
                    for url in urls:
                        print(Font.Color.YELLOW + "[V]" + Font.Color.WHITE +  "LINK N°{}: {}".format(i,url["value"]))
                        f.write("LINK N°{}: {}\r\n".format(i,url["value"]))
                        i = i +1
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))
                f.write("PROFILE-PIC: {}\r\n".format(profile_pic))
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-LINK: {}".format(link))
                f.write("PROFILE-LINK: {}\r\n".format(link))
                f.close()
                Image.append(profile_pic)
                username.append(user)
                Link.append(link)
                Names.append(name)
                f.close()
                if len(username):
                    json_file = "GUI/Reports/E-Mail/{}/Gravatar.json".format(email)
                    f = open(json_file, "w")
                    f.write('''{
                                "List":[
                                ]
                            }''')
                    f.close()

                    i = 0
                    for image in Image:
                        data2 = {
                            "username": "{}".format(username[i]),
                            "name": "{}".format(Names[i]),
                            "site": "{}".format(Link[i]),
                            "image": "{}".format(image)
                        }
                        with open(json_file, 'r+') as file:
                            file_data = json.load(file)
                            file_data["List"].append(data2)
                            file.seek(0)
                            json.dump(file_data, file, indent=4)
                        i = i +1
                else:
                    pass
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
        List.Gmail(report,email,"GMAIL/G-SUITE")
        List.Twitter(report,email,"TWITTER")
        List.Spotify(report,email,"SPOTIFY")
        List.Github(report,email,"GITHUB")
        List.Gravatar(report,email,"GRAVATAR")
        List.Imgur(report,email,"IMGUR")
