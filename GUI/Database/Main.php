<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<!DOCTYPE html>
<html>
    <head>
        <title>Dashboard</title>
        <?php
            $mode_file = "../Theme/Mode.json";
            if (file_exists($mode_file)){
                $reader = file_get_contents($mode_file);
                $parser = json_decode($reader,true); 
                $color = $parser["Color"]["Background"];
                $Style_name = "../Css/$color/Main.css";
                if (file_exists($Style_name)){
                    echo '<link rel = "stylesheet" href ="'.$Style_name.'">';                
                }
                else{
                    echo "<script>
                    alert ('VALUE NOT VALID MODE DISPLAYED:LIGHT-MODE');
                    </script>";
                    echo '<link rel = "stylesheet" href = "../Css/Light/Main.css">';
                }
            }
            else{
                echo "<script>
                alert ('THEME FILE NOT FOUND MODE DISPLAYED:LIGHT-MODE');
                </script>";
                echo '<link rel = "stylesheet" href = "../Css/Light/Main.css">';
            }
            echo "\n";
        ?>
        <link rel = "icon" href = "../Icon/Mr.Holmes.png">
        <meta charset ="UTF-8">
        <script src = "../../Script/Language.js"></script>
        <script src = "../../Script/Author.js"></script>
        <script src = "../../Script/Arrow.js"></script>
    </head>
    <body>
        <div class = "Top-bar">
            <p>MR.HOLMES</p>
            <div class = "languages">
                <button id = "Current">English</button>
                <div class = "Content">
                    <a onclick="Italian_Main()">Italiano</a>
                    <a onclick="English_Main()">English</a>
                </div>
            </div>
        </div>
        <div class = "Upper-card">
            <?php include("../Actions/Theme_Controller.php");?>
            <p id = "Const">A COMPLETE OSINT TOOL</p>
            <div class = "Cards">
                <div id = "Username">
                    <img src = "../Icon/social.png">
                    <p id = "Const">USERNAME</p>
                    <a href = "Username.php"><button>Search</button></a>
                </div>
                <div id = "Website">
                    <img src = "../Icon/browser.png">
                    <p id = "Const">WEBSITE</p>
                    <a href = "Websites.php"><button>Search</button></a>
                </div>
                <div id = "Phone">
                    <img src = "../Icon/phone.png">
                    <p id = "Const">Phone</p>
                    <a href = "Phone.php"><button>Search</button></a>
                </div>
            </div>
        </div>
        <a href = "#Footer" id = "Arrow" onclick="Active()"></a>
        <div class = "Footer" id = "Footer" name = "Footer">
            <p id = "Const">MY-CONTACTS</p>
            <div class = "Board">
                <a href = "https://instagram.com/lucks_022"><img src = "../Icon/instagram.png" id = "Exc"></a>
                <a href = "mailto:lukege287@gmail.com"><img src = "../Icon/Email.png"></a>
                <a href = "https://github.com/Lucksi"><img src = "../Icon/Git-hub.png"></a>
            </div>
        </div>
    </body>
</html>