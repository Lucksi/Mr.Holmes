#!/usr/bin/env python3
# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# License: GNU General Public License v3.0

import os
import sys

from Core.Support import Menu
from Core.Support import Font
from Core.Support import Language


# Load language configuration safely
try:
    filename = Language.Translation.Get_Language()
except Exception as e:
    print("Language configuration error:", e)
    sys.exit(1)


class Main:

    @staticmethod
    def Controll_Display():
        interface_file = "Display/Display.txt"

        # check if file exists
        if not os.path.isfile(interface_file):
            print(
                Font.Color.RED + "[!]" +
                Font.Color.WHITE +
                Language.Translation.Translate_Language(
                    filename, "Default", "NoDisplay", "None"
                ).format(interface_file)
            )
            sys.exit(1)

        # read file
        with open(interface_file, "r") as d:
            conf = d.read().strip()

        # validate mode
        if conf not in ["Desktop", "Mobile"]:
            print(
                Font.Color.RED + "[!]" +
                Font.Color.WHITE +
                Language.Translation.Translate_Language(
                    filename, "Default", "DisplayError", "None"
                )
            )
            sys.exit(1)

        return conf

    @staticmethod
    def Menu(mode):
        Menu.Main.main(mode)


if __name__ == "__main__":

    mode = Main.Controll_Display()

    try:
        Main.Menu(mode)

    except KeyboardInterrupt:
        print(
            Font.Color.RED + "\n\n[!]" +
            Font.Color.WHITE +
            Language.Translation.Translate_Language(
                filename, "Default", "KeyC", "None"
            )
        )
        sys.exit(0)

    except ModuleNotFoundError as error:
        print(
            Font.Color.RED + "\n\n[!]" +
            Font.Color.WHITE +
            Language.Translation.Translate_Language(
                filename, "Default", "Internal", "None"
            ).format(str(error))
        )
        sys.exit(1)

    except Exception as error:
        print(Font.Color.RED + "\nUnexpected error:", error)
        sys.exit(1)
