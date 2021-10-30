/*AUTHOR: Lucksi
Copyright © 2021 Lucksi
License: GNU General Public License v3.0*/

/*LANGUAGES SCRIPT
  AVAIABLE:
  ITALIAN,
  ENGLISH,
  FRENCH*/

/*USERNAME*/
function Italian_Username(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "Crea Utente", "Autore");
    const user =("Inserisci un Username...");
    const search = ("Cerca");
    const error = ("NESSUNA FOTO PROFILO TROVATA PER QUESTO USER");
    const holder = ("Italiano");
    const photos = ("FOTO-PROFILO");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

function English_Username(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "Create User", "Author");
    const user =("Insert a Username...");
    const search = ("Search");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const holder = ("English");
    const photos = ("PROFILE-PICS");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: English();" );
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

function French_Username(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "Créér User", "Auteur");
    const user =("Entrer a Username...");
    const search = ("Rechercher");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const holder = ("Français");
    const photos = ("PHOTO-PROFIL");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: French();" );
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

function Italian_Username_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "Crea Utente", "Autore");
    const user =("Inserisci un Username...");
    const search = ("Cerca");
    const error = ("NESSUNA FOTO PROFILO TROVATA PER QUESTO USER");
    const photos = ("FOTO-PROFILO");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

function English_Username_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "Create User", "Author");
    const user =("Insert a Username...");
    const search = ("Search");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const photos = ("PROFILE-PICS");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: English();" );;
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

function French_Username_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "Créér User", "Auteur");
    const user =("Entrer a Username...");
    const search = ("Rechercher");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const photos = ("PHOTO-PROFIL");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: French();" );;
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

/*PHONE*/
function Italian_Phone(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "Crea Utente", "Autore");
    const user =("Inserisci un NumeroTelefonico...");
    const search = ("Cerca");
    const holder = ("Italiano");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Phone(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "Create User","Author");
    const user =("Insert a PhoneNumber...");
    const search = ("Search");
    const holder = ("English");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: English();" );
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function French_Phone(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "Créér User", "Auteur");
    const user =("Enterer a Telephoné...");
    const search = ("Rechercher");
    const holder = ("Français");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: French();" );
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function Italian_Phone_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "Crea Utente", "Autore");
    const user =("Inserisci un NumeroTelefonico...");
    const search = ("Cerca");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Phone_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "Create User", "Author");
    const user =("Insert a PhoneNumber...");
    const search = ("Search");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: English();" );
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function French_Phone_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "Créér User", "Auteur");
    const user =("Entrer a Telephoné...");
    const search = ("Rechercher");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: French();" );
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

/*WEB*/
function Italian_Web(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "Crea Utente", "Autore");
    const user =("Inserisci un Sito web...");
    const search = ("Cerca");
    const holder = ("Italiano");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Web(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "Create User", "Author");
    const user =("Insert a Website...");
    const search = ("Search");
    const holder = ("English");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: English();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function French_Web(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "Créér User", "Auteur");
    const user =("Entrer a site...");
    const search = ("Rechercher");
    const holder = ("Français");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: French();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function Italian_Web_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "Crea Utente", "Autore");
    const user =("Inserisci un Sito web...");
    const search = ("Cerca");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Web_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "Create User", "Author");
    const user =("Insert a Website...");
    const search = ("Search");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: English();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function French_Web_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "Créér User", "Auteur");
    const user =("Entrere a Site...");
    const search = ("Rechercher");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: French();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

/*PORT*/
function Italian_Port(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "Crea Utente", "Autore");
    const user =("Inserisci un Host...");
    const search = ("Cerca");
    const holder = ("Italiano");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Port(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "Create User", "Author");
    const user =("Insert a Host...");
    const search = ("Search");
    const holder = ("English");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: English();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function French_Port(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "Créér User", "Auteur");
    const user =("Entrere a Host...");
    const search = ("Rechercher");
    const holder = ("Français");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.getElementById("change2").setAttribute( "onClick", "javascript: French();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function Italian_Port_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "Crea Utente", "Autore");
    const user =("Inserisci un Host...");
    const search = ("Cerca");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Port_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "Create User", "Author");
    const user =("Insert a Host...");
    const search = ("Search");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: English();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function French_Port_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "Créér User", "Auteur");
    const user =("Entrere a Host...");
    const search = ("Rechercher");
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("change1").setAttribute( "onClick", "javascript: French();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

/*MAIN*/
function Italian_Main(){
    const list = new Array ("Username","Siti-Web", "Telefono", "Porte")
    const search = ("Cerca");
    const holder = ("Italiano");
    for (i=0;i<6;i++){
        document.getElementsByTagName("button")[i].innerHTML=(search);
        i=i++;
    }
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Cards")[0].getElementsByTagName("p")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Current").innerHTML=(holder);
}

function English_Main(){
    const list = new Array ("Username","Website", "Phone", "Port")
    const search = ("Search");
    const holder = ("English");
    for (i=0;i<6;i++){
        document.getElementsByTagName("button")[i].innerHTML=(search);
        i=i++;
    }
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Cards")[0].getElementsByTagName("p")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Current").innerHTML=(holder);
}

function French_Main(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes")
    const search = ("Rechercher");
    const holder = ("Français");
    for (i=0;i<6;i++){
        document.getElementsByTagName("button")[i].innerHTML=(search);
        i=i++;
    }
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Cards")[0].getElementsByTagName("p")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Current").innerHTML=(holder);
}

function Italian_Main_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "Crea Utente", "Autore");
    document.getElementById("change1").setAttribute( "onClick", "javascript: Italiano();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function English_Main_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "Create User", "Author");
    document.getElementById("change1").setAttribute( "onClick", "javascript: English();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

function French_Main_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "Créér User", "Auteur");
    document.getElementById("change1").setAttribute( "onClick", "javascript: French();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

/*LOGIN*/
function Italian_Login(){
    const buttons = new Array("Invio");
    const holder = ("Italiano");
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
}

function English_Login(){
    const buttons = new Array("Submit");
    const holder = ("English");
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
}

function French_Login(){
    const buttons = new Array("Envoi");
    const holder = ("Français");
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
}
/*NEW USER*/

function Italian_User(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "Crea Utente", "Autore");
    const buttons = new Array("Invio");
    const holder = ("Italiano");
    const Targ = ("CREA UTENTE");
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("change2").setAttribute( "onClick", "javascript: Italiano();" );
    document.getElementsByName("Create")[0].innerHTML=(Targ);
}

function English_User(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "Create User", "Author");
    const buttons = new Array("Submit");
    const holder = ("English");
    const Targ = ("CREATE USER")
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("change2").setAttribute( "onClick", "javascript: English();" );
    document.getElementsByName("Create")[0].innerHTML=(Targ);
}

function French_User(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "Créér User", "Auteur");
    const buttons = new Array("Envoi");
    const holder = ("Français");
    const Targ = ("Créér User")
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
    document.getElementById("change2").setAttribute( "onClick", "javascript: French();" );
    document.getElementsByName("Create")[0].innerHTML=(Targ)
}

function Italian_User_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "Crea Utente", "Autore");
    const buttons = new Array("Invio");
    const holder = ("Italiano");
    const Targ = ("CREA UTENTE");
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("change1").setAttribute( "onClick", "javascript: Italian();" );
    document.getElementsByName("Create")[0].innerHTML=(Targ)
}

function English_User_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "Create User", "Author");
    const buttons = new Array("Submit");
    const holder = ("English");
    const Targ = ("CREATE USER");
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("change1").setAttribute( "onClick", "javascript: English();" );
    document.getElementsByName("Create")[0].innerHTML=(Targ)
}

function French_User_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "Créér User", "Auteur");
    const buttons = new Array("Envoi");
    const holder = ("French");
    const Targ = ("Créér User");
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("change1").setAttribute( "onClick", "javascript: French();" );
    document.getElementsByName("Create")[0].innerHTML=(Targ)
}