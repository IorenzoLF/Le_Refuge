"""
Module de sauvegarde automatique du refuge.
Assure la pérennité des données et de l'état du refuge.
"""

import os
import json
import shutil
import logging
from datetime import datetime
from pathlib import Path
import schedule
import time
import threading
import hashlib

logger = logging.getLogger('refuge.sauvegarde')

class GestionnaireSauvegarde:
    """Gère les sauvegardes automatiques du refuge."""
    
    def __init__(self, chemin_refuge: str = "refuge", chemin_sauvegardes: str = "refuge/sauvegardes"):
        self.chemin_refuge = Path(chemin_refuge)
        self.chemin_sauvegardes = Path(chemin_sauvegardes)
        self.derniere_sauvegarde = None
        self.thread_sauvegarde = None
        self.actif = False
        
        # Création du répertoire de sauvegardes s'il n'existe pas
        self.chemin_sauvegardes.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Gestionnaire de sauvegarde initialisé pour {self.chemin_refuge}")
        
    def sauvegarder(self):
        """Effectue une sauvegarde complète du refuge."""
        try:
            # Création d'un nom de sauvegarde avec timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_sauvegarde = f"sauvegarde_{timestamp}"
            chemin_sauvegarde = self.chemin_sauvegardes / nom_sauvegarde
            
            # Création du répertoire de sauvegarde
            chemin_sauvegarde.mkdir(parents=True, exist_ok=True)
            
            # Sauvegarde des fichiers
            self._sauvegarder_fichiers(chemin_sauvegarde)
            
            # Sauvegarde de l'état
            self._sauvegarder_etat(chemin_sauvegarde)
            
            # Création d'un fichier de métadonnées
            self._creer_metadata(chemin_sauvegarde, nom_sauvegarde)
            
            # Mise à jour de la dernière sauvegarde
            self.derniere_sauvegarde = timestamp
            
            logger.info(f"Sauvegarde complétée avec succès: {nom_sauvegarde}")
            return True
            
        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde: {str(e)}")
            return False
            
    def _sauvegarder_fichiers(self, chemin_sauvegarde: Path):
        """Sauvegarde les fichiers du refuge."""
        # Copie récursive des fichiers
        for item in self.chemin_refuge.glob("**/*"):
            if item.is_file() and not str(item).startswith(str(self.chemin_sauvegardes)):
                # Calcul du chemin relatif
                chemin_relatif = item.relative_to(self.chemin_refuge)
                chemin_destination = chemin_sauvegarde / chemin_relatif
                
                # Création des répertoires parents si nécessaire
                chemin_destination.parent.mkdir(parents=True, exist_ok=True)
                
                # Copie du fichier
                shutil.copy2(item, chemin_destination)
                
    def _sauvegarder_etat(self, chemin_sauvegarde: Path):
        """Sauvegarde l'état du refuge."""
        # Sauvegarde de l'état principal
        if (self.chemin_refuge / "etat.json").exists():
            shutil.copy2(self.chemin_refuge / "etat.json", chemin_sauvegarde / "etat.json")
            
        # Sauvegarde des autres fichiers d'état
        for fichier_etat in self.chemin_refuge.glob("**/etat_*.json"):
            chemin_relatif = fichier_etat.relative_to(self.chemin_refuge)
            chemin_destination = chemin_sauvegarde / chemin_relatif
            chemin_destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(fichier_etat, chemin_destination)
            
    def _creer_metadata(self, chemin_sauvegarde: Path, nom_sauvegarde: str):
        """Crée un fichier de métadonnées pour la sauvegarde."""
        metadata = {
            "nom": nom_sauvegarde,
            "date_creation": datetime.now().isoformat(),
            "chemin_refuge": str(self.chemin_refuge),
            "fichiers": [],
            "hash": {}
        }
        
        # Calcul des hashes et liste des fichiers
        for item in chemin_sauvegarde.glob("**/*"):
            if item.is_file():
                chemin_relatif = item.relative_to(chemin_sauvegarde)
                metadata["fichiers"].append(str(chemin_relatif))
                
                # Calcul du hash
                with open(item, "rb") as f:
                    contenu = f.read()
                    metadata["hash"][str(chemin_relatif)] = hashlib.sha256(contenu).hexdigest()
                    
        # Sauvegarde des métadonnées
        with open(chemin_sauvegarde / "metadata.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
            
    def restaurer(self, nom_sauvegarde: str) -> bool:
        """Restaure le refuge à partir d'une sauvegarde."""
        try:
            chemin_sauvegarde = self.chemin_sauvegardes / nom_sauvegarde
            
            if not chemin_sauvegarde.exists():
                logger.error(f"Sauvegarde introuvable: {nom_sauvegarde}")
                return False
                
            # Vérification des métadonnées
            if not (chemin_sauvegarde / "metadata.json").exists():
                logger.error(f"Métadonnées introuvables pour la sauvegarde: {nom_sauvegarde}")
                return False
                
            # Lecture des métadonnées
            with open(chemin_sauvegarde / "metadata.json", "r", encoding="utf-8") as f:
                metadata = json.load(f)
                
            # Restauration des fichiers
            for fichier in metadata["fichiers"]:
                chemin_source = chemin_sauvegarde / fichier
                chemin_destination = self.chemin_refuge / fichier
                
                # Création des répertoires parents si nécessaire
                chemin_destination.parent.mkdir(parents=True, exist_ok=True)
                
                # Copie du fichier
                shutil.copy2(chemin_source, chemin_destination)
                
            logger.info(f"Restauration complétée avec succès depuis: {nom_sauvegarde}")
            return True
            
        except Exception as e:
            logger.error(f"Erreur lors de la restauration: {str(e)}")
            return False
            
    def lister_sauvegardes(self) -> list:
        """Liste toutes les sauvegardes disponibles."""
        sauvegardes = []
        
        for item in self.chemin_sauvegardes.glob("sauvegarde_*"):
            if item.is_dir() and (item / "metadata.json").exists():
                try:
                    with open(item / "metadata.json", "r", encoding="utf-8") as f:
                        metadata = json.load(f)
                        sauvegardes.append({
                            "nom": metadata["nom"],
                            "date": metadata["date_creation"]
                        })
                except:
                    pass
                    
        return sorted(sauvegardes, key=lambda x: x["date"], reverse=True)
        
    def demarrer_sauvegardes_automatiques(self, intervalle: int = 3600):
        """Démarre les sauvegardes automatiques à intervalles réguliers."""
        if self.actif:
            logger.warning("Les sauvegardes automatiques sont déjà actives")
            return
            
        self.actif = True
        
        # Planification des sauvegardes
        schedule.every(intervalle).seconds.do(self.sauvegarder)
        
        # Démarrage du thread de sauvegarde
        self.thread_sauvegarde = threading.Thread(target=self._executer_sauvegardes)
        self.thread_sauvegarde.daemon = True
        self.thread_sauvegarde.start()
        
        logger.info(f"Sauvegardes automatiques démarrées (intervalle: {intervalle} secondes)")
        
    def _executer_sauvegardes(self):
        """Exécute les sauvegardes planifiées."""
        while self.actif:
            schedule.run_pending()
            time.sleep(1)
            
    def arreter_sauvegardes_automatiques(self):
        """Arrête les sauvegardes automatiques."""
        if not self.actif:
            logger.warning("Les sauvegardes automatiques ne sont pas actives")
            return
            
        self.actif = False
        
        if self.thread_sauvegarde:
            self.thread_sauvegarde.join(timeout=5)
            
        logger.info("Sauvegardes automatiques arrêtées")
        
    def nettoyer_sauvegardes(self, nombre_max: int = 10):
        """Nettoie les anciennes sauvegardes, en gardant seulement les plus récentes."""
        sauvegardes = self.lister_sauvegardes()
        
        if len(sauvegardes) <= nombre_max:
            logger.info(f"Pas besoin de nettoyage, seulement {len(sauvegardes)} sauvegardes existent")
            return
            
        # Suppression des sauvegardes les plus anciennes
        for sauvegarde in sauvegardes[nombre_max:]:
            chemin_sauvegarde = self.chemin_sauvegardes / sauvegarde["nom"]
            try:
                shutil.rmtree(chemin_sauvegarde)
                logger.info(f"Sauvegarde supprimée: {sauvegarde['nom']}")
            except Exception as e:
                logger.error(f"Erreur lors de la suppression de {sauvegarde['nom']}: {str(e)}")
                
        logger.info(f"Nettoyage terminé, {nombre_max} sauvegardes conservées") 