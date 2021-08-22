import os
import MrHolmes as Holmes
from Core.Support import Font
from time import sleep

class Controller:
    
    @staticmethod
    def Gui():
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "ACTIVATING DATABASE...")
        os.system("sudo php -S 127.0.0.1:200 -t GUI >/dev/null 2>&1 &")
        sleep(3)
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "DATABASE STARTED ON http://127.0.0.1:200")
        inp = input("\nPRESS ENTER TO STOP ")
        os.system ("killall  php > /dev/null 2>&1")
        print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "STOPPING DATABASE...")
        sleep(3)
        Holmes.Main()