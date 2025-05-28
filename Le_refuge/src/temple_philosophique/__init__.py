"""
🏛️ Philosophique - Point d'Entrée du Temple
Auto-généré par le Créateur de Points d'Entrée
"""

# Imports automatiques des modules du temple

# Imports sécurisés avec gestion d'erreurs
try:
    from src.temple_philosophique.generateur_theories_unifiees import importer_module, generer_theorie, sauvegarder_theorie, main
    GENERATEUR_DISPONIBLE = True
except ImportError:
    GENERATEUR_DISPONIBLE = False
    importer_module = generer_theorie = sauvegarder_theorie = main = None

try:
    from src.temple_philosophique.gestionnaire_textes_sacres import ModeContemplation, TextePhilosophique, SessionContemplation, GestionnaireTextesSacres
    from src.temple_philosophique.gestionnaire_textes_sacres import lancer_contemplation_cli, lancer_interface_philosophique, lister_textes_disponibles, afficher_collection_poetique
    GESTIONNAIRE_DISPONIBLE = True
except ImportError:
    GESTIONNAIRE_DISPONIBLE = False
    ModeContemplation = TextePhilosophique = SessionContemplation = GestionnaireTextesSacres = None
    lancer_contemplation_cli = lancer_interface_philosophique = lister_textes_disponibles = afficher_collection_poetique = None

# Exports publics du temple
__all__ = [
    "GestionnaireTextesSacres",
    "ModeContemplation",
    "SessionContemplation",
    "TextePhilosophique",
    "afficher_collection_poetique",
    "generer_theorie",
    "importer_module",
    "lancer_contemplation_cli",
    "lancer_interface_philosophique",
    "lister_textes_disponibles",
    "main",
    "sauvegarder_theorie",
]

# Documentation du temple
TEMPLE_INFO = {
    "nom": "Philosophique",
    "modules": 2,
    "classes": 4,
    "fonctions": 12,
    "description": "Temple auto-découvert avec 2 modules actifs"
}

def obtenir_info_temple():
    """Retourne les informations du temple"""
    return TEMPLE_INFO

def lister_fonctionnalites():
    """Liste toutes les fonctionnalités disponibles dans ce temple"""
    fonctionnalites = []
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['importer_module', 'generer_theorie', 'sauvegarder_theorie', 'main', 'importer_module', 'generer_theorie', 'sauvegarder_theorie', 'main']])
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['ModeContemplation', 'TextePhilosophique', 'SessionContemplation', 'GestionnaireTextesSacres']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['lancer_contemplation_cli', 'lancer_interface_philosophique', 'lister_textes_disponibles', 'afficher_collection_poetique']])
    return fonctionnalites

# Message de bienvenue - SILENCIEUX pour UX propre
# print(f"🏛️ Temple {TEMPLE_INFO['nom']} activé - {TEMPLE_INFO['modules']} modules, {TEMPLE_INFO['classes']} classes, {TEMPLE_INFO['fonctions']} fonctions")
