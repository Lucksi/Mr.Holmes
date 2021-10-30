<?php
    function Get_Language($Modality){
        $Language_file = "../Language/Language.json";
        if (file_exists($Language_file)){
            $reader = file_get_contents($Language_file);
            $Parser = json_decode($reader,true);
            $Language = $Parser["Language"]["Preference"];
            if ($Language == "Italian"){
                if ($Modality == "Login"){
                    echo "<body onload = Italian_{$Modality}()>";
                }
                else{
                    echo "<script>
                    if(screen.width > 711){
                        document.write('<body onload = Italian_{$Modality}()>');
                    }
                    else{
                        document.write('<body onload = Italian_{$Modality}_Mobile()>');
                    }
                    </script>";
                }
            }
            elseif($Language == "English") {
                if ($Modality == "Login"){
                    echo "<body onload = English_{$Modality}()>";
                }
                else{
                    echo "<script>
                    if(screen.width > 711){
                        document.write('<body onload = English_{$Modality}()>');
                    }
                    else{
                        document.write('<body onload = English_{$Modality}_Mobile()>');
                    }
                    </script>";
                }
            }
            elseif($Language == "Français") {
                if ($Modality == "Login"){
                    echo "<body onload = French_{$Modality}()>";
                }
                else{
                    echo "<script>
                    if(screen.width > 711){
                        document.write('<body onload = French_{$Modality}()>');
                    }
                    else{
                        document.write('<body onload = French_{$Modality}_Mobile()>');
                    }
                    </script>";
                }
            }
            else{
                if ($Modality == "Login"){
                    echo "<body onload = English_{$Modality}()>";
                }
                else{
                    echo "<script>
                    if(screen.width > 711){
                        document.write('<body onload = English_{$Modality}()>');
                    }
                    else{
                        document.write('<body onload = English_{$Modality}_Mobile()>');
                    }
                    </script>";
                }
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