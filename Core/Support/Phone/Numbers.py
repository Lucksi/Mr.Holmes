# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import phonenumbers
import MrHolmes as holmes
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from Core.Support import Font
from Core.Support import Language
from time import sleep

filename = Language.Translation.Get_Language()
filename


class Phony:

    def Number(num, report, code):
        print(Font.Color.GREEN +
              "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Phone", "Scan", "None").format(num))
        sleep(4)
        FormattedPhoneNumber = "+" + num
        try:
            Phone = phonenumbers.parse(FormattedPhoneNumber, None)
        except Exception as e:
            inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                        Language.Translation.Translate_Language(filename, "Phone", "NotFound2", "None"))
            holmes.Main.Menu()
        else:
            if not phonenumbers.is_valid_number(Phone):
                reality = (Language.Translation.Translate_Language(
                    filename, "Phone", "NoReal", "None"))

            reality = Language.Translation.Translate_Language(
                filename, "Phone", "Real", "None")
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

            for timezoneResult in timezone.time_zones_for_number(Phone):
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "TIMEZONE: {}".format(timezoneResult))

            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Phone", "Affidability", "None"))
            sleep(2)
            if phonenumbers.is_possible_number(Phone):
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Phone", "Exist", "None"))
            else:
                print(Font.Color.RED +
                      "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Phone", "NoExist", "None"))

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
