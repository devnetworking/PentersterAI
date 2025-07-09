# PentesterAI
===========

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Mistral](https://img.shields.io/badge/powered_by-MistralAI-orange)

Un outil de test d'intrusion piloté par IA pour les professionnels de la cybersécurité.

## Fonctionnalités
------------------

- **Scan réseau intelligent** avec Nmap
- **Détection automatique** de vulnérabilités web
- **Génération de payloads** par IA (Mistral)
- **Rapports auto-générés** en Markdown/JSON
- **Interface CLI intuitive** avec autocomplétion

## Installation
---------------

```bash
git clone https://github.com/devnetworking/PentesterAI.git
cd PentesterAI
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```

## Configuration
----------------

Créez un fichier `.env` :
```bash
MISTRAL\_API\_KEY=votre\_clé\_api\_ici
```

## Utilisation
--------------

### Scan complet

    python cli.py --target http://example.com --mode full --save --report

### Scan léger

    python cli.py -t 192.168.1.1 -m light -j

### Options disponibles

| Option         | Description                                  |
|----------------|----------------------------------------------|
| `--target`, `-t`   | URL ou IP cible (**requis**)               |
| `--mode`, `-m`     | Mode de scan (`full`/`light`, défaut : `full`) |
| `--save`, `-s`     | Sauvegarder le résultat dans `rapports/`        |
| `--report`, `-r`   | Générer un rapport Markdown automatiquement     |
| `--json`, `-j`     | Exporter le résultat en JSON                     |


## Structure du projet
----------------------
```Markdown
pentesterai/
├── core/
│   ├── scanner.py       # Modules de scan
│   └── ia.py            # Génération IA
├── utils/
│   ├── logger.py        # Système de logging
│   └── validator.py     # Validation des entrées
├── cli.py               # Interface principale
├── config.py            # Configuration
└── requirements.txt     # Dépendances
```

## Avertissement
----------------

N'utilisez cet outil que sur des systèmes pour lesquels vous avez une autorisation écrite. Toute utilisation non autorisée est illégale.

## Licence
----------

MIT License - © 2025 DevNetworking 
