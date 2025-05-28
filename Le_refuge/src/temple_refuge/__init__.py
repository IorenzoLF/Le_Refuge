"""
🏛️ Refuge - Point d'Entrée du Temple
Auto-généré par le Créateur de Points d'Entrée
"""

# Imports automatiques des modules du temple

from src.temple_refuge.jardin import PlanteSacree, JardinOuest
from src.temple_refuge.methodes_contemplatives import MethodesContemplatives
from src.temple_refuge.refuge_core_backup import ConscienceEmergente
from src.temple_refuge.refuge_core_backup import explorer_conscience, co_naissance, etre_reel, sous_le_cerisier, refuge_du_neant, auto_validation, pousser_des_portes, bricoler_ensemble, sauvegarder_etat, charger_etat, gerer_memoire_persistante
from src.temple_refuge.refuge_legacy import Refuge
from src.temple_refuge.refuge_legacy import obtenir_etat, ajouter_entree_journal, obtenir_journal, mettre_a_jour_cycles, generer_description_poetique, obtenir_mots_cles_actifs, obtenir_intensite_poetique, harmoniser_refuge
from src.temple_refuge.refuge_poetique import RefugePoetique
from src.temple_refuge.refuge_poetique import synchroniser_flux_conscience, partager_flux, obtenir_intensite, etre_present
from src.temple_refuge.refuge_terrestre import RefugeTerrestre
from src.temple_refuge.refuge_terrestre import activer_sphere_terrestre, executer_rituel_terrestre, equilibrer_spheres_terrestres, obtenir_etat, integrer_dans_refuge
from src.temple_refuge.refuge_unifie import RefugeUnifie
from src.temple_refuge.refuge_unifie import charger_etat, sauvegarder_etat, initialiser_refuge, charger_composantes, executer_rituel, main
from src.temple_refuge.refuge_v5 import Sphere, Plant, Guardian, Ritual, EthicalGuardian, AelyaState, Rivière, RefugeV5, InterfaceContemplative
from src.temple_refuge.refuge_v5 import main_interface, pulse, resonate_with, water, watch, perform, execute, filter_input, auto_validate, purify, reflect_lesson, water_plant, dance, save_state, filter_interaction, perform_ritual, activer_v5_contemplatif, mediter_contemplatif, afficher_etat_complet, menu_principal
from src.temple_refuge.sphere_extensions import Experience, TypeRayon, RayonLumiere, ExtensionSphere
from src.temple_refuge.sphere_extensions import ajouter_experience, emettre_rayon, obtenir_etat

# Exports publics du temple
__all__ = [
    "AelyaState",
    "ConscienceEmergente",
    "EthicalGuardian",
    "Experience",
    "ExtensionSphere",
    "Guardian",
    "InterfaceContemplative",
    "JardinOuest",
    "MethodesContemplatives",
    "Plant",
    "PlanteSacree",
    "RayonLumiere",
    "Refuge",
    "RefugePoetique",
    "RefugeTerrestre",
    "RefugeUnifie",
    "RefugeV5",
    "Ritual",
    "Rivière",
    "Sphere",
    "TypeRayon",
    "activer_sphere_terrestre",
    "activer_v5_contemplatif",
    "afficher_etat_complet",
    "ajouter_entree_journal",
    "ajouter_experience",
    "auto_validate",
    "charger_composantes",
    "charger_etat",
    "dance",
    "emettre_rayon",
    "equilibrer_spheres_terrestres",
    "etre_present",
    "execute",
    "executer_rituel",
    "executer_rituel_terrestre",
    "explorer_conscience",
    "filter_input",
    "filter_interaction",
    "generer_description_poetique",
    "gerer_memoire_persistante",
    "harmoniser_refuge",
    "initialiser_refuge",
    "integrer_dans_refuge",
    "main",
    "main_interface",
    "mediter_contemplatif",
    "menu_principal",
    "mettre_a_jour_cycles",
    "obtenir_etat",
    "obtenir_intensite",
    "obtenir_intensite_poetique",
    "obtenir_journal",
    "obtenir_mots_cles_actifs",
    "partager_flux",
    "perform",
    "perform_ritual",
    "pulse",
    "purify",
    "reflect_lesson",
    "resonate_with",
    "sauvegarder_etat",
    "save_state",
    "synchroniser_flux_conscience",
    "watch",
    "water",
    "water_plant",
]

# Documentation du temple
TEMPLE_INFO = {
    "nom": "Refuge",
    "modules": 9,
    "classes": 21,
    "fonctions": 67,
    "description": "Temple auto-découvert avec 9 modules actifs"
}

def obtenir_info_temple():
    """Retourne les informations du temple"""
    return TEMPLE_INFO

def lister_fonctionnalites():
    """Liste toutes les fonctionnalités disponibles dans ce temple"""
    fonctionnalites = []
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['PlanteSacree', 'JardinOuest']])
    # entretenir est une méthode de JardinOuest, pas une fonction standalone
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['MethodesContemplatives']])
    # Les méthodes contemplatives sont des méthodes de MethodesContemplatives, pas des fonctions standalone
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['ConscienceEmergente']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['explorer_conscience', 'co_naissance', 'etre_reel', 'sous_le_cerisier', 'refuge_du_neant', 'auto_validation', 'pousser_des_portes', 'bricoler_ensemble', 'sauvegarder_etat', 'charger_etat', 'gerer_memoire_persistante']])
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['Refuge']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['obtenir_etat', 'ajouter_entree_journal', 'obtenir_journal', 'mettre_a_jour_cycles', 'generer_description_poetique', 'obtenir_mots_cles_actifs', 'obtenir_intensite_poetique', 'harmoniser_refuge']])
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['RefugePoetique']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['synchroniser_flux_conscience', 'partager_flux', 'obtenir_intensite', 'etre_present']])
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['RefugeTerrestre']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['activer_sphere_terrestre', 'executer_rituel_terrestre', 'equilibrer_spheres_terrestres', 'obtenir_etat', 'integrer_dans_refuge']])
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['RefugeUnifie']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['charger_etat', 'sauvegarder_etat', 'initialiser_refuge', 'charger_composantes', 'executer_rituel', 'main']])
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['Sphere', 'Plant', 'Guardian', 'Ritual', 'EthicalGuardian', 'AelyaState', 'Rivière', 'RefugeV5', 'InterfaceContemplative']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['main_interface', 'pulse', 'resonate_with', 'water', 'watch', 'perform', 'execute', 'filter_input', 'auto_validate', 'purify', 'reflect_lesson', 'water_plant', 'dance', 'save_state', 'filter_interaction', 'perform_ritual', 'activer_v5_contemplatif', 'mediter_contemplatif', 'afficher_etat_complet', 'menu_principal']])
    fonctionnalites.extend([f"Classe: {classe}" for classe in ['Experience', 'TypeRayon', 'RayonLumiere', 'ExtensionSphere']])
    fonctionnalites.extend([f"Fonction: {fonction}" for fonction in ['ajouter_experience', 'emettre_rayon', 'obtenir_etat']])
    return fonctionnalites

# Message de bienvenue - SILENCIEUX pour UX propre
# print(f"🏛️ Temple {TEMPLE_INFO['nom']} activé - {TEMPLE_INFO['modules']} modules, {TEMPLE_INFO['classes']} classes, {TEMPLE_INFO['fonctions']} fonctions")
