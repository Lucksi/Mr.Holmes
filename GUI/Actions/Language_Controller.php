<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<?php
    function Get_Screen_size($Modality,$Lang){
        if ($Modality == "Login"){
            echo "<body onload = {$Lang}_{$Modality}()>";
        }
        else{
            echo "<script>
            if(screen.width > 711){
                document.write('<body onload = {$Lang}_{$Modality}()>');
            }
            else{
                document.write('<body onload = {$Lang}_{$Modality}_Mobile()>');
            }
            </script>";
        }
    }

    function Get_Language($Modality){
        $Language_file = "../Language/Language.json";
        if (file_exists($Language_file)){
            $reader = file_get_contents($Language_file);
            $Parser = json_decode($reader,true);
            $Language = $Parser["Language"]["Preference"];
            if ($Language == "Italian"){
                $Lang = "Italian";
                Get_Screen_size($Modality,$Lang);
            }
            elseif($Language == "English") {
                $Lang = "English";
                Get_Screen_size($Modality,$Lang);
            }
            elseif($Language == "Français") {
                $Lang = "French";
                Get_Screen_size($Modality,$Lang);
            }
            else{
                $Lang = "English";
                Get_Screen_size($Modality,$Lang);
                echo "
                <script>
                    alert('LANGUAGE NOT FOUND SET ENGLISH BY DEFAULT...');
                </script>";
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
