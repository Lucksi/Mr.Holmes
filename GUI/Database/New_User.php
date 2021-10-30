<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<!DOCTYPE html>
<html>
    <head>
        <title>New User</title>
        <?php
            require_once("../Actions/Theme_Controller.php");
            $File_Name = "New_User.css";
            Body_Theme($File_Name);
        ?>
        <?php require("../Actions/Credentials_Controller.php");?>
        <link rel = "icon" href = "../Icon/Base/Logo.png">
        <script src = "../Script/Language.js"></script>
        <script src = "../Script/Arrow.js"></script>
        <script src = "../Script/Author.js"></script>
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
                    <a href="Username.php">Username</a>
                    <a href="Websites.php">Website</a>
                    <a href="Phone.php">Phone</a>
                    <a href="Ports.php">Port</a>
                    <a href="New_User.php">Create User</a>
                    <a id = "change1" onclick="English()">Author</a>
                    <a onclick="Italian_User()">Italiano</a>
                    <a onclick="English_User()">English</a>
                    <a onclick="French_User()">Français</a>
                </div>
            </div>
            <div class = "languages">
                <button id = "Current" onclick="Active_Language()">English</button>
                <div class = "Content" id = "Content">
                    <a onclick="Italian_User()">Italiano</a>
                    <a onclick="English_User()">English</a>
                    <a onclick="French_User()">Français</a>
                </div>
            </div>
            <div class = "Link">
                <a href = "Username.php">Username</a>
                <a href = "Websites.php">Website</a>
                <a href = "Phone.php">Phone</a>
                <a href = "Ports.php">Port</a>
                <a href= "New_User.php">Create User</a>
                <a id = "change2">Author</a>
            </div>
        </div>
        <div class = "Upper-card">
            <?php require_once("../Actions/Theme_Controller.php");Image();?>
        </div>
        <center>
        <div class = "Container">
            <form action = "" method = "POST">
                <p id = "Const" name = "Create">CREATE USER</p>
                <p id = "Const">USERNAME</p>
                <input type = "text" placeholder = "Username..."  name = "username">
                <p id = "Const">PASSWORD</p>
                <input type = "password" placeholder = "Password..." name = "password">
                <button name = "Button2" id = "New_User">Submit</button>
            </form>
        </div>
        <center>
    </body>
</html>