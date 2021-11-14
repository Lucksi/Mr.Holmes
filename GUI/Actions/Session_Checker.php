<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0--> 
<?php
    function Moderate(){
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