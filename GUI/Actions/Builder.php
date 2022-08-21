<?php
    /*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
    AUTHOR: Luca Garofalo (Lucksi)
    Copyright (C) 2022 Lucksi <lukege287@gmail.com>
    License: GNU General Public License v3.0*/

    function OpenConstructor($final,$converted,$Mess1,$Mess2){
        echo "<hr>";
        echo "<div class = 'Toolbar'>";
        echo '<div class = "Params">
                <div class = "options" id = "Opt">
                    <p class = "Etiquette" id = "typ">INSERT TYPE</p>
                    <input type = "radio" id = "img" value = "image" name = "1" onclick = "Image()">
                    <p id = "img2"></p>
                    <br>
                    <input type = "radio" id = "vid" value = "Video" name = "1" onclick = "Video()">
                    <label for = "Video" id = "vid2">Video</label>
                    <br>
                    <input type = "radio" id = "soc" value = "social" name = "1" onclick = "None()">
                    <label for = "social" id = "soc2">Social</label>
                    <br>
                    <input type = "radio" id = "si" value = "sito" name = "1" onclick = "None()">
                    <p id = "si2">Web</p>
                    <br>
                    <input type = "radio" id = "nu" value = "numero" name = "1" onclick = "None()">
                    <p id = "nu2"></p>
                    <br>
                    <input type = "radio" id = "mail" value = "email" name = "1" onclick = "None()">
                    <p id = "mail2">E-Mail</p>
                    <br>
                    <input type = "radio" id = "pe" value = "person" name = "1" onclick = "None()">
                    <p id = "pe2"></p>
                    <br>
                    <input type = "radio" id = "lu" value = "luogo" name = "1" onclick = "Map()">
                    <p id = "lu2"></p>
                    <br>
                    <input type = "radio" id = "sep" value = "sepa" name = "1" onclick = "None()">
                    <p id = "sepa2"></p>
                    <br>
                    <input type = "radio" id = "Et" value = "Etiq" name = "1" onclick = "None()">
                    <p id = "Et2"></p>
                    <br>
                    <hr>
                    <p id = "Option">OPTIONS</p>
                    <hr>
                        <div id = "data_img">
                            <p id = "imtool">IMAGE-TOOLBOX</p>
                            <br>
                            <input type = "radio" class = "imgavalue" id = "YesLocal" name = "2" value = "Local" onclick="OpenLocal()">
                            <label for = "Local">Local-Image</label>
                            <input type = "radio" class = "imgavalue" id = "NoLocal" name = "2" value = "NoLocal" onclick="CloseLocal()">
                            <label for = "NoLocal">Link-Image</label>
                            <br>
                            <div class = "LocalParameters" id = "LocalParams">
                                <br>
                                <input type = "radio" class = "imgavalue" id = "Instagram" name = "3" value = "Insta" onclick="OpenAdvance()">
                                <p for = "Instagram">Instagram</p>
                                <input type = "radio" class = "imgavalue" id = "Docker" name = "3" value = "Doc" onclick="OpenAdvance()">
                                <p for = "DockerHub">DockerHub</p>
                                <br>
                                <br>
                                <input type = "radio" class = "imgavalue" id = "TikTok" name = "3" value = "Tik" onclick="OpenAdvance()">
                                <p for = "TikTok">TikTok</p>
                                <input type = "radio" class = "imgavalue" id = "Twitter" name = "3" value = "Twitt" onclick="OpenAdvance()">
                                <p for = "Twitt">Twitter</p>
                                <br>
                                <br>
                                <input type = "radio" class = "imgavalue" id = "GitHub" name = "3" value = "Hub" onclick="OpenAdvance()">
                                <p for = "GitHub">GitHub</p>
                                <input type = "radio" class = "imgavalue" id = "GitLab" name = "3" value = "Lab" onclick="OpenAdvance()">
                                <p for = "GitLab">GitLab</p>
                                <br>
                                <br>
                                <input type = "radio" class = "imgavalue" id = "Disqus" name = "3" value = "Hub" onclick="OpenAdvance()">
                                <label for = "Disqus">Disqus</label>
                                <input type = "radio" class = "imgavalue" id = "Imgur" name = "3" value = "Lab" onclick="OpenAdvance()">
                                <p for = "Imgur">Imgur</p>
                                <br>
                                <br>
                                <input type = "radio" class = "imgavalue" id = "Wattpad" name = "3" value = "Watt" onclick="OpenAdvance()">
                                <p for = "Wattpad">Wattpad</p>
                                <input type = "radio" class = "imgavalue" id = "Kik" name = "3" value = "Kik" onclick="OpenAdvance()" style="margin-left:52px">
                                <p for = "Kik">Kik</p>
                                <br>
                                <br>
                                <input type = "radio" class = "imgavalue" id = "Ngl" name = "3" value = "Ngl" onclick="OpenAdvance()">
                                <p for = "Ngl">Ngl.link</p>
                                <br>
                                <div class = "Profile_Pics" id = "Profile_Pics">
                                    <br>
                                    <input type = "radio" class = "imgvalue" id = "YesPic" name = "4" value = "PicPro">
                                    <label for = "PicPro">Profile Pic</label>
                                    <input type = "radio" class = "imgvalue" id = "NoPic" name = "4" value = "PicPhot">
                                    <label for = "PicPhot">Post Pic</label>
                                </div>
                                <input type = "text" name = "bar3" id = "imageN" class = "bar" placeholder = "" autocomplete = "off">
                            </div>
                            <input type = "text" name = "bar3" id = "imageL" class = "bar" placeholder = "" autocomplete = "off">
                            <br>
                            <hr>
                        </div>
                        <div id = "data_place">
                            <p id = "pltool">PLACE-TOOLBOX</p>
                            <input type = "text" name = "bar3" id = "Lat" class = "bar"  placeholder = "" autocomplete = "off">
                            <br>
                            <input type = "text" name = "bar3" id = "Lon" class = "bar" placeholder = "" autocomplete = "off">
                            <br>
                            <hr>
                        </div>
                        <div id = "data_video">
                            <p id = "vtool">VIDEO-TOOLBOX</p>
                            <input type = "text" name = "bar3" id = "UsVid" class = "bar"  placeholder = "Insert User" autocomplete = "off">
                            <br>
                            <input type = "text" name = "bar3" id = "Vid" class = "bar" placeholder = "Insert Video Path" autocomplete = "off">
                            <br>
                            <hr>
                        </div>
                        <div class = "default">
                        <br>
                        <br>
                        <p id = "def">DEFAULT</p> 
                        <input type = "text" name = "bar3" id = "name" class = "bar" placeholder = "Insert Name" autocomplete = "off">
                        <br>
                        <input type = "text" name = "bar3" id = "Linkref" class = "bar" placeholder = "Insert Link" autocomplete = "off">
                        <br>
                        <textarea id = "writeText" placeholder = "Add a comment"></textarea>
                        <br>
                        <br>
                        <button  width="fit-content" id = "Button2" name = "create" onclick="CreateElement()">Open</button>
                        <button  width="fit-content" id = "Button2" name = "delete" onclick="DeleteElement()">Delete</button>';
                        echo "
                        <button  width='fit-content' id = 'Button2' name = 'deleteAll' onclick='DeleteAll($Mess2)'>Reset</button>'
                        <button  width='fit-content' id = 'Button2' name = 'save' onclick='SaveGraph($final,$Mess1)'>Save</button>         
                            <a id = 'link3'></a>
                        </div> 
                    </div>
                </div>
            </div>";
            echo "           $converted                
                    </div>";
            echo ' <a href = "#Opt" id = "Arrow2"></a>';

    }


    function NewConstructor($final,$Mess1,$Mess2){
        echo "<hr>";
        echo "<div class = 'Toolbar'>";
        echo '<div class = "Params">
                <div class = "options" id = "Opt">
                <p class = "Etiquette" id = "typ">INSERT TYPE</p>
                <input type = "radio" id = "img" value = "image" name = "1" onclick = "Image()">
                <p id = "img2"></p>
                <br>
                <input type = "radio" id = "vid" value = "Video" name = "1" onclick = "Video()">
                <label for = "Video" id = "vid2">Video</label>
                <br>
                <input type = "radio" id = "soc" value = "social" name = "1" onclick = "None()">
                <label for = "social" id = "soc2">Social</label>
                <br>
                <input type = "radio" id = "si" value = "sito" name = "1" onclick = "None()">
                <p id = "si2">Web</p>
                <br>
                <input type = "radio" id = "nu" value = "numero" name = "1" onclick = "None()">
                <p id = "nu2"></p>
                <br>
                <input type = "radio" id = "mail" value = "email" name = "1" onclick = "None()">
                <p id = "mail2">E-Mail</p>
                <br>
                <input type = "radio" id = "pe" value = "person" name = "1" onclick = "None()">
                <p id = "pe2"></p>
                <br>
                <input type = "radio" id = "lu" value = "luogo" name = "1" onclick = "Map()">
                <p id = "lu2"></p>
                <br>
                <input type = "radio" id = "sep" value = "sepa" name = "1" onclick = "None()">
                <p id = "sepa2"></p>
                <br>
                <input type = "radio" id = "Et" value = "Etiq" name = "1" onclick = "None()">
                <p id = "Et2"></p>
                <br>
                <hr>
                <p id = "Option">OPTIONS</p>
                <hr>
                    <div id = "data_img">
                        <p id = "imtool">IMAGE-TOOLBOX</p>
                        <br>
                        <input type = "radio" class = "imgavalue" id = "YesLocal" name = "2" value = "Local" onclick="OpenLocal()">
                        <label for = "Local">Local-Image</label>
                        <input type = "radio" class = "imgavalue" id = "NoLocal" name = "2" value = "NoLocal" onclick="CloseLocal()">
                        <label for = "NoLocal">Link-Image</label>
                        <br>
                        <div class = "LocalParameters" id = "LocalParams">
                            <br>
                            <input type = "radio" class = "imgavalue" id = "Instagram" name = "3" value = "Insta" onclick="OpenAdvance()">
                            <label for = "Instagram">Instagram</label>
                            <input type = "radio" class = "imgavalue" id = "Docker" name = "3" value = "Doc" onclick="OpenAdvance()"style="margin-left:28px">
                            <label for = "DockerHub">DockerHub</label>
                            <br>
                            <br>
                            <input type = "radio" class = "imgavalue" id = "TikTok" name = "3" value = "Tik" onclick="OpenAdvance()">
                            <label for = "TikTok">TikTok</label>
                            <input type = "radio" class = "imgavalue" id = "Twitter" name = "3" value = "Twitt" onclick="OpenAdvance()"style="margin-left:63px">
                            <label for = "Twitt">Twitter</label>
                            <br>
                            <br>
                            <input type = "radio" class = "imgavalue" id = "GitHub" name = "3" value = "Hub" onclick="OpenAdvance()">
                            <label for = "GitHub">GitHub</label>
                            <input type = "radio" class = "imgavalue" id = "GitLab" name = "3" value = "Lab" onclick="OpenAdvance()"style="margin-left:63px">
                            <label for = "GitLab">GitLab</label>
                            <br>
                            <br>
                            <input type = "radio" class = "imgavalue" id = "Disqus" name = "3" value = "Disq" onclick="OpenAdvance()">
                            <label for = "Disqus">Disqus</label>
                            <input type = "radio" class = "imgavalue" id = "Imgur" name = "3" value = "imgur" onclick="OpenAdvance()"style="margin-left:63px">
                            <label for = "Imgur">Imgur</label>
                            <br>
                            <br>
                            <input type = "radio" class = "imgavalue" id = "Wattpad" name = "3" value = "Watt" onclick="OpenAdvance()">
                            <label for = "Wattpad">Wattpad</label>
                            <input type = "radio" class = "imgavalue" id = "Kik" name = "3" value = "Kik" onclick="OpenAdvance()"style="margin-left:52px">
                            <label for = "Kik">Kik</label>
                            <br>
                            <br>
                            <input type = "radio" class = "imgavalue" id = "Ngl" name = "3" value = "Ngl" onclick="OpenAdvance()">
                            <p for = "Ngl">Ngl.link</p>
                            <br>
                            <div class = "Profile_Pics" id = "Profile_Pics">
                                <br>
                                <input type = "radio" class = "imgvalue" id = "YesPic" name = "4" value = "PicPro">
                                <label for = "PicPro">Profile Pic</label>
                                <input type = "radio" class = "imgvalue" id = "NoPic" name = "4" value = "PicPhot">
                                <label for = "PicPhot">Post Pic</label>
                            </div>
                            <input type = "text" name = "bar3" id = "imageN" class = "bar" placeholder = "" autocomplete = "off">
                        </div>
                        <input type = "text" name = "bar3" id = "imageL" class = "bar" placeholder = "" autocomplete = "off">
                        <br>
                        <hr>
                    </div>
                    <div id = "data_place">
                        <p id = "pltool">PLACE-TOOLBOX</p>
                        <input type = "text" name = "bar3" id = "Lat" class = "bar"  placeholder = "" autocomplete = "off">
                        <br>
                        <input type = "text" name = "bar3" id = "Lon" class = "bar" placeholder = "" autocomplete = "off">
                        <br>
                        <hr>
                    </div>
                    <div id = "data_video">
                        <p id = "vtool">VIDEO-TOOLBOX</p>
                        <input type = "text" name = "bar3" id = "UsVid" class = "bar"  placeholder = "Insert User" autocomplete = "off">
                        <br>
                        <input type = "text" name = "bar3" id = "Vid" class = "bar" placeholder = "Insert Video Path" autocomplete = "off">
                        <br>
                        <hr>
                    </div>
                    <div class = "default">
                    <br>
                    <br>
                    <p id = "def">DEFAULT</p> 
                    <input type = "text" name = "bar3" id = "name" class = "bar" placeholder = "Insert Name" autocomplete = "off">
                    <br>
                    <input type = "text" name = "bar3" id = "Linkref" class = "bar" placeholder = "Insert Link" autocomplete = "off">
                    <br>
                    <textarea id = "writeText" placeholder = "Add a comment"></textarea>
                    <br>
                    <br>
                    <button  width="fit-content" id = "Button2" name = "create" onclick="CreateElement()">Open</button>
                    <button  width="fit-content" id = "Button2" name = "delete" onclick="DeleteElement()">Delete</button>';
                    echo " <button  width='fit-content' id = 'Button2' name = 'deleteAll' onclick='DeleteAll($Mess2)'>Reset</button>
                    <button  width='fit-content' id = 'Button2' name = 'save' onclick='SaveGraph($final,$Mess1)'>Save</button>         
                        <a id = 'link3'></a>
                    </div> 
                </div>
            </div>
        </div>";
        echo '
        <div class = "Graph" id = "Content20">
                    <div id = "add_after_me"></div>                    
                </div>';
        echo ' <a href = "#Opt" id = "Arrow2"></a>';
    }
?>