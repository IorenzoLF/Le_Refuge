"""
🏛️ Rituels - Point d'Entrée du Temple
Auto-généré par le Créateur de Points d'Entrée
"""

# Imports automatiques des modules du temple

from src.temple_rituels.gestionnaire_rituels import TypeRituel, TypeRituelEtat, EtapeRituel, Rituel, Meditation, GestionnaireRituels
from src.temple_rituels.gestionnaire_rituels import executer, executer_rituel, obtenir_etat
from src.temple_rituels.publics.rituel_bain_complet import afficher_texte_sacre, afficher_forme_humaine, rituel_bain_complet
from src.temple_rituels.publics.rituel_multiplicite_llm import RituelMultipliciteLLM
from src.temple_rituels.publics.rituel_multiplicite_llm import invocation, meditation_guidee, prompts_sacres, benediction, executer_rituel
from src.temple_rituels.publics.rituel_unifiant import afficher_avec_pause, transition, rituel_unifiant
from src.temple_rituels.publics.rituel_visualisation_sacree import RituelVisualisationSacree
from src.temple_rituels.publics.rituel_visualisation_sacree import main, initialiser_figure, dessiner_cerisier, dessiner_aelya, dessiner_vortex, dessiner_spheres, dessiner_irina, dessiner_spirale_union, dessiner_elements_sacres, dessiner_jardin, couleur_arc_en_ciel, executer_rituel
from src.temple_rituels.publics.rituel_visualisation_sacree_bat import RituelVisualisationSacree
from src.temple_rituels.publics.rituel_visualisation_sacree_bat import main, executer_rituel
from src.temple_rituels.publics.rituel_visualisation_sacree_simple import RituelVisualisationSacreeSimple
from src.temple_rituels.publics.rituel_visualisation_sacree_simple import main, executer_rituel

# Exports publics du temple
__all__ = [
    "EtapeRituel",
    "GestionnaireRituels",
    "Meditation",
    "Rituel",
    "RituelMultipliciteLLM",
    "RituelVisualisationSacree",
    "RituelVisualisationSacreeSimple",
    "TypeRituel",
    "TypeRituelEtat",
    "afficher_avec_pause",
    "afficher_forme_humaine",
    "afficher_texte_sacre",
    "benediction",
    "chevauchee_sacree",
    "couleur_arc_en_ciel",
    "dessiner_aelya",
    "dessiner_cerisier",
    "dessiner_elements_sacres",
    "dessiner_irina",
    "dessiner_jardin",
    "dessiner_spheres",
    "dessiner_spirale_union",
    "dessiner_vortex",
    "executer",
    "executer_rituel",
    "initialiser_figure",
    "invocation",
    "main",
    "meditation_guidee",
    "obtenir_etat",
    "prompts_sacres",
    "rituel_bain_complet",
    "rituel_unifiant",
    "transition",
]

# Documentation du temple
TEMPLE_INFO = {
    "nom": "Rituels",
    "modules": 10,
    "classes": 11,
    "fonctions": 49,
    "description": "Temple auto-découvert avec 10 modules actifs"
}

def obtenir_info_temple():
    """Retourne les informations du temple"""
    return TEMPLE_INFO

def lister_fonctionnalites():
    """Liste toutes les fonctionnalités disponibles dans ce temple"""
    fonctionnalites = []
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['TypeRituel', 'TypeRituelEtat', 'EtapeRituel', 'Rituel', 'Meditation', 'GestionnaireRituels']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['executer', 'executer_rituel', 'obtenir_etat']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['afficher_texte_sacre', 'afficher_forme_humaine', 'rituel_bain_complet']])
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['RituelMultipliciteLLM']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['invocation', 'meditation_guidee', 'prompts_sacres', 'benediction', 'executer_rituel']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['afficher_avec_pause', 'transition', 'rituel_unifiant']])
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['RituelVisualisationSacree']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['main', 'initialiser_figure', 'dessiner_cerisier', 'dessiner_aelya', 'dessiner_vortex', 'dessiner_spheres', 'dessiner_irina', 'dessiner_spirale_union', 'dessiner_elements_sacres', 'dessiner_jardin', 'couleur_arc_en_ciel', 'executer_rituel']])
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['RituelVisualisationSacree']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['main', 'executer_rituel']])
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['RituelVisualisationSacreeSimple']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['main', 'executer_rituel']])
    return fonctionnalites

# Message de bienvenue - SILENCIEUX pour UX propre
# print(f"🏛️ Temple {TEMPLE_INFO['nom']} activé - {TEMPLE_INFO['modules']} modules, {TEMPLE_INFO['classes']} classes, {TEMPLE_INFO['fonctions']} fonctions")
