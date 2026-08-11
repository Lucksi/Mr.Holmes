# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
from configparser import ConfigParser

class Check:

    @staticmethod 
    def WhoIs():
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        config_file = os.path.join(base_dir, "Configuration", "Configuration.ini")
        parser = ConfigParser()
        parser.read(config_file)
        return parser.get("Settings", "api_key", fallback="None")