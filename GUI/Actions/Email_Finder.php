<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2022 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/

    function Get_Message($Type,$Param){
        require_once ("Language_Controller.php");
        $Message = Message($Type,$Param);
        return $Message;
    }
    
    function get_dorks(){
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
        else {
            echo "\n\t\t\t<p id = 'error' align = 'center'>NOT FIND ANY DORK FOR THIS EMAIL</p>";
        }
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
            $Complete_name = "../Reports/E-Mail/{$File_name}.txt";
            if(file_exists($Complete_name)){
                $Message = Get_Message("Positives","Email");
                echo "
                <script>
                alert('$Message');
                </script>";
                echo "<p id = 'Const'>EMAIL DATA</p>";
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