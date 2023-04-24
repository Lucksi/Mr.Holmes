# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Support import Font
from Core.Support import Language
from time import sleep

filename = Language.Translation.Get_Language()
filename


class Search:

    @staticmethod
    def dork(username, report, nomefile, Type):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Dorks", "Generation", "None").format(Type))
        sleep(2)
        username = username.replace(" ","+")
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

    @staticmethod
    def Generator(Type,nomefile,report,phrase,data,between,seconddata):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Dorks", "Generation", "None").format(Type))
        sleep(2)
        if Type == "YANDEX":
            if "before:" in data:
                data = data.replace("before:+","date:<")
            elif "after" in data:
                data = data.replace("+after:","date:>")
            if between == "True":
                seconddata = seconddata.replace("before","")
                seconddata = seconddata.replace("+after","")
                data = "date:"+ seconddata
            else:
                pass
            data = data.replace("/","")
        phrase = phrase.replace(" ","+")
        f = open(report, "a")
        f.write("\n" + Type + "-DORKS:\n\n")
        f.close()
        f = open(nomefile, "r")
        for sites in f:
            site = sites.rstrip("\n")
            site = site.replace("{}", phrase).replace(")","){}".format(data))
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + site)
            sleep(2)
            f = open(report, "a")
            f.write(site + "\n")
        f.close()
        f.close()
        print(Font.Color.WHITE + Language.Translation.Translate_Language(filename,
              "Default", "Report", "None") + report)

