# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import os
import urllib
import json
from datetime import datetime
from Core.Support import Numbers
from Core.Support import Font
from Core.Support import Creds
from Core.Support import Proxies
from Core.Support import Requests_Search
from Core.Support import Clear
from Core.Support import Dorks
from time import sleep


class Phone_search:

    @staticmethod
    def Banner():
        Clear.Screen.Clear()
        f = open("Banners/Banner3.txt")
        banner = f.read()
        f.close()
        print(Font.Color.GREEN + banner)

    @staticmethod
    def Google_dork(username):
        report = "GUI/Reports/Phone/Dorks/{}_dorks.txt".format(username)
        nomefile = "Site_lists/Phone/Google_dorks.txt"
        fingerprints = "Site_lists/Phone/Fingerprints.txt"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "REMOVING OLD {}_Dorks.txt".format(username))
        else:
            pass
        Type = "GOOGLE"
        Dorks.Search.dork(username, report, nomefile, Type)
        f = open(report, "a")
        f.write("\nPOSSIBLE PHONE-FINGERPRINTS LINKS ON SOCIAL MEDIAS:\n")
        f.close()
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "GENERATING POSSIBLE PHONE-FINGERPRINTS LINK ON SOCIAL MEDIAS...")
        sleep(3)
        f = open(fingerprints, "r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", username)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + site)
            f = open(report, "a")
            f.write(site + "\n")
            sleep(2)
        f.close()
        f.close()
      
    @staticmethod
    def Yandex_dork(username):
        report = "GUI/Reports/Phone/Dorks/{}_dorks.txt".format(username)
        nomefile = "Site_lists/Phone/Yandex_dorks.txt"
        fingerprints = "Site_lists/Phone/Yandex_Fingerprints.txt"
        Type = "YANDEX"
        Dorks.Search.dork(username, report, nomefile, Type)
        f = open(report, "a")
        f.write("\nPOSSIBLE PHONE-FINGERPRINTS LINKS ON SOCIAL MEDIAS:\n")
        f.close()
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              "GENERATING POSSIBLE PHONE-FINGERPRINTS LINK ON SOCIAL MEDIAS...")
        sleep(3)
        f = open(fingerprints, "r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", username)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + site)
            f = open(report, "a")
            f.write(site + "\n")
            sleep(2)
        f.close()
        f.close()

    @staticmethod
    def lookup(username,report):
        f = open(report, "a")
        f.write("\nPHONE NUMBER FOUND ON:\n")
        f.close()
        f = open("Temp/Code.txt","r", newline=None)
        nation= f.read().rstrip("\n")
        f.close()
        if nation == "US":
            data = "Site_lists/Phone/Lookup/USA_phone.json"
            country = "UNITED-STATES"
            token = True
        elif nation == "IT":
            data = "Site_lists/Phone/Lookup/ITA_phone.json"
            country = "ITALY"
            token = True
        elif nation == "DE":
            data = "Site_lists/Phone/Lookup/DEU_phone.json"
            country = "GERMANY"
            token = True
        elif nation == "FR":
            data = "Site_lists/Phone/Lookup/FRA_phone.json"
            country = "FRANCE"
            token = True
        elif nation == "RO":
            data = "Site_lists/Phone/Lookup/ROU_phone.json"
            country = "ROMANIA"
            token = True
        elif nation == "CH":
            data = "Site_lists/Phone/Lookup/SWIS_phone.json"
            country = "SWITZERLAND"
            token = True
        else:
            token = True
            data = "Site_lists/Phone/Lookup/Undefined.json"
            country = "UNDEFINED"
        number = str(username)
        os.remove("Temp/Code.txt")
        subject = "PHONE-NUMBER"
        print(Font.Color.YELLOW + "\n[+]" + Font.Color.WHITE + "PHONE NUMBER COUNTRY:{}".format(country))
        if token:
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SEARCHING PHONE NUMBER ON DIFFERENT SITES")
           
            sc = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO USE A PROXY 'IT MAY CAUSE SOME PROBLEMS AND THE PROCESS WILL SLOW DOWN'(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if sc == 1:
                http_proxy = Proxies.proxy.final_proxis
                http_proxy2 = Proxies.proxy.choice3
                source = "http://ip-api.com/json/" + http_proxy2
                access = urllib.request.urlopen(source)
                content = access.read()
                final = json.loads(content)
                identity = "YOUR PROXY IP IS LOCATED IN: {} ({}) ".format(final ["regionName"],final["country"])
            else:
                http_proxy = None
                http_proxy2 = str(http_proxy)
                identity="None"
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "YOUR PROXY IP ADDRES IS: {} ".format(http_proxy2))
            if identity != "None":
                print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + identity)
            else:
                pass
            
            successfull = []
            successfullName = []
            ScraperSites = []
            Writable = True
            f = open (data,)
            data = json.loads(f.read())
            for sites in data:
                for data1 in sites:
                    name = sites[data1]["name"]    
                    if name == "CarteTelefonae":
                        username = username.replace("40","")
                    site1 = sites[data1]["url"].replace("{}",username)
                    site2 = sites[data1]["url2"].replace("{}",username)
                    main = sites[data1]["main"]
                    error = sites[data1]["Error"]
                    is_scrapable = sites[data1]["Scrapable"]
                    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "TRYING ON: {} ".format(name))
                    try:
                        Requests_Search.Search.search(error,report,site1,site2,http_proxy,sites,data1,username,subject,successfull,name,successfullName,is_scrapable,ScraperSites,Writable,main)
                    except Exception as e:
                        print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "CONNECTION-ERROR...TRYNG WITH NO PROXIES")
                        http_proxy = None
                        try:
                            Requests_Search.Search.search(error,report,site1,site2,http_proxy,sites,data1,username,subject,successfull,name,successfullName,is_scrapable,ScraperSites,Writable,main)
                        except Exception as e:
                            print(Font.Color.BLUE + "\n[N]"+ Font.Color.WHITE + "CANNOT REACH THIS SITE SKIPPING...")
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "{}: {} FOUNDS ON:".format(subject,username))
            
            if len(successfull):
                for names in successfull:
                    print(Font.Color.YELLOW +"[v]" + Font.Color.WHITE +  names)

        else:
            print(Font.Color.BLUE + "\n[N]" + Font.Color.WHITE + "OPS LOOKS LIKE THERE IS NO LOOKUP FILE FOR NOW..SKIPPING")
        
        sleep (3)
        dork = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A GOOGLE-DORK SEARCH?(1)YES(2)NO"+ Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if dork == 1:
            Phone_search.Google_dork(username)
            Phone_search.Yandex_dork(username)
        else:
            pass

    @staticmethod
    def searcher(username):
        Phone_search.Banner()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        Date = "Date: " + str(dt_string)
        report = "GUI/Reports/Phone/" + username + ".txt"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "REMOVING OLD {}.txt".format(username))
        f = open(report,"w")
        f.write("SCANNING EXECUTED ON:\n" + Date + "\n")
        f.close()
        num = username
        code = 1
        Numbers.Phony.Number(num,report,code)
        Phone_search.lookup(username,report)
        print(Font.Color.WHITE + "\nREPORT WRITTEN IN: " + os.getcwd() + "/" + report)
        f = open(report,"a")
        f.write("\nSCANNING EXECUTED WITH Mr.Holmes")
        f.close()
        Creds.Sender.mail(report, username)
