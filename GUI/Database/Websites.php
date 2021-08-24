<!DOCTYPE html>
<html>
    <head>
        <title>Websites</title>
        <?php
            $mode_file = "../Theme/Mode.json";
            if (file_exists($mode_file)){
                $reader = file_get_contents($mode_file);
                $parser = json_decode($reader,true); 
                $color = $parser["Color"]["Background"];
                if ($color == "Light"){
                    echo '<link rel = "stylesheet" href = "../Css/Website.css">';
                }
                elseif ($color == "Dark"){
                    echo '<link rel = "stylesheet" href = "../Css/Dark_Website.css">';
                }
                else {
                    echo "<script>
                    alert ('VALUE NOT VALID MODE DISPLAYED:LIGHT-MODE');
                    </script>";
                    echo '<link rel = "stylesheet" href = "../Css/Website.css">';
                }
            }
            else {
                echo "<script>
                alert ('THEME FILE NOT FOUND MODE DISPLAYED:LIGHT-MODE');
                </script>";
                echo '<link rel = "stylesheet" href = "../Css/Websites.css">';
            }
        ?>
        <link rel = "icon" href = "../Icon/Mr.Holmes.png">
        <meta charset ="UTF-8">
        <script src = "../../Script/Language.js"></script>    
    </head>
    <body>
        <div class = "Top-bar">
            <p>MR.HOLMES</p>
            <div class = "languages">
                <button id = "Current">English</button>
                <div class = "Content">
                    <a onclick="Italian_Web()">Italiano</a>
                    <a onclick="English_Web()">English</a>
                </div>
            </div>
            <div class = "Link">
                <a href = "Username.php">Username</a>
                <a href = "Websites.php">Websites</a>
                <a href = "Phone.php">Phone-Numbers</a>
            </div>
        </div>
        <div class = "Upper-card">
            <img src = "../Icon/Mr.Holmes.png">
            <center>
            <form action = "" method="POST">
            <input type= "text" placeholder = "Insert a Website..." id = "Searcher" name = "Searcher">
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
            alert('INSERT A WEBSITE');
            </script>";
        }
        else {
            $Complete_name = "../Reports/Websites/{$File_name}.txt";
            if(file_exists($Complete_name)){
                echo "
                <script>
                alert('WEBSITE FOUND');
                </script>";
                echo "<p id = 'Const'>WEBSITE DATA</p>";
                echo "<div class = 'Data'>";
                echo "<p id = 'Const'>REPORT:</p>";
                $data = fopen($Complete_name,"r")or die("Server-Error");
                while (!feof($data)){
                    $content = fgets($data);
                    echo "<p>".$content;
                }
                fclose($data);
                echo "</p>";
                echo "\n</div>";
                $Dir_Name = "../Reports/Websites/Robots/{$File_name}_robots.txt";
                if(file_exists($Dir_Name)){
                    echo "<div class = 'Data_rob'>";
                    echo "<p id = 'Const'>ROBOTS.TXT:</p>";
                    $data = fopen($Dir_Name,"r")or die("Server-Error");
                    while (!feof($data)){
                        $content = fgets($data);
                        echo "<p>".$content;
                    }
                    fclose($data);
                    echo "</p>";
                    echo "\n</div>";
                }
                else{
                    echo "<p>NOT ROBOTS.TXT FILE</p>";
                }
                echo "</div>";
            }
            else {
                echo "
                <script>
                alert('OPS WEBSITE NOT FOUND');
                </script>";
            }
        }
    }
    if(isset($_POST["Button"])){
        Checker();
    }
    ?>
    <noscript>Please enable javascript</noscript>
    </body>
</html>