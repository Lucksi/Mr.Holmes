#!/bin/bash
GREEN=$(tput setaf 2)
LIGHTBLUE=$(tput setaf 6)
WHITE=$(tput setaf 15)


function check {
  attempts=5;
  Password_path=$(<"Configuration/Pass_Update.txt")
  Password="${Password_path//$'\n'/ }"
  printf "$LIGHTBLUE\nINSERT YOUR UPDATE PASSWORD YOU HAVE $attempts ATTEMPTS\n\n"
  while [[ $attempts>0 ]];
    do
      read -p "$GREEN[#MR.HOLMES#]$WHITE-->" pass
      if [ "$pass" == "$Password" ];
        then
        printf "$LIGHTBLUE\nPASSWORD CORRECT!\n"
        update
      fi
        ((attempts=attempts-1))
        printf "$LIGHTBLUE\nWRONG PASSWORD REMAINING $attempts ATTEMPTS\n\n"
    done
    exit 1
}


function update {
  Update_path=$(<"Configuration/Update.txt")
  Update_path="${Update_path//$'\n'/ }"
  cd $Update_path
  mv Mr.Holmes Mr.Holmes2  &>/dev/null
  git clone https://github.com/Lucksi/Mr.Holmes &>/dev/null | printf "$WHITE\nUPDATING MR.HOLMES..\n"

  if [ $? -eq  0 ];
    then
    cd $Update_path
    cd Mr.Holmes
    chmod +x install.sh
    cd ../
    printf "$WHITE\nWOULD YOU LIKE TO DELETE THE OLD FILES?(1)YES(2)NO\n\n"
    read -p "$(tput setaf 2)[#MR.HOLMES#]$WHITE-->" conf
    if [ $conf = 1 ];
      then
      rm -r Mr.Holmes2 &>/dev/null | printf "$LIGHTBLUE\nDELETING OLD MR.HOLMES FILES"
    else
      printf "$LIGHTBLUE\nKEEPING OLD MR.HOLMES FILES"
    fi
    sleep 2
    printf "$(tput setaf 15)\n\nMR.HOLMES UPDATED CORRECTLY WOULD YOU LIKE TO RUN THE INSTALLER NOW?(1)YES(2)NO\n\n"
    read -p "$GREEN[#MR.HOLMES#]$WHITE-->" confvar
    if [ $confvar = 1 ];
      then
        cd Mr.Holmes
          ./install.sh
          exit 1
    fi
      printf "$WHITE\nPRESS ENTER TO EXIT"
      read -p exi
      exit 1

  fi
    printf "$LIGHTBLUE\n\nMR.HOLMES NOT INSTALLED HAVE YOU CHECKED YOUR INTERNET CONNECTION?\n\n"
    mv Mr.Holmes2 Mr.Holmes
    exit 1
}

check