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
            echo "<div class = 'Data2'>";
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
        else {
            echo "\n\t\t\t<p id = 'error' align = 'center'>NOT FIND ANY DORK FOR THIS EMAIL</p>";
        }
    }

    function Get_List($File_name,$Complete_name,$Name,$ImageName,$Site){
        $Json_file = str_replace(".txt",".json",$Complete_name);
        $Json_file2 = str_replace("{$File_name}.json",$Name,$Json_file);
        if(file_exists($Json_file2)){
            echo "<div class = 'Wrapper2'>";
            echo "\n\t\t<div class = 'Data_img3'>";
            echo "<p id = 'Const2'>{$Site}-RESULTS:</p>";
            $Reader2 = file_get_contents($Json_file2);
            $Parser2 = json_decode($Reader2,true);
            $Name_arr = array();
            foreach($Parser2["List"] as $Data){
                $user = $Data["username"];
                $link = $Data["site"];
                if(getimagesize("../Icon/Entities/Site_Icon/{$ImageName}") == false){  
                    echo "<a href = '$link' target = 'blank'><img src = '../Icon/Entities/Email.png' abbr title = '$user' id = 'noImage'></a>";
                }
                else{
                    echo "<a href = '$link' target = blank><img src = '../Icon/Entities/Site_Icon/{$ImageName}' abbr title=$user></a>";
                }
            }
        }
        echo "</div>";
    }
    
    function Checker() {
        $File_name = $_POST["Searcher"];
        if ($File_name == "") {
            $Message = Get_Message("NotEntered","Email");
            echo "
            <script>
            alert('$Message');
            </script>";
        }
        else {
            $Complete_name = "../Reports/E-Mail/{$File_name}/{$File_name}.txt";
            $Complete_name2 = "../Reports/E-Mail/{$File_name}/{$File_name}.mh";
            if(file_exists($Complete_name)){
                $Message = Get_Message("Positives","Email");
                echo "
                <script>
                alert('$Message');
                </script>";
                echo "<p id = 'Const'>EMAIL DATA</p>";
                echo "<div class = 'Data'>";
                echo "<p id = 'Const'>REPORT:</p>";
                $data = fopen($Complete_name,"r")or die("Sever-Error");
                while (!feof($data)){
                    $content = fgets($data);
                    echo "<p>".$content;
                }
                fclose($data);
                echo "</p>";
                echo "\n</div>";
                echo "<center>";
                Get_List($File_name,$Complete_name,"Github.json","GitHub.png","GITHUB");
                echo"<br><br><br>";
                Get_List($File_name,$Complete_name,"Gravatar.json","Gravatar.png","GRAVATAR");
                echo "</center>";
                $Complete_name = "../Reports/E-Mail/Dorks/{$File_name}_dorks.txt";
                get_dorks($Complete_name);
            }
            else if(file_exists($Complete_name2)){
                require_once("Decode.php");
                $Message = Get_Message("Positives","Email");
                echo "
                <script>
                alert('$Message');
                </script>";
                Get_List($File_name,$Complete_name,"Github.json","GitHub.png","GITHUB");
                echo"<br><br><br>";
                Get_List($File_name,$Complete_name,"Gravatar.json","Gravatar.png","GRAVATAR");
                echo "<p id = 'Const'>EMAIL DATA</p>";
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
                $Complete_name = "../Reports/E-Mail/Dorks/{$File_name}_dorks.txt";
                get_dorks($Complete_name);
            }
            else {
                $Message = Get_Message("Errors","Email");
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
