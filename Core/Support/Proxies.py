# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import random
from configparser import ConfigParser


class proxy:

    nomefile = "Configuration/Configuration.ini"
    Parser = ConfigParser()
    Parser.read(nomefile)
    Proxy_file = Parser["Settings"]["Proxy_List"]
    f = open(Proxy_file, "r")
    value = f.readlines()
    f.close()
    choice1 = random.choice(value)
    choice2 = choice1.split(":", 1)
    choice3 = choice2[0]

    final_proxis = {
        'http': "//" + choice1,
        'https': "//" + choice1,
    }
