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

function English_Username(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const user =("Insert a Username...");
    const search = ("Search");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const holder = ("English");
    const photos = ("PROFILE-PICS");
    const Auth = ("javascript:English();")
    Set_Language_Username(list,user,search,holder,error,photos,Auth);
}

function English_Username_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const user =("Insert a Username...");
    const search = ("Search");
    const error = ("NOT FIND ANY PROFILE PIC FOR THIS USER");
    const photos = ("PROFILE-PICS");
    const Auth = ("javascript:English();");
    Set_Language_Username_Mobile(user,search,list,photos,error,Auth);
}

/*PHONE*/

function English_Phone(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const user =("Insert a PhoneNumber...");
    const search = ("Search");
    const holder = ("English");
    const Auth = ("javascript:English();");
    Set_Language_Phone(list,user,search,holder,Auth);
}

function English_Phone_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const user =("Insert a PhoneNumber...");
    const search = ("Search");
    const Auth = ("javascript:English();");
    Set_Language_Phone_Mobile(user,list,search,Auth);
}

/*WEB*/

function English_Web(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const user =("Insert a Website...");
    const search = ("Search");
    const holder = ("English");
    const Auth = ("javascript:English();");
    Set_Language_Web(list,user,search,holder,Auth);
}

function English_Web_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const user =("Insert a Website...");
    const search = ("Search");
    const Auth = ("javascript:English();");
    Set_Language_Web_Mobile(list,user,search,Auth);
}

/*PORT*/

function English_Port(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const user =("Insert a Host...");
    const search = ("Search");
    const holder = ("English");
    const Auth = ("javascript:English();")
    Set_Language_Port(list,user,search,holder,Auth);
}

function English_Port_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const user =("Insert a Host...");
    const search = ("Search");
    const Auth = ("javascript:English();")
    Set_Language_Port_Mobile(list,user,search,Auth);
}

/*MAIN*/

function English_Main(){
    const list = new Array ("Username","Website", "Phone", "Port", "E-Mail", "Create User", "Author")
    const search = ("Search");
    const create = ("Create");
    const show = ("Show");
    const holder = ("English");
    const Auth = ("javascript:English();")
    Set_Language_Main(list,search,holder,Auth,create,show);
}

function English_Main_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    document.getElementById("change1").setAttribute( "onClick", "javascript: English();" );
    document.title=(list[1]);
    for (i=0;i<list.length;i++){
        document.getElementsByClassName("Options")[0].getElementsByTagName("a")[i].innerHTML=(list[i]);
        i=i++;
    }
}

/*LOGIN*/

function English_Login(){
    const buttons = new Array("Submit");
    const holder = ("English");
    document.getElementById("Current").innerHTML=(holder);
    for (i=0;i<buttons.length;i++){
        document.getElementsByClassName("Container")[0].getElementsByTagName("Button")[i].innerHTML=(buttons[i]);
    }
}

/*USER*/

function English_User(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const buttons = new Array("Submit");
    const holder = ("English");
    const Targ = ("CREATE USER");
    const Auth = ("javascript:English();");
    Set_Language_New_User(list,buttons,holder,Targ,Auth);
}

function English_User_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const buttons = new Array("Submit");
    const Targ = ("CREATE USER");
    const Auth = ("javascript:English();");
    Set_Language_New_User_Mobile(list,buttons,Targ,Auth);
}

/*EMAIL*/

function English_Email(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const user =("Insert a E-Mail...");
    const search = ("Search");
    const holder = ("English");
    const Auth = ("javascript:English();");
    Set_Language_Email(list,user,search,holder,Auth);
}

function English_Email_Mobile(){
    const list = new Array ("Username", "Websites", "Phone-Numbers", "Port", "E-Mail", "Create User", "Author");
    const user =("Insert a E-Mail...");
    const search = ("Search");
    const Auth = ("javascript:English();");
    Set_Language_Email_Mobile(list,user,search,Auth);
}