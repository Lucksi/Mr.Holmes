/*AUTHOR: Luca Garofalo (Lucksi)
Copyright (C) 2021-2022 Lucksi
License: GNU General Public License v3.0*/

/*SET LANGUAGE SECTION*/
function Set_Author_Lang(Auth){
    document.getElementById("change2").setAttribute("onClick",Auth);
}

function Set_Author_Lang_Mobile(Auth){
    document.getElementById("change1").setAttribute("onClick",Auth);
}

function Set_Language_Username(list,user,search,holder,error,photos,Auth){
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang(Auth);
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

function Set_Language_Username_Mobile(user,search,list,photos,error,Auth){
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.title=(list[0]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang_Mobile(Auth);
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

function Set_Language_Phone(list,user,search,holder,Auth){
    document.getElementById("Searcher").placeholder = user
    document.getElementById("But").innerHTML = (search);
    document.getElementById("Current").innerHTML = (holder);
    document.title = (list[2]);
    for (i = 0; i < list.length; i++) {
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML = (list[i]);
        i = i++;
    }
    Set_Author_Lang(Auth);
}

function Set_Language_Phone_Mobile(user,list,search,Auth){
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang_Mobile(Auth);
}

function Set_Language_Web(list,user,search,holder,Auth){
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang(Auth);
}

function Set_Language_Web_Mobile(list,user,search,Auth){
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang_Mobile(Auth);
}

function Set_Language_Main(list,search,holder,Auth,create,show){
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Cards")[0].getElementsByTagName("p")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<5;i++){
        document.getElementsByClassName("Cards")[0].getElementsByTagName("button")[i].innerHTML=(search);
        i=i++;
    }
    document.getElementsByClassName("Cards")[0].getElementsByTagName("button")[5].innerHTML=(create);
    document.getElementsByClassName("Cards")[0].getElementsByTagName("button")[6].innerHTML=(show);
    Set_Author_Lang(Auth);
}

function Set_Language_New_User(list,buttons,holder,Targ,Auth){
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
    
    document.getElementsByName("Create")[0].innerHTML=(Targ);
    Set_Author_Lang(Auth);
}

function Set_Language_Port(list,user,search,holder,Auth){
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[3]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang(Auth);
}

function Set_Language_Port_Mobile(list,user,search,Auth){
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.title=(list[3]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang_Mobile(Auth);
}

function Set_Language_New_User_Mobile(list,buttons,Targ,Auth){
    Set_Author_Lang_Mobile(Auth);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
    
    document.getElementsByName("Create")[0].innerHTML=(Targ);
}

function Set_Language_Email(list,user,search,holder,Auth){
    document.getElementById("Searcher").placeholder = user
    document.getElementById("But").innerHTML = (search);
    document.getElementById("Current").innerHTML = (holder);
    document.title = (list[2]);
    for (i = 0; i < list.length; i++) {
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML = (list[i]);
        i = i++;
    }
    Set_Author_Lang(Auth);
}

function Set_Language_Email_Mobile(list,user,search,Auth){
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.title=(list[2]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang_Mobile(Auth);
}

/*END SECTION*/

/*USERNAME*/

function Italian_Username(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const user =("Inserisci un Username...");
    const search = ("Cerca");
    const error = ("NESSUNA FOTO PROFILO TROVATA PER QUESTO USER");
    const holder = ("Italiano");
    const photos = ("FOTO-PROFILO");
    const Auth = ("javascript:Italiano();")
    Set_Language_Username(list,user,search,holder,error,photos,Auth);
}

function Italian_Username_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const user =("Inserisci un Username...");
    const search = ("Cerca");
    const error = ("NESSUNA FOTO PROFILO TROVATA PER QUESTO USER");
    const photos = ("FOTO-PROFILO");
    const Auth = ("javascript:Italiano();");
    Set_Language_Username_Mobile(user,search,list,photos,error,Auth);
}

/*PHONE*/

function Italian_Phone(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const user =("Inserisci un NumeroTelefonico...");
    const search = ("Cerca");
    const holder = ("Italiano");
    const Auth = ("javascript:Italiano();");
    Set_Language_Phone(list,user,search,holder,Auth);
}

function Italian_Phone_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const user =("Inserisci un NumeroTelefonico...");
    const search = ("Cerca");
    const Auth = ("javascript:Italiano();");
    Set_Language_Phone_Mobile(user,list,search,Auth);
}

/*WEB*/

function Italian_Web(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const user =("Inserisci un Sito web...");
    const search = ("Cerca");
    const holder = ("Italiano");
    const Auth = ("javascript:Italiano();");
    Set_Language_Web(list,user,search,holder,Auth);
}

function Italian_Web_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const user =("Inserisci un Sito web...");
    const search = ("Cerca");
    const Auth = ("javascript:Italiano();");
    Set_Language_Web_Mobile(list,user,search,Auth);
}

/*PORT*/

function Italian_Port(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const user =("Inserisci un Host...");
    const search = ("Cerca");
    const holder = ("Italiano");
    const Auth = ("javascript:Italiano();");
    Set_Language_Port(list,user,search,holder,Auth);
}

function Italian_Port_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const user =("Inserisci un Host...");
    const search = ("Cerca");
    const Auth = ("javascript:Italiano();")
    Set_Language_Port_Mobile(list,user,search,Auth);
}

/*MAIN*/

function Italian_Main(){
    const list = new Array ("Username","Siti-Web", "Telefono", "Porte","E-Mail", "Crea Utente","Autore")
    const search = ("Cerca");
    const create = ("Crea");
    const show = ("Mostra");
    const holder = ("Italiano");
    const Auth = ("javascript:Italiano();")
    Set_Language_Main(list,search,holder,Auth,create,show);
}

function Italian_Main_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    document.getElementById("change1").setAttribute( "onClick", "javascript: Italiano();" );
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

/*NEW USER*/

function Italian_User(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const buttons = new Array("Invio");
    const holder = ("Italiano");
    const Targ = ("CREA UTENTE");
    const Auth = ("javascript:Italiano();");
    Set_Language_New_User(list,buttons,holder,Targ,Auth);
}  

function Italian_User_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const buttons = new Array("Invio");
    const Targ = ("CREA UTENTE");
    const Auth = ("javascript:Italiano();");
    Set_Language_New_User_Mobile(list,buttons,Targ,Auth);
}

/*EMAIL*/

function Italian_Email(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const user =("Inserisci un E-Mail...");
    const search = ("Cerca");
    const holder = ("Italiano");
    const Auth = ("javascript:Italiano();");
    Set_Language_Email(list,user,search,holder,Auth);
}

function Italian_Email_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Autore");
    const user =("Inserisci un E-Mail...");
    const search = ("Cerca");
    const Auth = ("javascript:Italiano();");
    Set_Language_Email_Mobile(list,user,search,Auth);
}