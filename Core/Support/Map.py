# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2022-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Support import Font
from Core.Support import Language

LangFile = Language.Translation.Get_Language()
LangFile


class Creation:

    @staticmethod
    def mapPost(data_fold, Lat, Lon, image2):
        map_file = data_fold + \
            "/Map.html"
        rescue = 'var image = document.getElementById("Image");image.addEventListener("error",function handleError(){image.src="../../../../../../Icon/Entities/Image.png";image.style.width="250px";image.style.height="250px";});'
        content = '''
        <!--{}-->
        <html>
            <head>
                <title>Map Post</title>
                <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
                <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
                <meta charset ="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=0.9">
                <meta name="theme-color" content="#000000">
                <link rel = "icon" href = "../../../../../../Icon/Base/Logo.png">
                <link rel = "stylesheet" href= "../../../../../../Css/Dark/Style.css">
            </head>
            <body>
                <center>
                    <p id = "Const">POST ID: {}</p>
                    <a href = "../{}.jpg" target = "blank"><img src = "../{}.jpg" height="350px" width="350px" style="border: 3px solid;border-radius:20px;border-color:#ffffff;" id = "Image"></a>
                    <script>{}</script>
                </center>
                <br>
                <div class = "map" id="map"></div>
                <script>
                    var map = L.map("map").setView([{},{}], 14);
                    L.tileLayer('https://{}.tile.openstreetmap.org/{}/{}/{}.png',{}.addTo(map);
                    L.marker([{},{}]).addTo(map).bindPopup('Post id {} is approximatley based in this Area.').openPopup();
                </script>;       
            </body>
        </html>'''.format(Language.Translation.Translate_Language(LangFile, "Default", "Generated", "None"),image2, image2, image2, rescue, Lat, Lon, "{s}", "{z}", "{x}", "{y}", "{ attribution: '&copy; <a href= https://www.openstreetmap.org/copyright >OpenStreetMap</a> contributors'})", Lat, Lon, image2)
        f = open(map_file, "w", encoding="utf-8")
        f.write(content)
        f.close()
        print(Font.Color.BLUE + "[I]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(LangFile, "Default", "Map", "None").format(map_file))

    @staticmethod
    def mapPhone(jsonfile, Lat, Lon, num,Type):
        if Type == "Phone":
            link = '<link rel = "stylesheet" href= "../../../Css/Dark/Style.css">'
            icon = '<link rel = "icon" href= "../../../Icon/Base/Logo.png">'
        elif Type == "Web":
            link = '<link rel = "stylesheet" href= "../../../../Css/Dark/Style.css">'
            icon = '<link rel = "icon" href= "../../../../Icon/Base/Logo.png">'
        map_file = jsonfile.replace(".json", ".html")
        content = '''
        <!--{}-->
        <html>
            <head>
                <title>Map Phone</title>
                <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
                <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
                <meta charset ="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=0.9">
                <meta name="theme-color" content="#000000">
                {}
                {}
            </head>
            <body>
                <p id = "Const">PHONE NUMBER: {}</p>
                <div class = "map" id="map"></div>
                <script>
                    var map = L.map("map").setView([{},{}], 14);
                    L.tileLayer('https://{}.tile.openstreetmap.org/{}/{}/{}.png',{}.addTo(map);
                    L.marker([{},{}]).addTo(map).bindPopup('Number {} is approximatley based in this Area.').openPopup();
                </script>;       
            </body>
        </html>'''.format(Language.Translation.Translate_Language(LangFile, "Default", "Generated", "None"),link,icon,num,Lat, Lon, "{s}", "{z}", "{x}", "{y}", "{ attribution: '&copy; <a href= https://www.openstreetmap.org/copyright >OpenStreetMap</a> contributors'})", Lat, Lon, num)
        f = open(map_file, "w", encoding="utf-8")
        f.write(content)
        f.close()
        print(Font.Color.BLUE + "[I]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(LangFile,"Default", "Map", "None").format(map_file))

    @staticmethod
    def mapWeb(jsonfile, Lat, Lon, username):
        map_file = jsonfile.replace(".json", ".html")
        name = map_file.replace(".html","")
        content = '''
        <!--{}-->
        <html>
            <head>
                <title>Map Web</title>
                <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
                <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
                <meta charset ="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=0.9">
                <meta name="theme-color" content="#000000">
                <link rel = "stylesheet" href= "../../../../Css/Dark/Style.css">
                <link rel = "icon" href= "../../../../Icon/Base/Logo.png">
            </head>
            <body>
                <p id = "Const">WEBSITE: {}</p>
                <div class = "map" id="map"></div>
                <script>
                    var map = L.map("map").setView([{},{}], 14);
                    L.tileLayer('https://{}.tile.openstreetmap.org/{}/{}/{}.png',{}.addTo(map);
                    L.marker([{},{}]).addTo(map).bindPopup('{} is approximatley based in this Area.').openPopup();
                </script>;       
            </body>
        </html>'''.format(Language.Translation.Translate_Language(LangFile, "Default", "Generated", "None"),username,Lat, Lon, "{s}", "{z}", "{x}", "{y}", "{ attribution: '&copy; <a href= https://www.openstreetmap.org/copyright >OpenStreetMap</a> contributors'})", Lat, Lon,username)
        f = open(map_file, "w", encoding="utf-8")
        f.write(content)
        f.close()
        print(Font.Color.BLUE + "[I]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(LangFile,"Default", "Map", "None").format(map_file))
