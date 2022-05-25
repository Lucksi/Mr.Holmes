<?php
    /*AUTHOR: Luca Garofalo (Lucksi)
    Copyright 2021-2022 Lucksi
    License: GNU General Public License v3.0*/ 
    
    function Get_Dorks($Complete_name){
        if(file_exists($Complete_name)){
            echo "\n\t\t<div class = 'Data2'>";
            $data = fopen($Complete_name,"r")or die("Server-Error");
            echo "\n\t\t\t<p id = Const>DORKS-LIST:</p>\n";
            while (!feof($data)){
                $content = fgets($data);
                echo "\t\t\t<p>".$content."</p>";
            }
            fclose($data);
            echo "</p>";
            echo "\n\t\t</div>";
        }
        else{
            echo "\n\t\t\t<p id = 'error' align = 'center'>NOT FIND ANY DORK FOR THIS USER</p>";
        }
    }

    function Get_List($File_name,$Complete_name){
        echo "<div class = 'Wrapper2'>";
        echo "\n\t\t<div class = 'Data_img3'>";
        echo "<p id = 'Const2'>SOCIALS:</p>";
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
            $Complete_image = "../Icon/Entities/Site_Icon/{$link2}.png";
            array_push($Placeholder,$link2);
            if(file_exists($Complete_image)){
                $image = $Complete_image;
            }
            else{
                $image =  "../Icon/Entities/Social.png";
            }
            array_push($Image_arr,$image);
            }
        foreach($Name_arr as $Data  => $value){
                $link2 = $Data["name"];
                echo "<a href = '{$Name_arr[$Data]}' target = 'blank'>"."<img src = '{$Image_arr[$Data]}'abbr title = '{$Placeholder[$Data]}'></a>";                
            }
        echo "</div>";
    }

    function Get_Posts($File_name,$Folder_name,$Argument_Name){
        echo "<center>";
        echo "<div class = 'Wrapper2'>";
        echo "\n\t\t<div class = 'Data_img2'>";
        echo "<p id = 'Const2'>$Argument_Name:</p>";
        $Dir_Name = "../Reports/Usernames/{$File_name}/Profile_pics/{$Folder_name}/";
        if(file_exists($Dir_Name)){
            $image = glob($Dir_Name."*.jpg");
            $details = glob($Dir_Name."*.txt");
            $geo = glob($Dir_Name."*.json");
            $fold = glob("$Dir_Name*" ,GLOB_ONLYDIR);
            $i = 0;
            $g = 0;
            $n = 1;
            $n1 = 1;
            $j = 0;
            
            $profile_pic = str_replace("_Posts","",$Folder_name);
            if(getimagesize("../Reports/Usernames/{$File_name}/Profile_pics/Profile_pic_$profile_pic.jpg") == false){
                            
            }
            else{
                /*echo "\t\t\t<a href = '{$profile_pic}' target = 'blank'><img src = '{$profile_pic}' id = 'pics' abbr title = '$profile_pic'></a>";
                echo "<br>";*/
                echo "<a href = '../Reports/Usernames/{$File_name}/Profile_pics/Profile_pic_$profile_pic.jpg' target = 'blank'><img src = '../Reports/Usernames/{$File_name}/Profile_pics/Profile_pic_{$profile_pic}.jpg' id = 'Main_pics' abbr title = '$profile_pic'></a>";
            }
            #echo "<a href = ../Reports/Usernames/{$File_name}/Profile_pics/Profile_pic_$profile_pic.jpg' target = 'blank'><img src = '../Reports/Usernames/{$File_name}/Profile_pics/Profile_pic_$profile_pic.jpg' id = 'Main_pics' abbr title = '$profile_pic'></a>";
            
            foreach(array_reverse($image) as $Content1){
                $i = $i +1;
                $img1 = $Content1;
                if (file_exists($img1)){
                    if(getimagesize($img1) == false){

                    }
                    else{
                        echo "\t\t\t<a href = '{$img1}'target = 'blank'>"."<img src = '{$img1}' id = 'pics' abbr title = 'Post N°$i'></a>";
                    }
                }
                else{
                    echo "none";
                }
            }
            echo "</div>";
            echo "<div class = 'Data3'>";
            echo "<p id = 'Const2'>{$Argument_Name} DATAS:</p>";
            
            foreach(array_reverse($fold) as $Content => $value){
                $b = 0;
                $data_file = glob("$value/*"."txt");
                if ($Folder_name == "Instagram_Posts"){
                    $cut_img = str_replace("$value/","",$data_file[$b]);
                    $img = str_replace(".txt",".jpg",$cut_img);
                    $Content = "../Reports/Usernames/{$File_name}/Profile_pics/$Folder_name/$img";
                    echo "<a href = '{$Content}' target = blank><img src = '{$Content}' id = 'pics' abbr title = 'Post N°$n1'></a>";
                }
                $opener = fopen($data_file[$j],"r") or die("$php_errormsg");
                while(!feof($opener)){
                    $reader = fgets($opener);
                    echo "<p>$reader</p>";
                }                
                echo "<hr>";
                $n1 = $n1 +1 ;
            }
            echo "</div>";
            if ($Folder_name == "Instagram_Posts"){
                echo "<div class = 'Data4'>";
                echo "<p id = 'Const2'>{$Argument_Name} GEOLOCATION:</p>";
                foreach(array_reverse($fold) as $Content => $value){
                    $b = 0;
                    $data_file = glob("$value/*"."json");
                    $format_name = str_replace("$Dir_Name","",$data_file);
                    $complete_name = str_replace(".json","",$format_name);
                    $cut_img = str_replace("$value/","",$data_file[$b]);
                    if(file_exists($data_file[$b])){
                        $img = str_replace(".json",".jpg",$cut_img);
                        $Content = "../Reports/Usernames/{$File_name}/Profile_pics/$Folder_name/$img";
                        echo "<a href = '{$Content}' target = blank><img src = '{$Content}' id = 'pics' abbr title = 'Post N°$n'></a>";
                        $reader = file_get_contents($data_file[$b]);
                        $parser = json_decode($reader,true);
                        $Latitude = $parser["Geolocation"]["Latitude"];
                        $Longitude = $parser["Geolocation"]["Longitude"];
                        echo "
                        <div class = 'map' id='map{$g}'></div>
                        <script>
                        var map = L.map('map{$g}').setView([$Latitude,$Longitude], 14);
                        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                        attribution: '&copy; <a href= https://www.openstreetmap.org/copyright >OpenStreetMap</a> contributors'
                        }).addTo(map);
    
                        L.marker([$Latitude,$Longitude]).addTo(map)
                        .bindPopup('Post°{$n} is approximatley based in this Area.')
                        .openPopup();
                        </script>";
                        echo "<hr>";
                        $g = $g +1;
                    }
                    else{

                    }
                    $n = $n + 1;
                }
            }
        } 
        else{
            echo "\n\t\t\t<p align = 'center' id = 'error'>NOT FIND ANY $Argument_Name FOR THIS USER</p>";
        }
        echo"</div>";
        echo "</center>";
    }
    
    function Checker() {
        $File_name = $_POST["Searcher"];;
        if ($File_name == ""){
            echo "
            <script>
            alert('INSERT A USERNAME');
            </script>";
        }
        else {
            $Complete_name = "../Reports/Usernames/{$File_name}/{$File_name}.txt";
            if(file_exists($Complete_name)){
                echo "
                <script>
                alert('USERNAME FOUND');
                </script>";
                echo "\n\t<p id = 'Const'>USERNAME DATA</p>";
                echo "\n\t<div class = 'Wrapper'>";
                echo "\n\t\t<div class = 'Data'>";
                $data = fopen($Complete_name,"r")or die("Server-Error");
                echo "\n\t\t\t<p id = Const>REPORT:</p>\n";
                while (!feof($data)){
                    $content = fgets($data);
                    echo "\t\t\t<p>".$content."</p>";
                }
                fclose($data);
                echo "</p>";
                echo "\n\t\t</div>";
                echo "\n\t\t<div class = 'Data_img'>";
                $Dir_Name = "../Reports/Usernames/{$File_name}/Profile_pics/";
                if(file_exists($Dir_Name)){
                    $image = glob($Dir_Name."*.jpg");
                    echo "\t\t\t<p id = 'Const2'>PROFILE-PICS:$File_name</p>";
                    foreach($image as $Content) {
                        $abbr_1 = str_replace("../Reports/Usernames/{$File_name}/Profile_pics/Profile_pic_","",$Content);
                        $abbr_2 = str_replace(".jpg","",$abbr_1);
                        if(getimagesize($Content) == false){
                            
                        }
                        else{
                            echo "\t\t\t<a href = '{$Content}'target = 'blank'><img src = '{$Content}' id = 'pics' abbr title = '$abbr_2'></a>";
                            echo "<br>";
                        }
                    }
                }
                else{
                    echo "\t\t\t<p id = 'Const2'>PROFILE-PICS:$File_name</p>";
                    echo "\n\t\t\t<p id = 'error'>NOT FIND ANY PROFILE PIC FOR THIS USER</p>";
                }
                echo "\n\t\t</div>";
                echo "</div>";
                $Folder_name = "Instagram_Posts";
                $Argument_Name = "INSTAGRAM-POSTS";
                echo "<center>";
                Get_List($File_name,$Complete_name);
                echo "</center>";
                Get_Posts($File_name,$Folder_name,$Argument_Name);
                echo"</div>";
                $Folder_name = "Twitter_Posts";
                $Argument_Name = "TWITTER-POSTS";
                Get_Posts($File_name,$Folder_name,$Argument_Name);
                echo"</div>";
                $Complete_name = "../Reports/Usernames/Dorks/{$File_name}_Dorks.txt";
                Get_Dorks($Complete_name);
            }
            else {
                echo "
                <script>
                alert('OPS USERNAME NOT FOUND');
                </script>";
            }
        }
    }
    
    if(isset($_POST["Button"])){
        Checker();
    }
?>
