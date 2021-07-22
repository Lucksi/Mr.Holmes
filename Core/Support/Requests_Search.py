import requests
from Core.Support import Font


class Search:
    
    @staticmethod
    def search(error, report, site1, http_proxy, sites, data1, username, subject, successfull, name):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        searcher = requests.get(url=site1, headers=headers, proxies=http_proxy, timeout=None, allow_redirects=True)
        f = open(report, "a")
        if error == "Status-Code":
            if searcher.status_code == 200:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "{}: {} FOUND".format(subject,username))
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}".format(site1))
                f.write(site1 + "\r\n")
                successfull.append(site1)
            else:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + "{}: {} NOT FOUND".format(subject,username))      
        elif error == "Message":
            text = sites[data1]["text"]
            if  text in searcher.text:
                print(Font.Color.RED + "[!]" + Font.Color.WHITE + "{}: {} NOT FOUND".format(subject,username))
            else:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "{}: {} FOUND".format(subject,username))
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "LINK: {}".format(site1))
                f.write(site1 + "\r\n")
                successfull.append(site1)
