<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2022 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/ 
    
    $File_name = $_POST["Searcher"];

    function Get_Message($Type,$Param){
        require_once ("Language_Controller.php");
        $Message = Message($Type,$Param);
        return $Message;
    }

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

    function Get_List($File_name,$Complete_name){
        echo "<div class = 'Wrapper2'>";
        echo "\n\t\t<div class = 'Data_img3'>";
        echo "<p id = 'Const2'>ENTITIES:</p>";
        $Json_file = str_replace(".txt",".json",$Complete_name);
        $Json_file2 = str_replace("{$File_name}.json","Name.json",$Json_file);
        $Reader2 = file_get_contents($Json_file2);
        $Parser2 = json_decode($Reader2,true);
        $Reader = file_get_contents($Json_file);
        $Parser = json_decode($Reader,true);
        $Name_arr = array();
        $Image_arr = array();
        $Placeholder = array();
        foreach($Parser["List"] as $Data){
            $link = $Data["site"];
            array_push($Name_arr,$Data["site"]);
        }
        foreach($Parser2["Names"] as $Data){
            $link2 = $Data["name"];
            array_push($Placeholder,$link2);
            $image =  "../Icon/Entities/Web.png";
            array_push($Image_arr,$image);
        }
        foreach($Name_arr as $Data  => $value){
                $link2 = $Data["name"];
                echo "<a href = '{$Name_arr[$Data]}' target = 'blank'>"."<img src = '{$Image_arr[$Data]}'abbr title = '{$Placeholder[$Data]}'></a>";                
            }
        echo "</div>";
    }
    
    function Checker() {
        global $File_name;   
        if ($File_name == ""){
            $Message = Get_Message("NotEntered","Web");
            echo "
            <script>
            alert('$Message');
            </script>";
        }
        else {
            $Complete_name = "../Reports/Websites/{$File_name}/{$File_name}.txt";
            $Complete_name2 = "../Reports/Websites/{$File_name}/{$File_name}.mh";
            if(file_exists($Complete_name)){
                $Message = Get_Message("Positives","Web");
                echo "
                <script>
                alert('$Message');
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
                echo "</div>";
                echo "<center>";
                Get_List($File_name,$Complete_name);
                echo "</center>";
            }
            else if(file_exists($Complete_name2)){
                require_once("Decode.php");
                $Message = Get_Message("Positives","Web");
                echo "
                <script>
                alert('$Message');
                </script>";
                echo "<p id = 'Const'>WEBSITE DATA</p>";
                echo "<div class = 'Data'>";
                echo "<p id = 'Const'>REPORT:</p>";
                $data = fopen($Complete_name2,"r")or die("Server-Error");
                while (!feof($data)){
                    $content = fgets($data);
                    $string = Decode($content);
                    echo "<pre><p>".$string."</p></pre>";
                }
                fclose($data);
                echo "</p>";
                echo "\n</div>";
                Maps_Generator();
                echo "</div>";
                echo "<center>";
                Get_List($File_name,$Complete_name);
                echo "</center>";
            }
            else {
                $Message = Get_Message("NotEntered","Web");
                echo "
                <script>
                alert('$Message');
                </script>";
            }
        }
    }
    if(isset($_POST["Button"])){
        Checker();
    }
?>