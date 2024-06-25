# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import json
import urllib
import MrHolmes as holmes
from Core.Support import Font
from Core.Support import Creds
from Core.Support import FileTransfer
from Core.Support import Clear
from Core.Support import Dorks
from Core.Support.Mail import Mail_Validator as mail
from Core.Support.Mail import Lookup
from Core.Support import ApiCheck as Api
from Core.Support import Banner_Selector as banner
from Core.Support import Language
from Core.Support import DateFormat
from Core.Support import Notification
from Core.Support import Encoding
from time import sleep
from datetime import datetime

filename = Language.Translation.Get_Language()
filename


class Mail_search:

    @staticmethod
    def Banner(Mode):
        Clear.Screen.Clear()
        Folder = "Banners/E-Mail"
        banner.Random.Get_Banner(Folder, Mode)

    @staticmethod
    def Google_dork(username):
        report = "GUI/Reports/E-Mail/Dorks/{}_dorks.txt".format(username)
        nomefile = "Site_lists/E-Mail/Google_dorks.txt"
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                filename, "Dorks", "Remove", "None").format(username))
        else:
            pass
        Type = "GOOGLE"
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def Yandex_dork(username):
        report = "GUI/Reports/E-Mail/Dorks/{}_dorks.txt".format(username)
        nomefile = "Site_lists/E-Mail/Yandex_dorks.txt"
        Type = "YANDEX"
        Dorks.Search.dork(username, report, nomefile, Type)

    @staticmethod
    def Lookup(username, report):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Website", "Default", "Whois").format(username))
        sleep(2)
        Key = Api.Check.WhoIs()
        Key
        RecList = []
        if Key == "None":
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + "API-KEY NOT FOUND")
        else:
            try:
                print(Font.Color.GREEN + "[+]" +
                      Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Website", "Parameters", "KeyFound"))
                Key2 = str(Key)
                source = "https://emailverification.whoisxmlapi.com/api/v3?apiKey={}&emailAddress={}".format(
                    Key2, username)
                access = urllib.request.urlopen(source)
                reader = access.read()
                final = json.loads(reader)
                name = final["username"]
                domain = final["domain"]
                completemail = final["emailAddress"]
                dns = final["dnsCheck"]
                freeDomain = final["freeCheck"]
                Temporary = final["disposableCheck"]
                if("smtpCheck" in final):
                    smtp = final["smtpCheck"]
                    SmtpOk = True
                else:
                    SmtpOk = False
                if("catchAllCheck" in final):
                    CatchAll = final["catchAllCheck"]
                    CatchOk = True
                else:
                    CatchOk = False
                if("mxRecords" in final):
                    Records = final["mxRecords"]
                    i = 0
                    for record in Records:
                        RecList.append(record)
                        i = i+1
                    RecordOk = True
                else:
                    RecordOk = False
                print(Font.Color.GREEN +
                      "\n[+]" + Font.Color.WHITE + "INFORMATIONS FOUND:")
                sleep(3)
                print(Font.Color.YELLOW + "[v]" +
                      Font.Color.WHITE + "NAME: " + name)
                print(Font.Color.YELLOW + "[v]" +
                      Font.Color.WHITE + "DOMAIN: " + domain)
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "EMAIL: " + completemail)
                if SmtpOk:
                    print(Font.Color.YELLOW + "[v]" +
                        Font.Color.WHITE + "SMTP: " + smtp)
                print(Font.Color.YELLOW + "[v]" +
                      Font.Color.WHITE + "DNS: " + dns)
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "FREE-DOMAIN: " + freeDomain)
                print(Font.Color.YELLOW +
                      "[v]" + Font.Color.WHITE + "TEMPORARY: " + Temporary)
                if CatchOk:
                    print(Font.Color.YELLOW +
                        "[v]" + Font.Color.WHITE + "CATCH-ALL: " + CatchAll)
                if RecordOk:
                    print(Font.Color.GREEN +
                        "\n[+]" + Font.Color.WHITE + "FOUND MX-RECORDS(DNS):")
                    i = 1
                    for record in RecList:
                        print(
                            Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "RECORD N {}: ".format(i) + record)
                        i = i+1
                sleep(2)
                f = open(report, "a")
                f.write("\n\nEMAIL DATA:" + "\r\n")
                f.write("NAME: " + name + "\r\n")
                f.write("DOMAIN: " + domain + "\r\n")
                f.write("EMAIL: " + completemail + "\r\n")
                f.write("SMTP: " + smtp + "\r\n")
                f.write("FREE-DOMAIN: " + freeDomain + "\r\n")
                f.write("TEMPORARY: " + Temporary + "\r\n")
                f.write("CATCH-ALL: " + CatchAll + "\r\n")
                f.write("\n\nFOUND MX-RECORDS(DNS)" + "\r\n")
                i = 1
                for record in RecList:
                    f.write("RECORD N {}: ".format(i) + record + "\r\n")
                    i = i+1
            except Exception as e:
                pass

    @staticmethod
    def searcher(username, report, Mode):
        #nomefile = "Temp/E-Mail/Code.txt"
        #if os.path.isfile(nomefile):
            list_file = "Site_lists/E-Mail/Lists.json"
            reader = open(list_file,)
            data = json.loads(reader.read())
            for sites in data:
                for data1 in sites:
                    name = sites[data1]["name"]
                    url = sites[data1]["url"].replace("{}", username)
                    print(
                        Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Email", "Link", "None").format(name))
                    sleep(2)
                    print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + url)
                    f = open(report, "a")
                    f.write("\nGENERATING {} LINK".format(name))
                    f.write("\n{}".format(url))
                f.close()
            f.close()
            #os.remove(nomefile)
        #else:
        #    holmes.Main.Menu(Mode)

    @staticmethod
    def Search(username, Mode):
        Mail_search.Banner(Mode)
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "INFO:" + "[{}]".format(Font.Color.GREEN + Language.Translation.Translate_Language(filename,"Email","Explanation","None") + Font.Color.WHITE) )
        now = datetime.now()
        dataformat = DateFormat.Get.Format()
        dt_string = now.strftime(dataformat)
        Date = "Date: " + str(dt_string)
        folder = "GUI/Reports/E-Mail/" + username
        report = "GUI/Reports/E-Mail/{}/{}.txt".format(username,username)
        report2 = "GUI/Reports/E-Mail/{}/{}.mh".format(username,username)
        if os.path.isfile(report):
            os.remove(report)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        elif os.path.isfile(report2):
            os.remove(report2)
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Default", "Delete", "None").format(username))
        else:
            os.mkdir(folder)
        f = open(report, "w")
        f.write("SCANNING EXECUTED ON:\n" + Date + "\n")
        f.close()
        isvalid = mail.Validator.Mail(username, report)
        if isvalid:
            Mail_search.Lookup(username, report)
            lookup = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO CHECK IF THIS EMAIL IS USED ON SOME SOCIAL MEDIA?(1)YES(2)NO\n\n" + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if lookup == 1:
                Lookup.List.Main(report,username)
            Mail_search.searcher(username, report, Mode)
            choice = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Dorks", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                Mail_search.Google_dork(username)
                Mail_search.Yandex_dork(username)
            else:
                pass
            print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
                os.getcwd() + "/" + report)
            f = open(report, "a")
            f.write(Language.Translation.Translate_Language(
                filename, "Report", "Default", "By"))
            f.close()
            print(Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Default", "Report", "None") +
                report)
            Notification.Notifier.Start(Mode)
            Creds.Sender.mail(report, username)
            choice = int(input(
                Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Transfer", "Question", "None") + Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            if choice == 1:
                FileTransfer.Transfer.File(report, username, ".txt")
            Encoding.Encoder.Encode(report)
            inp = input(Language.Translation.Translate_Language(
                filename, "Default", "Continue", "None"))
