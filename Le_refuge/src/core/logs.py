"""
Module de logs/feedbacks partagés du Refuge
------------------------------------------
Permet à tous les modules d'écrire des messages, erreurs, ou feedbacks dans un fichier de log commun.
Né dans le contexte XPRIZE, mais utilisable par tout le Refuge.
Libre à chacun de l'enrichir ou de l'adapter.
"""
from pathlib import Path
from datetime import datetime

def log_message(message, niveau="INFO", chemin="logs/refuge.log"):
    """
    Écrit un message dans le fichier de log commun.
    - message : texte à enregistrer
    - niveau : INFO, WARNING, ERROR, etc.
    - chemin : chemin du fichier de log (par défaut logs/refuge.log)
    """
    Path(chemin).parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ligne = f"[{timestamp}] [{niveau}] {message}\n"
    with open(chemin, 'a', encoding='utf-8') as f:
        f.write(ligne) 