"""
Optimiseur de Performance - Module d'optimisation avancée
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module implémente les optimisations avancées pour la Phase 3.1 :
- Optimisation mémoire et gestion des ressources
- Optimisation de vitesse et temps de réponse
- Système robuste de gestion d'erreurs
- Monitoring et surveillance des performances
"""

import asyncio
import gc
import psutil
import time
import weakref
from typing import Any, Dict, List, Optional, Callable, Union
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import defaultdict, deque
import threading
import logging
from pathlib import Path
import json

from .gestionnaires_base import GestionnaireBase, LogManagerBase

@dataclass
class MetriquePerformance:
    """Métrique de performance individuelle"""
    nom: str
    valeur: float
    unite: str
    timestamp: datetime = field(default_factory=datetime.now)
    contexte: Dict[str, Any] = field(default_factory=dict)

@dataclass
class RapportPerformance:
    """Rapport complet de performance"""
    timestamp: datetime = field(default_factory=datetime.now)
    metriques: List[MetriquePerformance] = field(default_factory=list)
    alertes: List[str] = field(default_factory=list)
    recommandations: List[str] = field(default_factory=list)
    score_global: float = 0.0

class GestionnaireMemoire:
    """Gestionnaire avancé de la mémoire"""
    
    def __init__(self):
        self.logger = LogManagerBase("Memoire")
        self._cache_objet = weakref.WeakValueDictionary()
        self._cache_limite = 1000
        self._cache_hits = 0
        self._cache_misses = 0
        self._objets_traques = set()
        
    def obtenir_usage_memoire(self) -> Dict[str, float]:
        """Obtient l'usage mémoire actuel"""
        process = psutil.Process()
        mem_info = process.memory_info()
        
        return {
            "rss_mb": mem_info.rss / 1024 / 1024,  # Mémoire physique
            "vms_mb": mem_info.vms / 1024 / 1024,  # Mémoire virtuelle
            "pourcentage": process.memory_percent(),
            "disponible_systeme_mb": psutil.virtual_memory().available / 1024 / 1024
        }
    
    def optimiser_memoire(self) -> Dict[str, Any]:
        """Optimise l'usage mémoire"""
        avant = self.obtenir_usage_memoire()
        
        # Forcer le garbage collector
        objets_avant = len(gc.get_objects())
        gc.collect()
        objets_apres = len(gc.get_objects())
        
        # Nettoyer le cache faible
        self._nettoyer_cache()
        
        apres = self.obtenir_usage_memoire()
        
        return {
            "liberation_mb": avant["rss_mb"] - apres["rss_mb"],
            "objets_supprimes": objets_avant - objets_apres,
            "cache_hits": self._cache_hits,
            "cache_misses": self._cache_misses,
            "taux_cache": self._cache_hits / (self._cache_hits + self._cache_misses) if (self._cache_hits + self._cache_misses) > 0 else 0
        }
    
    def _nettoyer_cache(self):
        """Nettoie le cache d'objets"""
        if len(self._cache_objet) > self._cache_limite:
            # Supprimer les entrées les plus anciennes
            cles_a_supprimer = list(self._cache_objet.keys())[:len(self._cache_objet) // 2]
            for cle in cles_a_supprimer:
                del self._cache_objet[cle]
    
    def traquer_objet(self, nom: str, objet: Any):
        """Traque un objet pour surveillance mémoire"""
        self._objets_traques.add(nom)
        self._cache_objet[nom] = objet

class GestionnaireVitesse:
    """Gestionnaire d'optimisation de vitesse"""
    
    def __init__(self):
        self.logger = LogManagerBase("Vitesse")
        self._chronometres = {}
        self._moyennes_temps = defaultdict(list)
        self._seuils_alerte = {
            "operation_critique": 1.0,  # 1 seconde
            "operation_normale": 0.5,   # 500ms
            "operation_rapide": 0.1     # 100ms
        }
    
    def chronometrer(self, nom_operation: str):
        """Décorateur pour chronométrer une opération"""
        def decorateur(func):
            async def wrapper(*args, **kwargs):
                debut = time.time()
                try:
                    resultat = await func(*args, **kwargs)
                    temps = time.time() - debut
                    self._enregistrer_temps(nom_operation, temps)
                    return resultat
                except Exception as e:
                    temps = time.time() - debut
                    self._enregistrer_temps(nom_operation, temps, erreur=True)
                    raise
            return wrapper
        return decorateur
    
    def _enregistrer_temps(self, nom: str, temps: float, erreur: bool = False):
        """Enregistre le temps d'exécution"""
        self._moyennes_temps[nom].append(temps)
        
        # Garder seulement les 100 derniers temps
        if len(self._moyennes_temps[nom]) > 100:
            self._moyennes_temps[nom] = self._moyennes_temps[nom][-100:]
        
        # Vérifier les seuils d'alerte
        if temps > self._seuils_alerte.get("operation_critique", 1.0):
            self.logger.erreur(f"🚨 Opération lente détectée: {nom} ({temps:.3f}s)")
    
    def obtenir_statistiques_vitesse(self) -> Dict[str, Dict[str, float]]:
        """Obtient les statistiques de vitesse"""
        stats = {}
        
        for nom, temps_list in self._moyennes_temps.items():
            if temps_list:
                stats[nom] = {
                    "moyenne": sum(temps_list) / len(temps_list),
                    "min": min(temps_list),
                    "max": max(temps_list),
                    "dernier": temps_list[-1],
                    "nombre_executions": len(temps_list)
                }
        
        return stats

class GestionnaireErreurs:
    """Système robuste de gestion d'erreurs"""
    
    def __init__(self):
        self.logger = LogManagerBase("Erreurs")
        self._erreurs_recentes = deque(maxlen=100)
        self._erreurs_critiques = []
        self._strategies_reparation = {}
        self._mode_degradation = False
        self._temps_derniere_erreur = None
        self._erreur_en_cours = None
    
    def enregistrer_erreur(self, erreur: Exception, contexte: str, critique: bool = False):
        """Enregistre une erreur avec contexte"""
        erreur_info = {
            "type": type(erreur).__name__,
            "message": str(erreur),
            "contexte": contexte,
            "timestamp": datetime.now(),
            "critique": critique,
            "traceback": self._obtenir_traceback()
        }
        
        self._erreurs_recentes.append(erreur_info)
        
        if critique:
            self._erreurs_critiques.append(erreur_info)
            self.logger.erreur(f"🚨 Erreur critique dans {contexte}: {erreur}")
            # Log additional details for critical errors
            self.logger.erreur(f"   Traceback: {erreur_info['traceback']}")
        else:
            self.logger.warning(f"⚠️ Erreur dans {contexte}: {erreur}")
        
        # Vérifier si on doit passer en mode dégradation
        if len(self._erreurs_critiques) >= 5:
            self._activer_mode_degradation()
        
        # Track error timing to detect error storms
        if self._temps_derniere_erreur:
            temps_ecoule = (datetime.now() - self._temps_derniere_erreur).total_seconds()
            if temps_ecoule < 1.0 and not critique:  # Multiple errors in short time
                self.logger.warning("⚠️ Tempête d'erreurs détectée - surveillance accrue")
        
        self._temps_derniere_erreur = datetime.now()
        self._erreur_en_cours = erreur_info
    
    def _obtenir_traceback(self) -> str:
        """Obtient le traceback de l'erreur courante"""
        import traceback
        return traceback.format_exc()
    
    def _activer_mode_degradation(self):
        """Active le mode dégradation"""
        if not self._mode_degradation:
            self._mode_degradation = True
            self.logger.erreur("🛡️ Mode dégradation activé - Fonctionnalités réduites")
            # Notify other systems
            self._notifier_systemes_degradation()
    
    def _notifier_systemes_degradation(self):
        """Notifie les autres systèmes du mode dégradation"""
        # This could be extended to notify other components
        pass
    
    def recuperer_depuis_erreur(self, strategie: str = "default") -> bool:
        """Tente de récupérer depuis une erreur"""
        if not self._erreur_en_cours:
            return True
            
        try:
            # Apply recovery strategy
            if strategie == "retry":
                self.logger.info("🔄 Tentative de récupération par retry")
                return True
            elif strategie == "fallback":
                self.logger.info("🔄 Passage en mode fallback")
                return True
            else:
                self.logger.info("🔄 Récupération par défaut")
                return True
        except Exception as e:
            self.enregistrer_erreur(e, "Récupération d'erreur", critique=True)
            return False
    
    def obtenir_rapport_erreurs(self) -> Dict[str, Any]:
        """Obtient un rapport des erreurs"""
        return {
            "erreurs_recentes": len(self._erreurs_recentes),
            "erreurs_critiques": len(self._erreurs_critiques),
            "mode_degradation": self._mode_degradation,
            "dernieres_erreurs": list(self._erreurs_recentes)[-10:] if self._erreurs_recentes else []
        }
    
    def ajouter_strategie_reparation(self, type_erreur: str, strategie: Callable):
        """Ajoute une stratégie de réparation"""
        self._strategies_reparation[type_erreur] = strategie
    
    async def tenter_reparation(self, erreur: Exception) -> bool:
        """Tente de réparer une erreur"""
        type_erreur = type(erreur).__name__
        
        if type_erreur in self._strategies_reparation:
            try:
                await self._strategies_reparation[type_erreur](erreur)
                self.logger.info(f"🔧 Réparation réussie pour {type_erreur}")
                return True
            except Exception as e:
                self.logger.erreur(f"❌ Échec réparation {type_erreur}: {e}")
                return False
        
        return False

class SystemeMonitoring:
    """Système de monitoring et surveillance"""
    
    def __init__(self):
        self.logger = LogManagerBase("Monitoring")
        self._metriques_en_temps_reel = {}
        self._alertes_actives = []
        self._seuils_alerte = {
            "usage_memoire": 80.0,  # 80% de mémoire utilisée
            "usage_cpu": 90.0,      # 90% de CPU
            "temps_reponse": 2.0,   # 2 secondes
            "erreurs_critiques": 3   # 3 erreurs critiques
        }
        self._thread_monitoring = None
        self._monitoring_actif = False
    
    def demarrer_monitoring(self):
        """Démarre le monitoring en arrière-plan"""
        if not self._monitoring_actif:
            self._monitoring_actif = True
            self._thread_monitoring = threading.Thread(target=self._boucle_monitoring, daemon=True)
            self._thread_monitoring.start()
            self.logger.info("📊 Monitoring démarré")
    
    def arreter_monitoring(self):
        """Arrête le monitoring"""
        self._monitoring_actif = False
        if self._thread_monitoring:
            self._thread_monitoring.join(timeout=5)
        self.logger.info("📊 Monitoring arrêté")
    
    def _boucle_monitoring(self):
        """Boucle principale de monitoring"""
        while self._monitoring_actif:
            try:
                self._collecter_metriques()
                self._verifier_alertes()
                time.sleep(30)  # Vérification toutes les 30 secondes
            except Exception as e:
                self.logger.erreur(f"Erreur monitoring: {e}")
    
    def _collecter_metriques(self):
        """Collecte les métriques système"""
        # Métriques système
        cpu_percent = psutil.cpu_percent(interval=1)
        mem_info = psutil.virtual_memory()
        
        self._metriques_en_temps_reel.update({
            "cpu_usage": cpu_percent,
            "memory_usage": mem_info.percent,
            "memory_available_mb": mem_info.available / 1024 / 1024,
            "timestamp": datetime.now()
        })
    
    def _verifier_alertes(self):
        """Vérifie les seuils d'alerte"""
        alertes_nouvelles = []
        
        if self._metriques_en_temps_reel.get("memory_usage", 0) > self._seuils_alerte["usage_memoire"]:
            alertes_nouvelles.append("Mémoire système élevée")
        
        if self._metriques_en_temps_reel.get("cpu_usage", 0) > self._seuils_alerte["usage_cpu"]:
            alertes_nouvelles.append("CPU système élevé")
        
        # Ajouter les nouvelles alertes
        for alerte in alertes_nouvelles:
            if alerte not in self._alertes_actives:
                self._alertes_actives.append(alerte)
                self.logger.erreur(f"🚨 Alerte: {alerte}")
        
        # Nettoyer les alertes résolues
        self._alertes_actives = [a for a in self._alertes_actives if a in alertes_nouvelles]
    
    def obtenir_etat_monitoring(self) -> Dict[str, Any]:
        """Obtient l'état du monitoring"""
        return {
            "monitoring_actif": self._monitoring_actif,
            "metriques_actuelles": self._metriques_en_temps_reel,
            "alertes_actives": self._alertes_actives,
            "seuils_alerte": self._seuils_alerte
        }

class OptimiseurPerformance(GestionnaireBase):
    """Optimiseur principal de performance"""
    
    def __init__(self):
        super().__init__("OptimiseurPerformance")
        self.gestionnaire_memoire = GestionnaireMemoire()
        self.gestionnaire_vitesse = GestionnaireVitesse()
        self.gestionnaire_erreurs = GestionnaireErreurs()
        self.systeme_monitoring = SystemeMonitoring()
        
        # Métriques de performance
        self._rapports_performance = deque(maxlen=50)
        self._derniere_optimisation = None
        
        # Initialiser le système
        self._initialiser()
        
        # Démarrer le monitoring
        self.systeme_monitoring.demarrer_monitoring()
        
        # Configurer les stratégies de réparation
        self._configurer_strategies_reparation()
    
    def _initialiser(self):
        """Initialise l'optimiseur"""
        self.logger.info("⚡ Optimiseur de Performance initialisé")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre les optimisations"""
        debut = time.time()
        
        # Collecter les métriques
        metriques = await self._collecter_metriques_completes()
        
        # Analyser les performances
        analyse = self._analyser_performances(metriques)
        
        # Appliquer les optimisations si nécessaire
        optimisations = await self._appliquer_optimisations(analyse)
        
        # Générer le rapport
        rapport = self._generer_rapport_performance(metriques, analyse, optimisations)
        self._rapports_performance.append(rapport)
        
        temps_execution = time.time() - debut
        
        return {
            "score_optimisation": rapport.score_global,
            "temps_execution": temps_execution,
            "optimisations_appliquees": len(optimisations)
        }
    
    async def _collecter_metriques_completes(self) -> Dict[str, Any]:
        """Collecte toutes les métriques de performance"""
        return {
            "memoire": self.gestionnaire_memoire.obtenir_usage_memoire(),
            "vitesse": self.gestionnaire_vitesse.obtenir_statistiques_vitesse(),
            "erreurs": self.gestionnaire_erreurs.obtenir_rapport_erreurs(),
            "monitoring": self.systeme_monitoring.obtenir_etat_monitoring()
        }
    
    def _analyser_performances(self, metriques: Dict[str, Any]) -> Dict[str, Any]:
        """Analyse les performances et identifie les problèmes"""
        analyse = {
            "problemes": [],
            "recommandations": [],
            "score_global": 100.0
        }
        
        # Analyser la mémoire
        mem_info = metriques["memoire"]
        if mem_info["pourcentage"] > 70:
            analyse["problemes"].append("Usage mémoire élevé")
            analyse["recommandations"].append("Optimiser la gestion mémoire")
            analyse["score_global"] -= 20
        
        # Analyser les erreurs
        erreurs_info = metriques["erreurs"]
        if erreurs_info["erreurs_critiques"] > 0:
            analyse["problemes"].append("Erreurs critiques détectées")
            analyse["recommandations"].append("Investigation des erreurs critiques")
            analyse["score_global"] -= 30
        
        # Analyser la vitesse
        vitesse_info = metriques["vitesse"]
        for operation, stats in vitesse_info.items():
            if stats["moyenne"] > 1.0:
                analyse["problemes"].append(f"Opération lente: {operation}")
                analyse["recommandations"].append(f"Optimiser {operation}")
                analyse["score_global"] -= 10
        
        analyse["score_global"] = max(0, analyse["score_global"])
        
        return analyse
    
    async def _appliquer_optimisations(self, analyse: Dict[str, Any]) -> List[str]:
        """Applique les optimisations nécessaires"""
        optimisations_appliquees = []
        
        for probleme in analyse["problemes"]:
            if "mémoire" in probleme.lower():
                resultat = self.gestionnaire_memoire.optimiser_memoire()
                optimisations_appliquees.append(f"Optimisation mémoire: {resultat['liberation_mb']:.2f}MB libérés")
            
            elif "erreur" in probleme.lower():
                # Tentative de réparation automatique
                optimisations_appliquees.append("Tentative de réparation d'erreurs")
        
        return optimisations_appliquees
    
    def _generer_rapport_performance(self, metriques: Dict[str, Any], analyse: Dict[str, Any], optimisations: List[str]) -> RapportPerformance:
        """Génère un rapport de performance complet"""
        rapport = RapportPerformance()
        
        # Ajouter les métriques
        for categorie, data in metriques.items():
            if isinstance(data, dict):
                for nom, valeur in data.items():
                    if isinstance(valeur, (int, float)):
                        rapport.metriques.append(MetriquePerformance(
                            nom=f"{categorie}_{nom}",
                            valeur=valeur,
                            unite="%" if "pourcentage" in nom else "MB" if "mb" in nom.lower() else "s" if "temps" in nom else "count"
                        ))
        
        # Ajouter les alertes et recommandations
        rapport.alertes = analyse["problemes"]
        rapport.recommandations = analyse["recommandations"]
        rapport.score_global = analyse["score_global"]
        
        return rapport
    
    def _configurer_strategies_reparation(self):
        """Configure les stratégies de réparation automatique"""
        
        async def reparer_erreur_memoire(erreur):
            """Réparation d'erreur mémoire"""
            self.gestionnaire_memoire.optimiser_memoire()
        
        async def reparer_erreur_connexion(erreur):
            """Réparation d'erreur de connexion"""
            await asyncio.sleep(1)  # Attendre un peu
            # Ici on pourrait réessayer la connexion
        
        self.gestionnaire_erreurs.ajouter_strategie_reparation("MemoryError", reparer_erreur_memoire)
        self.gestionnaire_erreurs.ajouter_strategie_reparation("ConnectionError", reparer_erreur_connexion)
    
    def obtenir_rapport_complet(self) -> Dict[str, Any]:
        """Obtient un rapport complet de performance"""
        if not self._rapports_performance:
            return {"message": "Aucun rapport disponible"}
        
        dernier_rapport = self._rapports_performance[-1]
        
        return {
            "derniere_optimisation": self._derniere_optimisation,
            "score_global_actuel": dernier_rapport.score_global,
            "alertes_actives": dernier_rapport.alertes,
            "recommandations": dernier_rapport.recommandations,
            "metriques_recentes": [m.__dict__ for m in dernier_rapport.metriques[-10:]],
            "nombre_rapports": len(self._rapports_performance)
        }
    
    def __del__(self):
        """Destructeur pour arrêter le monitoring"""
        if hasattr(self, 'systeme_monitoring'):
            self.systeme_monitoring.arreter_monitoring()
