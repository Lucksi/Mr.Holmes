# AUTHOR: Lucksi
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

import os
Windows = "nt"


class Color:
    
    if os == Windows:
        YELLOW = "Color 6"
        RED = "Color 4"
        GREEN = "Color 2"
        BLUE = "Color 1"
        WHITE = "Color F"
    
    else:
        YELLOW2 = "\033[33m"
        YELLOW = "\033[0;93m"
        RED = "\033[31m"
        GREEN = "\033[32m"
        BLUE = "\033[94m"
        WHITE = "\033[97m"
        BANNER = "\033[41m"
        RESET = "\033[0m"
