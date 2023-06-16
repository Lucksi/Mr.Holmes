<?php    
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
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
                <img class = 'Mod' src = '../Icon/Base/Graph.png'>
                <p id = 'Const'>Graph</p>
                <a href = 'Schema.php'><button class = But>Create</button></a>
            </div>
            <div id = 'Ports'>
                <img class = 'Mod' src = '../Icon/Base/Marker.png'>
                <p id = 'Const'>MAP</p>
                <a href = 'Map.php'><button class = But>Create</button></a>
            </div>
            <br>
            <br>
            <div id = 'Username'>
                <img class = 'Mod' src = '../Icon/Base/Author.png'>
                <p id = 'Const'>PEOPLE</p>
                <a href = 'People.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Website'>
                <img class = 'Mod' src = '../Icon/Base/Author.png'>
                <p id = 'Const'>AUTHOR</p>
                <a href = 'New_User.php'><button class = But>Show</button></a>
            </div>";
            }
            else {
                echo "
                <img class = 'Mod' src = '../Icon/$color/Username.png'>
                <p id = 'Const'>USERNAME</p>
                <a href = 'Username.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Website'>
                <img class = 'Mod' src = '../Icon/$color/Website.png'>
                <p id = 'Const'>WEBSITE</p>
                <a href = 'Websites.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Phone'>
                <img class = 'Mod' src = '../Icon/$color/Phone.png'>
                <p id = 'Const'>Phone</p>
                <a href = 'Phone.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Ports'>
                <img class = 'Mod' src = '../Icon/$color/Ports.png'>
                <p id = 'Const'>Ports</p>
                <a href = 'Ports.php'><button class = But>Search</button></a>
            </div>
            <br>
            <br>
            <div id = 'Username'>
                <img class = 'Mod'  src = '../Icon/$color/Email.png'>
                <p id = 'Const' id = But>Email</p>
                <a href = 'Email.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Website'>
                <img class = 'Mod' src = '../Icon/$color/User.png'>
                <p id = 'Const'>CREATE-USER</p>
                <a href = 'New_User.php'><button class = But>Create</button></a>
            </div>
            <div id = 'Phone'>
                <img class = 'Mod' src = '../Icon/$color/Graph.png'>
                <p id = 'Const'>Graph</p>
                <a href = 'Schema.php'><button class = But>Open</button></a>
            </div>
            <div id = 'Ports'>
                <img class = 'Mod' src = '../Icon/$color/Marker.png'>
                <p id = 'Const'>Map</p>
                <a href = 'Map.php' ><button class = But>Open</button></a>
            </div>
            <br>
            <br>
            <div id = 'Username'>
                <img class = 'Mod' src = '../Icon/$color/Author.png'>
                <p id = 'Const'></p>
                <a href = 'People.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Website'>
                <img class = 'Mod' src = '../Icon/$color/Author.png'>
                <p id = 'Const'>Author</p>
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
                <img class = 'Mod' src = '../Icon/Base/Ports.png'>
                <p id = 'Const'>Graph</p>
                <a href = 'Schema.php'><button class = But>Create</button></a>
            </div>
            <div id = 'Ports'>
                <img class = 'Mod' src = '../Icon/Base/Marker.png'>
                <p id = 'Const'>Map</p>
                <a href = 'Map.php'><button class = But>Create</button></a>
            </div>
            <br>
            <br>
            <div id = 'USERNAME'>
                <img class = 'Mod' src = '../Icon/Base/Author.png'>
                <p id = 'Const'>People</p>
                <a href = 'People.php'><button class = But>Search</button></a>
            </div>
            <div id = 'Website'>
                <img class = 'Mod' src = '../Icon/Base/Author.png'>
                <p id = 'Const'>Author</p>
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
            else {
                echo "<img id = 'Main_img' src = '../Icon/$color/Logo.png'>";
            }
        }
        else {
            echo "<img id = 'Main_img' src = '../Icon/Base/Logo.png'>";
        }   
    }

    function Image2(){
        $mode_file = "../Theme/Mode.json";
        if (file_exists($mode_file)) {
            $reader = file_get_contents($mode_file);
            $parser = json_decode($reader,true); 
            $color = $parser["Color"]["Background"];
            if ($color == "Light" or $color == "Dark" ){
                $Folder = "../Icon/Base/Companies/";
            }
            else {
                $Folder = "../Icon/High-Contrast/Companies/";
            }
        }
        else {
            $Folder = "../Icon/Base/Companies/";
        }
        $image = glob($Folder."*.png");
        echo "<center>
        <div class = 'part'>
        <p>PARTNERSHIPS</p>";
        foreach($image as $Content => $pic){
            $name = str_replace(".png","",$pic);
            $name2 = str_replace($Folder,"",$name);
            echo "<img src = '$pic' abbr title = '$name2'";
        }
        echo "</div></center>";   
    }
   
?>