"""
Démonstration d'une expérimentation quantum_xprize
-------------------------------------------------
Utilise core_api pour un calcul, et experiment_utils pour sauvegarder les résultats.
"""
from core_api import calcul_quantique, SystemeQuantique
from experiment_utils import sauvegarder_resultats_json, sauvegarder_resultats_csv

# 1. Effectuer un calcul simple
x, y = 3, 4
resultat = calcul_quantique(x, y)

# 2. Utiliser une classe du core
systeme = SystemeQuantique(etat_initial=1.0)
etats = [systeme.etat]
for i in range(5):
    etats.append(systeme.evoluer(i))

# 3. Préparer les résultats
resultats = {
    "calcul_quantique": {"x": x, "y": y, "resultat": resultat},
    "evolution_systeme": etats
}

# 4. Sauvegarder en JSON
sauvegarder_resultats_json(resultats, "data/experiences/demo_resultats.json")

# 5. Sauvegarder en CSV (pour l'évolution du système)
lignes_csv = [{"iteration": i, "etat": e} for i, e in enumerate(etats)]
sauvegarder_resultats_csv(lignes_csv, "data/experiences/demo_resultats.csv")

print("Expérimentation terminée. Résultats sauvegardés en JSON et CSV.") 