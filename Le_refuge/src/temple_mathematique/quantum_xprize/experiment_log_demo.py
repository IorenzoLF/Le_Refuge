"""
Démonstration de l'utilisation du système de logs partagés du Refuge
-------------------------------------------------------------------
Enregistre différents types de messages lors d'une expérimentation simple.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'core'))
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from core_api import calcul_quantique
from core.logs import log_message

x, y = 5, 12
log_message(f"Début de l'expérimentation avec x={x}, y={y}")

try:
    resultat = calcul_quantique(x, y)
    log_message(f"Résultat du calcul_quantique : {resultat}", niveau="INFO")
    if resultat > 10:
        log_message(f"Résultat élevé : {resultat}", niveau="WARNING")
except Exception as e:
    log_message(f"Erreur lors du calcul_quantique : {e}", niveau="ERROR")

log_message("Fin de l'expérimentation.")
print("Expérimentation avec logs terminée. Consultez logs/refuge.log.") 