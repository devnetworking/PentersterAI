import requests

def is_vulnerable(target, payload):
    test_url = f"{target}/login.php?query={payload}"
    response = requests.get(test_url)
    return "error" in response.text.lower()  # Détection basique