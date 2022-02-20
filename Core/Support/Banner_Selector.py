# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import random
from Core.Support import Font
import tkinter


class Random:

    @staticmethod
    def Get_Banner(Folder):
        List = ["Banner1.txt", "Banner2.txt", "Banner3.txt"]
        screen = tkinter.Tk()
        Size = screen.winfo_screenwidth()
        screen.destroy()
        if Size <= 711:
            choice = List[2]
        else:
            choice = random.choice(List)
        f = open(Folder + "/" + choice, "r", newline=None)
        banner = f.read()
        f.close()
        print(Font.Color.GREEN + banner)
