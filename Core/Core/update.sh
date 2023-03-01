#!/bin/bash
# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

GREEN=$(tput setaf 2)
LIGHTBLUE=$(tput setaf 6)
WHITE=$(tput setaf 15)

function check {
  attempts=5;
  Password=$(sed -nr "/^\[Settings\]/ { :l /^password[ ]*=/ { s/.*=[ ]*//; p; q;}; n; b l;}" <Configuration/Configuration.ini)
  printf "${LIGHTBLUE}\nINSERT YOUR UPDATE PASSWORD YOU HAVE $attempts ATTEMPTS\n\n"
  while [[ $attempts>0 ]];
    do
      read -sp "$GREEN[#MR.HOLMES#]$WHITE-->" pass
      while [[ $pass == "" ]]
      do
        printf "${LIGHTBLUE}\n\nINSERT YOUR UPDATE PASSWORD YOU HAVE $attempts ATTEMPTS\n\n"
        read -sp "$GREEN[#MR.HOLMES#]$WHITE-->" pass
      done
      if [ "$pass" == "$Password" ];
        then
        printf "${LIGHTBLUE}\n\nPASSWORD CORRECT!\n"
        update
      fi
        ((attempts=attempts-1))
        printf "$LIGHTBLUE\n\nWRONG PASSWORD REMAINING: $attempts ATTEMPTS\n\n"
    done
    printf "${WHITE}\n\nYOU HAVE: $attempts PRESS ENTER TO EXIT"
    read -p
    exit 1
}

function update {
  Update_path=$(sed -nr "/^\[Settings\]/ { :l /^path[ ]*=/ { s/.*=[ ]*//; p; q;}; n; b l;}" <Configuration/Configuration.ini)
  cd $Update_path
  mv Mr.Holmes Mr.Holmes2  &>/dev/null
  git clone https://github.com/Lucksi/Mr.Holmes &>/dev/null | printf "$WHITE\nUPDATING MR.HOLMES..\n"

  if [ $? -eq  0 ];
    then
    cd $Update_path
    printf "${WHITE}\nWOULD YOU LIKE TO DELETE THE OLD FILES?(1)YES(2)NO\n\n"
    read -p "$GREEN[#MR.HOLMES#]$WHITE-->" conf
    if [ $conf = 1 ];
      then
      rm -r Mr.Holmes2 &>/dev/null | printf "${LIGHTBLUE}\nDELETING OLD MR.HOLMES FILES"
    else
      printf "${LIGHTBLUE}\nKEEPING OLD MR.HOLMES FILES"
    fi
    sleep 2
    printf "${WHITE}\n\nMR.HOLMES UPDATED CORRECTLY\n\n"
    read -p "$GREEN[#MR.HOLMES#]$WHITE-->" confvar
    printf "${WHITE}\nPRESS ENTER TO EXIT"
    read -p
    exit 1

  fi
    printf "${LIGHTBLUE}\n\nMR.HOLMES NOT INSTALLED HAVE YOU CHECKED YOUR INTERNET CONNECTION?\n\n"
    mv Mr.Holmes2 Mr.Holmes
    exit 1
}
check
