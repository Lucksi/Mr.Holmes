<!--AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0-->
<!DOCTYPE html>
<html> 
    <head>
        <title>Username</title>
        <?php
            $mode_file = "../Theme/Mode.json";
            if (file_exists($mode_file)){
                $reader = file_get_contents($mode_file);
                $parser = json_decode($reader,true); 
                $color = $parser["Color"]["Background"];
                $Style_name = "../Css/$color/Username.css";
                if (file_exists($Style_name)) {
                    echo '<link rel = "stylesheet" href ="'.$Style_name.'">';                
                }
                else {
                    echo "<script>
                    alert ('VALUE NOT VALID MODE DISPLAYED:LIGHT-MODE');
                    </script>";
                    echo '<link rel = "stylesheet" href = "../Css/Light/Username.css">';
                }
            }
            else {
                echo "<script>
                alert ('THEME FILE NOT FOUND MODE DISPLAYED:LIGHT-MODE');
                </script>";
                echo '<link rel = "stylesheet" href = "../Css/Light/Username.css">';
            }
            echo "\n";
        ?>
        <link rel = "icon" href = "../Icon/Mr.Holmes.png">
        <meta charset ="UTF-8">
        <script src = "../../Script/Language.js"></script>
        <script src = "../../Script/Author.js"></script>
    </head>
    <body>
        <div class = "Top-bar">
            <p>MR.HOLMES</p>
            <div class = "languages">
                <button id = "Current">English</button>
                <div class = "Content">
                    <a onclick="Italian_Username()">Italiano</a>
                    <a onclick="English_Username()">English</a>
                </div>
            </div>
            <div class = "Link">
                <a href = "Username.php">Username</a>
                <a href = "Websites.php">Websites</a>
                <a href = "Phone.php">Phone-Numbers</a>
                <a id = "change1" onclick= "English()">Author</a>
            </div>
        </div>
        <div class = "Upper-card">
            <?php include("../Actions/Theme_Controller.php");?>
            <center>
            <form action = "" method="POST">
            <input type= "text" placeholder = "Insert a Username..." id = "Searcher" name = "Searcher">
            <button  width="fit-content" id = "But" name = "Button">Search
            </center>
        </div>
    </form>
    <?php
        function Checker() {
            $File_name = $_POST["Searcher"];
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
                    echo "\n\t\t\t<p id = 'Const'>REPORT:</p>\n";
                    while (!feof($data)){
                        $content = fgets($data);
                        echo "\t\t\t<p>".$content;
                    }
                    fclose($data);
                    echo "</p>";
                    echo "\n\t\t</div>";
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
    </div>
        <noscript>Please enable javascript</noscript>
    </body>
</html>