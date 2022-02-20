<?php
    /*AUTHOR: Luca Garofalo (Lucksi)
    Copyright 2021-2022 Lucksi
    License: GNU General Public License v3.0*/ 
    
    function Get_Dorks($Complete_name){
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
            echo "\n\t\t\t<p id = 'error' align = 'center'>NOT FIND ANY DORK FOR THIS USER</p>";
        }
    }

    function Get_Posts($File_name,$Folder_name,$Argument_Name){
        echo "<div class = 'Wrapper2'>";
        echo "\n\t\t<div class = 'Data_img2'>";
        echo "<p id = 'Const2'>$Argument_Name:</p>";
        $Dir_Name = "../Reports/Usernames/Profile_pics/{$File_name}/{$Folder_name}/";
        if(file_exists($Dir_Name)){
            $image = glob($Dir_Name."*.jpg");
            $details = glob($Dir_Name."*.txt");
            $i = 0;
            $j = 0;
            $count_P = 0;
            $count_D = 0;
            
            foreach($image as $Content){
                $i = $i +1;
            }

            foreach($details as $Datas){
                $j = $j +1;
            }
            
            echo "<a href = '../Reports/Usernames/Profile_pics/{$File_name}/_Profile_pic_Instagram.jpg' target = 'blank'><img src = '../Reports/Usernames/Profile_pics/{$File_name}/_Profile_pic_Instagram.jpg' id = 'Main_pics' abbr title = 'Instagram Profile_pic'></a>";
            for ($count_P = 1; $count_P<=$i; $count_P ++){
                $Content = "../Reports/Usernames/Profile_pics/{$File_name}/Instagram_Photo/Pic_$count_P.jpg";
                echo "\t\t\t<a href = '{$Content}'target = 'blank'><img src = '{$Content}' id = 'pics' abbr title = 'Post N°$count_P'></a>";
            }
            echo "</div>";
            echo "<div class = 'Data3'>";
            echo "<p id = 'Const2'>{$Argument_Name} DATAS:</p>";
            for ($count_D = 1; $count_D<=$j; $count_D ++){
                $Text = "../Reports/Usernames/Profile_pics/{$File_name}/Instagram_Photo/Post_{$count_D}_details.txt";
                $opener = fopen($Text,"r");
                while(!feof($opener)){
                    $reader = fgets($opener);
                    echo "<p>$reader</p>";
                }
                echo "<hr>";
            }
            echo "</div>";
        }
        
        else{
            echo "\n\t\t\t<p align = 'center' id = 'error'>NOT FIND ANY $Argument_Name FOR THIS USER</p>";
        }
        echo"</div>";
    }
    
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
                echo "\n\t\t<div class = 'Data_img'>";
                $Dir_Name = "../Reports/Usernames/Profile_pics/{$File_name}/";
                if(file_exists($Dir_Name)){
                     $image = glob($Dir_Name."*.jpg");
                    echo "\t\t\t<p id = 'Const2'>PROFILE-PICS:$File_name</p>";
                    foreach($image as $Content) {
                        echo "\t\t\t<a href = '{$Content}'target = 'blank'><img src = '{$Content}' id = 'pics' abbr title = '$Content'></a>";
                        echo "<br>";
                    }
                }
                else{
                    echo "\n\t\t\t<p id = 'error'>NOT FIND ANY PROFILE PIC FOR THIS USER</p>";
                }
                echo "\n\t\t</div>";
                echo "</div>";
                $Folder_name = "Instagram_Photo";
                $Argument_Name = "INSTAGRAM-POSTS";
                Get_Posts($File_name,$Folder_name,$Argument_Name);
                echo"</div>";
                $Complete_name = "../Reports/Usernames/Dorks/{$File_name}_Dorks.txt";
                Get_Dorks($Complete_name);
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
?>