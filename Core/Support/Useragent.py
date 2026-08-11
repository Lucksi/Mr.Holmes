# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0 

import os
import random
from configparser import ConfigParser


class Select:
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    nomefile = os.path.join(base_dir, "Configuration", "Configuration.ini")
    default_useragent_file = os.path.join(base_dir, "Useragents", "Useragent.txt")
    parser = ConfigParser()
    parser.read(nomefile)
    useragent_file = parser.get("Settings", "useragent_list", fallback=default_useragent_file)
    if not os.path.isabs(useragent_file):
        useragent_file = os.path.join(base_dir, useragent_file)
    try:
        with open(useragent_file, "r") as useragent_handle:
            value = [line.strip() for line in useragent_handle if line.strip()]
    except OSError:
        value = []
    agent = random.choice(value) if value else "Mozilla/5.0"