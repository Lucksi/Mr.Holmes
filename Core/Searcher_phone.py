import os
import requests
import urllib
import json
from datetime import datetime
from Core.Support import Numbers
from Core.Support import Font
from Core.Support import Creds
from Core.Support import Proxies
from time import sleep


class Phone_search:
    @staticmethod
    def Google_dork(numberf,report):
        nomefile = "Site_lists/Phone/Google_dorks.txt"
        f = open (report ,"a")
        f.write("\nPOSSIBLE GOOGLE DORKS LINKS:\n")
        f.close()
        print(Font.Color.GREEN + "\n[+]" +Font.Color.WHITE + "GENERATING POSSIBLE GOOGLE DORKS LINK...")
        sleep(3)
        f = open(nomefile,"r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", numberf)
            print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + site)
            f = open(report,"a")
            f.write(site + "\n")
            sleep(2)
        f.close()
        f.close()

    @staticmethod
    def lookup(username,report):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SEARCHING PHONE NUMBER ON DIFFERENT SITES")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        number = str(username)
        sc = int(input(
            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO USE A PROXY 'IT MAY CAUSE SOME PROBLEMS AND THE PROCESS WILL SLOW DOWN'(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
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
        succ = 0
        failed = 0
        f = open(report, "a")
        f.write("\nPHONE NUMBER FOUND ON:")
        f.close()
        f = open ("Site_lists/Phone/list_phone.json",)
        data = json.loads(f.read())
        for sites in data:
            for data1 in sites:
                site1 = sites[data1]["url"].replace("{}",username)
                name = sites[data1]["name"]
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "TRYING ON: {} ".format(name))
                try:
                    searcher = requests.get(site1, headers=headers, proxies=http_proxy, timeout=None)
                    status = str(searcher.status_code)
                    f = open(report, "a")
                    if searcher.status_code == 200:
                        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "PHONE-NUMBER: {} FOUND WITH STATUS CODE:".format(username) + status)
                        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "LINK: {}".format(site1))
                        f.write(site1 + "\r\n")
                        succ = succ + 1
                        succ2 = str(succ)
                    else:
                        print(Font.Color.RED + "[!]" + Font.Color.WHITE + "PHONE-NUMBER: {} NOT FOUND WITH STATUS CODE:".format(username) + status)
                        failed = failed + 1
                        failed2 = str(failed)
                except Exception as e:
                    print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ERROR..TRYNG WITH NO PROXIES")
                    searcher = requests.get(site1, headers=headers, proxies=None, timeout=None)
                    status = str(searcher.status_code)
                    f = open(report, "a")
                    if searcher.status_code == 200:
                        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "PHONE-NUMBER: {} FOUND WITH STATUS CODE:".format(username) + status)
                        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "LINK: {}".format(site1))
                        f.write(site1 + "\r\n")
                        succ = succ + 1
                        succ2 = str(succ)
                    else:
                        print(Font.Color.RED + "[!]" + Font.Color.WHITE + "PHONE-NUMBER:{} NOT FOUND WITH STATUS CODE:".format(username) + status)
                        failed = failed + 1
                        failed2 = str(failed)
        f.close()
        sleep (3)
        dork = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A GOOGLE-DORK SEARCH?(1)YES(2)NO"+ Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if dork == 1:
            Phone_search.Google_dork(number, report)
        else:
            pass

    @staticmethod
    def searcher(username):
        os.system("clear")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        Date = "Date: " + str(dt_string)
        f = open("Banners/Banner3.txt")
        banner = f.read()
        f.close()
        print(Font.Color.GREEN + banner)
        report = "Reports/Phone/" + username + ".txt"
        if os.path.isfile(report):
            os.remove(report)
        f = open(report,"w")
        f.write("SCANNING EXECUTED ON:\n" + Date + "\n")
        f.close()
        num = username
        Numbers.Phony.Number(num,report)
        Phone_search.lookup(username,report)
        os.system("Core/Support/./Notification.sh")
        print(Font.Color.WHITE + "\nREPORT WRITTEN IN: " + os.getcwd() + "/" + report)
        Creds.Sender.mail(report, username)