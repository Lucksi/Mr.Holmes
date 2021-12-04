# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import json
import requests
from Core.Support import Font
from bs4 import BeautifulSoup as soup

headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
destination = "GUI/Reports/Usernames/Profile_pics/"

class info:
   
    @staticmethod
    def Imgur(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} IMGUR PROFILE...".format(username))
        url = "https://api.imgur.com/account/v1/accounts/{}?client_id=546c25a59c58ad7".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
        reader = openurl.text
        converted = json.loads(reader)
        id_user = converted["id"]
        user = converted["username"]
        bio = converted["bio"]
        reputation = converted["reputation_count"]
        profile_pic = converted["avatar_url"]
        cover_url = converted["cover_url"]
        creation = converted["created_at"]

        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "ID: {}".format(id_user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USERNAME: {}".format(user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "BIO: {}".format(bio))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "REPUTATION: {}".format(reputation))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "AVATAR-IMAGE: {}".format(profile_pic))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "COVER-IMAGE: {}".format(cover_url))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "ACCOUNT-CREATED ON: {}".format(creation))

        download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO DOWNLOAD {} PROFILE PIC?(1)YES(2)NO".format(username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if download == 1:
            image = destination + "{}/_Profile_pic_Imgur.jpg".format(username)
            getter = requests.get(profile_pic, headers=headers, allow_redirects=True)
            open(image, "wb").write(getter.content)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "PROFILE PIC SAVED ON: {}".format(image))
        else:
            pass
        
        f = open(report,"a")
        f.write("\nIMGUR DATA:\n")
        f.write("ID: {}\r\n".format(id_user))
        f.write("USERNAME: {}\r\n".format(user))
        f.write("BIO: {}\r\n".format(bio))
        f.write("REPUTATION: {}\r\n".format(reputation))
        f.write("ACCOUNT-CREATED ON: {}\r\n".format(creation))
    
    @staticmethod
    def Pr0gramm(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} PR0GRAMM PROFILE...".format(username))
        url = "https://pr0gramm.com/api/profile/info?name={}".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
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
        

        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "ID: {}".format(id_user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USERNAME: {}".format(user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "SCORE: {}".format(score))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "COMMENT-DELETED: {}".format(comment_deleted))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "COMMENT-COUNTS: {}".format(comment_count))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "UPLOAD: {}".format(upload_count))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "TAGS: {}".format(tags))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LIKES: {}".format(likes))

        f = open(report,"a")
        f.write("\nPR0GRAMM DATA:\n")
        f.write("ID: {}\r\n".format(id_user))
        f.write("USERNAME: {}\r\n".format(user))
        f.write("SCORE: {}\r\n".format(score))
        f.write("COMMENT-DELETED: {}\r\n".format(comment_deleted))
        f.write("COMMENT-COUNTS: {}\r\n".format(comment_count))
        f.write("UPLOAD: {}\r\n".format(upload_count))
        f.write("TAGS: {}\r\n".format(tags))
        f.write("LIKES: {}\r\n".format(likes))
        
        
    
    
    @staticmethod
    def Binarysearch(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} BINARYSEARCH PROFILE...".format(username))
        url = "https://binarysearch.com/api/users/{}/profile".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
        reader = openurl.text
        converted = json.loads(reader)
        id_user = converted["user"]["id"]
        user = converted["user"]["username"]
        admin = converted["user"]["isAdmin"]
        verified = converted["user"]["isVerified"]
        location = converted["user"]["location"]
        bio = converted["user"]["bio"]
        major = converted["user"]["major"]


        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "ID: {}".format(id_user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USERNAME: {}".format(user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "IS-ADMIN?: {}".format(admin))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "IS-VERIFIED?: {}".format(verified))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LOCATION: {}".format(location))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "BIO: {}".format(bio))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "MAJOR: {}".format(major))

        f = open(report,"a")
        f.write("\nBINARYSEARCH DATA:\n")
        f.write("ID: {}\r\n".format(id_user))
        f.write("USERNAME: {}\r\n".format(user))
        f.write("BIO: {}\r\n".format(bio))
        f.write("IS-ADMIN: {}\r\n".format(admin))
        f.write("IS-VERIFIED: {}\r\n".format(verified))
        f.write("LOCATION: {}\r\n".format(location))
        f.write("MAJOR: {}\r\n".format(major))
        
        
    @staticmethod
    def MixCloud(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} MIXCLOUD PROFILE...".format(username))
        url = "https://api.mixcloud.com/{}/".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
        reader = openurl.text
        converted = json.loads(reader)
        user = converted["name"]
        usern2 = converted["username"]
        bio = converted["biog"]
        follower = converted["follower_count"]
        followers = converted["following_count"]
        is_pro = converted["is_pro"]
        is_premium = converted["is_premium"]
        created = converted["created_time"]
        profile_pic = converted["pictures"]["640wx640h"]
       
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USERNAME: {}".format(usern2))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "NAME: {}".format(user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "IS-PRO?: {}".format(is_pro))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "IS-PREMIUM?: {}".format(is_premium))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FOLLOWER: {}".format(follower))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FOLLOWERS: {}".format(followers))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "BIO: {}".format(bio))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "CREATED-ON: {}".format(created))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

        download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO DOWNLOAD {} PROFILE PIC?(1)YES(2)NO".format(username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if download == 1:
            image = destination + "{}/_Profile_pic_MixCloud.jpg".format(username)
            getter = requests.get(profile_pic, headers=headers, allow_redirects=True)
            open(image, "wb").write(getter.content)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "PROFILE PIC SAVED ON: {}".format(image))
        else:
            pass

        f = open(report,"a")
        f.write("\nMIXCLOUD DATA:\n")
        f.write("USERNAME: {}\r\n".format(usern2))
        f.write("NAME: {}\r\n".format(user))
        f.write("BIO: {}\r\n".format(bio))
        f.write("IS-PRO?: {}\r\n".format(is_pro))
        f.write("IS-PREMIUM? : {}\r\n".format(is_premium))
        f.write("FOLLOWER: {}\r\n".format(follower))
        f.write("FOLLOWERS: {}\r\n".format(followers))
        f.write("CREATED-ON: {}\r\n".format(created))
       
    @staticmethod
    def Nitter(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} NITTER PROFILE...".format(username))
        url = "https://nitter.nixnet.services/{}".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
        Blocked = 'User "{}" has been suspended'.format(username)
        text = openurl.text
        if Blocked in text:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "LOOKS LIKE THIS USER HAS BEEN BANNED..CANNOT SCRAPE DATA")
            pass
        else:
            reader = soup(openurl.content, "html.parser")
            user = reader.find("a",href=True,class_="profile-card-fullname")
            pic = reader.find("a", href=True ,class_= "profile-card-avatar")
            profile_pic = "https://nitter.nixnet.services" +  pic["href"]
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USER: " + user["href"].replace("/",""))
            
            post_items = reader.find_all("li",class_="posts")
            for item in post_items:
                posts = item.find("span",class_="profile-stat-num").text
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "POSTS: {}".format(posts))
            
            follower_items = reader.find_all("li",class_="followers")
            for item in follower_items:
                follower = item.find("span",class_="profile-stat-num").text
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FOLLWERS: {}".format(follower))
            
            followed_item = reader.find_all("li",class_="following")
            for item in followed_item:
                followed = item.find("span",class_="profile-stat-num").text
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FOLLOWING: {}".format(followed))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: "  + profile_pic)
            
            download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO DOWNLOAD {} PROFILE PIC?(1)YES(2)NO".format(username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            
            if download == 1:
                image = destination + "{}/_Profile_pic_Nitter.jpg".format(username)
                getter = requests.get(profile_pic, headers=headers, allow_redirects=True)
                open(image, "wb").write(getter.content)
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "PROFILE PIC SAVED ON: {}".format(image))
            else:
                pass

            f = open(report,"a")
            f.write("\nNITTER DATA:\n")
            f.write("USERNAME: {}\r\n".format(user["href"].replace("/","")))
            f.write("POSTS: {}\r\n".format(posts))
            f.write("FOLLOWERS: {}\r\n".format(follower))
            f.write("FOLLOWING: {}\r\n".format(followed))    

    @staticmethod
    def Dockerhub(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} DOCKERHUB PROFILE...".format(username))
        url = "https://hub.docker.com/v2/users/{}/".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
        reader = openurl.text
        converted = json.loads(reader)
        id_user = converted["id"]
        user = converted["username"]
        full_name = converted["full_name"]
        location = converted["location"]
        profile_creation = converted["date_joined"]
        account_type = converted["type"]
        profile_pic1 = converted["gravatar_url"]
        profile_pic = profile_pic1.replace("&","0&")
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "ID: {}".format(id_user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USERNAME: {}".format(user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FULL-NAME: {}".format(full_name))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LOCATION: {}".format(location))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "CREATED-ON: {}".format(profile_creation))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "ACCOUNT-TYPE: {}".format(account_type))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

        download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO DOWNLOAD {} PROFILE PIC?(1)YES(2)NO".format(username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        
        if download == 1:
            image = destination + "{}/_Profile_pic_DockerHub.jpg".format(username)
            getter = requests.get(profile_pic, headers=headers, allow_redirects=True)
            open(image, "wb").write(getter.content)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "PROFILE PIC SAVED ON: {}".format(image))
        else:
            pass

        f = open(report,"a")
        f.write("\nDOCKERHUB DATA:\n")
        f.write("ID: {}\r\n".format(id_user))
        f.write("USERNAME: {}\r\n".format(user))
        f.write("FULL-NAME: {}\r\n".format(full_name))
        f.write("LOCATION: {}\r\n".format(location))
        f.write("CREATED-ON: {}\r\n".format(profile_creation))
        f.write("ACCOUNT-TYPE: {}\r\n".format(account_type))
       
    @staticmethod
    def Kik(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} KIK PROFILE...".format(username))
        url = "https://ws2.kik.com/user/{}".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
        reader = openurl.text
        converted = json.loads(reader)
        info = []
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
                info.append(name)
        if found == True:
            profile_pic = profile[3]
        else:
            profile_pic = "None"
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FIRST-NAME: {}".format(info[0]))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LAST-NAME: {}".format(info[1]))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

        download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO DOWNLOAD {} PROFILE PIC?(1)YES(2)NO".format(username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        
        if download == 1:
            if profile_pic != "None":
                image = destination + "{}/_Profile_pic_Kik.jpg".format(username)
                getter = requests.get(profile_pic, headers=headers, allow_redirects=True)
                open(image, "wb").write(getter.content)
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "PROFILE PIC SAVED ON: {}".format(image))
            else:
                pass
        else:
            pass
        
        f = open(report,"a")
        f.write("\nKIK DATA:\n")
        f.write("FIRST-NAME: {}\r\n".format(info[0]))
        f.write("LAST-NAME: {}\r\n".format(info[1]))

    @staticmethod
    def GitLab(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} GIT-LAB PROFILE...".format(username))
        url = "https://gitlab.com/api/v4/users?username={}".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
        reader = openurl.text
        converted = json.loads(reader)
        id_user = converted[0]["id"]
        name = converted[0]["name"]
        user = converted[0]["username"]
        status = converted[0]["state"]
        profile_pic = converted[0]["avatar_url"].replace("&","0&")
       
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "ID: {}".format(id_user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USERNAME: {}".format(user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "NAME: {}".format(name))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "STATUS: {}".format(status))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))
        
         
        download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO DOWNLOAD {} PROFILE PIC?(1)YES(2)NO".format(username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        
        if download == 1:
            image = destination + "{}/_Profile_pic_GitLab.jpg".format(username)
            getter = requests.get(profile_pic, headers=headers, allow_redirects=True)
            open(image, "wb").write(getter.content)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "PROFILE PIC SAVED ON: {}".format(image))
        else:
            pass
        
        f = open(report,"a")
        
        f.write("\nGITLAB DATA:\n")
        f.write("ID: {}\r\n".format(id_user))
        f.write("NAME: {}\r\n".format(name))
        f.write("USERNAME: {}\r\n".format(user))
        f.write("STATUS: {}\r\n".format(status))

    @staticmethod
    def Wattpad(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} WATTPAD PROFILE...".format(username))
        url = "https://www.wattpad.com/api/v3/users/{}/".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
        reader = openurl.text
        converted = json.loads(reader)
        user = converted["username"]
        votes = converted["votesReceived"]
        stories = converted["numStoriesPublished"]
        creation = converted["createDate"]
        followers = converted["numFollowers"]
        following = converted["numFollowing"]
        profile_pic = converted["avatar"]
        bio = converted["description"]
        gender = converted["gender"]

        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USERNAME: {}".format(user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "BIO: {}".format(bio))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "GENDER: {}".format(gender))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "VOTES: {}".format(votes))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "CREATED-ON: {}".format(creation))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "STORIES: {}".format(stories))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FOLLOWERS: {}".format(followers))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FOLLOWING: {}".format(following))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

        download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO DOWNLOAD {} PROFILE PIC?(1)YES(2)NO".format(username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        
        if download == 1:
            image = destination + "{}/_Profile_pic_Wattpad.jpg".format(username)
            getter = requests.get(profile_pic, headers=headers, allow_redirects=True)
            open(image, "wb").write(getter.content)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "PROFILE PIC SAVED ON: {}".format(image))
        else:
            pass
        
        f = open(report,"a")
        
        f.write("\nWATTPAD DATA:\n")
        f.write("USERNAME: {}\r\n".format(user))
        f.write("BIO: {}\r\n".format(bio))
        f.write("GENDER: {}\r\n".format(gender))
        f.write("VOTES: {}\r\n".format(votes))
        f.write("CREATED-ON: {}\r\n".format(creation))
        f.write("STORIES: {}\r\n".format(stories))
        f.write("FOLLOWERS: {}\r\n".format(followers))
        f.write("FOLLOWING: {}\r\n".format(following))

    @staticmethod
    def Github(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} GITHUB PROFILE...".format(username))
        url = "https://api.github.com/users/{}".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
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

        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USERNAME: {}".format(user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "BIO: {}".format(bio))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "REPOSITORIES: {}".format(repositories))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "GISTS: {}".format(gist))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "CREATED-ON: {}".format(creation))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LAST UPDATE: {}".format(modification))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FOLLOWERS: {}".format(followers))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FOLLOWING: {}".format(following))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "BLOG: {}".format(blog))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LOCATION: {}".format(location))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "NAME: {}".format(name))

        download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO DOWNLOAD {} PROFILE PIC?(1)YES(2)NO".format(username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        
        if download == 1:
            image = destination + "{}/_Profile_pic_GitHub.jpg".format(username)
            getter = requests.get(profile_pic, headers=headers, allow_redirects=True)
            open(image, "wb").write(getter.content)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "PROFILE PIC SAVED ON: {}".format(image))
        else:
            pass
        
        f = open(report,"a")
        
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
