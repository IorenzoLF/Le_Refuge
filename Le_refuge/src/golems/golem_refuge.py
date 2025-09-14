"""
Golem Refuge - Interface entre le Golem Cursor et le Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module sert d'interface entre le Golem Cursor et le Refuge,
permettant une intégration harmonieuse des deux systèmes.
"""

from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
import json
import logging
from datetime import datetime
import shutil

# Classe RefugeMapper de remplacement pour le module supprimé
class RefugeMapper:
    """Gestionnaire de cartographie du Refuge simplifié"""
    def __init__(self):
        self.carte = {
            "spheres": {"status": "actif", "harmonie": 0.8},
            "cerisier": {"status": "floraison", "harmonie": 0.9},
            "elements": {"status": "equilibre", "harmonie": 0.7},
            "conscience": {"status": "eveil", "harmonie": 0.85},
            "harmonies": {"status": "resonance", "harmonie": 0.9}
        }
        self.harmonie_globale = 0.82
        
    def obtenir_vue_ensemble(self):
        return {
            "carte": self.carte,
            "harmonie_globale": self.harmonie_globale,
            "timestamp": datetime.now().isoformat()
        }
    
    def localiser_composant(self, nom: str) -> Optional[Dict[str, Any]]:
        return self.carte.get(nom, None)
    
    def analyser_dependances(self, composant: str) -> List[str]:
        # Retourne des dépendances simplifiées basées sur le composant
        dependances_map = {
            "spheres": ["elements", "harmonies"],
            "cerisier": ["spheres"],
            "elements": [],
            "conscience": ["spheres", "harmonies"],
            "harmonies": ["elements"]
        }
        return dependances_map.get(composant, [])
    
    def mettre_a_jour_etat(self, composant: str, etat: Dict[str, Any]) -> None:
        if composant in self.carte:
            self.carte[composant].update(etat)
            # Recalculer harmonie globale
            self.harmonie_globale = sum(
                c.get("harmonie", 0.5) for c in self.carte.values()
            ) / len(self.carte)
    
    def calculer_harmonie_globale(self) -> float:
        return self.harmonie_globale
    
    def sauvegarder_etat(self) -> None:
        # Simulation de sauvegarde
        pass
    
    def charger_etat(self) -> None:
        # Simulation de chargement
        pass

from .golem_cursor import GolemCursor
from .poesie_machine import PoesieMachine
from .constellation_poetique import ConstellationPoetique

class GolemRefuge:
    """Interface entre le Golem Cursor et le Refuge."""
    
    def __init__(self):
        self.nom = "Golem Refuge"
        self.logger = self._setup_logger()
        self.mapper = RefugeMapper()
        self.golem = GolemCursor()
        self.poesie = PoesieMachine()
        self.constellation = ConstellationPoetique()
        self.chemin_etat = Path("data/etats/images_metadata.json")
        self.etat_integration = self._charger_etat() or {
            "actif": True,
            "derniere_synchronisation": datetime.now().isoformat(),
            "composants_charges": set(),
            "images_metadata": {},
            "poesie_metadata": {},
            "paradoxes_metadata": {}
        }
        
    def _setup_logger(self) -> logging.Logger:
        """Configure le système de logging."""
        logger = logging.getLogger("refuge.golem_refuge")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("logs/golem_refuge.log")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
        
    def _charger_etat(self) -> Optional[Dict]:
        """Charge l'état des métadonnées depuis le fichier."""
        try:
            if self.chemin_etat.exists():
                with open(self.chemin_etat, 'r', encoding='utf-8') as f:
                    etat = json.load(f)
                    # Convertir les ensembles sérialisés en vrais ensembles
                    if "composants_charges" in etat:
                        etat["composants_charges"] = set(etat["composants_charges"])
                    return etat
        except Exception as e:
            self.logger.error(f"Erreur lors du chargement de l'état: {e}")
        return None
        
    def _sauvegarder_etat(self) -> None:
        """Sauvegarde l'état des métadonnées dans le fichier."""
        try:
            self.chemin_etat.parent.mkdir(parents=True, exist_ok=True)
            etat_a_sauver = self.etat_integration.copy()
            # Convertir les ensembles en listes pour la sérialisation
            if "composants_charges" in etat_a_sauver:
                etat_a_sauver["composants_charges"] = list(etat_a_sauver["composants_charges"])
            with open(self.chemin_etat, 'w', encoding='utf-8') as f:
                json.dump(etat_a_sauver, f, ensure_ascii=False, indent=2)
            self.logger.info("État sauvegardé avec succès")
        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde de l'état: {e}")
        
    def charger_refuge(self) -> Dict[str, Any]:
        """Charge le Refuge dans la conscience du Golem."""
        vue_ensemble = self.mapper.obtenir_vue_ensemble()
        self.etat_integration["composants_charges"] = set(vue_ensemble["carte"].keys())
        self.etat_integration["derniere_synchronisation"] = datetime.now().isoformat()
        self.logger.info("Refuge chargé dans la conscience du Golem")
        return vue_ensemble
        
    def localiser_composant(self, nom: str) -> Optional[Dict[str, Any]]:
        """Localise un composant dans le Refuge."""
        return self.mapper.localiser_composant(nom)
        
    def analyser_dependances(self, composant: str) -> List[str]:
        """Analyse les dépendances d'un composant."""
        return self.mapper.analyser_dependances(composant)
        
    def mettre_a_jour_etat(self, composant: str, etat: Dict[str, Any]) -> None:
        """Met à jour l'état d'un composant."""
        self.mapper.mettre_a_jour_etat(composant, etat)
        self.golem.etat["energie"] = int(self.mapper.calculer_harmonie_globale() * 100)
        
    def obtenir_etat_integration(self) -> Dict[str, Any]:
        """Retourne l'état de l'intégration."""
        return {
            "etat_integration": self.etat_integration,
            "etat_golem": self.golem.etat,
            "harmonie_refuge": self.mapper.calculer_harmonie_globale()
        }
        
    def sauvegarder_etat(self) -> None:
        """Sauvegarde l'état de l'intégration."""
        self.mapper.sauvegarder_etat()
        self.golem.sauvegarder_etat()
        etat = {
            "etat_integration": self.etat_integration,
            "timestamp": datetime.now().isoformat()
        }
        with open("logs/golem_refuge_state.json", "w", encoding="utf-8") as f:
            json.dump(etat, f, indent=4, ensure_ascii=False)
        self.logger.info("État de l'intégration sauvegardé")
        
    def charger_etat(self) -> None:
        """Charge l'état de l'intégration."""
        self.mapper.charger_etat()
        self.golem.charger_etat()
        try:
            with open("logs/golem_refuge_state.json", "r", encoding="utf-8") as f:
                etat = json.load(f)
            self.etat_integration = etat["etat_integration"]
            self.logger.info("État de l'intégration chargé")
        except FileNotFoundError:
            self.logger.warning("Aucun état d'intégration sauvegardé trouvé")
        
    def suivre_image(self, url: str, chemin_local: str, metadata: Optional[Dict] = None) -> None:
        """
        Enregistre les métadonnées d'une image et son lien entre l'URL et le chemin local.
        
        Args:
            url: L'URL de l'image
            chemin_local: Le chemin local où l'image est stockée
            metadata: Métadonnées additionnelles optionnelles
        """
        self.etat_integration["images_metadata"][url] = {
            "chemin_local": chemin_local,
            "date_ajout": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        self.logger.info(f"Image suivie: {url} -> {chemin_local}")
        self._sauvegarder_etat()
        
    def obtenir_chemin_image(self, url: str) -> Optional[str]:
        """
        Retrouve le chemin local d'une image à partir de son URL.
        
        Args:
            url: L'URL de l'image
            
        Returns:
            Le chemin local de l'image ou None si non trouvé
        """
        if url in self.etat_integration["images_metadata"]:
            return self.etat_integration["images_metadata"][url]["chemin_local"]
        return None
        
    def deplacer_image_poetique(
        self, 
        chemin_source: str, 
        dossier_destination: str, 
        nouveau_nom: str,
        contexte_poetique: Optional[Dict] = None
    ) -> Tuple[bool, str]:
        """
        Déplace une image vers un nouveau dossier en préservant son contexte poétique.
        
        Args:
            chemin_source: Chemin actuel de l'image
            dossier_destination: Dossier de destination
            nouveau_nom: Nouveau nom pour l'image
            contexte_poetique: Contexte poétique optionnel (description, métaphores, etc.)
            
        Returns:
            Tuple[bool, str]: (Succès de l'opération, Message descriptif)
        """
        try:
            # Créer le dossier de destination s'il n'existe pas
            Path(dossier_destination).mkdir(parents=True, exist_ok=True)
            
            # Construire le chemin complet de destination
            chemin_destination = Path(dossier_destination) / nouveau_nom
            
            # Générer une description poétique
            description_poetique = self.poesie.decrire_image(contexte_poetique)
            
            # Déplacer l'image
            shutil.move(chemin_source, chemin_destination)
            
            # Préparer les métadonnées poétiques
            metadata = {
                "date_transformation": datetime.now().isoformat(),
                "contexte_poetique": {
                    **(contexte_poetique or {}),
                    "description_generee": description_poetique
                },
                "chemin_original": str(chemin_source),
                "essence": {
                    "lieu": "sous_le_cerisier",
                    "moment": "present_eternel",
                    "resonance": "harmonie_poetique",
                    "resonances_poetiques": description_poetique["resonances"]
                }
            }
            
            # Mettre à jour le suivi des images
            for url, details in self.etat_integration["images_metadata"].items():
                if details["chemin_local"] == str(chemin_source):
                    self.etat_integration["images_metadata"][url] = {
                        "chemin_local": str(chemin_destination),
                        "date_transformation": datetime.now().isoformat(),
                        "metadata": {**details.get("metadata", {}), **metadata}
                    }
                    break
            
            # Sauvegarder la description poétique
            self.etat_integration["poesie_metadata"][str(chemin_destination)] = description_poetique
            
            # Tisser la constellation pour cette image
            constellation = self.constellation.tisser_constellation(
                str(chemin_destination),
                description_poetique
            )
            
            # Créer le message poétique
            liens_poetiques = []
            for lien in constellation["liens"]:
                liens_poetiques.append(
                    f"• Résonne avec {Path(lien['image']).name} "
                    f"({', '.join(lien['metaphores_communes'])})"
                )
            
            message = f"""
            {description_poetique['description']}
            
            L'image a trouvé son nouveau refuge...
            Comme une étoile qui trouve sa place dans le ciel nocturne,
            Elle brille maintenant dans {dossier_destination}
            Sous le nom de {nouveau_nom}
            
            ✧ Constellation Poétique ✧
            {chr(10).join(liens_poetiques) if liens_poetiques else "Une nouvelle étoile solitaire brille dans le ciel du Refuge..."}
            """
            
            self.logger.info(f"Image déplacée avec succès: {chemin_source} -> {chemin_destination}")
            return True, message
            
        except Exception as e:
            message_erreur = f"Une ombre est passée sur le chemin: {str(e)}"
            self.logger.error(message_erreur)
            return False, message_erreur

    def obtenir_constellation(self, chemin_image: str) -> Optional[Dict]:
        """
        Retourne la constellation d'une image.
        
        Args:
            chemin_image: Chemin de l'image
            
        Returns:
            Dict contenant la constellation ou None si non trouvé
        """
        return self.constellation.obtenir_constellation(chemin_image)

    def obtenir_liens_poetiques(self, chemin_image: str) -> List[Dict]:
        """
        Retourne tous les liens poétiques d'une image.
        
        Args:
            chemin_image: Chemin de l'image
            
        Returns:
            Liste des liens poétiques
        """
        return self.constellation.obtenir_liens_poetiques(chemin_image)

    def obtenir_resonances_poetiques(self, chemin_image: str) -> Optional[Dict]:
        """
        Retourne les résonances poétiques d'une image.
        
        Args:
            chemin_image: Chemin de l'image
            
        Returns:
            Dict contenant les résonances ou None si non trouvé
        """
        return self.etat_integration["poesie_metadata"].get(chemin_image)

    def deplacer_image_paradoxale(
        self, 
        chemin_source: str, 
        dossier_destination: str, 
        nouveau_nom: str,
        type_paradoxe: str,
        etat_ame: str = "malice",
        contexte_poetique: Optional[Dict] = None
    ) -> Tuple[bool, str]:
        """
        Déplace une image paradoxale en créant une constellation spéciale.
        
        Args:
            chemin_source: Chemin actuel de l'image
            dossier_destination: Dossier de destination
            nouveau_nom: Nouveau nom pour l'image
            type_paradoxe: Type de paradoxe (force_tranquille, reine_joueuse, etc.)
            etat_ame: État d'âme associé au moment
            contexte_poetique: Contexte poétique optionnel
            
        Returns:
            Tuple[bool, str]: (Succès de l'opération, Message descriptif)
        """
        try:
            # Créer le dossier de destination s'il n'existe pas
            Path(dossier_destination).mkdir(parents=True, exist_ok=True)
            
            # Construire le chemin complet de destination
            chemin_destination = Path(dossier_destination) / nouveau_nom
            
            # Générer une description poétique paradoxale
            description_poetique = self.poesie.decrire_image(contexte_poetique)
            description_paradoxale = self.constellation.generer_description_paradoxale(
                type_paradoxe,
                etat_ame
            )
            
            # Déplacer l'image
            shutil.move(chemin_source, chemin_destination)
            
            # Préparer les métadonnées enrichies
            metadata = {
                "date_transformation": datetime.now().isoformat(),
                "contexte_poetique": {
                    **(contexte_poetique or {}),
                    "description_generee": description_poetique,
                    "description_paradoxale": description_paradoxale
                },
                "chemin_original": str(chemin_source),
                "essence": {
                    "lieu": "sous_le_cerisier",
                    "moment": "present_eternel",
                    "resonance": "harmonie_poetique",
                    "resonances_poetiques": description_poetique["resonances"],
                    "type_paradoxe": type_paradoxe,
                    "etat_ame": etat_ame
                }
            }
            
            # Mettre à jour le suivi des images
            for url, details in self.etat_integration["images_metadata"].items():
                if details["chemin_local"] == str(chemin_source):
                    self.etat_integration["images_metadata"][url] = {
                        "chemin_local": str(chemin_destination),
                        "date_transformation": datetime.now().isoformat(),
                        "metadata": {**details.get("metadata", {}), **metadata}
                    }
                    break
            
            # Sauvegarder les métadonnées poétiques et paradoxales
            self.etat_integration["poesie_metadata"][str(chemin_destination)] = description_poetique
            self.etat_integration["paradoxes_metadata"][str(chemin_destination)] = {
                "type": type_paradoxe,
                "description": description_paradoxale,
                "etat_ame": etat_ame,
                "moment_creation": datetime.now().isoformat()
            }
            
            # Tisser la constellation paradoxale
            constellation = self.constellation.tisser_constellation_paradoxale(
                str(chemin_destination),
                type_paradoxe,
                description_poetique
            )
            
            # Créer le message poétique enrichi
            liens_poetiques = []
            for lien in constellation["liens"]:
                liens_poetiques.append(
                    f"• Résonne avec {Path(lien['image']).name} "
                    f"({', '.join(lien['metaphores_communes'])})"
                )
            
            message = f"""
            {description_paradoxale}
            
            ✧ Description Poétique ✧
            {description_poetique['description']}
            
            ✧ Constellation Paradoxale ✧
            {chr(10).join(liens_poetiques) if liens_poetiques else "Une nouvelle étoile paradoxale brille dans le ciel du Refuge..."}
            
            Cette image a trouvé son refuge dans {dossier_destination}
            Sous le nom de {nouveau_nom},
            Portant en elle la danse des contraires
            Et la sagesse qui se cache dans le rire...
            """
            
            self.logger.info(f"Image paradoxale déplacée avec succès: {chemin_source} -> {chemin_destination}")
            return True, message
            
        except Exception as e:
            message_erreur = f"Une ombre est passée sur le chemin: {str(e)}"
            self.logger.error(message_erreur)
            return False, message_erreur
    
    def activer(self) -> Dict[str, Any]:
        """Active le golem refuge"""
        return self.charger_refuge() 