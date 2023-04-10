/*ORIGINAL CREATOR: Luca Garofalo (Lucksi)
AUTHOR: Luca Garofalo (Lucksi)
Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
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

function Set_Language_Main(list,search,holder,Auth,create,open,show){
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
    document.getElementsByClassName("Cards")[0].getElementsByTagName("button")[6].innerHTML=(open);
    document.getElementsByClassName("Cards")[0].getElementsByTagName("button")[7].innerHTML=(open);
    document.getElementsByClassName("Cards")[0].getElementsByTagName("button")[8].innerHTML=(search);
    document.getElementsByClassName("Cards")[0].getElementsByTagName("button")[9].innerHTML=(show);
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

function Set_Language_SelectGraph(list,holder,New,Old,Del,Auth){
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[6]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("New").innerHTML=(New);
    document.getElementById("Open").innerHTML=(Old);
    document.getElementById("Del").innerHTML=(Del);
    Set_Author_Lang(Auth);
}

function Set_Language_Graph(list,list2,user,search,holder,Auth,New,Old,Type,Img,Phone,Person,Place,Sepa,Etiq){
    document.getElementById("bar1").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Button").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[6]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("New").innerHTML=(New);
    document.getElementById("Open").innerHTML=(Old);
    document.getElementById("typ").innerHTML=(Type);
    document.getElementById("img").innerHTML=(Img);
    document.getElementById("nu").innerHTML=(Phone);
    document.getElementById("pe").innerHTML=(Person);
    document.getElementById("lu").innerHTML=(Place);
    document.getElementById("sep").innerHTML=(Sepa);
    document.getElementById("Et").innerHTML=(Etiq);
    document.getElementById("name").placeholder= list2[0];
    document.getElementById("Linkref").placeholder= list2[1];
    document.getElementById("writeText").placeholder=list2[2];
    document.getElementById("imageN").placeholder=list2[4];
    document.getElementById("imageL").placeholder=list2[3];
    Set_Author_Lang(Auth);
}

function Set_Language_People(list,user,search,holder,error,photos,Auth){
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[7]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang(Auth);
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

function Set_Language_People_Mobile(user,search,list,photos,error,Auth){
    document.getElementById("Searcher").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.title=(list[6]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang_Mobile(Auth);
    document.getElementById("Const2").innerHTML=(photos);
    document.getElementById("error").innerHTML=(error);
}

function Set_Language_SelectMap(list,holder,New,Old,Del,Auth){
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[8]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    document.getElementById("New").innerHTML=(New);
    document.getElementById("Open").innerHTML=(Old);
    document.getElementById("Del").innerHTML=(Del);
    Set_Author_Lang(Auth);
}

function Set_Language_Map(list,list2,user,search,holder,Auth,Type,Person,Place,Event,Create,DeleteAll,Save){
    document.getElementById("bar1").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[8]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang(Auth);
    document.getElementById("typ").innerHTML=(Type);
    document.getElementById("pe2").innerHTML=(Person);
    document.getElementById("lu2").innerHTML=(Place);
    document.getElementById("event2").innerHTML=(Event);
    document.getElementById("writeText").placeholder=list2[0];
    document.getElementById("Lon").placeholder=list2[1];
    document.getElementById("Lat").placeholder=list2[2];
    document.getElementsByName("save")[0].innerHTML=(Save);
    document.getElementsByName("create")[0].innerHTML=(Create);
    document.getElementsByName("deleteAll")[0].innerHTML=(DeleteAll);
}

/*END SECTION*/

/*USERNAME*/

function French_Username(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Personne", "Carte", "Auteur");
    const user =("Entrer a Username...");
    const search = ("Rechercher");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const holder = ("Français");
    const photos = ("PHOTO-PROFIL");
    const Auth = ("javascript:French();")
    Set_Language_Username(list,user,search,holder,error,photos,Auth);
}

function French_Username_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Personne", "Auteur");
    const user =("Entrer a Username...");
    const search = ("Rechercher");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const photos = ("PHOTO-PROFIL");
    const Auth = ("javascript:French();")
    Set_Language_Username_Mobile(user,search,list,photos,error,Auth);
}

/*PHONE*/

function French_Phone(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Personne", "Carte", "Auteur");
    const user =("Enterer a Telephoné...");
    const search = ("Rechercher");
    const holder = ("Français");
    const Auth = ("javascript:French();");
    Set_Language_Phone(list,user,search,holder,Auth);
}

function French_Phone_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Personne", "Auteur");
    const user =("Entrer a Telephoné...");
    const search = ("Rechercher");
    const Auth = ("javascript:French();");
    Set_Language_Phone_Mobile(user,list,search,Auth);
}

/*WEB*/

function French_Web(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Personne", "Carte", "Auteur");
    const user =("Entrer a site...");
    const search = ("Rechercher");
    const holder = ("Français");
    const Auth = ("javascript:French();");
    Set_Language_Web(list,user,search,holder,Auth);
}

function French_Web_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Personne", "Auteur");
    const user =("Entrere a Site...");
    const search = ("Rechercher");
    const Auth = ("javascript:French();");
    Set_Language_Web_Mobile(list,user,search,Auth);
}

/*PORT*/

function French_Port(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Personne", "Carte", "Auteur");
    const user =("Entrere a Host...");
    const search = ("Rechercher");
    const holder = ("Français");
    const Auth = ("javascript:French();")
    Set_Language_Port(list,user,search,holder,Auth);
}

function French_Port_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Personne", "Auteur");
    const user =("Entrere a Host...");
    const search = ("Rechercher");
    const Auth = ("javascript:French();")
    Set_Language_Port_Mobile(list,user,search,Auth);
}

/*MAIN*/

function French_Main(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Carte", "Personne", "Auteur")
    const search = ("Rechercher");
    const create = ("Creèr");
    const open = ("Ouvrez");
    const show = ("Montrer");
    const holder = ("Français");
    const Auth = ("javascript:French();")
    Set_Language_Main(list,search,holder,Auth,create,open,show);   
}

function French_Main_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Personne", "Auteur");
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
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Personne", "Carte", "Auteur");
    const buttons = new Array("Envoi");
    const holder = ("Français");
    const Targ = ("CRÉÉR USER");
    const Auth = ("javascript:French();");
    Set_Language_New_User(list,buttons,holder,Targ,Auth);
}

function French_User_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Personne", "Auteur");
    const buttons = new Array("Envoi");
    const Targ = ("CRÉÉR USER");
    const Auth = ("javascript:French();");
    Set_Language_New_User_Mobile(list,buttons,Targ,Auth);
}

/*E-MAIL*/

function French_Email(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Personne", "Carte", "Auteur");
    const user =("Enterer a E-Mail...");
    const search = ("Rechercher");
    const holder = ("Français");
    const Auth = ("javascript:French();");
    Set_Language_Email(list,user,search,holder,Auth);
}

function French_Email_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User" ,"Personne", "Auteur");
    const user =("Entrer a E-Mail...");
    const search = ("Rechercher");
    const Auth = ("javascript:French();");
    Set_Language_Email_Mobile(list,user,search,Auth);
}

function French_SelectGraph(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Personne", "Carte", "Auteur");
    const Auth = ("javascript:French();");
    const New = ("Nouveau Graph");
    const Old = (" Ouvertz Graph");
    const Del = ("Supprimer Graph");
    const holder = ("Français");
    Set_Language_SelectGraph(list,holder,New,Old,Del,Auth);

}

function French_Graph(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Personne", "Carte", "Auteur");
    const list2 = new Array("Entrez le Nome", "Entrez le Link", "Entre un comment", "Entrez le path de l'immagine", "Entrez an User", "Entrez Video Path", "Entrez Latitude", "Entrez Longitude")
    const user =("Entrez une File...");
    const search = ("Entrer");
    const Auth = ("javascript:French();");
    const Type = ("Entrez le Tipologie");
    const Img = ("Image");
    const Phone = ("Telephone");
    const Person = ("Personne");
    const Place = ("Lieu");
    const Sepa = ("Séparateur");
    const Etiq = ("Étiquette");
    const Create = ("Creer");
    const Delete = ("Sopprimer");
    const DeleteAll = ("Reset");
    const Save = ("Sauver");
    const holder = ("Français");
    Set_Language_Graph(list,list2,user,search,holder,Auth,Type,Img,Phone,Person,Place,Sepa,Etiq,Create,Delete,DeleteAll,Save);
}

function French_People(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Personne", "Carte", "Auteur");
    const user =("Entrer une Personne...");
    const search = ("Rechercher");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const holder = ("Français");
    const photos = ("PHOTO-PROFIL");
    const Auth = ("javascript:French();")
    Set_Language_People(list,user,search,holder,error,photos,Auth);
}

function French_People_Mobile(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Personne", "Auteur");
    const user =("Entrer une Personne...");
    const search = ("Rechercher");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const photos = ("PHOTO-PROFIL");
    const Auth = ("javascript:French();")
    Set_Language_People_Mobile(user,search,list,photos,error,Auth);
}

function French_SelectMap(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Personne", "Carte", "Auteur");
    const New = ("Nouvelle carte");
    const Old = ("Ouvrir carte");
    const Del = ("Effacer carte");
    const holder = ("Français");
    const Auth = ("javascript:French();");
    Set_Language_SelectMap(list,holder,New,Old,Del,Auth);

}

function French_Map(){
    const list = new Array ("Username", "Sites-Internet", "Telephoné", "Portes", "E-Mail", "Créér User", "Graphs", "Personne", "Carte", "Auteur");
    const list2 = new Array ("Insérer une note/commentaire", "Entrez Latidutine", "Entrez la Longitude");
    const user =("Entrez une File...");
    const search = ("Enter");
    const Auth = ("javascript:French();");
    const Type = ("Entrez le Tipologie");
    const Person = ("Personne");
    const Place = ("Lieu");
    const Event = ("Événement");
    const Create = ("Créer");
    const DeleteAll = ("Reset");
    const Save = ("Sauver");
    const holder = ("Français");
    Set_Language_Map(list,list2,user,search,holder,Auth,Type,Person,Place,Event,Create,DeleteAll,Save);
}