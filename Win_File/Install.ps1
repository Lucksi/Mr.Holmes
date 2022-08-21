# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

function Banner(){
    Clear-Host
    Get-Content("Banners/Banner6.txt")
}

function Packet_Installer(){
    Write-Host "`nINSTALLING PYTHON3..."
    Install-Module -Name Python3  -Scope CurrentUser | Out-Null
    Write-Host "`nINSTALLING PHP..."
    Install-Package Php -Scope CurrentUser | Out-Null
    Write-Host "`nUNPACKING PHP..."
    Install-Php -Scope CurrentUser | Out-Null
}

function Preferences(){
    $Language = Read-Host -Prompt "`nSELECT YOUR GUI-DEFAULT LANGUAGE`n(1)ENGLISH`n(2)ITALIANO`n(3)FRANÇAIS`n`n[#MR.HOLMES#]-->"
    while($Language -eq ""){
        $Color = Read-Host -Prompt "`nSELECT YOUR GUI-DEFAULT LANGUAGE`n(1)ENGLISH`n(2)ITALIANO`n(3)FRANÇAIS`n`n[#MR.HOLMES#]-->"
    }
    if($Language -eq 1){
        '{
            "Language":{
                "Preference": "English"
            }
        }' | Out-File -FilePath .\GUI\Language\Language.json -Encoding Ascii
        $mode = "ENGLISH"
    }
    elseif ($Language -eq 2) {
        '{
            "Language":{
                "Preference": "Italian"
            }
        }' | Out-File -FilePath .\GUI\Language\Language.json -Encoding Ascii
        $mode = "ITALIANO"
    }
    elseif ($Language -eq 3) {
        '{
            "Language":{
                "Preference": "French"
            }
        }' | Out-File -FilePath .\GUI\Language\Language.json -Encoding Ascii
        $mode = "FRANÇAIS"
    }

    Write-Host "`nGUI-LANGUAGE:$mode"
    $Color = Read-Host -Prompt "`nSELECT YOUR GUI-DEFAULT THEME`n(1)LIGHT`n(2)DARK`n(3)HIGH-CONTRAST`n(4)UCHIHA`n`n[#MR.HOLMES#]-->"
    while($Color -eq ""){
        $Color = Read-Host -Prompt "`nSELECT YOUR GUI-DEFAULT THEME`n(1)LIGHT`n(2)DARK`n(3)HIGH-CONTRAST`n(4)UCHIHA`n`n[#MR.HOLMES#]-->"
    }
    if($Color -eq 1){
        '{
            "Color":{
                "Background": "Light"
            }
        }' | Out-File -FilePath .\GUI\Theme\Mode.json -Encoding Ascii
        $mode = "LIGHT"
    }
    elseif ($color -eq 2) {
        '{
            "Color":{
                "Background": "Dark"
            }
        }' | Out-File -FilePath .\GUI\Theme\Mode.json -Encoding Ascii
        $mode = "DARK"
    }
    elseif ($Color -eq 3) {
        '{
            "Color":{
                "Background": "High-Contrast"
            }
        }' | Out-File -FilePath .\GUI\Theme\Mode.json -Encoding Ascii
        $mode = "HIGH-CONTRAST"
    }
    elseif ($color -eq 4) {
        '{
            "Color":{
                "Background": "Uchiha"
            }
        }' | Out-File -FilePath .\GUI\Theme\Mode.json -Encoding Ascii
        $mode = "UCHIHA"
    }

    Write-Host "`nGUI-THEME:$mode"
}

function Mail_Options(){
    $Opt = Read-Host -Prompt "`nWOULD YOU LIKE TO ENABLE EMAIL-OPTION(1)YES(2)NO`n`n[#MR.HOLMES#]-->"
    while($Opt -eq ""){
        $Email = Read-Host -Prompt "`nWOULD YOU LIKE TO ENABLE EMAIL-OPTION(1)YES(2)NO`n`n[#MR.HOLMES#]-->"
    }
    if ($Opt -eq 1){
        $Status = "Enabled"
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
    }
    elseif($Opt -eq 2){
        $Status ="Disabled"
		$Email ="None"
		$Password ="None"
		$Destination ="None"
		$Server ="None"
		$Port ="None"
    }
    else{
        Mail_Options
    }
   
}

function Options(){
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
    while ($Log_Session -eq ""){
        $Log_Session = Read-Host -Prompt "`nWOULD YOU LIKE TO SAVE YOUR LOG SESSION(1)YES(2)NO`n`n[#MR.HOLMES#]-->"
    }
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
    while($Access -eq ""){
        $Access = Read-Host -Prompt "`nWOULD YOU LIKE TO ADD SOME CREDENTIALS FOR ACCESS THE DATABASE?(1)YES(2)NO`n`n[#MR.HOLMES]-->"
    }
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
        }' | Out-File -FilePath .\GUI\Credentials\Login.json -Encoding Ascii
        '{
            "Users":[
                {
                "Username": "Admin",
                "Password": "Qwerty123"
                }
            ]
        }' | Out-File -FilePath .\GUI\Credentials\Users.json -Encoding Ascii
        Write-Host "`nYOUR DEFAULT CREDENTIALS ARE:`nUSERNAME: Admin`nPASSWORD: Qwerty123"
    }
    elseif ($Access -eq "False") {
        '{
            "Database":{
                "Status": "Deactive"
            }
        }' | Out-File -FilePath .\GUI\Credentials\Login.json -Encoding Ascii
        '{
            "Users":[
                {
                "Username": "None",
                "Password": "None"
                }
            ]
        }' | Out-File -FilePath .\GUI\Credentials\Users.json -Encoding Ascii
    }
    $Lang = Read-Host -Prompt "`nINSERT YOUR CLI-LANGUAGE`n(1)ENGLISH`n(2)ITALIANO`n(3)FRANÇAIS`n`n[#MR.HOLMES#]-->"
    while($Lang -eq ""){
        $Lang = Read-Host -Prompt "`nINSERT YOUR CLI-LANGUAGE`n(1)ENGLISH`n(2)ITALIANO`n(3)FRANÇAIS`n`n[#MR.HOLMES#]-->"
    }
    if($Lang -eq 1){
        $Cli = "english"
        $Mode = "ENGLISH"
    }
    elseif($Lang -eq 2){
        $Cli = "italian"
        $Mode = "ITALIANO"
    }
    elseif($Lang -eq 3){
        $Cli = "french"
        $Mode = "FRANÇAIS"
    }
    Write-Host "`nCLI-LANGUAGE:$Mode"
    Preferences;
    ";THIS FILE HAS BEEN GENERATE BY MR.HOLMES INSTALLER" | Out-File -FilePath .\Configuration/Configuration.ini -Encoding Ascii
    ";CHANGE THESE VALUE IF YOU WANT TO UPDATE YOUR SETTINGS FROM HERE" | Out-File -FilePath .\Configuration/Configuration.ini -Append -Encoding Ascii
    ";BUT DO NOT CHANGE THE PARAMETERS NAME" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "[Smtp]" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "status= $Status" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "email= $Email" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "password= $Password" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "destination= $Destination" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "server= $Server" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "port= $Port" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "[Settings]" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "password= $Update_Password" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "api_key= $Api" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "proxy_list= $Proxy_List" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "show_logs= $Log_Session" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "database= $Token" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
    "language= $Cli" | Out-File -FilePath .\Configuration\Configuration.ini -Append -Encoding Ascii
}

function installer(){
    Write-Host "`nWELCOME TO THE INSTALLATION MANAGER WOULD YOU LIKE TO BEGIN(1)YES(2)NO?" -ForegroundColor Green
    $DECISION = Read-Host -Prompt "`n[#MR.HOLMES#]-->"
    if ( $DECISION -eq 1 ){
        Packet_Installer;
        Mail_Options;
        Options;
        Write-Host "INSTALLING-PYTHON-REQUIREMENTS..." -ForegroundColor Blue
        Start-Process -FilePath .\Win_File\Req.cmd
        Write-Host "`nTHANK YOU FOR HAVE INSTALLED Mr.Holmes" -ForegroundColor Green
    }
    else{
        Write-Host "`nINSTALLATION INTERRUPTED...EXIT" -ForegroundColor Green
        Exit-PSSession;
    }
}
Banner;
installer;
Exit-PSSession;
