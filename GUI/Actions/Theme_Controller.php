<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<?php
    
    function Body_Theme($File_Name){
        $mode_file = "../Theme/Mode.json";
        if (file_exists($mode_file)) {
            $reader = file_get_contents($mode_file);
            $parser = json_decode($reader,true); 
            $color = $parser["Color"]["Background"];
            $Style_name = "../Css/$color/$File_Name";
            if (file_exists($Style_name)) {
                echo '<link rel = "stylesheet" href ="'.$Style_name.'">';                
            }
            else {
                echo "<script>
                alert ('VALUE NOT VALID MODE DISPLAYED:LIGHT-MODE');
                </script>";
                echo "<link rel = 'stylesheet' href = '../Css/Light/$File_Name'>";
            }
        }
        else {
            echo "<script>
            alert ('THEME FILE NOT FOUND MODE DISPLAYED:LIGHT-MODE');
            </script>";
            echo "<link rel = 'stylesheet' href = '../Css/Light/$File_Name'>";
        }
        echo "\n";
    }
    
    function Image(){
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
    }
   
?>