/*LANGUAGES SCRIPT
  AVAIABLE:
  ITALIAN,
  ENGLISH*/

  function Italian_Username(){
    const list = new Array ("Username", "Telefono", "Siti-Web");
    const user =("Inserisci un Username...");
    const search = ("Cerca");
    const holder = ("Italiano");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Username(){
    const list = new Array ("Username", "Phone-Numbers", "Websites");
    const user =("Insert a Username...");
    const search = ("Search");
    const holder = ("English");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function Italian_Phone(){
    const list = new Array ("Username", "Telefono", "Siti-Web");
    const user =("Inserisci un NumeroTelefonico...");
    const search = ("Cerca");
    const holder = ("Italiano");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Phone(){
    const list = new Array ("Username", "Phone-Numbers", "Websites");
    const user =("Insert a PhoneNumber...");
    const search = ("Search");
    const holder = ("English");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function Italian_Web(){
    const list = new Array ("Username", "Numeri di Telefono", "Siti-Web");
    const user =("Inserisci un Sito web...");
    const search = ("Cerca");
    const holder = ("Italiano");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Web(){
    const list = new Array ("Username", "Phone-Numbers", "Websites");
    const user =("Insert a Website...");
    const search = ("Search");
    const holder = ("English");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}