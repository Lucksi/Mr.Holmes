<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<?php    
    function Body_Theme($File_Name){
        $mode_file = "../Theme/Mode.json";
        if (file_exists($mode_file)) {
            $reader = file_get_contents($mode_file);
            $parser = json_decode($reader,true); 
            $color = $parser["Color"]["Background"];
            $Style_name = "../Css/$color/$File_Name";
            if (file_exists($Style_name)) {
                echo '<link rel = "stylesheet" href ="'.$Style_name.'">';
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
            if ($color == "Kamui"){
                echo '
                <img src = "../Icon/Uchiha/Sharingan.png"onclick="Play()">
                <p id = "Const">USERNAME</p>
                <a href = "Username.php"><button>Search</button></a>
            </div>
            <div id = "Website">
                <img src = "../Icon/Uchiha/Website.png"onclick="Play()">
                <p id = "Const">WEBSITE</p>
                <a href = "Websites.php"><button>Search</button></a>
            </div>
            <div id = "Phone">
                <img src = "../Icon/Uchiha/Phone.png"onclick="Play()">
                <p id = "Const">Phone</p>
                <a href = "Phone.php"><button>Search</button></a>
            </div>';
            }
            else {
                echo "
                <img src = '../Icon/Base/social.png'>
                <p id = 'Const'>USERNAME</p>
                <a href = 'Username.php'><button>Search</button></a>
            </div>
            <div id = 'Website'>
                <img src = '../Icon/Base/browser.png'>
                <p id = 'Const'>WEBSITE</p>
                <a href = 'Websites.php'><button>Search</button></a>
            </div>
            <div id = 'Phone'>
                <img src = '../Icon/Base/phone.png'>
                <p id = 'Const'>Phone</p>
                <a href = 'Phone.php'><button>Search</button></a>
            </div>";
            }
        }
        else {
            echo "
            <img src = '../Icon/Base/social.png'>
            <p id = 'Const'>USERNAME</p>
            <a href = 'Username.php'><button>Search</button></a>
        </div>
        <div id = 'Website'>
            <img src = '../Icon/Base/browser.png'>
            <p id = 'Const'>WEBSITE</p>
            <a href = 'Websites.php'><button>Search</button></a>
        </div>
        <div id = 'Phone'>
            <img src = '../Icon/Base/phone.png'>
            <p id = 'Const'>Phone</p>
            <a href = 'Phone.php'><button>Search</button></a>
        </div>";
        }   
    }
    
    function Image(){
        $mode_file = "../Theme/Mode.json";
        if (file_exists($mode_file)) {
            $reader = file_get_contents($mode_file);
            $parser = json_decode($reader,true); 
            $color = $parser["Color"]["Background"];
            if ($color == "High-Contrast"){
                echo "<img src = '../Icon/High-Contrast/Mr.Holmes_Contrast.png'>\n";
            }
            elseif ($color == "Uchiha"){
                echo "<img src = '../Icon/Uchiha/Sharingan.png'onclick='Play()'>";
            }
            else {
                echo "<img src = '../Icon/Base/Mr.Holmes.png'>";
            }
        }
        else {
            echo "<img src = '../Icon/Mr.Holmes.png'>";
        }   
    }
   
?>
