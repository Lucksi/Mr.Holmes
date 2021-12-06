<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<!DOCTYPE html>
<html>
    <head>
        <title>New User</title>
        <script src = "../Script/Language.js"></script>
        <script src = "../Script/Arrow.js"></script>
        <script src = "../Script/Author.js"></script>
        <?php
            require("../Actions/Session_Checker.php");
            require_once("../Actions/Theme_Controller.php");
            $File_Name = "New_User.css";
            Body_Theme($File_Name);
            require("../Actions/Credentials_Controller.php");
        ?>
        <link rel = "icon" href = "../Icon/Base/Logo.png">
        <meta charset ="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=0.9">
        <meta name="theme-color" content="#000000">
    </head>
    <?php
        require_once("../Actions/Language_Controller.php");
        $Modality = "User";
        Get_Language($Modality);
    ?>
        <div class = "Top-bar">
            <p>MR.HOLMES</p>
            <div class = "Hidden-bar">
                <button id = "Menu" onclick="Active_Mobile()">MENU</button>
                <div class="Options" id ="Options1">
                    <a href="Username.php"></a>
                    <a href="Websites.php"></a>
                    <a href="Phone.php"></a>
                    <a href="Ports.php"></a>
                    <a href="New_User.php"></a>
                    <a id = "change1"></a>
                    <a onclick="Italian_User_Mobile()">Italiano</a>
                    <a onclick="English_User_Mobile()">English</a>
                    <a onclick="French_User_Mobile()">Français</a>
                </div>
            </div>
            <div class = "languages">
                <button id = "Current" onclick="Active_Language()"></button>
                <div class = "Content" id = "Content">
                    <a onclick="Italian_User()">Italiano</a>
                    <a onclick="English_User()">English</a>
                    <a onclick="French_User()">Français</a>
                </div>
            </div>
            <div class = "Link">
                <a href = "Username.php"></a>
                <a href = "Websites.php"></a>
                <a href = "Phone.php"></a>
                <a href = "Ports.php"></a>
                <a href= "New_User.php"></a>
                <a id = "change2"></a>
            </div>
        </div>
        <div class = "Upper-card">
            <?php require_once("../Actions/Theme_Controller.php");Image();?>
        </div>
        <center>
        <div class = "Container">
            <form action = "" method = "POST">
                <p id = "Const" name = "Create"></p>
                <p id = "Const">USERNAME</p>
                <input type = "text" placeholder = "Username..."  name = "username">
                <p id = "Const">PASSWORD</p>
                <input type = "password" placeholder = "Password..." name = "password">
                <button name = "Button2" id = "New_User"></button>
            </form>
        </div>
        <center>
        <noscript>Please enable javascript</noscript>
    </body>
</html>
