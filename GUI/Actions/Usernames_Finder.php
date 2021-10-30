<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<?php 
    function Checker() {
        $File_name = $_POST["Searcher"];;
        if ($File_name == ""){
            echo "
            <script>
            alert('INSERT A USERNAME');
            </script>";
            }
            else {
                $Complete_name = "../Reports/Usernames/{$File_name}.txt";
                if(file_exists($Complete_name)){
                    echo "
                    <script>
                    alert('USERNAME FOUND');
                    </script>";
                    echo "\n\t<p id = 'Const'>USERNAME DATA</p>";
                    echo "\n\t<div class = 'Wrapper'>";
                    echo "\n\t\t<div class = 'Data'>";
                    $data = fopen($Complete_name,"r")or die("Server-Error");
                    echo "\n\t\t\t<p id = Const>REPORT:</p>\n";
                    while (!feof($data)){
                        $content = fgets($data);
                        echo "\t\t\t<p>".$content."</p>";
                    }
                    fclose($data);
                    echo "</p>";
                    echo "\n\t\t</div>";
                    $Complete_name = "../Reports/Usernames/Dorks/{$File_name}_Dorks.txt";
                    if(file_exists($Complete_name)){
                        echo "\n\t\t<div class = 'Data2'>";
                        $data = fopen($Complete_name,"r")or die("Server-Error");
                        echo "\n\t\t\t<p id = Const>DORKS-LIST:</p>\n";
                        while (!feof($data)){
                            $content = fgets($data);
                            echo "\t\t\t<p>".$content."</p>";
                        }
                        fclose($data);
                        echo "</p>";
                        echo "\n\t\t</div>";
                    }
                    else{

                    }
                    echo "\n\t\t<div class = 'Data_img'>";
                    $Dir_Name = "../Reports/Usernames/Profile_pics/{$File_name}/";
                    if(file_exists($Dir_Name)){
                        $image = glob($Dir_Name."*.jpg");
                        echo "\t\t\t<p id = 'Const2'>PROFILE-PICS:$File_Name</p>";
                        foreach($image as $Content) {
                            echo "\t\t\t<img src = '{$Content}' id = 'pics'>";
                            echo "<br>";
                        }
                    }
                    else{
                        echo "\n\t\t\t<p id = 'error'>NOT FIND ANY PROFILE PIC FOR THIS USER</p>";
                    }
                    echo "\n\t\t</div>";
                    echo "</div>";
                }
                else {
                    echo "
                    <script>
                    alert('OPS USERNAME NOT FOUND');
                    </script>";
                }
            }
        }
        if(isset($_POST["Button"])){
            Checker();
        }
        echo "\n";
    ?>