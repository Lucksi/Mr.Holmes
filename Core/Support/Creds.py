# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from Core.Support import Font
from email.mime.multipart import MIMEMultipart
from configparser import ConfigParser
import smtplib

class Sender:
    @staticmethod
    def mail(report,username):
        mail = int(input(
            Font.Color.BLUE + "\n[?]" + Font.Color.WHITE + "WOULD YOU LIKE TO RECIEVE A DATA-MAIL?(1)YES(2)NO" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if mail == 1:
            print(
                Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SENDING EMAIL PLEASE WAIT...")
            nomefile = "Configuration/Configuration.ini"
            Parser = ConfigParser()
            Parser.read(nomefile)            
            email = Parser["Smtp"]["Email"]
            password = Parser["Smtp"]["Password"]
            destination = Parser["Smtp"]["Destination"]
            host = Parser["Smtp"]["Server"]
            host2 = (str(host))
            port = Parser["Smtp"]["Port"]
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
            file.add_header("Content-Disposition", "attachment;filename=" + filename)
            message.attach(file)
            try:
                server = smtplib.SMTP(host2, port2)
                server.ehlo()
                server.starttls()
                server.login(email, password)
                text = message.as_string()
                server.sendmail(email, destination, text)
                inp = input(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE + "EMAIL SENT PRESS ENTER TO CONTINUE...")
                server.close()
            except smtplib.SMTPException:
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "OPS LOOKS LIKE THE EMAIL HAS NOT BE SENT")
                inp = input("\nPRESS ENTER TO CONTINUE")
        elif mail == 2:
            inp = input("\nPRESS ENTER TO CONTINUE")