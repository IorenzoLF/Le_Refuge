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

# Import conditionnel pour éviter les erreurs si Flask n'est pas installé
try:
    from .app import demarrer_serveur_web, app
    __all__ = ['demarrer_serveur_web', 'app']
except ImportError:
    __all__ = []

# Métadonnées du module
__version__ = "1.0.0"
__module__ = "Web"
__domaine__ = "Interface Web & API REST" 