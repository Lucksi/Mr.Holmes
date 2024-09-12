# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Support import Font
from Core.Support import Language
from Core.Support import Clear


class One_time:

    @staticmethod
    def Agreement():
        Clear.Screen.Clear()
        f = open("Banners/Banner1.txt", "r")
        reader = f.read()
        f.close()
        print(Font.Color.GREEN + reader)
        filename = Language.Translation.Get_Language()
        filename
        try:
            choice = str(input(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Eula", "Text", "None") +
                         Font.Color.GREEN + "(Y)" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Eula", "Agree", "None") + Font.Color.RED + "(N)" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Eula", "Disagree", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == "Y" or choice == "y":
                f = open("Configuration/Agreement.txt", "w")
                f.write("Agreement Accepted")
                f.close()
            elif choice == "N" or choice == "n":
                print(
                    Font.Color.RED + Language.Translation.Translate_Language(filename, "Eula", "Alert", "None"))
                exit()
            else:
                One_time.Agreement()
        except ValueError:
            One_time.Agreement()
