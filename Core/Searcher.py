# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import os
import urllib 
import json
import logging
import shutil
from Core.Support import Font
from Core.Support import Creds
from Core.Support import Proxies
from Core.Support import Requests_Search
from Core.Support import Scraper
from Core.Support import Clear
from Core.Support import Dorks
from datetime import datetime
from time import sleep
from configparser import ConfigParser

class MrHolmes:

    @staticmethod
    def Banner():
        Clear.Screen.Clear()
        f = open("Banners/Banner2.txt","r")
        banner = f.read()
        f.close()
        print(Font.Color.GREEN + banner)

    @staticmethod
    def Google_dork(username):
        report = "GUI/Reports/Usernames/Dorks/{}_Dorks.txt".format(username)
        nomefile = "Site_lists/Username/Google_dorks.txt"
        Type = "GOOGLE"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "REMOVING OLD {}_Dorks.txt".format(username))
        else:
            pass
        Dorks.Search.dork(username,report,nomefile,Type)
    
    @staticmethod
    def Yandex_dork(username):
        report = "GUI/Reports/Usernames/Dorks/{}_Dorks.txt".format(username)
        nomefile = "Site_lists/Username/Yandex_dorks.txt"
        Type = "YANDEX"
        Dorks.Search.dork(username,report,nomefile,Type)
    
    @staticmethod
    def Bing_dork(username):
        report = "GUI/Reports/Usernames/Dorks/Bing_{}_Dorks.txt".format(username)
        nomefile = "Site_lists/Username/Bing_dorks.txt"
        Type = "BING"
        Dorks.Search.dork(username,report,nomefile,Type)

    @staticmethod
    def search(username):
        successfull = []
        successfullName = []
        ScraperSites = []
        Writable = True
        MrHolmes.Banner()
        subject = "USERNAME"
        nomefile = "Site_lists/Username/site_list.json"
        report = "GUI/Reports/Usernames/" + username + ".txt"
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        Date = "Date: " + str(dt_string)
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
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "REMOVING OLD {}.txt".format(username))
        f = open(report, "a")
        f.write("SCANNING EXECUTED ON:\n" + Date + "\r\n")
        f.write("\nUSERNAME FOUND ON:\r\n")
        f.close()
        f = open(nomefile,)
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "YOUR PROXY IP ADDRES IS: {} ".format(http_proxy2))
        if identity != "None":
            print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + identity)
        else:
            pass
        nomefile = "Configuration/Configuration.ini"
        Parser = ConfigParser()
        Parser.read(nomefile)            
        Conf_Log = Parser["Settings"]["Show_Logs"]
        if Conf_Log == "True":
            file_Log = "Logs/Session_" + username + ".log"
            logging.basicConfig(filename= file_Log, filemode = "w", format="%(asctime)s %(message)s")
            Logger = logging.getLogger()
            Logger.setLevel(logging.DEBUG)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "LOGS ENABLED..FILE SAVED ON: {}".format(file_Log))
        else:
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "LOGS DISABLED")
        data = json.loads(f.read())
        for sites in data:
            for data1 in sites:
                site1 = sites[data1]["user"].replace("{}",username)
                site2= sites[data1]["user2"].replace("{}", username)
                name = sites[data1]["name"]
                main = sites[data1]["main"]
                error = sites[data1]["Error"]
                exception_char = sites[data1]["exception"]
                is_scrapable = sites[data1]["Scrapable"]
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "TRYING ON: {} ".format(name))
                for errors in exception_char:
                    if errors in username:
                        alert = "NOT-CORRECT"
                        break
                    else:
                        alert = "CORRECT"
                if alert == "NOT-CORRECT":
                    print(Font.Color.YELLOW2  + "[U]" + Font.Color.WHITE + "USERNAME FORMAT NOT VALID..SKIPPING")   
                else:
                    try:
                        Requests_Search.Search.search(error, report, site1, site2, http_proxy, sites, data1, username, subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main) 
                    except Exception as e:
                        print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")
                        http_proxy = None
                        try:
                            Requests_Search.Search.search(error, report, site1, site2, http_proxy, sites, data1, username, subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main)           
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]"+ Font.Color.WHITE + "CANNOT REACH THIS SITE SKIPPING...")
        Nsfw = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO SCAN ON NSFW SITES?(1)YES(2)NO\n\n"+ Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if Nsfw == 1:
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "YOUR PROXY IP ADDRES IS: {} ".format(http_proxy2))
            if identity != "None":
                print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + identity)
            else:
                pass
            nomefile = "Site_lists/Username/NSFW_site_list.json"
            f = open(nomefile,)
            data = json.loads(f.read())
            for sites in data:
                for data1 in sites:
                    site1 = sites[data1]["user"].replace("{}",username)
                    site2= sites[data1]["user2"].replace("{}", username)
                    name = sites[data1]["name"]
                    error = sites[data1]["Error"]
                    main = sites[data1]["main"]
                    exception_char = sites[data1]["exception"]
                    is_scrapable = sites[data1]["Scrapable"]
                    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "TRYING ON: {} ".format(name))
                    for errors in exception_char:
                        if errors in username:
                            alert = "NOT-CORRECT"
                            break
                        else:
                            alert = "CORRECT"
                    if alert == "NOT-CORRECT":
                        print(Font.Color.YELLOW2  + "[U]" + Font.Color.WHITE + "USERNAME FORMAT NOT VALID..SKIPPING")   
                    else:
                        try:
                            Requests_Search.Search.search(error, report, site1, site2, http_proxy, sites, data1, username, subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main) 
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")
                            http_proxy = None
                            try:
                                Requests_Search.Search.search(error, report, site1, site2, http_proxy, sites, data1, username, subject, successfull, name, successfullName, is_scrapable, ScraperSites, Writable, main)
                            except Exception as e:
                                print(Font.Color.BLUE + "\n[N]"+ Font.Color.WHITE + "CANNOT REACH THIS SITE SKIPPING...")
        else:
            pass
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "{}: {} FOUNDS ON:".format(subject,username))
        sleep(3)
        if len(successfull):
            for names in successfull:
                print(Font.Color.YELLOW +"[v]" + Font.Color.WHITE +  names)
            if len(ScraperSites):
                os.chdir("GUI/Reports/Usernames/Profile_pics")
                if os.path.isdir(username):
                    shutil.rmtree(username)
                    os.mkdir(username)
                else:
                    os.mkdir(username)
                os.chdir("../../../../")
                choice = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO SCRAPE USER DATA?(1)YES(2)NO\n\n" + Font.Color.GREEN + "[*MR.HOLMES*]" + Font.Color.WHITE + "-->"))
                if choice == 1:
                    choice = int(input(
                    Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO USE A PROXY 'IT MAY CAUSE SOME PROBLEMS AND THE PROCESS WILL SLOW DOWN'(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
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
                    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "YOUR PROXY IP ADDRES IS: {} ".format(http_proxy2))
                    if identity != "None":
                        print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + identity)
                    else:
                        pass 
                    
                    if "Imgur" in ScraperSites:
                        try:
                            Scraper.info.Imgur(report, username , http_proxy)
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")      
                            http_proxy = None
                            Scraper.info.Imgur(report, username , http_proxy)
                    else:
                        pass
                    
                    if "Pr0gramm" in ScraperSites:
                        try:
                            Scraper.info.Pr0gramm(report, username , http_proxy)
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")      
                            http_proxy = None
                            Scraper.info.Pr0gramm(report, username , http_proxy)
                    else:
                        pass
                    
                    if "BinarySearch" in ScraperSites:
                        try:
                            Scraper.info.Binarysearch(report, username , http_proxy)
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")      
                            http_proxy = None
                            Scraper.info.Binarysearch(report, username , http_proxy)
                    else:
                        pass 
                    
                    if "MixCloud" in ScraperSites:
                        try:
                            Scraper.info.MixCloud(report, username , http_proxy)
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")      
                            http_proxy = None
                            Scraper.info.MixCloud(report, username , http_proxy)
                    else:
                        pass
                    
                    if "Nitter" in ScraperSites:
                        try:
                            Scraper.info.Nitter(report, username , http_proxy)
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")      
                            http_proxy = None
                            Scraper.info.Nitter(report, username , http_proxy)
                    else:
                        pass
                    
                    if "DockerHub" in ScraperSites:
                        try:
                            Scraper.info.Dockerhub(report, username , http_proxy)
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")      
                            http_proxy = None
                            Scraper.info.Dockerhub(report, username , http_proxy)
                    else:
                        pass

                    if "Kik" in ScraperSites:
                        try:
                            Scraper.info.Kik(report, username , http_proxy)
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")      
                            http_proxy = None
                            Scraper.info.Kik(report, username , http_proxy)
                    else:
                        pass

                    if "GitLab" in ScraperSites:
                        try:
                            Scraper.info.GitLab(report, username , http_proxy)
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")      
                            http_proxy = None
                            Scraper.info.GitLab(report, username , http_proxy)
                    else:
                        pass
                    
                    if "Wattpad" in ScraperSites:
                        try:
                            Scraper.info.Wattpad(report, username , http_proxy)
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")      
                            http_proxy = None
                            Scraper.info.Wattpad(report, username , http_proxy)
                    else:
                        pass

                    if "GitHub" in ScraperSites:
                        try:
                            Scraper.info.Github(report, username , http_proxy)
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")      
                            http_proxy = None
                            Scraper.info.Github(report, username , http_proxy)
                    else:
                        pass
                else:
                    pass
            else:
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "OPS LOOKS LIKE THERE IS NO SITE TO SCRAPE...¯\_(ツ)_/¯")
        else:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "OPS LOOKS LIKE USERNAME: {} HAS NOT BEEN FOUND ON ANY WEBSITE..¯\_(ツ)_/¯".format(username))
        count = 1
        if count == 1:
            choice = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A GOOGLE DORK ATTACK?(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                MrHolmes.Google_dork(username)
                MrHolmes.Yandex_dork(username)
            print(Font.Color.WHITE + "\nREPORT WRITTEN IN: " + os.getcwd() + "/" + report)
            f = open(report,"a")
            f.write("\nSCANNING EXECUTED WITH Mr.Holmes")
            f.close()
            Creds.Sender.mail(report, username)
