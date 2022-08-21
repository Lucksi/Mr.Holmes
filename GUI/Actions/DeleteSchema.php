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

    function Delete(){
        $filename = $_POST["bar"];
        $filename2 = '" "';
        $final = str_replace(" ",$filename,$filename2);
        $path = "../Graphs/{$filename}/{$filename}.mh";
        $path2 = "../Graphs/{$filename}/encode.mh";
        if(file_exists($path)){
            $Message = Get_Message("Errors","Canc");
            unlink($path);
            unlink($path2);
            rmdir("../Graphs/{$filename}");
            echo "<script>
            alert('$Message');
            </script>";
        }    
        else{
            $Message = Get_Message("Errors","Graph");
            echo "
            <script>
            alert('$Message');
            </script>";
        }
    }
    if(isset($_POST["Button"])){
        Delete();
    }
?> 