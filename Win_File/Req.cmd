::AUTHOR: Luca Garofalo (Lucksi)
::Copyright © 2021 Lucksi
::License: GNU General Public License v3.0

@ECHO OFF

pip3 install -r requirements.txt 2>NUL >NUL
echo REQUIREMENTS INSTALLED SUCCESFULLY
cd ../
echo Path= %CD% >>Mr.Holmes/Configuration/Configuration.ini