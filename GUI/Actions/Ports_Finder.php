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
    
    function Checker() {
        $File_name = $_POST["Searcher"];
        if ($File_name == "") {
            $Message = Get_Message("NotEntered","Host");
            echo "
            <script>
            alert('$Message');
            </script>";
        }
        else {
            $Complete_name = "../Reports/Ports/{$File_name}.txt";
            $Complete_name2 = "../Reports/Ports/{$File_name}.mh";
            if(file_exists($Complete_name)){
                $Message = Get_Message("Positives","Host");
                echo "
                <script>
                alert('$Message');
                </script>";
                echo "<p id = 'Const'>HOST-PORT DATA</p>";
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
            }
            else if(file_exists($Complete_name2)){
                require_once("Decode.php");
                $Message = Get_Message("Positives","Host");
                echo "
                <script>
                alert('$Message');
                </script>";
                echo "<p id = 'Const'>HOST-PORT DATA</p>";
                echo "<div class = 'Data'>";
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
            }
            else {
                $Message = Get_Message("Errors","Host");
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