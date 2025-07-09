import nmap
import requests
from bs4 import BeautifulSoup

class NetworkScanner:
    def run(self, target):
        print(f"[*] Scanning réseau de {target}...")
        nm = nmap.PortScanner()
        nm.scan(hosts=target, arguments="-sV --script vulners")
        for host in nm.all_hosts():
            print(f"Ports ouverts : {nm[host].all_tcp()}")

class WebScanner:
    def run(self, target):
        print(f"[*] Analyse web de {target}...")
        response = requests.get(target)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        print(f"{len(forms)} formulaires trouvés !")