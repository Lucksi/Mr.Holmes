<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2022-2023 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/

    function Get_Message($Type,$Param){
        require_once ("Language_Controller.php");
        $Message = Message($Type,$Param);
        return $Message;
    }

    function Toolbar($final,$Mess1,$Mess2){
        require("Builder.php");
        NewConstructor($final,$Mess1,$Mess2);
    }

    function filenae(){
        $filename = $_POST["bar1"];
        $filename2 = '" "';
        $final = str_replace(" ",$filename,$filename2);
        $path = "../Graphs/{$filename}/{$filename}.mh";
        $path2 = "../Graphs/{$filename}/encode.mh";
        if(file_exists($path)){
            $Message = Get_Message("Positives","Graph");
            echo "
            <script>
            alert('$Message');
            </script>";
        }    
        else{
            $Mess1 = Get_Message("Question","Graph");
            $Msg = '" "';
            $finalMsg = str_replace(" ",$Mess1,$Msg);
            $Mess2 = Get_Message("Question","Reset");
            $Msg2 = '" "';
            $finalMsg2 = str_replace(" ",$Mess2,$Msg2);
            mkdir("../Graphs/{$filename}",0777);
            chmod("../Graphs/{$filename}",0777);
            $tmp = "../Graphs/Temp.txt";
            $tmp2 = "../Graphs/TempEncode.txt";
            $d = fopen($tmp,"w");
            fwrite($d,$path);
            fclose($d);
            $d = fopen($tmp2,"w");
            fwrite($d,$path2);
            fclose($d);
            Toolbar($final,$finalMsg,$finalMsg2);
        }
    }
    if(isset($_POST["Button"])){
        filenae();
    }
?>