# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2022 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import requests
from bs4 import BeautifulSoup as soup
from Core.Support import Font
from Core.Support.Username import Scraper
from Core.Support import Language
from time import sleep


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

filename = Language.Translation.Get_Language()
filename 

class Search:

    @staticmethod
    def Instagram(report, username, http_proxy, InstagramParams, PostLocations, PostGpsCoordinates, imagefold):
        List = []
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCANNING FOR {} INSTAGRAM RESULTS...".format(username))
        url = "https://www.picuki.com/search/{}".format(username)
        req = requests.get(url, timeout=15, proxies=None, headers=headers)
        sleep(4)
        if req.status_code == 200:
            reader = soup(req.content, "html.parser")
            users = reader.find_all("div", class_="profile-result")
            i = 1
            f = open(report, "a")
            f.write("\n\n--------------------------------\nSHOWING INSTAGRAM RESULTS FOR: {}\n".format(username))
            for user in users:
                if i <= 20:
                    usern = user.find(
                        "div", class_="result-username").text.replace("@", "")
                    link = "https://instagram.com/{}".format(usern)
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER FOUND: {}".format(
                        Font.Color.GREEN + usern + Font.Color.WHITE))
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}\n".format(
                        Font.Color.GREEN + link + Font.Color.WHITE))
                    List.append(usern)
                    f.write("\nUSER FOUND: {}".format(usern))
                    f.write("\nLINK: {}\n".format(link))
                    i = i+1
                else:
                    break
            f.close()
            print(Font.Color.GREEN + "[+]" +
                  Font.Color.WHITE + "TOTAL USERNAMES FOUND")

        else:
            print("ERROR")
        j = 1
        if len(List):
            for Names in List:
                print(Font.Color.YELLOW +
                    "[v]" + Font.Color.WHITE + "USERNAME N°{}: {}".format(j, Names))
                j = j+1
            opt = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO SCRAPE DATA(1)YES(2)NO\n\n" +
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
                                        PostLocations, PostGpsCoordinates, "People", username)
        else:
             print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "NO USER HAS BEEN FOUND")
    
    @staticmethod
    def Twitter(report, username, http_proxy, TwitterParams,imagefold):
        List = []
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCANNING FOR {} TWITTER RESULTS...".format(username))
        url = "https://nitter.net/search?f=users&q={}".format(username)
        req = requests.get(url, timeout=15, proxies=None, headers=headers)
        sleep(4)
        if req.status_code == 200:
            reader = soup(req.content, "html.parser")
            users = reader.find_all("div", class_="timeline-item")
            i = 1
            f = open(report, "a")
            f.write("--------------------------------\nSHOWING TWITTER RESULTS FOR: {}\n".format(username))
            for user in users:
                if i <= 20:
                    usern = user.find(
                        "a", class_="username").text.replace("@", "")
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
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}\n".format(
                        Font.Color.GREEN + link + Font.Color.WHITE))
                    List.append(usern)
                    f.write("\nUSER FOUND: {}".format(usern))
                    f.write("\nFULL-NAME: {}\n".format(full_name))
                    f.write("\nBIO: {}\n".format(bio))
                    f.write("\nLINK: {}\n".format(link))
                    i = i+1
                else:
                    break
            f.close()
            print(Font.Color.GREEN + "[+]" +
                  Font.Color.WHITE + "TOTAL USERNAMES FOUND")
        else:
            print("ERROR")
        j = 1
        if len(List):
            for Names in List:
                print(Font.Color.YELLOW +
                    "[v]" + Font.Color.WHITE + "USERNAME N°{}: {}".format(j, Names))
                j = j+1
            opt = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO SCRAPE DATA(1)YES(2)NO\n\n" +
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
                                        "People", username)
        else:
            print( print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "NO USER HAS BEEN FOUND"))

    @staticmethod
    def TikTok(report, username, http_proxy,imagefold):
        List = []
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCANNING FOR {} TIKTOK RESULTS...".format(username))
        url = "https://urlebird.com/search/?q={}".format(username)
        req = requests.get(url, timeout=15, proxies=None, headers=headers)
        sleep(4)
        if req.status_code == 200:
            reader = soup(req.content, "html.parser")
            users = reader.find_all("div", class_="info text-truncate")
            i = 1
            f = open(report, "a")
            f.write("--------------------------------\nSHOWING TIKTOK RESULTS FOR: {}\n".format(username))
            for user in users:
                if i <= 20:
                    usern = user.find(
                        "a", class_="uri").text
                    link = "https://tiktok.com/{}".format(usern)
                    followers = user.find(
                        "span", class_="followers").text
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER FOUND: {}".format(
                        Font.Color.GREEN + usern + Font.Color.WHITE))
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FOLLOWERS: {}".format(
                        Font.Color.GREEN + followers + Font.Color.WHITE))
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}\n".format(
                        Font.Color.GREEN + link + Font.Color.WHITE))
                    List.append(usern)
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
        j = 1
        if len(List):
            for Names in List:
                print(Font.Color.YELLOW +
                    "[v]" + Font.Color.WHITE + "USERNAME N°{}: {}".format(j, Names))
                j = j+1
            opt = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO SCRAPE DATA(1)YES(2)NO\n\n" +
                            Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if opt == 1:
                check = str(input(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "INSERT THE USERNANE TO CHECK\n\n" +
                                Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if check not in List:
                    pass
                else:
                    check = check.replace("@","")
                    if os.path.isdir(imagefold):
                        pass
                    else:
                        os.mkdir(imagefold)
                    Scraper.info.TikTok(report, check, http_proxy,
                                        "People", username)
        else:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "NO USER HAS BEEN FOUND")