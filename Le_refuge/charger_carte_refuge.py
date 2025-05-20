import json
import os

# Chemin absolu vers la racine du projet
DOSSIER_RACINE = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(DOSSIER_RACINE, 'index_refuge.json')
if not os.path.exists(INDEX_PATH):
    # On cherche dans le dossier parent si besoin
    INDEX_PATH = os.path.join(DOSSIER_RACINE, 'le_refuge', 'index_refuge.json')

class CarteRefuge:
    def __init__(self, chemin_index=INDEX_PATH):
        self.chemin_index = os.path.abspath(chemin_index)
        self.carte = None
        self.charger()

    def charger(self):
        try:
            with open(self.chemin_index, 'r', encoding='utf-8') as f:
                self.carte = json.load(f)
        except Exception as e:
            print(f"Erreur lors du chargement de la carte du refuge : {e}")
            self.carte = None

    def lister(self, categorie):
        if self.carte and categorie in self.carte:
            return self.carte[categorie]
        return []

    def resume(self):
        if not self.carte:
            return "Aucune carte chargée."
        resume = [f"Catégorie : {cat} — {len(fichiers)} éléments" for cat, fichiers in self.carte.items() if cat != "dernière_mise_à_jour"]
        resume.append(f"Dernière mise à jour : {self.carte.get('dernière_mise_à_jour', 'inconnue')}")
        return '\n'.join(resume)

if __name__ == "__main__":
    carte = CarteRefuge()
    print(carte.resume()) 