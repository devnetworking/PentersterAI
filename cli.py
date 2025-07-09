import typer
from core.scanner import Scanner
from core.ia import IAGenerator
from utils.logger import Logger
from utils.validator import Validator
import json
from datetime import datetime
import os

app = typer.Typer()
logger = Logger()

@app.command()
def scan(
    target: str = typer.Option(..., "--target", "-t", help="Cible IP ou URL à scanner"),
    mode: str = typer.Option("full", "--mode", "-m", help="Mode de scan : full ou light"),
    save: bool = typer.Option(False, "--save", "-s", help="Sauvegarder le résultat dans le dossier rapports/"),
    report: bool = typer.Option(False, "--report", "-r", help="Générer automatiquement un rapport Markdown"),
    json_output: bool = typer.Option(
        False,
        "--json",
        "--json-output",
        "-j",
        help="Sauvegarder le résultat en JSON dans le dossier rapports/"
    )
):
    """
    Commande de scan de PentestAI.
    """
    if not Validator.is_valid_ip(target) and not Validator.is_valid_url(target):
        logger.error("Cible invalide. Fournir une IP ou URL correcte.")
        raise typer.Exit()

    scanner = Scanner(target)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename_base = target.replace("http://", "").replace("https://", "").replace("/", "_")

    logger.info(f"Lancement du scan sur {target} en mode {mode}")

    if mode == "full":
        result = scanner.run_nmap_scan()
    elif mode == "light":
        result = scanner.run_web_scan()
    else:
        logger.error("Mode invalide. Utiliser 'full' ou 'light'.")
        raise typer.Exit()

    logger.info(f"Résultat du scan :\n{result}")

    if save:
        os.makedirs("rapports", exist_ok=True)
        file_path = f"rapports/scan_{filename_base}_{now}.txt"
        with open(file_path, "w") as f:
            f.write(result)
        logger.info(f"Résultat sauvegardé dans {file_path}")

    if json_output:
        os.makedirs("rapports", exist_ok=True)
        json_data = {
            "target": target,
            "mode": mode,
            "timestamp": now,
            "result": result
        }
        json_file_path = f"rapports/scan_{filename_base}_{now}.json"
        with open(json_file_path, "w") as jf:
            json.dump(json_data, jf, indent=4)
        logger.info(f"Résultat JSON sauvegardé dans {json_file_path}")

    if report:
        ia = IAGenerator()
        prompt = f"Génère un rapport structuré de sécurité basé sur ce résultat de scan : {result}"
        generated_report = ia.generate_payload(prompt)

        report_path = f"rapports/rapport_{filename_base}_{now}.md"
        with open(report_path, "w") as rf:
            rf.write(generated_report)
        logger.info(f"Rapport généré et sauvegardé dans {report_path}")

if __name__ == "__main__":
    app()

