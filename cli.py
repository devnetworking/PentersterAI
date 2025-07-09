import argparse
from core.scanner import NetworkScanner, WebScanner
from core.ia import IAAssistant
from core.exploits import ExploitManager

def main():
    parser = argparse.ArgumentParser(description="PentestAI - Framework de test d'intrusion piloté par IA")
    parser.add_argument("--target", required=True, help="Cible (URL ou IP)")
    parser.add_argument("--mode", choices=["scan", "attack", "full"], default="scan", help="Mode d'opération")
    args = parser.parse_args()

    # Initialisation des modules
    ia = IAAssistant(api_key="your_openai_key")
    network_scanner = NetworkScanner()
    web_scanner = WebScanner()
    exploit_manager = ExploitManager(ia)

    # Exécution
    if args.mode in ["scan", "full"]:
        print("[+] Phase de reconnaissance...")
        network_scanner.run(args.target)
        web_scanner.run(args.target)

    if args.mode in ["attack", "full"]:
        print("[+] Phase d'attaque...")
        exploit_manager.run(args.target)

if __name__ == "__main__":
    main()