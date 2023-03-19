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
                    echo "<a href = '$reader' download><button id = 'clicker'>Download</button></a>";
                }
            ?>
            <script>
                function download(){
                    var text = document.getElementById("Download");
                    text.innerHTML="DOWNLOAD WILL START IN 0 SECONDS";
                    var clickerLink = document.getElementById("clicker");
                    clickerLink.click();
                }
                function Count(){
                    var text = document.getElementById("Download");
                    text.innerHTML="DOWNLOAD WILL START IN 5 SECONDS";
                    const myTimeout = setTimeout(download, 5000);
                }
            </script>
            <style>
                body{
                    background-color: #1a2b34;                
                }
                .Bolder{
                    font-size: 20px;
                    font-weight:bold;
                    color: white;
                    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                    margin-top:30px
                }
                #Main {
                    margin-top:none;
                    font-weight:bold;
                    color: white;
                    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                    font-size:23px;
                    margin-top:-5px;
                    margin-left:-5px;
                }
                button{
                    border: 3px solid black;
                    background-color: #ff4500;
                    height: 40px;
                    width: fit-content;
                    font-family: 'Courier New', Courier, monospace;
                    font-size: 20px;
                    font-weight: bold;
                    color: #f0f8ff;
                }
                button:hover{
                    animation:click 2s infinite;
                }
                .Content{
                    margin-top:100px;
                }
                img{
                    margin-top:-50px; 
                    height:80px;
                    width:80px;
                }
                @keyframes click {
                    0%{color: #f0f8ff; background-color: #ff4500;}
                    50%{color: #000000; background-color: #f0f8ff;}
                    100%{color: #f0f8ff; background-color: #ff4500;}
                }
            </style>
            <meta charset ="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=0.9">
            <meta name="theme-color" content="#000000">
            <title>File-Transfer</title>
        </head>
        <body onload="Count()">
            <p id = "Main">FILE-TRANSFER</p>
            <center>
                <div class = "Content">
                    <img src = "Images/Download.png">
                    <p class = "Bolder" id = "Download"></p>
                    <p class = "Bolder"> IF THE DOWNLOAD WONT START AUTOMATICALLY PRESS THIS BUTTON</p>
                    <noscript><p class = "Bolder">LOOKS LIKE YOU HAVE JAVSCRIPT DISABLED PRESS THIS BUTTON FOR DOWNLOAD THE FILE</p></noscript>
                    <?php 
                        GetFile();
                    ?>
                </div>
            </center>
        </body>
    </html>