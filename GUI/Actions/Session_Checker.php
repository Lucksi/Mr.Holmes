<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/ 
    
    function Moderate(){
        error_reporting(0);
        $Session_Token = "../Session/Token.txt";
        $Login_file = "../Credentials/Login.json";
        if(file_exists($Login_file)){    
            $reader = file_get_contents($Login_file);
            $Parser = json_decode($reader,true);
            $Status = $Parser["Database"]["Status"];
            if($Status == "Active"){   
                if(file_exists($Session_Token)){
                    header("Location: ");
                }
                else {
                    header("Location: ../Login/Login.php");
                }
            }
            else {
                header("Location: ");
            }
        }
        else {
            exit(0);
        }
    }
    Moderate();
?>
