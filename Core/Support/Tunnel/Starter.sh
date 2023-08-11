#!/bin/bash
# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

ngrok http $1 >/dev/null 2>&1 &
sleep 5
link=$(curl -s -N http://127.0.0.1:4040/api/tunnels|sed 's#"# #g'|sed 's#http#\nhttp#g'|sed 's#.io#.io\n#g'|grep https|head -n 1)
if [ "$link" == "" ];
    then
    link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
fi
printf "$link"