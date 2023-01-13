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
            <style>
                .Bolder{
                    font-size: 15px;
                    font-weight:bold;
                    color: black;
                    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                    margin-top:30px
                }
                #Main {
                    margin-top:none;
                    font-weight:bold;
                    color: black;
                    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                    font-size:23px;
                    margin-top:-5px;
                    margin-left:-5px;
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
                .Content{
                    margin-top:100px;
                }
                img{
                    margin-top:-50px; 
                    height:80px;
                    width:80px;
                }
                @keyframes click {
                    0%{background-color:blue;color:white;}
                    50%{background-color:rgb(0, 255, 98);color:white;}
                    100%{background-color:blue;color:white;}
                }
            </style>
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