<?php    
    /*AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2022 Lucksi
    License: GNU General Public License v3.0*/ 
    
    function Body_Theme($File_Name){
        $mode_file = "../Theme/Mode.json";
        if (file_exists($mode_file)) {
            $reader = file_get_contents($mode_file);
            $parser = json_decode($reader,true); 
            $color = $parser["Color"]["Background"];
            $Style_name = "../Css/$color/$File_Name";
            if (file_exists($Style_name)) {
                echo '<link rel = "stylesheet" id = "Theme" href ="'.$Style_name.'">';
                if ($color == "Uchiha"){
                    echo ' <script src = "../Script/Audio.js"></script>';
                }         
            }
            else {
                echo "<script>
                alert ('VALUE NOT VALID MODE DISPLAYED:LIGHT-MODE');
                </script>";
                echo "<link rel = 'stylesheet' href = '../Css/Light/$File_Name'>";
            }
        }   
        else {
            echo "<script>
            alert ('THEME FILE NOT FOUND MODE DISPLAYED:LIGHT-MODE');
            </script>";
            echo "<link rel = 'stylesheet' href = '../Css/Light/$File_Name'>";
        }
        echo "\n";
    }
    
    function Cards() {
        $mode_file = "../Theme/Mode.json";
        if (file_exists($mode_file)) {
            $reader = file_get_contents($mode_file);
            $parser = json_decode($reader,true); 
            $color = $parser["Color"]["Background"];
            if ($color == "Light" or $color == "Dark" or $color == "High-Contrast"){
                echo "
                <img class = 'Mod' src = '../Icon/Base/social.png'>
                <p id = 'Const'>USERNAME</p>
                <a href = 'Username.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Website'>
                <img class = 'Mod' src = '../Icon/Base/browser.png'>
                <p id = 'Const'>WEBSITE</p>
                <a href = 'Websites.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Phone'>
                <img class = 'Mod' src = '../Icon/Base/phone.png'>
                <p id = 'Const'>Phone</p>
                <a href = 'Phone.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Ports'>
                <img class = 'Mod' src = '../Icon/Base/Ports.png'>
                <p id = 'Const'>Ports</p>
                <a href = 'Ports.php'><button class = But>Search</button></a>
            </div>
            <br>
            <br>
            <div id = 'Username'>
                <img class = 'Mod'  src = '../Icon/Base/Email.png'>
                <p id = 'Const'>Email</p>
                <a href = 'Email.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Website'>
                <img class = 'Mod' src = '../Icon/Base/User.png'>
                <p id = 'Const'>CREATE-USER</p>
                <a href = 'New_User.php'><button class = But>Create</button></a>
            </div>
            <div id = 'Phone'>
                <img class = 'Mod' src = '../Icon/Base/Author.png'>
                <p id = 'Const'>AUTHOR</p>
                <a id = 'change2'><button class = But>Show</button></a>
            </div>";
            }
            else {
                echo "
                <img class = 'Mod' src = '../Icon/$color/Username.png'onclick='Play()'>
                <p id = 'Const'>USERNAME</p>
                <a href = 'Username.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Website'>
                <img class = 'Mod' src = '../Icon/$color/Website.png'onclick='Play()'>
                <p id = 'Const'>WEBSITE</p>
                <a href = 'Websites.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Phone'>
                <img class = 'Mod' src = '../Icon/$color/Phone.png'onclick='Play()'>
                <p id = 'Const'>Phone</p>
                <a href = 'Phone.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Ports'>
                <img class = 'Mod' src = '../Icon/$color/Ports.png'onclick='Play()'>
                <p id = 'Const'>Ports</p>
                <a href = 'Ports.php'><button class = But>Search</button></a>
            </div>
            <br>
            <br>
            <div id = 'Username'>
                <img class = 'Mod'  src = '../Icon/$color/Email.png'onclick='Play()'>
                <p id = 'Const' id = But>Email</p>
                <a href = 'Email.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Website'>
                <img class = 'Mod' src = '../Icon/$color/User.png'onclick='Play()'>
                <p id = 'Const'>CREATE-USER</p>
                <a href = 'New_User.php'><button class = But>Create</button></a>
            </div>
            <div id = 'Phone'>
                <img class = 'Mod' src = '../Icon/$color/Author.png'onclick='Play()'>
                <p id = 'Const'>AUTHOR</p>
                <a id = 'change2'><button class = But>Show</button></a>
            </div>";
            }
        }
        else {
            echo "
            <img class = 'Mod' src = '../Icon/Base/social.png'>
            <p id = 'Const'>USERNAME</p>
            <a href = 'Username.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Website'>
                <img class = 'Mod' src = '../Icon/Base/browser.png'>
                <p id = 'Const'>WEBSITE</p>
                <a href = 'Websites.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Phone'>
                <img class = 'Mod' src = '../Icon/Base/phone.png'>
                <p id = 'Const'>Phone</p>
                <a href = 'Phone.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Ports'>
                <img class = 'Mod' src = '../Icon/Base/Ports.png'>
                <p id = 'Const'>Ports</p>
                <a href = 'Ports.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Username'>
                <img class = 'Mod'  src = '../Icon/Base/Email.png'>
                <p id = 'Const' id = But>Email</p>
                <a href = 'Email.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Website'>
                <img class = 'Mod' src = '../Icon/Base/User.png'>
                <p id = 'Const'>CREATE-USER</p>
                <a href = 'New_User.php'><button class = But>Create</button></a>
            </div>
            <div id = 'Phone'>
                <img class = 'Mod' src = '../Icon/Base/Author.png'>
                <p id = 'Const'>AUTHOR</p>
                <a id = 'change2'><button class = But>Show</button></a>
            </div>";
        }   
    }
    
    function Image(){
        $mode_file = "../Theme/Mode.json";
        if (file_exists($mode_file)) {
            $reader = file_get_contents($mode_file);
            $parser = json_decode($reader,true); 
            $color = $parser["Color"]["Background"];
            if ($color == "Light" or $color == "Dark" ){
                echo "<img src = '../Icon/Base/Logo.png'>";
            }
            elseif ($color == "Uchiha"){
                echo "<img id = 'Main_img' src = '../Icon/Uchiha/Logo.png'onclick='Play()'>";
            }
            else {
                echo "<img id = 'Main_img' src = '../Icon/$color/Logo.png'>";
            }
        }
        else {
            echo "<img id = 'Main_img' src = '../Icon/Base/Logo.png'>";
        }   
    }
   
?>