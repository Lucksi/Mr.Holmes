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
                        Content();
                    ?>
                </div>
            </center>
        </body>
    </html>