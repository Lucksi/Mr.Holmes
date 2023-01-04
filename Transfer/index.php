<!--ORIGINAL CREATOR: Luca Garofalo (Lucksi)
AUTHOR: Luca Garofalo (Lucksi)
Copyright (C) 2023 Lucksi <lukege287@gmail.com>
License: GNU General Public License v3.0-->
<!DOCTYPE html>
    <html>
        <head>
            <?php
                function GetFile() {
                    $filename = fopen("file.txt","r") or die("Unable to open file");
                    $reader = fread($filename,filesize("file.txt"));
                    fclose($filename);
                    echo "<a href = '$reader' download><button id = 'clicker' onsuccess='alert(ciao);'>Download</button></a>";
                }
            ?>
            <script>
                function download(){
                    var a1 = document.getElementById("clicker");
                    a1.click();
                    alert("Download Completed");
                }
            </script>
            <style>
                #Download {
                    font-size: 15px;
                    font-weight:bold;
                    color: black;
                    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                    margin-top:100px;
                }

                #Main {
                    margin-top:none;
                    font-weight:bold;
                    color: black;
                    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                }
                button{
                    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                    font-size:18px;
                    background-color:blue;
                    color:white;
                    border:3px solid black;
                    border-radius:10px;
                }

                button:hover{
                    animation:click 2s infinite;
                }

                @keyframes click {
                    0%{background-color:blue;color:white;}
                    50%{background-color:rgb(0, 255, 98);color:black;}
                    100%{background-color:blue;color:white;}
                }
            </style>
            <meta charset ="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=0.9">
            <meta name="theme-color" content="#000000">
            <title>File-Transfer</title>
        </head>
        <body onload="download()">
            <p id = "Main">MR.HOLMES-FILE-TRANSFER</p>
            <center>
                <p id = "Download">IF THE DOWNLOAD WONT START AUTOMATICALLY PRESS THIS BUTTON</p>
                <?php 
                    GetFile();
                ?>
            </center>
        </body>
    </html>