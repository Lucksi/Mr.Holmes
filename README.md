<p align="center">
  <img width="200" height="200" src="Icon/Mr.Holmes.png">
</p>

# :mag: Mr.Holmes 
### Mr.Holmes is a information gathering tool (OSINT). Is main purpose is to gain information about domains,username and phone numbers with the help of public source avaiable on the internet also it use the google dorks attack for specific researchers. It also use proxies for make your requests completley anonymous and a WhoIS Api for getting more information about a domain.
<br>

# :heavy_exclamation_mark: DISCLAIMER
### This Tool is Not 100% Precise so it can fail somtimes. Also this tool is made for educational and research purposes only..use it wisely
<br>

#  SCREENSHOT
![Screenshot](Screenshot/Screenshot.png)

<br>

# :heavy_check_mark: INSTALLATION LINUX/MAC:
    git clone https://github.com/Lucksi/Mr.Holmes
    cd Mr.Holmes
    sudo chmod +x install.sh
    sudo ./install.sh
<br>

# :heavy_check_mark: INSTALLATION TERMUX:
    pkg install proot
    git clone https://github.com/Lucksi/Mr.Holmes
    cd Mr.Holmes
    proot -0 chmod +x install_Termux.sh
    ./install_Termux.sh
<br>

#  USAGE LINUX/MAC:
    sudo python3 MrHolmes.py
<br>

#  USAGE TERMUX:
    python3 MrHolmes.py
<br>

# API KEY LINK:
    https://whois.whoisxmlapi.com
<br>

# SETTINGS FOLDER:

    Configuration/Configuration.ini
<br>

# :heavy_exclamation_mark: ATTENTION
### DATABASE NOT AVAIABLE ON TERMUX
<br>

# VERSIONS LIST:
    https://lucksi.github.io/Mr.Holmes/Pages/versions.html
<br>

# :heavy_check_mark: GUI DARK/LIGHT MODE:
    cd GUI
    cd Theme
    edit Mode.json
    write:Light=(Light-Mode)
    write:Dark=(Dark-Mode) 
    write:High-Contrast(High-Contrast-Mode)
    write:Uchiha(Uchiha-Mode)

<br>

# MODE CODE EXAMPLE:
    {
        "Color": {
            "Background": "Light"
        }
    }
    

<br>

# :heavy_check_mark: GUI/USERNAME/PASSWORD:
    cd GUI
    cd Credentials
    edit Login.json
    write:Status=Active/Deactive
    edit Users.json
    write:Username=Your Username
    write:Password=Your Password
#

<br>

# MODE CODE EXAMPLE:
    Login.json
    {
        "Database": {
            "Status": "Active",
        }
    }
    Users.json
    {
        "Users":[
            {
                "Username": "Your Username,
                "Password": "Your Password,
            }
        ]
    }
<br>

# DEFAULT USERNAME AND PASSWORD:
    Username:Admin
    Password:Qwerty123

<br>

# INTERACTIVE MAP HAS BEEN MADE WITH:
## Leaflet: https://leafletjs.com

<br>

# :last_quarter_moon: DARK MODE:
![Screenshot](Screenshot/Dark_Mode.png)

<br>

# :full_moon: LIGHT MODE:
![Screenshot](Screenshot/Light_Mode.png)

<br>

# :last_quarter_moon: HIGH-CONTRAST MODE:
![Screenshot](Screenshot/High-Contrast_Mode.png)

<br>

# Uchiha MODE:
![Screenshot](Screenshot/Uchiha_Mode.png)

<br>

## <p align= center>MADE WITH :heart: BY LUCKSI IN :it:</p>
