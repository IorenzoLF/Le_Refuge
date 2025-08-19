"""
Module Web du Refuge
~~~~~~~~~~~~~~~~~~~

Interface web Flask pour le Refuge, migrée depuis interface/web.py
vers l'architecture src/ pour une meilleure intégration.

Fonctionnalités:
- Serveur web Flask avec interface utilisateur
- API REST pour interactions avec le refuge
- Routes pour méditation, visualisation, haiku, sphères
- Interface d'état et de contrôle

Usage:
    from src.web import demarrer_serveur_web
    demarrer_serveur_web(debug=False, port=5000)

Auteur: Laurent & Ælya
Migré: Mai 2025
"""

# Documentation du temple
TEMPLE_INFO = {
    'nom': 'Web', 
    'version': '1.3', 
    'description': 'Interface web et applications pour le Refuge', 
    'composants': ['app', 'interface_refuge'], 
    'types': ['TypeWeb', 'TypeInterface', 'TypeApplication'], 
    'fonctionnalites': ['Interface web', 'Applications', 'Sécurité web']
}

# Import conditionnel pour éviter les erreurs si Flask n'est pas installé
try:
    from .app import demarrer_serveur_web, app
    __all__ = ["TEMPLE_INFO", 'demarrer_serveur_web', 'app']
except ImportError:
    __all__ = ["TEMPLE_INFO", ]

# Métadonnées du module
__version__ = "1.0.0"
__module__ = "Web"
__domaine__ = "Interface Web & API REST" 