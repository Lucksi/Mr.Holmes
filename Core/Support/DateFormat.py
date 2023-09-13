# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from configparser import ConfigParser
from Core.Support import Font
from Core.Support import Language

filename = Language.Translation.Get_Language()
filename

class Get:

    @staticmethod
    def Format():
        Config_file = "Configuration/Configuration.ini"
        Parser = ConfigParser()
        Parser.read(Config_file)
        dataformat = Parser["Settings"]["date_format"]
        if dataformat == "eu":
            dateregex = "%d/%m/%Y %H:%M:%S"
            localformat = "DD/MM/YYYY" 
        elif dataformat == "us":
            dateregex = "%m/%d/%Y %H:%M:%S"
            localformat = "MM/DD/YYYY"
        elif dataformat == "as":
            dateregex = "%Y/%m/%d %H:%M:%S"
            localformat = "YYYY/MM/DD"
        else:
            dateregex = "%d/%m/%Y %H:%M:%S"
        Zone = dataformat.upper() + ":"+ localformat
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "DateFormat", "None").format("[" + Font.Color.GREEN + Zone + Font.Color.WHITE + "]")) 
        return dateregex  
    
    @staticmethod
    def Format2():
        Config_file = "Configuration/Configuration.ini"
        Parser = ConfigParser()
        Parser.read(Config_file)
        dataformat = Parser["Settings"]["date_format"]
        if dataformat == "eu":
            dateregex = "%d/%m/%Y"
        elif dataformat == "us":
            dateregex = "%m/%d/%Y"
        elif dataformat == "as":
            dateregex = "%Y/%m/%d"
        else:
            dateregex = "%d/%m/%Y"
        return dateregex

    @staticmethod
    def Continent():
        Config_file = "Configuration/Configuration.ini"
        Parser = ConfigParser()
        Parser.read(Config_file)
        dataformat = Parser["Settings"]["date_format"]
        if dataformat == "eu":
            continent = "EUROPE         |"
        elif dataformat == "us":
            continent = "AMERICA        |"
        elif dataformat == "as":
            continent = "ASIA           |"
        else:
            continent = "EUROPE         |"
        return continent   