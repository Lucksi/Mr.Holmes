<!--ORIGINAL CREATOR: Luca Garofalo (Lucksi)
AUTHOR: Luca Garofalo (Lucksi)
Copyright (C) 2023 Lucksi <lukege287@gmail.com>
License: GNU General Public License v3.0-->
<!DOCTYPE HTML>
<html>
    <head>
        <title>Graph</title>
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
            $File_Name = "Schema.css";
            Body_Theme($File_Name);
        ?>   
        <link rel = "icon" href = "../Icon/Base/Logo.png">
        <meta charset ="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=0.9">
        <meta name="theme-color" content="#000000">
    </head>
    <?php
        require_once("../Actions/Language_Controller.php");
        $Modality = "SelectMap";
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
                    <a href ="Ports.php"></a>
                    <a href = "Email.php"></a>
                    <a href="New_User.php"></a>
                    <a id = "change1"></a>
                    <?php 
                        require_once("../Actions/Language_Controller.php");
                        $Modality = "_SelectMap_Mobile()";
                        List_Languages($Modality);
                    ?>
                </div>
            </div>
            <div class = "languages">
                <button id = "Current" onclick="Active_Language()"></button>
                <div class = "Content" id = "Content">
                    <?php 
                        require_once("../Actions/Language_Controller.php");
                        $Modality = "_SelectMap()";
                        List_Languages($Modality);
                    ?>
                </div>
            </div>
            <div class = "Link">
                <a href= "Username.php"></a>
                <a href = "Websites.php"></a>
                <a href = "Phone.php"></a>
                <a href = "Ports.php"></a>
                <a href = "Email.php"></a>
                <a href= "New_User.php"></a>
                <a href="Schema.php"></a>
                <a href="People.php"></a>
                <a href="Map.php"></a>
                <a id = "change2"></a>
            </div>
        </div>
        <?php 
            require_once("../Actions/Javascript_Controller.php");NoScript_Navbar();
            echo"<br>"; 
            require_once("../Actions/Javascript_Controller.php");NoScript_Alert();
        ?>
        <div class = "Upper-card">
            <?php require_once("../Actions/Theme_Controller.php");Image();?>
            <div id = "Options">
                <a href = "NewMap.php"><button  id = "New" name = "New" type = "button"></button></a>
                <a href = "OpenMap.php"><button  id = "Open" name = "Open" type = "button"></button></a>
                <a href = "DeleteMap.php"><button  id = "Del" name = "Del" type = "button"></button></a>
            </div>
        </div> 
    </body>
</html>
