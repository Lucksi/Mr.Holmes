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
    document.getElementById("Lat").placeholder=list2[6];
    document.getElementById("Lon").placeholder=list2[7];
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

function Italian_Username(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Persone", "Mappa", "Autore");
    const user =("Inserisci un Username...");
    const search = ("Cerca");
    const error = ("NESSUNA FOTO PROFILO TROVATA PER QUESTO USER");
    const holder = ("Italiano");
    const photos = ("FOTO-PROFILO");
    const Auth = ("javascript:Italiano();")
    Set_Language_Username(list,user,search,holder,error,photos,Auth);
}

function Italian_Username_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Persone",  "Autore");
    const user =("Inserisci un Username...");
    const search = ("Cerca");
    const error = ("NESSUNA FOTO PROFILO TROVATA PER QUESTO USER");
    const photos = ("FOTO-PROFILO");
    const Auth = ("javascript:Italiano();");
    Set_Language_Username_Mobile(user,search,list,photos,error,Auth);
}

/*PHONE*/

function Italian_Phone(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Persone", "Mappa", "Autore");
    const user =("Inserisci un NumeroTelefonico...");
    const search = ("Cerca");
    const holder = ("Italiano");
    const Auth = ("javascript:Italiano();");
    Set_Language_Phone(list,user,search,holder,Auth);
}

function Italian_Phone_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Persone", "Autore");
    const user =("Inserisci un NumeroTelefonico...");
    const search = ("Cerca");
    const Auth = ("javascript:Italiano();");
    Set_Language_Phone_Mobile(user,list,search,Auth);
}

/*WEB*/

function Italian_Web(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Persone", "Mappa", "Autore");
    const user =("Inserisci un Sito web...");
    const search = ("Cerca");
    const holder = ("Italiano");
    const Auth = ("javascript:Italiano();");
    Set_Language_Web(list,user,search,holder,Auth);
}

function Italian_Web_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Persone", "Autore");
    const user =("Inserisci un Sito web...");
    const search = ("Cerca");
    const Auth = ("javascript:Italiano();");
    Set_Language_Web_Mobile(list,user,search,Auth);
}

/*PORT*/

function Italian_Port(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Persone", "Mappa", "Autore");
    const user =("Inserisci un Host...");
    const search = ("Cerca");
    const holder = ("Italiano");
    const Auth = ("javascript:Italiano();");
    Set_Language_Port(list,user,search,holder,Auth);
}

function Italian_Port_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Persone", "Autore");
    const user =("Inserisci un Host...");
    const search = ("Cerca");
    const Auth = ("javascript:Italiano();")
    Set_Language_Port_Mobile(list,user,search,Auth);
}

/*MAIN*/

function Italian_Main(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Mappa", "Persone", "Autore");
    const search = ("Cerca");
    const create = ("Crea");
    const show = ("Mostra");
    const open = ("Apri");
    const holder = ("Italiano");
    const Auth = ("javascript:Italiano();")
    Set_Language_Main(list,search,holder,Auth,create,open,show);
}

function Italian_Main_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Persone", "Autore");
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
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Persone", "Mappa", "Autore");
    const buttons = new Array("Invio");
    const holder = ("Italiano");
    const Targ = ("CREA UTENTE");
    const Auth = ("javascript:Italiano();");
    Set_Language_New_User(list,buttons,holder,Targ,Auth);
}  

function Italian_User_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Persone", "Autore");
    const buttons = new Array("Invio");
    const Targ = ("CREA UTENTE");
    const Auth = ("javascript:Italiano();");
    Set_Language_New_User_Mobile(list,buttons,Targ,Auth);
}

/*EMAIL*/

function Italian_Email(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Persone", "Mappa", "Autore");
    const user =("Inserisci un E-Mail...");
    const search = ("Cerca");
    const holder = ("Italiano");
    const Auth = ("javascript:Italiano();");
    Set_Language_Email(list,user,search,holder,Auth);
}

function Italian_Email_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente", "Persone", "Autore");
    const user =("Inserisci un E-Mail...");
    const search = ("Cerca");
    const Auth = ("javascript:Italiano();");
    Set_Language_Email_Mobile(list,user,search,Auth);
}

function Italian_SelectGraph(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Persone", "Mappa", "Autore");
    const Auth = ("javascript:Italiano();");
    const New = ("Nuovo Grafico");
    const Old = ("Apri Grafico");
    const Del = (" Cancella Grafico");
    const holder = ("Italiano");
    Set_Language_SelectGraph(list,holder,New,Old,Del,Auth);

}

function Italian_Graph(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Persone", "Mappa", "Autore");
    const list2 = new Array("Inserisci il Nome", "Inserisci Collegemento", "Inserisci nota/commento", "Inserisci il percoso dell'immagine", "Inserisci Utente","Inserisci il percorso del video", "Inserisci Latidutine", "Inserisci Longitudine")
    const user =("Inserisci un File...");
    const search = ("Invio");
    const Auth = ("javascript:Italiano();");
    const Type = ("Inserisci Tipo");
    const Img = ("Immagine");
    const Phone = ("Telefono");
    const Person = ("Persona");
    const Place = ("Luogo");
    const Sepa = ("Separatore");
    const Etiq = ("Etichetta");
    const Create = ("Crea");
    const Delete = ("Elimina");
    const DeleteAll = ("Resetta")
    const Save = ("Salva");
    const holder = ("Italiano");
    Set_Language_Graph(list,list2,user,search,holder,Auth,Type,Img,Phone,Person,Place,Sepa,Etiq,Create,Delete,DeleteAll,Save);
}

function Italian_People(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Persone", "Mappa", "Autore");
    const user =("Inserisci un Nome...");
    const search = ("Cerca");
    const error = ("NESSUNA FOTO PROFILO TROVATA PER QUESTO USER");
    const holder = ("Italiano");
    const photos = ("FOTO-PROFILO");
    const Auth = ("javascript:Italiano();")
    Set_Language_People(list,user,search,holder,error,photos,Auth);
}

function Italian_People_Mobile(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Persone",  "Autore");
    const user =("Inserisci un Nome...");
    const search = ("Cerca");
    const error = ("NESSUNA FOTO PROFILO TROVATA PER QUESTO USER");
    const photos = ("FOTO-PROFILO");
    const Auth = ("javascript:Italiano();");
    Set_Language_Username_People(user,search,list,photos,error,Auth);
}

function Italian_SelectMap(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Persone", "Mappa", "Autore");
    const New = ("Nuova Mappa");
    const Old = ("Apri Mappa");
    const Del = ("Cancella Mappa");
    const holder = ("Italiano");
    const Auth = ("javascript:Italiano();");
    Set_Language_SelectMap(list,holder,New,Old,Del,Auth);

}

function Italian_Map(){
    const list = new Array ("Username", "Siti-Web", "Telefono", "Porte", "E-Mail", "Crea Utente",  "Grafico" , "Persone", "Mappa", "Autore");
    const list2 = new Array ("Inserisci nota/commento", "Inserisci Latidutine", "Inserisci Longitudine");
    const user =("Inserisci nome File...");
    const search = ("Invio");
    const Auth = ("javascript:Italiano();");
    const Type = ("Inserisci Tipo");
    const Person = ("Persona");
    const Place = ("Luogo");
    const Event = ("Evento");
    const Create = ("Crea");
    const DeleteAll = ("Reset");
    const Save = ("Salva");
    const holder = ("Italiano");
    Set_Language_Map(list,list2,user,search,holder,Auth,Type,Person,Place,Event,Create,DeleteAll,Save);
}