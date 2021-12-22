# AUTHOR: Luca Garofalo (Lucksi)
# Copyright © 2021 Lucksi
# License: GNU General Public License v3.0

function Banner(){
    Clear-Host
    Get-Content("Banners/Banner6.txt")
}

function Packet_Installer(){
    Write-Host "`nINSTALLING PYTHON3..."
    Install-Package python3 -Scope CurrentUser | Out-Null
}

function Options(){
    $Email = Read-Host -Prompt "`nINSERT YOUR EMAIL ADDRESS`n`n[#MR.HOLMES#]-->"
    while($Email -eq ""){
        $Email = Read-Host -Prompt "`nINSERT YOUR EMAIL ADDRESS`n`n[#MR.HOLMES#]-->"
    }
    $Password = Read-Host -Prompt "`nINSERT YOUR EMAIL PASSWORD`n`n[#MR.HOLMES#]-->"
    while($Password -eq ""){
        $Password = Read-Host -Prompt "`nINSERT YOUR EMAIL PASSWORD`n`n[#MR.HOLMES#]-->"
    }
    $Destination = Read-Host -Prompt "`nINSERT YOUR DESTINATION EMAIL`n`n[#MR.HOLMES#]-->"
    while($Destination -eq ""){
        $Destination = Read-Host -Prompt "`nINSERT YOUR DESTINATION EMAIL`n`n[#MR.HOLMES#]-->"
    }
    $Server = Read-Host -Prompt "`nINSERT YOUR SMTP-SERVER`n`n[#MR.HOLMES#]-->"
    while($Server -eq ""){
        $Server = Read-Host -Prompt "`nINSERT YOUR SMTP-SERVER`n`n[#MR.HOLMES#]-->"
    }
    $Port = Read-Host -Prompt "`nINSERT YOUR SMTP SERVER-PORT`n`n[#MR.HOLMES#]-->"
    while($Port -eq ""){
        $Port = Read-Host -Prompt "`nINSERT YOUR SMTP SERVER-PORT`n`n[#MR.HOLMES#]-->"
    }
    $Update_Password = Read-Host -Prompt "`nINSERT YOUR UPDATE PASSWORD`n`n[#MR.HOLMES#]-->"
    while($Update_Password -eq ""){
        $Update_Password = Read-Host -Prompt "`nINSERT YOUR UPDATE PASSWORD`n`n[#MR.HOLMES#]-->"
    }
    $Api = Read-Host -Prompt "`nINSERT YOUR WHOIS API KEY 'LEAVE EMPTY IF YOU HAVENT ONE'`n`n[#MR.HOLMES#]-->"
    if($Api -eq ""){
        $Api = "None"
    }
    $Proxy_List = Read-Host -Prompt "`nINSERT YOUR PROXY-LIST 'LEAVE EMPTY FOR USE THE DEFAULT ONE'`n`n[#MR.HOLMES#]-->"
    if($Proxy_List -eq ""){
        $Proxy_List = "Proxies/Proxy_list.txt"
    }
    $Log_Session = Read-Host -Prompt "`nWOULD YOU LIKE TO SAVE YOUR LOG SESSION(1)YES(2)NO`n`n[#MR.HOLMES#]-->"
    if($Log_Session -eq 1){
        $Log_Session = "True"
    }
    elseif($Log_Session -eq 2) {
        $Log_Session = "False"
    }
    $Token = Read-Host -Prompt "`nWOULD YOU LIKE TO ACCESS YOUR DATABASE ON OTHER DEVICES(ON THE SAME NETWORK)?(1)YES(2)NO`n`n[#MR.HOLMES#]-->"
    if($Token -eq 1){
        $Token = "True"
    }
    elseif ($Token -eq 2) {
        $Token = "False"
    }
    $Access = Read-Host -Prompt "`nWOULD YOU LIKE TO ADD SOME CREDENTIALS FOR ACCESS THE DATABASE?(1)YES(2)NO`n`n[#MR.HOLMES]-->"
    if ($Access -eq 1){
        $Access = "True"
    }
    elseif($Access -eq 2){
        $Access = "False"
    }
    if ($Access -eq "True"){
        '{
            "Database":{
                "Status": "Active"
            }
        }' | Out-File -FilePath .\GUI\Credentials\Login.json
        '{
            "Users":[
                {
                "Username": "Admin",
                "Password": "Qwerty123"
                }
            ]
        }' | Out-File -FilePath .\GUI\Credentials\Users.json
        Write-Host "`nYOUR DEFAULT CREDENTIALS ARE:`nUSERNAME: Admin`nPASSWORD: Qwerty123"
    }
    elseif ($Access -eq "False") {
        '{
            "Database":{
                "Status": "Deactive"
            }
        }' | Out-File -FilePath .\GUI\Credentials\Login.json
        '{
            "Users":[
                {
                "Username": "None",
                "Password": "None"
                }
            ]
        }' | Out-File -FilePath .\GUI\Credentials\Users.json
    }
    ";CHANGE THESE VALUE IF YOU WANT TO UPDATE YOUR SETTINGS FROM HERE" | Out-File -FilePath .\Configuration/Configuration.ini -Encoding Ascii
    ";BUT DO NOT CHANGE THE PARAMETERS NAME" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "[Smtp]" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "Email= $Email" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "Password= $Password" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "Destination= $Destination" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "Server= $Server" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "Port= $Port" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "[Settings]" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "Password= $Update_Password" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "Api_Key= $Api" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "Proxy_List= $Proxy_List" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "Show_Logs= $Log_Session" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "Database= $Token" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
}

function installer(){
    Write-Host "`nWELCOME TO THE INSTALLATION MANAGER WOULD YOU LIKE TO BEGIN(1)YES(2)NO?" -ForegroundColor Green
    $DECISION = Read-Host -Prompt "`n[#MR.HOLMES#]-->"
    if ( $DECISION -eq 1 ){
        Packet_Installer;
        Options;
        Write-Host "INSTALLING-PYTHON-REQUIREMENTS..." -ForegroundColor Blue
        Start-Process -FilePath .\Win_File\Req.cmd
        Write-Host "`nTHANK YOU FOR HAVE INSTALLED Mr.Holmes" -ForegroundColor Green
    }
    elseif ( $DECISION -eq 2) {
        Write-Host "`nINSTALLATION INTERRUPTED...EXIT" -ForegroundColor Green
    }
}
Banner;
installer;
Exit-PSSession;
