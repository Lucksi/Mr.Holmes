<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/ 
    
    $File_name = $_POST["Searcher"];

    function Get_Message($Type,$Param){
        require_once ("Language_Controller.php");
        $Message = Message($Type,$Param);
        return $Message;
    }

    function Get_List($File_name,$Complete_name,$Name,$ImageName,$extension,$Arg){
        $Json_file = str_replace($extension,".json",$Complete_name);
        $Json_file2 = str_replace("{$File_name}.json",$Name,$Json_file);
        if(file_exists($Json_file2)){
            echo "<div class = 'Wrapper2'>";
            echo "\n\t\t<div class = 'Data_img3'>";
            echo "<p id = 'Const2'>$Arg :</p>";
            $Reader2 = file_get_contents($Json_file2);
            $Parser2 = json_decode($Reader2,true);
            foreach($Parser2["List"] as $Data){
                $user = $Data["username"];
                $link = $Data["site"];
                echo "<a href = '$link' target = blank><img src = '../Icon/Entities/Site_Icon/{$ImageName}' abbr title=$user></a>";
            }
            echo "</div>";
        }
        else{

        }
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
                echo "<center>";
                Get_List($File_name,$Complete_name,"Insta_Link.json","Instagram.png",".txt","DOMAIN RESULTS ON INSTAGRAM");
                Get_List($File_name,$Complete_name,"InstaName_Link.json","Instagram.png",".txt","NAME RESULTS ON INSTAGRAM");
                Get_List($File_name,$Complete_name,"Twitter_Link.json","Twitter.png",".txt","DOMAIN RESULTS ON TWITTER");
                Get_List($File_name,$Complete_name,"TwitterName_Link.json","Twitter.png",".txt","NAME RESULTS ON TWITTER");
                Get_List($File_name,$Complete_name,"TikTok_Link.json","TikTok.png",".txt","DOMAIN RESULTS ON TIKTOK");
                Get_List($File_name,$Complete_name,"TikTokName_Link.json","TikTok.png",".txt","NAME RESULTS ON TIKTOK");
                Get_List($File_name,$Complete_name,"Github_Link.json","GitHub.png",".txt","DOMAIN RESULTS ON GITHUB");
                Get_List($File_name,$Complete_name,"GithubName_Link.json","GitHub.png",".txt","NAME RESULTS ON GITHUB");
                echo "</center>";
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
                Get_List($File_name,$Complete_name2,"Insta_Link.json","Instagram.png",".mh","DOMAIN RESULTS ON INSTAGRAM");
                Get_List($File_name,$Complete_name2,"InstaName_Link.json","Instagram.png",".mh","NAME RESULTS ON INSTAGRAM");
                Get_List($File_name,$Complete_name2,"Twitter_Link.json","Twitter.png",".mh","DOMAIN RESULTS ON TWITTER");
                Get_List($File_name,$Complete_name2,"TwitterName_Link.json","Twitter.png",".mh","NAME RESULTS ON TWITTER");
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
