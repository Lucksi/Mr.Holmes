<?php
    /*AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2022 Lucksi
    License: GNU General Public License v3.0*/ 

    function Total_Languages(){
        $Dir_Name = "../Script/Language/";
        $Files = glob($Dir_Name."*.js");
        foreach($Files as $Content){
            echo "\n\t\t<script src = '{$Content}'></script>";
        }
        echo "\n";
    }

    function List_Languages($Modality){
        $Dir_Name = "../Script/Language/";
        $Files = glob($Dir_Name."*.js");
        foreach($Files as $Content){
            $new = str_replace("../Script/Language/","",$Content);
            $name = str_replace(".js","",$new);
            if ($name == "Italian"){
                $finalname = "Italiano";
            }
            else if ($name == "French"){
                $finalname = "Français";
            }
            else{
                $finalname = $name;
            }
            $action = str_replace(".js",$Modality,$new);
            echo "<a onclick='{$action}'>$finalname</a>\n\t\t\t\t";
        }
        echo "\n";
    }
    
    function Get_Screen_size($Modality,$Lang){
        if ($Modality == "Login"){
            echo "<body onload = {$Lang}_{$Modality}()>\n";
        }
        else{
            echo "
            <script>
            if(screen.width > 711){
                document.write('<body onload = {$Lang}_{$Modality}()>');
            }
            else{
                document.write('<body onload = {$Lang}_{$Modality}_Mobile()>');
            }
            </script>\n";
        }
    }

    function Get_Language($Modality){
        $Language_file = "../Language/Language.json";
        if (file_exists($Language_file)){
            $reader = file_get_contents($Language_file);
            $Parser = json_decode($reader,true);
            $Language = $Parser["Language"]["Preference"];
            $LangFile = "../Script/Language/{$Language}.js";
            if (file_exists($LangFile)){
                $Lang = $Language;
                Get_Screen_size($Modality,$Lang);
            }
            else {
                $Lang = "English";
                Get_Screen_size($Modality,$Lang);
                echo "
                <script>
                    alert('LANGUAGE NOT FOUND SET ENGLISH BY DEFAULT...');
                </script>";
                echo "\n";
            }
        }  
        else {
            echo "<script>
            alert('INTERNAL ERROR MISSING: Languages/Language.json EXIT SESSION');
            </script>";
            exit(0);
        }
    }
?>