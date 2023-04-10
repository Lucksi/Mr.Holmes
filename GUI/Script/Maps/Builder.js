/*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
AUTHOR: Luca Garofalo (Lucksi)
Copyright (C) 2023 Lucksi <lukege287@gmail.com>
License: GNU General Public License v3.0*/

var LocationList = [];

function CreateElement(){
    var comment = document.getElementById("writeText").value;
    var IsEntity = false;
    if(document.getElementById("pe").checked == true ){
        comment = "[Entity Used Person]:" + comment;
        IsEntity = true;
    }
    else if (document.getElementById("ev").checked == true){
        comment = "[Entity Used Event]:" + comment;
        IsEntity = true;
    }
    else if (document.getElementById("place").checked == true){
        comment = "[Entity Used Place]:" + comment;
        IsEntity = true;
    }
    else{
        IsEntity = false;
    }
    if (IsEntity == false){
        alert("Entity not selected");
    }
    else{
        var latidute = document.getElementById("Lat").value;
        var longitude = document.getElementById("Lon").value;
        L.marker([latidute ,longitude]).addTo(map).bindPopup(comment).openPopup().addEventListener("click",function(e){
        map.panTo([latidute,longitude])});
        var item = "L.marker([" + latidute + "," + longitude + "]).addTo(map).bindPopup('"+ comment + "').openPopup().addEventListener('click',function(e){map.panTo(["+ latidute +"," + longitude +"])})";
        LocationList.push(item);
    }     
}

function DeleteAll(Message){
    if(confirm(Message)){
        window.location.reload();
    }
    else{
        alert("Aborted");
    }
}

function SaveGraph(filename){
    var filename2 = filename + ".mh";
    var text = " <div id = 'Content20' class = >'<div class ='map' id='map'></div>"+
    "<script>"+
         "var map = L.map('map').setView([0.0,0.0], 3);"+
         "L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{ attribution: '&copy; <a href= https://www.openstreetmap.org/copyright >OpenStreetMap</a> contributors'}).addTo(map);" +
     "" + LocationList + "</script></div>";   
    var crypt = false;
    var charset = "";
    crypt = true
    charset = "Encoded"; 
    var cryfile = new Blob([charset], {type: "text/plain"});
    var data = new FormData();
    data.append("upFile",cryfile);
    var req = new XMLHttpRequest();
    req.open("POST","../Actions/Upload_MapFold.php");
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
    req.open("POST","../Actions/Upload_MapFile.php");
    req.onload=function(){
        console.log(this.response);
    };
    req.send(data);
    alert("Download Complete: " + filename2);
}