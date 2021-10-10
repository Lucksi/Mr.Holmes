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
            if ($color == "Light" or $color == "Dark" or $color == "High-Contrast"){
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
            </div>
            <div id = 'Ports'>
                <img src = '../Icon/Base/Ports.png'>
                <p id = 'Const'>Ports</p>
                <a href = 'Ports.php'><button>Search</button></a>
            </div>";
            }
            else {
                echo "
                <img src = '../Icon/$color/Username.png'onclick='Play()'>
                <p id = 'Const'>USERNAME</p>
                <a href = 'Username.php'><button>Search</button></a>
            </div>
            <div id = 'Website'>
                <img src = '../Icon/$color/Website.png'onclick='Play()'>
                <p id = 'Const'>WEBSITE</p>
                <a href = 'Websites.php'><button>Search</button></a>
            </div>
            <div id = 'Phone'>
                <img src = '../Icon/$color/Phone.png'onclick='Play()'>
                <p id = 'Const'>Phone</p>
                <a href = 'Phone.php'><button>Search</button></a>
            </div>
            <div id = 'Username'>
                <img src = '../Icon/$color/Ports.png'onclick='Play()'>
                <p id = 'Const'>Ports</p>
                <a href = 'Ports.php'><button>Search</button></a>
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
        </div>
        <div id = 'Ports'>
            <img src = '../Icon/Base/Ports.png'>
            <p id = 'Const'>Ports</p>
            <a href = 'Ports.php'><button>Search</button></a>
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
                echo "<img src = '../Icon/Uchiha/Logo.png'onclick='Play()'>";
            }
            else {
                echo "<img src = '../Icon/$color/Logo.png'>";
            }
        }
        else {
            echo "<img src = '../Icon/Base/Logo.png'>";
        }   
    }
   
?>
