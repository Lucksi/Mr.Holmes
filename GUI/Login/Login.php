<!--ORIGINAL CREATOR: Luca Garofalo (Lucksi)
AUTHOR: Luca Garofalo (Lucksi)
Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
License: GNU General Public License v3.0-->
<!DOCTYPE html>
<html>
    <head>
        <title>Login</title>
        <?php
            require_once("../Actions/Language_Controller.php");
            Total_Languages();
        ?>
        <script src = "../Script/Arrow.js"></script>
        <?php
            require_once("../Actions/Theme_Controller.php");
            $File_Name = "Login.css";
            Body_Theme($File_Name);
        ?>
        <link rel = "icon" href = "../Icon/Mr.Holmes.png">
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
                    <?php 
                        require_once("../Actions/Language_Controller.php");
                        $Modality = "_Login()";
                        List_Languages($Modality);
                    ?>
                </div>
            </div>
        </div>
        <div class = "Upper-card">
            <?php require_once("../Actions/Theme_Controller.php");Image();?>
        </div>
        <center>
        <div class = "Container">
            <form action = "../Actions/Credentials_Controller.php" method = "POST">
                <p id = "Const">LOGIN</p>
                <p id = "Const">USERNAME</p>
                <input type = "text" placeholder = "Username..."  name = "username" autocomplete = "off">
                <p id = "Const">PASSWORD</p>
                <input type = "password" placeholder = "Password..." name = "password">
                <button name = "Button">Submit</button>
            </form>
        </div>
        <center>
    </body>
</html>
