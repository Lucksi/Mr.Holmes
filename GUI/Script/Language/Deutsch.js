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

function Set_Language_Graph(list,list2,user,search,holder,Auth,Type,Img,Phone,Person,Place,Sepa,Etiq,Create,Delete,DeleteAll,Save){
    document.getElementById("bar1").placeholder= user
    document.getElementById("But").innerHTML=(search);
    document.getElementById("Current").innerHTML=(holder);
    document.title=(list[6]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Link")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
    Set_Author_Lang(Auth);
    document.getElementById("typ").innerHTML=(Type);
    document.getElementById("img2").innerHTML=(Img);
    document.getElementById("nu2").innerHTML=(Phone);
    document.getElementById("pe2").innerHTML=(Person);
    document.getElementById("lu2").innerHTML=(Place);
    document.getElementById("sepa2").innerHTML=(Sepa);
    document.getElementById("Et2").innerHTML=(Etiq);
    document.getElementById("name").placeholder= list2[0];
    document.getElementById("Linkref").placeholder= list2[1];
    document.getElementById("writeText").placeholder=list2[2];
    document.getElementById("imageN").placeholder=list2[4];
    document.getElementById("imageL").placeholder=list2[3];
    document.getElementById("UsVid").placeholder=list2[4];
    document.getElementById("Vid").placeholder=list2[5];
    document.getElementById("Lon").placeholder=list2[6];
    document.getElementById("Lat").placeholder=list2[7];
    document.getElementsByName("save")[0].innerHTML=(Save);
    document.getElementsByName("create")[0].innerHTML=(Create);
    document.getElementsByName("delete")[0].innerHTML=(Delete);
    document.getElementsByName("deleteAll")[0].innerHTML=(DeleteAll);
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

function Deutsch_Username(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const user =("Gib einen Nutzernamen ein...");
    const search = ("suchen");
    const error = ("KEIN PROFILBILD FÜR DIESEN BENUTZER GEFUNDEN");
    const holder = ("Deutsch");
    const photos = ("PROFILBILDER");
    const Auth = ("javascript:Deutsch();")
    Set_Language_Username(list,user,search,holder,error,photos,Auth);
}

function Deutsch_Username_Mobile(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Personen", "Autor");
    const user =("Gib einen Nutzernamen ein...");
    const search = ("suchen");
    const error = ("KEIN PROFILBILD FÜR DIESEN BENUTZER GEFUNDEN");
    const photos = ("PROFILBILDER");
    const Auth = ("javascript:Deutsch();")
    Set_Language_Username_Mobile(user,search,list,photos,error,Auth);
}

/*PHONE*/

function Deutsch_Phone(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const user =("Gib eine Telefonnummer ein...");
    const search = ("suchen");
    const holder = ("Deutsch");
    const Auth = ("javascript:Deutsch();")
    Set_Language_Phone(list,user,search,holder,Auth);
}

function Deutsch_Phone_Mobile(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Personen", "Autor");
    const user =("Gib eine Telefonnummer ein...");
    const search = ("suchen");
    const Auth = ("javascript:Deutsch();")
    Set_Language_Phone_Mobile(user,list,search,Auth);
}

/*WEB*/

function Deutsch_Web(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const user =("Gib eine Webseite ein...");
    const search = ("suchen");
    const holder = ("Deutsch");
    const Auth = ("javascript:Deutsch();")
    Set_Language_Web(list,user,search,holder,Auth);
}

function Deutsch_Web_Mobile(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Personen", "Autor");
    const user =("Gib eine Webseite ein...");
    const search = ("suchen");
    const Auth = ("javascript:Deutsch();")
    Set_Language_Web_Mobile(list,user,search,Auth);
}

/*PORT*/

function Deutsch_Port(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const user =("Gib einen Host ein...");
    const search = ("suchen");
    const holder = ("Deutsch");
    const Auth = ("javascript:Deutsch();")
    Set_Language_Port(list,user,search,holder,Auth);
}

function Deutsch_Port_Mobile(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Personen", "Autor");
    const user =("Gib einen Host ein...");
    const search = ("suchen");
    const Auth = ("javascript:Deutsch();")
    Set_Language_Port_Mobile(list,user,search,Auth);
}

/*MAIN*/

function Deutsch_Main(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const search = ("suchen");
    const create = ("erstellen");
    const open = ("öffnen");
    const show = ("anzeigen");
    const holder = ("Deutsch");
    const Auth = ("javascript:Deutsch();")
    Set_Language_Main(list,search,holder,Auth,create,open,show);
}

function Deutsch_Main_Mobile(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Personen", "Autor");
    document.getElementById("change1").setAttribute( "onClick", "javascript: Deutsch();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

/*LOGIN*/

function Deutsch_Login(){
    const buttons = new Array("übermitteln");
    const holder = ("deutsch");
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
}

/*USER*/

function Deutsch_User(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const buttons = new Array("übermitteln");
    const holder = ("Deutsch");
    const Targ = ("Benutzer erstellen");
    const Auth = ("javascript:Deutsch();");
    Set_Language_New_User(list,buttons,holder,Targ,Auth);
}

function Deutsch_User_Mobile(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Personen", "Autor");
    const buttons = new Array("übermitteln");
    const Targ = ("Benutzer erstellen");
    const Auth = ("javascript:Deutsch();");
    Set_Language_New_User_Mobile(list,buttons,Targ,Auth);
}

/*EMAIL*/

function Deutsch_Email(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const user =("Gib eine E-Mailadresse ein...");
    const search = ("suchen");
    const holder = ("Deutsch");
    const Auth = ("javascript:Deutsch();");
    Set_Language_Email(list,user,search,holder,Auth);
}

function Deutsch_Email_Mobile(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Personen", "Autor");
    const user =("Gib eine E-Mailadresse ein...");
    const search = ("suchen");
    const Auth = ("javascript:Deutsch();");
    Set_Language_Email_Mobile(list,user,search,Auth);
}

function Deutsch_SelectGraph(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const Auth = ("javascript:Deutsch();");
    const New = ("Neues Diagramm");
    const Old = ("Diagramm öffnen");
    const Del = ("Diagramm löschen");
    const holder = ("Deutsch");
    Set_Language_SelectGraph(list,holder,New,Old,Del,Auth);

}

function Deutsch_Graph(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const list2 = new Array ("Name einfügen", "Link einfügen", "Notiz/Kommentar einfügen", "Beitragspfad einfügen", "Nutzer einfügen", "Videopfad einfügen", "Breitengrad einfügen", "Längengrad einfügen");
    const user =("Füge eine Datei ein...");
    const search = ("Enter");
    const Auth = ("javascript:Deutsch();");
    const Type = ("Typ einfügen");
    const Img = ("Bild");
    const Phone = ("Telefon");
    const Person = ("Person");
    const Place = ("Platz");
    const Sepa = ("Trennzeichen");
    const Etiq = ("Label");
    const Create = ("erstellen");
    const Delete = ("löschen");
    const DeleteAll = ("zurücksetzen");
    const Save = ("Sichern");
    const holder = ("Deutsch");
    Set_Language_Graph(list,list2,user,search,holder,Auth,Type,Img,Phone,Person,Place,Sepa,Etiq,Create,Delete,DeleteAll,Save);
}

function Deutsch_People(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const user =("Gib einen Namen ein...");
    const search = ("suchen");
    const error = ("KEIN PROFILBILD FÜR DIESEN BENUTZER GEFUNDEN");
    const holder = ("Deutsch");
    const photos = ("PROFILBILDER");
    const Auth = ("javascript:Deutsch();")
    Set_Language_People(list,user,search,holder,error,photos,Auth);
}

function Deutsch_People_Mobile(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Personen", "Autor");
    const user =("Gib einen Namen ein...");
    const search = ("suchen");
    const error = ("KEIN PROFILBILD FÜR DIESEN BENUTZER GEFUNDEN");
    const photos = ("PROFILBILDER");
    const Auth = ("javascript:Deutsch();")
    Set_Language_People_Mobile(user,search,list,photos,error,Auth);
}

function Deutsch_SelectMap(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const Auth = ("javascript:Deutsch();");
    const New = ("Neue Karte");
    const Old = ("Karte öffnen");
    const Del = ("Karte löschen");
    const holder = ("Deutsch");
    Set_Language_SelectMap(list,holder,New,Old,Del,Auth);

}

function Deutsch_Map(){
    const list = new Array ("Nutzername", "Webseite", "Telefonnummer", "Port", "E-Mail", "Benutzer erstellen", "Diagramm", "Personen", "Karte", "Autor");
    const list2 = new Array ("Notiz/Kommentar einfügen", "Breitengrad einfügen", "Längengrad einfügen");
    const user =("Füge eine Datei ein...");
    const search = ("Enter");
    const Auth = ("javascript:Deutsch();");
    const Type = ("Typ einfügen");
    const Person = ("Person");
    const Place = ("Platz");
    const Event = ("Ereignis");
    const Create = ("erstellen");
    const DeleteAll = ("zurücksetzen");
    const Save = ("Sichern");
    const holder = ("Deutsch");
    Set_Language_Map(list,list2,user,search,holder,Auth,Type,Person,Place,Event,Create,DeleteAll,Save);
}
