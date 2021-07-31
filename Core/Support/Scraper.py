import json
import requests
from Core.Support import Font
from bs4 import BeautifulSoup as soup

headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
destination = "Reports/Usernames/Profile_pics/"

class info:
   
    @staticmethod
    def imgur(report,username,http_proxy):
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
            image = destination + "{}_Profile_pic_Imgur.jpg".format(username)
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
        f.write("PROFILE-IMAGE: {}\r\n".format(profile_pic))
        f.write("COVER-IMAGE: {}\r\n".format(cover_url))
        f.write("ACCOUNT-CREATED ON: {}\r\n".format(creation))
    
    @staticmethod
    def pr0gramm(report,username,http_proxy):
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
            image = destination + "{}_Profile_pic_MixCloud.jpg".format(username)
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
        f.write("PROFILE-PIC: {}\r\n".format(profile_pic))

    @staticmethod
    def Nitter(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} NITTER PROFILE...".format(username))
        url = " https://nitter.nixnet.services/{}".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
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
            image = destination + "{}_Profile_pic_Nitter.jpg".format(username)
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
        f.write("PROFILE-PIC: {}\r\n".format(profile_pic))


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
            image = destination + "{}_Profile_pic_DockerHub.jpg".format(username)
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
        f.write("PROFILE-PIC: {}\r\n".format(profile_pic))

    @staticmethod
    def Kik(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING {} KIK PROFILE...".format(username))
        url = "https://ws2.kik.com/user/{}".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
        reader = openurl.text
        converted = json.loads(reader)
        name = converted["firstName"]
        lastName = converted["lastName"]
        profile_pic = converted["displayPic"]

        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "FIRST-NAME: {}".format(name))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LAST-NAME: {}".format(lastName))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))

        download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO DOWNLOAD {} PROFILE PIC?(1)YES(2)NO".format(username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        
        if download == 1:
            image = destination + "{}_Profile_pic_Kik.jpg".format(username)
            getter = requests.get(profile_pic, headers=headers, allow_redirects=True)
            open(image, "wb").write(getter.content)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "PROFILE PIC SAVED ON: {}".format(image))
        else:
            pass
        
        f = open(report,"a")
        f.write("\nKIK DATA:\n")
        f.write("FIRST-NAME: {}\r\n".format(name))
        f.write("LAST-NAME: {}\r\n".format(lastName))
        f.write("PROFILE-PIC: {}\r\n".format(profile_pic))

    @staticmethod
    def GitLab(report,username,http_proxy):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCRAPING GIT-LAB PROFILE...".format(username))
        url = "https://gitlab.com/api/v4/users?username={}".format(username)
        openurl = requests.get(url,proxies=http_proxy,headers=headers)
        reader = openurl.text
        converted = json.loads(reader)
        id_user = converted[0]["id"]
        name = converted[0]["name"]
        user = converted[0]["username"]
        status = converted[0]["state"]
        profile_pic = converted[0]["avatar_url".replace("&","0&")]
        
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "ID: {}".format(id_user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "USERNAME: {}".format(user))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "NAME: {}".format(name))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "STATUS: {}".format(status))
        print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "PROFILE-PIC: {}".format(profile_pic))
        
         
        download = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO DOWNLOAD {} PROFILE PIC?(1)YES(2)NO".format(username) + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        
        if download == 1:
            image = destination + "{}_Profile_pic_GitLab.jpg".format(username)
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
        f.write("PROFILE-PIC: {}\r\n".format(profile_pic))
