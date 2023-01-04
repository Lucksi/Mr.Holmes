# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from Core.Support import Font
from email.mime.multipart import MIMEMultipart
from configparser import ConfigParser
from Core.Support import Language
import smtplib
import re as Regex

LangFile = Language.Translation.Get_Language()
LangFile


class Sender:

    @staticmethod
    def mail(report, username):
        nomefile = "Configuration/Configuration.ini"
        Parser = ConfigParser()
        Parser.read(nomefile)
        status = Parser["Smtp"]["status"]
        if status == "Enabled":
            simbols = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            email = Parser["Smtp"]["email"]
            destination = Parser["Smtp"]["destination"]
            if Regex.fullmatch(simbols, email) and Regex.fullmatch(simbols, destination):
                mail = int(input(
                    Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "RecapEmail", "Sender", "None") + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                if mail == 1:
                    print(
                        Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "RecapEmail", "InProgress", "None"))
                    email = Parser["Smtp"]["email"]
                    password = Parser["Smtp"]["password"]
                    destination = Parser["Smtp"]["destination"]
                    host = Parser["Smtp"]["server"]
                    host2 = (str(host))
                    port = Parser["Smtp"]["port"]
                    port2 = (int(port))
                    message = MIMEMultipart()
                    message['From'] = "MR.HOLMES:"
                    message["To"] = destination
                    message["Subject"] = "RESULTS FOR: " + username
                    msg = "Query results:"
                    message.attach(MIMEText(msg, "plain"))
                    filename = report
                    attachment = open(filename, "rb")
                    file = MIMEBase("application", "octet-stream")
                    file.set_payload(attachment.read())
                    encoders.encode_base64(file)
                    file.add_header("Content-Disposition",
                                    "attachment;filename=" + filename)
                    message.attach(file)
                    try:
                        server = smtplib.SMTP(host2, port2)
                        server.ehlo()
                        server.starttls()
                        server.login(email, password)
                        text = message.as_string()
                        server.sendmail(email, destination, text)
                        inp = input(
                            Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE + Language.Translation.Translate_Language(LangFile, "RecapEmail", "Sent", "None"))
                        server.close()
                    except smtplib.SMTPException:
                        inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                                    Language.Translation.Translate_Language(LangFile, "RecapEmail", "NotSent", "None"))
                elif mail == 2:
                    pass
                    #inp = input(Language.Translation.Translate_Language(
                    #    LangFile, "Default", "Continue", "None"))
            else:
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                    LangFile, "RecapEmail", "NotValid", "None"))
        else:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                LangFile, "RecapEmail", "Disabled", "None"))
