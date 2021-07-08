import os
import urllib 
import json
from Core.Support import Font
from Core.Support import Creds
from Core.Support import Numbers
from time import sleep
from datetime import datetime


class Web:
    

    @staticmethod
    def trace(username,report):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "DOING TRACEROUTE FOR: {}...".format(username))
        command = ("traceroute " + username)
        proces = os.popen(command)
        results = str(proces.read())
        print(results)
        f = open (report,"a")
        f.write("\nTRACEROUTE SEQUENCE:" + "\r\n")
        f.write(results)
        f.close()


    @staticmethod
    def google_dork(username,report,number,num):
        nomefile = "Site_lists/Websites/Google_dorks.txt"
        format = "www." + username
        f = open (report ,"a")
        f.write("\n\nPOSSIBLE GOOGLE DORKS LINKS:\n")
        f.close()
        print(Font.Color.GREEN + "\n[+]" +Font.Color.WHITE + "GENERATING POSSIBLE GOOGLE DORKS LINK...")
        sleep(3)
        f = open(nomefile,"r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", format)
            print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + site)
            f = open(report,"a")
            f.write(site + "\n")
            sleep(2)
        f.close()
        if number == True:
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "GENERATING LINK FOR {} PHONE NUMBER {}...".format(username,num))
            phonen = "Site_lists/Websites/phoneNumbers_dork.txt"
            f = open(phonen,"r")
            for sites in f:
                site = sites.rstrip("\n")
                site = site.replace("{}", num)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + site)
                f = open(report,"a")
                f.write(site + "\n")
                sleep(2)
            f.close()
        else:
            pass
        f.close()
        choice = int(input(
            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A TRACEROUTE SCAN?(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            Web.trace(username,report)

    @staticmethod
    def whois_lookup(username,report):
        api = "Api/api_key.txt"
        f = open(api,"r")
        Key = f.read().rstrip("\n")
        f.close()
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "LOOKING FOR WHO IS INFORMATION ABOUT: {}...".format(username))
        sleep(2)
        if Key == "":
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "API KEY NOT FOUND DOING CLASSICAL WHOIS LOOKUP...")
            command = ("whois " + username)
            proces = os.popen(command)
            results = str(proces.read())
            final = results + command
            print(Font.Color.WHITE + results)
            f = open (report,"a")
            f.write("\nWEBSITE DATA:" + "\r\n")
            f.write(results)
            f.close()
	    num = None
            number = False
        else:
            try:
                print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + "API KEY FOUND..")
                Key2 = str(Key)
                source = "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={}&domainName={}&outputFormat=JSON".format(Key2,username)
                access = urllib.request.urlopen(source)
                reader = access.read()
                final = json.loads(reader)
                created = "CREATION-DATE: " + final["WhoisRecord"]["createdDate"]
                modified = "UPDATE-DATE: " + final["WhoisRecord"]["updatedDate"]
                expired = "EXPIRED-DATE: " + final["WhoisRecord"]["expiresDate"]
                domain =  "DOMAIN: " + final["WhoisRecord"]["registrant"]["name"]
                organization = "ORGANIZATION: " + final["WhoisRecord"]["registrant"]["organization"]
                nation = "NATION: " + final["WhoisRecord"]["registrant"]["country"]
                nationCode = "NATION-CODE: " + final["WhoisRecord"]["registrant"]["countryCode"]
                state= "STATE: " + final["WhoisRecord"]["registrant"]["state"]
                city = "CITY: " + final["WhoisRecord"]["registrant"]["city"]
                street = "STREET: " + final["WhoisRecord"]["registrant"]["street1"]
                email = "EMAIL: " + final["WhoisRecord"]["registrant"]["email"]
                telephone = "TELEPHONE: " + final["WhoisRecord"]["registrant"]["telephone"]
                telephone2 = final["WhoisRecord"]["registrant"]["telephone"]
                street2 = str(final["WhoisRecord"]["registrant"]["street1"])
                city2 = str(final["WhoisRecord"]["registrant"]["city"])
                link = "https://www.google.com/maps/place/{} {}".format(street2,city2)
                sleep(2)
                print(Font.Color.YELLOW + "\n[+]" + Font.Color.WHITE + created)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + modified)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + expired)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + domain)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + organization)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + nation)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + nationCode)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + state)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + city)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + street)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + email)
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + telephone)
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "GENERATING GOOGLE MAPS LINK...")
                print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + link)
                f = open(report,"a")
                f.write("\nWEBSITE DATA:" + "\r\n")
                f.write(created + "\r\n")
                f.write(modified + "\r\n")
                f.write(expired + "\r\n")
                f.write(domain + "\r\n")
                f.write(organization + "\r\n")
                f.write(nation + "\r\n")
                f.write(nationCode + "\r\n")
                f.write(state + "\r\n")
                f.write(city + "\r\n")
                f.write(street + "\r\n")
                f.write(email + "\r\n")
                f.write(telephone + "\r\n")
                f.write(link + "\r\n")
                f.close()
                num = telephone2
                if num != "":
                    number = True
                    sc= int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "PHONE NUMBER FOUND:{} WOULD YOU LIKE TO EXECUTE A SCAN(1)YES(2)NO".format(num)  + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                    if sc == 1:
                        f = open(report,"a")
                        f.write("\nPHONE NUMBER DATA:")
                        f.close()
                        print("")
                        Numbers.Phony.Number(num,report)
                    else:
                        pass
                else:
                    print(Font.Color.RED + "[!]" + Font.Color.WHITE + "PHONE NUMBER NOT FOUND")
            except Exception as e:
                num = None
                number = False
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + "OPS LOOKS LIKE SOME OF THE DETAILS ARE NOT AVAIABLE DOING CLASSICAL WHO IS...")
                command = ("whois " + username)
                proces = os.popen(command)
                results = str(proces.read())
                final = results + command
                print(Font.Color.WHITE + results)
                f = open (report,"a")
                f.write("\nWEBSITE DATA:" + "\r\n")
                f.write(results)
                f.close()
        choice = int(input(
             Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A GOOGLE DORK ATTACK?(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            Web.google_dork(username,report,number,num)
        else:
            choice = int(input(
            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A TRACEROUTE SCAN?(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                Web.trace(username,report)
    
    @staticmethod
    def search(username):
        report = "Reports/Websites/" + username + ".txt"
        f = open("Banners/Banner4.txt","r")
        banner = f.read()
        f.close()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        Date = "Date: " + str(dt_string)
        if os.path.isfile(report):
            os.remove(report)  
        source = "http://ip-api.com/json/" + username
        access = urllib.request.urlopen(source)
        content = access.read()
        final = json.loads(content)
        ip= "IP: " + final ["query"]
        country = "NATION: " + final ["country"]
        country_code = "NATION-CODE: " + final ["countryCode"]
        region = "REGION-CODE: " + final ["region"]
        regionName = "REGION-NAME: " + final ["regionName"]
        city = "CITY: " + final ["city"]
        timezone = "TIMEZONE: " + final ["timezone"]
        isp = "ISP: " + final ["isp"]
        org = "ORG: " + final ["org"]
        asp = "AS: " + final ["as"]
        lat2 = str(final["lat"])
        final_lat = "LAT: {}".format(lat2)
        lon2 = str(final["lon"])
        final_lon = "LONG: {}".format(lon2)
        zip_data = "ZIP/POSTAL-CODE: " + final ["zip"]
        link = "https://www.google.com/maps/place/{},{}".format(lat2,lon2)
		
		
        os.system("cls" if os.name == "nt" else "clear")
        print(Font.Color.GREEN + banner)
        print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + "SEARCH INFORMATION FOR: {}".format(username))
        sleep(3)
        print(Font.Color.YELLOW + "\n[+]" + Font.Color.WHITE + ip)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + country)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + country_code)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + region)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + regionName)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + city)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + timezone)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + isp)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + org)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + asp)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + final_lat)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + final_lon)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + zip_data)
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "GENERATING GOOGLE MAPS LINK...")
        sleep(2)
        print(Font.Color.YELLOW + "[+]" + Font.Color.WHITE + link)
        f = open(report,"a")
        f.write("SCANNING EXECUTED ON:\n" + Date + "\r\n")
        f.write(ip + "\r\n")
        f.write(country + "\r\n")
        f.write(country_code + "\r\n")
        f.write(region + "\r\n")
        f.write(regionName + "\r\n")
        f.write(city + "\r\n")
        f.write(timezone + "\r\n")
        f.write(isp + "\r\n")
        f.write(org + "\r\n")
        f.write(asp + "\r\n")
        f.write(final_lat + "\r\n")
        f.write(final_lon + "\r\n")
        f.write(zip_data + "\r\n")
        f.write("\nGOOGLE MAPS LINK:\r\n")
        f.write(link + "\r\n")
        f.write
        f.close()
        choice = int(input(
            Font.Color.BLUE + " \n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A WHO-IS LOOKUP?(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if choice == 1:
            Web.whois_lookup(username,report)
       
        else:
            choice = int(input(
            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO PERFORM A TRACEROUTE SCAN?(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                Web.trace(username,report)

        os.system("Core/Support/./Notification.sh")
        print(Font.Color.WHITE + "\nREPORT WRITTEN IN: " + os.getcwd() + "/" + report)
        Creds.Sender.mail(report, username)
