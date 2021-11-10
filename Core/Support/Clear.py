# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import os

Windows = "nt"

class Screen:
    
    def Clear():
        os.system("cls" if os.name == "nt" else "clear")