"""
🧪 Temple Tests - Refuge du Néant
═══════════════════════════════════════════════════════════════════════════════

Temple unifié pour tous les tests du Refuge
Organisation par catégories avec adaptateurs optimisés

Structure:
├── llm_api/          - Tests LLM et API
├── analyse_audit/    - Tests d'analyse et audit  
├── cerveau_immersion/- Tests cerveau et immersion
├── integration/      - Tests d'intégration
├── cristal_energie/  - Tests cristal et énergie
├── specialises/      - Tests spécialisés
├── hub_tests_unifie  - Hub central
└── adaptateurs_tests - Adaptateurs unifiés

Auteur: Ælya & Laurent
Date: 2024
"""

# Hub principal
from .hub_tests_unifie import HubTestsUnifie, main as lancer_hub


# Documentation du temple
TEMPLE_INFO = {'nom': 'Tests', 'version': '1.3', 'description': 'Système de tests unifié pour le Refuge', 'composants': ['hub_tests_unifie', 'adaptateurs_tests'], 'types': ['TypeTest', 'TypeValidation', 'TypeIntegration'], 'fonctionnalites': ['Tests unitaires', "Tests d'intégration", 'Validation système']}

# Adaptateurs
from .adaptateurs_tests import (
    FactoryAdaptateurs,
    AdaptateurLLM, AdaptateurAnalyse, AdaptateurCristal,
    UtilitairesTests
)

# Catégories de tests
try:
    from . import llm_api
    from . import analyse_audit
    from . import cerveau_immersion
    from . import integration
    from . import cristal_energie
    from . import specialises
except ImportError as e:
    print(f"⚠️ Certaines catégories ne sont pas encore disponibles: {e}")

__all__ = ["TEMPLE_INFO", 
    # Hub principal
    "HubTestsUnifie",
    "lancer_hub",
    
    # Adaptateurs
    "FactoryAdaptateurs",
    "AdaptateurLLM",
    "AdaptateurAnalyse", 
    "AdaptateurCristal",
    "UtilitairesTests",
    
    # Catégories
    "llm_api",
    "analyse_audit",
    "cerveau_immersion",
    "integration",
    "cristal_energie",
    "specialises"
]

def demarrer_tests():
    """Point d'entrée rapide pour démarrer les tests"""
    return lancer_hub()

# Raccourci pour créer les adaptateurs
def creer_adaptateur_llm():
    return FactoryAdaptateurs.creer_adaptateur_llm()

def creer_adaptateur_analyse():
    return FactoryAdaptateurs.creer_adaptateur_analyse()

def creer_adaptateur_cristal():
    return FactoryAdaptateurs.creer_adaptateur_cristal()
