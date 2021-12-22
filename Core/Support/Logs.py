# AUTHOR: Luca Garofalo (Lucksi)
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import logging
from configparser import ConfigParser
from Core.Support import Font


class Log:

    @staticmethod
    def Checker(username, folder):
        nomefile = "Configuration/Configuration.ini"
        Parser = ConfigParser()
        Parser.read(nomefile)
        Conf_Log = Parser["Settings"]["Show_Logs"]
        if Conf_Log == "True":
            file_Log = "Logs/" + folder + "/Session_" + username + ".log"
            logging.basicConfig(filename=file_Log, filemode="w",
                                format="%(asctime)s %(message)s")
            Logger = logging.getLogger()
            Logger.setLevel(logging.DEBUG)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  "LOGS ENABLED..FILE SAVED ON: {}".format(file_Log))
        else:
            print(Font.Color.BLUE + "\n[I]" +
                  Font.Color.WHITE + "LOGS DISABLED")
