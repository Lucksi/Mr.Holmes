from hashlib import new
import random
import itertools
from itertools import cycle
class proxy:
    
    Https_proxies = [
        "20.195.17.90:3128",
        "20.97.28.47:8080",
        "138.68.42.77:3128",
        "178.134.155.82:48146",
    ]

    Not_Working = {
        "167.71.171.14:8080",
        "176.235.131.230:9090",
        "180.250.170.210:59778",
        "190.85.244.70:999",
        "89.36.195.238:35328",
        "222.252.156.61:62694",
        "193.136.19.68:8080",
        "157.230.103.91:36635",
    }
    
    choice1 = random.choice(Https_proxies)
    choice2 = choice1.split(":",1)
    choice3 = choice2[0]
    final_proxis = {
        'http': "//" + choice1,
        'https': "//" + choice1,
    }