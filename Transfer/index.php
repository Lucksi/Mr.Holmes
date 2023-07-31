<!--ORIGINAL CREATOR: Luca Garofalo (Lucksi)
AUTHOR: Luca Garofalo (Lucksi)
Copyright (C) 2023 Lucksi <lukege287@gmail.com>
License: GNU General Public License v3.0-->
<!DOCTYPE html>
    <html>
        <head>
            <link rel = "stylesheet" href = "Css/Main.css">
            <link rel = "icon" href = "Images/Download.png">
            <meta charset ="UTF-8">
            <script type = "text/javascript" src ="Scripts/Scripts.js"></script>
            <meta name="viewport" content="width=device-width, initial-scale=0.9">
            <meta name="theme-color" content="#000000">
            <title>File-Transfer</title>
            <?php
                function GetLogin(){
                    $filePassw = "Logpass.txt";
                    if(file_exists($filePassw)){
                        $opener = fopen("Logpass.txt","r") or die("Unable to open file");
                        $reader = fread($opener,filesize("Logpass.txt"));
                        fclose($opener);
                        echo "<form method = 'POST' id = 'pass'><input type = 'password' required placeholder = 'Insert the Passcode' name = 'code'><button  type = 'submit' name = 'sub'>Submit</button></form>";
                        if(isset($_POST["sub"])){
                            $codeinput = $_POST["code"];
                            $codeinput64 = base64_encode($codeinput);
                            if($codeinput64 == $reader){
                                echo "<script>alert('Passcode correct')</script>";
                                echo "<script>(function(){document.getElementById('pass').style.display='none';})();</script>";
                                Content();
                            }
                            else{
                                echo "<script>alert('Passcode incorrect')</script>";
                            }
                        }
                    }
                    else{
                        Content();
                    }
                }
                function Content(){
                    echo '
                    <p class = "Bolder" id = "Download"></p>
                    <p class = "Bolder"> IF THE DOWNLOAD WONT START AUTOMATICALLY PRESS THIS BUTTON</p>
                    <noscript><p class = "Bolder">LOOKS LIKE YOU HAVE JAVSCRIPT DISABLED PRESS THIS BUTTON FOR DOWNLOAD THE FILE</p></noscript>
                    ';
                    GetFile();
                }
                function GetFile() {
                    $filename = fopen("file.txt","r") or die("Unable to open file");
                    $reader = fread($filename,filesize("file.txt"));
                    fclose($filename);
                    echo "<a href = '$reader' download><button id = 'clicker'>Download</button></a>";
                }
            ?>
        </head>
        <body onload="Count()">
            <p id = "Main">MR.HOLMES FILE-TRANSFER</p>
            <center>
                <div class = "Content">
                    <img src = "Images/Download.png">
                    <?php
                        GetLogin();
                    ?>
                </div>
            </center>
        </body>
    </html>