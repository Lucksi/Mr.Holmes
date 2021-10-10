import os

Windows = "nt"

class Screen:
    
    def Clear():
        os.system("cls" if os.name == "nt" else "clear")