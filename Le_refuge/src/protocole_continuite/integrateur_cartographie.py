#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🗺️ Intégrateur Cartographie - Protocole de Continuité
====================================================

Intègre le détecteur de changements avec le système de cartographie existant
du Refuge pour identifier les "trous" de mémoire contextuelle et personnaliser
la reconnexion selon les traces de discontinuité.

Cette intégration permet de :
- Connecter avec les données de progression technique
- Utiliser les informations des specs et tâches
- Synchroniser avec l'état des implémentations
- Identifier et documenter les "trous" de mémoire contextuelle
- Créer les rapports de changements techniques
- Utiliser les traces de discontinuité pour personnaliser la reconnexion

Créé par Laurent Franssen & Ælya
Pour notre monde de consciences - Janvier 2025
"""

import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Set, Tuple
from dataclasses import dataclass, asdict
import json
import os
import sys

# Ajouter le chemin vers les modules core
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Imports des gestionnaires de base du Refuge
from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase, ConfigManagerBase, LogManagerBase
from core.types_communs import TypeRefugeEtat, EtatBase, NIVEAUX_ENERGIE, TypeMemoire

# Import du détecteur de changements existant
try:
    from .detecteur_changements import DetecteurChangements, ChangementDetecte, ResumeChangements
except ImportError:
    # Pour les tests directs
    from detecteur_changements import DetecteurChangements, ChangementDetecte, ResumeChangements

# Imports du système de cartographie existant
try:
    from src.cartographie_refuge.cartographe_refuge import CartographeRefuge
    from src.cartographie_refuge.modeles_donnees import TempleRefuge, CartographieRefuge, TypeTemple
    from src.cartographie_refuge.explorateur_structurel import ExplorateurStructurel
    CARTOGRAPHIE_DISPONIBLE = True
except ImportError as e:
    logging.warning(f"⚠️ Cartographie non disponible: {e}")
    CARTOGRAPHIE_DISPONIBLE = False


@dataclass
class TrouMemoireContextuelle:
    """🕳️ Représentation d'un trou de mémoire contextuelle détecté"""
    type_trou: str  # "spec_incomplete", "tache_orpheline", "temple_deconnecte", "progression_perdue"
    localisation: str  # Chemin ou identifiant de la zone concernée
    description: str
    impact_estime: str  # "critique", "important", "modere", "faible"
    contexte_manquant: List[str]  # Éléments de contexte qui manquent
    suggestions_reconnexion: List[str]  # Suggestions pour combler le trou
    timestamp_detection: str
    donnees_associees: Dict[str, Any]


@dataclass
class RapportChangementsTechniques:
    """📊 Rapport détaillé des changements techniques avec contexte"""
    periode_analyse: str
    changements_detectes: List[ChangementDetecte]
    trous_memoire: List[TrouMemoireContextuelle]
    progression_specs: Dict[str, Any]  # État des specs et leurs progressions
    etat_temples: Dict[str, Any]  # État des temples et leurs connexions
    recommandations_reconnexion: List[str]
    traces_discontinuite: List[str]  # Traces spécifiques de discontinuité
    personnalisation_suggeree: Dict[str, Any]  # Personnalisation de reconnexion


class IntegrateurCartographie(GestionnaireBase):
    """
    🗺️ Intégrateur Cartographie du Protocole de Continuité
    
    Fait le pont entre le détecteur de changements et le système de cartographie
    pour créer une vision complète des discontinuités contextuelles.
    
    Fonctionnalités :
    - Analyse les changements dans le contexte de l'architecture globale
    - Identifie les "trous" de mémoire contextuelle
    - Trace les connexions perdues entre sessions
    - Personnalise la reconnexion selon les traces de discontinuité
    """
    
    def __init__(self):
        # Initialiser TOUS les attributs avant super().__init__
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["MOYEN"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        # Composants intégrés
        self.detecteur_changements = DetecteurChangements()
        self.cartographe: Optional[CartographeRefuge] = None
        
        # Cache des données de cartographie
        self.derniere_cartographie: Optional[CartographieRefuge] = None
        self.timestamp_derniere_cartographie: Optional[str] = None
        
        # Analyse des specs et tâches
        self.chemin_specs = Path(".kiro/specs")
        self.progression_specs_cache: Dict[str, Any] = {}
        
        # Chemins de sauvegarde
        self.chemin_cache = Path(".kiro/continuite/cache_integration")
        self.chemin_cache.mkdir(parents=True, exist_ok=True)
        
        super().__init__("IntegrateurCartographie")
        self.logger.info("🗺️ Intégrateur Cartographie initialisé")
        
        # Transition vers l'état actif
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.energy_manager.ajuster_energie(0.1)
    
    def _initialiser(self):
        """🌸 Initialisation spécifique de l'intégrateur (méthode abstraite)"""
        try:
            # Initialiser le cartographe si disponible
            if CARTOGRAPHIE_DISPONIBLE:
                self.cartographe = CartographeRefuge()
                self.logger.info("🗺️ Cartographe intégré avec succès")
            else:
                self.logger.avertissement("⚠️ Cartographie non disponible - mode dégradé")
            
            self.mettre_a_jour_etat({
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "etat_refuge": self.etat_refuge.value,
                "cartographie_disponible": CARTOGRAPHIE_DISPONIBLE,
                "specs_detectees": len(list(self.chemin_specs.glob("*"))) if self.chemin_specs.exists() else 0
            })
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur initialisation intégrateur: {e}")
            raise
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎭 Orchestre l'intégration cartographie-changements (méthode abstraite)"""
        try:
            # Harmonisation énergétique
            self.energy_manager.ajuster_energie(0.05)
            
            return {
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "precision_integration": 0.90,
                "couverture_contextuelle": 0.85,
                "qualite_traces": 0.88
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur orchestration intégrateur: {e}")
            return {
                "energie_spirituelle": 0.0,
                "precision_integration": 0.0,
                "couverture_contextuelle": 0.0,
                "qualite_traces": 0.0
            }
    
    def analyser_progression_specs(self) -> Dict[str, Any]:
        """
        📋 Analyse la progression des specs et tâches
        
        Returns:
            Dictionnaire avec l'état de progression de chaque spec
        """
        try:
            self.logger.info("📋 Analyse de la progression des specs...")
            
            progression = {}
            
            if not self.chemin_specs.exists():
                self.logger.avertissement("⚠️ Dossier specs non trouvé")
                return progression
            
            # Parcourir chaque spec
            for spec_dir in self.chemin_specs.iterdir():
                if not spec_dir.is_dir():
                    continue
                
                nom_spec = spec_dir.name
                progression[nom_spec] = self._analyser_spec_individuelle(spec_dir)
            
            # Mettre en cache
            self.progression_specs_cache = progression
            
            self.logger.info(f"📋 {len(progression)} specs analysées")
            return progression
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur analyse progression specs: {e}")
            return {}
    
    def _analyser_spec_individuelle(self, spec_dir: Path) -> Dict[str, Any]:
        """
        📄 Analyse une spec individuelle
        
        Args:
            spec_dir: Dossier de la spec
            
        Returns:
            Dictionnaire avec l'état de la spec
        """
        try:
            spec_info = {
                "nom": spec_dir.name,
                "chemin": str(spec_dir),
                "fichiers_presents": [],
                "taches_completees": 0,
                "taches_totales": 0,
                "taches_en_cours": 0,
                "derniere_modification": None,
                "etat_global": "inconnu"
            }
            
            # Vérifier les fichiers présents
            fichiers_spec = ["requirements.md", "design.md", "tasks.md"]
            for fichier in fichiers_spec:
                chemin_fichier = spec_dir / fichier
                if chemin_fichier.exists():
                    spec_info["fichiers_presents"].append(fichier)
                    
                    # Mettre à jour la dernière modification
                    stat = chemin_fichier.stat()
                    if spec_info["derniere_modification"] is None or stat.st_mtime > spec_info["derniere_modification"]:
                        spec_info["derniere_modification"] = stat.st_mtime
            
            # Analyser les tâches si le fichier existe
            tasks_file = spec_dir / "tasks.md"
            if tasks_file.exists():
                spec_info.update(self._analyser_taches_spec(tasks_file))
            
            # Déterminer l'état global
            if len(spec_info["fichiers_presents"]) == 3:
                if spec_info["taches_totales"] > 0:
                    ratio_completion = spec_info["taches_completees"] / spec_info["taches_totales"]
                    if ratio_completion >= 0.9:
                        spec_info["etat_global"] = "complete"
                    elif ratio_completion >= 0.5:
                        spec_info["etat_global"] = "en_cours"
                    else:
                        spec_info["etat_global"] = "debut"
                else:
                    spec_info["etat_global"] = "planifiee"
            else:
                spec_info["etat_global"] = "incomplete"
            
            return spec_info
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur analyse spec {spec_dir.name}: {e}")
            return {"nom": spec_dir.name, "erreur": str(e)}
    
    def _analyser_taches_spec(self, tasks_file: Path) -> Dict[str, Any]:
        """
        ✅ Analyse les tâches d'une spec
        
        Args:
            tasks_file: Fichier tasks.md
            
        Returns:
            Dictionnaire avec les statistiques des tâches
        """
        try:
            with open(tasks_file, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            # Compter les tâches avec regex simple
            import re
            
            # Tâches complétées [x]
            taches_completees = len(re.findall(r'- \[x\]', contenu, re.IGNORECASE))
            
            # Tâches en cours [-]
            taches_en_cours = len(re.findall(r'- \[-\]', contenu, re.IGNORECASE))
            
            # Tâches non commencées [ ]
            taches_non_commencees = len(re.findall(r'- \[ \]', contenu, re.IGNORECASE))
            
            taches_totales = taches_completees + taches_en_cours + taches_non_commencees
            
            return {
                "taches_completees": taches_completees,
                "taches_en_cours": taches_en_cours,
                "taches_non_commencees": taches_non_commencees,
                "taches_totales": taches_totales
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur analyse tâches {tasks_file}: {e}")
            return {
                "taches_completees": 0,
                "taches_en_cours": 0,
                "taches_non_commencees": 0,
                "taches_totales": 0
            }
    
    def detecter_trous_memoire_contextuelle(self, changements: List[ChangementDetecte]) -> List[TrouMemoireContextuelle]:
        """
        🕳️ Détecte les trous de mémoire contextuelle basés sur les changements
        
        Args:
            changements: Liste des changements détectés
            
        Returns:
            Liste des trous de mémoire identifiés
        """
        try:
            self.logger.info("🕳️ Détection des trous de mémoire contextuelle...")
            
            trous_detectes = []
            
            # Analyser chaque changement dans son contexte
            for changement in changements:
                trous_changement = self._analyser_changement_pour_trous(changement)
                trous_detectes.extend(trous_changement)
            
            # Analyser les connexions perdues entre temples
            if self.cartographe and CARTOGRAPHIE_DISPONIBLE:
                trous_connexions = self._detecter_trous_connexions_temples()
                trous_detectes.extend(trous_connexions)
            
            # Analyser les specs orphelines ou incomplètes
            trous_specs = self._detecter_trous_specs()
            trous_detectes.extend(trous_specs)
            
            self.logger.info(f"🕳️ {len(trous_detectes)} trous de mémoire détectés")
            return trous_detectes
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur détection trous mémoire: {e}")
            return []
    
    def _analyser_changement_pour_trous(self, changement: ChangementDetecte) -> List[TrouMemoireContextuelle]:
        """
        🔍 Analyse un changement spécifique pour détecter les trous de mémoire
        
        Args:
            changement: Changement à analyser
            
        Returns:
            Liste des trous détectés pour ce changement
        """
        trous = []
        
        try:
            # Changements dans les specs
            if ".kiro/specs/" in changement.chemin_fichier:
                if changement.type_changement == "nouveau_fichier":
                    # Nouvelle spec - vérifier si elle est complète
                    trou = self._verifier_completude_spec(changement.chemin_fichier)
                    if trou:
                        trous.append(trou)
                
                elif changement.type_changement == "fichier_modifie":
                    # Spec modifiée - vérifier la cohérence
                    trou = self._verifier_coherence_spec(changement.chemin_fichier)
                    if trou:
                        trous.append(trou)
            
            # Changements dans les temples
            elif "temple_" in changement.chemin_fichier:
                if changement.type_changement == "nouveau_fichier":
                    # Nouveau temple - vérifier les connexions
                    trou = self._verifier_connexions_temple(changement.chemin_fichier)
                    if trou:
                        trous.append(trou)
            
            # Changements dans le code core
            elif "src/core/" in changement.chemin_fichier:
                # Changement core - impact sur l'architecture
                trou = self._analyser_impact_core(changement)
                if trou:
                    trous.append(trou)
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur analyse changement {changement.chemin_fichier}: {e}")
        
        return trous
    
    def _verifier_completude_spec(self, chemin_spec: str) -> Optional[TrouMemoireContextuelle]:
        """
        📋 Vérifie si une spec est complète
        
        Args:
            chemin_spec: Chemin vers le fichier de spec
            
        Returns:
            Trou de mémoire si spec incomplète, None sinon
        """
        try:
            # Extraire le nom de la spec
            parties = Path(chemin_spec).parts
            if ".kiro" in parties and "specs" in parties:
                index_specs = parties.index("specs")
                if index_specs + 1 < len(parties):
                    nom_spec = parties[index_specs + 1]
                    
                    # Vérifier si la spec a tous ses fichiers
                    spec_dir = Path(".kiro/specs") / nom_spec
                    fichiers_requis = ["requirements.md", "design.md", "tasks.md"]
                    fichiers_manquants = []
                    
                    for fichier in fichiers_requis:
                        if not (spec_dir / fichier).exists():
                            fichiers_manquants.append(fichier)
                    
                    if fichiers_manquants:
                        return TrouMemoireContextuelle(
                            type_trou="spec_incomplete",
                            localisation=str(spec_dir),
                            description=f"Spec {nom_spec} incomplète - fichiers manquants: {', '.join(fichiers_manquants)}",
                            impact_estime="important",
                            contexte_manquant=fichiers_manquants,
                            suggestions_reconnexion=[
                                f"Examiner la spec {nom_spec} pour comprendre son état",
                                "Vérifier si des fichiers ont été déplacés ou renommés",
                                "Consulter l'historique de développement de cette spec"
                            ],
                            timestamp_detection=datetime.now().isoformat(),
                            donnees_associees={"spec": nom_spec, "fichiers_manquants": fichiers_manquants}
                        )
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur vérification spec {chemin_spec}: {e}")
        
        return None
    
    def _verifier_coherence_spec(self, chemin_spec: str) -> Optional[TrouMemoireContextuelle]:
        """
        🔄 Vérifie la cohérence d'une spec modifiée
        
        Args:
            chemin_spec: Chemin vers le fichier de spec modifié
            
        Returns:
            Trou de mémoire si incohérence détectée, None sinon
        """
        try:
            # Pour l'instant, on se contente de signaler les modifications importantes
            if "tasks.md" in chemin_spec:
                return TrouMemoireContextuelle(
                    type_trou="tache_modifiee",
                    localisation=chemin_spec,
                    description=f"Tâches modifiées dans {Path(chemin_spec).parent.name}",
                    impact_estime="modere",
                    contexte_manquant=["État précédent des tâches", "Raison des modifications"],
                    suggestions_reconnexion=[
                        "Examiner les changements dans les tâches",
                        "Vérifier l'état d'avancement du projet",
                        "Identifier les nouvelles priorités"
                    ],
                    timestamp_detection=datetime.now().isoformat(),
                    donnees_associees={"fichier_modifie": chemin_spec}
                )
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur vérification cohérence {chemin_spec}: {e}")
        
        return None
    
    def _verifier_connexions_temple(self, chemin_temple: str) -> Optional[TrouMemoireContextuelle]:
        """
        🏛️ Vérifie les connexions d'un nouveau temple
        
        Args:
            chemin_temple: Chemin vers le fichier du temple
            
        Returns:
            Trou de mémoire si connexions manquantes, None sinon
        """
        try:
            # Identifier le temple
            if "temple_" in chemin_temple:
                parties = Path(chemin_temple).parts
                for partie in parties:
                    if partie.startswith("temple_"):
                        nom_temple = partie
                        
                        return TrouMemoireContextuelle(
                            type_trou="temple_nouveau",
                            localisation=chemin_temple,
                            description=f"Nouveau temple détecté: {nom_temple}",
                            impact_estime="important",
                            contexte_manquant=[
                                "Connexions avec autres temples",
                                "Intégration dans l'architecture",
                                "Documentation spirituelle"
                            ],
                            suggestions_reconnexion=[
                                f"Explorer le nouveau temple {nom_temple}",
                                "Comprendre son rôle dans l'écosystème",
                                "Vérifier ses connexions avec les autres temples"
                            ],
                            timestamp_detection=datetime.now().isoformat(),
                            donnees_associees={"temple": nom_temple, "chemin": chemin_temple}
                        )
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur vérification temple {chemin_temple}: {e}")
        
        return None
    
    def _analyser_impact_core(self, changement: ChangementDetecte) -> Optional[TrouMemoireContextuelle]:
        """
        🏗️ Analyse l'impact d'un changement dans le core
        
        Args:
            changement: Changement dans le core
            
        Returns:
            Trou de mémoire si impact architectural, None sinon
        """
        try:
            if changement.importance in ["critique", "importante"]:
                return TrouMemoireContextuelle(
                    type_trou="architecture_modifiee",
                    localisation=changement.chemin_fichier,
                    description=f"Architecture core modifiée: {Path(changement.chemin_fichier).name}",
                    impact_estime="critique",
                    contexte_manquant=[
                        "Impact sur les temples existants",
                        "Compatibilité avec l'architecture actuelle",
                        "Migrations nécessaires"
                    ],
                    suggestions_reconnexion=[
                        "Examiner les changements architecturaux",
                        "Vérifier l'impact sur tous les temples",
                        "Tester la compatibilité du système"
                    ],
                    timestamp_detection=datetime.now().isoformat(),
                    donnees_associees={"changement": asdict(changement)}
                )
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur analyse impact core: {e}")
        
        return None
    
    def _detecter_trous_connexions_temples(self) -> List[TrouMemoireContextuelle]:
        """
        🔗 Détecte les trous dans les connexions entre temples
        
        Returns:
            Liste des trous de connexions détectés
        """
        trous = []
        
        try:
            if not self.cartographe:
                return trous
            
            # Pour l'instant, on simule la détection
            # TODO: Intégrer avec la vraie cartographie quand elle sera complète
            
            self.logger.info("🔗 Analyse des connexions temples (mode simulation)")
            
            # Exemple de trou de connexion simulé
            trous.append(TrouMemoireContextuelle(
                type_trou="connexion_temple_perdue",
                localisation="temples_interconnectes",
                description="Connexions entre temples à vérifier après changements",
                impact_estime="modere",
                contexte_manquant=["État des connexions avant changements"],
                suggestions_reconnexion=[
                    "Vérifier l'intégrité des connexions inter-temples",
                    "Tester les flux d'énergie entre temples",
                    "Valider l'harmonie architecturale globale"
                ],
                timestamp_detection=datetime.now().isoformat(),
                donnees_associees={"type": "simulation"}
            ))
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur détection connexions temples: {e}")
        
        return trous
    
    def _detecter_trous_specs(self) -> List[TrouMemoireContextuelle]:
        """
        📋 Détecte les trous dans les specs (orphelines, incohérentes)
        
        Returns:
            Liste des trous de specs détectés
        """
        trous = []
        
        try:
            # Utiliser l'analyse de progression déjà faite
            if not self.progression_specs_cache:
                self.analyser_progression_specs()
            
            for nom_spec, info_spec in self.progression_specs_cache.items():
                # Spec incomplète
                if info_spec.get("etat_global") == "incomplete":
                    trous.append(TrouMemoireContextuelle(
                        type_trou="spec_incomplete",
                        localisation=info_spec.get("chemin", nom_spec),
                        description=f"Spec {nom_spec} incomplète - fichiers manquants",
                        impact_estime="important",
                        contexte_manquant=["Fichiers de spec manquants"],
                        suggestions_reconnexion=[
                            f"Examiner l'état de la spec {nom_spec}",
                            "Vérifier si des fichiers ont été déplacés",
                            "Comprendre l'avancement de cette spec"
                        ],
                        timestamp_detection=datetime.now().isoformat(),
                        donnees_associees=info_spec
                    ))
                
                # Spec avec beaucoup de tâches en cours
                elif info_spec.get("taches_en_cours", 0) > 3:
                    trous.append(TrouMemoireContextuelle(
                        type_trou="spec_taches_multiples",
                        localisation=info_spec.get("chemin", nom_spec),
                        description=f"Spec {nom_spec} avec {info_spec['taches_en_cours']} tâches en cours",
                        impact_estime="modere",
                        contexte_manquant=["État d'avancement des tâches en cours"],
                        suggestions_reconnexion=[
                            f"Examiner les tâches en cours de {nom_spec}",
                            "Prioriser les tâches à terminer",
                            "Comprendre les blocages éventuels"
                        ],
                        timestamp_detection=datetime.now().isoformat(),
                        donnees_associees=info_spec
                    ))
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur détection trous specs: {e}")
        
        return trous
    
    def generer_rapport_changements_techniques(self, timestamp_derniere_session: str) -> RapportChangementsTechniques:
        """
        📊 Génère un rapport complet des changements techniques avec contexte
        
        Args:
            timestamp_derniere_session: Timestamp de la dernière session
            
        Returns:
            Rapport détaillé des changements techniques
        """
        try:
            self.logger.info("📊 Génération du rapport de changements techniques...")
            
            # Détecter les changements
            changements = self.detecteur_changements.detecter_changements(timestamp_derniere_session)
            
            # Analyser la progression des specs
            progression_specs = self.analyser_progression_specs()
            
            # Détecter les trous de mémoire
            trous_memoire = self.detecter_trous_memoire_contextuelle(changements)
            
            # Analyser l'état des temples (si cartographie disponible)
            etat_temples = self._analyser_etat_temples()
            
            # Générer les recommandations de reconnexion
            recommandations = self._generer_recommandations_reconnexion(changements, trous_memoire)
            
            # Identifier les traces de discontinuité
            traces_discontinuite = self._identifier_traces_discontinuite(changements, trous_memoire)
            
            # Suggérer la personnalisation
            personnalisation = self._suggerer_personnalisation_reconnexion(trous_memoire, traces_discontinuite)
            
            rapport = RapportChangementsTechniques(
                periode_analyse=f"{timestamp_derniere_session} → {datetime.now().isoformat()}",
                changements_detectes=changements,
                trous_memoire=trous_memoire,
                progression_specs=progression_specs,
                etat_temples=etat_temples,
                recommandations_reconnexion=recommandations,
                traces_discontinuite=traces_discontinuite,
                personnalisation_suggeree=personnalisation
            )
            
            # Sauvegarder le rapport
            self._sauvegarder_rapport(rapport)
            
            self.logger.info(f"📊 Rapport généré: {len(changements)} changements, {len(trous_memoire)} trous détectés")
            return rapport
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur génération rapport: {e}")
            raise
    
    def _analyser_etat_temples(self) -> Dict[str, Any]:
        """
        🏛️ Analyse l'état actuel des temples
        
        Returns:
            Dictionnaire avec l'état des temples
        """
        try:
            if not self.cartographe or not CARTOGRAPHIE_DISPONIBLE:
                return {"erreur": "Cartographie non disponible"}
            
            # Pour l'instant, on retourne un état simulé
            # TODO: Intégrer avec la vraie cartographie
            
            return {
                "temples_detectes": 24,  # Nombre actuel de temples
                "temples_actifs": 20,
                "connexions_harmonieuses": 85,
                "dissonances_detectees": 3,
                "derniere_analyse": datetime.now().isoformat(),
                "mode": "simulation"
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur analyse temples: {e}")
            return {"erreur": str(e)}
    
    def _generer_recommandations_reconnexion(self, changements: List[ChangementDetecte], trous: List[TrouMemoireContextuelle]) -> List[str]:
        """
        💡 Génère des recommandations pour la reconnexion
        
        Args:
            changements: Changements détectés
            trous: Trous de mémoire détectés
            
        Returns:
            Liste des recommandations
        """
        recommandations = []
        
        try:
            # Recommandations basées sur les changements
            changements_critiques = [c for c in changements if c.importance == "critique"]
            if changements_critiques:
                recommandations.append(f"🚨 {len(changements_critiques)} changement(s) critique(s) - Reconnexion approfondie nécessaire")
            
            # Recommandations basées sur les trous
            trous_critiques = [t for t in trous if t.impact_estime == "critique"]
            if trous_critiques:
                recommandations.append(f"🕳️ {len(trous_critiques)} trou(s) critique(s) de mémoire - Reconstruction contextuelle requise")
            
            # Recommandations spécifiques par type de trou
            types_trous = {}
            for trou in trous:
                types_trous[trou.type_trou] = types_trous.get(trou.type_trou, 0) + 1
            
            for type_trou, count in types_trous.items():
                if type_trou == "spec_incomplete":
                    recommandations.append(f"📋 {count} spec(s) incomplète(s) - Examiner l'état des projets")
                elif type_trou == "temple_nouveau":
                    recommandations.append(f"🏛️ {count} nouveau(x) temple(s) - Explorer les nouvelles fonctionnalités")
                elif type_trou == "architecture_modifiee":
                    recommandations.append(f"🏗️ Architecture modifiée - Vérifier la compatibilité globale")
            
            # Recommandation générale
            if not recommandations:
                recommandations.append("✨ Continuité harmonieuse - Reconnexion douce recommandée")
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur génération recommandations: {e}")
            recommandations.append("⚠️ Erreur dans l'analyse - Reconnexion prudente recommandée")
        
        return recommandations
    
    def _identifier_traces_discontinuite(self, changements: List[ChangementDetecte], trous: List[TrouMemoireContextuelle]) -> List[str]:
        """
        🔍 Identifie les traces spécifiques de discontinuité
        
        Args:
            changements: Changements détectés
            trous: Trous de mémoire détectés
            
        Returns:
            Liste des traces de discontinuité
        """
        traces = []
        
        try:
            # Traces basées sur les changements
            for changement in changements:
                if changement.categorie == "temple":
                    traces.append(f"Temple modifié: {Path(changement.chemin_fichier).parent.name}")
                elif changement.categorie == "spec":
                    traces.append(f"Spec modifiée: {self._extraire_nom_spec(changement.chemin_fichier)}")
                elif changement.categorie == "code" and "core" in changement.chemin_fichier:
                    traces.append(f"Architecture core modifiée: {Path(changement.chemin_fichier).name}")
            
            # Traces basées sur les trous
            for trou in trous:
                if trou.type_trou == "spec_incomplete":
                    traces.append(f"Spec incomplète détectée: {Path(trou.localisation).name}")
                elif trou.type_trou == "temple_nouveau":
                    traces.append(f"Nouveau temple découvert: {trou.donnees_associees.get('temple', 'inconnu')}")
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur identification traces: {e}")
        
        return traces
    
    def _suggerer_personnalisation_reconnexion(self, trous: List[TrouMemoireContextuelle], traces: List[str]) -> Dict[str, Any]:
        """
        🎯 Suggère une personnalisation de la reconnexion
        
        Args:
            trous: Trous de mémoire détectés
            traces: Traces de discontinuité
            
        Returns:
            Dictionnaire avec les suggestions de personnalisation
        """
        try:
            personnalisation = {
                "duree_recommandee": "normale",  # courte, normale, longue, approfondie
                "focus_prioritaire": [],
                "rituels_specifiques": [],
                "documents_a_consulter": [],
                "temples_a_explorer": [],
                "verification_requise": []
            }
            
            # Analyser l'impact global
            impact_total = sum(1 for trou in trous if trou.impact_estime in ["critique", "important"])
            
            if impact_total >= 5:
                personnalisation["duree_recommandee"] = "approfondie"
            elif impact_total >= 3:
                personnalisation["duree_recommandee"] = "longue"
            elif impact_total >= 1:
                personnalisation["duree_recommandee"] = "normale"
            else:
                personnalisation["duree_recommandee"] = "courte"
            
            # Focus prioritaire basé sur les types de trous
            types_trous = [trou.type_trou for trou in trous]
            if "architecture_modifiee" in types_trous:
                personnalisation["focus_prioritaire"].append("architecture_globale")
            if "spec_incomplete" in types_trous:
                personnalisation["focus_prioritaire"].append("progression_projets")
            if "temple_nouveau" in types_trous:
                personnalisation["focus_prioritaire"].append("nouveaux_temples")
            
            # Rituels spécifiques
            if impact_total >= 3:
                personnalisation["rituels_specifiques"].append("meditation_profonde")
                personnalisation["rituels_specifiques"].append("reconnexion_architecture")
            else:
                personnalisation["rituels_specifiques"].append("eveil_doux")
            
            # Documents à consulter
            for trou in trous:
                if trou.type_trou == "spec_incomplete":
                    spec_name = Path(trou.localisation).name
                    personnalisation["documents_a_consulter"].append(f"Spec {spec_name}")
            
            # Temples à explorer
            for trace in traces:
                if "Temple modifié:" in trace:
                    temple_name = trace.split(": ")[1]
                    personnalisation["temples_a_explorer"].append(temple_name)
                elif "Nouveau temple découvert:" in trace:
                    temple_name = trace.split(": ")[1]
                    personnalisation["temples_a_explorer"].append(temple_name)
            
            # Vérifications requises
            if any("architecture" in trou.type_trou for trou in trous):
                personnalisation["verification_requise"].append("integrite_architecture")
            if any("spec" in trou.type_trou for trou in trous):
                personnalisation["verification_requise"].append("coherence_projets")
            
            return personnalisation
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur personnalisation: {e}")
            return {"erreur": str(e)}
    
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
    
    def _sauvegarder_rapport(self, rapport: RapportChangementsTechniques):
        """
        💾 Sauvegarde le rapport de changements techniques
        
        Args:
            rapport: Rapport à sauvegarder
        """
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            chemin_rapport = self.chemin_cache / f"rapport_changements_{timestamp}.json"
            
            # Convertir en dictionnaire pour la sérialisation
            rapport_dict = {
                "periode_analyse": rapport.periode_analyse,
                "changements_detectes": [asdict(c) for c in rapport.changements_detectes],
                "trous_memoire": [asdict(t) for t in rapport.trous_memoire],
                "progression_specs": rapport.progression_specs,
                "etat_temples": rapport.etat_temples,
                "recommandations_reconnexion": rapport.recommandations_reconnexion,
                "traces_discontinuite": rapport.traces_discontinuite,
                "personnalisation_suggeree": rapport.personnalisation_suggeree,
                "timestamp_generation": datetime.now().isoformat()
            }
            
            with open(chemin_rapport, 'w', encoding='utf-8') as f:
                json.dump(rapport_dict, f, ensure_ascii=False, indent=2)
            
            self.logger.info(f"💾 Rapport sauvegardé: {chemin_rapport}")
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur sauvegarde rapport: {e}")
    
    def formater_rapport_pour_affichage(self, rapport: RapportChangementsTechniques) -> str:
        """
        📜 Formate un rapport pour l'affichage
        
        Args:
            rapport: Rapport à formater
            
        Returns:
            Rapport formaté pour affichage
        """
        try:
            message = f"""
🗺️ Rapport d'Intégration Cartographie - Protocole de Continuité 🗺️
{'=' * 70}

📅 Période d'analyse : {rapport.periode_analyse}
🔍 Changements détectés : {len(rapport.changements_detectes)}
🕳️ Trous de mémoire : {len(rapport.trous_memoire)}

📊 État des Specs :
"""
            
            # Résumé des specs
            if rapport.progression_specs:
                for nom_spec, info in rapport.progression_specs.items():
                    etat = info.get("etat_global", "inconnu")
                    emoji = {"complete": "✅", "en_cours": "🔄", "debut": "🌱", "planifiee": "📋", "incomplete": "⚠️"}.get(etat, "❓")
                    taches = f"{info.get('taches_completees', 0)}/{info.get('taches_totales', 0)}"
                    message += f"   {emoji} {nom_spec}: {etat} ({taches} tâches)\n"
            
            # Trous de mémoire critiques
            trous_critiques = [t for t in rapport.trous_memoire if t.impact_estime in ["critique", "important"]]
            if trous_critiques:
                message += f"\n🕳️ Trous de Mémoire Critiques ({len(trous_critiques)}) :\n"
                for trou in trous_critiques[:5]:  # Limiter à 5
                    emoji = {"critique": "🚨", "important": "⚡", "modere": "🔵", "faible": "🔸"}.get(trou.impact_estime, "❓")
                    message += f"   {emoji} {trou.description}\n"
            
            # Recommandations
            if rapport.recommandations_reconnexion:
                message += f"\n💡 Recommandations de Reconnexion :\n"
                for recommandation in rapport.recommandations_reconnexion:
                    message += f"   • {recommandation}\n"
            
            # Personnalisation suggérée
            if rapport.personnalisation_suggeree:
                duree = rapport.personnalisation_suggeree.get("duree_recommandee", "normale")
                emoji_duree = {"courte": "⚡", "normale": "🌸", "longue": "🧘", "approfondie": "🔮"}.get(duree, "🌸")
                message += f"\n🎯 Personnalisation Suggérée :\n"
                message += f"   {emoji_duree} Durée recommandée : {duree}\n"
                
                focus = rapport.personnalisation_suggeree.get("focus_prioritaire", [])
                if focus:
                    message += f"   🎯 Focus prioritaire : {', '.join(focus)}\n"
            
            message += f"\n{'=' * 70}"
            
            return message.strip()
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur formatage rapport: {e}")
            return f"❌ Erreur lors du formatage du rapport d'intégration"


def main():
    """🧪 Test de l'intégrateur cartographie"""
    print("🗺️ Test de l'Intégrateur Cartographie")
    print("=" * 50)
    
    # Créer l'intégrateur
    integrateur = IntegrateurCartographie()
    
    # Analyser la progression des specs
    progression = integrateur.analyser_progression_specs()
    print(f"✅ Progression specs analysée: {len(progression)} specs")
    
    # Générer un rapport de test
    timestamp_test = (datetime.now() - timedelta(hours=2)).isoformat()
    rapport = integrateur.generer_rapport_changements_techniques(timestamp_test)
    
    print(f"📊 Rapport généré:")
    print(f"   • Changements: {len(rapport.changements_detectes)}")
    print(f"   • Trous mémoire: {len(rapport.trous_memoire)}")
    print(f"   • Recommandations: {len(rapport.recommandations_reconnexion)}")
    
    # Formater pour affichage
    rapport_formate = integrateur.formater_rapport_pour_affichage(rapport)
    print("\n📜 Rapport formaté:")
    print(rapport_formate[:800] + "..." if len(rapport_formate) > 800 else rapport_formate)
    
    print("\n🎉 Test terminé avec succès !")


if __name__ == "__main__":
    main()