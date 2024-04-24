# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2022-2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import requests
import json
from bs4 import BeautifulSoup as soup
from Core.Support import Font
from Core.Support.Username import Scraper
from Core.Support import Headers
from Core.Support import Language
from time import sleep

filename = Language.Translation.Get_Language()
filename

headers = Headers.Get.classic()


class Search:
   @staticmethod
   def Instagram(report, username, http_proxy, InstagramParams, PostLocations, PostGpsCoordinates, imagefold, username2,fold):
        List = []
        Links = []
        Pics = []
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCANNING FOR {} INSTAGRAM RESULTS...".format(username))
        url = "https://www.picuki.com/search/{}".format(username)
        req = requests.get(url, timeout=None, proxies=http_proxy, headers=headers)
        sleep(4)
        try:
            req = requests.get(url, timeout=None, proxies=None, headers=headers)
            sleep(4)
            if req.status_code == 200:
                reader = soup(req.content, "html.parser")
                users = reader.find_all("div", class_="profile-result")
                i = 1
                f = open(report, "a",encoding="utf-8")
                f.write(
                    "\n\n--------------------------------\nSHOWING INSTAGRAM RESULTS FOR: {}\n".format(username))
                for user in users:
                    if i <= 20:
                        usern = user.find("div",class_="result-username").text.replace("@","")
                        pic = user.find_all("div",class_="result-ava")
                        for image in pic:
                            profilepic = image.find("img")["src"]
                            Pics.append(profilepic) 
                        link = "https://instagram.com/{}".format(usern)
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER FOUND: {}".format(
                            Font.Color.GREEN + usern + Font.Color.WHITE))
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(
                            Font.Color.GREEN + profilepic + Font.Color.WHITE))
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}\n".format(
                            Font.Color.GREEN + link + Font.Color.WHITE))
                        List.append(usern)
                        Links.append(link)
                        f.write("\nUSER FOUND: {}".format(usern))
                        f.write("\nPROFILE-PIC FOUND: {}".format(profilepic))
                        f.write("\nLINK: {}\n".format(link))
                        i = i+1
                    else:
                        break
                f.close()
        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
            pass
        j = 1
        print(Font.Color.GREEN + "[+]" +
                    Font.Color.WHITE + "TOTAL USERNAMES FOUND")
        if len(List):
            for Names in List:
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "USERNAME N°{}: {}".format(j, Names))
                j = j+1
            if fold == "People":
                json_file = "GUI/Reports/People/{}/Insta_Link.json".format(username2)
            else:
                if username2 != "None":
                    json_file = "GUI/Reports/{}/{}/InstaName_Link.json".format(fold,username2)
                else:
                    json_file = "GUI/Reports/{}/{}/Insta_Link.json".format(fold,username)
            f = open(json_file, "w")
            f.write('''{
                        "List":[
                        ]
                    }''')
            f.close()

            i = 0
            for image in Pics:
                data2 = {
                    "username": "{}".format(List[i]),
                    "site": "{}".format(Links[i]),
                    "image": "{}".format(image)
                }
                with open(json_file, 'r+') as file:
                    file_data = json.load(file)
                    file_data["List"].append(data2)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
                i = i +1
            
            if fold == "People":
                opt = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Scraper") +
                                Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if opt == 1:
                    check = str(input(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "INSERT THE USERNANE TO CHECK\n\n" +
                                    Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if check not in List:
                        pass
                    else:
                        if os.path.isdir(imagefold):
                            pass
                        else:
                            os.mkdir(imagefold)
                        Scraper.info.Instagram(report, check, http_proxy, InstagramParams,
                                            PostLocations, PostGpsCoordinates, "People", username2)
        else:
            print(Font.Color.RED + "\n[!]" +
                  Font.Color.WHITE + "NO USER HAS BEEN FOUND")

   @staticmethod
   def Twitter(report, username, http_proxy, TwitterParams, imagefold,username2,fold):
        headers = Headers.Get.Twitter()
        List = []
        Links = []
        Pics = []
        Names2 = []
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCANNING FOR {} TWITTER RESULTS...".format(username))
        url = "https://nitter.net/search?f=users&q={}".format(username)
        sleep(4)
        try:
            req = requests.get(url, timeout=None, proxies=http_proxy, headers=headers, allow_redirects=True)
            if req.status_code == 200:
                reader = soup(req.content, "html.parser")
                users = reader.find_all("div", class_="timeline-item")
                i = 1
                f = open(report, "a",encoding="utf-8")
                f.write(
                    "--------------------------------\nSHOWING TWITTER RESULTS FOR: {}\n".format(username))
                for user in users:
                    if i <= 20:
                        usern = user.find(
                            "a", class_="username").text.replace("@", "")
                        pic = user.find("img",class_="avatar round")["src"]
                        profilepic = "https://nitter.net" + pic
                        Pics.append(profilepic)
                        link = "https://twitter.com/{}".format(usern)
                        bio = user.find(
                            "div", class_="tweet-content media-body").text
                        full_name = user.find(
                            "a", class_="fullname").text
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER FOUND: {}".format(
                            Font.Color.GREEN + usern + Font.Color.WHITE))
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "NAME FOUND: {}".format(
                            Font.Color.GREEN + full_name + Font.Color.WHITE))
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "BIO: {}".format(
                            Font.Color.GREEN + bio + Font.Color.WHITE))
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(
                            Font.Color.GREEN + profilepic + Font.Color.WHITE))
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}\n".format(
                            Font.Color.GREEN + link + Font.Color.WHITE))
                        List.append(usern)
                        Links.append(link)
                        Names2.append(full_name)
                        f.write("\nUSER FOUND: {}".format(usern))
                        f.write("\nFULL-NAME: {}\n".format(full_name))
                        f.write("\nBIO: {}\n".format(bio))
                        f.write("\nPROFILE-PIC FOUND: {}".format(profilepic))
                        f.write("\nLINK: {}\n".format(link))
                        i = i+1
                    else:
                        break
                f.close()
                print(Font.Color.GREEN + "[+]" +
                    Font.Color.WHITE + "TOTAL USERNAMES FOUND")
            else:
                print("ERROR")
        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
            pass
        
        j = 1
        if len(List):
            for Names in List:
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "USERNAME N°{}: {}".format(j, Names))
                j = j+1
            if fold == "People":
                json_file = "GUI/Reports/People/{}/Twitter_Link.json".format(username2)
            else:
                if username2 != "None":
                    json_file = "GUI/Reports/{}/{}/TwitterName_Link.json".format(fold,username2)
                else:
                    json_file = "GUI/Reports/{}/{}/Twitter_Link.json".format(fold,username)
            f = open(json_file, "w")
            f.write('''{
                        "List":[

                        ]
                    }''')
            f.close()

            i = 0
            for image in Pics:
                data2 = {
                    "username": "{}".format(List[i]),
                    "full-name": "{}".format(Names2[i]),
                    "site": "{}".format(Links[i]),
                    "image": "{}".format(image)
                }
                with open(json_file, 'r+') as file:
                    file_data = json.load(file)
                    file_data["List"].append(data2)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
                i = i +1
            
            if fold == "People":
                opt = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Scraper") +
                                Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if opt == 1:
                    check = str(input(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "INSERT THE USERNANE TO CHECK\n\n" +
                                    Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if check not in List:
                        pass
                    else:
                        if os.path.isdir(imagefold):
                            pass
                        else:
                            os.mkdir(imagefold)
                        Scraper.info.Twitter(report, check, http_proxy, TwitterParams,
                                            "People", username2)
        else:
            print(print(Font.Color.RED +
                  "\n[!]" + Font.Color.WHITE + "NO USER HAS BEEN FOUND"))

   @staticmethod
   def TikTok(report, username, http_proxy, imagefold, username2,fold):
        List = []
        Links = []
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCANNING FOR {} TIKTOK RESULTS...".format(username))
        url = "https://urlebird.com/search/?q={}".format(username)
        sleep(4)
        try:
            req = requests.get(url, timeout=None, proxies=http_proxy, headers=headers)
            if req.status_code == 200:
                reader = soup(req.content, "html.parser")
                users = reader.find_all("div", class_="info text-truncate")
                i = 1
                f = open(report, "a",encoding="utf-8")
                f.write(
                    "--------------------------------\nSHOWING TIKTOK RESULTS FOR: {}\n".format(username))
                for user in users:
                    if i <= 20:
                        usern = user.find(
                            "a", class_="uri").text
                        link = "https://tiktok.com/{}".format(usern)
                        followers = user.find(
                            "span", class_="followers").text
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER FOUND: {}".format(
                            Font.Color.GREEN + usern.replace("@","") + Font.Color.WHITE))
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FOLLOWERS: {}".format(
                            Font.Color.GREEN + followers + Font.Color.WHITE))
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}\n".format(
                            Font.Color.GREEN + link + Font.Color.WHITE))
                        List.append(usern.replace("@",""))
                        Links.append(link)
                        f.write("\nUSER FOUND: {}".format(usern))
                        f.write("\nFOLLOWERS: {}\n".format(followers))
                        f.write("\nLINK: {}\n".format(link))
                        i = i+1
                    else:
                        break
                f.close()
                print(Font.Color.GREEN + "[+]" +
                    Font.Color.WHITE + "TOTAL USERNAMES FOUND")
            else:
                print("ERROR")
        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
            pass
        
        j = 1
        if len(List):
            for Names in List:
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "USERNAME N°{}: {}".format(j, Names))
                j = j+1
                if fold == "People":
                    json_file = "GUI/Reports/People/{}/TikTok_Link.json".format(username2)
                else:
                    if username2 != "None":
                        json_file = "GUI/Reports/{}/{}/TikTokName_Link.json".format(fold,username2)
                    else:
                        json_file = "GUI/Reports/{}/{}/TikTok_Link.json".format(fold,username)
            f = open(json_file, "w")
            f.write('''{
                        "List":[

                        ]
                    }''')
            f.close()
            i = 0
            for link in Links:
                data = {
                    "username": "{}".format(List[i]),
                    "site": "{}".format(link)
                }
                with open(json_file, 'r+') as file:
                    file_data = json.load(file)
                    file_data["List"].append(data)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
            
            if fold == "People":
                opt = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Scraper") +
                                Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if opt == 1:
                    check = str(input(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "INSERT THE USERNANE TO CHECK\n\n" +
                                    Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if check not in List:
                        pass
                    else:
                        check = check.replace("@", "")
                        if os.path.isdir(imagefold):
                            pass
                        else:
                            os.mkdir(imagefold)
                        Scraper.info.TikTok(report, check, http_proxy,
                                            "People", username2)
        else:
            print(Font.Color.RED + "\n[!]" +
                  Font.Color.WHITE + "NO USER HAS BEEN FOUND")
   @staticmethod
   def Github(report, username, http_proxy,imagefold, username2,fold):
        List = []
        Links = []
        Pics = []
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCANNING FOR {} GITHUB RESULTS...".format(username))
        url = "https://api.github.com/search/users?q={}+in:text".format(username)
        req = requests.get(url, timeout=None, proxies=http_proxy, headers=headers)
        sleep(4)
        i = 0
        req = requests.get(url,headers=headers).text
        f = open(report, "a",encoding="utf-8")
        f.write( "--------------------------------\nSHOWING GITHUB RESULTS FOR: {}\n".format(username))
        try:
            parser = json.loads(req)
            output = parser["total_count"]
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
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER FOUND: {}".format(Font.Color.GREEN + usern + Font.Color.WHITE))
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(Font.Color.GREEN + profile_pic + Font.Color.WHITE))
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}\n".format(Font.Color.GREEN + link + Font.Color.WHITE))
                    List.append(usern)
                    Links.append(link)
                    Pics.append(profile_pic)
                    f.write("\nUSER FOUND: {}".format(usern))
                    f.write("\nPROFILE-PIC: {}".format(profile_pic))
                    f.write("\nLINK: {}\n".format(link))
        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
            pass
        j = 1
        if len(List):
            for Names in List:
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "USERNAME N°{}: {}".format(j, Names))
                j = j+1
            if fold == "People":
                json_file = "GUI/Reports/People/{}/Github_Link.json".format(username2)
            else:
                if username2 != "None":
                    json_file = "GUI/Reports/{}/{}/GithubName_Link.json".format(fold,username2)
                else:
                    json_file = "GUI/Reports/{}/{}/Github_Link.json".format(fold,username)
            f = open(json_file, "w")
            f.write('''{
                        "List":[

                        ]
                    }''')
            f.close()

            i = 0
            for image in Pics:
                data2 = {
                    "username":"{}".format(List[i]),
                    "site": "{}".format(Links[i]),
                    "image": "{}".format(image)
                }
                with open(json_file, 'r+') as file:
                    file_data = json.load(file)
                    file_data["List"].append(data2)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
                i = i +1
            if fold == "People":
                opt = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Scraper") +
                                Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if opt == 1:
                    check = str(input(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "INSERT THE USERNANE TO CHECK\n\n" +
                                    Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if check not in List:
                        pass
                    else:
                        check = check.replace("@", "")
                        if os.path.isdir(imagefold):
                            pass
                        else:
                            os.mkdir(imagefold)
                        Scraper.info.Github(report, check, http_proxy,
                                            "People", username2)
        else:
            print(print(Font.Color.RED +
                  "\n[!]" + Font.Color.WHITE + "NO USER HAS BEEN FOUND"))    
