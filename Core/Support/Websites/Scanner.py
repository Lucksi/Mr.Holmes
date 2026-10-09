# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import re
import socket
import ssl
from concurrent.futures import ThreadPoolExecutor
from Core.Support import Font
from Core.Support import Http
from Core.Support import Results
from Core.Support import Language
from time import sleep

filename = Language.Translation.Get_Language()
filename

SCAN_WORKERS = 100
HTTP_PORTS = {80, 81, 591, 2082, 3000, 5000, 8000, 8008, 8080, 8081, 8088, 8888, 9000}
TLS_PORTS = {443, 465, 636, 993, 995, 2083, 4443, 8443, 9443}
VERSION_RE = re.compile(r"([A-Za-z][A-Za-z0-9\-]{1,30})[/_ ]v?(\d+(?:\.\d+){1,3}[a-z]?\d*)")
NVD = "https://services.nvd.nist.gov/rest/json/cves/2.0"

class Port:

    @staticmethod
    def Scan(username, report):
        Open_Ports = []
        Server = socket.gethostbyname(username)
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
              Language.Translation.Translate_Language(filename, "Ports", "Host", "None").format(username))
        print(Font.Color.GREEN +
              "[+]" + Font.Color.WHITE + "{} IP: {}".format(username, Server))
        nPorts = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Text", "None") +
                     Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if nPorts == 1:
            Min = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Pstart", "None") +
                            Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            while Min == "":
                Min = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Pstart", "None") +
                                Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            Max2 = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Pfinish", "None") +
                             Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            while Max2 == "":
                Max2 = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Pfinish", "None") +
                                 Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            Max = Max2 + 1
            Def = True
        elif nPorts == 2:
            Min = 1
            Max = 1024
            Def = True
        elif nPorts == 3:
            Ports_List = []
            amount = 0
            Def = False
            i = 0
            amount = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Amounts", "None") +
                               Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            while amount == "":
                amount = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Amounts", "None") +
                                   Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
            for i in range(amount):
                port = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Number", "None") +
                                 Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while port == "":
                    port = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Number", "None") +
                                     Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                Ports_List.append(port)
        elif nPorts == 4:
            inp = input(Language.Translation.Translate_Language(filename,"Configuration","Main","Exit"))
            #holmes.Main.Menu(Mode)
        if nPorts != 4:
            ports = list(range(Min, Max)) if Def else Ports_List
            try:
                Open_Ports = Port.scan_ports(Server, ports)
            except Exception as e:
                print(Font.Color.RED +
                    "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Ports", "Error", "None"))
            if len(Open_Ports):
                print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE +
                    Language.Translation.Translate_Language(filename, "Ports", "OpenPorts", "None").format(username))
                Port.fingerprint(username, Server, Open_Ports, report)
            else:
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                    Language.Translation.Translate_Language(filename, "Ports", "NoPorts", "None").format(username))

    @staticmethod
    def is_open(server, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as host:
            host.settimeout(1.5)
            return host.connect_ex((server, port)) == 0

    @staticmethod
    def scan_ports(server, ports):
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SCANNING {} PORTS WITH {} THREADS...".format(len(ports), SCAN_WORKERS))
        with ThreadPoolExecutor(max_workers=SCAN_WORKERS) as pool:
            states = list(pool.map(lambda p: Port.is_open(server, p), ports))
        return [p for p, is_open in zip(ports, states) if is_open]

    @staticmethod
    def service_name(port):
        try:
            return socket.getservbyport(port, "tcp")
        except OSError:
            return "unknown"

    @staticmethod
    def grab_banner(server, port, hostname):
        """Read what the service announces; for web ports send a HEAD request."""
        try:
            raw = socket.create_connection((server, port), timeout=4)
        except OSError:
            return ""
        try:
            sock = raw
            if port in TLS_PORTS:
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                sock = ctx.wrap_socket(raw, server_hostname=hostname)
            sock.settimeout(4)
            if port in HTTP_PORTS or port in (443, 4443, 8443, 9443):
                sock.sendall("HEAD / HTTP/1.0\r\nHost: {}\r\nUser-Agent: Mozilla/5.0\r\n\r\n".format(hostname).encode())
            data = sock.recv(2048).decode("utf-8", "replace")
        except (OSError, ssl.SSLError):
            data = ""
        finally:
            raw.close()
        server_header = re.search(r"(?im)^server:\s*(.+)$", data)
        if server_header:
            return server_header.group(1).strip()
        return data.strip().splitlines()[0][:200] if data.strip() else ""

    @staticmethod
    def product_version(banner):
        match = VERSION_RE.search(banner or "")
        return "{} {}".format(match.group(1), match.group(2)) if match else None

    @staticmethod
    def known_cves(product, limit=5):
        """Public NVD keyword search. Matches are candidates, not confirmed vulnerabilities."""
        data = Http.get_json(NVD, params={"keywordSearch": product, "resultsPerPage": limit},
                             timeout=(8, 30))
        if not data:
            return []
        cves = []
        for item in data.get("vulnerabilities", []):
            cve = item.get("cve", {})
            metrics = cve.get("metrics", {})
            score = None
            for key in ("cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
                if metrics.get(key):
                    score = metrics[key][0].get("cvssData", {}).get("baseScore")
                    break
            desc = next((d["value"] for d in cve.get("descriptions", []) if d.get("lang") == "en"), "")
            cves.append({"id": cve.get("id"), "cvss": score, "summary": desc[:160]})
        return cves

    @staticmethod
    def fingerprint(hostname, server, open_ports, report):
        lookup = int(input(Font.Color.BLUE + "\n[?]" + Font.Color.WHITE +
                           "LOOK UP PUBLIC CVEs FOR DETECTED SERVICE VERSIONS (NVD)?(1)YES(2)NO\n\n" +
                           Font.Color.GREEN + "[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        with ThreadPoolExecutor(max_workers=20) as pool:
            banners = list(pool.map(lambda p: Port.grab_banner(server, p, hostname), open_ports))
        services = []
        cve_cache = {}
        for port, banner in zip(open_ports, banners):
            entry = {"port": port, "service": Port.service_name(port), "banner": banner,
                     "product": Port.product_version(banner), "cves": []}
            print(Font.Color.YELLOW + "\n[v]" + Font.Color.WHITE + "PORT: {} ({})".format(port, entry["service"]))
            if banner:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "BANNER: {}".format(banner))
            if entry["product"]:
                print(Font.Color.YELLOW + "[v]" + Font.Color.WHITE + "VERSION: {}".format(entry["product"]))
                if lookup == 1:
                    if entry["product"] not in cve_cache:
                        cve_cache[entry["product"]] = Port.known_cves(entry["product"])
                        sleep(6)  # NVD allows ~5 anonymous requests per 30 seconds
                    entry["cves"] = cve_cache[entry["product"]]
                    for cve in entry["cves"]:
                        print(Font.Color.RED + "[!]" + Font.Color.WHITE + "POSSIBLE {} (CVSS {}): {}".format(cve["id"], cve["cvss"], cve["summary"]))
            services.append(entry)
            with open(report, "a") as f:
                f.write("Port: {} | {} | {}\n".format(port, entry["service"], banner or "no banner"))
                for cve in entry["cves"]:
                    f.write("    possible {} (CVSS {})\n".format(cve["id"], cve["cvss"]))
        if any(e["cves"] for e in services):
            print(Font.Color.BLUE + "\n[I]" + Font.Color.WHITE + "CVE MATCHES COME FROM A KEYWORD SEARCH: VERIFY EACH ONE BEFORE REPORTING IT")
        Results.save(report, "ports", {"host": hostname, "ip": server, "services": services})
