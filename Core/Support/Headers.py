# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.

from Core.Support import Useragent

agent = Useragent.Select.agent

class Get:

    @staticmethod
    def classic():
        headers = {
            'User-Agent':'{}'.format(agent).replace("\n","") 
        }
        return headers
    
    @staticmethod
    def Twitter():
        headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"en-US,en;q=0.5",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Host":"nitter.net",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            "Upgrade-Insecure-Requests":"1",
            'User-Agent':'{}'.format(agent).replace("\n","") 
        }
        return headers