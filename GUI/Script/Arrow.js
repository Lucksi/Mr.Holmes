/*AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0*/

function Active(){
    document.getElementById("Footer").style.display= "block";
    document.getElementById("Arrow").setAttribute("onClick", "javascript: Deactive();" );
} 

function Deactive(){
    document.getElementById("Footer").style.display= "none";
    document.getElementById("Arrow").setAttribute("onClick", "javascript: Active();" );
}
