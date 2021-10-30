<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<!DOCTYPE html>
<html>
    <head>
        <title>Login</title>
        <?php
            require_once("../Actions/Theme_Controller.php");
            $File_Name = "Login.css";
            Body_Theme($File_Name);
        ?>
        <?php require("../Actions/Credentials_Controller.php");?>
        <link rel = "icon" href = "../Icon/Mr.Holmes.png">
        <script src = "../Script/Language.js"></script>
        <script src = "../Script/Arrow.js"></script>
        <meta charset ="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=0.9">
        <meta name="theme-color" content="#000000">
    </head>
    <?php
        require_once("../Actions/Language_Controller.php");
        $Modality = "Login";
        Get_Language($Modality);
    ?>
        <div class = "Top-bar">
            <p>MR.HOLMES</p>
            <div class = "languages">
                <button id = "Current" onclick="Active_Language()">English</button>
                <div class = "Content" id = "Content">
                    <a onclick="Italian_Login()">Italiano</a>
                    <a onclick="English_Login()">English</a>
                    <a onclick="French_Login()">French</a>
                </div>
            </div>
        </div>
        <div class = "Upper-card">
            <?php require_once("../Actions/Theme_Controller.php");Image();?>
        </div>
        <center>
        <div class = "Container">
            <form action = "" method = "POST">
                <p id = "Const">LOGIN</p>
                <p id = "Const">USERNAME</p>
                <input type = "text" placeholder = "Username..."  name = "username">
                <p id = "Const">PASSWORD</p>
                <input type = "password" placeholder = "Password..." name = "password">
                <button name = "Button">Submit</button>
            </form>
        </div>
        <center>
    </body>
</html>
