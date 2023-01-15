# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import json
import requests
from Core.Support import Font
from Core.Support.Username import Get_Posts
from Core.Support import Language
from bs4 import BeautifulSoup as soup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

filename = Language.Translation.Get_Language()
filename


class info:

    @staticmethod
    def Profile_Pic(username, profile_pic, SiteName, Opt,name2):
        image = "GUI/Reports/{}/{}/Profile_pics/Profile_pic_{}.jpg".format(
        Opt, name2, SiteName)
        getter = requests.get(
            profile_pic, headers=headers, allow_redirects=True)
        try:
            try:
                  open(image, "wb+").write(getter.content)
            except Exception as e:
                  print(str(e))
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Username", "Default", "Saved").format(image))
        except Exception as e:
            print("error" + str(e))
        f = open(image,"rb")
        reader = f.read()
        f.close()

    @staticmethod
    def Get_Url(username, Name):
        filename = "Site_lists/Username/site_list.json"
        reader = open(filename,)
        parser = json.loads(reader.read())
        site = parser[0][Name]["Scrapable_url"].replace("{}", username)
        return site

    @staticmethod
    def Imgur(report, username, http_proxy,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} IMGUR PROFILE...".format(username))
        url = info.Get_Url(username, "Imgur")
        url
        openurl = requests.get(url, proxies=http_proxy,
                               headers=headers, timeout=15)
        try:
            reader = openurl.text
            converted = json.loads(reader)
            id_user = converted["id"]
            user = converted["username"]
            bio = converted["bio"]
            reputation = converted["reputation_count"]
            profile_pic = converted["avatar_url"]
            cover_url = converted["cover_url"]
            creation = converted["created_at"]

            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "ID: {}".format(id_user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "BIO: {}".format(bio))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "REPUTATION: {}".format(reputation))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "AVATAR-IMAGE: {}".format(profile_pic))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "COVER-IMAGE: {}".format(cover_url))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  "ACCOUNT-CREATED ON: {}".format(creation))

            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if download == 1:
                SiteName = "Imgur"
                info.Profile_Pic(username, profile_pic, SiteName,Opt,name2)
            else:
                pass

            f = open(report, "a", encoding="utf-8")
            f.write("\nIMGUR DATA:\n")
            f.write("ID: {}\r\n".format(id_user))
            f.write("USERNAME: {}\r\n".format(user))
            f.write("BIO: {}\r\n".format(bio))
            f.write("REPUTATION: {}\r\n".format(reputation))
            f.write("ACCOUNT-CREATED ON: {}\r\n".format(creation))
            f.close()

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
            pass

    @staticmethod
    def Pr0gramm(report, username, http_proxy,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} PR0GRAMM PROFILE...".format(username))
        url = info.Get_Url(username, "Pr0gramm")
        url
        openurl = requests.get(url, proxies=http_proxy,
                               headers=headers, timeout=15)
        try:
            reader = openurl.text
            converted = json.loads(reader)
            id_user = converted["user"]["id"]
            user = converted["user"]["name"]
            score = converted["user"]["score"]
            comment_deleted = converted["user"]["commentDelete"]
            comment_count = converted["commentCount"]
            upload_count = converted["uploadCount"]
            likes = converted["likeCount"]
            tags = converted["tagCount"]

            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "ID: {}".format(id_user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "SCORE: {}".format(score))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  "COMMENT-DELETED: {}".format(comment_deleted))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  "COMMENT-COUNTS: {}".format(comment_count))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "UPLOAD: {}".format(upload_count))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "TAGS: {}".format(tags))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "LIKES: {}".format(likes))

            f = open(report, "a", encoding="utf-8")
            f.write("\nPR0GRAMM DATA:\n")
            f.write("ID: {}\r\n".format(id_user))
            f.write("USERNAME: {}\r\n".format(user))
            f.write("SCORE: {}\r\n".format(score))
            f.write("COMMENT-DELETED: {}\r\n".format(comment_deleted))
            f.write("COMMENT-COUNTS: {}\r\n".format(comment_count))
            f.write("UPLOAD: {}\r\n".format(upload_count))
            f.write("TAGS: {}\r\n".format(tags))
            f.write("LIKES: {}\r\n".format(likes))
            f.close()

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
            pass

    @staticmethod
    def Binarysearch(report, username, http_proxy,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} BINARYSEARCH PROFILE...".format(username))
        url = info.Get_Url(username, "BinarySearch")
        url
        openurl = requests.get(url, proxies=http_proxy, headers=headers)
        try:
            reader = openurl.text
            converted = json.loads(reader)
            id_user = converted["user"]["id"]
            user = converted["user"]["username"]
            admin = converted["user"]["isAdmin"]
            verified = converted["user"]["isVerified"]
            location = converted["user"]["location"]
            bio = converted["user"]["bio"]
            major = converted["user"]["major"]

            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "ID: {}".format(id_user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(user))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "IS-ADMIN?: {}".format(admin))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "IS-VERIFIED?: {}".format(verified))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "LOCATION: {}".format(location))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "BIO: {}".format(bio))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "MAJOR: {}".format(major))

            f = open(report, "a", encoding="utf-8")
            f.write("\nBINARYSEARCH DATA:\n")
            f.write("ID: {}\r\n".format(id_user))
            f.write("USERNAME: {}\r\n".format(user))
            f.write("BIO: {}\r\n".format(bio))
            f.write("IS-ADMIN: {}\r\n".format(admin))
            f.write("IS-VERIFIED: {}\r\n".format(verified))
            f.write("LOCATION: {}\r\n".format(location))
            f.write("MAJOR: {}\r\n".format(major))
            f.close()

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
            pass

    @staticmethod
    def MixCloud(report, username, http_proxy,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} MIXCLOUD PROFILE...".format(username))
        url = info.Get_Url(username, "MixCloud")
        url
        openurl = requests.get(url, proxies=http_proxy,
                               headers=headers, timeout=30)
        try:
            reader = openurl.text
            converted = json.loads(reader)
            user = converted["name"]
            usern2 = converted["username"]
            bio = converted["biog"]
            followers = converted["follower_count"]
            followeed = converted["following_count"]
            is_pro = converted["is_pro"]
            is_premium = converted["is_premium"]
            created = converted["created_time"]
            profile_pic = converted["pictures"]["640wx640h"]

            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "USERNAME: {}".format(usern2))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "NAME: {}".format(user))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "IS-PRO?: {}".format(is_pro))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "IS-PREMIUM?: {}".format(is_premium))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "FOLLOWER: {}".format(followeed))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "FOLLOWERS: {}".format(followers))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "BIO: {}".format(bio))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "CREATED-ON: {}".format(created))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if download == 1:
                SiteName = "MixCloud"
                info.Profile_Pic(username, profile_pic, SiteName,Opt,name2)
            else:
                pass

            f = open(report, "a", encoding="utf-8")
            f.write("\nMIXCLOUD DATA:\n")
            f.write("USERNAME: {}\r\n".format(usern2))
            f.write("NAME: {}\r\n".format(user))
            f.write("BIO: {}\r\n".format(bio))
            f.write("IS-PRO?: {}\r\n".format(is_pro))
            f.write("IS-PREMIUM? : {}\r\n".format(is_premium))
            f.write("FOLLOWEED: {}\r\n".format(followeed))
            f.write("FOLLOWERS: {}\r\n".format(followers))
            f.write("CREATED-ON: {}\r\n".format(created))
            f.close()

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
            pass

    @staticmethod
    def Instagram(report, username, http_proxy, InstagramParams, PostLocations, PostGpsCoordinates,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} INSTAGRAM PROFILE...".format(username))
        url = info.Get_Url(username, "Instagram")
        url
        openurl = requests.get(url, proxies=http_proxy,
                               headers=headers, timeout=None)
        try:
            Blocked = 'Profile is private.'.format(username)
            text = openurl.text
            if Blocked in text:

                url = "https://www.pixwox.com/it/profile/{}/".format(username)
                openurl2 = requests.get(url, proxies=http_proxy,
                                                      headers=headers, timeout=None)
                reader = soup(openurl2.content, "html.parser")
                name = reader.find("h1",class_="fullname").text
                bio = reader.find("div",class_="sum").text.strip()
                post_n = reader.find_all("div",class_="item item_posts")
                profile_pic = reader.find("a",class_="downbtn")["href"]
                for value in post_n:
                        posts = value.find("div",class_="num").text.replace("\n","")
                follow_n = reader.find_all("div",class_="item item_followers")
                for value in follow_n:
                        followers = value.find("div",class_="num").text.replace("\n","")
                followed_n = reader.find_all("div",class_="item item_following")
                for value in followed_n:
                        followed = value.find("div",class_="num").text.replace("\n","")
                print(Font.Color.YELLOW + "[v]" +
                      Font.Color.WHITE + "USERNAME: {}".format(username))
                print(Font.Color.YELLOW + "[v]" +
                      Font.Color.WHITE + "NAME: {}".format(name))
                print(Font.Color.YELLOW + "[v]" +
                      Font.Color.WHITE + "BIO: {}".format(bio.strip()))
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "POSTS: {}".format(posts.replace("\n","")))
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "FOLLOWERS: {}".format(followers.replace("\n","")))
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "FOLLOWED: {}".format(followed.replace("\n","")))
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))
                download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                    username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if download == 1:
                    SiteName = "Instagram"
                    info.Profile_Pic(username,
                                     profile_pic, SiteName,Opt,name2)
                else:
                    pass
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Username", "Instagram", "Private"))
                Flag = False
                IsPrivate1 = "True"
                InstagramParams.append(IsPrivate1)
                InstagramParams.append(followers)
                InstagramParams.append(posts)
            else:
                IsPrivate1 = "False"
                InstagramParams.append(IsPrivate1)
                Flag = True
                reader = soup(openurl.content, "html.parser")
                name = reader.find("h2", class_="profile-name-bottom").text
                followers = reader.find("span", class_="followed_by").text
                InstagramParams.append(followers)
                followed = reader.find("span", class_="follows").text
                bio = reader.find("div", class_="profile-description").text
                posts = reader.find("span", class_="total_posts").text
                InstagramParams.append(posts)
                profile = reader.find_all("div", class_="profile-avatar")
                for image in profile:
                    profile_pic = image.find(
                        "a", class_="profile-hd-link launchLightbox")["data-video-poster"]
                print(Font.Color.YELLOW + "[v]" +
                      Font.Color.WHITE + "USERNAME: {}".format(username))
                print(Font.Color.YELLOW + "[v]" +
                      Font.Color.WHITE + "NAME: {}".format(name))
                print(Font.Color.YELLOW + "[v]" +
                      Font.Color.WHITE + "BIO: {}".format(bio.strip()))
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "POSTS: {}".format(posts))
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "FOLLOWERS: {}".format(followers))
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "FOLLOWED: {}".format(followed))
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

                f = open(report, "a", encoding="utf-8")
                f.write("\nINSTAGRAM DATA:\n")
                f.write("USERNAME: {}\r\n".format(username))
                f.write("NAME: {}\r\n".format(name))
                f.write("BIO: {}\r\n".format(bio.strip()))
                f.write("POSTS: {}\r\n".format(posts))
                f.write("FOLLOWED: {}\r\n".format(followed))
                f.write("FOLLOWERS: {}\r\n".format(followers))
                f.close()

                download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                    username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

                if download == 1:
                    SiteName = "Instagram"
                    info.Profile_Pic(username,
                                     profile_pic, SiteName,Opt,name2)
                else:
                    pass
        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            Flag = False
            IsPrivate1 = "Undefined"
            InstagramParams.append(IsPrivate1)
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
            Flag = False
            IsPrivate1 = "Undefined"
            InstagramParams.append(IsPrivate1)
            pass
        finally:
            if Flag == True:
                Photos = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Pics").format(
                    username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

                if Photos == 1:
                    Posts = float(posts.replace(",", ''))
                    try:
                        Get_Posts.Downloader.Instagram(url,
                                                       username, http_proxy, Posts, PostLocations, PostGpsCoordinates,Opt,name2)
                    except ConnectionError:
                        print(Font.Color.RED +
                              "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
                else:
                    pass

    @staticmethod
    def Twitter(report, username, http_proxy, TwitterParams ,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} TWITTER PROFILE...".format(username))
        url = info.Get_Url(username, "Twitter")
        url
        openurl = requests.get(url, proxies=http_proxy,
                               headers=headers)
        try:
            Blocked = 'User "{}" has been suspended'.format(username)
            text = openurl.text
            if Blocked in text:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Username", "Twitter", "Blocked"))
                Flag = False
                IsPrivate = "Undefined"
                TwitterParams.append(IsPrivate)
                pass
            else:
                Private = "This account&#x27;s tweets are protected."
                text = openurl.text
                if Private in text:
                  IsPrivate = "True"
                  TwitterParams.append(IsPrivate)
                else:
                  IsPrivate = "False"
                  TwitterParams.append(IsPrivate)
                Flag = True
                reader = soup(openurl.content, "html.parser")
                user = reader.find(
                    "a", href=True, class_="profile-card-fullname")
                pic = reader.find("a", href=True, class_="profile-card-avatar")
                profile_pic = url.replace("/"+username, "") + pic["href"]
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                      "USER: " + user["href"].replace("/", ""))
                follower_items = reader.find_all("li", class_="followers")
                for item in follower_items:
                    follower = item.find(
                        "span", class_="profile-stat-num").text
                    print(Font.Color.YELLOW +
                          "[v]" + Font.Color.WHITE + "FOLLWERS: {}".format(follower))
                TwitterParams.append(follower)


                post_items = reader.find_all("li", class_="posts")
                for item in post_items:
                    posts = item.find("span", class_="profile-stat-num").text
                    print(Font.Color.YELLOW +
                          "[v]" + Font.Color.WHITE + "POSTS: {}".format(posts))
                TwitterParams.append(posts)

               
                followed_item = reader.find_all("li", class_="following")
                for item in followed_item:
                    followed = item.find(
                        "span", class_="profile-stat-num").text
                    print(Font.Color.YELLOW +
                          "[v]" + Font.Color.WHITE + "FOLLOWING: {}".format(followed))
                    print(Font.Color.YELLOW +
                          "[v]" + Font.Color.WHITE + "PROFILE-PIC: " + profile_pic)

                download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                    username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

                if download == 1:
                    SiteName = "Twitter"
                    info.Profile_Pic(username,
                                     profile_pic, SiteName ,Opt,name2)
                else:
                    pass

                f = open(report, "a", encoding="utf-8")
                f.write("\nTWITTER DATA:\n")
                f.write("USERNAME: {}\r\n".format(
                    user["href"].replace("/", "")))
                f.write("POSTS: {}\r\n".format(posts))
                f.write("FOLLOWERS: {}\r\n".format(follower))
                f.write("FOLLOWING: {}\r\n".format(followed))
                f.close()

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            Flag = False
            IsPrivate = "Undefined"
            TwitterParams.append(IsPrivate)
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
            Flag = False
            IsPrivate = "Undefined"
            TwitterParams.append(IsPrivate)
            pass
        except requests.Timeout as err:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
            Flag = False
            IsPrivate = "Undefined"
            TwitterParams[0].append(IsPrivate)
        finally:
            if Flag == True:
                Photos = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Pics").format(
                    username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if Photos == 1:
                    Private = "This account&#x27;s tweets are protected."
                    text = openurl.text
                    if Private in text:
                        print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                              Language.Translation.Translate_Language(filename, "Username", "Twitter", "Protected").format(username))
                    else:
                        Posts = float(posts.replace(",", ''))
                        try:
                            Get_Posts.Downloader.Twitter(url,
                                                         username, http_proxy, Posts ,Opt,name2)
                        except ConnectionError:
                            print(Font.Color.RED +
                                  "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
                else:
                    pass

    @staticmethod
    def Dockerhub(report, username, http_proxy ,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} DOCKERHUB PROFILE...".format(username))
        url = info.Get_Url(username, "DockerHub")
        url
        openurl = requests.get(url, proxies=http_proxy,
                               headers=headers, timeout=15)
        try:
            reader = openurl.text
            converted = json.loads(reader)
            id_user = converted["id"]
            user = converted["username"]
            full_name = converted["full_name"]
            location = converted["location"]
            profile_creation = converted["date_joined"]
            account_type = converted["type"]
            profile_pic1 = converted["gravatar_url"]
            profile_pic = profile_pic1.replace("&", "0&")
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "ID: {}".format(id_user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(user))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "FULL-NAME: {}".format(full_name))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "LOCATION: {}".format(location))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  "CREATED-ON: {}".format(profile_creation))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  "ACCOUNT-TYPE: {}".format(account_type))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

            if download == 1:
                SiteName = "DockerHub"
                info.Profile_Pic(username, profile_pic, SiteName ,Opt,name2)
            else:
                pass

            f = open(report, "a", encoding="utf-8")
            f.write("\nDOCKERHUB DATA:\n")
            f.write("ID: {}\r\n".format(id_user))
            f.write("USERNAME: {}\r\n".format(user))
            f.write("FULL-NAME: {}\r\n".format(full_name))
            f.write("LOCATION: {}\r\n".format(location))
            f.write("CREATED-ON: {}\r\n".format(profile_creation))
            f.write("ACCOUNT-TYPE: {}\r\n".format(account_type))
            f.close()
        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
            pass

    @staticmethod
    def Kik(report, username, http_proxy ,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} KIK PROFILE...".format(username))
        url = info.Get_Url(username, "Kik")
        url
        openurl = requests.get(url, proxies=http_proxy,
                               headers=headers, timeout=15)
        try:
            reader = openurl.text
            converted = json.loads(reader)
            target = []
            profile = []
            for values in converted:
                name = converted[values]
                if values == "displayPic":
                    found = True
                    profile.append(name)
                    break
                else:
                    found = False
                    profile.append("None")
                    target.append(name)
            if found == True:
                profile_pic = profile[3]
            else:
                profile_pic = "None"
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "FIRST-NAME: {}".format(target[0]))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "LAST-NAME: {}".format(target[1]))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

            if download == 1:
                if profile_pic != "None":
                    SiteName = "Kik"
                    info.Profile_Pic(username,
                                     profile_pic, SiteName ,Opt,name2)
                else:
                    pass
            else:
                pass

            f = open(report, "a", encoding="utf-8")
            f.write("\nKIK DATA:\n")
            f.write("FIRST-NAME: {}\r\n".format(target[0]))
            f.write("LAST-NAME: {}\r\n".format(target[1]))
            f.close()
        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass

        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
            pass

    @staticmethod
    def GitLab(report, username, http_proxy ,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} GIT-LAB PROFILE...".format(username))
        url = info.Get_Url(username, "GitLab")
        url
        openurl = requests.get(url, proxies=http_proxy,
                               headers=headers, timeout=15)
        try:
            reader = openurl.text
            converted = json.loads(reader)
            id_user = converted[0]["id"]
            name = converted[0]["name"]
            user = converted[0]["username"]
            status = converted[0]["state"]
            profile_pic = converted[0]["avatar_url"].replace("&", "0&")

            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "ID: {}".format(id_user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "NAME: {}".format(name))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "STATUS: {}".format(status))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

            if download == 1:
                SiteName = "GitLab"
                info.Profile_Pic(username, profile_pic, SiteName ,Opt,name2)
            else:
                pass

            f = open(report, "a", encoding="utf-8")

            f.write("\nGITLAB DATA:\n")
            f.write("ID: {}\r\n".format(id_user))
            f.write("NAME: {}\r\n".format(name))
            f.write("USERNAME: {}\r\n".format(user))
            f.write("STATUS: {}\r\n".format(status))
            f.close()

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
            pass

    @staticmethod
    def Wattpad(report, username, http_proxy ,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} WATTPAD PROFILE...".format(username))
        url = info.Get_Url(username, "Wattpad")
        url
        openurl = requests.get(url, proxies=http_proxy,
                               headers=headers, timeout=15)
        try:
            reader = openurl.text
            converted = json.loads(reader)
            user = converted["username"]
            votes = converted["votesReceived"]
            stories = converted["numStoriesPublished"]
            creation = converted["createDate"]
            modification = converted["modifyDate"]
            followers = converted["numFollowers"]
            following = converted["numFollowing"]
            profile_pic = converted["avatar"]
            bio = converted["description"]
            gender = converted["gender"]
            Location = converted["location"]
            isPrivate = converted["isPrivate"]

            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "BIO: {}".format(bio))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "GENDER: {}".format(gender))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "VOTES: {}".format(votes))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "CREATED-ON: {}".format(creation))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "MODIFIED-ON: {}".format(modification))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "STORIES: {}".format(stories))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "FOLLOWERS: {}".format(followers))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "FOLLOWING: {}".format(following))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "LOCATION: {}".format(Location))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "PRIVATE: {}".format(isPrivate))

            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

            if download == 1:
                SiteName = "Wattpad"
                info.Profile_Pic(username, profile_pic, SiteName ,Opt,name2)
            else:
                pass

            f = open(report, "a", encoding="utf-8")

            f.write("\nWATTPAD DATA:\n")
            f.write("USERNAME: {}\r\n".format(user))
            f.write("BIO: {}\r\n".format(bio))
            f.write("GENDER: {}\r\n".format(gender))
            f.write("VOTES: {}\r\n".format(votes))
            f.write("CREATED-ON: {}\r\n".format(creation))
            f.write("STORIES: {}\r\n".format(stories))
            f.write("FOLLOWERS: {}\r\n".format(followers))
            f.write("FOLLOWING: {}\r\n".format(following))
            f.write("LOCATION: {}\r\n".format(Location))
            f.write("PRIVATE: {}\r\n".format(isPrivate))
            f.close()

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
            pass

    @staticmethod
    def Github(report, username, http_proxy ,Opt,name2):
        try:
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  "SCRAPING {} GITHUB PROFILE...".format(username))
            url = info.Get_Url(username, "GitHub")
            url
            openurl = requests.get(url, proxies=http_proxy,
                                   headers=headers, timeout=15)
            reader = openurl.text
            converted = json.loads(reader)
            user = converted["login"]
            repositories = converted["public_repos"]
            gist = converted["public_gists"]
            creation = converted["created_at"]
            modification = converted["updated_at"]
            followers = converted["followers"]
            following = converted["following"]
            profile_pic = converted["avatar_url"]
            bio = converted["bio"]
            blog = converted["blog"]
            location = converted["location"]
            name = converted["name"]
            email = converted["email"]
            twitter = converted["twitter_username"]
            is_hireable = converted["hireable"]
            company = converted["company"]

            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "BIO: {}".format(bio))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  "REPOSITORIES: {}".format(repositories))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "GISTS: {}".format(gist))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "CREATED-ON: {}".format(creation))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "LAST UPDATE: {}".format(modification))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "FOLLOWERS: {}".format(followers))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "FOLLOWING: {}".format(following))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "BLOG: {}".format(blog))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "LOCATION: {}".format(location))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "NAME: {}".format(name))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "EMAIL: {}".format(email))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "TWITTER: {}".format(twitter))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "HIREABLE: {}".format(is_hireable))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "COMPANY: {}".format(company))

            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

            if download == 1:
                SiteName = "GitHub"
                info.Profile_Pic(username, profile_pic, SiteName ,Opt,name2)
            else:
                pass
            f = open(report, "a", encoding="utf-8")
            f.write("\nGIT-HUB DATA:\n")
            f.write("USERNAME: {}\r\n".format(user))
            f.write("BIO: {}\r\n".format(bio))
            f.write("REPOSITORIES: {}\r\n".format(repositories))
            f.write("GISTS: {}\r\n".format(gist))
            f.write("CREATED-ON: {}\r\n".format(creation))
            f.write("UPDATED-ON: {}\r\n".format(modification))
            f.write("FOLLOWERS: {}\r\n".format(followers))
            f.write("FOLLOWING: {}\r\n".format(following))
            f.write("BLOG: {}\r\n".format(blog))
            f.write("LOCATION: {}\r\n".format(location))
            f.write("NAME: {}\r\n".format(name))
            f.write("EMAIL: {}\r\n".format(email))
            f.write("TWITTER: {}\r\n".format(twitter))
            f.write("HIREABLE: {}\r\n".format(is_hireable))
            f.write("COMPANY: {}\r\n".format(company))
            f.close()

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
            pass

    @staticmethod
    def TikTok(report, username, http_proxy ,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} TIKTOK PROFILE...".format(username))
        url = info.Get_Url(username, "TikTok")
        url
        openurl = requests.get(url, proxies=http_proxy,
                               headers=headers, timeout=15)
        Posts = 0
        Flag = True
        try:
            reader = soup(openurl.content, "html.parser")
            user = reader.find("h1", class_="user").text
            name = reader.find("h5", class_="text-dark").text
            followers = reader.find(
                "div", class_="col-7 col-md-auto text-truncate").text
            followed = reader.find(
                "div", class_="col-auto d-none d-sm-block text-truncate").text
            like = reader.find("div", class_="col-auto").text
            profile = reader.find_all(
                "div", class_="col-md-auto justify-content-center text-center")
            postsect = reader.find_all("div", class_="info3")
            for post in postsect:
                Posts = Posts + 1

            for image in profile:
                profile_pic = image.find("img")["src"]

            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "NAME: {}".format(name))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "LIKES: {}".format(like))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "FOLLOWERS: {}".format(followers))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "FOLLOWED: {}".format(followed))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

            f = open(report, "a", encoding="utf-8")
            f.write("\nTIKTOK DATA:\n")
            f.write("USERNAME: {}\r\n".format(user))
            f.write("NAME: {}\r\n".format(name))
            f.write("LIKES: {}\r\n".format(like))
            f.write("FOLLOWED: {}\r\n".format(followed))
            f.write("FOLLOWERS: {}\r\n".format(followers))
            f.close()

            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

            if download == 1:
                SiteName = "TikTok"
                info.Profile_Pic(username, profile_pic, SiteName ,Opt,name2)
            else:
                pass

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            Flag = False
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
            Flag = False
            pass
        finally:
            if Flag == True:
                Video = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Pics").format(
                    username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

                if Video == 1:
                    try:
                        Get_Posts.Downloader.TikTok(
                            url, username, http_proxy, Posts ,Opt,name2)
                    except ConnectionError:
                        print(Font.Color.RED +
                              "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
                else:
                    pass

    @staticmethod
    def Minecraft(report, username, http_proxy ,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} MINECRAFT PROFILE...".format(username))
        url = info.Get_Url(username, "Minecraft")
        url
        openurl = requests.get(url, proxies=http_proxy, headers=headers)
        try:
            reader = openurl.text
            converted = json.loads(reader)
            id_user = converted["id"]
            user = converted["name"]

            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "ID: {}".format(id_user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(user))

            f = open(report, "a", encoding="utf-8")
            f.write("\nMINECRAFT DATA:\n")
            f.write("ID: {}\r\n".format(id_user))
            f.write("USERNAME: {}\r\n".format(user))
            f.close()

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
            pass

    @staticmethod
    def Ngl(report, username, http_proxy ,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} NGL.LINK PROFILE...".format(username))
        url = info.Get_Url(username, "Ngl.link")
        url
        openurl = requests.get(url, proxies=http_proxy, headers=headers)
        try:
            reader = soup(openurl.content, "html.parser")
            profile_pic = reader.find("img", class_="pfp")["src"]
            clicks = reader.find("span", class_="clickCount").text
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(username))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "CLICKS: {}".format(clicks))

            f = open(report, "a", encoding="utf-8")
            f.write("\nNGL.LINK DATA:\n")
            f.write("USERNAME: {}\r\n".format(username))
            f.write("CLICKS: {}\r\n".format(clicks))
            f.close()

            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

            if download == 1:
                SiteName = "Ngl.link"
                info.Profile_Pic(username, profile_pic, SiteName ,Opt,name2)
            else:
                pass

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None"))
            pass

    @staticmethod
    def Disqus(report, username, http_proxy ,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} DISQUS PROFILE...".format(username))
        url = info.Get_Url(username, "Disqus")
        url
        openurl = requests.get(url, proxies=http_proxy, headers=headers)
        try:
            reader = openurl.text
            converted = json.loads(reader)
            id_user = converted["response"]["id"]
            user = converted["response"]["username"]
            creation = converted["response"]["joinedAt"]
            location = converted["response"]["location"]
            private = converted["response"]["isPrivate"]
            Followers = converted["response"]["numFollowers"]
            rep = converted["response"]["reputation"]
            Followed = converted["response"]["numFollowing"]
            bio = converted["response"]["about"]
            profile_pic = converted["response"]["avatar"]["permalink"]

            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "ID: {}".format(id_user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(user))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "CREATED ON: {}".format(creation))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "LOCATION: {}".format(location))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "PRIVATE: {}".format(private))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "FOLLOWERS: {}".format(Followers))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "FOLLOWED: {}".format(Followed))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "BIO: {}".format(bio))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "REPUTATION: {}".format(rep))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

            if download == 1:
                SiteName = "Disqus"
                info.Profile_Pic(username, profile_pic, SiteName ,Opt,name2)
            else:
                pass
            f = open(report, "a", encoding="utf-8")
            f.write("\nDISQUS DATA:\n")
            f.write("ID: {}\r\n".format(id_user))
            f.write("USERNAME: {}\r\n".format(user))
            f.write("CREATED ON: {}\r\n".format(creation))
            f.write("LOCATION: {}\r\n".format(location))
            f.write("PRIVATE: {}\r\n".format(private))
            f.write("FOLLOWERS: {}\r\n".format(Followers))
            f.write("FOLLOWED: {}\r\n".format(Followed))
            f.write("BIO: {}\r\n".format(bio))
            f.write("REPUTATION: {}\r\n".format(rep))
            f.close()

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
            pass

    @staticmethod
    def Tellonym(report, username, http_proxy ,Opt,name2):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "SCRAPING {} TELLONYM PROFILE...".format(username))
        url = info.Get_Url(username, "Tellonym")
        url
        openurl = requests.get(url, proxies=http_proxy, headers=headers)
        try:
            reader = soup(openurl.content, "html.parser")
            profile_pic = reader.find(
                "meta", attrs={"name": "twitter:image"})["content"]
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "USERNAME: {}".format(username))
            print(Font.Color.YELLOW + "[v]" +
                  Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

            f = open(report, "a", encoding="utf-8")
            f.write("\nTELLONYM DATA:\n")
            f.write("USERNAME: {}\r\n".format(username))
            f.write("PROFILE-PIC: {}\r\n".format(profile_pic))
            f.close()

            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Username", "Default", "Profile_Pic").format(
                username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))

            if download == 1:
                SiteName = "Tellonym"
                info.Profile_Pic(username, profile_pic, SiteName ,Opt,name2)
            else:
                pass

        except ConnectionError:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Connection_Error2", "None"))
            pass
        except Exception as e:
            print(Font.Color.RED + "[!]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Error", "None") + str(e))
            pass
