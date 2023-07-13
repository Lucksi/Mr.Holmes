<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/ 

    function Message($Type,$Param){
        $Language_file = "../Language/Language.json";
        $reader = file_get_contents($Language_file);
        $Parser = json_decode($reader,true);
        $Language = $Parser["Language"]["Preference"];
        $PoPups = "../Language/Messages.json";
        $reader = file_get_contents($PoPups);
        $decoder = json_decode($reader,true);
        if($Language == "Browser"){
            $Lang = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'],0,2);
            if($Lang == "it"){
                $Language = "Italian";
            }
            else if($Lang == "fr"){
                $Language = "French";
            }
            else{
                $Language = "English";
            }
        }
        $Message = $decoder["{$Type}"][0]["{$Language}"]["{$Param}"];
        return $Message;
    }

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
        if ($Modality == "Login" || $Modality == "SelectGrpah" || $Modality == "Graph"){
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
            if($Language == "Browser"){
                $Lang = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'],0,2);
                if($Lang == "it"){
                    Get_Screen_size($Modality,"Italian");
                }
                else if($Lang == "fr"){
                    Get_Screen_size($Modality,"French");
                }
                else{
                    Get_Screen_size($Modality,"English");
                }
                Get_Screen_size($Modality,$Lang);
            }
            else{
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
        }  
        else {
            echo "<script>
            alert('INTERNAL ERROR MISSING: Languages/Language.json EXIT SESSION');
            </script>";
            exit(0);
        }
        return $Language;
    }
?>
