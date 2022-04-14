# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import random
from Core.Support import Font


class Random:

    @staticmethod
    def Get_Banner(Folder):
        List = ["Banner1.txt", "Banner2.txt", "Banner3.txt"]
        choice = random.choice(List)
        f = open(Folder + "/" + choice, "r", newline=None)
        banner = f.read()
        f.close()
        print(Font.Color.GREEN + banner)
