<p align="center">
  <img width="650px" height="100px" src="Icon/Banner.png">
</p>

<p align = "center">
  <img src = "https://img.shields.io/github/stars/Lucksi/Mr.Holmes">
  <img src = "https://img.shields.io/github/forks/Lucksi/Mr.Holmes">
  <img src = "https://img.shields.io/badge/Maintained%3F-yes-green.svg">
  <img src = "https://img.shields.io/github/license/Lucksi/Mr.Holmes">
  <img src = "https://img.shields.io/github/repo-size/Lucksi/Mr.Holmes">
  <img src= "https://img.shields.io/github/languages/count/Lucksi/Mr.Holmes">
  <img src = "https://visitor-badge.laobi.icu/badge?page_id=Lucksi.Mr.Holmes">
</p>

# :mag: Mr.Holmes 

**Mr.Holmes ist ein Tool zum Sammeln von Informationen (OSINT). Der Hauptzweck besteht darin, mithilfe öffentlicher Quellen im Internet Informationen über Domänen, Benutzernamen und Telefonnummern zu erhalten. Außerdem wird der Google-Dorks-Angriff für bestimmte Forscher genutzt. Es verwendet außerdem Proxys, um Ihre Anfragen vollständig anonym zu machen, und eine WhoIS-API, um weitere Informationen über eine Domain zu erhalten.**
<br>

# :heavy_exclamation_mark: HAFTUNGSAUSSCHLUSS
**Dieses Tool ist nicht 100 % genau und kann daher manchmal ausfallen. Außerdem dient dieses Tool nur zu Bildungs- und Forschungszwecken. Ich übernehme keinerlei Verantwortung für eine unsachgemäße Verwendung dieses Tools.**
<br>

#  SCREENSHOT
![Screenshot](Screenshot/Screenshot.png)

<br>

<p align = "center">
<img src = "Screenshot/Termux.png" height = "400px" width = "300px">
</p>

<br>

# :heavy_check_mark: INSTALLATION LINUX/MAC:
```bash
git clone https://github.com/Lucksi/Mr.Holmes
cd Mr.Holmes
sudo apt-get update
sudo chmod +x install.sh
sudo bash install.sh
```
<br>

# :heavy_check_mark: INSTALLATION WINDOWS (1°WAY)
**Wenn Sie Git auf Ihrem Windows-Rechner installiert haben, können Sie die folgenden Befehle ausführen:**
```cmd
git clone https://github.com/Lucksi/Mr.Holmes
cd Mr.Holmes
Install.cmd
```
<br>

# :heavy_check_mark: INSTALLATION WINDOWS (2° WAY):
**Wenn Sie die ZIP-Datei von Mr.Holmes herunterladen, sollten Sie diese zunächst entpacken und anschließend die folgenden Befehle ausführen:**
```cmd
ren Mr.Holmes-master Mr.Holmes
cd Mr.Holmes
Install.cmd
```
<br>

# :heavy_check_mark: INSTALLATION TERMUX:
```bash
pkg install proot
git clone https://github.com/Lucksi/Mr.Holmes
cd Mr.Holmes
proot -0 chmod +x install_Termux.sh
./install_Termux.sh
```
<br>

#  USAGE LINUX/MAC:
    sudo python3 MrHolmes.py
    OR:
    cd Launchers
    Execute Launcher.sh

<br>

#  USAGE TERMUX/WINDOWS:
    python3 MrHolmes.py
<br>

#  USAGE WINDOWS:
    python MrHolmes.py
    OR
    cd Launchers
    Execute Win_Launcher.exe

<br>

# API KEY LINK:
    https://whois.whoisxmlapi.com
<br>

# SETTINGS FOLDER:

    Configuration/Configuration.ini
<br>

# :heavy_exclamation_mark: ATTENTION
**DATENBANK NICHT AUF TERMUX VERFÜGBAR**
<br>

# :heavy_exclamation_mark: ATTENTION ON WINDOWS
**WENN PYTHON UND PHP NICHT INSTALLIERT WERDEN, MÜSSEN SIE SIE MANUELL HERUNTERLADEN:**
    
<br>

# VERSIONS LIST:
    https://lucksi.github.io/Mr.Holmes/Pages/versions.html
<br>

# :heavy_check_mark: GUI DARK/LIGHT MODE:
```bash
cd GUI
cd Theme
edit Mode.json
write:Light=(Light-Mode)
write:Dark=(Dark-Mode) 
write:High-Contrast(High-Contrast-Mode)
```
<br>

# :heavy_check_mark: Mode.json CODE EXAMPLE:
```json
{
    "Color": {
        "Background": "Light"
    }
}
```
<br>

# :heavy_check_mark: GUI/USERNAME/PASSWORD:
```bash
cd GUI
cd Credentials
edit Login.json
write:Status=Active/Deactive
edit Users.json
write:Username=Your Username
write:Password=Your Password
```
<br>

# :heavy_check_mark: Login.json CODE EXAMPLE:
```json    
{
    "Database": {
        "Status": "Active"
    }
}
```
<br>

# :heavy_check_mark: Users.json CODE EXAMPLE
```json
{
    "Users":[
        {
            "Username": "Your Username",
            "Password": "Your Password"
        }
    ]
}
```
<br>

# :heavy_check_mark: LANGUAGE SETTINGS:
```bash
cd GUI
cd Language
edit Language.json
```
<br>

# :heavy_check_mark: Language.json CODE EXAMPLE:
```json
{
    "Language": {
        "Preference": "English"
    }
}
```
<br>

# DEFAULT USERNAME AND PASSWORD:
    Username:Admin
    Password:Qwerty123

<br>

# AVAIABLE LANGUAGES:
    Italiano 🇮🇹 
    English 🏴󠁧󠁢󠁥󠁮󠁧󠁿
    Français 🇫🇷
    Deutsch 🇩🇪

<br>

# ACTUAL VERSION:
## T.G.D-1.0.4

<br>

# INTERACTIVE MAP HAS BEEN MADE WITH:
**Broschüre: https://leafletjs.com**

<br>

# USERNAME ENTITIES:
**Die Symbole im Ordner: /GUI/Icon/Entities/Site_Icon stammen von: https://www.iconfinder.com/. Alle Quellenangabe geht an die jeweiligen Ersteller**

<br>

# ENCODING:
**Mit dieser Version ist es möglich, Ihre Berichte zu verschlüsseln**

<br>

# DECODING:
**Mit dieser Version ist es möglich, Ihre Berichte zu entschlüsseln**

<br>

# HYPOTHESIS
**Diese neue Version ermöglicht es, auf der Grundlage ihrer Zahlen in verschiedenen sozialen Medien, einschließlich möglicher Hobbys/Interessen, einige „Hypothesen“ zu diesem Thema zu erstellen (diese sind möglicherweise nicht zu 100 % zugänglich)**

<br>

# EMAIL-LOOKUP:
**Mit dieser neuen Version ist es möglich, zu überprüfen, ob eine E-Mail mit bestimmten sozialen Netzwerken/Diensten verbunden ist, ohne dass die Zielperson dies bemerkt.**

<br>

# GRAPHS:
**Mit dieser neuen Version wurde die Möglichkeit hinzugefügt, Diagramme zu erstellen, um ein Schema für die Informationsplanung zu erstellen.**

<br>

# EXAMPLE:

![Screenshot](Screenshot/Graph_Test.png)

<br>

# MAPS:
**Mit dieser neuen Version wurde die Möglichkeit hinzugefügt, interaktive Karten zu erstellen.**

<br>

# EXAMPLE:

![Screenshot](Screenshot/Map_Test.png)

<br>

# DORKS:
**Mit dieser neuen Version ist es möglich, Video/Ton/Bilder über Dorks (1) zu durchsuchen und spezifische Recherchen durchzuführen, indem das Datum „1998/01/1“ oder der Datumsbereich „1998/01/01-2020/12“ hinzugefügt wird /31' (2).**

<br>

# EXAMPLE (1):

![Screenshot](Screenshot/Dorks.png)

<br>

# EXAMPLE (2):

![Screenshot](Screenshot/Dorks2.png)

<br>

# PDF:
**Mit dieser neuen Version wurde die Möglichkeit hinzugefügt, Ihre Diagramme in PDF zu konvertieren.**

<br>

# EXAMPLE:
<p align = "center">
<img src="Screenshot/Dark_Pdf.png" height ="400px" width = "400px" border = "5px" style="border-color:white;">
</p>

<br>

# AVAILBLE PDF-THEMES:
    Light 🌕
    Dark 🌗
    High-Contrast 🌗

<br>

# FILE-TRANSFER:
**Mit dieser Version ist es möglich, Ihre Berichte per QR-Code direkt auf Ihr Telefon zu übertragen**

<br>

# FILE-TRANSFER PAGE:
<p align = "center">
<img src="Screenshot/File-Transfer.jpg" height ="500px" width = "300px" border = "5px" style="border-color:white;">
</p>

<br>

# :last_quarter_moon: DARK MODE:
![Screenshot](Screenshot/Dark_Mode.png)

<br>

<p align = "center">
<img src="Screenshot/Dark.jpg" height ="500px" width = "300px" border = "5px" style="border-color:white;">
</p>

<br>

# :full_moon: LIGHT MODE:
![Screenshot](Screenshot/Light_Mode.png)

<br>

<p align = "center">
<img src="Screenshot/Light.jpg" height ="500px" width = "300px" border = "5px" style="border-color:gray;">
</p>


<br>

# :last_quarter_moon: HIGH-CONTRAST MODE:
![Screenshot](Screenshot/High-Contrast_Mode.png)

<br>

<p align = "center">
<img src="Screenshot/High-Contrast.jpg" height ="490px" width = "300px" border = "5px" style="border-color:white;">
</p>

<hr>
<br>


## <p align = center> STARGAZERS OVER TIME 


[![Stargazers over time](https://starchart.cc/Lucksi/Mr.Holmes.svg)](https://starchart.cc/Lucksi/Mr.Holmes)

<br>

## <p align= center>MADE WITH :heart: BY LUCKSI IN :it:</p>

## <p align = center>  URSPRÜNGLICHER ERSTELLER: <a href = "https://github.com/Lucksi">LUCA GAROFALO (Lucksi)</a></p>


## <p align = center>LIZENZ: GPL-3.0 License <br>COPYRIGHT: (C) 2021-2023 Lucksi 
