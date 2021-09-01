# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import requests
from Core.Support import Font

class Search:
    
    @staticmethod
    def search(error,report,site1,site2,http_proxy,sites,data1,username,subject,successfull,name,successfullName,is_scrapable,ScraperSites,Writable,main):
       
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        searcher = requests.get(url=site2, headers=headers, proxies=http_proxy, timeout=None, allow_redirects=True)
        f = open(report, "a")
        if error == "Status-Code":
            if searcher.status_code == 200:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "{}: {} FOUND".format(subject,username))
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}".format(site1))
                if Writable == True:
                    f.write(site1 + "\r\n")
                else:
                    f.write("{}:{}\r\n".format(name,main))
                successfull.append(site1)
                successfullName.append(name)
                if is_scrapable == "True":
                    ScraperSites.append(name)
            elif searcher.status_code == 404 or searcher.status_code == 204:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + "{}: {} NOT FOUND".format(subject,username))      
            else:
                print(Font.Color.BLUE + "[N]" + Font.Color.WHITE + "CONNECTION-ERROR...")
        elif error == "Message":
            text = sites[data1]["text"]
            if  text in searcher.text:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + "{}: {} NOT FOUND".format(subject,username))
            else:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "{}: {} FOUND".format(subject,username))
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}".format(site1))
                if Writable == True:
                    f.write(site1 + "\r\n")
                else:
                    f.write("{}:{}\r\n".format(name,main))
                successfull.append(site1)
                successfullName.append(name)
                if is_scrapable == "True":
                    ScraperSites.append(name)
            
        elif error == "Response-Url":
            response = sites[data1]["response"]
            if searcher.url == response:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + "{}: {} NOT FOUND".format(subject,username))
            else:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "{}: {} FOUND".format(subject,username))
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}".format(site1))
                if Writable == True:
                    f.write(site1 + "\r\n")
                else:
                    f.write("{}:{}\r\n".format(name,main))
                successfull.append(site1)
                successfullName.append(name)
                if is_scrapable == "True":
                    ScraperSites.append(name)