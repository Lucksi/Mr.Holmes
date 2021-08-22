<!DOCTYPE html>
<html>
    <head>
        <title>Websites</title>
        <link rel = "stylesheet" href = "../Css/Style.css">
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
            $Complete_name = "../../Reports/Websites/{$File_name}.txt";
            if(file_exists($Complete_name)){
                echo "
                <script>
                alert('WEBSITE FOUND');
                </script>";
                echo "<p id = 'Const'>WEBSITE DATA</p>";
                echo "<div class = 'Data'>";
                $data = fopen($Complete_name,"r")or die("Serbver");
                while (!feof($data)){
                    $content = fgets($data);
                    echo "<p>".$content;
                }
                fclose($data);
                echo "</p>";
                echo "\n</div>"; 
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