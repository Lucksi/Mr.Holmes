#!/bin/bash
. /etc/os-release
DIST="$ID"
BLUE=$(tput setaf 6)
GREEN=$(tput setaf 2)
WHITE=$(tput setaf 15)
LIGHTGREEN=$(tput setaf 10)

function banner {
	clear
	reader=$(<"Banners/Banner6.txt")
	echo "${GREEN}$reader"
}


function installer {
	printf "${BLUE}\n\nCHECKING LINUX DISTRIBUTION..."
	sleep 2
	printf "${GREEN}\n\n[+]${WHITE}LINUX DISTRIBITIUN FOUND:$DIST${GREEN}[+]"
	printf "${BLUE}\n\nWELCOME TO THE INSTALLATION MANAGER WOULD YOU LIKE TO BEGIN(1)YES(2)NO\n\n"
	read -p "$GREEN[#MR.HOLMES#]$WHITE-->" confvar
	if [ $confvar == 1 ]; 
		then
            proot -0 pkg install python3 &> /dev/null | printf "${WHITE2}\nINSTALLING PYTHON3\n"
            proot -0 pkg install python3-pip &> /dev/null | printf "${WHITE2}\nINSTALLING PIP"
            proot -0 pkg install zenity &> /dev/null | printf "${WHITE2}\n\nINSTALLING ZENITY"
			proot -0 pkg install whois &> /dev/null | printf "${WHITE2}\n\nINSTALLING WHOIS"
            proot -0 pkg install tracepath &> /dev/null | printf "${WHITE2}\n\nINSTALLING TRACEROUTE"
			proot -0 pip3 install -r requirements.txt &> /dev/null | printf "${BLUE}\n\nINSTALLING-PYTHON-REQUIREMENTS..."
			printf "${GREEN}\n\n[+]${WHITE}REQUIREMENTS INSTALLED SUCCESFULLY${GREEN}[+]"
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
				printf "${WHITE}\nINSERT YOUR UPDATE-PASSWORD\n\n"
				read -sp"$GREEN[#MR.HOLMES#]$WHITE-->" up_pass
				while [ "$up_pass" = "" ];
				do
                  printf "${WHITE}\nINSERT YOUR UPDATE-PASSWORD \n\n"
                  read -sp"$GREEN[#MR.HOLMES#]$WHITE-->" up_pass
				done
				printf "${WHITE}\n\nINSERT YOUR WHO-IS-XMLAPI-KEY(LEAVE EMPTY IF YOU HAVENT ONE)\n\n"
				read -p"$GREEN[#MR.HOLMES#]$WHITE-->" key
				if [ "$key" = "" ];
				then
					key="None"
				fi
				printf "${BLUE}\nCREATING CONFIGURATION FILE"
				cd Configuration
				echo "[Smtp]">Configuration.ini
				echo "Email = $recipient">>Configuration.ini
				echo "Password = $password">>Configuration.ini
				echo "Pestination = $destination">>Configuration.ini
				echo "Server= $server">>Configuration.ini
				echo "Port= $port">>Configuration.ini
				echo "">>Configuration.ini
				echo "[Settings]">>Configuration.ini
				echo "Password = $up_pass">>Configuration.ini
				echo "Api_Key = $key">>Configuration.ini 
				rm UNTILED.txt &> /dev/null
				cd ../
				cd Core
				printf "\n\nGIVING PERMISSION TO LUNCH FOR CORE FILES"
				proot -0 chmod +x update.sh
				cd Support
				proot -0 chmod +x Notification.sh
				cd ../
				cd ../
				cd ../
				echo "Path = `pwd`">>Mr.Holmes/Configuration/Configuration.ini
				sleep 2
				printf "${GREEN}\n\n[+]${WHITE}PROGRAM INSTALLED CORRECTLY${GREEN}[+]"
				printf "${LIGHTGREEN}\n\nTHANK YOU FOR HAVE INSTALLED Mr.Holmes\n\n"
				exit 1
    fi
	  printf "\n${BLUE}INSTALLATION INTERRUPTED EXIT...\n\n"
      exit 1
}
banner
installer
