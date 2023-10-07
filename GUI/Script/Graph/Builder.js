/*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
AUTHOR: Luca Garofalo (Lucksi)
Copyright (C) 2022-2023 Lucksi <lukege287@gmail.com>
License: GNU General Public License v3.0*/


function CreateElement(){
    var name = document.getElementById("name").value;
    var url1= document.getElementById("Linkref").value;
    var comment = document.getElementById("writeText").value;
    if (name == ""){
        alert("Name not inserted");
    }
    else{
        if (comment == ""){
            var textbox = "";
        }
        else if(comment != ""){
            var textbox = "<textarea readonly class = 'commentBox' id = '" + name +" comment'>" +comment+"</textarea>";
        }
        if (document.getElementById("soc").checked == true){
            const image = "../Icon/Entities/Social.png";
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '<div id = "new">');
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            textbox);
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            "<p class = par id = '" + name + "text'>" + name + "</p>");
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            "<p><a href = " + url1 + " target = blank><img src = " + image + " width = 100px id = " + name + "></a></p>");
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '</div>');
            document.getElementById("add_after_me").setAttribute("id","Past");
            document.getElementById("new").setAttribute("id","add_after_me");
        }
        else if (document.getElementById("pe").checked == true){
            const image = "../Icon/Entities/Person.png";
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '<div id = "new">');
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            textbox);
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            "<p class = par id = '" + name + "text'>" + name + "</p>");
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            "<p><a href = " + url1 + " target = blank  id ='" + name + "link'" + "><img src = " + image + " width = 100px id = '" + name + "'></a></p>");
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '</div>');
            document.getElementById("add_after_me").setAttribute("id","Past");
            document.getElementById("new").setAttribute("id","add_after_me");
        }
        else if (document.getElementById("si").checked == true){
            const image = "../Icon/Entities/Web.png";
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '<div id = "new">');
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            textbox);
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            "<p class = par id = '" + name + "text'>" + name + "</p>");
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            "<p><a href = " + url1 + " target = blank  id ='" + name + "link'" + "><img src = " + image + " width = 100px id = '" + name + "'></a></p>");
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '</div>');
            document.getElementById("add_after_me").setAttribute("id","Past");
            document.getElementById("new").setAttribute("id","add_after_me");
        }
        else if (document.getElementById("nu").checked == true){
            const simbols = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
            if (simbols.test(name)){
                const image = "../Icon/Entities/Phone.png";
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                '<div id = "new">');
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                textbox);
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                "<p class = par id = '" + name + "text'>" + name + "</p>");
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                "<p><a href = " + url1 + " target = blank  id ='" + name + "link'" + "><img src = " + image + " width = 100px id = '" + name + "'></a></p>");
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                '</div>');
                document.getElementById("add_after_me").setAttribute("id","Past");
                document.getElementById("new").setAttribute("id","add_after_me");
            }
            else{
                alert("Phone Number Format Not Valid");
            }
        }
        else if (document.getElementById("mail").checked == true){
            const simbols = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}";
            if(name.match(simbols)){
                const image = "../Icon/Entities/Email.png";
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                '<div id = "new">');
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                textbox);
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                "<p class = par id = '" + name + "text'>" + name + "</p>");
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                "<p><a href = " + url1 + " target = blank  id ='" + name + "link'" + "><img src = " + image + " width = 100px id = '" + name + "'></a></p>");
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                '</div>');
                document.getElementById("add_after_me").setAttribute("id","Past");
                document.getElementById("new").setAttribute("id","add_after_me");
            }
            else{
                alert("Email Format Not Valid");
            }
            
        }
        else if (document.getElementById("img").checked == true){
            var user = document.getElementById("imageN").value;
            var Img = document.getElementById("imageL").value;
            var image = "";
            if (document.getElementById("YesLocal").checked == true){
                var Final = "";
                var Path = "";
                var Ok = "False";
                if (document.getElementById("Use").checked == true){
                    Path = "../Reports/Usernames/";
                    Ok = "True"
                }
                else if(document.getElementById("Per").checked == true){
                    Path = "../Reports/People/";
                    Ok = "True"
                    user = user.replace(" ","_");
                }
                if(Ok == "True"){
                    if(document.getElementById("YesPic").checked == true){
                        if (document.getElementById("Instagram").checked == true){
                            var path = "Profile_pics/Profile_pic_Instagram.jpg";
                        }
                        else if (document.getElementById("Twitter").checked == true){
                            var path = "Profile_pics/Profile_pic_Twitter.jpg ";
                        }
                        else if (document.getElementById("TikTok").checked == true){
                            var path = "Profile_pics/Profile_pic_TikTok.jpg ";
                        }
                        else if (document.getElementById("Docker").checked == true){
                            var path = "Profile_pics/Profile_pic_DockerHub.jpg ";
                        }
                        else if (document.getElementById("GitHub").checked == true){
                            var path = "Profile_pics/Profile_pic_GitHub.jpg ";
                        }
                        else if (document.getElementById("GitLab").checked == true){
                            var path = "Profile_pics/Profile_pic_GitLab.jpg ";
                        }
                        else if (document.getElementById("Disqus").checked == true){
                            var path = "Profile_pics/Profile_pic_Disqus.jpg ";
                        }
                        else if (document.getElementById("Imgur").checked == true){
                            var path = "Profile_pics/Profile_pic_Imgur.jpg ";
                        }
                        else if (document.getElementById("Wattpad").checked == true){
                            var path = "Profile_pics/Profile_pic_Wattpad.jpg ";
                        }
                        else if (document.getElementById("Kik").checked == true){
                            var path = "Profile_pics/Profile_pic_Kik.jpg ";
                        }
                        else if (document.getElementById("Ngl").checked == true){
                            var path = "Profile_pics/Profile_pic_Ngl.link.jpg ";
                        }
                        else if (document.getElementById("Tellonym").checked == true){
                            var path = "Profile_pics/Profile_pic_Tellonym.jpg";
                        }
                        else if (document.getElementById("Chess.com").checked == true){
                            var path = "Profile_pics/Profile_pic_Chess.com.jpg";
                        }
                        else if (document.getElementById("Gravatar").checked == true){
                            var path = "Profile_pics/Profile_pic_Gravatar.jpg";
                        }
                        Final = Path + user + "/" + path;
                        image = Final + " width = 150px style = 'border-radius:20px; margin-top:20px'";
                        url1 = Final;
                    }
                    else{
                        if (document.getElementById("Instagram").checked == true){
                            var path = "Profile_pics/Instagram_Posts";
                        }
                        else if (document.getElementById("Twitter").checked == true){
                            var path = "Profile_pics/Twitter_Posts";
                        }
                        else{
                            alert("Insert an Option");
                        }
                        Final = Path + user + "/" + path + "/"
                        image = Final + Img + " width = 150px style = 'border-radius:20px;margin-top:20px'";
                        url1 = Final + Img;
                    }
                }
                else{
                    alert("Missing Parameter");
                }
            }
            else if (document.getElementById("NoLocal").checked == true){
                if(Img != ""){
                    image = Img + "  width = 150px style = 'border-radius:20px;margin-top:20px'";
                    url1 = Img;
                }
                else{
                    image = "../Icon/Entities/Image.png  width = 100px";
                }
                Ok = "True"
            }
            if (Ok == "True"){
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                '<div id = "new">');
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                textbox);
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                "<p class = par id = '" + name + "text'>" + name + "</p>");
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                "<p><a href = " + url1 + " target = blank  id ='" + name + "link'" + "style = 'text-decoration:none;'><img id = '" + name +"_image' src = " + image + " ></a></p>");
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                '</div>');
                document.getElementById("add_after_me").setAttribute("id","Past");
                document.getElementById("new").setAttribute("id","add_after_me");
                var img3 = document.getElementById(name + "_image");
                img3.addEventListener('error',function handleError(){
                    img3.src = "../Icon/Entities/Image.png";
                    img3.style.width = "100px";
                    alert("Image not found replaced with Default image");
                });
            }
            else{
                alert("Error");
            }
        }
        else if (document.getElementById("lu").checked == true){
            var latidue = document.getElementById("Lat").value;
            var longitude = document.getElementById("Lon").value;
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '<div id = "new">');
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            textbox);
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            "<p class = par id = '" + name + "text'>" + name + "</p>");
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            "<div class = 'map' id= 'map" + name + "'></div>"+
            "<script type = text/javascript>"+ 
            "var map = L.map('map" + name + "').setView([" + latidue + "," + longitude + "],10);"+
            "L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',"+
            "{attribution: '&copy; <a href= https://www.openstreetmap.org/copyright >OpenStreetMap</a> contributors'}).addTo(map);"+
            
            "L.marker([" + latidue + "," + longitude + "]).addTo(map)."+
            "bindPopup('Location is approximatley based in this Area.')"+
            ".openPopup();</script>");
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '</div>');
            document.getElementById("add_after_me").setAttribute("id","Past");
            document.getElementById("new").setAttribute("id","add_after_me");
        }
        else if (document.getElementById("sep").checked == true){
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '<div id = "new">');
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            "<hr id = '" + name + "separator" + "' width = 700px style = 'margin-top:20px;'>");
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '</div>');
            document.getElementById("add_after_me").setAttribute("id","Past");
            document.getElementById("new").setAttribute("id","add_after_me");
        }
        else if (document.getElementById("Et").checked == true){
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '<div id = "new">');
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            "<p id = '" + name + "Label" + "' style = 'text-align:center;font-size:x-large;'>" + name + "</p>");
            document.getElementById("add_after_me").insertAdjacentHTML("afterend",
            '</div>');
            document.getElementById("add_after_me").setAttribute("id","Past");
            document.getElementById("new").setAttribute("id","add_after_me");
        }
        else if (document.getElementById("vid").checked == true){
            var UserVideo = document.getElementById("UsVid").value;
            var VideoName = document.getElementById("Vid").value;
            var Ok = "False";
            if (document.getElementById("Use2").checked == true){
                Path = "../Reports/Usernames/";
                Ok = "True"
            }
            else if(document.getElementById("Per2").checked == true){
                Path = "../Reports/People/";
                Ok = "True"
                UserVideo = UserVideo.replace(" ","_");
            }
            if(Ok == "True"){
                var Final2 = Path + UserVideo + "/" + "Profile_pics/TikTok_Posts/" + VideoName + ".mp4";
                var image1 = Path + UserVideo + "/" + "Profile_pics/TikTok_Posts/" + VideoName + "/" + VideoName + ".jpg";
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                '<div id = "new">');
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                textbox);
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                "<p class = par id = '" + name + "text'>" + name + "</p>");
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                "<p><a href = " + Final2 + " target = blank  id ='" + name + "video'" + "><video controls src ='" + Final2 +"' width = 10px height = 100px id ='" + name + "' poster = '" + image1 + "'></a></p>");
                document.getElementById("add_after_me").insertAdjacentHTML("afterend",
                '</div>');
                document.getElementById("add_after_me").setAttribute("id","Past");
                document.getElementById("new").setAttribute("id","add_after_me");
            }
            else{
                alert("Missing Parameter");
            }
        }
    }
}

function DeleteElement(){
    var name = document.getElementById("name").value;
    var rem = document.getElementById(name);
    var sec = document.getElementById(name + "text"); 
    var link = document.getElementById(name + "link");
    var text = document.getElementById(name + " comment");
    if (name == ""){
        alert("Name not inserted");
    }
    else{
        if(document.getElementById("sep").checked == true){
            var separ = document.getElementById(name + "separator");
            separ.remove()
        }
        else if(document.getElementById("Et").checked == true){
            var Label = document.getElementById(name + "Label");
            Label.remove()
        }
        else if(document.getElementById("vid").checked == true){
            var video = document.getElementById(name + "video");
            video.remove()
        }
        else if(document.getElementById("lu").checked == true){
            var map = document.getElementById("map" + name);
            map.remove()
        }
        else if(document.getElementById("img").checked == true){
            var map = document.getElementById(name + "_image");
            map.remove()
        }
        else{
            rem.remove();
        }
        sec.remove();
        text.remove();
        link.remove();
    }
}

function DeleteAll(Message){
    if(confirm(Message)){
        var content = document.getElementById("Content20");
        content.replaceChildren();
        content.innerHTML='<div id="add_after_me"></div>';
        alert("Content Resetted");
    }
    else{
        alert("Aborted");
    }
}

function SaveGraph(filename, Message){
    var filename2 = filename + ".mh";
    var text = document.getElementById("Content20").outerHTML;
    var crypt = false;
    var charset = "";
    if(confirm(Message)){
        crypt = true
        charset = "Encoded"; 
    }
    else{
        crypt = false ;
        charset = "NotEncoded";
    }
    var cryfile = new Blob([charset], {type: "text/plain"});
    var data = new FormData();
    data.append("upFile",cryfile);
    var req = new XMLHttpRequest();
    req.open("POST","../Actions/Upload_Fold.php");
    req.onload=function(){
        console.log(this.response);
    };
    req.send(data);
    if(crypt == true){
        var encode = window.btoa(text);
    }
    else if (crypt == false){
        var encode = text;
    }
    var file = new Blob([encode], {type: "text/plain"});
    var data = new FormData();
    data.append("upFile",file);
    var req = new XMLHttpRequest();
    req.open("POST","../Actions/Upload_File.php");
    req.onload=function(){
        console.log(this.response);
    };
    req.send(data);
    alert("Download Complete: " + filename2);
}
