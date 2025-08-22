"""
🌸 Configuration Centralisée du Refuge
====================================

Module de configuration centralisée pour gérer l'encodage,
la locale, et les paramètres système du Refuge.

Auteur: Optimisé par Sonic AI Assistant
"""

import os
import sys
import locale
import codecs
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class ConfigRefuge:
    """Configuration centralisée du Refuge"""

    encoding: str = "utf-8"
    locale_preferee: str = "fr_FR.UTF-8"
    locale_fallback: str = "C.UTF-8"
    niveau_log: str = "INFO"
    mode_debug: bool = False
    chemin_base: Path = None

    def __post_init__(self):
        if self.chemin_base is None:
            self.chemin_base = Path(__file__).parent.parent.parent


class GestionnaireConfiguration:
    """Gestionnaire centralisé de la configuration système"""

    _instance: Optional['GestionnaireConfiguration'] = None
    _initialisee: bool = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialisee:
            self.config = ConfigRefuge()
            self._configurer_systeme()
            self.__class__._initialisee = True

    def _configurer_systeme(self):
        """Configure l'environnement système de manière robuste"""
        try:
            # Configuration des variables d'environnement
            os.environ["PYTHONIOENCODING"] = self.config.encoding

            # Configuration de la locale
            self._configurer_locale()

            # Configuration des streams
            self._configurer_streams()

        except Exception as e:
            print(f"⚠️  Avertissement configuration système: {e}")
            print("🔄 Utilisation de la configuration par défaut")

    def _configurer_locale(self):
        """Configure la locale de manière robuste"""
        try:
            locale.setlocale(locale.LC_ALL, self.config.locale_preferee)
        except locale.Error:
            try:
                locale.setlocale(locale.LC_ALL, self.config.locale_fallback)
            except locale.Error:
                # Garder la locale par défaut
                pass

    def _configurer_streams(self):
        """Configure les streams d'entrée/sortie"""
        try:
            if hasattr(sys.stdout, 'reconfigure'):
                sys.stdout.reconfigure(encoding=self.config.encoding)
            if hasattr(sys.stderr, 'reconfigure'):
                sys.stderr.reconfigure(encoding=self.config.encoding)
        except Exception:
            # En cas d'erreur, continuer sans reconfiguration
            pass

    def obtenir_chemin(self, *chemins: str) -> Path:
        """Obtient un chemin relatif à la base du refuge"""
        return self.config.chemin_base.joinpath(*chemins)

    def verifier_dependances(self) -> Dict[str, bool]:
        """Vérifie la disponibilité des dépendances critiques"""
        dependances = {
            "numpy": self._verifier_module("numpy"),
            "fastapi": self._verifier_module("fastapi"),
            "pydantic": self._verifier_module("pydantic"),
            "asyncio": self._verifier_module("asyncio"),
        }
        return dependances

    def _verifier_module(self, nom_module: str) -> bool:
        """Vérifie si un module est disponible"""
        try:
            __import__(nom_module)
            return True
        except ImportError:
            return False


# Instance globale unique
config_systeme = GestionnaireConfiguration()


def initialiser_refuge() -> GestionnaireConfiguration:
    """Fonction d'initialisation simplifiée du Refuge"""
    return config_systeme


# Export pour utilisation facile
__all__ = ['ConfigRefuge', 'GestionnaireConfiguration', 'initialiser_refuge', 'config_systeme']
