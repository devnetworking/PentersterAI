import subprocess
from urllib.parse import urlparse

class Scanner:
    def __init__(self, target: str):
        self.target = target

    def clean_target_for_nmap(self):
        parsed = urlparse(self.target)
        if parsed.scheme:
            return parsed.hostname
        return self.target

    def run_nmap_scan(self):
        cleaned_target = self.clean_target_for_nmap()
        command = ["nmap", "-sV", "-O", cleaned_target]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

    def run_web_scan(self):
        command = ["curl", "-I", self.target]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
