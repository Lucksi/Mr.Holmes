<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/ 
    
    $Input_username = $_POST["username"];
    $Input_Password = $_POST["password"];
    
    function Confront_Creds(){
        global $Input_username;
        global $Input_Password;
        $Flag = 0;
        $Login_file = "../Credentials/Users.json";
        $Reader = file_get_contents($Login_file);
        $Parser = json_decode($Reader,true);
        foreach($Parser["Users"] as $Data){
            if($Input_username == $Data["Username"] and $Input_Password == $Data["Password"]){
                $Flag = 1;
            }
        }
        if ($Flag == 1){
            $Session_File = "../Session/Token.txt";
            header("Location: ../Database/Main.php");
            $Creator = fopen($Session_File,"w")or die("SESSION-ERROR");
            fwrite($Creator,"LOG FOR YOUR CURRENT SESSION_THIS WILL EXPIRE ONCE YOU QUIT YOUR SESSION");
            fclose($Creator);
        }
        else {
            header("Location: ../Login/Login.php");
            echo "
            <script>
            alert('USERNAME OR PASSWORD INCORRECT');
            </script>";
        }
    }
    
    function Check_Creds(){
        global $Input_username;
        global $Input_Password;
        if ($Input_Password == "" and $Input_username == ""){
            header("Location: ../Login/Login.php");
            echo "
            <script>
            alert('USERNAME OR PASSWORD NOT INSERTED');
            </script>
            ";
        }
        else{
            Confront_Creds();
        }  
    }

    function Create_User(){
        global $Input_username;
        global $Input_Password;
        $Flag = 0;
        $Database = "../Credentials/Users.json";
        if(file_exists($Database)){
            $Reader = file_get_contents($Database);
            $Parser = json_decode($Reader,true);
            $Credentials = $Parser["Users"];
            if ($Input_Password == "" and $Input_username == ""){
                echo "
                <script>
                alert('USERNAME OR PASSWORD NOT INSERTED');
                </script>
                ";
            }
            else {
                foreach($Parser["Users"] as $Data){
                    if($Input_username == $Data["Username"]){
                        $Flag = 1;
                    }
                }
                if ($Flag == 1){
                    echo "<script>
                    alert('OPS USER $Input_username ALREADY EXIST');
                    </script>";
                }
                else {
                    echo "<script>
                    alert('USER $Input_username CREATED');
                    </script>";
                    $json_string = file_get_contents($Database);
                    $json = json_decode($json_string, true);
                    array_push($json["Users"], array("Username" => "$Input_username", "Password" => "$Input_Password"));
                    $strNew = json_encode($json,JSON_PRETTY_PRINT);
                    file_put_contents($Database, $strNew);
                }
            }
        }
        else {
            echo "<script>alert('ESSENTIAL FILE NOT FOUND EXIT')</script>";        
            exit(0);
        }
    }
    if(isset($_POST["Button2"])){
       Create_User();
    }
    elseif(isset($_POST["Button"])){
        Check_Creds();              
    } 
?>