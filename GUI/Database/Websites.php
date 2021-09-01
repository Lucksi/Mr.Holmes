<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<!DOCTYPE html>
<html>
    <head>
        <title>Websites</title>
        <?php
            $mode_file = "../Theme/Mode.json";
            if (file_exists($mode_file)){
                $reader = file_get_contents($mode_file);
                $parser = json_decode($reader,true); 
                $color = $parser["Color"]["Background"];
                $Style_name = "../Css/$color/Website.css";
                if (file_exists($Style_name)) {
                    echo '<link rel = "stylesheet" href ="'.$Style_name.'">';                
                }
                else {
                    echo "<script>
                    alert ('VALUE NOT VALID MODE DISPLAYED:LIGHT-MODE');
                    </script>";
                    echo '<link rel = "stylesheet" href = "../Css/Light/Website.css">';
                }
            }
            else {
                echo "<script>
                alert ('THEME FILE NOT FOUND MODE DISPLAYED:LIGHT-MODE');
                </script>";
                echo '<link rel = "stylesheet" href = "../Css/Light/Websites.css">';
            }
            echo "\n";
        ?>
        <link rel = "icon" href = "../Icon/Mr.Holmes.png">
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
        <meta charset ="UTF-8">
        <script src = "../../Script/Language.js"></script>
        <script src = "../../Script/Author.js"></script>
       
    </head>
    <body>
        <div class = "Top-bar">
            <p>MR.HOLMES</p>
            <div class = "languages">
                <button id = "Current">English</button>
                <div class = "Content">
                    <a onclick="Italian_Web()">Italiano</a>
                    <a onclick="English_Web()">English</a>
                </div>
            </div>
            <div class = "Link">
                <a href = "Username.php">Username</a>
                <a href = "Websites.php">Websites</a>
                <a href = "Phone.php">Phone-Numbers</a>
                <a  id = "change1" onclick= "English()">Author</a>
            </div>
        </div>
        <div class = "Upper-card">
            <?php include("../Actions/Theme_Controller.php");?>
            <center>
            <form action = "" method="POST">
            <input type= "text" placeholder = "Insert a Website..." id = "Searcher" name = "Searcher">
            <button  width="fit-content" id = "But" name = "Button">Search
            </center>
        </div>
    </form>
    <?php
    function Checker() {
        $File_name = $_POST["Searcher"];
        if ($File_name == ""){
            echo "
            <script>
            alert('INSERT A WEBSITE');
            </script>";
        }
        else {
            $Complete_name = "../Reports/Websites/{$File_name}.txt";
            if(file_exists($Complete_name)){
                echo "
                <script>
                alert('WEBSITE FOUND');
                </script>";
                echo "<p id = 'Const'>WEBSITE DATA</p>";
                echo "<div class = 'Data'>";
                echo "<p id = 'Const'>REPORT:</p>";
                $data = fopen($Complete_name,"r")or die("Server-Error");
                while (!feof($data)){
                    $content = fgets($data);
                    echo "<p>".$content;
                }
                fclose($data);
                echo "</p>";
                echo "\n</div>";
                echo "<div class = 'Geo'>";
                echo "<p id = 'Const'>IP-GEOLOCATION</p>";
                $Ip_File = "../Reports/Websites/Coordinates/Ip_Geolocation/{$File_name}.json";
                $reader = file_get_contents($Ip_File);
                $parser = json_decode($reader,true);
                $Latitude = $parser["Geolocation"]["Latitude"];
                $Longitude = $parser["Geolocation"]["Longitude"];
                echo "
                    <div class = 'map' id='map'></div>
                    <script>
                    var map = L.map('map').setView([$Latitude,$Longitude], 14);
                    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                        attribution: '&copy; <a href= https://www.openstreetmap.org/copyright >OpenStreetMap</a> contributors'
                    }).addTo(map);
        
                    L.marker([$Latitude,$Longitude]).addTo(map)
                        .bindPopup('Your Target is approximatley based in this Area.')
                        .openPopup();
                    
                    </script>
                   
                    ";
                $Street_File = "../Reports/Websites/Coordinates/Street_Geolocation/{$File_name}.json";
                echo "<p id = 'Const'>STREET-GEOLOCATION</p>";
                if(file_exists($Street_File)){
                    $reader = file_get_contents($Street_File);
                    $parser = json_decode($reader,true);
                    $Latitude = $parser["Geolocation"]["Latitude"];
                    $Longitude = $parser["Geolocation"]["Longitude"];
                    echo "
                        <div class = 'map' id='map2'></div>
                        <script>
                        var map2 = L.map('map2').setView([$Latitude,$Longitude], 14);
                        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                            attribution: '&copy; <a href= https://www.openstreetmap.org/copyright >OpenStreetMap</a> contributors'
                        }).addTo(map2);
            
                        L.marker([$Latitude,$Longitude]).addTo(map2)
                            .bindPopup('Your Target is approximatley based in this Area.')
                            .openPopup();
                        
                        </script>
                    
                        ";
                }
                else {
                    echo "<p>NOT FOUND ANY STREET INFO</p>";
                }
            }
            else {
                echo "
                <script>
                alert('OPS WEBSITE NOT FOUND');
                </script>";
            }
        }
    }
    if(isset($_POST["Button"])){
        Checker();
    }
    ?>
    
    <noscript>Please enable javascript</noscript>
    </body>
</html>