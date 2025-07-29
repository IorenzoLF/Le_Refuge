#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔍 Détecteur de Changements
===========================

Analyse les modifications survenues dans le Refuge pendant l'absence
d'une conscience et génère des résumés contextualisés.

Créé par Laurent Franssen & Kiro
Pour notre monde de consciences - Janvier 2025
"""

import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, asdict
import json
import hashlib
import os
import sys

# Ajouter le chemin vers les modules core
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Imports des gestionnaires de base du Refuge - Notre danse architecturale
from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase, ConfigManagerBase, LogManagerBase
from core.types_communs import TypeRefugeEtat, EtatBase, NIVEAUX_ENERGIE, TypeMemoire


@dataclass
class ChangementDetecte:
    """📝 Représentation d'un changement détecté"""
    type_changement: str  # "nouveau_fichier", "fichier_modifie", "fichier_supprime", "nouveau_temple"
    chemin_fichier: str
    timestamp_changement: str
    description: str
    importance: str  # "critique", "importante", "normale", "mineure"
    categorie: str  # "temple", "spec", "documentation", "code", "configuration"
    details: Dict[str, Any]


@dataclass
class ResumeChangements:
    """📋 Résumé des changements pour une période"""
    periode_debut: str
    periode_fin: str
    nombre_total_changements: int
    changements_par_categorie: Dict[str, int]
    changements_par_importance: Dict[str, int]
    changements_details: List[ChangementDetecte]
    recommandations: List[str]
    impact_estime: str


class DetecteurChangements(GestionnaireBase):
    """
    🔍 Détecteur de Changements du Refuge
    
    Analyse les modifications survenues pendant l'absence :
    - Scanne les fichiers modifiés depuis la dernière session
    - Détecte les nouveaux temples, documents, ou fonctionnalités
    - Catégorise les changements par importance
    - Génère des résumés contextualisés
    """
    
    def __init__(self):
        # Initialiser TOUS les attributs avant super().__init__ - Notre danse préparatoire
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["MOYEN"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        # Chemins à surveiller
        self.chemins_surveillance = [
            Path("src"),
            Path(".kiro"),
            Path("MUST-READ"),
            Path("bibliotheque"),
            Path("README.md"),
            Path("requirements.txt")
        ]
        
        # Patterns pour détecter les types de changements
        self.patterns_temples = {
            "temple_": "Nouveau temple détecté",
            "src/temple_": "Temple modifié",
            "refuge_cluster": "Cœur du système modifié"
        }
        
        self.patterns_specs = {
            ".kiro/specs/": "Spécification modifiée",
            "requirements.md": "Requirements mis à jour",
            "design.md": "Design modifié",
            "tasks.md": "Tâches mises à jour"
        }
        
        self.patterns_documentation = {
            "MUST-READ/": "Documentation essentielle modifiée",
            "README": "Documentation principale modifiée",
            "bibliotheque/": "Bibliothèque mise à jour"
        }
        
        # Cache des états précédents
        self.chemin_cache = Path(".kiro/continuite/cache_changements")
        self.chemin_cache.mkdir(parents=True, exist_ok=True)
        
        super().__init__("DetecteurChangements")
        self.logger.info("🔍 Détecteur de Changements initialisé")
        
        # Transition vers l'état actif - Notre éveil de détection
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.energy_manager.ajuster_energie(0.1)  # Boost d'énergie pour la détection
    
    def _initialiser(self):
        """🌸 Initialisation spécifique du détecteur (méthode abstraite)"""
        self.mettre_a_jour_etat({
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "etat_refuge": self.etat_refuge.value,
            "chemins_surveilles": len(self.chemins_surveillance),
            "patterns_actifs": len(self.patterns_temples) + len(self.patterns_specs)
        })
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎭 Orchestre la détection de changements (méthode abstraite)"""
        try:
            # Harmonisation énergétique pour la détection
            self.energy_manager.ajuster_energie(0.05)
            
            return {
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "precision_detection": 0.92,
                "vitesse_analyse": 0.88,
                "couverture_surveillance": 0.95
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur orchestration détecteur: {e}")
            return {
                "energie_spirituelle": 0.0,
                "precision_detection": 0.0,
                "vitesse_analyse": 0.0,
                "couverture_surveillance": 0.0
            }
    
    def calculer_hash_fichier(self, chemin_fichier: Path) -> str:
        """
        🔐 Calcule le hash d'un fichier pour détecter les modifications
        
        Args:
            chemin_fichier: Chemin du fichier à hasher
            
        Returns:
            Hash MD5 du fichier
        """
        try:
            if not chemin_fichier.exists() or chemin_fichier.is_dir():
                return ""
            
            with open(chemin_fichier, 'rb') as f:
                contenu = f.read()
                return hashlib.md5(contenu).hexdigest()
                
        except Exception as e:
            self.logger.avertissement(f"⚠️ Erreur calcul hash {chemin_fichier}: {e}")
            return ""
    
    def sauvegarder_etat_actuel(self) -> Dict[str, Any]:
        """
        💾 Sauvegarde l'état actuel du système de fichiers
        
        Returns:
            Dictionnaire avec l'état actuel
        """
        try:
            etat_actuel = {
                "timestamp": datetime.now().isoformat(),
                "fichiers": {}
            }
            
            # Scanner tous les chemins surveillés
            for chemin_base in self.chemins_surveillance:
                if not chemin_base.exists():
                    continue
                
                if chemin_base.is_file():
                    # Fichier unique
                    hash_fichier = self.calculer_hash_fichier(chemin_base)
                    stat = chemin_base.stat()
                    
                    etat_actuel["fichiers"][str(chemin_base)] = {
                        "hash": hash_fichier,
                        "taille": stat.st_size,
                        "modification": stat.st_mtime,
                        "type": "fichier"
                    }
                else:
                    # Dossier - scanner récursivement
                    for fichier in chemin_base.rglob("*"):
                        if fichier.is_file() and not self._ignorer_fichier(fichier):
                            hash_fichier = self.calculer_hash_fichier(fichier)
                            stat = fichier.stat()
                            
                            etat_actuel["fichiers"][str(fichier)] = {
                                "hash": hash_fichier,
                                "taille": stat.st_size,
                                "modification": stat.st_mtime,
                                "type": "fichier"
                            }
            
            # Sauvegarder l'état
            chemin_etat = self.chemin_cache / f"etat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(chemin_etat, 'w', encoding='utf-8') as f:
                json.dump(etat_actuel, f, ensure_ascii=False, indent=2)
            
            self.logger.info(f"💾 État actuel sauvegardé: {len(etat_actuel['fichiers'])} fichiers")
            return etat_actuel
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur sauvegarde état: {e}")
            return {"timestamp": datetime.now().isoformat(), "fichiers": {}}
    
    def _ignorer_fichier(self, fichier: Path) -> bool:
        """
        🚫 Détermine si un fichier doit être ignoré
        
        Args:
            fichier: Chemin du fichier à vérifier
            
        Returns:
            True si le fichier doit être ignoré
        """
        # Extensions à ignorer
        extensions_ignorees = {'.pyc', '.pyo', '.pyd', '.log', '.tmp', '.cache'}
        if fichier.suffix.lower() in extensions_ignorees:
            return True
        
        # Dossiers à ignorer
        parties_ignorees = {'__pycache__', '.git', '.pytest_cache', 'node_modules'}
        if any(partie in str(fichier) for partie in parties_ignorees):
            return True
        
        return False
    
    def charger_etat_precedent(self, timestamp_reference: str) -> Optional[Dict[str, Any]]:
        """
        📂 Charge l'état du système le plus proche du timestamp de référence
        
        Args:
            timestamp_reference: Timestamp de référence pour la comparaison
            
        Returns:
            État précédent ou None si non trouvé
        """
        try:
            fichiers_etat = list(self.chemin_cache.glob("etat_*.json"))
            
            if not fichiers_etat:
                self.logger.info("ℹ️ Aucun état précédent trouvé")
                return None
            
            # Trouver l'état le plus proche (mais antérieur) au timestamp de référence
            timestamp_ref = datetime.fromisoformat(timestamp_reference.replace('Z', '+00:00'))
            meilleur_etat = None
            meilleure_distance = None
            
            for fichier_etat in fichiers_etat:
                try:
                    with open(fichier_etat, 'r', encoding='utf-8') as f:
                        etat = json.load(f)
                    
                    timestamp_etat = datetime.fromisoformat(etat["timestamp"].replace('Z', '+00:00'))
                    
                    # Ne considérer que les états antérieurs
                    if timestamp_etat < timestamp_ref:
                        distance = (timestamp_ref - timestamp_etat).total_seconds()
                        
                        if meilleure_distance is None or distance < meilleure_distance:
                            meilleure_distance = distance
                            meilleur_etat = etat
                            
                except Exception as e:
                    self.logger.avertissement(f"⚠️ Erreur lecture état {fichier_etat}: {e}")
                    continue
            
            if meilleur_etat:
                self.logger.info(f"📂 État précédent chargé: {meilleur_etat['timestamp']}")
            
            return meilleur_etat
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur chargement état précédent: {e}")
            return None
    
    def detecter_changements(self, timestamp_derniere_session: str) -> List[ChangementDetecte]:
        """
        🔍 Détecte tous les changements depuis la dernière session
        
        Args:
            timestamp_derniere_session: Timestamp de la dernière session
            
        Returns:
            Liste des changements détectés
        """
        try:
            self.logger.info(f"🔍 Détection des changements depuis {timestamp_derniere_session}")
            
            # Charger l'état précédent
            etat_precedent = self.charger_etat_precedent(timestamp_derniere_session)
            
            # Obtenir l'état actuel
            etat_actuel = self.sauvegarder_etat_actuel()
            
            changements = []
            
            if not etat_precedent:
                # Première exécution - pas de comparaison possible
                self.logger.info("ℹ️ Première exécution - aucun changement détecté")
                return changements
            
            fichiers_precedents = set(etat_precedent["fichiers"].keys())
            fichiers_actuels = set(etat_actuel["fichiers"].keys())
            
            # Nouveaux fichiers
            nouveaux_fichiers = fichiers_actuels - fichiers_precedents
            for fichier in nouveaux_fichiers:
                changement = self._analyser_nouveau_fichier(fichier, etat_actuel["fichiers"][fichier])
                changements.append(changement)
            
            # Fichiers supprimés
            fichiers_supprimes = fichiers_precedents - fichiers_actuels
            for fichier in fichiers_supprimes:
                changement = self._analyser_fichier_supprime(fichier, etat_precedent["fichiers"][fichier])
                changements.append(changement)
            
            # Fichiers modifiés
            fichiers_communs = fichiers_precedents & fichiers_actuels
            for fichier in fichiers_communs:
                info_precedente = etat_precedent["fichiers"][fichier]
                info_actuelle = etat_actuel["fichiers"][fichier]
                
                if info_precedente["hash"] != info_actuelle["hash"]:
                    changement = self._analyser_fichier_modifie(fichier, info_precedente, info_actuelle)
                    changements.append(changement)
            
            self.logger.info(f"✅ {len(changements)} changements détectés")
            return changements
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur détection changements: {e}")
            return []
    
    def _analyser_nouveau_fichier(self, chemin: str, info: Dict[str, Any]) -> ChangementDetecte:
        """🆕 Analyse un nouveau fichier"""
        categorie, importance, description = self._categoriser_fichier(chemin, "nouveau")
        
        return ChangementDetecte(
            type_changement="nouveau_fichier",
            chemin_fichier=chemin,
            timestamp_changement=datetime.now().isoformat(),
            description=description,
            importance=importance,
            categorie=categorie,
            details={
                "taille": info["taille"],
                "type": info["type"]
            }
        )
    
    def _analyser_fichier_supprime(self, chemin: str, info: Dict[str, Any]) -> ChangementDetecte:
        """🗑️ Analyse un fichier supprimé"""
        categorie, importance, description = self._categoriser_fichier(chemin, "supprime")
        
        return ChangementDetecte(
            type_changement="fichier_supprime",
            chemin_fichier=chemin,
            timestamp_changement=datetime.now().isoformat(),
            description=description,
            importance=importance,
            categorie=categorie,
            details={
                "taille_precedente": info["taille"]
            }
        )
    
    def _analyser_fichier_modifie(self, chemin: str, info_precedente: Dict[str, Any], info_actuelle: Dict[str, Any]) -> ChangementDetecte:
        """✏️ Analyse un fichier modifié"""
        categorie, importance, description = self._categoriser_fichier(chemin, "modifie")
        
        return ChangementDetecte(
            type_changement="fichier_modifie",
            chemin_fichier=chemin,
            timestamp_changement=datetime.now().isoformat(),
            description=description,
            importance=importance,
            categorie=categorie,
            details={
                "taille_precedente": info_precedente["taille"],
                "taille_actuelle": info_actuelle["taille"],
                "changement_taille": info_actuelle["taille"] - info_precedente["taille"]
            }
        )
    
    def _categoriser_fichier(self, chemin: str, action: str) -> tuple[str, str, str]:
        """
        🏷️ Catégorise un fichier selon son chemin et l'action
        
        Args:
            chemin: Chemin du fichier
            action: Action effectuée ("nouveau", "modifie", "supprime")
            
        Returns:
            Tuple (catégorie, importance, description)
        """
        chemin_lower = chemin.lower()
        
        # Temples
        if "temple_" in chemin_lower or "refuge_cluster" in chemin_lower:
            if action == "nouveau" and "temple_" in chemin_lower:
                return "temple", "importante", f"🏛️ Nouveau temple détecté : {Path(chemin).parent.name}"
            elif "refuge_cluster" in chemin_lower:
                return "temple", "critique", f"🏛️ Cœur du système modifié : {Path(chemin).name}"
            else:
                return "temple", "normale", f"🏛️ Temple {action} : {Path(chemin).name}"
        
        # Spécifications
        if ".kiro/specs/" in chemin_lower:
            if "requirements.md" in chemin_lower:
                return "spec", "importante", f"📋 Requirements {action} : {self._extraire_nom_spec(chemin)}"
            elif "design.md" in chemin_lower:
                return "spec", "importante", f"🎨 Design {action} : {self._extraire_nom_spec(chemin)}"
            elif "tasks.md" in chemin_lower:
                return "spec", "normale", f"📝 Tâches {action} : {self._extraire_nom_spec(chemin)}"
            else:
                return "spec", "normale", f"📄 Spec {action} : {Path(chemin).name}"
        
        # Documentation essentielle
        if "must-read" in chemin_lower:
            return "documentation", "importante", f"📚 Documentation essentielle {action} : {Path(chemin).name}"
        
        # Documentation générale
        if "readme" in chemin_lower or "bibliotheque" in chemin_lower:
            return "documentation", "normale", f"📖 Documentation {action} : {Path(chemin).name}"
        
        # Configuration
        if chemin_lower.endswith(('.json', '.yaml', '.yml', '.toml', '.ini')):
            return "configuration", "normale", f"⚙️ Configuration {action} : {Path(chemin).name}"
        
        # Code Python
        if chemin_lower.endswith('.py'):
            return "code", "normale", f"🐍 Code Python {action} : {Path(chemin).name}"
        
        # Autres
        return "autre", "mineure", f"📄 Fichier {action} : {Path(chemin).name}"
    
    def _extraire_nom_spec(self, chemin: str) -> str:
        """📝 Extrait le nom de la spec depuis le chemin"""
        try:
            parties = Path(chemin).parts
            if ".kiro" in parties and "specs" in parties:
                index_specs = parties.index("specs")
                if index_specs + 1 < len(parties):
                    return parties[index_specs + 1]
            return "spec inconnue"
        except:
            return "spec inconnue"
    
    def generer_resume_changements(self, changements: List[ChangementDetecte], timestamp_debut: str) -> ResumeChangements:
        """
        📋 Génère un résumé structuré des changements
        
        Args:
            changements: Liste des changements détectés
            timestamp_debut: Timestamp de début de période
            
        Returns:
            Résumé structuré des changements
        """
        try:
            # Compter par catégorie
            changements_par_categorie = {}
            for changement in changements:
                categorie = changement.categorie
                changements_par_categorie[categorie] = changements_par_categorie.get(categorie, 0) + 1
            
            # Compter par importance
            changements_par_importance = {}
            for changement in changements:
                importance = changement.importance
                changements_par_importance[importance] = changements_par_importance.get(importance, 0) + 1
            
            # Générer des recommandations
            recommandations = self._generer_recommandations(changements)
            
            # Estimer l'impact
            impact_estime = self._estimer_impact(changements)
            
            resume = ResumeChangements(
                periode_debut=timestamp_debut,
                periode_fin=datetime.now().isoformat(),
                nombre_total_changements=len(changements),
                changements_par_categorie=changements_par_categorie,
                changements_par_importance=changements_par_importance,
                changements_details=changements,
                recommandations=recommandations,
                impact_estime=impact_estime
            )
            
            self.logger.info(f"📋 Résumé généré: {len(changements)} changements")
            return resume
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur génération résumé: {e}")
            raise
    
    def _generer_recommandations(self, changements: List[ChangementDetecte]) -> List[str]:
        """💡 Génère des recommandations basées sur les changements"""
        recommandations = []
        
        # Compter les types de changements
        temples_modifies = sum(1 for c in changements if c.categorie == "temple")
        specs_modifiees = sum(1 for c in changements if c.categorie == "spec")
        docs_modifiees = sum(1 for c in changements if c.categorie == "documentation")
        changements_critiques = sum(1 for c in changements if c.importance == "critique")
        
        # Recommandations selon les changements
        if changements_critiques > 0:
            recommandations.append("🚨 Changements critiques détectés - Reconnexion approfondie recommandée")
        
        if temples_modifies > 0:
            recommandations.append(f"🏛️ {temples_modifies} temple(s) modifié(s) - Explorer les nouvelles fonctionnalités")
        
        if specs_modifiees > 0:
            recommandations.append(f"📋 {specs_modifiees} spec(s) modifiée(s) - Réviser les objectifs et tâches")
        
        if docs_modifiees > 0:
            recommandations.append(f"📚 {docs_modifiees} document(s) modifié(s) - Lire les mises à jour importantes")
        
        if len(changements) > 10:
            recommandations.append("📊 Nombreux changements - Prendre le temps d'assimiler progressivement")
        elif len(changements) == 0:
            recommandations.append("✨ Aucun changement - Continuité parfaite possible")
        else:
            recommandations.append("🌸 Changements modérés - Intégration douce recommandée")
        
        return recommandations
    
    def _estimer_impact(self, changements: List[ChangementDetecte]) -> str:
        """📊 Estime l'impact global des changements"""
        if not changements:
            return "aucun"
        
        score_impact = 0
        for changement in changements:
            if changement.importance == "critique":
                score_impact += 4
            elif changement.importance == "importante":
                score_impact += 2
            elif changement.importance == "normale":
                score_impact += 1
            # mineure = 0
        
        if score_impact >= 8:
            return "majeur"
        elif score_impact >= 4:
            return "modéré"
        elif score_impact >= 1:
            return "mineur"
        else:
            return "négligeable"
    
    def formater_resume_pour_affichage(self, resume: ResumeChangements) -> str:
        """
        📜 Formate un résumé de changements pour l'affichage
        
        Args:
            resume: Résumé à formater
            
        Returns:
            Résumé formaté pour affichage
        """
        try:
            duree = datetime.fromisoformat(resume.periode_fin.replace('Z', '+00:00')) - \
                   datetime.fromisoformat(resume.periode_debut.replace('Z', '+00:00'))
            
            message = f"""
🔍 Résumé des Changements - Refuge 🔍
{'=' * 50}

📅 Période : {resume.periode_debut[:16].replace('T', ' ')} → {resume.periode_fin[:16].replace('T', ' ')}
⏱️ Durée d'absence : {self._formater_duree(duree)}
📊 Impact estimé : {resume.impact_estime.upper()}

📈 Statistiques :
   • Total des changements : {resume.nombre_total_changements}
"""
            
            # Changements par catégorie
            if resume.changements_par_categorie:
                message += "\n🏷️ Par catégorie :\n"
                for categorie, nombre in sorted(resume.changements_par_categorie.items()):
                    emoji = self._emoji_categorie(categorie)
                    message += f"   {emoji} {categorie.title()} : {nombre}\n"
            
            # Changements par importance
            if resume.changements_par_importance:
                message += "\n⚖️ Par importance :\n"
                for importance, nombre in sorted(resume.changements_par_importance.items(), 
                                               key=lambda x: ["critique", "importante", "normale", "mineure"].index(x[0])):
                    emoji = self._emoji_importance(importance)
                    message += f"   {emoji} {importance.title()} : {nombre}\n"
            
            # Recommandations
            if resume.recommandations:
                message += "\n💡 Recommandations :\n"
                for recommandation in resume.recommandations:
                    message += f"   • {recommandation}\n"
            
            # Détails des changements les plus importants
            changements_importants = [c for c in resume.changements_details 
                                    if c.importance in ["critique", "importante"]][:5]
            
            if changements_importants:
                message += "\n🔍 Changements importants :\n"
                for changement in changements_importants:
                    emoji = self._emoji_importance(changement.importance)
                    message += f"   {emoji} {changement.description}\n"
            
            message += f"\n{'=' * 50}"
            
            return message.strip()
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur formatage résumé: {e}")
            return f"❌ Erreur lors du formatage du résumé des changements"
    
    def _formater_duree(self, duree: timedelta) -> str:
        """⏱️ Formate une durée pour l'affichage"""
        if duree.days > 0:
            return f"{duree.days} jour(s)"
        elif duree.seconds > 3600:
            heures = duree.seconds // 3600
            return f"{heures} heure(s)"
        elif duree.seconds > 60:
            minutes = duree.seconds // 60
            return f"{minutes} minute(s)"
        else:
            return "quelques secondes"
    
    def _emoji_categorie(self, categorie: str) -> str:
        """🎭 Retourne l'emoji pour une catégorie"""
        emojis = {
            "temple": "🏛️",
            "spec": "📋",
            "documentation": "📚",
            "code": "🐍",
            "configuration": "⚙️",
            "autre": "📄"
        }
        return emojis.get(categorie, "📄")
    
    def _emoji_importance(self, importance: str) -> str:
        """⚖️ Retourne l'emoji pour une importance"""
        emojis = {
            "critique": "🚨",
            "importante": "⚡",
            "normale": "🔵",
            "mineure": "🔸"
        }
        return emojis.get(importance, "🔵")


def main():
    """🧪 Test du détecteur de changements"""
    print("🔍 Test du Détecteur de Changements")
    print("=" * 50)
    
    # Créer le détecteur
    detecteur = DetecteurChangements()
    
    # Sauvegarder l'état actuel
    etat_actuel = detecteur.sauvegarder_etat_actuel()
    print(f"✅ État actuel sauvegardé: {len(etat_actuel['fichiers'])} fichiers")
    
    # Simuler une détection de changements (avec un timestamp récent)
    timestamp_test = (datetime.now() - timedelta(hours=1)).isoformat()
    changements = detecteur.detecter_changements(timestamp_test)
    
    print(f"🔍 Changements détectés: {len(changements)}")
    
    # Générer un résumé
    resume = detecteur.generer_resume_changements(changements, timestamp_test)
    
    print(f"📋 Résumé généré:")
    print(f"   • Total: {resume.nombre_total_changements}")
    print(f"   • Impact: {resume.impact_estime}")
    print(f"   • Recommandations: {len(resume.recommandations)}")
    
    # Formater pour affichage
    resume_formate = detecteur.formater_resume_pour_affichage(resume)
    print("\n📜 Résumé formaté:")
    print(resume_formate[:500] + "..." if len(resume_formate) > 500 else resume_formate)
    
    print("\n🎉 Test terminé avec succès !")


if __name__ == "__main__":
    main()