#!/bin/bash
# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2022-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0s

GREEN=$(tput setaf 2)
WHITE=$(tput setaf 15)
BLUE=$(tput setaf 6)

function Banner {
    clear
	reader=$(<"../Banners/Launcher.txt")
	echo "${GREEN}$reader"
}

function Core {
    printf "${GREEN}\n\n[+]${WHITE}WOULD YOU LIKE TO EXECUTE MR.HOLMES IN:\n(1)NO-ROOT(DATABASE NOT AVAIABLE)\n(2)ROOT(ALL FUNCTIONALITES AVAIABLE)\n(3)EXIT\n\n"
    read -p"$GREEN[#MR.HOLMES#]$WHITE-->" Choice
    while [ $Choice != 3 ];
        do
        if [ $Choice == 1 ];
            then
            printf "${GREEN}\n[+]${WHITE}EXECUTING AS NO-ROOT.."
            sleep 2
            cd ../
            python3 MrHolmes.py
            cd Launchers
        elif [ $Choice == 2 ];
            then
            printf "${GREEN}\n[+]${WHITE}EXECUTING AS ROOT..\n\n"
            sleep 2
            cd ../
            sudo python3 MrHolmes.py
            cd Launchers
        fi
        Main
    done
    printf "${WHITE}\nCLOSE THIS WINDOW FOR EXIT"
    exit 0
}

function Main {
    Banner
    Core
}
Main
