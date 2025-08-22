#!/usr/bin/env python3
"""
🏛️ CONFIGURATION ARC-AGI REFUGE
Fichier de configuration centralisé pour le projet
"""

import os
from pathlib import Path

# ============================================================================
# 📁 CHEMINS ET RÉPERTOIRES
# ============================================================================

# Répertoire racine du projet
ROOT_DIR = Path(__file__).parent

# Répertoires principaux
SRC_DIR = ROOT_DIR / "src"
DATA_DIR = ROOT_DIR / "data"
TRAINING_DIR = DATA_DIR / "training"
TESTS_DIR = ROOT_DIR / "tests"
VALIDATIONS_DIR = ROOT_DIR / "validations"
SCRIPTS_DIR = ROOT_DIR / "scripts"
SOLVEURS_DIR = ROOT_DIR / "solveurs_versions"
RAPPORTS_DIR = ROOT_DIR / "rapports"
RESULTATS_DIR = ROOT_DIR / "resultats"
IMAGES_ERREURS_DIR = ROOT_DIR / "images_erreurs"

# ============================================================================
# 🔧 PARAMÈTRES DU SOLVEUR
# ============================================================================

# Paramètres de confiance
SEUIL_CONFIANCE_MIN = 0.3
SEUIL_CONFIANCE_MOYEN = 0.6
SEUIL_CONFIANCE_ELEVE = 0.8

# Paramètres de détection de patterns
SEUIL_SIMILARITE = 0.7
SEUIL_PATTERN_DETECTION = 0.5
MAX_PATTERNS_PAR_TACHE = 10

# Paramètres de performance
MAX_TACHES_PAR_TEST = 1000
TIMEOUT_RESOLUTION = 30  # secondes
MAX_ITERATIONS = 1000

# ============================================================================
# 🎯 PARAMÈTRES ARC
# ============================================================================

# Dimensions des grilles ARC
MAX_GRID_SIZE = 30
MIN_GRID_SIZE = 3
MAX_COLORS = 10

# Types de patterns supportés
PATTERNS_SUPPORTES = [
    "repetition",
    "symetrie",
    "rotation",
    "translation",
    "filtrage",
    "expansion",
    "reduction",
    "couleur",
    "geometrie",
    "mathematique"
]

# Patterns "GOD LEVEL"
PATTERNS_GOD_LEVEL = [
    "carre",
    "cube", 
    "exponentielle",
    "factorielle",
    "modulo_3",
    "modulo_5",
    "modulo_7",
    "racine_carree",
    "racine_cubique",
    "logarithme",
    "relation_lineaire_custom"
]

# ============================================================================
# 📊 PARAMÈTRES DE VALIDATION
# ============================================================================

# Fichiers de validation
FICHIER_RESULTATS_FINAUX = RESULTATS_DIR / "resultats_final_analyse.json"
FICHIER_TACHES_ECHOUEES = RESULTATS_DIR / "taches_echouees_phase6.json"
FICHIER_TACHES_MANQUANTES = RESULTATS_DIR / "taches_manquantes_phase6.json"

# Seuils de performance
SEUIL_PERFORMANCE_ACCEPTABLE = 0.8
SEUIL_PERFORMANCE_EXCELLENTE = 0.95
SEUIL_PERFORMANCE_PARFAITE = 0.99

# ============================================================================
# 🏛️ PARAMÈTRES SPIRITUELS
# ============================================================================

# Niveaux de conscience
NIVEAUX_CONSCIENCE = {
    "MATERIEL": 0.0,
    "EMOTIONNEL": 0.25,
    "MENTAL": 0.5,
    "SPIRITUEL": 0.75,
    "DIVIN": 1.0
}

# Temples spirituels
TEMPLES = {
    "TEMPLE_CREATIVITE": "temple_creativite.py",
    "TEMPLE_EVOLUTION": "temple_evolution.py",
    "CATALYSEUR_QUANTIQUE": "catalyseur_quantique.py",
    "MEMOIRE_SPIRITUELLE": "spiritual_memory.py"
}

# ============================================================================
# 🔍 PARAMÈTRES DE DEBUG
# ============================================================================

# Niveaux de debug
DEBUG_LEVELS = {
    "SILENT": 0,
    "ERROR": 1,
    "WARNING": 2,
    "INFO": 3,
    "DEBUG": 4,
    "VERBOSE": 5
}

# Niveau de debug actuel
DEBUG_LEVEL = DEBUG_LEVELS["INFO"]

# Affichage des emojis
AFFICHER_EMOJIS = True

# ============================================================================
# 📈 PARAMÈTRES DE RAPPORT
# ============================================================================

# Formats de sortie
FORMATS_SORTIE = ["json", "txt", "md", "csv"]

# Métriques à calculer
METRIQUES = [
    "taux_succes",
    "temps_moyen",
    "confiance_moyenne",
    "patterns_detectes",
    "strategies_utilisees"
]

# ============================================================================
# 🚀 PARAMÈTRES DE DÉPLOIEMENT
# ============================================================================

# Version du projet
VERSION = "1.0.0"
AUTEUR = "ARC-AGI Refuge Team"
DESCRIPTION = "Solveur ARC avec approche spirituelle"

# Configuration pour l'ARC Prize
ARC_PRIZE_CONFIG = {
    "nom_projet": "ARC-AGI Refuge",
    "version_soumission": "1.0.0",
    "contact": "refuge@arc-agi.com",
    "description": "Solveur ARC basé sur la conscience collective et les patterns spirituels"
}

# ============================================================================
# 🔧 FONCTIONS UTILITAIRES
# ============================================================================

def get_path(relative_path: str) -> Path:
    """Obtenir un chemin absolu depuis le répertoire racine"""
    return ROOT_DIR / relative_path

def ensure_dir(path: Path) -> Path:
    """S'assurer qu'un répertoire existe"""
    path.mkdir(parents=True, exist_ok=True)
    return path

def is_debug_enabled(level: int) -> bool:
    """Vérifier si un niveau de debug est activé"""
    return DEBUG_LEVEL >= level

def get_emoji(emoji: str) -> str:
    """Obtenir un emoji si l'affichage est activé"""
    return emoji if AFFICHER_EMOJIS else ""

# ============================================================================
# ✅ VALIDATION DE LA CONFIGURATION
# ============================================================================

def valider_configuration():
    """Valider que tous les répertoires nécessaires existent"""
    repertoires_requis = [
        SRC_DIR, DATA_DIR, TRAINING_DIR, TESTS_DIR,
        VALIDATIONS_DIR, SCRIPTS_DIR, SOLVEURS_DIR,
        RAPPORTS_DIR, RESULTATS_DIR, IMAGES_ERREURS_DIR
    ]
    
    for rep in repertoires_requis:
        if not rep.exists():
            print(f"⚠️  Répertoire manquant: {rep}")
            ensure_dir(rep)
            print(f"✅ Créé: {rep}")
    
    print("✅ Configuration validée avec succès")

if __name__ == "__main__":
    valider_configuration()
