# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import random
from Core.Support import Font


class Random:

    @staticmethod
    def Get_Banner(Folder,Mode):
        List = ["Banner1.txt", "Banner2.txt", "Banner3.txt"]
        if Mode == "Desktop":
            choice = random.choice(List)
        elif Mode == "Mobile":
            choice = List[2]
        else:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "LOOKS LIKE THERE IS AN INVALID OPTION ACCEPTED ONLY 'Desktop' OR 'Mobile' EXIT...")
            exit()
        f = open(Folder + "/" + choice, "r", newline=None)
        banner = f.read()
        f.close()
        print(Font.Color.GREEN + banner)