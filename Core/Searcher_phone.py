import MrHolmes as holmes
import phonenumbers
import os
import requests
import urllib
import json
from datetime import datetime
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
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
    def social_engine(number,report):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        numberf = number.replace("+","")
        nomefile = "Site_lists/Phone/lists_soc_mob.txt"
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
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SEARCHING " + numberf + " ON SOCIAL MEDIA..")
        f = open(nomefile,"r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}",numberf)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "TRYING ON: {} ".format(site))
            try:
                Scanner = requests.get(site,headers=headers,proxies=http_proxy,timeout=None)
                status = str(Scanner.status_code)
                if Scanner.status_code == 200:
                    print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "PHONE NUMBER FOUND WITH STATUS CODE: {}".format(status))
                    f = open(report,"a")
                    f.write("PHONE NUMBER FOUND ON:" + site + "\n")
                    f.close()
                else:
                    print(Font.Color.RED + "[!]" + Font.Color.WHITE + "PHONE NUMBER NOT FOUND WITH STATUS CODE: {}".format(status))
            
            except Exception as e:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + "ERROR..TRYNG WITH NO PROXIES")
                Scanner = requests.get(site,headers=headers,proxies=None,timeout=None)
                status = str(Scanner.status_code)
                if Scanner.status_code == 200:
                    print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "PHONE NUMBER FOUND WITH STATUS CODE: {}".format(status))
                    f = open(report,"a")
                    f.write("\nPHONE NUMBER FOUND ON:\n" + site + "\n")
                    f.close()
                else:
                     print(Font.Color.RED + "[!]" + Font.Color.WHITE + "PHONE NUMBER NOT FOUND WITH STATUS CODE: {}".format(status))
        
        dork = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A GOOGLE-DORK SEARCH?(1)YES(2)NO"+ Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if dork == 1:
            Phone_search.Google_dork(numberf, report)
        else:
            pass
    
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
        f = open ("Site_lists/Phone/lists_phone.txt","r")
        for sites in f:
            site = sites.rstrip("\n")
            site= site.replace("{}",number)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "TRYING ON: {} ".format(site))
            try:
                Scanner = requests.get(site,headers=headers,proxies=http_proxy,timeout=None)
                status = str(Scanner.status_code)
                if Scanner.status_code == 200:
                    print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "PHONE NUMBER FOUND WITH STATUS CODE: {}".format(status))
                    f = open(report,"a")
                    f.write("PHONE NUMBER FOUND ON:" + site + "\n")
                    f.close()
                else:
                    print(Font.Color.RED + "[!]" + Font.Color.WHITE + "PHONE NUMBER NOT FOUND WITH STATUS CODE: {}".format(status))
            
            except Exception as e:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + "ERROR..TRYNG WITH NO PROXIES")
                Scanner = requests.get(site,headers=headers,proxies=None,timeout=None)
                status = str(Scanner.status_code)
                if Scanner.status_code == 200:
                    print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "PHONE NUMBER FOUND WITH STATUS CODE: {}".format(status))
                    f = open(report,"a")
                    f.write("\nPHONE NUMBER FOUND ON:\n" + site + "\n")
                    f.close()
                else:
                     print(Font.Color.RED + "[!]" + Font.Color.WHITE + "PHONE NUMBER NOT FOUND WITH STATUS CODE: {}".format(status))
            sleep (3)
        social = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A SOCIAL MEDIA SEARCH?(1)YES(2)NO"+ Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if social == 1:
            Phone_search.social_engine(number,report)
        else:
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
        print (Font.Color.GREEN + "[+]" + Font.Color.WHITE + "SCANNING NUMBER: {}...".format(username))
        sleep(4)
        FormattedPhoneNumber = "+" + username
        try:
            Phone = phonenumbers.parse(FormattedPhoneNumber, None)
        except Exception as e:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "NUMBER NOT FOUND")
        else:
            if not phonenumbers.is_valid_number(Phone):
                print("NUMBER NOT VALID")
                holmes.Main.main()

        number = phonenumbers.format_number(
                Phone, phonenumbers.PhoneNumberFormat.E164
            ).replace("+", "")
        numberCode = phonenumbers.format_number(
                Phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            ).split(" ")[0]
        numberNation = phonenumbers.region_code_for_country_code(
                int(numberCode)
            )

        localNumber = phonenumbers.format_number(
                Phone, phonenumbers.PhoneNumberFormat.E164
            ).replace(numberCode, "")
        international = phonenumbers.format_number(
                Phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )

        nation = geocoder.country_name_for_number(Phone, "en")
        location = geocoder.description_for_number(Phone, "en")
        carrierName = carrier.name_for_number(Phone, "en")

        
        print(Font.Color.YELLOW + "\n[+]" + Font.Color.WHITE + "INTERNATIONAL NUMBER: {}".format(international))
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE +"LOCAL NUMBER: {}".format(localNumber))
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE +"COUNTRY PREFIX: {}".format(numberCode))
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE +"COUNTRY CODE: {}".format(numberNation))
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE +"CARRIER/ISP: {}".format(carrierName))
        for timezoneResult in timezone.time_zones_for_number(Phone):
            print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "TIMEZONE: {}".format(timezoneResult))
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "CHECKING THE AFFIDABILITY OF THE NUMBER")
        sleep(2)
        if phonenumbers.is_possible_number(Phone):
            print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + "THIS NUMBER EXIST")
        else:
             print(Font.Color.RED + "[!]" + Font.Color.WHITE +"THIS NUMBER DOESN'T EXIST.")
        f = open(report,"a")
        f.write(Date + "\n")
        f.write("INTERNATIONAL NUMBER: " + international + "\n")
        f.write("LOCAL NUMBER: " + localNumber + "\n")
        f.write("COUNTRY PREFIX: " + numberCode + "\n")
        f.write("COUNTRY CODE: " + numberNation + "\n")
        f.write("CARRIER/ISP: " + carrierName + "\n")
        f.write("TIMEZONE: " + timezoneResult + "\n")
        f.close()
        Phone_search.lookup(username,report)
        os.system("Core/Support/./Notification.sh")
        print(Font.Color.WHITE + "\nREPORT WRITTEN IN: " + os.getcwd() + "/" + report)
        Creds.Sender.mail(report, username)
