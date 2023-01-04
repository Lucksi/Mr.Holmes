<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/ 
    
    function Active(){
        $Login_file = "Credentials/Login.json";
        if (file_exists($Login_file)){
            $reader = file_get_contents($Login_file);
            $Parser = json_decode($reader,true);
            $Status = $Parser["Database"]["Status"];
            if (($Status == "Active")){
                header("Location: ../Login/Login.php");
            }
            elseif(($Status == "Deactive")) {
                header("Location: ../Database/Main.php");
            }
        }
        else {
           echo "<script>
           alert('INTERNAL ERROR MISSING: Credentials/Login.json EXIT SESSION');
           </script>";
           exit(0);
        }
    }
    Active()
?>