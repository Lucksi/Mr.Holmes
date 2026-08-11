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

    @staticmethod
    def _read_values():
        try:
            with open(proxy.Proxy_file, "r", encoding="utf-8") as handle:
                return [line.strip() for line in handle if line.strip() and not line.startswith("#")]
        except Exception:
            return []

    @staticmethod
    def rotate():
        value = proxy._read_values()
        if not value:
            return None, "None"
        choice1 = random.choice(value)
        choice2 = choice1.split(":", 1)
        choice3 = choice2[0]
        final_proxis = {
            'http': "http://" + choice1,
            'https': "http://" + choice1,
        }
        return final_proxis, choice3

    @staticmethod
    def current():
        value = proxy._read_values()
        if not value:
            return None, "None"
        choice1 = random.choice(value)
        choice2 = choice1.split(":", 1)
        choice3 = choice2[0]
        return {
            'http': "http://" + choice1,
            'https': "http://" + choice1,
        }, choice3

    choice1 = "None"
    choice2 = ["None", "None"]
    choice3 = "None"
    final_proxis = {
        'http': "http://None",
        'https': "http://None",
    }
