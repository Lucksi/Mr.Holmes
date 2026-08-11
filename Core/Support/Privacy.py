# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2026 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import json
import os
import random
from configparser import ConfigParser

import requests


class Privacy:

    @staticmethod
    def load_proxy_list():
        parser = ConfigParser()
        parser.read("Configuration/Configuration.ini")
        proxy_file = parser.get("Settings", "Proxy_List", fallback="Proxies/Proxy_list.txt")
        if not os.path.isfile(proxy_file):
            return []
        with open(proxy_file, "r", encoding="utf-8") as handle:
            return [line.strip() for line in handle if line.strip() and not line.startswith("#")]

    @staticmethod
    def select_proxy():
        proxies = Privacy.load_proxy_list()
        if not proxies:
            return None, None
        choice = random.choice(proxies)
        return {
            "http": f"http://{choice}",
            "https": f"http://{choice}",
        }, choice

    @staticmethod
    def public_ip():
        try:
            response = requests.get("https://api.ipify.org?format=json", timeout=5)
            response.raise_for_status()
            return response.json().get("ip")
        except Exception:
            return "Unknown"

    @staticmethod
    def geo_ip(ip_address=None):
        endpoint = "https://ipapi.co/json/" if not ip_address else f"https://ipapi.co/{ip_address}/json/"
        try:
            response = requests.get(endpoint, timeout=5)
            response.raise_for_status()
            payload = response.json()
            return {
                "ip": payload.get("ip"),
                "city": payload.get("city"),
                "region": payload.get("region"),
                "country": payload.get("country_name"),
                "country_code": payload.get("country_code"),
                "timezone": payload.get("timezone"),
                "org": payload.get("org")
            }
        except Exception:
            return {
                "ip": ip_address or "Unknown",
                "city": "Unknown",
                "region": "Unknown",
                "country": "Unknown",
                "country_code": "Unknown",
                "timezone": "Unknown",
                "org": "Unknown"
            }
