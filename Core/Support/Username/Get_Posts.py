# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0


import os
import requests
import urllib
import json
from Core.Support import Font
from Core.Support import Language
from bs4 import BeautifulSoup as soup
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

LangFile = Language.Translation.Get_Language()
LangFile


class Downloader:

    @staticmethod
    def Instagram(url, username, http_proxy, Posts):
        if Posts > 0:
            if Posts <= 12:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Download_Full").format(username))
                range_band = Posts
            else:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Download_Partial").format(username))
                range_band = 12
            folder = "GUI/Reports/Usernames/Profile_pics/{}/Instagram_Photo".format(
                username)
            if os.path.isdir(folder):
                os.rmdir(folder)
            os.mkdir(folder)

            details = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE +
                                Language.Translation.Translate_Language(LangFile, "Username", "Default", "Details") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            openurl = requests.get(
                url, proxies=http_proxy, headers=headers)
            reader = soup(openurl.content, "html.parser")
            profile = reader.find_all("div", class_="photo")

            i = 1
            j = 1
            d = 1
            t = 1

            while i <= range_band:
                for image in profile:
                    try:
                        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                              Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Download").format(str(i)))
                        profile_pic = image.find(
                            "img", class_="post-image")["src"]
                        image = folder + "/Pic_{}.jpg".format(str(i))
                        getter = requests.get(
                            profile_pic, headers=headers, allow_redirects=True)
                        open(image, "wb").write(getter.content)
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                              "DOWNLOAD SUCCESSFULL..")
                        i = i+1
                    except ConnectionError:
                        print(
                            Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Connection_Error2", "None"))
                        i = i+1
                        continue
                    except Exception as e:
                        print(
                            Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Error", "None"))
                        i = i+1
                        continue

            if details == 1:
                description = reader.find_all("div", class_="photo-info")
                while j <= range_band:
                    for info in description:
                        try:
                            filename = folder + \
                                "/Post_{}_details.txt".format(str(j))
                            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                                  Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Details").format(str(j)))
                            descr = info.find(
                                "div", class_="photo-description").text
                            location = info.find(
                                "div", class_="photo-location").text
                            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                  "DESCRIPTION: {}".format(descr.strip()))
                            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                  "LOCATION: {}".format(location.strip()))
                            f = open(filename, "w", encoding="utf-8")
                            f.write("POST N°{} DATA:\n".format(str(j)))
                            f.write("DESCRIPTION: {}\r\n".format(descr.strip()))
                            f.write("LOCATION: {}\r\n".format(
                                location.strip()))
                            if location.strip() == "":
                                pass
                            else:
                                jsonfile = folder + \
                                    "/Post_{}_GeoData.json".format(str(j))
                                final_loc = location.strip()
                                format_loc = final_loc.replace(" ", "+")
                                req = "https://nominatim.openstreetmap.org/search.php?q={}&format=json".format(
                                    format_loc)
                                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                                      Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "GeoData").format(str(j)))
                                sleep(2)
                                url = urllib.request.urlopen(req)
                                try:
                                    Reader = url.read()
                                    parser = json.loads(Reader)
                                    Lat = parser[0]["lat"]
                                    Lon = parser[0]["lon"]
                                    data = {
                                        "Geolocation": {
                                            "Latitude": Lat,
                                            "Longitude": Lon
                                        }
                                    }
                                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                          "LATITUDE:" + Font.Color.GREEN + " {}".format(Lat))
                                    sleep(2)
                                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                          "LONGITUDE:" + Font.Color.GREEN + " {}".format(Lon))
                                    sleep(2)
                                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                          "GOOGLE MAPS LINK: https://www.google.it/maps/place/{},{}".format(Lat, Lon))
                                    with open(jsonfile, "w", encoding="utf-8") as output:
                                        json.dump(data, output,
                                                  ensure_ascii=False, indent=4)
                                except Exception as e:
                                    print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                                        LangFile, "Username", "Instagram", "NoGeoData"))
                            f.close()
                            j = j+1
                            sleep(2)
                        except ConnectionError:
                            print(Font.Color.RED + "[!]" +
                                  Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Connection_Error2", "None"))
                            j = j+1
                            continue
                        except Exception as e:
                            print(Font.Color.RED + "[!]" +
                                  Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Error", "None"))
                            j = j+1
                            continue

                footer = reader.find_all(
                    "div", class_="likes_comments_photo")
                while d <= range_band:
                    for info in footer:
                        try:
                            filename = folder + \
                                "/Post_{}_details.txt".format(str(d))
                            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                                  Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Likes/Comments").format(str(d)))
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
                            f.write("COMMENTS: {}\r\n".format(
                                comments.strip()))
                            f.close()
                            d = d+1
                            sleep(2)
                        except ConnectionError:
                            print(Font.Color.RED + "[!]" +
                                  Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Connection_Error2", "None"))
                            d = d+1
                            continue
                        except Exception as e:
                            print(Font.Color.RED + "[!]" +
                                  Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Error", "None"))
                            d = d+1
                            continue

                Time = reader.find_all("div", class_="time")
                while t <= range_band:
                    for info in Time:
                        try:
                            filename = folder + \
                                "/Post_{}_details.txt".format(str(t))
                            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                                  Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Data").format(str(t)))
                            time = info.find("span").text
                            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                  "POSTED: {}".format(time.strip()))

                            f = open(filename, "a")
                            f.write("POSTED: {}\r\n".format(time.strip()))
                            f.close()
                            t = t+1
                            sleep(2)
                        except ConnectionError:
                            print(Font.Color.RED + "[!]" +
                                  Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Connection_Error2", "None"))
                            t = t+1
                            continue
                        except Exception as e:
                            print(Font.Color.RED + "[!]" +
                                  Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Error", "None"))
                            t = t+1
                            continue

                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "TotDetails").format(folder))
            else:
                pass

            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Image").format(folder))
        else:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "NoPost"))
