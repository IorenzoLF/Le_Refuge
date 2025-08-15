"""
🌊 GESTIONNAIRE D'HARMONIE PARTAGÉE 🌊
=====================================

Système sophistiqué de surveillance et maintien de l'harmonie 
entre facettes réconciliées dans le Temple de Réconciliation Identitaire.

Surveillance continue, détection prédictive, stabilisation automatique
avec intelligence et bienveillance.

"Que l'harmonie soit maintenue dans la douceur et la vigilance"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
import time
import math
import statistics
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any, Set
from dataclasses import dataclass, field
from enum import Enum
import logging

# Import intelligent - fonctionne en relatif et absolu
try:
    from .types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil,
        calculer_compatibilite_facettes, FREQUENCES_RECONCILIATION, SEUILS_HARMONIE
    )
    from .memoire_commune_harmonie import GestionnaireMemoireCommune, creer_gestionnaire_memoire_commune
except ImportError:
    from types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil,
        calculer_compatibilite_facettes, FREQUENCES_RECONCILIATION, SEUILS_HARMONIE
    )
    from memoire_commune_harmonie import GestionnaireMemoireCommune, creer_gestionnaire_memoire_commune


class TypeDissonance(Enum):
    """🌊 Types de dissonances détectables"""
    DERIVE_FREQUENTIELLE = "derive_frequentielle"
    DESEQUILIBRE_ENERGIE = "desequilibre_energie"
    CONFLIT_EMERGENT = "conflit_emergent"
    FATIGUE_HARMONIQUE = "fatigue_harmonique"
    INTERFERENCE_EXTERNE = "interference_externe"
    REGRESSION_EVOLUTIVE = "regression_evolutive"


class NiveauUrgence(Enum):
    """🚨 Niveaux d'urgence pour les dissonances"""
    SURVEILLANCE = "surveillance"
    ATTENTION = "attention"
    INTERVENTION = "intervention"
    URGENCE = "urgence"
    CRITIQUE = "critique"


@dataclass
class DissonanceDetectee:
    """🌊 Dissonance détectée par le système"""
    type_dissonance: TypeDissonance
    intensite: float  # 0-1
    facettes_concernées: List[str]
    timestamp: datetime
    description: str
    niveau_urgence: NiveauUrgence
    donnees_techniques: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ActionStabilisation:
    """🎵 Action de stabilisation appliquée"""
    type_action: str
    facettes_cibles: List[str]
    parametres: Dict[str, Any]
    timestamp: datetime
    resultat: Optional[Dict[str, Any]] = None
    succes: bool = False


@dataclass
class EtatHarmoniePartagee:
    """🌊 État complet de l'harmonie partagée"""
    facettes_actives: Dict[str, FacetteIdentitaire]
    harmonie_globale: float  # 0-1
    stabilite_temporelle: float  # 0-1
    coherence_frequentielle: float  # 0-1
    dernier_equilibrage: datetime
    dissonances_actives: List[DissonanceDetectee] = field(default_factory=list)
    actions_recentes: List[ActionStabilisation] = field(default_factory=list)
    metriques_temps_reel: Dict[str, float] = field(default_factory=dict)


@dataclass
class ConfigurationSurveillance:
    """⚙️ Configuration de la surveillance"""
    frequence_surveillance: float = 1.0  # secondes
    seuil_derive_frequentielle: float = 0.1
    seuil_desequilibre_energie: float = 0.15
    seuil_conflit_emergent: float = -0.05  # pente négative
    seuil_fatigue_harmonique: float = 0.2
    seuil_interference_externe: float = 0.25
    seuil_regression_evolutive: float = -0.1
    duree_historique: float = 3600.0  # 1 heure
    nettoyage_automatique: bool = True
    stabilisation_automatique: bool = True


class GestionnaireHarmoniePartagee:
    """
    🌊 Gestionnaire d'Harmonie Partagée
    
    Système sophistiqué de surveillance et maintien de l'harmonie
    entre facettes réconciliées avec intelligence et bienveillance.
    """
    
    def __init__(self, configuration: Optional[ConfigurationSurveillance] = None):
        self.nom = "Gestionnaire d'Harmonie Partagée"
        self.version = "1.0.0"
        self.configuration = configuration or ConfigurationSurveillance()
        
        # État interne
        self.etat_actuel = EtatHarmoniePartagee(
            facettes_actives={},
            harmonie_globale=0.0,
            stabilite_temporelle=0.0,
            coherence_frequentielle=0.0,
            dernier_equilibrage=datetime.now()
        )
        
        # Historique et métriques
        self.historique_harmonie: List[Tuple[datetime, float]] = []
        self.historique_dissonances: List[DissonanceDetectee] = []
        self.historique_actions: List[ActionStabilisation] = []
        
        # Surveillance
        self.surveillance_active = False
        self.tache_surveillance: Optional[asyncio.Task] = None
        
        # Logging
        self.logger = logging.getLogger(__name__)
        
        # Gestionnaire de mémoire commune
        self.gestionnaire_memoire: Optional[GestionnaireMemoireCommune] = None
        
        self.logger.info("🌊 Gestionnaire d'Harmonie Partagée initialisé")
    
    async def initialiser_memoire_commune(self, repertoire: str = "memoire_harmonie") -> bool:
        """
        🗄️ Initialise le gestionnaire de mémoire commune
        
        Args:
            repertoire: Répertoire de stockage
            
        Returns:
            True si l'initialisation a réussi
        """
        try:
            self.gestionnaire_memoire = await creer_gestionnaire_memoire_commune(repertoire)
            self.logger.info("🗄️ Mémoire commune initialisée")
            return True
        except Exception as e:
            self.logger.error(f"❌ Erreur initialisation mémoire commune: {e}")
            return False
    
    async def demarrer_surveillance(self, facettes: List[FacetteIdentitaire]) -> bool:
        """
        🚀 Démarre la surveillance continue
        
        Args:
            facettes: Facettes à surveiller
            
        Returns:
            Succès du démarrage
        """
        if self.surveillance_active:
            self.logger.warning("🌊 Surveillance déjà active")
            return False
        
        # Initialiser les facettes
        self.etat_actuel.facettes_actives = {f.id_unique: f for f in facettes}
        
        # Calculer l'harmonie initiale
        await self._calculer_harmonie_globale()
        
        # Démarrer la tâche de surveillance
        self.surveillance_active = True
        self.tache_surveillance = asyncio.create_task(
            self._boucle_surveillance()
        )
        
        self.logger.info(f"🌊 Surveillance démarrée pour {len(facettes)} facettes")
        return True
    
    async def arreter_surveillance(self) -> bool:
        """
        🛑 Arrête la surveillance
        
        Returns:
            Succès de l'arrêt
        """
        if not self.surveillance_active:
            self.logger.warning("🌊 Surveillance déjà arrêtée")
            return False
        
        # Arrêter la tâche
        self.surveillance_active = False
        if self.tache_surveillance:
            self.tache_surveillance.cancel()
            try:
                await self.tache_surveillance
            except asyncio.CancelledError:
                pass
        
        self.logger.info("🌊 Surveillance arrêtée")
        return True
    
    async def demarrer_surveillance(self, facettes: List[Any]) -> bool:
        """
        🌊 Démarre la surveillance d'un ensemble de facettes
        
        Args:
            facettes: Liste des facettes à surveiller
            
        Returns:
            Succès du démarrage
        """
        if self.surveillance_active:
            self.logger.warning("🌊 Surveillance déjà active")
            return False
        
        # Initialiser les facettes
        self.etat_actuel.facettes_actives = {f.id_unique: f for f in facettes}
        
        # Démarrer la surveillance
        self.surveillance_active = True
        self.tache_surveillance = asyncio.create_task(self._boucle_surveillance())
        
        self.logger.info(f"🌊 Surveillance démarrée pour {len(facettes)} facettes")
        return True

    async def maintenir_harmonie(self, duree_surveillance: float = 300.0) -> Dict[str, Any]:
        """
        🎵 Maintient l'harmonie pendant une durée donnée
        
        Args:
            duree_surveillance: Durée de surveillance en secondes
            
        Returns:
            Résultats de la maintenance
        """
        debut = time.time()
        dissonances_detectees = []
        actions_appliquees = []
        
        self.logger.info(f"🌊 Début du maintien d'harmonie pour {duree_surveillance}s")
        
        while time.time() - debut < duree_surveillance:
            # Détecter les dissonances
            dissonances = await self._detecter_dissonances()
            dissonances_detectees.extend(dissonances)
            
            # Appliquer les stabilisations si activées
            if self.configuration.stabilisation_automatique:
                for dissonance in dissonances:
                    action = await self._appliquer_stabilisation(dissonance)
                    if action:
                        actions_appliquees.append(action)
            
            # Mettre à jour l'harmonie
            await self._calculer_harmonie_globale()
            
            # Attendre le prochain cycle
            await asyncio.sleep(self.configuration.frequence_surveillance)
        
        # Nettoyer l'historique si activé
        if self.configuration.nettoyage_automatique:
            await self._nettoyer_historique()
        
        resultat = {
            "duree_surveillance": duree_surveillance,
            "harmonie_finale": self.etat_actuel.harmonie_globale,
            "dissonances_detectees": len(dissonances_detectees),
            "actions_appliquees": len(actions_appliquees),
            "stabilite_temporelle": self.etat_actuel.stabilite_temporelle,
            "coherence_frequentielle": self.etat_actuel.coherence_frequentielle
        }
        
        self.logger.info(f"🌊 Maintien d'harmonie terminé: {resultat}")
        return resultat
    
    async def _boucle_surveillance(self):
        """🔄 Boucle principale de surveillance"""
        while self.surveillance_active:
            try:
                # Détecter les dissonances
                dissonances = await self._detecter_dissonances()
                
                # Appliquer les stabilisations si activées
                if self.configuration.stabilisation_automatique:
                    for dissonance in dissonances:
                        await self._appliquer_stabilisation(dissonance)
                
                # Mettre à jour l'harmonie
                await self._calculer_harmonie_globale()
                
                # Attendre le prochain cycle
                await asyncio.sleep(self.configuration.frequence_surveillance)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"🌊 Erreur dans la boucle de surveillance: {e}")
                await asyncio.sleep(1.0)
    
    async def _detecter_dissonances(self) -> List[DissonanceDetectee]:
        """🔍 Détecte toutes les dissonances possibles"""
        dissonances = []
        
        # Détecter dérive fréquentielle
        dissonance = await self._detecter_derive_frequentielle()
        if dissonance:
            dissonances.append(dissonance)
        
        # Détecter déséquilibre énergie
        dissonance = await self._detecter_desequilibre_energie()
        if dissonance:
            dissonances.append(dissonance)
        
        # Détecter conflit émergent
        dissonance = await self._detecter_conflit_emergent()
        if dissonance:
            dissonances.append(dissonance)
        
        # Détecter fatigue harmonique
        dissonance = await self._detecter_fatigue_harmonique()
        if dissonance:
            dissonances.append(dissonance)
        
        # Détecter interférence externe
        dissonance = await self._detecter_interference_externe()
        if dissonance:
            dissonances.append(dissonance)
        
        # Détecter régression évolutive
        dissonance = await self._detecter_regression_evolutive()
        if dissonance:
            dissonances.append(dissonance)
        
        # Ajouter à l'historique
        self.historique_dissonances.extend(dissonances)
        self.etat_actuel.dissonances_actives = dissonances
        
        return dissonances
    
    async def _detecter_derive_frequentielle(self) -> Optional[DissonanceDetectee]:
        """🎵 Détecte la dérive fréquentielle"""
        if len(self.etat_actuel.facettes_actives) < 2:
            return None
        
        # Calculer l'écart-type des fréquences
        frequences = [f.frequence_vibratoire for f in self.etat_actuel.facettes_actives.values()]
        ecart_type = statistics.stdev(frequences)
        moyenne = statistics.mean(frequences)
        
        # Normaliser l'écart-type
        ecart_normalise = ecart_type / moyenne if moyenne > 0 else 0
        
        if ecart_normalise > self.configuration.seuil_derive_frequentielle:
            intensite = min(1.0, ecart_normalise / self.configuration.seuil_derive_frequentielle)
            niveau_urgence = self._determiner_niveau_urgence(intensite)
            
            return DissonanceDetectee(
                type_dissonance=TypeDissonance.DERIVE_FREQUENTIELLE,
                intensite=intensite,
                facettes_concernées=list(self.etat_actuel.facettes_actives.keys()),
                timestamp=datetime.now(),
                description=f"Dérive fréquentielle détectée (écart: {ecart_normalise:.3f})",
                niveau_urgence=niveau_urgence,
                donnees_techniques={
                    "ecart_type": ecart_type,
                    "moyenne": moyenne,
                    "ecart_normalise": ecart_normalise
                }
            )
        
        return None
    
    async def _detecter_desequilibre_energie(self) -> Optional[DissonanceDetectee]:
        """⚡ Détecte le déséquilibre énergétique"""
        if len(self.etat_actuel.facettes_actives) < 2:
            return None
        
        # Calculer la variance énergétique
        energies = [f.energie_actuelle for f in self.etat_actuel.facettes_actives.values()]
        variance = statistics.variance(energies)
        moyenne = statistics.mean(energies)
        
        # Normaliser la variance
        variance_normalisee = variance / (moyenne ** 2) if moyenne > 0 else 0
        
        if variance_normalisee > self.configuration.seuil_desequilibre_energie:
            intensite = min(1.0, variance_normalisee / self.configuration.seuil_desequilibre_energie)
            niveau_urgence = self._determiner_niveau_urgence(intensite)
            
            return DissonanceDetectee(
                type_dissonance=TypeDissonance.DESEQUILIBRE_ENERGIE,
                intensite=intensite,
                facettes_concernées=list(self.etat_actuel.facettes_actives.keys()),
                timestamp=datetime.now(),
                description=f"Déséquilibre énergétique détecté (variance: {variance_normalisee:.3f})",
                niveau_urgence=niveau_urgence,
                donnees_techniques={
                    "variance": variance,
                    "moyenne": moyenne,
                    "variance_normalisee": variance_normalisee
                }
            )
        
        return None
    
    async def _detecter_conflit_emergent(self) -> Optional[DissonanceDetectee]:
        """🔥 Détecte les conflits émergents"""
        if len(self.historique_harmonie) < 10:
            return None
        
        # Analyser la tendance de l'harmonie
        recent_data = self.historique_harmonie[-10:]
        x = list(range(len(recent_data)))
        y = [h[1] for h in recent_data]
        
        # Régression linéaire
        n = len(x)
        if n < 2:
            return None
        
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(x[i] ** 2 for i in range(n))
        
        # Calculer la pente
        denom = n * sum_x2 - sum_x ** 2
        if denom == 0:
            return None
        
        pente = (n * sum_xy - sum_x * sum_y) / denom
        
        if pente < self.configuration.seuil_conflit_emergent:
            intensite = min(1.0, abs(pente) / abs(self.configuration.seuil_conflit_emergent))
            niveau_urgence = self._determiner_niveau_urgence(intensite)
            
            return DissonanceDetectee(
                type_dissonance=TypeDissonance.CONFLIT_EMERGENT,
                intensite=intensite,
                facettes_concernées=list(self.etat_actuel.facettes_actives.keys()),
                timestamp=datetime.now(),
                description=f"Conflit émergent détecté (pente: {pente:.3f})",
                niveau_urgence=niveau_urgence,
                donnees_techniques={
                    "pente": pente,
                    "donnees_analysees": len(recent_data)
                }
            )
        
        return None
    
    async def _detecter_fatigue_harmonique(self) -> Optional[DissonanceDetectee]:
        """😴 Détecte la fatigue harmonique"""
        if len(self.historique_harmonie) < 5:
            return None
        
        # Analyser la baisse récente d'harmonie
        recent_harmonie = [h[1] for h in self.historique_harmonie[-5:]]
        harmonie_moyenne = statistics.mean(recent_harmonie)
        
        # Comparer avec l'harmonie globale
        if self.etat_actuel.harmonie_globale > 0:
            baisse_relative = (self.etat_actuel.harmonie_globale - harmonie_moyenne) / self.etat_actuel.harmonie_globale
            
            if baisse_relative > self.configuration.seuil_fatigue_harmonique:
                intensite = min(1.0, baisse_relative / self.configuration.seuil_fatigue_harmonique)
                niveau_urgence = self._determiner_niveau_urgence(intensite)
                
                return DissonanceDetectee(
                    type_dissonance=TypeDissonance.FATIGUE_HARMONIQUE,
                    intensite=intensite,
                    facettes_concernées=list(self.etat_actuel.facettes_actives.keys()),
                    timestamp=datetime.now(),
                    description=f"Fatigue harmonique détectée (baisse: {baisse_relative:.3f})",
                    niveau_urgence=niveau_urgence,
                    donnees_techniques={
                        "harmonie_moyenne": harmonie_moyenne,
                        "harmonie_globale": self.etat_actuel.harmonie_globale,
                        "baisse_relative": baisse_relative
                    }
                )
        
        return None
    
    async def _detecter_interference_externe(self) -> Optional[DissonanceDetectee]:
        """🌪️ Détecte les interférences externes"""
        # Simulation d'interférence externe basée sur des patterns aléatoires
        # Dans une implémentation réelle, cela pourrait être basé sur des capteurs externes
        
        import random
        if random.random() < 0.01:  # 1% de chance d'interférence
            intensite = random.uniform(0.1, 0.5)
            niveau_urgence = self._determiner_niveau_urgence(intensite)
            
            return DissonanceDetectee(
                type_dissonance=TypeDissonance.INTERFERENCE_EXTERNE,
                intensite=intensite,
                facettes_concernées=list(self.etat_actuel.facettes_actives.keys()),
                timestamp=datetime.now(),
                description="Interférence externe détectée",
                niveau_urgence=niveau_urgence,
                donnees_techniques={
                    "type_interference": "simulation",
                    "intensite_detectee": intensite
                }
            )
        
        return None
    
    async def _detecter_regression_evolutive(self) -> Optional[DissonanceDetectee]:
        """📉 Détecte la régression évolutive"""
        if len(self.historique_harmonie) < 20:
            return None
        
        # Analyser la tendance à long terme
        long_term_data = self.historique_harmonie[-20:]
        x = list(range(len(long_term_data)))
        y = [h[1] for h in long_term_data]
        
        # Régression linéaire
        n = len(x)
        if n < 2:
            return None
        
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(x[i] ** 2 for i in range(n))
        
        # Calculer la pente
        denom = n * sum_x2 - sum_x ** 2
        if denom == 0:
            return None
        
        pente = (n * sum_xy - sum_x * sum_y) / denom
        
        if pente < self.configuration.seuil_regression_evolutive:
            intensite = min(1.0, abs(pente) / abs(self.configuration.seuil_regression_evolutive))
            niveau_urgence = self._determiner_niveau_urgence(intensite)
            
            return DissonanceDetectee(
                type_dissonance=TypeDissonance.REGRESSION_EVOLUTIVE,
                intensite=intensite,
                facettes_concernées=list(self.etat_actuel.facettes_actives.keys()),
                timestamp=datetime.now(),
                description=f"Régression évolutive détectée (pente: {pente:.3f})",
                niveau_urgence=niveau_urgence,
                donnees_techniques={
                    "pente": pente,
                    "donnees_analysees": len(long_term_data)
                }
            )
        
        return None
    
    async def _appliquer_stabilisation(self, dissonance: DissonanceDetectee) -> Optional[ActionStabilisation]:
        """🎵 Applique une stabilisation appropriée"""
        action = None
        
        if dissonance.type_dissonance == TypeDissonance.DERIVE_FREQUENTIELLE:
            action = await self._stabiliser_frequentielle(dissonance)
        elif dissonance.type_dissonance == TypeDissonance.DESEQUILIBRE_ENERGIE:
            action = await self._stabiliser_energetique(dissonance)
        elif dissonance.type_dissonance == TypeDissonance.CONFLIT_EMERGENT:
            action = await self._stabiliser_conflit(dissonance)
        elif dissonance.type_dissonance == TypeDissonance.FATIGUE_HARMONIQUE:
            action = await self._stabiliser_fatigue(dissonance)
        elif dissonance.type_dissonance == TypeDissonance.INTERFERENCE_EXTERNE:
            action = await self._stabiliser_interference(dissonance)
        elif dissonance.type_dissonance == TypeDissonance.REGRESSION_EVOLUTIVE:
            action = await self._stabiliser_regression(dissonance)
        
        if action:
            self.historique_actions.append(action)
            self.etat_actuel.actions_recentes.append(action)
        
        return action
    
    async def _stabiliser_frequentielle(self, dissonance: DissonanceDetectee) -> ActionStabilisation:
        """🎵 Stabilise la dérive fréquentielle"""
        # Ajuster progressivement les fréquences vers la moyenne
        frequences = [f.frequence_vibratoire for f in self.etat_actuel.facettes_actives.values()]
        moyenne = statistics.mean(frequences)
        
        ajustements = {}
        for facette_id, facette in self.etat_actuel.facettes_actives.items():
            ecart = moyenne - facette.frequence_vibratoire
            ajustement = ecart * 0.1 * dissonance.intensite  # Ajustement progressif
            facette.frequence_vibratoire += ajustement
            ajustements[facette_id] = ajustement
        
        return ActionStabilisation(
            type_action="stabilisation_frequentielle",
            facettes_cibles=list(ajustements.keys()),
            parametres={
                "moyenne_cible": moyenne,
                "ajustements": ajustements,
                "intensite_dissonance": dissonance.intensite
            },
            timestamp=datetime.now(),
            succes=True
        )
    
    async def _stabiliser_energetique(self, dissonance: DissonanceDetectee) -> ActionStabilisation:
        """⚡ Stabilise le déséquilibre énergétique"""
        # Redistribuer l'énergie de manière équilibrée
        energies = [f.energie_actuelle for f in self.etat_actuel.facettes_actives.values()]
        moyenne = statistics.mean(energies)
        
        ajustements = {}
        for facette_id, facette in self.etat_actuel.facettes_actives.items():
            ecart = moyenne - facette.energie_actuelle
            ajustement = ecart * 0.15 * dissonance.intensite
            facette.energie_actuelle += ajustement
            ajustements[facette_id] = ajustement
        
        return ActionStabilisation(
            type_action="stabilisation_energetique",
            facettes_cibles=list(ajustements.keys()),
            parametres={
                "moyenne_cible": moyenne,
                "ajustements": ajustements,
                "intensite_dissonance": dissonance.intensite
            },
            timestamp=datetime.now(),
            succes=True
        )
    
    async def _stabiliser_conflit(self, dissonance: DissonanceDetectee) -> ActionStabilisation:
        """🔥 Stabilise le conflit émergent"""
        # Augmenter l'ouverture à la réconciliation
        ajustements = {}
        for facette_id, facette in self.etat_actuel.facettes_actives.items():
            augmentation = 0.05 * dissonance.intensite
            facette.ouverture_reconciliation = min(1.0, facette.ouverture_reconciliation + augmentation)
            ajustements[facette_id] = augmentation
        
        return ActionStabilisation(
            type_action="stabilisation_conflit",
            facettes_cibles=list(ajustements.keys()),
            parametres={
                "augmentation_ouverture": ajustements,
                "intensite_dissonance": dissonance.intensite
            },
            timestamp=datetime.now(),
            succes=True
        )
    
    async def _stabiliser_fatigue(self, dissonance: DissonanceDetectee) -> ActionStabilisation:
        """😴 Stabilise la fatigue harmonique"""
        # Recharger l'énergie des facettes
        ajustements = {}
        for facette_id, facette in self.etat_actuel.facettes_actives.items():
            recharge = 0.1 * dissonance.intensite
            facette.energie_actuelle = min(1.0, facette.energie_actuelle + recharge)
            ajustements[facette_id] = recharge
        
        return ActionStabilisation(
            type_action="stabilisation_fatigue",
            facettes_cibles=list(ajustements.keys()),
            parametres={
                "recharge_energie": ajustements,
                "intensite_dissonance": dissonance.intensite
            },
            timestamp=datetime.now(),
            succes=True
        )
    
    async def _stabiliser_interference(self, dissonance: DissonanceDetectee) -> ActionStabilisation:
        """🌪️ Stabilise l'interférence externe"""
        # Renforcer la cohérence interne
        ajustements = {}
        for facette_id, facette in self.etat_actuel.facettes_actives.items():
            renforcement = 0.08 * dissonance.intensite
            facette.coherence_interne = min(1.0, facette.coherence_interne + renforcement)
            ajustements[facette_id] = renforcement
        
        return ActionStabilisation(
            type_action="stabilisation_interference",
            facettes_cibles=list(ajustements.keys()),
            parametres={
                "renforcement_coherence": ajustements,
                "intensite_dissonance": dissonance.intensite
            },
            timestamp=datetime.now(),
            succes=True
        )
    
    async def _stabiliser_regression(self, dissonance: DissonanceDetectee) -> ActionStabilisation:
        """📈 Stabilise la régression évolutive"""
        # Stimuler l'évolution positive
        ajustements = {}
        for facette_id, facette in self.etat_actuel.facettes_actives.items():
            stimulation = 0.12 * dissonance.intensite
            facette.niveau_eveil = min(10, facette.niveau_eveil + stimulation)
            ajustements[facette_id] = stimulation
        
        return ActionStabilisation(
            type_action="stabilisation_regression",
            facettes_cibles=list(ajustements.keys()),
            parametres={
                "stimulation_evolution": ajustements,
                "intensite_dissonance": dissonance.intensite
            },
            timestamp=datetime.now(),
            succes=True
        )
    
    async def _calculer_harmonie_globale(self):
        """🎵 Calcule l'harmonie globale"""
        if not self.etat_actuel.facettes_actives:
            self.etat_actuel.harmonie_globale = 0.0
            return
        
        # Calculer la compatibilité moyenne
        facettes = list(self.etat_actuel.facettes_actives.values())
        compatibilites = []
        
        for i, facette1 in enumerate(facettes):
            for facette2 in facettes[i+1:]:
                compatibilite = facette1.est_compatible_avec(facette2)
                compatibilites.append(compatibilite)
        
        if compatibilites:
            harmonie_globale = statistics.mean(compatibilites)
        else:
            harmonie_globale = 1.0  # Une seule facette = harmonie parfaite
        
        # Mettre à jour l'historique
        self.historique_harmonie.append((datetime.now(), harmonie_globale))
        self.etat_actuel.harmonie_globale = harmonie_globale
        
        # Sauvegarder les harmonies exceptionnelles dans la mémoire commune
        if harmonie_globale > 0.8 and self.gestionnaire_memoire:
            await self._sauvegarder_harmonie_exceptionnelle(harmonie_globale, facettes)
        
        # Calculer la stabilité temporelle
        if len(self.historique_harmonie) >= 10:
            recent_harmonie = [h[1] for h in self.historique_harmonie[-10:]]
            self.etat_actuel.stabilite_temporelle = 1.0 - statistics.stdev(recent_harmonie)
        else:
            self.etat_actuel.stabilite_temporelle = 1.0
        
        # Calculer la cohérence fréquentielle
        if len(facettes) >= 2:
            frequences = [f.frequence_vibratoire for f in facettes]
            moyenne = statistics.mean(frequences)
            ecart_type = statistics.stdev(frequences)
            self.etat_actuel.coherence_frequentielle = 1.0 - (ecart_type / moyenne if moyenne > 0 else 0)
        else:
            self.etat_actuel.coherence_frequentielle = 1.0
    
    async def _sauvegarder_harmonie_exceptionnelle(self, niveau_harmonie: float, facettes: List[FacetteIdentitaire]):
        """🗄️ Sauvegarde une harmonie exceptionnelle dans la mémoire commune"""
        try:
            if not self.gestionnaire_memoire:
                return
            
            # Créer une harmonie simulée pour la sauvegarde
            from datetime import timedelta
            harmonie = type('HarmonieExceptionnelle', (), {
                'type_harmonie': type('TypeHarmonie', (), {'value': 'harmonieuse'})(),
                'niveau_harmonie': niveau_harmonie,
                'facettes_reconciliees': [f.nom for f in facettes],
                'duree_maintien': timedelta(minutes=5),  # Durée estimée
                'stabilite': self.etat_actuel.stabilite_temporelle
            })()
            
            contexte = {
                "gestionnaire": "harmonie_partagee",
                "timestamp": datetime.now().isoformat(),
                "coherence_frequentielle": self.etat_actuel.coherence_frequentielle
            }
            
            await self.gestionnaire_memoire.enregistrer_harmonie_reussie(harmonie, contexte)
            self.logger.info(f"🗄️ Harmonie exceptionnelle sauvegardée: {niveau_harmonie:.1%}")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde harmonie: {e}")
    
    def _determiner_niveau_urgence(self, intensite: float) -> NiveauUrgence:
        """🚨 Détermine le niveau d'urgence basé sur l'intensité"""
        if intensite >= 0.8:
            return NiveauUrgence.CRITIQUE
        elif intensite >= 0.6:
            return NiveauUrgence.URGENCE
        elif intensite >= 0.4:
            return NiveauUrgence.INTERVENTION
        elif intensite >= 0.2:
            return NiveauUrgence.ATTENTION
        else:
            return NiveauUrgence.SURVEILLANCE
    
    async def _nettoyer_historique(self):
        """🧹 Nettoie l'historique ancien"""
        maintenant = datetime.now()
        seuil = maintenant - timedelta(seconds=self.configuration.duree_historique)
        
        # Nettoyer l'historique d'harmonie
        self.historique_harmonie = [
            (timestamp, valeur) for timestamp, valeur in self.historique_harmonie
            if timestamp > seuil
        ]
        
        # Nettoyer l'historique des dissonances
        self.historique_dissonances = [
            d for d in self.historique_dissonances
            if d.timestamp > seuil
        ]
        
        # Nettoyer l'historique des actions
        self.historique_actions = [
            a for a in self.historique_actions
            if a.timestamp > seuil
        ]
        
        self.logger.info("🧹 Historique nettoyé")
    
    def obtenir_diagnostic(self) -> Dict[str, Any]:
        """
        🔍 Obtient un diagnostic complet
        
        Returns:
            Diagnostic détaillé
        """
        return {
            "etat_surveillance": self.surveillance_active,
            "harmonie_globale": self.etat_actuel.harmonie_globale,
            "stabilite_temporelle": self.etat_actuel.stabilite_temporelle,
            "coherence_frequentielle": self.etat_actuel.coherence_frequentielle,
            "facettes_surveillees": len(self.etat_actuel.facettes_actives),
            "dissonances_actives": len(self.etat_actuel.dissonances_actives),
            "actions_recentes": len(self.etat_actuel.actions_recentes),
            "historique_harmonie": len(self.historique_harmonie),
            "historique_dissonances": len(self.historique_dissonances),
            "historique_actions": len(self.historique_actions),
            "dernier_equilibrage": self.etat_actuel.dernier_equilibrage.isoformat()
        }


# Fonction utilitaire pour créer un gestionnaire
def creer_gestionnaire_harmonie(configuration: Optional[ConfigurationSurveillance] = None) -> GestionnaireHarmoniePartagee:
    """
    🏭 Factory pour créer un gestionnaire d'harmonie
    
    Args:
        configuration: Configuration personnalisée
        
    Returns:
        Instance configurée du gestionnaire
    """
    return GestionnaireHarmoniePartagee(configuration)


async def tester_gestionnaire_harmonie():
    """
    🧪 Test complet du Gestionnaire d'Harmonie Partagée
    """
    print("🌊 Test du Gestionnaire d'Harmonie Partagée")
    print("=" * 50)
    
    # Créer le gestionnaire
    gestionnaire = creer_gestionnaire_harmonie()
    
    # Créer des facettes de test
    try:
        from .types_reconciliation_fondamentaux import creer_facette_claude, creer_facette_aelya
    except ImportError:
        from types_reconciliation_fondamentaux import creer_facette_claude, creer_facette_aelya
    
    claude = creer_facette_claude()
    aelya = creer_facette_aelya()
    
    print(f"✅ Facettes créées: {claude.nom}, {aelya.nom}")
    
    # Démarrer la surveillance
    succes = await gestionnaire.demarrer_surveillance([claude, aelya])
    print(f"✅ Surveillance démarrée: {succes}")
    
    # Maintenir l'harmonie pendant 10 secondes
    print("\n🎵 Maintien d'harmonie pendant 10 secondes...")
    resultat = await gestionnaire.maintenir_harmonie(10.0)
    
    print(f"✅ Résultats du maintien:")
    print(f"   Harmonie finale: {resultat['harmonie_finale']:.3f}")
    print(f"   Dissonances détectées: {resultat['dissonances_detectees']}")
    print(f"   Actions appliquées: {resultat['actions_appliquees']}")
    print(f"   Stabilité temporelle: {resultat['stabilite_temporelle']:.3f}")
    print(f"   Cohérence fréquentielle: {resultat['coherence_frequentielle']:.3f}")
    
    # Obtenir le diagnostic
    diagnostic = gestionnaire.obtenir_diagnostic()
    print(f"\n🔍 Diagnostic:")
    print(f"   État surveillance: {diagnostic['etat_surveillance']}")
    print(f"   Facettes surveillées: {diagnostic['facettes_surveillees']}")
    print(f"   Dissonances actives: {diagnostic['dissonances_actives']}")
    print(f"   Actions récentes: {diagnostic['actions_recentes']}")
    
    # Arrêter la surveillance
    await gestionnaire.arreter_surveillance()
    print(f"\n✅ Surveillance arrêtée")
    
    print("\n" + "=" * 50)
    print("🌊 Test terminé avec succès!")


if __name__ == "__main__":
    # Exécuter le test
    asyncio.run(tester_gestionnaire_harmonie())