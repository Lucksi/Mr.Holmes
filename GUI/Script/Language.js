/*AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0*/

/*LANGUAGES SCRIPT
  AVAIABLE:
  ITALIAN,
  ENGLISH*/

  function Italian_Username(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Autore");
    const user =("Inserisci un Username...");
    const search = ("Cerca");
    const error = ("NESSUNA FOTO PROFILO TROVATA PER QUESTO USER");
    const holder = ("Italiano");
    const photos = ("FOTO-PROFILO");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change1").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

function English_Username(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Author");
    const user =("Insert a Username...");
    const search = ("Search");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const holder = ("English");
    const photos = ("PROFILE-PICS");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change1").setAttribute( "onClick", "javascript: English();" );;
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

function Italian_Phone(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Autore");
    const user =("Inserisci un NumeroTelefonico...");
    const search = ("Cerca");
    const holder = ("Italiano");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change1").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Phone(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Author");
    const user =("Insert a PhoneNumber...");
    const search = ("Search");
    const holder = ("English");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change1").setAttribute( "onClick", "javascript: English();" );
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function Italian_Web(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Autore");
    const user =("Inserisci un Sito web...");
    const search = ("Cerca");
    const holder = ("Italiano");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change1").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Web(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Author");
    const user =("Insert a Website...");
    const search = ("Search");
    const holder = ("English");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change1").setAttribute( "onClick", "javascript: English();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}
