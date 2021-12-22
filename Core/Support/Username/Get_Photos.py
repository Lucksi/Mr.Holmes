# AUTHOR: Luca Garofalo (Lucksi)
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import os
import requests
from Core.Support import Font
from bs4 import BeautifulSoup as soup
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}


class Downloader:

    @staticmethod
    def Instagram(username, http_proxy, Posts):
        if Posts > 0:
            if Posts <= 12:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      "DOWNLOADING {} INSTAGRAM PHOTO...".format(username))
                range_band = Posts
            else:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      "DOWNLOADING {} FIRST 12 INSTAGRAM PHOTO...".format(username))
                range_band = 12
            folder = "GUI/Reports/Usernames/Profile_pics/{}/Instagram_Photo".format(
                username)
            if os.path.isdir(folder):
                os.rmdir(folder)
            os.mkdir(folder)

            details = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE +
                                "WOULD YOU LIKE TO DOWNLOAD POST-DETAILS?(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            url = "https://www.picuki.com/profile/{}".format(username)
            openurl = requests.get(url, proxies=http_proxy, headers=headers)
            reader = soup(openurl.content, "html.parser")
            profile = reader.find_all("div", class_="photo")
            i = 1
            j = 1
            d = 1
            t = 1
            
            while i <= range_band:
                for image in profile:
                    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                          "DOWNLOAD IMAGE NUMBER:{}...".format(str(i)))
                    profile_pic = image.find("img", class_="post-image")["src"]
                    image = folder + "/Pic_{}.jpg".format(str(i))
                    getter = requests.get(
                        profile_pic, headers=headers, allow_redirects=True)
                    open(image, "wb").write(getter.content)
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                          "DOWNLOAD SUCCESSFULL..")
                    i = i+1

            if details == 1:
                description = reader.find_all("div", class_="photo-info")
                while j <= range_band:
                    for info in description:
                        filename = folder + \
                            "/Post_{}_details.txt".format(str(j))
                        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                              "CHECKING POST {} DETAILS...".format(str(j)))
                        tagged = info.find(
                            "a", href=True, class_="user-nickname mt-6")
                        descr = info.find(
                            "div", class_="photo-description").text
                        location = info.find(
                            "div", class_="photo-location").text
                        print(Font.Color.YELLOW +
                              "[v]" + Font.Color.WHITE + "TAGGED USERS: {}".format(tagged))
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                              "DESCRIPTION: {}".format(descr.strip()))
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                              "LOCATION: {}".format(location.strip()))
                        
                        f = open(filename, "w")
                        f.write("POST DATA:\n")
                        f.write("TAGGED USERS: {}\r\n".format(tagged))
                        f.write("DESCRIPTION: {}\r\n".format(descr.strip()))
                        f.write("LOCATION: {}\r\n".format(location.strip()))
                        f.close()
                        j = j+1
                        sleep(2)

                footer = reader.find_all("div", class_="likes_comments_photo")
                while d <= range_band:
                    for info in footer:
                        filename = folder + \
                            "/Post_{}_details.txt".format(str(d))
                        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                              "CHECKING POST {} LIKES AND COMMENTS...".format(str(d)))
                        likes = info.find("div", class_="likes_photo").text
                        comments = info.find(
                            "div", class_="comments_photo").text
                        time = info.find()
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                              "LIKES: {}".format(likes.strip()))
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                              "COMMENTS: {}".format(comments.strip()))

                        f = open(filename, "a")
                        f.write("LIKES: {}\r\n".format(likes.strip()))
                        f.write("COMMENTS: {}\r\n".format(comments.strip()))
                        f.close()
                        d = d+1
                        sleep(2)

                Time = reader.find_all("div", class_="time")
                while t <= range_band:
                    for info in Time:
                        filename = folder + \
                            "/Post_{}_details.txt".format(str(t))
                        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                              "CHECKING POST {} PUBLISHED TIME ...".format(str(t)))
                        time = info.find("span").text
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                              "POSTED: {}".format(time.strip()))

                        f = open(filename, "a")
                        f.write("POSTED: {}\r\n".format(time.strip()))
                        f.close()
                        t = t+1
                        sleep(2)

                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      "POSTS DETAILS SAVED ON: {}...".format(folder))
            else:
                pass

            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  "IMAGES SAVED ON: {}".format(folder))
        else:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                  "THIS USER HAS NO POST..CANNOT DOWNLOAD PROFILE PICS")