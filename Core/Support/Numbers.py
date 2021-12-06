# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import phonenumbers
import MrHolmes as holmes
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from Core.Support import Font 
from time import sleep
 
 
class Phony:
   
    def Number(num,report,code):
        print (Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCANNING NUMBER: {}...".format(num))
        sleep(4)
        FormattedPhoneNumber = "+" + num
        try:
            Phone = phonenumbers.parse(FormattedPhoneNumber, None)
        except Exception as e:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "NUMBER NOT FOUND...PRESS ENTER TO CONTINUE")
                holmes.Main.Menu()
        else:
            if not phonenumbers.is_valid_number(Phone):
                reality = ("THIS IS PROBABLY NOT A REAL PHONE-NUMBER")
                
            reality = "THIS IS PROBABLY A REAL PHONE NUMBER"
            print(Font.Color.BLUE + "[I]" + Font.Color.WHITE + reality)
            
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
            
                    
            print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE + "INTERNATIONAL NUMBER: {}".format(international))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +"LOCAL NUMBER: {}".format(localNumber))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +"COUNTRY PREFIX: {}".format(numberCode))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +"COUNTRY CODE: {}".format(numberNation))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +"COUNTRY: {}".format(nation))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +"AREA/ZONE: {}".format(location))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +"CARRIER/ISP: {}".format(carrierName))
            
            for timezoneResult in timezone.time_zones_for_number(Phone):
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "TIMEZONE: {}".format(timezoneResult))
            
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "CHECKING THE AFFIDABILITY OF THE NUMBER")
            sleep(2)
            if phonenumbers.is_possible_number(Phone):
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "THIS NUMBER EXIST OR IS A VOIP NUMBER")
            else:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE +"THIS NUMBER DOESN'T EXIST.")
            
            f = open(report,"a")
            f.write("INTERNATIONAL NUMBER: " + international + "\n")
            f.write("LOCAL NUMBER: " + localNumber + "\n")
            f.write("COUNTRY PREFIX: " + numberCode + "\n")
            f.write("COUNTRY CODE: " + numberNation + "\n")
            f.write("COUNTRY:" + nation + "\n")
            f.write("AREA/ZONE" + location + "\n")
            f.write("CARRIER/ISP: " + carrierName + "\n")
            f.write("TIMEZONE: " + timezoneResult + "\n")
            f.close()
            
            if code == 0:
                 pass
            elif code == 1:
                f = open("Temp/Code.txt","w")
                f.write(numberNation)
                f.close()
