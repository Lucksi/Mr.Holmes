<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2023 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/

    function Get_Message($Type,$Param){
        require_once ("Language_Controller.php");
        $Message = Message($Type,$Param);
        return $Message;
    }

    function Toolbar($final,$converted,$Mess1,$Mess2){
        require("Builder.php");
        OpenMapConstructor($final,$converted,$Mess1,$Mess2);
    }

    function Decode($content){
        $converted = base64_decode($content);
        $String = utf8_encode($converted);
        return $String;
    }

    function Open(){
        $filename = $_POST["bar"];
        $filename2 = '" "';
        $final = str_replace(" ",$filename,$filename2);
        $path = "../Maps/{$filename}/{$filename}.mh";
        $path2 = "../Maps/{$filename}/encode.mh";
        if(!file_exists($path)){
            $Message = Get_Message("Errors","Graph");
            echo "<script>
            alert('$Message');
            </script>";
        }
        else{
            $Message = Get_Message("Positives","Graph");
            echo "<script>
            alert('$Message');
            </script>";
            $content = file_get_contents($path);
            $reader2 = fopen($path2,"r")or die("2Error");
            $encode = file_get_contents($path2);
            if($encode == "Encoded"){
                $converted = Decode($content);
            }
            else if($encode == "NotEncoded"){
                $converted = $content;
            }
            else{
                echo "<script>alert('OPS Looks Like there is an invalid Encode Value exit)</script>";
                exit();
            }
            $tmp = "../Maps/Temp.txt";
            $tmp2 = "../Maps/TempEncode.txt";
            if(file_exists($tmp)){
                unlink($tmp);
            }
            if(file_exists($tmp2)){
                unlink($tmp2);
            }
            $Mess1 = Get_Message("Question","Graph");
            $Msg = '" "';
            $finalMsg = str_replace(" ",$Mess1,$Msg);
            $Mess2 = Get_Message("Question","Reset");
            $Msg2 = '" "';
            $finalMsg2 = str_replace(" ",$Mess2,$Msg2);
            $d = fopen($tmp,"w");
            fwrite($d,$path);
            fclose($d);
            $d = fopen($tmp2,"w");
            fwrite($d,$path2);
            fclose($d);
            Toolbar($final,$converted,$finalMsg,$finalMsg2);
        }    
    }
    if(isset($_POST["Button"])){
        Open();
    }
?>