# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import os
from Core.Support import Font
from Core.Support import Clear
from Core.Support.Websites import Scanner
from Core.Support import Creds
from Core.Support import Banner_Selector as banner
from Core.Support import Language
from Core.Support import Notification
from datetime import datetime

filename = Language.Translation.Get_Language()
filename


class Ports:

    @staticmethod
    def Banner(Mode):
        Clear.Screen.Clear()
        Folder = "Banners/Ports"
        banner.Random.Get_Banner(Folder, Mode)

    @staticmethod
    def Main(username, Mode):
        Ports.Banner(Mode)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        Date = "Date: " + str(dt_string)
        report = "GUI/Reports/Ports/{}.txt".format(username)
        if os.path.exists(report):
            print(Font.Color.BLUE + "[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
            os.remove(report)
        f = open(report, "a")
        f.write("SCANNING EXECUTED ON:\n" + Date + "\r\n")
        f.write("OPEN PORTS:\r\n")
        f.close()
        Scanner.Port.Scan(username, report)
        f = open(report, "a")
        f.write(Language.Translation.Translate_Language(
            filename, "Report", "Default", "By"))
        f.close()
        print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
              os.getcwd() + "/" + report)
        Notification.Notifier.Start(Mode)
        Creds.Sender.mail(report, username)
