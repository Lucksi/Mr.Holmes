<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/ 

    function Get_Message($Type,$Param){
        require_once ("Language_Controller.php");
        $Message = Message($Type,$Param);
        return $Message;
    }

    function get_dorks($Complete_name){
        if(file_exists($Complete_name)){
            echo "<div class = 'Dataf'>";
            echo "<p id = 'Const'>DORKS:</p>";
            $data = fopen($Complete_name,"r")or die("Sever-Error");
            while (!feof($data)){
                $content = fgets($data);
                echo "<p>".$content;
            }
            fclose($data);
            echo "</p>";
            echo "\n</div>";     
        }
        else{
            echo "\n\t\t\t<p id align = 'center' = 'error'>NOT FIND ANY DORK FOR THIS NUMBER</p>";
        }
    }

    function Maps_Generator($File_name){
        echo "<br>";
        echo "<div class = 'Geo'>";
        echo "<p id = 'Const'>PHONE-GEOLOCATION</p>";
        $Area_File = "../Reports/Phone/{$File_name}/Area_GeoLocation.json";
        $Time_Zone_File = "../Reports/Phone/{$File_name}/Zone_GeoLocation.json";
        $reader = file_get_contents($Area_File);
        $parser = json_decode($reader,true);
        $Latitude = $parser["Geolocation"]["Latitude"];
        $Longitude = $parser["Geolocation"]["Longitude"];
        $reader2 = file_get_contents($Time_Zone_File);
        $parser2 = json_decode($reader2,true);
        $Latitude2 = $parser2["Geolocation"]["Latitude"];
        $Longitude2 = $parser2["Geolocation"]["Longitude"];
        $MarkLat ="";
        $MarkLon="";
        if (file_exists($Area_File)){
            $MarkLat = $Latitude;
            $MarkLon = $Longitude;
            $Area_Marker =  "var marker = new L.marker([$Latitude,$Longitude]).addTo(map)
            .bindPopup('Your Target Area approximatley based in this Area.')
            .openPopup();";
        }
        else{
            $Area_Marker = "";
        }
        if (file_exists($Time_Zone_File)){
            if ($MarkLat == "" &&  $MarkLon == ""){
                $MarkLat = $Latitude2;
                $MarkLon = $Longitude2;
            }
            $Area_Marker2 =  "var marker = new L.marker([$Latitude2,$Longitude2]).addTo(map)
            .bindPopup('Your Target Zone approximatley based in this Area.')
            .openPopup();";
        }
        else{
            $Area_Marker2 = "";
        }
        echo "
        <div class = 'map' id='map'></div>
        <script>
        var map = L.map('map').setView([$MarkLat,$MarkLon], 7);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href= https://www.openstreetmap.org/copyright >OpenStreetMap</a> contributors'
        }).addTo(map);
        $Area_Marker
        $Area_Marker2
        </script>";
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
            $image =  "../Icon/Entities/Phone.png";
            array_push($Image_arr,$image);
        }
        foreach($Name_arr as $Data  => $value){
                $link2 = $Data["name"];
                echo "<a href = '{$Name_arr[$Data]}' target = 'blank'>"."<img src = '{$Image_arr[$Data]}'abbr title = '{$Placeholder[$Data]}'></a>";                
            }
        echo "</div>";
    }
    
    function Checker() {
        $File_name = $_POST["Searcher"];
        if ($File_name == "") {
            $Message = Get_Message("NotEntered","Phone");
            echo "
            <script>
            alert('$Message');
            </script>";
        }
        else {
            $Complete_name = "../Reports/Phone/{$File_name}/{$File_name}.txt";
            $Complete_name2 = "../Reports/Phone/{$File_name}/{$File_name}.mh";
            if(file_exists($Complete_name)){
                $Message = Get_Message("Positives","Phone");
                echo "
                <script>
                alert('$Message');
                </script>";
                echo "<p id = 'Const'>NUMBER DATA</p>";
                echo "<div class = 'Datap'>";
                echo "<p id = 'Const'>REPORT:</p>";
                $data = fopen($Complete_name,"r")or die("Sever-Error");
                while (!feof($data)){
                    $content = fgets($data);
                    echo "<p>".$content;
                }
                fclose($data);
                echo "</p>";
                echo "\n</div>";
                Maps_Generator($File_name);
                echo "</div>";
                $Complete_name = "../Reports/Phone/Dorks/{$File_name}_dorks.txt";
                get_dorks($Complete_name);
                $Complete_name = "../Reports/Phone/{$File_name}/{$File_name}.txt";
                echo "<center>";
                Get_List($File_name,$Complete_name);
                echo "</center>";
            }
            else if (file_exists($Complete_name2)){
                require_once("Decode.php");
                $Message = Get_Message("Positives","Phone");
                echo "
                <script>
                alert('$Message');
                </script>";
                echo "<p id = 'Const'>NUMBER DATA</p>";
                echo "<div class = 'Datap'>";
                echo "<p id = 'Const'>REPORT:</p>";
                $data = fopen($Complete_name2,"r")or die("Sever-Error");
                while (!feof($data)){
                    $content = fgets($data);
                    $string = Decode($content);
                    echo "<pre><p>".$string."</p></pre>";
                }
                fclose($data);
                echo "</p>";
                echo "\n</div>";
                Maps_Generator($File_name);
                echo "</div>";
                $Complete_name = "../Reports/Phone/Dorks/{$File_name}_dorks.txt";
                get_dorks($Complete_name);
                $Complete_name = "../Reports/Phone/{$File_name}/{$File_name}.txt";
                echo "<center>";
                Get_List($File_name,$Complete_name);
                echo "</center>";
            }
            else {
                $Message = Get_Message("Errors","Phone");
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
