<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<?php
    $mode_file = "../Theme/Mode.json";
    if (file_exists($mode_file)) {
        $reader = file_get_contents($mode_file);
        $parser = json_decode($reader,true); 
        $color = $parser["Color"]["Background"];
        if ($color == "High-Contrast"){
            echo "<img src = '../Icon/Mr.Holmes_Contrast.png'>";
        }
        else {
            echo "<img src = '../Icon/Mr.Holmes.png'>";
        }
    }
    else {
        echo "<img src = '../Icon/Mr.Holmes.png'>";
    }   
?>
