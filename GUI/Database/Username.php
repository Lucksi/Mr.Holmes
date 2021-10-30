<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<!DOCTYPE html>
<html> 
    <head>
        <title>Username</title>
        <?php
            require("../Actions/Session_Checker.php");
            require_once("../Actions/Theme_Controller.php");
            $File_Name = "Username.css";
            Body_Theme($File_Name);
        ?>   
        <link rel = "icon" href = "../Icon/Base/Logo.png">
        <meta charset ="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=0.9">
        <meta name="theme-color" content="#000000">
        <script src = "../Script/Language.js"></script>
        <script src = "../Script/Author.js"></script>
        <script src = "../Script/Arrow.js"></script>
    </head>
    <?php
        require_once("../Actions/Language_Controller.php");
        $Modality = "Username";
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
                    <a href ="Ports.php">Port</a>
                    <a href="New_User.php">Create User</a>
                    <a id = "change1" onclick="English()">Author</a>
                    <a onclick="Italian_Username_Mobile()">Italiano</a>
                    <a onclick="English_Username_Mobile()">English</a>
                    <a onclick="French_Username_Mobile()">Français</a>
                </div>
            </div>
            <div class = "languages">
                <button id = "Current" onclick="Active_Language()">English</button>
                <div class = "Content" id = "Content">
                    <a onclick="Italian_Username()">Italiano</a>
                    <a onclick="English_Username()">English</a>
                    <a onclick="French_Username()">Français</a>
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
            <center>
            <form action = "" method="POST">
            <input type= "text" placeholder = "Insert a Username..." id = "Searcher" name = "Searcher">
            <button  width="fit-content" id = "But" name = "Button">Search
            </center>
        </div>
    </form>
    <?php require("../Actions/Usernames_Finder.php");?>
    </div>
        <noscript>Please enable javascript</noscript>
    </body>
</html>