# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0 

import random
from configparser import ConfigParser

DEFAULT_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


class Select:
   
    nomefile = "Configuration/Configuration.ini"
    parser = ConfigParser()
    parser.read(nomefile)
    useragent_file = parser.get("Settings", "useragent_List", fallback="Useragents/Useragent.txt")
    try:
        with open(useragent_file, "r") as f:
            value = [line for line in f.readlines() if line.strip()]
    except OSError:
        value = []
    agent = random.choice(value).replace("\n","") if value else DEFAULT_AGENT