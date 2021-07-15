import os
import urllib 
import json
from Core.Support import Font
from Core.Support import Creds
from Core.Support import Proxies
from Core.Support import Requests_Search
from datetime import datetime
from time import sleep


class MrHolmes:

    @staticmethod
    def Google_dork(username,report):
        nomefile = "Site_lists/Username/Google_dorks.txt"
        f = open (report ,"a")
        f.write("\nGOOGLE DORKS LINKS:\n")
        f.close()
        print(Font.Color.GREEN + "\n[+]" +Font.Color.WHITE + "GENERATING POSSIBLE GOOGLE DORKS LINK...")
        sleep(3)
        f = open(nomefile,"r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", username)
            print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + site)
            f = open(report,"a")
            f.write(site + "\n")
            sleep(2)
        f.close()
        f.close()

    @staticmethod
    def search(username):
        f = open("Banners/Banner2.txt","r")
        banner = f.read()
        f.close()
        subject = "USERNAME"
        nomefile = "Site_lists/Username/site_list.json"
        report = "Reports/Usernames/" + username + ".txt"
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        Date = "Date: " + str(dt_string)
        if os.path.isfile(report):
            os.remove(report)
        f = open(report, "a")
        f.write("SCANNING EXECUTED ON:\n" + Date + "\r\n")
        f.write("USERNAME FOUND ON:\r\n")
        f.close()
        f = open(nomefile,)
        choice = int(input(
            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO USE A PROXY 'IT MAY CAUSE SOME PROBLEMS AND THE PROCESS WILL SLOW DOWN'(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            http_proxy = Proxies.proxy.final_proxis
            http_proxy2 = Proxies.proxy.choice3
            source = "http://ip-api.com/json/" + http_proxy2
            access = urllib.request.urlopen(source)
            content = access.read()
            final = json.loads(content)
            identity = "YOUR PROXY IP IS LOCATED IN: " + final ["regionName"]
        else:
            http_proxy = None
            http_proxy2 = str(http_proxy)
            identity="None"
        os.system("clear")
        print(Font.Color.GREEN + banner)
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "YOUR PROXY IP ADDRES IS: {} ".format(http_proxy2))
        if identity != "None":
            print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + identity)
        else:
            pass
        data = json.loads(f.read())
        for sites in data:
            for data1 in sites:
                site1 = sites[data1]["user"].replace("{}",username)
                name = sites[data1]["name"]
                error = sites[data1]["Error"]
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "TRYING ON: {} ".format(name))
                try:
                   Requests_Search.Search.search(error, report, site1, http_proxy, sites, data1, username, subject) 
                except Exception as e:
                    print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ERROR..,TRYNG WITH NO PROXIES")
                    http_proxy = None
                    Requests_Search.Search.search(error, report, site1, http_proxy, sites, data1, username, subject)
        count = 1
        if count == 1:
            choice = int(input(
            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A GOOGLE DORK ATTACK?(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                MrHolmes.Google_dork(username,report)
            print(Font.Color.WHITE + "\nREPORT WRITTEN IN: " + os.getcwd() + "/" + report)
            f = open(report,"a")
            f.write("\nSCANNING EXECUTED WITH Mr.Holmes")
            f.close()
            Creds.Sender.mail(report, username)
