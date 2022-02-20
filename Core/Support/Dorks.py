# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import requests
from Core.Support import Font
from Core.Support import Language
from time import sleep
from bs4 import BeautifulSoup as soup

filename = Language.Translation.Get_Language()
filename


class Search:
    
    @staticmethod
    def Download(username):
        Google_url = "https://www.google.com/search?&q=intext:{} filetype:txt OR filetype:docx OR filetype:pdf"
        Yandex_url = ""
        Direct = requests.get(Google_url,allow_redirects=True)
         

    @staticmethod
    def dork(username, report, nomefile, Type):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Dorks", "Generation", "None").format(Type))
        sleep(2)
        f = open(report, "a")
        f.write(Type + "-DORKS:\n\n")
        f.close()
        f = open(nomefile, "r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", username)
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + site)
            sleep(2)
            f = open(report, "a")
            f.write(site + "\n")
        f.close()
        f.close()
        print(Font.Color.WHITE + Language.Translation.Translate_Language(filename,
              "Default", "Report", "None") + report)
