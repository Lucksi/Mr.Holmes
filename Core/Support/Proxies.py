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
    Proxy_file = Parser.get("Settings", "Proxy_List", fallback="Proxies/Proxy_list.txt")
    try:
        with open(Proxy_file, "r") as f:
            value = [line.strip() for line in f.readlines() if line.strip()]
    except OSError:
        value = []
    choice1 = random.choice(value) if value else ""
    choice2 = choice1.split(":", 1)
    choice3 = choice2[0]

    # requests needs a scheme; the old "//host:port\n" value was never a valid proxy URL
    proxy_url = choice1 if "://" in choice1 else "http://" + choice1
    final_proxis = {
        'http': proxy_url,
        'https': proxy_url,
    } if choice1 else None
