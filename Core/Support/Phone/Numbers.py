# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import phonenumbers
import MrHolmes as holmes
import json
import urllib
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from Core.Support import Font
from Core.Support import Language
from Core.Support import Map
from time import sleep

filename = Language.Translation.Get_Language()
filename


class Phony:

    @staticmethod
    def Get_GeoLocation(zone, param1, param2, jsonfile, num, Type):
        req = "https://nominatim.openstreetmap.org/search.php?q={}&format=json".format(
            zone)
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Phone", "Geo", "None").format(num))
        sleep(2)
        url = urllib.request.urlopen(req)
        try:
            Reader = url.read()
            parser = json.loads(Reader)
            Lat = parser[0]["lat"]
            Lon = parser[0]["lon"]
            data = {
                "Geolocation": {
                    "Latitude": Lat,
                    "Longitude": Lon
                }
            }
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  "LATITUDE:" + Font.Color.GREEN + " {}".format(Lat))
            sleep(2)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  "LONGITUDE:" + Font.Color.GREEN + " {}".format(Lon))
            sleep(2)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  "GOOGLE MAPS LINK: https://www.google.it/maps/place/{},{}".format(Lat, Lon))
            datafile = open(jsonfile, "a", encoding="utf-8")
            json.dump(data, datafile,
                      ensure_ascii=False, indent=4)
            datafile.close()
            Map.Creation.mapPhone(jsonfile, Lat, Lon, num, Type)

        except Exception as e:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                filename, "Phone", "NoGeo", "None") + str(e))
            pass

    @staticmethod
    def Number(num, report, code, Mode, Type, username):
        phoneList=[]
        print(Font.Color.GREEN +
              "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Phone", "Scan", "None").format(num))
        sleep(4)
        FormattedPhoneNumber = "+" + num
        try:
            Phone = phonenumbers.parse(FormattedPhoneNumber, None)
        except Exception as e:
            inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                        Language.Translation.Translate_Language(filename, "Phone", "NotFound2", "None"))
            holmes.Main.Menu(Mode)
        else:
            if not phonenumbers.is_valid_number(Phone):
                reality = (Language.Translation.Translate_Language(
                    filename, "Phone", "NoReal", "None"))
            else:
                reality = Language.Translation.Translate_Language(
                    filename, "Phone", "Real", "None")
                print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + reality)

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

            print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE +
                  "INTERNATIONAL NUMBER: {}".format(international))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "LOCAL NUMBER: {}".format(localNumber))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  "COUNTRY PREFIX: {}".format(numberCode))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  "COUNTRY CODE: {}".format(numberNation))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "COUNTRY: {}".format(nation))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "AREA/ZONE: {}".format(location))
            print(Font.Color.YELLOW +
                  "[v]" + Font.Color.WHITE + "CARRIER/ISP: {}".format(carrierName))
            i = 1
            for timezoneResult in timezone.time_zones_for_number(Phone):
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "TIMEZONE N°{}: {}".format(i, timezoneResult))
                i = i+1
            sleep(2)
            if location != "":
                jsonfile = report.replace(
                    num + ".txt", "Area_GeoLocation.json")
                if " " in location:
                    zone = location.split(" ", 1)[1]
                else:
                    zone = location
                print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Phone", "Area", "None"))
                try:
                    Phony.Get_GeoLocation(zone, "Lat", "Long", jsonfile, num, Type)
                except Exception as e:
                    print(Font.Color.RED + "[!]" + Font.Color.WHITE + "SOMETHING WENT WRONG")
                    pass
            else:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Phone", "NoArea", "None"))
            zone = timezoneResult.split("/", 1)[-1]

            if zone != "Unknown":
                print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Phone", "Zone", "None"))
                jsonfile = report.replace(
                    num + ".txt", "Zone_GeoLocation.json")
                Phony.Get_GeoLocation(zone, "Lat", "Long", jsonfile, num, Type)

            else:
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Phone", "NoZone", "None").format(number))
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Phone", "Affidability", "None"))
            sleep(2)
            if phonenumbers.is_possible_number(Phone):
                print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Phone", "Exist", "None"))
            else:
                print(Font.Color.RED +
                      "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Phone", "NoExist", "None"))

            f = open(report, "a")
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
                f = open("Temp/Phone/Code.txt", "w")
                f.write(numberNation)
                f.close()
            formatted2 = str(international).replace(numberCode,"").replace(" ","-")
            formatted3 = formatted2.replace("-","",1)
            formatted4 = str(international).replace(numberCode,"0").replace(" ","")
            formatted1 = "(%2B{}){}".format(numberCode,str(formatted2).replace("-","",1))
            formatted5 = formatted4.replace("0","")
            phoneList.append(formatted1)
            phoneList.append(formatted2)
            phoneList.append(formatted4)
            phoneList.append(formatted5)
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "FORMATTING PHONE NUMBER...")
            sleep(2)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "INTERNATIONAL-FORMAT: "+ international)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "RFC3966-FORMAT: "+ formatted1.replace("%2B",""))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LOCAL-FORMAT: " + formatted3)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LOCAL-FORMAT(2): " + formatted4)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
            "LOCAL-FORMAT(3): " + formatted5)
            return phoneList
