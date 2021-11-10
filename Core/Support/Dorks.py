# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

from Core.Support import Font
from time import sleep

class Search:

    @staticmethod
    def dork(username,report,nomefile,Type):
        print(Font.Color.GREEN + "\n[+]" +Font.Color.WHITE + "GENERATING POSSIBLE {} DORKS LINK...".format(Type))
        sleep(2)
        f = open(report,"a")
        f.write(Type + "-DORKS:\n\n")
        f.close()
        f = open(nomefile,"r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", username)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + site)
            sleep(2)
            f = open(report,"a")
            f.write(site + "\n")
        f.close()
        f.close()
        print(Font.Color.WHITE + "\nREPORT WRITTEN IN: {}".format(report))