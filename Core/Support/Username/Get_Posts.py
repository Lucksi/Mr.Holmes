# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import requests
import urllib
import json
import shutil
from Core.Support import Font
from Core.Support import Language
from Core.Support import Headers
from bs4 import BeautifulSoup as soup
from time import sleep
from Core.Support import Map

headers = Headers.Get.classic()

LangFile = Language.Translation.Get_Language()
LangFile


class Downloader:

    @staticmethod
    def checkFile(filename,type):
        with open(filename,"rb") as check:
            content = check.read()
            if len(content):
                if type == "Image":
                    print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile,"Username","Default","PostImg").format(len(content)))
                else:
                     print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile,"Username","Default","PostVid").format(len(content)))
            else:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile,"Default","Error","None"))
    
    @staticmethod
    def InsertToFile(json_file, Tagged, Link, Type):
        if os.path.exists(json_file):
            exist = "True"
            pass
        else:
            f = open(json_file, "w")
            f.write('''{
                        "List":[

                        ]
                    }''')
            f.close()
            exist = "False"
        opener = open(json_file, "r")
        reader = json.load(opener)
        v = 0
        try:
            for Parameter in Tagged:
                if exist == "True":
                    for Data in reader:
                        ParamIn = reader[Data][v]["Name"]
                        if ParamIn == Parameter:
                            Ok = "False"
                        else:
                            Ok = "True"
                        v = v+1
                else:
                    Ok = "True"
                if Ok == "True":
                    if Type == "TaggedLink":
                        data = {
                            "Name": "None",
                            "Link": "{}".format(Parameter)
                        }
                    else:
                        data = {
                            "Name": "{}".format(Parameter),
                            "Link": "{}{}".format(Link, Parameter)
                        }
                    with open(json_file, 'r+') as file:
                        file_data = json.load(file)
                        file_data["List"].append(data)
                        file.seek(0)
                        json.dump(file_data, file, indent=4)
                else:
                    pass
        except Exception as e:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "A ERROR OCCURRED {}".format(str(e)))

    @staticmethod
    def Instagram(url, username, http_proxy, Posts, PostLocations, PostGpsCoordinates, Opt, name2):
        if Posts > 0:
            if Posts <= 12:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Download_Full").format(username))
                range_band = Posts
            else:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Download_Partial").format(username))
                range_band = 12
            folder = "GUI/Reports/{}/{}/Profile_pics/Instagram_Posts".format(
                Opt, name2)
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
            TaggedUser = []
            TaggedHashtag = []
            TaggedLink = []
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
                              Language.Translation.Translate_Language(LangFile, "Username", "Default", "Check").format(name + ".jpg"))
                        sleep(2)
                        if os.path.exists(image):
                            print(
                                Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Username", "Default", "CheckTrue"))
                            sleep(2)
                        else:
                            print(
                                Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Username", "Default", "CheckFalse"))
                            getter = requests.get(
                                profile_pic, headers=headers, allow_redirects=False)
                            open(image, "wb").write(getter.content)
                            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                  Language.Translation.Translate_Language(LangFile, "Username", "Default", "Success"))
                            Downloader.checkFile(image,"Image")
                            sleep(5)
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
                            TempTag = []
                            TempHash = []
                            TempLink = []
                            os.mkdir(data_fold)
                            filename = data_fold + \
                                "/{}.txt".format(arr_name[j-1])
                            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                                  Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Details").format(str(j)))
                            descr = info.find(
                                "div", class_="photo-description").text
                            if "#" in descr:
                                count = descr.count("#")
                                text = str(descr.split("#", 1)[1])
                                """if " " in text or "\n" in text:
                                    text = text.split("\n",1)[-1]"""
                                text2 = text.split("#")
                                for tag in text2:
                                    if "\n" in tag:
                                        tag = tag.split("\n", 1)[0]
                                    if " " in tag:
                                        tag = tag.split(" ", 1)[0]
                                    if "https" in text2 or "http" in text2:
                                        TempLink.append(tag.replace("\n", ""))
                                        if tag in TaggedLink:
                                            pass
                                        else:
                                            TaggedLink.append(
                                                tag.replace("\n", ""))
                                    else:
                                        TempHash.append("#" +
                                                        tag.replace("\n", ""))
                                        if tag in TaggedHashtag:
                                            pass
                                        else:
                                            TaggedHashtag.append(
                                                tag.replace("\n", ""))
                            tagg = info.find_all("u")
                            for user in tagg:
                                tagged = user.text.replace("@", "")
                                TempTag.append(tagged)
                                if tagged in TaggedUser:
                                    pass
                                else:
                                    TaggedUser.append(tagged)
                            location = info.find(
                                "div", class_="photo-location").text
                            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                  "DESCRIPTION: {}".format(descr.strip()))
                            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                  "LOCATION: {}".format(location.strip()))
                            print(
                                Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "TAGGED-USERS:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + ", ".join(TempTag) + Font.Color.WHITE + "]"))
                            print(
                                Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "TAGGED-HASHTAGS:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + ", ".join(TempHash) + Font.Color.WHITE + "]"))
                            print(
                                Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINKS:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + ", ".join(TempLink) + Font.Color.WHITE + "]"))
                            f = open(filename, "w", encoding="utf-8")
                            f.write("POST ID {} DATA:\n".format(str(name)))
                            f.write("DESCRIPTION: {}\r\n".format(descr.strip()))
                            f.write("LOCATION: {}\r\n".format(
                                    location.strip()))
                            f.write(
                                "TAGGED-USERS: {}\r\n".format(", ".join(TempTag)))
                            f.write(
                                "TAGGED-HASHTAGS: {}\r\n".format(", ".join(TempHash)))
                            f.write(
                                "LINKS: {}\r\n".format(", ".join(TempLink)))
                            TempTag.clear()
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
                                    FormattedGps = "POST N°" + \
                                        str(j) + ": " + final_loc + ": https://www.google.it/maps/place/{},{}".format(Lat, Lon)
                                    EntryGps = final_loc + ": https://www.google.it/maps/place/{},{}".format(Lat, Lon)
                                    PostGpsCoordinates.append(FormattedGps)
                                    if EntryGps in PostLocations:
                                        pass
                                    else:
                                        PostLocations.append(EntryGps)
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
                                    image2 = arr_name[j-1]
                                    Map.Creation.mapPost(
                                        data_fold, Lat, Lon, image2)
                                    #", " + Lat + ", " + Lon
                                except Exception as e:
                                    print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                                        LangFile, "Username", "Instagram", "NoGeoData") + str(e))
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
                """footer = reader.find_all(
                    "span", class_="icon-thumbs-up-alt")
                print(footer)"""
                """while d <= range_band:
                    for info in footer:
                        try:
                            data_fold = folder + "/" + arr_name[d-1]
                            filename = data_fold + \
                                "/{}.txt".format(arr_name[d-1])
                            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                                  Language.Translation.Translate_Language(LangFile, "Username", "Instagram", "Likes/Comments").format(str(d)))
                            likes = info.find("span")[0].text
                            comments = info.find(
                                "span")[1].text
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
                """
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
                        sleep(2)
                else:
                    pass
                if TaggedUser == []:
                    pass
                else:
                    j = 1
                    report = "GUI/Reports/{}/{}/{}.txt".format(
                        Opt, name2, name2)
                    print(Font.Color.GREEN +
                          "\n[+]" + Font.Color.WHITE + "GETTING INSTAGRAM TAGGED USERS")
                    f = open(report, "a")
                    f.write("\nGETTING INSTAGRAM TAGGED USERS:\n")
                    for User in TaggedUser:
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER N°{}: ".format(
                            str(j)) + User + ": https://instagram.com/{}".format(User))
                        f.write("USER N°{}: ".format(
                            str(j)) + User + ": https://instagram.com/{}".format(User) + "\n")
                        j = j + 1
                    f.close()
                    json_file = "GUI/Reports/{}/{}/Profile_pics/Instagram_Posts/Users.json".format(
                        Opt, name2)
                    Downloader.InsertToFile(
                        json_file, TaggedUser, " https://instagram.com/", "TaggedUser")

                if TaggedHashtag == []:
                    pass
                else:
                    i = 1
                    report = "GUI/Reports/{}/{}/{}.txt".format(
                        Opt, name2, name2)
                    print(Font.Color.GREEN +
                          "\n[+]" + Font.Color.WHITE + "GETTING INSTAGRAM TAGGED HASHTAGS")
                    f = open(report, "a")
                    f.write("\nGETTING INSTAGRAM TAGGED HASHTAGS:\n")
                    for Tag in TaggedHashtag:
                        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "TAG N°{}: ".format(
                            str(i)) + Tag + ": https://instagram.com/explore/tags/{}".format(Tag))
                        f.write("HASHTAG N°{}: ".format(
                            str(i)) + Tag + ": https://instagram.com/explore/tags/{}".format(Tag) + "\n")
                        i = i + 1
                    f.close()
                    json_file = "GUI/Reports/{}/{}/Profile_pics/Instagram_Posts/Hashtags.json".format(
                        Opt, name2)
                    Downloader.InsertToFile(
                        json_file, TaggedHashtag, " https://instagram.com/explore/tags/", "TaggedHashtag")

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
    def Twitter(url, username, http_proxy, Posts, Opt, name2):
        headers = Headers.Get.Twitter()
        if Posts > 0:
            if Posts <= 12:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "Download_Full").format(username))
                range_band = Posts
            else:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "Download_Partial").format(username))
                range_band = 12
            folder = "GUI/Reports/{}/{}/Profile_pics/Twitter_Posts".format(
                Opt, name2)
            if os.path.isdir(folder):
                shutil.rmtree(folder)
            os.mkdir(folder)
            medias = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile,"Username","Twitter","MediaOnly") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if medias == 1:
                url = url + "/media"
                param = "/media"
            else:
                url = url + "/with_replies"
                param = "/with_replies"
            openurl = requests.get(
                url, proxies=http_proxy, headers=headers, allow_redirects=True)
            if "No items found" in openurl.text:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + "SOMETHING WENT WRONG...")
            reader = soup(openurl.content, "html.parser")
            i = 1
            j = 1
            TaggedUser = []
            TaggedHastag = []
            TaggedLink = []
            profile = reader.find_all("div", class_="tweet-body")
            for info in profile:
                try:
                    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "Details").format(str(i)))
                    image_try = info.find("a", class_="still-image")
                    retweet2 = info.find("div",class_="retweet-header")
                    replayed = info.find("div",class_="replying-to")
                    if replayed != None:
                        replayed = "TRUE"
                        userRep = info.find_all("div",class_="replying-to")
                        for user in userRep:
                            repUser = user.find("a")["href"].replace("/","")
                    else:
                        replayed = "FALSE"
                    if retweet2 != None:
                        retweet2 = "TRUE"
                        nameOrig = info.find("a",class_="fullname")["title"]
                        userOrig = info.find("a",class_="username")["title"]
                    else:
                        retweet2 = "FALSE"
                    sleep(2)
                    if image_try != None:
                        post = info.find(
                            "a", class_="still-image")["href"]
                        print(
                            Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "Yes_Image").format(str(j)))
                        profile_pic = url.replace(
                            username+ param, "") + post.replace("/pic/", "pic/")
                        image = folder + "/Pic_{}.jpg".format(str(i))
                        getter = requests.get(
                            profile_pic, headers=headers, allow_redirects=False)
                        try:
                            open(image, "wb").write(getter.content)
                            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                  Language.Translation.Translate_Language(LangFile, "Username", "Default", "Success"))
                            Downloader.checkFile(image,"Image")
                            j = j+1
                            sleep(5)
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
                                    username + param, "") + post.replace("/pic/", "pic/")
                                image = folder + "/Pic_{}.jpg".format(str(i))
                                getter = requests.get(
                                    profile_pic, headers=headers, allow_redirects=False)
                                try:
                                    open(image, "wb").write(getter.content)
                                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                                          "DOWNLOAD SUCCESSFULL..")
                                    j = j+1
                                    Downloader.checkFile(image,"Image")
                                    sleep(5)
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
                    TempUser = []
                    TempHashtag = []
                    TempLinks = []
                    if text:
                        desc = info.find(
                            "div", class_="tweet-content media-body").text
                        print(
                            Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "DESCRIPTION: {}".format(desc))
                        taggedArea = info.find_all(
                            "div", class_="tweet-content media-body")
                        for Tag in taggedArea:
                            tagged = Tag.find_all("a")
                            for tag in tagged:
                                if tag.text.startswith("@"):
                                    User = tag.text.replace("@", "")
                                    TempUser.append(User)
                                    if User in TaggedUser:
                                        pass
                                    else:
                                        TaggedUser.append(User)
                                elif tag.text.startswith("#"):
                                    Tag = tag.text.replace("#", "")
                                    TempHashtag.append("#" + Tag)
                                    if Tag in TaggedHastag:
                                        pass
                                    else:
                                        TaggedHastag.append(Tag)
                                else:
                                    Link = tag["href"]
                                    TempLinks.append(Link)
                                    if Link in TaggedLink:
                                        pass
                                    else:
                                        TaggedLink.append(Link)

                    else:
                        print(Font.Color.RED +
                              "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Username", "Twitter", "No_Desc"))
                    footer = info.find_all("span", class_="tweet-stat")
                    comment = footer[0].get_text()
                    likes = footer[1].get_text()
                    retweet = footer[2].get_text()
                    quote = footer[3].get_text()
                    print(
                        Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "IS A RETWEET: {}".format(retweet2))
                    print(
                        Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "IS A REPLY: {}".format(replayed))
                    if retweet2 == "TRUE":
                        print(
                            Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FULL-NAME:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + nameOrig + Font.Color.WHITE + "]"))
                        print(
                            Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USERNAME:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + userOrig + Font.Color.WHITE + "]"))
                    if replayed == "TRUE":
                        print(
                            Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "REPLAYED TO:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + repUser + Font.Color.WHITE + "]"))
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
                    print(Font.Color.YELLOW +
                          "[v]" + Font.Color.WHITE + "TAGGED-USERS:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + ", ".join(TempUser) + Font.Color.WHITE + "]"))
                    print(Font.Color.YELLOW +
                          "[v]" + Font.Color.WHITE + "HASTAGS:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + ", ".join(TempHashtag) + Font.Color.WHITE + "]"))
                    print(Font.Color.YELLOW +
                          "[v]" + Font.Color.WHITE + "LINKS:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + ", ".join(TempLinks) + Font.Color.WHITE + "]"))
                    data_fold = folder + "/" + "Pic_{}".format(str(i))
                    os.mkdir(data_fold)
                    filename = data_fold + \
                        "/Post_{}_details.txt".format(str(i))
                    f = open(filename, "w", encoding="utf-8")
                    f.write("POST N°{} DATA:\n".format(str(i)))
                    f.write("IS A RETWEET: {}\r\n".format(text))
                    if retweet2 == "TRUE":
                        f.write("FULL-NAME: {}\r\n".format(nameOrig))
                        f.write("DESCRIPTION: {}\r\n".format(userOrig))
                    f.write("IS A REPLY: {}\r\n".format(comment))
                    if replayed == "TRUE":
                        f.write("DESCRIPTION: {}\r\n".format(repUser))
                    f.write("DESCRIPTION: {}\r\n".format(text))
                    f.write("COMMENTS: {}\r\n".format(comment))
                    f.write("LIKES: {}\r\n".format(likes))
                    f.write("RETWEETS: {}\r\n".format(retweet))
                    f.write("QUOTES: {}\r\n".format(quote))
                    f.write("POSTED ON: {}\r\n".format(date))
                    f.write("TAGGED-USERS: {}\r\n".format(", ".join(TempUser)))
                    f.write("HASHTAGS: {}\r\n".format(", ".join(TempHashtag)))
                    f.write("LINKS: {}\r\n".format(", ".join(TempLinks)))
                    i = i+1
                    TempUser.clear()
                    sleep(3)
                    if i == range_band + 1:
                        break

                except ConnectionError:
                    print(Font.Color.RED + "[!]" +
                          Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Connection_Error2", "None"))
                    i = i+1
                    if i < range_band + 1:
                        continue
                    else:
                        break
                except Exception as e:
                    print(Font.Color.RED + "[!]" +
                          Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Error", "None") + str(e))
                    i = i+1
                    if i < range_band + 1:
                        continue
                    else:
                        break
            if TaggedUser == []:
                pass
            else:
                report = "GUI/Reports/{}/{}/{}.txt".format(
                    Opt, name2, name2)
                j = 1
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + "GETTING TWITTER TAGGED USERS")
                f = open(report, "a")
                f.write("\nGETTING TWITTER TAGGED USERS:\n")
                for User in TaggedUser:
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER N°{}: ".format(
                        str(j)) + User + ": https://twitter.com/{}".format(User))
                    f.write("USER N°{}: ".format(
                        str(j)) + User + ": https://twitter.com/{}".format(User) + "\n")
                    j = j + 1
                f.close()
                json_file = "GUI/Reports/{}/{}/Profile_pics/Twitter_Posts/Users.json".format(
                    Opt, name2)
                Downloader.InsertToFile(
                    json_file, TaggedUser, " https://twitter.com/", "TaggedUser")

            if TaggedHastag == []:
                pass
            else:
                report = "GUI/Reports/{}/{}/{}.txt".format(
                    Opt, name2, name2)
                x = 1
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + "GETTING TWITTER TAGGED-HASHTAGS")
                f = open(report, "a")
                f.write("\nGETTING TWITTER TAGGED HASHTAGS:\n")
                for Tag in TaggedHastag:
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER N°{}: ".format(
                        str(x)) + Tag + ": https://twitter.com/hashtag/{}".format(Tag))
                    f.write("USER N°{}: ".format(
                        str(x)) + Tag + ": https://twitter.com/hashtag/{}".format(Tag) + "\n")
                    x = x + 1
                f.close()
                json_file = "GUI/Reports/{}/{}/Profile_pics/Twitter_Posts/Hashtags.json".format(
                    Opt, name2)
                Downloader.InsertToFile(
                    json_file, TaggedHastag, " https://twitter.com/hashtag/", "TaggedHastag")

            if TaggedLink == []:
                pass
            else:
                report = "GUI/Reports/{}/{}/{}.txt".format(
                    Opt, name2, name2)
                x = 1
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + "GETTING TWITTER POST HYPERLINKS:")
                f = open(report, "a")
                f.write("\nGETTING TWITTER POST HYPERLINKS:\n")
                for Link in TaggedLink:
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK N°{}: ".format(
                        str(x)) + Link)
                    f.write("LINK N°{}: ".format(
                        str(x)) + Link + "\n")
                    x = x + 1
                f.close()
                json_file = "GUI/Reports/{}/{}/Profile_pics/Twitter_Posts/Links.json".format(
                    Opt, name2)
                Downloader.InsertToFile(
                    json_file, TaggedLink, "Link", "TaggedLink")
        else:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(LangFile, "Username", "Default", "NoPost"))

    @staticmethod
    def TikTok(url, username, http_proxy, Posts, Opt, name2):
        if Posts > 0:
            if Posts <= 12:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "TikTok", "Download_Full").format(username))
                range_band = Posts
            else:
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(LangFile, "Username", "TikTok", "Download_Partial").format(username))
                range_band = 12
            folder = "GUI/Reports/{}/{}/Profile_pics/TikTok_Posts".format(
                Opt, name2)
            if os.path.isdir(folder):
                keep = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE +
                                 Language.Translation.Translate_Language(LangFile, "Username", "TikTok", "FoldFound") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if keep == 1:
                    shutil.rmtree(folder)
                    os.mkdir(folder)
                else:
                    pass
            else:
                os.mkdir(folder)
            i = 1
            TaggedUser = []
            TaggedHashtag = []
            TaggedLink = []
            openurl = requests.get(
                url, proxies=http_proxy, headers=headers, allow_redirects=True)
            reader = soup(openurl.content, "html.parser")
            stats = reader.find_all("div", class_="flex items-center mb-1")
            postsect = reader.find_all("div", class_="info3")
            for video in postsect:
                try:
                    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                          Language.Translation.Translate_Language(LangFile, "Username", "TikTok", "Download").format(str(i)))
                    title = video.find_all("a")[1]["href"]
                    openurl2 = requests.get(
                        title, headers=headers, allow_redirects=True)
                    reader2 = soup(openurl2.content, "html.parser")
                    video = reader2.find("video")["src"]
                    poster = reader2.find("video")["poster"]
                    name = title.replace("https://urlebird.com/video/", "")
                    filename = folder + "/" + name.replace("/", ".mp4")
                    foldername = folder + "/" + name.replace("/", "")
                    print(Font.Color.GREEN + "[+]" + Font.Color.WHITE +
                          "VIDEO ID {}".format(name.replace("/", "")))
                    print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                        LangFile, "Username", "Default", "Check") .format(name.replace("/", ".mp4")))
                    if os.path.exists(foldername):
                        print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                            LangFile, "Username", "Default", "VideoCheckTrue"))
                    else:
                        print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                            LangFile, "Username", "Default", "VideoCheckFalse"))
                        os.mkdir(foldername)
                        report = foldername + "/" + name.replace("/", ".txt")
                        reportImage = foldername + "/" + \
                            name.replace("/", ".jpg")
                        sleep(2)
                        getter = requests.get(
                            video, headers=headers, allow_redirects=True)
                        open(filename, "wb").write(getter.content)
                        print(Font.Color.YELLOW + "[V]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                            LangFile, "Username", "Default", "Success"))
                        Downloader.checkFile(filename,"Video")
                        print(Font.Color.BLUE +
                              "[I]" + Font.Color.WHITE + "DONWLOAD IMAGE POSTER")
                        sleep(2)
                        getter2 = requests.get(
                            poster, headers=headers, allow_redirects=True)
                        open(reportImage, "wb").write(getter2.content)
                        print(Font.Color.YELLOW + "[V]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                            LangFile, "Username", "Default", "Success"))
                        Downloader.checkFile(reportImage,"Image")
                        sleep(2)
                        details = reader2.find("video").text
                        print(Font.Color.YELLOW + "[V]" + Font.Color.WHITE +
                              "DETAILS: {}".format(details.replace("\n", "")))
                        date = reader2.find("h6").text
                        print(
                            Font.Color.YELLOW + "[V]" + Font.Color.WHITE + "POSTED ON: {}".format(date))
                        stats = reader2.find_all("div", class_="row mt-3 mb-1 stats")
                        for stat in stats:
                            pass
                            #play = stat.find("div",class_="col-md-3 col-6")[1].text.replace("▶️","").replace(" ","",1)
                            #print(play)
                            #comments = stat.find(
                            #    "div",class_="col-md-3 col-6")[2].text.replace("📑","").replace(" ","",1)
                            #shares = stat.find("div",class_="col-md-3 col-6")[3].text.replace("↪️","").replace(" ","",1)
                        """print(
                            Font.Color.YELLOW + "[V]" + Font.Color.WHITE + "PLAYES : {}".format(play))
                        print(
                            Font.Color.YELLOW + "[V]" + Font.Color.WHITE + "COMMENTS: {}".format(comments))
                        print(
                            Font.Color.YELLOW + "[V]" + Font.Color.WHITE + "SHARES: {}".format(shares))"""
                        if '<div class="music">' in openurl2.text:
                            music = reader2.find("div", class_="music").text.replace("🎵","").replace(" ","",1)
                            print(
                                Font.Color.YELLOW + "[V]" + Font.Color.WHITE + "SONG: {}".format(music.replace("\n", "")))
                        else:
                            music = "\nNONE"
                            print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                                LangFile, "Username", "TikTok", "NoSong"))
                        TempUser = []
                        TempTag = []
                        TempLinks = []
                        TagSection = reader2.find_all("div", class_="info2")
                        for Tag in TagSection:
                            tag = Tag.find_all("a")
                            for user in tag:
                                tagged = user.text
                                if "#" in tagged:
                                    tagged = tagged.replace("#", "")
                                    if "https" in tagged or "http" in tagged:
                                        Text = Tag.find("p").text
                                        TempLinks.append(Text)
                                        if tagged in TaggedLink:
                                            pass
                                        else:
                                            TaggedLink.append(Text)
                                    else:
                                        TempTag.append("#" + tagged)
                                        if tagged in TaggedHashtag:
                                            pass
                                        else:
                                            TaggedHashtag.append(tagged)
                                else:
                                    TaggedUser.append(tagged)
                                    TempUser.append(tagged)
                                    if tagged in TaggedUser:
                                        pass
                                    else:
                                        TaggedUser.append(tagged)
                        print(
                            Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "TAGGED-USERS:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + ", ".join(TempUser) + Font.Color.WHITE + "]"))
                        print(
                            Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "TAGGED-HASHTAG:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + ", ".join(TempTag) + Font.Color.WHITE + "]"))
                        print(
                            Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "TAGGED-LINKS:{}".format(Font.Color.WHITE + "[" + Font.Color.GREEN + ", ".join(TempLinks) + Font.Color.WHITE + "]"))

                        f = open(report, "w", encoding="utf-8")
                        f.write("TITLE: {}\n".format(name))
                        f.write("DETAILS: {}".format(
                            details.replace("\n", "")))
                        f.write("\nPOSTED ON: {}\n".format(date))
                        """f.write("\nPLAYED: {}".format(play))
                        f.write("\nCOMMENTS: {}".format(comments))
                        f.write("\nSHARES: {}\n".format(shares))"""
                        f.write("SONG: {}\r\n".format(music.replace("\n", "")))
                        f.write("TAGGED-USERS: {}\n".format(", ".join(TempUser)))
                        f.write("TAGGED-HASHTAG: {}".format(", ".join(TempTag)))
                        f.close()
                        TempTag.clear()
                        TempUser.clear()
                    i = i+1
                    sleep(13)
                    if i == range_band + 1:
                        break
                except ConnectionError:
                    print(Font.Color.RED + "[!]" +
                          Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Connection_Error2", "None"))
                    i = i+1
                    if i < range_band + 1:
                        continue
                    else:
                        break
                except Exception as e:
                    print(Font.Color.RED + "[!]" +
                          Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "Default", "Error", "None"))
                    i = i+1
                    if i < range_band + 1:
                        continue
                    else:
                        break
            report = "GUI/Reports/{}/{}/{}.txt".format(
                Opt, name2, name2)
            if TaggedUser == []:
                pass
            else:
                # report = "GUI/Reports/{}/{}/{}.txt".format(
                #        Opt, name2, name2)
                j = 1
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + "GETTING TIKTOK TAGGED USERS")
                f = open(report, "a")
                f.write("\nGETTING TIKTOK TAGGED USERS:\n")
                for User in TaggedUser:
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER N°{}: ".format(
                        str(j)) + User + ": https://tiktok.com/{}".format(User))
                    f.write("USER N°{}: ".format(
                        str(j)) + User + ": https://tiktok.com/{}".format(User) + "\n")
                    j = j + 1
                f.close()
                json_file = "GUI/Reports/{}/{}/Profile_pics/TikTok_Posts/Users.json".format(
                    Opt, name2)
                Downloader.InsertToFile(
                    json_file, TaggedUser, " https://tiktok.com/", "TaggedUser")

            if TaggedHashtag == []:
                pass
            else:
                x = 1
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + "GETTING TIKTOK TAGGED HASHTAG")
                f = open(report, "a")
                f.write("\nGETTING TIKTOK TAGGED HASHTAG:\n")
                for Tag in TaggedHashtag:
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "HASHTAG N°{}: ".format(
                        str(x)) + Tag + ": https://tiktok.com/tag/{}".format(Tag))
                    f.write("HASHTAG N°{}: ".format(
                        str(x)) + Tag + ": https://tiktok.com/tag/{}".format(Tag) + "\n")
                    x = x + 1
                f.close()
                json_file = "GUI/Reports/{}/{}/Profile_pics/TikTok_Posts/Hashtags.json".format(
                    Opt, name2)
                Downloader.InsertToFile(
                    json_file, TaggedHashtag, " https://tiktok.com/tag/", "TaggedHashtag")

            if TaggedLink == []:
                pass
            else:
                v = 1
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + "GETTING TIKTOK TAGGED LINKS")
                f = open(report, "a")
                f.write("\nGETTING TIKTOK TAGGED LINKS:\n")
                for Link in TaggedLink:
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK N°{}: ".format(
                        str(v)) + Link)
                    f.write("LINK N°{}: ".format(
                        str(v)) + Link + "\n")
                    v = v + 1
                f.close()
                json_file = "GUI/Reports/{}/{}/Profile_pics/TikTok_Posts/Links.json".format(
                    Opt, name2)
                Downloader.InsertToFile(
                    json_file, TaggedLink, "Link", "TaggedLink", "TaggedLink")
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(LangFile, "Username", "Default", "Video").format(folder))
        else:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(LangFile, "Username", "Default", "NoPost"))
