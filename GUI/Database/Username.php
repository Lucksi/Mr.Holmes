<!DOCTYPE html>
<html>
    <head>
        <title>Username</title>
        <link rel = "stylesheet" href = "../Css/Username.css">
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
                    <a onclick="Italian_Username()">Italiano</a>
                    <a onclick="English_Username()">English</a>
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
                echo "<p id = 'Const'>USERNAME DATA</p>";
                echo "<div class = 'Wrapper'>";
                echo "<div class = 'Data'>";
                echo "<p>";
                $data = fopen($Complete_name,"r")or die("Server-Error");
                echo "<p id = 'Const'>REPORT:</p>";
                while (!feof($data)){
                    $content = fgets($data);
                    echo "<p>".$content;
                }
                fclose($data);
                echo "</p>";
                echo "\n</div>";
                echo "<div class = 'Data_img'>";
                $Dir_Name = "../Reports/Usernames/Profile_pics/{$File_name}/";
                if(file_exists($Dir_Name)){
                    $image = glob($Dir_Name."*.jpg");
                    echo "<p id = 'Const'>PROFILE-PICS:$File_Name</p>";
                    foreach($image as $Content) {
                        echo "<img src = '{$Content}' id = 'pics'>";
                        echo "<br>";
                    }
                }
                else{
                    echo "<p>NOT FIND ANY PROFILE PIC FOR THIS USER";
                }
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
    ?>
    <noscript>Please enable javascript</noscript>
    </body>
</html>