<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<?php
    $Input_username = $_POST["username"];
    $Input_Password = $_POST["password"];
    
    function Confront_Creds(){
        global $Input_username;
        global $Input_Password;
        $Login_file = "../Credentials/Login.json";
        $Reader = file_get_contents($Login_file);
        $Parser = json_decode($Reader,true);
        $Username_1 = $Parser["Database"]["Username"];
        $Password_1 = $Parser["Database"]["Password"];
        $Session_File = "../Session/Token.txt";
        if ($Username_1 == $Input_username and $Password_1 == $Input_Password){
            header("Location: ../Database/Main.php");
            $Creator = fopen($Session_File,"w")or die("SESSION-ERROR");
            fwrite($Creator,"LOG FOR YOUR CURRENT SESSION_THIS WILL EXPIRE ONCE YOU QUIT YOUR SESSION");
            fclose($Creator);
        }
        else {
            echo "
            <script>
            alert('USERNAME OR PASSWORD INCORRECT');
            </script>";
        }
    }
    
    function Check_Creds() {
        global $Input_username;
        global $Input_Password;
        if ($Input_Password == "" and $Input_username == ""){
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
    if (isset($_POST["Button"])){
        Check_Creds();              
    } 
?>