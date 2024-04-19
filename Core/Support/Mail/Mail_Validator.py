# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import re as Regex
from Core.Support import Font
from Core.Support import Language
from time import sleep

filename = Language.Translation.Get_Language()
filename

class Validator:

      @staticmethod
      def Mail(username, report):
            print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                 Language.Translation.Translate_Language(filename, "Email", "Check", "None").format(username))
            simbols = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            sleep(3)
            if Regex.fullmatch(simbols, username):
                  print(Font.Color.YELLOW + "[v]" +
                        Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Valid", "None"))
                  f = open(report, "a")
                  f.write("\n\nTHIS EMAIL IS VALID")
                  f.close()
                  Valid = True

            else:
                  simbols = r'/^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i;'
                  if Regex.fullmatch(simbols, username):
                        print(Font.Color.YELLOW + "[v]" +
                              Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Valid", "None"))
                        f = open(report, "a")
                        f.write("\n\nTHIS EMAIL IS VALID")
                        f.close()
                        Valid = True
                  else:
                        print(Font.Color.RED +
                              "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "NotValid", "None"))
                        f = open(report, "a")
                        f.write("\n\nTHIS EMAIL IS NOT VALID")
                        f.close()
                        inp = input(Language.Translation.Translate_Language(filename, "Default", "Continue", "None"))
                        Valid = False
            return Valid
