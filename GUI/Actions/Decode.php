<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright 2022-2023 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/ 

    function Decode($content){
        $converted = base64_decode($content);
        $String = utf8_encode($converted);
        return $String;
    }
?>