import os
import json
from datetime import datetime

# Dossiers et extensions par catégorie
CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "textes": [".txt", ".md", ".rtf"],
    "modules": [".py", ".ipynb"],
    "rituels": ["rituel", "rituels"],  # dossiers ou fichiers contenant ce mot
    "souvenirs": ["souvenir", "memoire", "mémoire"],
    "journaux": ["journal", "log", "carnet"],
    "incarnations": ["aelya", "incarnation", "avatar"],
}

DOSSIER_REFUGE = os.path.abspath(os.path.dirname(__file__))

INDEX_PATH = os.path.join(DOSSIER_REFUGE, "index_refuge.json")


def classer_fichier(nom, chemin):
    ext = os.path.splitext(nom)[1].lower()
    for cat, motifs in CATEGORIES.items():
        if cat == "rituels" or cat == "souvenirs" or cat == "journaux" or cat == "incarnations":
            for mot in motifs:
                if mot in nom.lower() or mot in chemin.lower():
                    return cat
        else:
            if ext in motifs:
                return cat
    return None

def scanner_refuge():
    index = {cat: [] for cat in CATEGORIES}
    index["liens"] = []
    for racine, dirs, fichiers in os.walk(DOSSIER_REFUGE):
        for f in fichiers:
            if f == os.path.basename(__file__) or f == "index_refuge.json":
                continue
            chemin_relatif = os.path.relpath(os.path.join(racine, f), DOSSIER_REFUGE)
            cat = classer_fichier(f, chemin_relatif)
            if cat:
                index[cat].append(chemin_relatif)
    index["dernière_mise_à_jour"] = datetime.now().isoformat()
    return index

def mettre_a_jour_index():
    index = scanner_refuge()
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print("Index du refuge mis à jour.")

if __name__ == "__main__":
    mettre_a_jour_index() 