"""
🗺️ Générateur de Carte du Refuge
Migré depuis scripts/utils/carte_refuge.py
Scanner automatique pour créer et maintenir index_refuge.json
"""

import os
import json
from datetime import datetime
from pathlib import Path

# Chemin vers la racine du projet (depuis src/utils/)
DOSSIER_RACINE = Path(__file__).parent.parent.parent
INDEX_PATH = DOSSIER_RACINE / "index_refuge.json"

# Dossiers et extensions par catégorie - Version enrichie pour le Refuge
CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".tiff"],
    "textes": [".txt", ".md", ".rtf", ".doc", ".docx"],
    "modules": [".py", ".ipynb", ".pyi"],
    "configurations": [".json", ".yaml", ".yml", ".toml", ".ini", ".cfg"],
    "rituels": ["rituel", "rituels", "ceremony", "ceremonie"],
    "souvenirs": ["souvenir", "memoire", "mémoire", "memory", "memories"],
    "journaux": ["journal", "log", "carnet", "diary", "note"],
    "incarnations": ["aelya", "ælya", "incarnation", "avatar", "nourhan"],
    "spheres": ["sphere", "sphère", "sphères"],
    "elements": ["element", "élément", "elements", "éléments", "sacre", "sacré"],
    "meditation": ["meditation", "méditation", "zen", "mindfulness"],
    "musique": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg"],
    "videos": [".mp4", ".avi", ".mov", ".mkv", ".webm", ".flv"],
    "donnees": [".csv", ".xlsx", ".db", ".sqlite", ".sql"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "scripts": [".bat", ".sh", ".ps1", ".cmd"],
    "web": [".html", ".css", ".js", ".vue", ".react"],
    "poesie": ["poeme", "poème", "poetry", "vers", "haiku"],
    "conscience": ["conscience", "consciousness", "awareness", "eveil", "éveil"],
    "harmonie": ["harmonie", "harmony", "equilibre", "équilibre", "balance"],
    "exploration": ["exploration", "discovery", "recherche", "investigation"],
    "transformation": ["transformation", "evolution", "évolution", "metamorphose"],
    "connexion": ["connexion", "connection", "lien", "bridge", "pont"]
}

def classer_fichier(nom, chemin):
    """Classe un fichier selon les catégories du Refuge
    
    Args:
        nom: Nom du fichier
        chemin: Chemin relatif du fichier
        
    Returns:
        str: Nom de la catégorie ou None
    """
    nom_lower = nom.lower()
    chemin_lower = chemin.lower()
    ext = os.path.splitext(nom)[1].lower()
    
    # Catégories par extension
    for cat, motifs in CATEGORIES.items():
        if cat in ["images", "textes", "modules", "configurations", "musique", 
                  "videos", "donnees", "archives", "scripts", "web"]:
            if ext in motifs:
                return cat
    
    # Catégories par mots-clés dans le nom/chemin
    for cat, motifs in CATEGORIES.items():
        if cat not in ["images", "textes", "modules", "configurations", "musique",
                      "videos", "donnees", "archives", "scripts", "web"]:
            for mot in motifs:
                if mot in nom_lower or mot in chemin_lower:
                    return cat
    
    return "autres"  # Catégorie par défaut

def scanner_refuge():
    """Scanne le refuge et génère l'index complet
    
    Returns:
        dict: Index complet du refuge par catégories
    """
    # Initialisation avec toutes les catégories
    index = {cat: [] for cat in CATEGORIES}
    index["autres"] = []
    index["stats"] = {}
    
    print(f"🔍 Scan du refuge depuis: {DOSSIER_RACINE}")
    
    fichiers_total = 0
    dossiers_total = 0
    
    # Parcours de tous les fichiers
    for racine, dirs, fichiers in os.walk(DOSSIER_RACINE):
        # Ignorer certains dossiers
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in 
                  ['__pycache__', 'node_modules', '.git', '.venv', 'venv']]
        
        dossiers_total += len(dirs)
        
        for fichier in fichiers:
            # Ignorer certains fichiers
            if (fichier.startswith('.') or 
                fichier == os.path.basename(__file__) or 
                fichier == "index_refuge.json"):
                continue
                
            chemin_complet = os.path.join(racine, fichier)
            chemin_relatif = os.path.relpath(chemin_complet, DOSSIER_RACINE)
            
            # Classification
            categorie = classer_fichier(fichier, chemin_relatif)
            index[categorie].append(chemin_relatif)
            fichiers_total += 1
    
    # Statistiques
    index["stats"] = {
        "fichiers_total": fichiers_total,
        "dossiers_total": dossiers_total,
        "categories_actives": len([cat for cat, fichiers in index.items() 
                                 if cat not in ["stats", "dernière_mise_à_jour"] and fichiers])
    }
    
    # Métadonnées
    index["dernière_mise_à_jour"] = datetime.now().isoformat()
    
    return index

def mettre_a_jour_index():
    """Met à jour l'index du refuge"""
    print("🗺️ Génération de la carte du refuge...")
    
    index = scanner_refuge()
    
    # Sauvegarde
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    # Rapport
    stats = index["stats"]
    categories_actives = [(cat, len(fichiers)) for cat, fichiers in index.items() 
                         if cat not in ["stats", "dernière_mise_à_jour"] and fichiers]
    
    print(f"✅ Index du refuge mis à jour!")
    print(f"📊 {stats['fichiers_total']} fichiers, {stats['dossiers_total']} dossiers")
    print(f"📂 {stats['categories_actives']} catégories actives:")
    
    for cat, count in sorted(categories_actives, key=lambda x: x[1], reverse=True):
        print(f"   • {cat.capitalize()}: {count} éléments")
    
    print(f"💾 Sauvegardé dans: {INDEX_PATH}")

def afficher_resume_index():
    """Affiche un résumé de l'index existant"""
    if not INDEX_PATH.exists():
        print("❌ Aucun index trouvé. Exécutez d'abord la génération.")
        return
    
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    print("📋 Résumé de l'index du refuge:")
    print("-" * 40)
    
    for cat, fichiers in index.items():
        if cat not in ["stats", "dernière_mise_à_jour"] and fichiers:
            print(f"📁 {cat.capitalize()}: {len(fichiers)} éléments")
    
    if "stats" in index:
        stats = index["stats"]
        print(f"\n📊 Total: {stats['fichiers_total']} fichiers")
    
    derniere_maj = index.get('dernière_mise_à_jour', 'inconnue')
    print(f"🕒 Dernière mise à jour: {derniere_maj}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "resume":
        afficher_resume_index()
    else:
        mettre_a_jour_index() 