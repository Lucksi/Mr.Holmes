# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

from Core.Support import Font
from Core.Support import Clear

class One_time:

    @staticmethod
    def Agreement():
        Clear.Screen.Clear()
        f = open("Banners/Banner1.txt","r")
        reader = f.read()
        f.close()
        print(Font.Color.GREEN + reader)
        try:
            choice=str(input(Font.Color.WHITE + "\nTHIS TOOL IS MADE ONLY FOT EDUCATIONAL AND RESEARCH PURPOUSES ONLY I DO NOT ASSUME\nANY KIND OF WARRANTY FOR ANY IMPROPE USE OF THIS TOOL USE IT WITH GOOD SENSE\n\nPRESS" + Font.Color.GREEN + "(Y)" + Font.Color.WHITE + "TO ACCEPT OR" + Font.Color.RED + "(N)" + Font.Color.WHITE + "TO DECLINE\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == "Y" or choice == "y":
                f = open("Configuration/Agreement.txt","w")
                f.write("Agreement Accepted")
                f.close()
            elif choice == "N" or choice == "n":
                print(Font.Color.RED + "\nYOU HAVE TO AGREE THIS TERME IN ORDER TO USE THIS TOOL\n")
                exit()
            else:
                One_time.Agreement
        except ValueError:
            One_time.Agreement()
