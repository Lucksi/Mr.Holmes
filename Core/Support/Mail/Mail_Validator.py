# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import re as Regex
from Core.Support import Font
from time import sleep


class Validator:

      @staticmethod
      def Mail(username, report):
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                  "CHECKING IF {} IS A VALID EMAIL".format(username))
            simbols = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            sleep(3)
            if Regex.fullmatch(simbols, username):
                  print(Font.Color.YELLOW + "[v]" +
                        Font.Color.WHITE + "THIS EMAIL IS VALID")
                  f = open(report, "a")
                  f.write("\n\nTHIS EMAIL IS VALID")
                  f.close
                  f = open("Temp/E-Mail/Code.txt", "w")
                  f.write("Is-Valid")
                  f.close()
            else:
                  print(Font.Color.RED +
                        "[!]" + Font.Color.WHITE + "THIS EMAIL IS NOT VALID")
                  f = open(report, "a")
                  f.write("\n\nTHIS EMAIL IS NOT VALID")
                  f.close()
                  inp = input("\nPRESS ENTER TO CONTINUE")
