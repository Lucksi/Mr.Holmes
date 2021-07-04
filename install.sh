#!/bin/bash
. /etc/os-release
DIST="$ID"

function installer {
	clear
	printf "$(tput setaf 6)CHECKING LINUX DISTRIBUTION..."
	sleep 2
	printf "$(tput setaf 2)\n\n[+]$(tput setaf 15)LINUX DISTRIBITIUN FOUND:$DIST$(tput setaf 2)[+]"
	printf "$(tput setaf 6)\n\nWELCOME TO THE INSTALLATION MANAGER WOULD YOU LIKE TO BEGIN(1)YES(2)NO\n\n"
	read -p "$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" confvar
	if [ $confvar == 1 ]; 
		then
            sudo apt install python3 &> /dev/null | printf "$(tput setaf 15)\nINSTALLING PYTHON3\n"
            sudo apt install python3-pip &> /dev/null | printf "$(tput setaf 15)\nINSTALLING PIP"
            sudo apt install zenity &> /dev/null | printf "$(tput setaf 15)\n\nINSTALLING ZENITY"
			sudo apt install whois &> /dev/null | printf "$(tput setaf 15)\n\nINSTALLING WHOIS"
			sudo pip3 install -r requirements.txt &> /dev/null | printf "$(tput setaf 6)\n\nINSTALLING-PYTHON-REQUIREMENTS..."
			printf "$(tput setaf 2)\n\n[+]$(tput setaf 15)REQUIREMENTS INSTALLED SUCCESFULLY$(tput setaf 2)[+]"
			printf "$(tput setaf 15)\n\nINSERT YOUR RECIPIENT EMAIL\n\n"
			read -p"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" recipient
				while [ "$recipient" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR RECIPIENT EMAIL\n\n"
                  read -p"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" recipient
				done
				printf "$(tput setaf 15)\nINSERT YOUR EMAIL PASSWORD\n\n"
				read -sp"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" password
				while [ "$password" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR EMAIL PASSWORD\n\n"
                  read -sp"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" password
                		done
				printf "$(tput setaf 15)\n\nINSERT YOUR DESTINATION EMAIL\n\n"
				read -p"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" destination
				while [ "$destination" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR DESTINATION EMAIL\n\n"
                  read -p"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" destination
				done
				printf "$(tput setaf 15)\nINSERT YOUR SMTP SERVER EX smtp.test.com\n\n"
				read -p"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" server
				while [ "$server" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR SMTP SERVER EX smtp.test.com\n\n"
                  read -p"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" server
				done
				printf "$(tput setaf 15)\nINSERT YOUR SMTP SERVER PORT EX 768\n\n"
				read -p"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" port
				while [ "$port" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR SMTP SERVER PORT \n\n"
                  read -p"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" port
				done
				printf "$(tput setaf 15)\nINSERT YOUR UPDATE-PASSWORD\n\n"
				read -sp"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" up_pass
				while [ "$up_pass" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR UPDATE-PASSWORD \n\n"
                  read -sp"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" up_pass
				done
				printf "$(tput setaf 15)\n\nINSERT YOUR WHO-IS API-KEY(LEAVE EMPTY IF YOU HAVENT ONE)\n\n"
				read -p"$(tput setaf 2)[#MR.HOLMES#]$(tput setaf 15)-->" key
				printf "$(tput setaf 6)\n\nCREATING CONFIGURATION FILE"
				cd Configuration
				echo "$recipient">Recipient.txt
				echo "$password">Password.txt
				echo "$destination">Destination.txt
				echo "$server">Server.txt
				echo "$port">Port.txt
				echo "$up_pass">Pass_Update.txt
				rm UNTILED.txt &> /dev/null
				cd ../
				cd Api
				echo "$key">api_key.txt
				cd ../
				cd Core
				printf "\nGIVING PERMISSION TO LUNCH FOR CORE FILES"
				sudo chmod +x update.sh
				cd Support
				sudo chmod +x Notification.sh
				cd ../
				cd ../
				cd ../
				echo "`pwd`">Mr.Holmes/Configuration/Update.txt
				sleep 2
				printf "$(tput setaf 2)\n\n[+]$(tput setaf 15)PROGRAM INSTALLED CORRECTLY$(tput setaf 2)[+]"
				printf "$(tput setaf 10)\n\nTHANK YOU FOR HAVE INSTALLED Mr.Holmes\n\n"
    fi
      exit 1
}
installer
