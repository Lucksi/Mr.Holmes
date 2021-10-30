<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0--> 
<?php
    function Checker() {
        $File_name = $_POST["Searcher"];
        if ($File_name == "") {
            echo "
            <script>
            alert('INSERT A NUMBER');
            </script>";
        }
        else {
            $Complete_name = "../Reports/Phone/{$File_name}.txt";
            if(file_exists($Complete_name)){
                echo "
                <script>
                alert('NUMBER FOUND');
                </script>";
                echo "<p id = 'Const'>NUMBER DATA</p>";
                echo "<div class = 'Datap'>";
                echo "<p id = 'Const'>REPORT:</p>";
                $data = fopen($Complete_name,"r")or die("Sever-Error");
                while (!feof($data)){
                    $content = fgets($data);
                    echo "<p>".$content;
                }
                fclose($data);
                echo "</p>";
                echo "\n</div>";
                $Complete_name = "../Reports/Phone/Dorks/{$File_name}_dorks.txt";
                if(file_exists($Complete_name)){
                    echo "<div class = 'Dataf'>";
                    echo "<p id = 'Const'>DORKS:</p>";
                    $data = fopen($Complete_name,"r")or die("Sever-Error");
                    while (!feof($data)){
                        $content = fgets($data);
                        echo "<p>".$content;
                    }
                    fclose($data);
                    echo "</p>";
                    echo "\n</div>";     
                }
            }
            else {
                echo "
                <script>
                alert('OPS NUMBER NOT FOUND');
                </script>";
            }
        }
    }
    if(isset($_POST["Button"])){
        Checker();
    }
?>