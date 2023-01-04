# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import logging
import os
from configparser import ConfigParser
from Core.Support import Font
from Core.Support import Language

filename = Language.Translation.Get_Language()
filename


class Log:

    @staticmethod
    def Checker(username, folder):
        nomefile = "Configuration/Configuration.ini"
        Parser = ConfigParser()
        Parser.read(nomefile)
        Conf_Log = Parser["Settings"]["Show_Logs"]
        if Conf_Log == "True":
            file_Log = "Logs/{}/Session_{}.log".format(folder, username)
            try:
                if (os.name != "nt"):
                    logging.basicConfig(filename=file_Log, filemode="w",
                                        format="%(asctime)s %(message)s", force=True)
                else:
                    logging.basicConfig(filename=file_Log, filemode="w",
                                        format="%(asctime)s %(message)s")
                Logger = logging.getLogger()
                Logger.setLevel(logging.DEBUG)
                print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Logs", "Enabled", "None").format(file_Log))
            finally:
                logging.shutdown()
        else:
            print(Font.Color.BLUE + "\n[I]" +
                  Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Logs", "Disabled", "None"))
