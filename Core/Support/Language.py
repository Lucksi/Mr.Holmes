# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2022-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import json
import os
from configparser import ConfigParser


class Translation:

    @staticmethod
    def _config_path():
        return os.path.join("Configuration", "Configuration.ini")

    @staticmethod
    def Get_Language():
        Parser = ConfigParser()
        Parser.read(Translation._config_path())
        try:
            Lang = Parser["Settings"]["language"]
        except (KeyError, TypeError, ValueError):
            Lang = "english"
        filename = "Lang/{}.json".format(Lang)
        if os.path.isfile(filename):
            filename = filename
        else:
            filename = "Lang/english.json"
        return filename

    @staticmethod
    def Translate_Language(filename, List, Row, SubRow):
        reader = open(filename, )
        parser = json.loads(reader.read())
        try:
            if List == "Configuration" or List == "Username" or List == "Website" or List == "Report":
                Phrase = parser[List][0][Row][SubRow]
            else:
                Phrase = parser[List][Row]
            return Phrase
        except Exception as e:
            filename = "Lang/english.json"
            reader = open(filename, )
            parser = json.loads(reader.read())
            if List == "Configuration" or List == "Username" or List == "Website" or List == "Report":
                Phrase = parser[List][0][Row][SubRow]
            else:
                Phrase = parser[List][Row]
            return Phrase
    
    @staticmethod
    def Get_Language2():
        Parser = ConfigParser()
        Parser.read(Translation._config_path())
        try:
            Lang = Parser["Settings"]["language"]
        except (KeyError, TypeError, ValueError):
            Lang = "english"
        filename = "Lang/{}.json".format(Lang)
        if os.path.isfile(filename):
            Lang = Lang.upper()
            if Lang == "FRENCH":
                Lang = Lang + " "
        else:
            Lang = "ENGLISH"
        return Lang