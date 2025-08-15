"""
Intelligence Adaptative - Système d'apprentissage et d'évolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module implémente l'intelligence adaptative pour la Phase 3.3 :
- Apprentissage continu et amélioration automatique
- Adaptation contextuelle selon le contexte utilisateur
- Personnalisation avancée des préférences
- Évolution autonome et auto-amélioration
"""

import asyncio
import json
import time
import pickle
from typing import Any, Dict, List, Optional, Callable, Union, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import defaultdict, deque
from enum import Enum
import numpy as np
from pathlib import Path
import hashlib

from .gestionnaires_base import GestionnaireBase, LogManagerBase, EnergyManagerBase

class TypeApprentissage(Enum):
    """Types d'apprentissage"""
    SUPERVISE = "supervise"
    NON_SUPERVISE = "non_supervise"
    PAR_RENFORCEMENT = "renforcement"
    TRANSFERT = "transfert"
    META_APPRENTISSAGE = "meta_apprentissage"

@dataclass
class ExperienceApprentissage:
    """Expérience d'apprentissage"""
    contexte: Dict[str, Any]
    action: str
    resultat: Any
    feedback: float  # Score de satisfaction (-1 à 1)
    timestamp: datetime = field(default_factory=datetime.now)
    type_apprentissage: TypeApprentissage = TypeApprentissage.NON_SUPERVISE
    metadonnees: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ModeleAdaptatif:
    """Modèle adaptatif"""
    nom: str
    type_modele: str
    parametres: Dict[str, Any]
    performance: float = 0.0
    nombre_entrainements: int = 0
    derniere_mise_a_jour: datetime = field(default_factory=datetime.now)
    version: int = 1

@dataclass
class ContexteUtilisateur:
    """Contexte utilisateur pour adaptation"""
    identifiant: str
    preferences: Dict[str, Any]
    historique_interactions: List[Dict[str, Any]]
    niveau_expertise: float = 0.5
    style_apprentissage: str = "visuel"
    derniere_activite: datetime = field(default_factory=datetime.now)
    metriques_utilisation: Dict[str, float] = field(default_factory=dict)

class GestionnaireApprentissage:
    """Gestionnaire d'apprentissage continu"""
    
    def __init__(self):
        self.logger = LogManagerBase("Apprentissage")
        self._experiences = deque(maxlen=10000)
        self._modeles = {}
        self._strategies_apprentissage = {}
        self._performance_globale = 0.0
        self._apprentissage_actif = True
        
        # Métriques d'apprentissage
        self._metriques_apprentissage = {
            "experiences_total": 0,
            "modeles_actifs": 0,
            "performance_moyenne": 0.0,
            "taux_amelioration": 0.0
        }
    
    def ajouter_experience(self, experience: ExperienceApprentissage):
        """Ajoute une expérience d'apprentissage"""
        self._experiences.append(experience)
        self._metriques_apprentissage["experiences_total"] += 1
        
        # Déclencher l'apprentissage si nécessaire
        if len(self._experiences) % 10 == 0:  # Tous les 10 expériences
            asyncio.create_task(self._declencher_apprentissage())
        
        self.logger.debug(f"📚 Expérience ajoutée: {experience.action}")
    
    async def _declencher_apprentissage(self):
        """Déclenche un cycle d'apprentissage"""
        if not self._apprentissage_actif:
            return
        
        try:
            # Analyser les expériences récentes
            experiences_recentes = list(self._experiences)[-100:]  # 100 dernières
            
            # Calculer la performance moyenne
            feedbacks = [exp.feedback for exp in experiences_recentes]
            performance_moyenne = np.mean(feedbacks) if feedbacks else 0.0
            
            # Mettre à jour les métriques
            ancienne_performance = self._performance_globale
            self._performance_globale = performance_moyenne
            self._metriques_apprentissage["performance_moyenne"] = performance_moyenne
            
            # Calculer le taux d'amélioration
            if ancienne_performance > 0:
                taux_amelioration = (performance_moyenne - ancienne_performance) / ancienne_performance
                self._metriques_apprentissage["taux_amelioration"] = taux_amelioration
            
            # Mettre à jour les modèles
            await self._mettre_a_jour_modeles(experiences_recentes)
            
            self.logger.info(f"🧠 Apprentissage terminé - Performance: {performance_moyenne:.3f}")
            
        except Exception as e:
            self.logger.erreur(f"Erreur apprentissage: {e}")
    
    async def _mettre_a_jour_modeles(self, experiences: List[ExperienceApprentissage]):
        """Met à jour les modèles d'apprentissage"""
        for nom_modele, modele in self._modeles.items():
            try:
                # Trouver les expériences pertinentes pour ce modèle
                experiences_pertinentes = [
                    exp for exp in experiences 
                    if exp.type_apprentissage == modele.type_modele
                ]
                
                if experiences_pertinentes:
                    # Mettre à jour le modèle
                    nouvelle_performance = await self._entrainer_modele(modele, experiences_pertinentes)
                    modele.performance = nouvelle_performance
                    modele.nombre_entrainements += 1
                    modele.derniere_mise_a_jour = datetime.now()
                    modele.version += 1
                    
                    self.logger.debug(f"🔄 Modèle mis à jour: {nom_modele} (v{modele.version})")
            
            except Exception as e:
                self.logger.erreur(f"Erreur mise à jour modèle {nom_modele}: {e}")
    
    async def _entrainer_modele(self, modele: ModeleAdaptatif, experiences: List[ExperienceApprentissage]) -> float:
        """Entraîne un modèle avec des expériences"""
        # Simulation d'entraînement - dans un vrai système, on utiliserait des algorithmes ML
        feedbacks = [exp.feedback for exp in experiences]
        return np.mean(feedbacks) if feedbacks else 0.0
    
    def ajouter_modele(self, nom: str, type_modele: str, parametres: Dict[str, Any]):
        """Ajoute un nouveau modèle d'apprentissage"""
        self._modeles[nom] = ModeleAdaptatif(
            nom=nom,
            type_modele=type_modele,
            parametres=parametres
        )
        self._metriques_apprentissage["modeles_actifs"] = len(self._modeles)
        self.logger.info(f"🧠 Modèle ajouté: {nom}")
    
    def obtenir_metriques_apprentissage(self) -> Dict[str, Any]:
        """Obtient les métriques d'apprentissage"""
        return {
            **self._metriques_apprentissage,
            "modeles": {nom: {
                "performance": modele.performance,
                "entrainements": modele.nombre_entrainements,
                "version": modele.version
            } for nom, modele in self._modeles.items()}
        }

class GestionnaireAdaptationContextuelle:
    """Gestionnaire d'adaptation contextuelle"""
    
    def __init__(self):
        self.logger = LogManagerBase("Adaptation")
        self._contextes_utilisateurs = {}
        self._regles_adaptation = {}
        self._historique_adaptations = deque(maxlen=1000)
        self._patterns_contextuels = defaultdict(list)
        
    def enregistrer_utilisateur(self, identifiant: str, preferences_initiales: Dict[str, Any] = None):
        """Enregistre un utilisateur pour adaptation contextuelle"""
        if preferences_initiales is None:
            preferences_initiales = {
                "niveau_detail": "moyen",
                "style_interface": "classique",
                "frequence_notifications": "normale",
                "preferences_visuelles": {}
            }
        
        self._contextes_utilisateurs[identifiant] = ContexteUtilisateur(
            identifiant=identifiant,
            preferences=preferences_initiales,
            historique_interactions=[]
        )
        
        self.logger.info(f"👤 Utilisateur enregistré: {identifiant}")
    
    def enregistrer_interaction(self, identifiant: str, interaction: Dict[str, Any]):
        """Enregistre une interaction utilisateur"""
        if identifiant not in self._contextes_utilisateurs:
            self.enregistrer_utilisateur(identifiant)
        
        contexte = self._contextes_utilisateurs[identifiant]
        contexte.historique_interactions.append(interaction)
        contexte.derniere_activite = datetime.now()
        
        # Analyser le pattern d'interaction
        self._analyser_pattern_interaction(identifiant, interaction)
        
        self.logger.debug(f"📝 Interaction enregistrée pour {identifiant}")
    
    def _analyser_pattern_interaction(self, identifiant: str, interaction: Dict[str, Any]):
        """Analyse le pattern d'interaction"""
        # Extraire les caractéristiques de l'interaction
        caracteristiques = {
            "type": interaction.get("type", "inconnu"),
            "duree": interaction.get("duree", 0),
            "complexite": interaction.get("complexite", 1),
            "succes": interaction.get("succes", True)
        }
        
        self._patterns_contextuels[identifiant].append(caracteristiques)
        
        # Garder seulement les 100 derniers patterns
        if len(self._patterns_contextuels[identifiant]) > 100:
            self._patterns_contextuels[identifiant] = self._patterns_contextuels[identifiant][-100:]
    
    def adapter_interface(self, identifiant: str, contexte_actuel: Dict[str, Any]) -> Dict[str, Any]:
        """Adapte l'interface selon le contexte utilisateur"""
        if identifiant not in self._contextes_utilisateurs:
            return self._interface_par_defaut()
        
        contexte = self._contextes_utilisateurs[identifiant]
        patterns = self._patterns_contextuels[identifiant]
        
        # Analyser les patterns récents
        adaptation = self._calculer_adaptation(contexte, patterns, contexte_actuel)
        
        # Enregistrer l'adaptation
        self._historique_adaptations.append({
            "identifiant": identifiant,
            "adaptation": adaptation,
            "timestamp": datetime.now()
        })
        
        self.logger.info(f"🎨 Interface adaptée pour {identifiant}")
        return adaptation
    
    def _calculer_adaptation(self, contexte: ContexteUtilisateur, patterns: List[Dict], contexte_actuel: Dict[str, Any]) -> Dict[str, Any]:
        """Calcule l'adaptation optimale"""
        adaptation = contexte.preferences.copy()
        
        # Analyser les patterns récents
        if patterns:
            patterns_recents = patterns[-10:]  # 10 derniers patterns
            
            # Calculer le niveau d'expertise basé sur les patterns
            succes_rate = sum(1 for p in patterns_recents if p.get("succes", True)) / len(patterns_recents)
            complexite_moyenne = np.mean([p.get("complexite", 1) for p in patterns_recents])
            
            # Adapter le niveau de détail
            if succes_rate > 0.8 and complexite_moyenne > 2:
                adaptation["niveau_detail"] = "avance"
            elif succes_rate < 0.5:
                adaptation["niveau_detail"] = "debutant"
            
            # Adapter le style d'interface
            if complexite_moyenne > 3:
                adaptation["style_interface"] = "minimaliste"
            elif complexite_moyenne < 1.5:
                adaptation["style_interface"] = "guide"
        
        # Adapter selon le contexte actuel
        if contexte_actuel.get("urgence", False):
            adaptation["frequence_notifications"] = "elevée"
        
        if contexte_actuel.get("environnement", "") == "mobile":
            adaptation["style_interface"] = "mobile"
        
        return adaptation
    
    def _interface_par_defaut(self) -> Dict[str, Any]:
        """Retourne l'interface par défaut"""
        return {
            "niveau_detail": "moyen",
            "style_interface": "classique",
            "frequence_notifications": "normale",
            "preferences_visuelles": {}
        }
    
    def obtenir_statistiques_adaptation(self) -> Dict[str, Any]:
        """Obtient les statistiques d'adaptation"""
        return {
            "utilisateurs_enregistres": len(self._contextes_utilisateurs),
            "adaptations_total": len(self._historique_adaptations),
            "patterns_analyses": sum(len(patterns) for patterns in self._patterns_contextuels.values())
        }

class GestionnairePersonnalisation:
    """Gestionnaire de personnalisation avancée"""
    
    def __init__(self):
        self.logger = LogManagerBase("Personnalisation")
        self._profils_utilisateurs = {}
        self._preferences_globales = {}
        self._recommandations_cache = {}
        self._apprentissage_preferences = defaultdict(list)
        
    def creer_profil_utilisateur(self, identifiant: str, donnees_initiales: Dict[str, Any] = None):
        """Crée un profil utilisateur personnalisé"""
        if donnees_initiales is None:
            donnees_initiales = {
                "nom": "Utilisateur",
                "age": 25,
                "interets": [],
                "niveau_technique": "intermediaire",
                "preferences_visuelles": {
                    "theme": "clair",
                    "couleurs": ["bleu", "vert"],
                    "police": "standard"
                },
                "preferences_fonctionnelles": {
                    "notifications": True,
                    "sauvegarde_auto": True,
                    "mode_expert": False
                }
            }
        
        self._profils_utilisateurs[identifiant] = {
            "donnees": donnees_initiales,
            "historique_preferences": [],
            "derniere_mise_a_jour": datetime.now(),
            "score_personnalisation": 0.0
        }
        
        self.logger.info(f"👤 Profil créé: {identifiant}")
    
    def mettre_a_jour_preferences(self, identifiant: str, nouvelles_preferences: Dict[str, Any]):
        """Met à jour les préférences d'un utilisateur"""
        if identifiant not in self._profils_utilisateurs:
            self.creer_profil_utilisateur(identifiant)
        
        profil = self._profils_utilisateurs[identifiant]
        
        # Sauvegarder l'historique
        profil["historique_preferences"].append({
            "preferences": nouvelles_preferences,
            "timestamp": datetime.now()
        })
        
        # Mettre à jour les données actuelles
        profil["donnees"].update(nouvelles_preferences)
        profil["derniere_mise_a_jour"] = datetime.now()
        
        # Calculer le score de personnalisation
        profil["score_personnalisation"] = self._calculer_score_personnalisation(profil)
        
        self.logger.info(f"⚙️ Préférences mises à jour pour {identifiant}")
    
    def _calculer_score_personnalisation(self, profil: Dict[str, Any]) -> float:
        """Calcule le score de personnalisation"""
        score = 0.0
        
        # Score basé sur la richesse des préférences
        donnees = profil["donnees"]
        score += len(donnees.get("interets", [])) * 0.1
        score += len(donnees.get("preferences_visuelles", {})) * 0.05
        score += len(donnees.get("preferences_fonctionnelles", {})) * 0.05
        
        # Score basé sur l'historique
        score += len(profil["historique_preferences"]) * 0.02
        
        return min(score, 1.0)  # Normaliser entre 0 et 1
    
    def generer_recommandations(self, identifiant: str, contexte: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """Génère des recommandations personnalisées"""
        if identifiant not in self._profils_utilisateurs:
            return []
        
        profil = self._profils_utilisateurs[identifiant]
        donnees = profil["donnees"]
        
        recommandations = []
        
        # Recommandations basées sur les intérêts
        for interet in donnees.get("interets", []):
            recommandations.append({
                "type": "interet",
                "contenu": f"Contenu lié à {interet}",
                "priorite": 0.8,
                "raison": f"Basé sur votre intérêt pour {interet}"
            })
        
        # Recommandations basées sur le niveau technique
        niveau = donnees.get("niveau_technique", "intermediaire")
        if niveau == "debutant":
            recommandations.append({
                "type": "tutoriel",
                "contenu": "Guide de démarrage",
                "priorite": 0.9,
                "raison": "Recommandé pour les débutants"
            })
        elif niveau == "expert":
            recommandations.append({
                "type": "fonctionnalite_avancee",
                "contenu": "Fonctionnalités avancées",
                "priorite": 0.7,
                "raison": "Adapté à votre niveau expert"
            })
        
        # Recommandations basées sur le contexte
        if contexte:
            if contexte.get("heure", 0) < 8 or contexte.get("heure", 0) > 22:
                recommandations.append({
                    "type": "mode_nuit",
                    "contenu": "Activer le mode nuit",
                    "priorite": 0.6,
                    "raison": "Heure tardive détectée"
                })
        
        # Trier par priorité
        recommandations.sort(key=lambda x: x["priorite"], reverse=True)
        
        return recommandations[:5]  # Retourner les 5 meilleures
    
    def obtenir_profil_complet(self, identifiant: str) -> Dict[str, Any]:
        """Obtient le profil complet d'un utilisateur"""
        if identifiant not in self._profils_utilisateurs:
            return {}
        
        profil = self._profils_utilisateurs[identifiant]
        
        return {
            "identifiant": identifiant,
            "donnees": profil["donnees"],
            "score_personnalisation": profil["score_personnalisation"],
            "derniere_mise_a_jour": profil["derniere_mise_a_jour"].isoformat(),
            "nombre_preferences": len(profil["historique_preferences"])
        }

class SystemeEvolutionAutonome:
    """Système d'évolution autonome"""
    
    def __init__(self):
        self.logger = LogManagerBase("Evolution")
        self.energie_evolution = EnergyManagerBase()
        self._strategies_evolution = []
        self._metriques_evolution = {}
        self._evolution_actif = True
        self._derniere_evolution = None
        
        # Note: L'évolution autonome sera démarrée manuellement si nécessaire
    
    def ajouter_strategie_evolution(self, nom: str, strategie: Callable, priorite: int = 1):
        """Ajoute une stratégie d'évolution"""
        self._strategies_evolution.append({
            "nom": nom,
            "strategie": strategie,
            "priorite": priorite,
            "derniere_execution": None,
            "succes": 0,
            "echecs": 0
        })
        
        self.logger.info(f"🧬 Stratégie d'évolution ajoutée: {nom}")
    
    async def _boucle_evolution_autonome(self):
        """Boucle d'évolution autonome"""
        while self._evolution_actif:
            try:
                await self._executer_evolution()
                await asyncio.sleep(300)  # Évolution toutes les 5 minutes
            except Exception as e:
                self.logger.erreur(f"Erreur évolution autonome: {e}")
                await asyncio.sleep(600)  # Attendre plus longtemps en cas d'erreur
    
    async def _executer_evolution(self):
        """Exécute un cycle d'évolution"""
        if not self._strategies_evolution:
            return
        
        # Trier les stratégies par priorité
        strategies_triees = sorted(self._strategies_evolution, key=lambda x: x["priorite"], reverse=True)
        
        for strategie_info in strategies_triees:
            try:
                # Vérifier si la stratégie doit être exécutée
                if self._doit_executer_strategie(strategie_info):
                    await self._executer_strategie(strategie_info)
                    
                    # Mettre à jour l'énergie
                    self.energie_evolution.ajuster_energie(0.05)
                    
            except Exception as e:
                strategie_info["echecs"] += 1
                self.logger.erreur(f"Erreur stratégie {strategie_info['nom']}: {e}")
        
        self._derniere_evolution = datetime.now()
        self.logger.info("🧬 Cycle d'évolution terminé")
    
    def _doit_executer_strategie(self, strategie_info: Dict[str, Any]) -> bool:
        """Détermine si une stratégie doit être exécutée"""
        # Logique simple : exécuter si pas exécutée récemment ou si taux de succès élevé
        derniere_execution = strategie_info.get("derniere_execution")
        
        if derniere_execution is None:
            return True
        
        # Exécuter si plus de 1 heure s'est écoulée
        if datetime.now() - derniere_execution > timedelta(hours=1):
            return True
        
        # Exécuter si taux de succès élevé (> 80%)
        total_executions = strategie_info["succes"] + strategie_info["echecs"]
        if total_executions > 0:
            taux_succes = strategie_info["succes"] / total_executions
            if taux_succes > 0.8:
                return True
        
        return False
    
    async def _executer_strategie(self, strategie_info: Dict[str, Any]):
        """Exécute une stratégie d'évolution"""
        strategie_info["derniere_execution"] = datetime.now()
        
        try:
            if asyncio.iscoroutinefunction(strategie_info["strategie"]):
                await strategie_info["strategie"]()
            else:
                strategie_info["strategie"]()
            
            strategie_info["succes"] += 1
            self.logger.info(f"✅ Stratégie réussie: {strategie_info['nom']}")
            
        except Exception as e:
            strategie_info["echecs"] += 1
            raise e
    
    def obtenir_metriques_evolution(self) -> Dict[str, Any]:
        """Obtient les métriques d'évolution"""
        return {
            "energie_evolution": self.energie_evolution.niveau_energie,
            "strategies_actives": len(self._strategies_evolution),
            "derniere_evolution": self._derniere_evolution.isoformat() if self._derniere_evolution else None,
            "strategies": [{
                "nom": s["nom"],
                "priorite": s["priorite"],
                "succes": s["succes"],
                "echecs": s["echecs"],
                "taux_succes": s["succes"] / (s["succes"] + s["echecs"]) if (s["succes"] + s["echecs"]) > 0 else 0
            } for s in self._strategies_evolution]
        }

class IntelligenceAdaptative(GestionnaireBase):
    """Système d'intelligence adaptative principal"""
    
    def __init__(self):
        super().__init__("IntelligenceAdaptative")
        self.gestionnaire_apprentissage = GestionnaireApprentissage()
        self.gestionnaire_adaptation = GestionnaireAdaptationContextuelle()
        self.gestionnaire_personnalisation = GestionnairePersonnalisation()
        self.systeme_evolution = SystemeEvolutionAutonome()
        self.energie_intelligence = EnergyManagerBase()
        
        # Initialiser le système
        self._initialiser()
        
        # Configurer les stratégies d'évolution par défaut
        self._configurer_strategies_evolution()
        
        # Note: Les boucles d'évolution seront démarrées manuellement si nécessaire
    
    def _initialiser(self):
        """Initialise l'intelligence adaptative"""
        self.logger.info("🧠 Intelligence Adaptative initialisée")
        
        # Ajouter des modèles d'apprentissage par défaut
        self.gestionnaire_apprentissage.ajouter_modele(
            "preferences_utilisateur",
            TypeApprentissage.NON_SUPERVISE,
            {"algorithme": "clustering", "parametres": {}}
        )
        
        self.gestionnaire_apprentissage.ajouter_modele(
            "adaptation_contextuelle",
            TypeApprentissage.SUPERVISE,
            {"algorithme": "regression", "parametres": {}}
        )
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre l'intelligence adaptative"""
        debut = time.time()
        
        # Collecter les métriques de tous les composants
        metriques_apprentissage = self.gestionnaire_apprentissage.obtenir_metriques_apprentissage()
        metriques_adaptation = self.gestionnaire_adaptation.obtenir_statistiques_adaptation()
        metriques_evolution = self.systeme_evolution.obtenir_metriques_evolution()
        
        # Calculer le score global d'intelligence
        score_apprentissage = metriques_apprentissage.get("performance_moyenne", 0.0)
        score_adaptation = metriques_adaptation.get("utilisateurs_enregistres", 0) / 10  # Normaliser
        score_evolution = self.systeme_evolution.energie_evolution.niveau_energie
        
        score_global = (score_apprentissage + score_adaptation + score_evolution) / 3
        
        # Mettre à jour l'énergie
        self.energie_intelligence.ajuster_energie(score_global * 0.1)
        
        temps_execution = time.time() - debut
        
        return {
            "score_intelligence": score_global,
            "score_apprentissage": score_apprentissage,
            "score_adaptation": score_adaptation,
            "score_evolution": score_evolution,
            "temps_execution": temps_execution
        }
    
    def _configurer_strategies_evolution(self):
        """Configure les stratégies d'évolution par défaut"""
        
        async def strategie_optimisation_modeles():
            """Stratégie d'optimisation des modèles"""
            # Optimiser les modèles d'apprentissage
            pass
        
        async def strategie_adaptation_preferences():
            """Stratégie d'adaptation des préférences"""
            # Adapter les préférences globales
            pass
        
        self.systeme_evolution.ajouter_strategie_evolution("optimisation_modeles", strategie_optimisation_modeles, priorite=2)
        self.systeme_evolution.ajouter_strategie_evolution("adaptation_preferences", strategie_adaptation_preferences, priorite=1)
    
    def obtenir_etat_complet(self) -> Dict[str, Any]:
        """Obtient l'état complet de l'intelligence adaptative"""
        return {
            "intelligence": {
                "energie": self.energie_intelligence.niveau_energie,
                "score_global": self.energie_intelligence.niveau_energie
            },
            "apprentissage": self.gestionnaire_apprentissage.obtenir_metriques_apprentissage(),
            "adaptation": self.gestionnaire_adaptation.obtenir_statistiques_adaptation(),
            "evolution": self.systeme_evolution.obtenir_metriques_evolution()
        }
