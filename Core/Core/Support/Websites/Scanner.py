# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import socket
from Core.Support import Font
from Core.Support import Language
from time import sleep

filename = Language.Translation.Get_Language()
filename

class Port:

    @staticmethod
    def Get_Port(Server, report, port, Open_Ports):
        print(Font.Color.GREEN +
              "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Check", "None").format(port))
        host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host.settimeout(2)
        Result = host.connect_ex((Server, port))
        if Result == 0:
            print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Ports", "Port", "None").format(port) + Font.Color.GREEN + Language.Translation.Translate_Language(filename, "Ports", "Open", "None"))
            Open_Ports.append(port)
            f = open(report, "a")
            f.write("Port: {}\n".format(port))
            f.close()
        else:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE +
                  Language.Translation.Translate_Language(filename, "Ports", "Port", "None").format(port) + Font.Color.RED + Language.Translation.Translate_Language(filename, "Ports", "Closed", "None"))
        host.close()

    @staticmethod
    def Scan(username, report):
        Open_Ports = []
        Server = socket.gethostbyname(username)
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Ports", "Host", "None").format(username))
        print(Font.Color.GREEN +
              "[+]" + Font.Color.WHITE + "{} IP: {}".format(username, Server))
        nPorts = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Text", "None") +
                     Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if nPorts == 1:
            Min = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Pstart", "None") +
                            Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            while Min == "":
                Min = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Pstart", "None") +
                                Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            Max2 = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Pfinish", "None") +
                             Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            while Max2 == "":
                Max2 = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Pfinish", "None") +
                                 Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            Max = Max2 + 1
            Def = True
        elif nPorts == 2:
            Min = 1
            Max = 1024
            Def = True
        elif nPorts == 3:
            Ports_List = []
            amount = 0
            Def = False
            i = 0
            amount = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Amounts", "None") +
                               Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            while amount == "":
                amount = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Amounts", "None") +
                                   Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            for i in range(amount):
                port = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Number", "None") +
                                 Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while port == "":
                    port = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Number", "None") +
                                     Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                Ports_List.append(port)
        elif nPorts == 4:
            inp = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
            #holmes.Main.Menu(Mode)
        if nPorts != 4:
            try:
                if Def:
                    for port in range(Min, Max):
                        Port.Get_Port(Server, report, port, Open_Ports)
                else:
                    for port in Ports_List:
                        Port.Get_Port(Server, report, port, Open_Ports)
            except Exception as e:
                print(Font.Color.RED +
                    "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Error", "None"))
            if len(Open_Ports):
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                    Language.Translation.Translate_Language(filename, "Ports", "OpenPorts", "None").format(username))
                sleep(4)
                for ports in Open_Ports:
                    print(Font.Color.YELLOW +
                        "[v]" + Font.Color.WHITE + "PORT: {}".format(ports))
            
            else:
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                    Language.Translation.Translate_Language(filename, "Ports", "NoPorts", "None").format(username))