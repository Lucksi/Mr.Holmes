<!--ORIGINAL CREATOR: Luca Garofalo (Lucksi)
AUTHOR: Luca Garofalo (Lucksi)
Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
License: GNU General Public License v3.0-->
<!DOCTYPE html>
<html>
    <head>
        <title>Dashboard</title>
        <?php
            require_once("../Actions/Language_Controller.php");
            Total_Languages();
        ?>
        <script src = "../Script/Author.js"></script>
        <script src = "../Script/Arrow.js"></script>
        <?php
            $exception = "/firefox/i";
            $browser = $_SERVER["HTTP_USER_AGENT"];
            if(preg_match($exception,$browser)){
     
            }
            else{
                require("../Actions/Session_Checker.php");
            }
            require_once("../Actions/Theme_Controller.php");
            $File_Name = "Main.css";
            Body_Theme($File_Name);
        ?>
        <link rel = "icon" href = "../Icon/Base/Logo.png">
        <meta charset ="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=0.9">
        <meta name="theme-color" content="#000000">
    </head>
    <?php
        require_once("../Actions/Language_Controller.php");
        $Modality = "Main";
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
                <a href = "Ports.php"></a>
                <a href="Email.php"></a>
                <a href="New_User.php"></a>
                <a href= "People.php"></a>
                <a id = "change1"></a>
                <?php 
                    require_once("../Actions/Language_Controller.php");
                    $Modality = "_Main_Mobile()";
                    List_Languages($Modality);
                ?>
            </div>
        </div>
        <div class = "languages">
            <button id = "Current" onclick="Active_Language()"></button>
            <div class = "Content" id = "Content">
                <?php 
                    require_once("../Actions/Language_Controller.php");
                    $Modality = "_Main()";
                    List_Languages($Modality);
                ?>
            </div>
        </div>
    </div>
    <?php require_once("../Actions/Javascript_Controller.php");NoScript_Alert();?>
    <div class = "Upper-card">
        <?php require_once("../Actions/Theme_Controller.php");Image()?>
        <p id = "Const">A COMPLETE OSINT TOOL</p>
        <div class = "Cards">
            <div id = "Username">
                <?php require_once("../Actions/Theme_Controller.php");Cards()?>
            </div>
        </div>
        <a href = "#Footer" id = "Arrow" onclick="Active()"></a>
        <div class = "Footer" id = "Footer" name = "Footer">
            <p id = "Const">MY-CONTACTS</p>
            <div class = "Board">
                <a href = "https://instagram.com/lucks_022" target = "blank"><img src = "../Icon/instagram.png" id = "Exc" abbr title = "Instagram"></a>
                <a href = "mailto:lukege287@gmail.com" target = "blank"><img src = "../Icon/Email.png" abbr title = "Email" ></a>
                <a href = "https://github.com/Lucksi" target = "blank"><img src = "../Icon/Git-hub.png" abbr title = "GitHub"></a>
                <a href = "https://linkedin.com/in/lucksi" target = "blank"><img src = "../Icon/linkedin.png" abbr title = "Linkedin"></a>
                <a href = "https://twitter.com/Lucksi_22" target = "blank"><img src = "../Icon/Twitter.png" abbr title = "Twitter"></a>
            </div>
        </div>
    </body>
</html>
