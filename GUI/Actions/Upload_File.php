<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2022-2023 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/

    $filename = "../Graphs/Temp.txt";
    $reader = fopen("../Graphs/Temp.txt","r");
    $name = fgets($reader);
    fclose($reader);
    echo move_uploaded_file(
        $_FILES["upFile"]["tmp_name"],
        $name
    )? "OK":"ERROR";
?>