from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from Core.Support import Font
from email.mime.multipart import MIMEMultipart
import smtplib

class Sender:
    @staticmethod
    def mail(report,username):
        mail = int(input(
            Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO RECIEVE A DATA-MAIL?(1)YES(2)NO" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if mail == 1:
            print(
                Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SENDING EMAIL PLEASE WAIT" + Font.Color.GREEN + "[+]")
            f = open("Configuration/Recipient.txt", "r")
            dent = f.read()
            f.close()
            f = open("Configuration/Password.txt", "r")
            dent2 = f.read()
            f.close()
            f = open("Configuration/Destination.txt", "r")
            dent3 = f.read()
            f.close()
            f = open("Configuration/Server.txt", "r")
            dent4 = f.read().replace('\n', '')
            f.close()
            f = open("Configuration/Port.txt", "r")
            dent5 = f.read().replace('\n', '')
            f.close()
            email = dent
            password = dent2
            destination = dent3
            host = dent4
            host2 = (str(host))
            port = dent5
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
            server = smtplib.SMTP(host2, port2)
            server.ehlo()
            server.starttls()
            server.login(email, password)
            text = message.as_string()
            server.sendmail(email, destination, text)
            inp = input(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "EMAIL SENT PRESS ENTER TO CONTINUE...")
            server.close()