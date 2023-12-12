#!/bin/bash
# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

BLUE=$(tput setaf 6)
GREEN=$(tput setaf 2)
WHITE=$(tput setaf 15)
LIGHTGREEN=$(tput setaf 10)

function banner {
	clear
	reader=$(<"Banners/Banner3.txt")
	echo "${GREEN}$reader"
}

function Packet_Installer {
	proot -0 pkg install git -y &> /dev/null | printf "${WHITE}\nINSTALLING GIT\n"
	proot -0 pkg install python3 -y &> /dev/null | printf "${WHITE}\nINSTALLING PYTHON3\n"
    proot -0 pkg install python3-pip -y &> /dev/null | printf "${WHITE}\nINSTALLING PIP"
	proot -0 pkg install whois -y &> /dev/null | printf "${WHITE}\n\nINSTALLING WHOIS"
    proot -0 pkg install tracepath -y &> /dev/null | printf "${WHITE}\n\nINSTALLING TRACEROUTE"
    proot -0 pkg install php -y &> /dev/null | printf "${WHITE}\n\nINSTALLING PHP"
	proot -0 pip3 install -r requirements.txt &> /dev/null | printf "${BLUE}\n\nINSTALLING-PYTHON-REQUIREMENTS..."
	printf "${GREEN}\n\n[+]${WHITE}REQUIREMENTS INSTALLED SUCCESFULLY${GREEN}[+]"
}

function Options {
	printf "${BLUE}\n\n[?]${WHITE}WOULD YOU LIKE TO ENABLE EMAIL-OPTION(1)YES(2)NO\n\n"
	read -p"$GREEN[#MR.HOLMES#]$WHITE-->" Opt
	while [ "$Opt" = "" ];
		do
        printf "${BLUE}\n\n[?]${WHITE}WOULD YOU LIKE TO ENABLE EMAIL-OPTION(1)YES(2)(NO)\n\n"
		read -p"$GREEN[#MR.HOLMES#]$WHITE-->" Opt
	done
	if [ $Opt == 1 ];
		then
		status="Enabled"
		printf "${WHITE}\n\nINSERT YOUR RECIPIENT EMAIL\n\n"
		read -p"$GREEN[#MR.HOLMES#]$WHITE-->" recipient
		while [ "$recipient" = "" ];
			do
			printf "${WHITE}\nINSERT YOUR RECIPIENT EMAIL\n\n"
			read -p"$GREEN[#MR.HOLMES#]$WHITE-->" recipient
		done
		printf "${WHITE}\nINSERT YOUR EMAIL PASSWORD\n\n"
		read -sp"$GREEN[#MR.HOLMES#]$WHITE-->" password
		while [ "$password" = "" ];
			do
			printf "${WHITE}\nINSERT YOUR EMAIL PASSWORD\n\n"
			read -sp"$GREEN[#MR.HOLMES#]$WHITE-->" password
		done
		printf "${WHITE}\n\nINSERT YOUR DESTINATION EMAIL\n\n"
		read -p"$GREEN[#MR.HOLMES#]$WHITE-->" destination
		while [ "$destination" = "" ];
			do
			printf "${WHITE}\nINSERT YOUR DESTINATION EMAIL\n\n"
			read -p"$GREEN[#MR.HOLMES#]$WHITE-->" destination
		done
		printf "${WHITE}\nINSERT YOUR SMTP SERVER EX smtp.test.com\n\n"
		read -p"$GREEN[#MR.HOLMES#]$WHITE-->" server
		while [ "$server" = "" ];
			do
			printf "${WHITE}\nINSERT YOUR SMTP SERVER EX smtp.test.com\n\n"
			read -p"$GREEN[#MR.HOLMES#]$WHITE-->" server
		done
		printf "${WHITE}\nINSERT YOUR SMTP SERVER PORT EX 768\n\n"
		read -p"$GREEN[#MR.HOLMES#]$WHITE-->" port
		while [ "$port" = "" ];
			do
			printf "${WHITE}\nINSERT YOUR SMTP SERVER PORT \n\n"
			read -p"$GREEN[#MR.HOLMES#]$WHITE-->" port
		done
	elif [ $Opt == 2 ];
		then
		printf "${GREEN}\n[+]${WHITE}SKIPPING..."
		status="Disabled"
		recipient="None"
		password="None"
		destination="None"
		server="None"
		port="None"
	else
		Options
	fi
	printf "\n"
	printf "${WHITE}\nINSERT YOUR UPDATE-PASSWORD\n\n"
	read -sp"$GREEN[#MR.HOLMES#]$WHITE-->" up_pass
	while [ "$up_pass" = "" ];
		do
        printf "${WHITE}\nINSERT YOUR UPDATE-PASSWORD \n\n"
        read -sp"$GREEN[#MR.HOLMES#]$WHITE-->" up_pass
	done
	printf "${WHITE}\n\nINSERT YOUR WHO-IS-XMLAPI-KEY(LEAVE EMPTY IF YOU HAVENT ONE)\n\n"
	read -p"$GREEN[#MR.HOLMES#]$WHITE-->" key
	if [ "$key" == "" ];
		then
		key="None"
	fi
	printf "${WHITE}\n\nINSERT YOUR PROXY_LIST FULL-PATH(LEAVE EMPTY IF YOU WANT THE DEFAULT LIST)\n\n"
	read -p"$GREEN[#MR.HOLMES#]$WHITE-->" proxies
	if [ "$proxies" == "" ];
		then
		proxies="Proxies/Proxy_list.txt"
	fi
	printf "${WHITE}\n\nINSERT YOUR USERAGENT_LIST FULL-PATH(LEAVE EMPTY IF YOU WANT THE DEFAULT LIST)\n\n"
	read -p"$GREEN[#MR.HOLMES#]$WHITE-->" useragent
	if [ "$useragent" == "" ];
		then
		useragent="Useragents/Useragent.txt"
	fi
	printf "${WHITE}\n\nWOULD YOU LIKE TO SAVE YOUR LOG SESSIONS(1)YES(2)NO\n\n"
	read -p"$GREEN[#MR.HOLMES#]$WHITE-->" Logs
	if [ $Logs == 2 ];
		then
		Logs="False"
	elif [ $Logs == 1 ];
		then
		Logs="True"
	fi
	printf "${WHITE}\nSELECT YOUR CLI-DEFAULT LANGUAGE\n(1)ENGLISH\n(2)ITALIANO\n(3)FRANÇAIS\n\n"
	read -p"$GREEN[#MR.HOLMES#]$WHITE-->" Language
	while [ "$Language" == "" ];
		do
		printf "${WHITE}\nSELECT YOUR GUI-DEFAULT LANGUAGE\n(1)ENGLISH\n(2)ITALIANO\n(3)FRANÇAIS\n\n"
		read -p"$GREEN[#MR.HOLMES#]$WHITE-->" Language
	done
	if [ $Language == 1 ];
		then
		Lang="English"
		mode="ENGLISH"

	elif [ $Language == 2 ];
		then
		Lang="Italian"
		mode="ITALIANO" 

	elif [ $Language == 3 ];
		then
		Lang="French"
		mode="FRANÇAIS"
	fi
	printf "\n${WHITE}CLI-LANGUAGE:${GREEN}$mode\n"
	printf "${WHITE}\nSELECT YOUR DATE-FORMAT\n(1)EUROPE(DD/MM/YYYY)\n(2)AMERICA'USA'(MM/DD/YYYY)\n(3)ASIA(YYYY/MM/DD)\n\n"
	read -p"$GREEN[#MR.HOLMES#]$WHITE-->" DateFormat
	while [ "$DateFormat" == "" ];
		do
		printf "${WHITE}\nSELECT YOUR DATE-FORMAT\n(1)EUROPE(DD/MM/YYYY)\n(2)AMERICA'USA'(MM/DD/YYYY)\n(3)ASIA(YYYY/MM/DD)\n\n"
		read -p"$GREEN[#MR.HOLMES#]$WHITE-->" DateFormat
	done
	if [ $DateFormat == 1 ];
		then
		Date="eu"
		mode="EUROPE(EU)"

	elif [ $DateFormat == 2 ];
		then
		Date="us"
		mode="AMERICA(US)" 

	elif [ $DateFormat == 3 ];
		then
		Date="as"
		mode="ASIA(AS)"
	fi
	printf "\n${WHITE}DATE-FORMAT:${GREEN}$mode\n"
	printf "${BLUE}\nCREATING CONFIGURATION FILE"
	cd Configuration
	echo ";THIS FILE HAS BEEN GENERATE BY MR.HOLMES INSTALLER">Configuration.ini
	echo ";CHANGE THESE VALUE IF YOU WANT TO UPDATE YOUR SETTINGS FROM HERE">>Configuration.ini
	echo ";BUT DO NOT CHANGE THE PARAMETERS NAME">>Configuration.ini
	echo "">>Configuration.ini
	echo "[Smtp]">>Configuration.ini
	echo "status = $status">>Configuration.ini
	echo "email = $recipient">>Configuration.ini
	echo "password = $password">>Configuration.ini
	echo "destination = $destination">>Configuration.ini
	echo "server= $server">>Configuration.ini
	echo "port= $port">>Configuration.ini
	echo "">>Configuration.ini
	echo "[Settings]">>Configuration.ini
	echo "password = $up_pass">>Configuration.ini
	echo "api_key = $key">>Configuration.ini 
	echo "proxy_list" = $proxies>>Configuration.ini
	echo "useragent_list" = $useragent>>Configuration.ini
	echo "show_logs = $Logs">>Configuration.ini
	echo "language"= "$Lang">>Configuration.ini
	echo "date_format"= "$Date">>Configuration.ini
	rm UNTILED.txt &> /dev/null
}

function AutoInstaller {
	printf "${GREEN}\n[+]${WHITE}AUTO-INSTALLER MODE...\n"
	Packet_Installer
	sleep 5
	echo ";THIS FILE HAS BEEN GENERATE BY MR.HOLMES INSTALLER">Configuration/Configuration.ini
	echo ";CHANGE THESE VALUE IF YOU WANT TO UPDATE YOUR SETTINGS FROM HERE">>Configuration/Configuration.ini
	echo ";BUT DO NOT CHANGE THE PARAMETERS NAME">>Configuration/Configuration.ini
	echo "">>Configuration/Configuration.ini
	echo "[Smtp]">>Configuration/Configuration.ini
	echo "status" = "Disabled">>Configuration/Configuration.ini
	echo "email = None">>Configuration/Configuration.ini
	echo "password = None">>Configuration/Configuration.ini
	echo "destination = None">>Configuration/Configuration.ini
	echo "server= None">>Configuration/Configuration.ini
	echo "port= None">>Configuration/Configuration.ini
	echo "">>Configuration/Configuration.ini
	echo "[Settings]">>Configuration/Configuration.ini
	echo "password = Holmes">>Configuration/Configuration.ini
	echo "api_key = None">>Configuration/Configuration.ini
	echo "proxy_list" = "Proxies/Proxy_list.txt">>Configuration/Configuration.ini
	echo "useragent_list" = "Useragents/Useragent.txt">>Configuration/Configuration.ini
	echo "show_logs = False">>Configuration/Configuration.ini
	echo "database"= "False">>Configuration/Configuration.ini
	echo "language"= "english">>Configuration/Configuration.ini
	echo "date_format"= "eu">>Configuration/Configuration.ini
	rm Configuration/UNTILED.txt &> /dev/null
	printf "\n\n${WHITE}EMAIL-SERVER:${GREEN}DISABLED\n"
	printf "\n${WHITE}SHOW-LOGS:${GREEN}FALSE\n"
	printf "\n${WHITE}UPDATE-PASSWORD:${GREEN}Holmes\n"
	printf "\n${WHITE}API-KEY:${GREEN}None\n"
	printf "\n${WHITE}PROXIES:${GREEN}DEFAULT\n"
	printf "\n${WHITE}USERAGENTS:${GREEN}DEFAULT\n"
	printf "\n${WHITE}CLI-LANGUAGE:${GREEN}ENGLISH\n"
	printf "\n${WHITE}DATA-FORMAT:${GREEN}EUROPE(EU)"
}


function installer {
	printf "${BLUE}\n\nWELCOME TO THE INSTALLATION MANAGER WOULD YOU LIKE TO BEGIN(1)YES(2)NO\n\n"
	read -p "$GREEN[#MR.HOLMES#]$WHITE-->" confvar
	if [ $confvar == 1 ];
		then 
		printf "${BLUE}\nWOULD YOU LIKE TO SET(1)MANUAL-INSTALLATION(2)AUTO-INSTALLATION\n\n"
		read -p "$GREEN[#MR.HOLMES#]$WHITE-->" selected
		while [ "$selected" == "" ];
			do
			printf "${BLUE}\n\nWOULD YOU LIKE TO SET(1)MANUAL-INSTALLATION(2)AUTO-INSTALLATION\n\n"
			read -p "$GREEN[#MR.HOLMES#]$WHITE-->" selected
		done
		if [ $selected == 1 ];
			then 
			Packet_Installer
			Mail_Options
			Options
			cd ../
			
		elif [ $selected == 2 ];
			then
		    AutoInstaller
		fi
		cd Core
		printf "${WHITE}\n\nGIVING PERMISSION TO LUNCH FOR CORE FILES"
		sudo chmod +x update.sh
		cd ../
		cd Launchers
		sudo chmod +x Launcher.sh
		cd ../
		cd ../
		echo "path = `pwd`">>Mr.Holmes/Configuration/Configuration.ini
		sleep 2
		printf "\n\nSETTING CLI INTERFACE..."
		echo "Mobile">Mr.Holmes/Display/Display.txt
		sleep 2
		printf "${GREEN}\n\n[+]${WHITE}PROGRAM INSTALLED CORRECTLY${GREEN}[+]"
		printf "${LIGHTGREEN}\n\nTHANK YOU FOR HAVE INSTALLED Mr.Holmes\n\n"
		exit 0
	fi
	printf "\n${BLUE}INSTALLATION INTERRUPTED EXIT...\n\n"
    	exit 1
}
banner
installer
