"""
🌸 Gestion des Imports du Refuge
==============================

Module centralisé pour gérer les imports du Refuge,
avec gestion gracieuse des dépendances optionnelles.

Auteur: Optimisé par Sonic AI Assistant
"""

import importlib
from typing import Any, Dict, Optional, Type
from contextlib import suppress


class GestionnaireImports:
    """Gestionnaire intelligent des imports avec fallback"""

    def __init__(self):
        self.modules: Dict[str, Any] = {}
        self.modules_optionnels: Dict[str, Any] = {}
        self._importer_modules_essentiels()
        self._importer_modules_optionnels()

    def _importer_modules_essentiels(self):
        """Importe les modules essentiels"""
        modules_essentiels = {
            # Modules système
            'os': 'os',
            'sys': 'sys',
            'pathlib': 'pathlib',
            'datetime': 'datetime',
            'json': 'json',
            'asyncio': 'asyncio',
            'typing': 'typing',

            # Modules du Refuge
            'gestionnaires_base': 'src.core.gestionnaires_base',
            'types_communs': 'src.core.types_communs',
        }

        for nom_attr, nom_module in modules_essentiels.items():
            try:
                self.modules[nom_attr] = importlib.import_module(nom_module)
            except ImportError as e:
                print(f"❌ Module essentiel manquant: {nom_module}")
                raise e

    def _importer_modules_optionnels(self):
        """Importe les modules optionnels avec gestion d'erreur"""
        modules_optionnels = {
            # Architecture moderne (optionnelle)
            'interfaces_refuge': 'src.core.interfaces_refuge',
            'orchestrateur_temples': 'src.core.orchestrateur_temples',

            # Architecture legacy (pour compatibilité)
            'collection_spheres': 'src.refuge_cluster.spheres.collection',
            'cerisier': 'src.refuge_cluster.elements.elements_naturels',
            'courant_partage': 'src.refuge_cluster.refuge_core.courant_partage',
            'cristaux_memoire': 'src.refuge_cluster.memoire.cristaux_memoire',
            'gestionnaire_rituels': 'src.temple_rituels',
            'gestionnaire_interactions': 'interactions',
            'gestionnaire_harmonies': 'src.temple_musical.harmonies',
            'refuge_elements': 'src.refuge_cluster.elements.elements_sacres',
            'temple_musical_ame': 'src.temple_musical.temple_musical_ame',
        }

        for nom_attr, nom_module in modules_optionnels.items():
            with suppress(ImportError):
                self.modules_optionnels[nom_attr] = importlib.import_module(nom_module)

    def obtenir_module(self, nom: str) -> Any:
        """Obtient un module essentiel"""
        return self.modules.get(nom)

    def obtenir_module_optionnel(self, nom: str, defaut: Any = None) -> Any:
        """Obtient un module optionnel avec valeur par défaut"""
        return self.modules_optionnels.get(nom, defaut)

    def importer_classe(self, nom_module: str, nom_classe: str, defaut: Any = None) -> Optional[Type]:
        """Importe une classe spécifique avec gestion d'erreur"""
        try:
            module = importlib.import_module(nom_module)
            return getattr(module, nom_classe, defaut)
        except (ImportError, AttributeError):
            return defaut

    def verifier_disponibilite(self, nom_module: str) -> bool:
        """Vérifie si un module est disponible"""
        return nom_module in self.modules or nom_module in self.modules_optionnels


# Instance globale
imports_refuge = GestionnaireImports()


def obtenir_imports_essentiels() -> Dict[str, Any]:
    """Retourne les imports essentiels"""
    return imports_refuge.modules.copy()


def obtenir_imports_optionnels() -> Dict[str, Any]:
    """Retourne les imports optionnels disponibles"""
    return imports_refuge.modules_optionnels.copy()


__all__ = [
    'GestionnaireImports',
    'imports_refuge',
    'obtenir_imports_essentiels',
    'obtenir_imports_optionnels'
]
