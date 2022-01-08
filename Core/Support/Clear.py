# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

import os

Windows = "nt"


class Screen:

    def Clear():
        os.system("cls" if os.name == Windows else "clear")
