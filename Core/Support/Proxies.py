import random

class proxy:
    
    Proxy_file = "Proxies/Proxy_list.txt"
    f = open(Proxy_file,"r")
    value = f.readlines()
    f.close()
    choice1 = random.choice(value)
    choice2 = choice1.split(":",1)
    choice3 = choice2[0]
    
    final_proxis = {
        'http': "//" + choice1,
        'https': "//" + choice1,
    }