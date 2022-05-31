# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0


import os
import requests
import urllib
import json
import shutil
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
            folder = "GUI/Reports/Usernames/{}/Profile_pics/Instagram_Posts".format(
                username)
            if os.path.isdir(folder):
                keep = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE +
                            Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "FoldFound") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if keep == 1:
                    shutil.rmtree(folder)
                    os.mkdir(folder)
                else:
                    pass
            else:
                os.mkdir(folder)
            details = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE +
                                Language.Translation.Translate_Language(LangFile, "Username", "Default", "Details") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            openurl = requests.get(
                url, proxies=http_proxy, headers=headers, allow_redirects=True)
            reader = soup(openurl.content, "html.parser")
            profile = reader.find_all("div", class_="photo")

            i = 1
            j = 1
            d = 1
            t = 1
            arr_name = []

            while i <= range_band:
                for image in profile:
                    try:
                        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                              Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Download").format(str(i)))
                        profile_pic = image.find(
                            "img", class_="post-image")["src"]
                        name = image.find("a")["href"].replace(
                            "https://www.picuki.com/media/", "")
                        arr_name.append(name)
                        print(
                            Font.Color.GREEN + "[+]" + Font.Color.WHITE + "POST ID: {}".format(name))
                        image = folder + "/{}.jpg".format(name)
                        print(Font.Color.BLUE + "[I]" + Font.Color.WHITE +
                            Language.Translation.Translate_Language(LangFile, "Username", "Default", "Check").format(name))
                        sleep(2)
                        if os.path.exists(image):
                            print(
                                Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Username", "Default", "CheckTrue"))
                            sleep(2)
                        else:
                            print(
                                Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Username", "Default", "CheckFalse"))
                            getter = requests.get(
                                profile_pic, headers=headers, allow_redirects=True)
                            open(image, "wb").write(getter.content)
                            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                  Language.Translation.Translate_Language(LangFile,"Username","Default","Success"))
                        i = i+1
                    except ConnectionError:
                        print(
                            Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Connection_Error2", "None"))
                        i = i+1
                        continue
                    except Exception as e:
                        print(
                            Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Error", "None") + str(e))
                        i = i+1
                        continue

            if details == 1:
                description = reader.find_all("div", class_="photo-info")
                while j <= range_band:
                    for info in description:
                        try:
                            data_fold = folder + "/" + arr_name[j-1]
                            if os.path.isdir(data_fold):
                                shutil.rmtree(data_fold)

                            os.mkdir(data_fold)
                            filename = data_fold + \
                                "/{}.txt".format(arr_name[j-1])
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
                            f.write("POST ID {} DATA:\n".format(str(name)))
                            f.write("DESCRIPTION: {}\r\n".format(descr.strip()))
                            f.write("LOCATION: {}\r\n".format(
                                    location.strip()))
                            if location.strip() == "":
                                pass
                            else:
                                jsonfile = data_fold + \
                                    "/{}.json".format(arr_name[j-1])
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
                                  Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Error", "None") + str(e))
                            j = j+1
                            continue
                footer = reader.find_all(
                    "div", class_="likes_comments_photo")
                while d <= range_band:
                    for info in footer:
                        try:
                            data_fold = folder + "/" + arr_name[d-1]
                            filename = data_fold + \
                                "/{}.txt".format(arr_name[d-1])
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
                            data_fold = folder + "/" + arr_name[t-1]
                            filename = data_fold + \
                                "/{}.txt".format(arr_name[t-1])
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
                else:
                    pass
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "Default", "TotDetails").format(folder))
            else:
                pass

            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(LangFile, "Username", "Default", "Image").format(folder))
        else:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(LangFile, "Username", "Default", "NoPost"))

    @staticmethod
    def Twitter(url, username, http_proxy, Posts):
        url = url + "/search"
        if Posts > 0:
            if Posts <= 12:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "Download_Full").format(username))
                range_band = Posts
            else:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "Download_Partial").format(username))
                range_band = 12
            folder = "GUI/Reports/Usernames/{}/Profile_pics/Twitter_Posts".format(
                username)
            if os.path.isdir(folder):
                shutil.rmtree(folder)
            os.mkdir(folder)
            openurl = requests.get(
                url, proxies=http_proxy, headers=headers, allow_redirects=True)

            reader = soup(openurl.content, "html.parser")
            i = 1
            j = 1
            profile = reader.find_all("div", class_="timeline-item")

            for info in profile:
                try:
                    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "Details").format(str(i)))
                    image_try = info.find("a", class_="still-image")
                    sleep(2)
                    if image_try != None:
                        post = info.find(
                            "a", class_="still-image")["href"]
                        print(
                            Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "Yes_Image").format(str(j)))
                        profile_pic = url.replace(
                            username+"/search", "") + post.replace("/pic/", "pic/")
                        image = folder + "/Pic_{}.jpg".format(str(j))
                        getter = requests.get(
                            profile_pic, headers=headers, allow_redirects=False)
                        try:
                            open(image, "wb").write(getter.content)
                            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                  Language.Translation.Translate_Language(LangFile,"Username","Default","Success"))
                            j = j+1
                            sleep(2)
                        except ConnectionError:
                            print(Font.Color.RED + "[!]" +
                                  Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Connection_Error2", "None"))
                            continue
                        except Exception as e:
                            print(Font.Color.RED + "[!]" +
                                  Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Error", "None"))
                            continue
                    else:
                        poster_pics = info.find_all(
                            "div", class_="card-image")
                        if poster_pics != None:
                            for data in poster_pics:
                                print(
                                    Font.Color.YELLOW + "[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "Yes_Image").format(str(j)))
                                post = data.find("img")["src"]
                                profile_pic = url.replace(
                                    username + "/search", "") + post.replace("/pic/", "pic/")
                                image = folder + \
                                    "/Pic_{}.jpg".format(str(j))
                                getter = requests.get(
                                    profile_pic, headers=headers, allow_redirects=False)
                                try:
                                    open(image, "wb").write(getter.content)
                                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                          "DOWNLOAD SUCCESSFULL..")
                                    j = j+1
                                    sleep(2)
                                except ConnectionError:
                                    print(Font.Color.RED + "[!]" +
                                          Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Connection_Error2", "None"))
                                    continue
                                except Exception as e:
                                    print(Font.Color.RED + "[!]" +
                                          Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Error", "None"))
                                    continue
                        else:
                            print(Font.Color.RED +
                                  "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "No_Image"))
                    text = info.find(
                        "div", class_="tweet-content media-body").text
                    if text:
                        desc = info.find(
                            "div", class_="tweet-content media-body").text
                        print(
                            Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "DESCRIPTION: {}".format(desc))
                    else:
                        print(Font.Color.RED +
                              "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "No_Desc"))
                    footer = info.find_all("span", class_="tweet-stat")
                    comment = footer[0].get_text()
                    likes = footer[1].get_text()
                    retweet = footer[2].get_text()
                    quote = footer[3].get_text()
                    print(
                        Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "COMMENTS: {}".format(comment))
                    print(Font.Color.YELLOW +
                          "[v]" + Font.Color.WHITE + "LIKES: {}".format(likes))
                    print(
                        Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "RETWEETS: {}".format(retweet))
                    print(Font.Color.YELLOW +
                          "[v]" + Font.Color.WHITE + "QUOTES: {}".format(quote))
                    date = info.find("span", class_="tweet-date").text
                    print(Font.Color.YELLOW +
                          "[v]" + Font.Color.WHITE + "POSTED ON: {}".format(date))
                    data_fold = folder + "/" + "Pic_{}".format(str(i))
                    os.mkdir(data_fold)
                    filename = data_fold + \
                        "/Post_{}_details.txt".format(str(i))
                    f = open(filename, "w", encoding="utf-8")
                    f.write("POST N°{} DATA:\n".format(str(i)))
                    f.write("DESCRIPTION: {}\r\n".format(text))
                    f.write("COMMENTS: {}\r\n".format(comment))
                    f.write("LIKES: {}\r\n".format(likes))
                    f.write("RETWEETS: {}\r\n".format(retweet))
                    f.write("QUOTES: {}\r\n".format(quote))
                    f.write("POSTED ON: {}\r\n".format(date))
                    i = i+1
                    sleep(2)
                    if i == range_band + 1:
                        f = open(data_fold + "Max_Counter.txt", "w")
                        f.write("{}".format(str(i)))
                        f.close()
                        break
                except ConnectionError:
                    print(Font.Color.RED + "[!]" +
                          Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Connection_Error2", "None"))
                    i = i+1
                    continue
                except Exception as e:
                    print(Font.Color.RED + "[!]" +
                          Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Error", "None") + str(e))
                    i = i+1
                    continue
        else:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(LangFile, "Username", "Default", "NoPost"))
