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

function French_Username(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const user =("Entrer a Username...");
    const search = ("Rechercher");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const holder = ("Français");
    const photos = ("PHOTO-PROFIL");
    const Auth = ("javascript:French();")
    Set_Language_Username(list,user,search,holder,error,photos,Auth);
}

function French_Username_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const user =("Entrer a Username...");
    const search = ("Rechercher");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const photos = ("PHOTO-PROFIL");
    const Auth = ("javascript:French();")
    Set_Language_Username_Mobile(user,search,list,photos,error,Auth);
}

/*PHONE*/

function French_Phone(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const user =("Enterer a Telephoné...");
    const search = ("Rechercher");
    const holder = ("Français");
    const Auth = ("javascript:French();");
    Set_Language_Phone(list,user,search,holder,Auth);
}

function French_Phone_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const user =("Entrer a Telephoné...");
    const search = ("Rechercher");
    const Auth = ("javascript:French();");
    Set_Language_Phone_Mobile(user,list,search,Auth);
}

/*WEB*/

function French_Web(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const user =("Entrer a site...");
    const search = ("Rechercher");
    const holder = ("Français");
    const Auth = ("javascript:French();");
    Set_Language_Web(list,user,search,holder,Auth);
}

function French_Web_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const user =("Entrere a Site...");
    const search = ("Rechercher");
    const Auth = ("javascript:French();");
    Set_Language_Web_Mobile(list,user,search,Auth);
}

/*PORT*/

function French_Port(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const user =("Entrere a Host...");
    const search = ("Rechercher");
    const holder = ("Français");
    const Auth = ("javascript:French();")
    Set_Language_Port(list,user,search,holder,Auth);
}

function French_Port_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const user =("Entrere a Host...");
    const search = ("Rechercher");
    const Auth = ("javascript:French();")
    Set_Language_Port_Mobile(list,user,search,Auth);
}

/*MAIN*/

function French_Main(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur")
    const search = ("Rechercher");
    const create = ("Creèr");
    const show = ("Montrer");
    const holder = ("Français");
    const Auth = ("javascript:French();")
    Set_Language_Main(list,search,holder,Auth,create,show);   
}

function French_Main_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    document.getElementById("change1").setAttribute( "onClick", "javascript: French();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

/*LOGIN*/

function French_Login(){
    const buttons = new Array("Envoi");
    const holder = ("Français");
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
}

/*NEW USER*/

function French_User(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const buttons = new Array("Envoi");
    const holder = ("Français");
    const Targ = ("CRÉÉR USER");
    const Auth = ("javascript:French();");
    Set_Language_New_User(list,buttons,holder,Targ,Auth);
}

function French_User_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const buttons = new Array("Envoi");
    const Targ = ("CRÉÉR USER");
    const Auth = ("javascript:French();");
    Set_Language_New_User_Mobile(list,buttons,Targ,Auth);
}

/*E-MAIL*/

function French_Email(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const user =("Enterer a E-Mail...");
    const search = ("Rechercher");
    const holder = ("Français");
    const Auth = ("javascript:French();");
    Set_Language_Email(list,user,search,holder,Auth);
}

function French_Email_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Auteur");
    const user =("Entrer a E-Mail...");
    const search = ("Rechercher");
    const Auth = ("javascript:French();");
    Set_Language_Email_Mobile(list,user,search,Auth);
}