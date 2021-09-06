<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<?php
    $File_name = $_POST["Searcher"];
    
    function Maps_Generator(){
        global $File_name;
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
        </script>";
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
            </script>";
        }
        else {
             echo "<p>NOT FOUND ANY STREET INFO</p>";
        }
    }
    
    function Checker() {
        global $File_name;   
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
                Maps_Generator();
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