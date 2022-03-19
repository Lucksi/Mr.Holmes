<?php
    /*AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2022 Lucksi
    License: GNU General Public License v3.0*/ 

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

    function Get_List($File_name,$Complete_name){
        echo "<div class = 'Wrapper2'>";
        echo "\n\t\t<div class = 'Data_img3'>";
        echo "<p id = 'Const2'>ENTITIES:</p>";
        $Json_file = str_replace(".txt",".json",$Complete_name);
        $Reader = file_get_contents($Json_file);
        $Parser = json_decode($Reader,true);
        foreach($Parser["List"] as $Data){
            $link = $Data["site"];
            echo "<a href = '$link' target = 'blank'><img src = '../Icon/Entities/Phone.png'></a>";
        }
        echo "</div>";
    }
    
    function Checker() {
        $File_name = $_POST["Searcher"];
        if ($File_name == "") {
            echo "
            <script>
            alert('INSERT A NUMBER');
            </script>";
        }
        else {
            $Complete_name = "../Reports/Phone/{$File_name}.txt";
            if(file_exists($Complete_name)){
                echo "
                <script>
                alert('NUMBER FOUND');
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
                $Complete_name = "../Reports/Phone/Dorks/{$File_name}_dorks.txt";
                get_dorks($Complete_name);
                $Complete_name = "../Reports/Phone/{$File_name}.txt";
                echo "<center>";
                Get_List($File_name,$Complete_name);
                echo "</center>";
            }
            else {
                echo "
                <script>
                alert('OPS NUMBER NOT FOUND');
                </script>";
            }
        }
    }
    if(isset($_POST["Button"])){
        Checker();
    }
?>
