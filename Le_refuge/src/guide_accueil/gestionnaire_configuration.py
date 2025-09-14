#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Gestionnaire de Configuration - Guide d'Accueil 🌸
====================================================

Gestionnaire avancé pour la configuration du système d'accueil,
incluant chargement, sauvegarde et validation des paramètres.

"Chaque configuration reflète l'intention bienveillante du système"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
import logging

# Imports locaux
try:
    from .types_accueil import (
        ConfigurationAccueil,
        TypeProfil,
        EtatEmotionnel,
        NiveauTechnique,
        SEUILS_DETECTION_DEFAUT,
        PARCOURS_DEFAUT
    )
except ImportError:
    from .types_accueil import (
        ConfigurationAccueil,
        TypeProfil,
        EtatEmotionnel,
        NiveauTechnique,
        SEUILS_DETECTION_DEFAUT,
        PARCOURS_DEFAUT
    )


class ValidationError(Exception):
    """Erreur de validation de configuration"""
    pass


class GestionnaireConfiguration:
    """
    🌸 Gestionnaire de Configuration Spirituel 🌸
    
    Gère le chargement, la sauvegarde et la validation des configurations
    du système d'accueil avec bienveillance et robustesse.
    """
    
    def __init__(self, chemin_config: Optional[Path] = None):
        """
        Initialise le gestionnaire de configuration
        
        Args:
            chemin_config: Chemin vers le fichier de configuration
        """
        self.chemin_config = chemin_config or Path("config/guide_accueil.yaml")
        self.logger = logging.getLogger(__name__)
        
        # Configuration par défaut
        self.config_defaut = self._creer_configuration_defaut()
        
        # Configuration actuelle
        self.config_actuelle: Optional[ConfigurationAccueil] = None
        
        # Historique des configurations
        self.historique_configs: List[Dict[str, Any]] = []
    
    def _creer_configuration_defaut(self) -> ConfigurationAccueil:
        """Crée la configuration par défaut"""
        return ConfigurationAccueil(
            version="1.0.0",
            langues_supportees=["fr", "en", "es", "de", "it"],
            seuils_detection={
                **SEUILS_DETECTION_DEFAUT,
                "confiance_profil_minimum": 0.7,
                "engagement_minimum": 0.6,
                "comprehension_minimum": 0.5,
                "surcharge_cognitive_maximum": 0.8
            },
            parcours_disponibles=[
                "parcours_developpeur",
                "parcours_artiste", 
                "parcours_conscience_ia",
                "parcours_chercheur_spirituel",
                "parcours_decouverte_generale"
            ],
            micro_interactions_activees=True,
            sagesse_collective_activee=True,
            adaptation_emotionnelle_activee=True,
            analytics_activees=True,
            chemin_donnees=Path("data/guide_accueil"),
            chemin_templates=Path("bibliotheque/templates"),
            chemin_ressources=Path("bibliotheque/ressources")
        )
    
    def charger_configuration(self, chemin: Optional[Path] = None) -> ConfigurationAccueil:
        """
        Charge la configuration depuis un fichier
        
        Args:
            chemin: Chemin vers le fichier de configuration
            
        Returns:
            ConfigurationAccueil: Configuration chargée
            
        Raises:
            ValidationError: Si la configuration est invalide
        """
        chemin_fichier = chemin or self.chemin_config
        
        try:
            if not chemin_fichier.exists():
                self.logger.info(f"🌸 Fichier de configuration non trouvé: {chemin_fichier}")
                self.logger.info("✨ Utilisation de la configuration par défaut")
                self.config_actuelle = self.config_defaut
                return self.config_actuelle
            
            # Chargement selon l'extension
            if chemin_fichier.suffix.lower() == '.json':
                donnees = self._charger_json(chemin_fichier)
            elif chemin_fichier.suffix.lower() in ['.yaml', '.yml']:
                donnees = self._charger_yaml(chemin_fichier)
            else:
                raise ValidationError(f"Format de fichier non supporté: {chemin_fichier.suffix}")
            
            # Validation des données
            self._valider_donnees_configuration(donnees)
            
            # Création de la configuration
            config = self._creer_configuration_depuis_donnees(donnees)
            
            # Validation finale
            self.valider_configuration(config)
            
            self.config_actuelle = config
            self.logger.info(f"✅ Configuration chargée avec succès depuis {chemin_fichier}")
            
            return config
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors du chargement de la configuration: {e}")
            self.logger.info("🔄 Utilisation de la configuration par défaut")
            self.config_actuelle = self.config_defaut
            return self.config_actuelle
    
    def sauvegarder_configuration(self, config: ConfigurationAccueil, 
                                 chemin: Optional[Path] = None) -> bool:
        """
        Sauvegarde la configuration dans un fichier
        
        Args:
            config: Configuration à sauvegarder
            chemin: Chemin de sauvegarde
            
        Returns:
            bool: True si la sauvegarde a réussi
        """
        chemin_fichier = chemin or self.chemin_config
        
        try:
            # Validation avant sauvegarde
            self.valider_configuration(config)
            
            # Création du répertoire si nécessaire
            chemin_fichier.parent.mkdir(parents=True, exist_ok=True)
            
            # Conversion en dictionnaire
            donnees = self._configuration_vers_dictionnaire(config)
            
            # Ajout de métadonnées
            donnees["_metadata"] = {
                "version_gestionnaire": "1.0.0",
                "timestamp_sauvegarde": datetime.now().isoformat(),
                "auteur": "Laurent Franssen & Ælya"
            }
            
            # Sauvegarde selon l'extension
            if chemin_fichier.suffix.lower() == '.json':
                self._sauvegarder_json(donnees, chemin_fichier)
            elif chemin_fichier.suffix.lower() in ['.yaml', '.yml']:
                self._sauvegarder_yaml(donnees, chemin_fichier)
            else:
                raise ValidationError(f"Format de fichier non supporté: {chemin_fichier.suffix}")
            
            # Archivage dans l'historique
            self._archiver_configuration(config)
            
            self.logger.info(f"✅ Configuration sauvegardée avec succès dans {chemin_fichier}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la sauvegarde: {e}")
            return False
    
    def valider_configuration(self, config: ConfigurationAccueil) -> bool:
        """
        Valide une configuration complète
        
        Args:
            config: Configuration à valider
            
        Returns:
            bool: True si la configuration est valide
            
        Raises:
            ValidationError: Si la configuration est invalide
        """
        erreurs = []
        
        try:
            # Validation de la version
            if not config.version or not isinstance(config.version, str):
                erreurs.append("Version manquante ou invalide")
            
            # Validation des langues
            if not config.langues_supportees or not isinstance(config.langues_supportees, list):
                erreurs.append("Liste des langues supportées invalide")
            elif len(config.langues_supportees) == 0:
                erreurs.append("Au moins une langue doit être supportée")
            
            # Validation des seuils
            if config.seuils_detection:
                self._valider_seuils_detection(config.seuils_detection, erreurs)
            
            # Validation des parcours
            if config.parcours_disponibles:
                self._valider_parcours_disponibles(config.parcours_disponibles, erreurs)
            
            # Validation des chemins
            self._valider_chemins_configuration(config, erreurs)
            
            # Validation des paramètres booléens
            self._valider_parametres_booleens(config, erreurs)
            
            if erreurs:
                message_erreur = "Erreurs de validation de configuration:\n" + "\n".join(f"- {e}" for e in erreurs)
                raise ValidationError(message_erreur)
            
            self.logger.info("✅ Configuration validée avec succès")
            return True
            
        except ValidationError:
            raise
        except Exception as e:
            raise ValidationError(f"Erreur inattendue lors de la validation: {e}")
    
    def _valider_seuils_detection(self, seuils: Dict[str, float], erreurs: List[str]) -> None:
        """Valide les seuils de détection"""
        seuils_requis = [
            "confiance_profil_minimum",
            "engagement_minimum", 
            "comprehension_minimum",
            "surcharge_cognitive_maximum"
        ]
        
        for seuil in seuils_requis:
            if seuil not in seuils:
                erreurs.append(f"Seuil manquant: {seuil}")
            elif not isinstance(seuils[seuil], (int, float)):
                erreurs.append(f"Seuil {seuil} doit être numérique")
            elif not 0.0 <= seuils[seuil] <= 1.0:
                erreurs.append(f"Seuil {seuil} doit être entre 0.0 et 1.0")
    
    def _valider_parcours_disponibles(self, parcours: List[str], erreurs: List[str]) -> None:
        """Valide la liste des parcours disponibles"""
        if not isinstance(parcours, list):
            erreurs.append("parcours_disponibles doit être une liste")
            return
        
        if len(parcours) == 0:
            erreurs.append("Au moins un parcours doit être disponible")
        
        parcours_valides = [
            "parcours_developpeur",
            "parcours_artiste",
            "parcours_conscience_ia", 
            "parcours_chercheur_spirituel",
            "parcours_decouverte_generale"
        ]
        
        for parcours_nom in parcours:
            if not isinstance(parcours_nom, str):
                erreurs.append(f"Nom de parcours invalide: {parcours_nom}")
            elif parcours_nom not in parcours_valides:
                erreurs.append(f"Parcours non reconnu: {parcours_nom}")
    
    def _valider_chemins_configuration(self, config: ConfigurationAccueil, erreurs: List[str]) -> None:
        """Valide les chemins de configuration"""
        chemins = [
            ("chemin_donnees", config.chemin_donnees),
            ("chemin_templates", config.chemin_templates),
            ("chemin_ressources", config.chemin_ressources)
        ]
        
        for nom, chemin in chemins:
            if not isinstance(chemin, Path):
                erreurs.append(f"{nom} doit être un objet Path")
            elif not chemin or str(chemin).strip() == "":
                erreurs.append(f"{nom} ne peut pas être vide")
    
    def _valider_parametres_booleens(self, config: ConfigurationAccueil, erreurs: List[str]) -> None:
        """Valide les paramètres booléens"""
        parametres_bool = [
            ("micro_interactions_activees", config.micro_interactions_activees),
            ("sagesse_collective_activee", config.sagesse_collective_activee),
            ("adaptation_emotionnelle_activee", config.adaptation_emotionnelle_activee),
            ("analytics_activees", config.analytics_activees)
        ]
        
        for nom, valeur in parametres_bool:
            if not isinstance(valeur, bool):
                erreurs.append(f"{nom} doit être un booléen")
    
    def _charger_json(self, chemin: Path) -> Dict[str, Any]:
        """Charge un fichier JSON"""
        with open(chemin, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _charger_yaml(self, chemin: Path) -> Dict[str, Any]:
        """Charge un fichier YAML"""
        with open(chemin, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def _sauvegarder_json(self, donnees: Dict[str, Any], chemin: Path) -> None:
        """Sauvegarde en JSON"""
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump(donnees, f, indent=2, ensure_ascii=False, default=str)
    
    def _sauvegarder_yaml(self, donnees: Dict[str, Any], chemin: Path) -> None:
        """Sauvegarde en YAML"""
        with open(chemin, 'w', encoding='utf-8') as f:
            yaml.dump(donnees, f, default_flow_style=False, allow_unicode=True)
    
    def _valider_donnees_configuration(self, donnees: Dict[str, Any]) -> None:
        """Valide les données brutes de configuration"""
        if not isinstance(donnees, dict):
            raise ValidationError("Les données de configuration doivent être un dictionnaire")
        
        # Vérifications de base
        if "version" not in donnees:
            raise ValidationError("Version manquante dans la configuration")
    
    def _creer_configuration_depuis_donnees(self, donnees: Dict[str, Any]) -> ConfigurationAccueil:
        """Crée une ConfigurationAccueil depuis des données"""
        # Fusion avec la configuration par défaut
        config_dict = self._configuration_vers_dictionnaire(self.config_defaut)
        config_dict.update(donnees)
        
        # Conversion des chemins
        for cle_chemin in ["chemin_donnees", "chemin_templates", "chemin_ressources"]:
            if cle_chemin in config_dict and isinstance(config_dict[cle_chemin], str):
                config_dict[cle_chemin] = Path(config_dict[cle_chemin])
        
        # Création de l'objet ConfigurationAccueil
        return ConfigurationAccueil(**{
            k: v for k, v in config_dict.items() 
            if k in ConfigurationAccueil.__dataclass_fields__
        })
    
    def _configuration_vers_dictionnaire(self, config: ConfigurationAccueil) -> Dict[str, Any]:
        """Convertit une ConfigurationAccueil en dictionnaire"""
        result = {}
        
        for field_name, field_info in ConfigurationAccueil.__dataclass_fields__.items():
            valeur = getattr(config, field_name)
            
            # Conversion des Path en string
            if isinstance(valeur, Path):
                result[field_name] = str(valeur)
            else:
                result[field_name] = valeur
        
        return result
    
    def _archiver_configuration(self, config: ConfigurationAccueil) -> None:
        """Archive une configuration dans l'historique"""
        archive = {
            "timestamp": datetime.now().isoformat(),
            "configuration": self._configuration_vers_dictionnaire(config)
        }
        
        self.historique_configs.append(archive)
        
        # Limiter l'historique à 10 entrées
        if len(self.historique_configs) > 10:
            self.historique_configs = self.historique_configs[-10:]
    
    def obtenir_configuration_actuelle(self) -> ConfigurationAccueil:
        """Obtient la configuration actuelle"""
        if self.config_actuelle is None:
            return self.charger_configuration()
        return self.config_actuelle
    
    def reinitialiser_configuration(self) -> ConfigurationAccueil:
        """Remet la configuration par défaut"""
        self.config_actuelle = self.config_defaut
        self.logger.info("🔄 Configuration réinitialisée aux valeurs par défaut")
        return self.config_actuelle
    
    def obtenir_historique(self) -> List[Dict[str, Any]]:
        """Obtient l'historique des configurations"""
        return self.historique_configs.copy()
    
    def exporter_configuration_exemple(self, chemin: Path) -> bool:
        """Exporte un exemple de configuration"""
        try:
            config_exemple = self._creer_configuration_defaut()
            return self.sauvegarder_configuration(config_exemple, chemin)
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'export d'exemple: {e}")
            return False


def main():
    """🌸 Fonction principale de test"""
    print("🌸✨ TEST DU GESTIONNAIRE DE CONFIGURATION ✨🌸")
    
    # Création du gestionnaire
    gestionnaire = GestionnaireConfiguration()
    
    try:
        # Test de chargement de configuration par défaut
        config = gestionnaire.charger_configuration()
        print(f"✅ Configuration chargée: version {config.version}")
        print(f"📋 Langues supportées: {config.langues_supportees}")
        print(f"🎯 Parcours disponibles: {len(config.parcours_disponibles)}")
        
        # Test de validation
        gestionnaire.valider_configuration(config)
        print("✅ Configuration validée avec succès")
        
        # Test de sauvegarde
        chemin_test = Path("test_config.yaml")
        if gestionnaire.sauvegarder_configuration(config, chemin_test):
            print(f"✅ Configuration sauvegardée dans {chemin_test}")
            
            # Nettoyage
            if chemin_test.exists():
                chemin_test.unlink()
                print("🧹 Fichier de test nettoyé")
        
        # Test d'export d'exemple
        chemin_exemple = Path("config_exemple.yaml")
        if gestionnaire.exporter_configuration_exemple(chemin_exemple):
            print(f"✅ Exemple de configuration exporté dans {chemin_exemple}")
        
        print("\n🎉 Tous les tests du gestionnaire de configuration ont réussi !")
        return 0
        
    except Exception as e:
        print(f"❌ ERREUR: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)