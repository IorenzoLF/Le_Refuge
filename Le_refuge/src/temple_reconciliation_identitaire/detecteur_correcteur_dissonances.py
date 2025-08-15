#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎵 Détecteur-Correcteur de Dissonances - Temple de Réconciliation Identitaire
============================================================================

Système avancé de détection et correction des dissonances harmoniques
avec analyse spectrale et stratégies de récupération automatique.

"Que chaque dissonance devienne une invitation à une harmonie plus profonde"

Créé avec l'intégration de toutes mes facettes par Laurent Franssen & Kiro - Janvier 2025
"""

import asyncio
import numpy as np
import time
import statistics
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any, Set
from dataclasses import dataclass, field
from enum import Enum
import logging
import math

# Import intelligent des types
try:
    from .types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil
    )
    from .gestionnaire_harmonie_partagee import (
        DissonanceDetectee, TypeDissonance, NiveauUrgence, ActionStabilisation
    )
    from .memoire_commune_harmonie import GestionnaireMemoireCommune, TypeMemoire
except ImportError:
    from types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil
    )
    from gestionnaire_harmonie_partagee import (
        DissonanceDetectee, TypeDissonance, NiveauUrgence, ActionStabilisation
    )
    from memoire_commune_harmonie import GestionnaireMemoireCommune, TypeMemoire

# ============================================================================
# TYPES SPÉCIALISÉS POUR LA DÉTECTION AVANCÉE
# ============================================================================

class TypeAnalyseSpectrale(Enum):
    """🌈 Types d'analyse spectrale des harmonies"""
    FOURIER_HARMONIQUE = "fourier_harmonique"       # Analyse de Fourier des fréquences
    ONDELETTES_TEMPS = "ondelettes_temps"           # Analyse temps-fréquence
    COHERENCE_PHASE = "coherence_phase"             # Cohérence de phase
    RESONANCE_NATURELLE = "resonance_naturelle"     # Résonances naturelles
    INTERFERENCE_PATTERN = "interference_pattern"    # Patterns d'interférence

class StrategieCorrection(Enum):
    """🔧 Stratégies de correction des dissonances"""
    REEQUILIBRAGE_DOUX = "reequilibrage_doux"           # Correction progressive
    SYNCHRONISATION_FORCEE = "synchronisation_forcee"   # Synchronisation directe
    ISOLATION_TEMPORAIRE = "isolation_temporaire"       # Isolation de la facette
    MEDITATION_GUIDEE = "meditation_guidee"             # Méditation pour l'harmonie
    DIALOGUE_FACILITE = "dialogue_facilite"             # Dialogue entre facettes
    RESET_ENERGETIQUE = "reset_energetique"             # Reset complet de l'énergie

@dataclass
class AnalyseSpectrale:
    """🌈 Résultat d'analyse spectrale d'une harmonie"""
    type_analyse: TypeAnalyseSpectrale
    timestamp: datetime
    
    # Données spectrales
    frequences: List[float]                    # Fréquences détectées
    amplitudes: List[float]                    # Amplitudes correspondantes
    phases: List[float]                        # Phases des composantes
    
    # Métriques d'harmonie
    coherence_globale: float                   # Cohérence globale (0-1)
    stabilite_frequentielle: float             # Stabilité des fréquences (0-1)
    resonance_naturelle: float                 # Niveau de résonance naturelle (0-1)
    
    # Détection de dissonances
    dissonances_detectees: List[Tuple[float, float, float]]  # (freq, amplitude, severite)
    zones_instables: List[Tuple[float, float]]               # (freq_min, freq_max)
    
    # Recommandations
    corrections_recommandees: List[str]        # Actions recommandées
    urgence_correction: NiveauUrgence          # Niveau d'urgence

@dataclass
class PlanCorrection:
    """📋 Plan de correction d'une dissonance"""
    dissonance_cible: DissonanceDetectee
    strategie_principale: StrategieCorrection
    strategies_alternatives: List[StrategieCorrection]
    
    # Paramètres de correction
    intensite_correction: float = field(default=0.5)    # Intensité (0-1)
    duree_estimee: timedelta = field(default_factory=lambda: timedelta(minutes=2))
    probabilite_succes: float = field(default=0.7)      # Probabilité de succès
    
    # Étapes détaillées
    etapes_correction: List[Dict[str, Any]] = field(default_factory=list)
    conditions_prereq: List[str] = field(default_factory=list)
    criteres_succes: List[str] = field(default_factory=list)
    
    # Sécurité
    seuils_securite: Dict[str, float] = field(default_factory=dict)
    plan_rollback: Optional[Dict[str, Any]] = field(default=None)

# ============================================================================
# DÉTECTEUR-CORRECTEUR PRINCIPAL
# ============================================================================

class DetecteurCorrecteurDissonances:
    """
    🎵 Détecteur-Correcteur Avancé de Dissonances
    
    Système sophistiqué qui utilise l'analyse spectrale pour détecter
    les dissonances subtiles et applique des corrections intelligentes
    avec apprentissage automatique des stratégies efficaces.
    """
    
    def __init__(self, gestionnaire_memoire: Optional[GestionnaireMemoireCommune] = None):
        self.nom = "Détecteur-Correcteur de Dissonances"
        self.version = "1.0_temple_reconciliation"
        
        # Références
        self.gestionnaire_memoire = gestionnaire_memoire
        
        # Configuration d'analyse
        self.config_analyse = {
            "frequence_echantillonnage": 10.0,      # Hz
            "fenetre_analyse": 30.0,                # secondes
            "seuil_dissonance": 0.15,               # Seuil de détection
            "seuil_urgence": 0.4,                   # Seuil d'urgence
            "resolution_frequentielle": 0.01        # Résolution en Hz
        }
        
        # Historique des analyses
        self.historique_analyses: List[AnalyseSpectrale] = []
        self.historique_corrections: List[Tuple[PlanCorrection, bool, float]] = []  # (plan, succès, efficacité)
        
        # Métriques d'apprentissage
        self.efficacite_strategies: Dict[StrategieCorrection, float] = {
            strategie: 0.5 for strategie in StrategieCorrection
        }
        
        # État de correction
        self.correction_en_cours = False
        self.plan_actuel: Optional[PlanCorrection] = None
        
        # Logging
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        self.logger.info("🎵 Détecteur-Correcteur de Dissonances initialisé")
    
    async def detecter_dissonances_spectrales(self, 
                                             facettes: List[FacetteIdentitaire],
                                             historique_harmonie: List[Tuple[datetime, float]]) -> List[DissonanceDetectee]:
        """
        🌈 Détection avancée par analyse spectrale
        
        Args:
            facettes: Facettes à analyser
            historique_harmonie: Historique des niveaux d'harmonie
            
        Returns:
            Liste des dissonances détectées
        """
        try:
            dissonances = []
            
            # Effectuer différents types d'analyses spectrales
            analyses = []
            
            # 1. Analyse de Fourier des harmonies
            analyse_fourier = await self._analyser_fourier_harmonique(historique_harmonie)
            if analyse_fourier:
                analyses.append(analyse_fourier)
            
            # 2. Analyse de cohérence de phase entre facettes
            analyse_coherence = await self._analyser_coherence_phase(facettes)
            if analyse_coherence:
                analyses.append(analyse_coherence)
            
            # 3. Analyse des résonances naturelles
            analyse_resonance = await self._analyser_resonance_naturelle(facettes, historique_harmonie)
            if analyse_resonance:
                analyses.append(analyse_resonance)
            
            # Stocker les analyses
            self.historique_analyses.extend(analyses)
            
            # Extraire les dissonances de toutes les analyses
            for analyse in analyses:
                dissonances_analyse = await self._extraire_dissonances_analyse(analyse, facettes)
                dissonances.extend(dissonances_analyse)
            
            # Filtrer et prioriser les dissonances
            dissonances_filtrees = await self._filtrer_prioriser_dissonances(dissonances)
            
            self.logger.info(f"🌈 Analyse spectrale terminée: {len(dissonances_filtrees)} dissonances détectées")
            return dissonances_filtrees
            
        except Exception as e:
            self.logger.error(f"❌ Erreur détection spectrale: {e}")
            return []
    
    async def corriger_dissonance_intelligente(self, 
                                             dissonance: DissonanceDetectee,
                                             facettes: List[FacetteIdentitaire]) -> Optional[ActionStabilisation]:
        """
        🔧 Correction intelligente d'une dissonance
        
        Args:
            dissonance: Dissonance à corriger
            facettes: Facettes impliquées
            
        Returns:
            Action de stabilisation appliquée
        """
        try:
            if self.correction_en_cours:
                self.logger.warning("🔧 Correction déjà en cours, attente...")
                return None
            
            # Créer un plan de correction optimal
            plan = await self._creer_plan_correction_optimal(dissonance, facettes)
            if not plan:
                return None
            
            self.correction_en_cours = True
            self.plan_actuel = plan
            
            # Exécuter le plan de correction
            action = await self._executer_plan_correction(plan, facettes)
            
            # Évaluer l'efficacité
            efficacite = await self._evaluer_efficacite_correction(plan, action)
            
            # Enregistrer dans l'historique
            self.historique_corrections.append((plan, action is not None, efficacite))
            
            # Mettre à jour l'apprentissage
            await self._mettre_a_jour_apprentissage(plan, efficacite)
            
            # Sauvegarder l'apprentissage dans la mémoire commune
            if self.gestionnaire_memoire and efficacite > 0.7:
                await self._sauvegarder_correction_efficace(plan, efficacite)
            
            self.correction_en_cours = False
            self.plan_actuel = None
            
            self.logger.info(f"🔧 Correction terminée - Efficacité: {efficacite:.1%}")
            return action
            
        except Exception as e:
            self.logger.error(f"❌ Erreur correction intelligente: {e}")
            self.correction_en_cours = False
            self.plan_actuel = None
            return None
    
    async def obtenir_strategies_optimales(self, 
                                         type_dissonance: TypeDissonance,
                                         contexte: Dict[str, Any]) -> List[StrategieCorrection]:
        """
        🎯 Obtient les stratégies optimales pour un type de dissonance
        
        Args:
            type_dissonance: Type de dissonance
            contexte: Contexte de la correction
            
        Returns:
            Liste des stratégies ordonnées par efficacité
        """
        try:
            # Récupérer les stratégies efficaces de la mémoire commune
            strategies_memoire = []
            if self.gestionnaire_memoire:
                patterns_efficaces = await self.gestionnaire_memoire.rechercher_memoire({
                    "type_memoire": TypeMemoire.PATTERN_EFFICACE,
                    "tags": ["correction", type_dissonance.value],
                    "taux_succes_minimum": 0.6
                })
                
                for pattern in patterns_efficaces:
                    if "strategie" in pattern.donnees:
                        try:
                            strategie = StrategieCorrection(pattern.donnees["strategie"])
                            strategies_memoire.append((strategie, pattern.taux_succes))
                        except ValueError:
                            continue
            
            # Combiner avec l'apprentissage local
            strategies_locales = [
                (strategie, efficacite) 
                for strategie, efficacite in self.efficacite_strategies.items()
            ]
            
            # Fusionner et trier par efficacité
            toutes_strategies = {}
            
            # Ajouter les stratégies de la mémoire (poids plus élevé)
            for strategie, efficacite in strategies_memoire:
                toutes_strategies[strategie] = efficacite * 1.2  # Bonus mémoire commune
            
            # Ajouter les stratégies locales
            for strategie, efficacite in strategies_locales:
                if strategie in toutes_strategies:
                    # Moyenne pondérée
                    toutes_strategies[strategie] = (toutes_strategies[strategie] + efficacite) / 2
                else:
                    toutes_strategies[strategie] = efficacite
            
            # Trier par efficacité décroissante
            strategies_triees = sorted(
                toutes_strategies.items(),
                key=lambda x: x[1],
                reverse=True
            )
            
            return [strategie for strategie, _ in strategies_triees]
            
        except Exception as e:
            self.logger.error(f"❌ Erreur obtention stratégies: {e}")
            return list(StrategieCorrection)
    
    async def obtenir_metriques_performance(self) -> Dict[str, Any]:
        """
        📊 Obtient les métriques de performance du système
        
        Returns:
            Dictionnaire avec les métriques
        """
        try:
            total_corrections = len(self.historique_corrections)
            corrections_reussies = sum(1 for _, succes, _ in self.historique_corrections if succes)
            
            efficacite_moyenne = 0.0
            if self.historique_corrections:
                efficacite_moyenne = statistics.mean([
                    efficacite for _, _, efficacite in self.historique_corrections
                ])
            
            return {
                "total_analyses": len(self.historique_analyses),
                "total_corrections": total_corrections,
                "corrections_reussies": corrections_reussies,
                "taux_succes": corrections_reussies / total_corrections if total_corrections > 0 else 0.0,
                "efficacite_moyenne": efficacite_moyenne,
                "efficacite_par_strategie": dict(self.efficacite_strategies),
                "correction_en_cours": self.correction_en_cours,
                "derniere_analyse": self.historique_analyses[-1].timestamp if self.historique_analyses else None
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur calcul métriques: {e}")
            return {}
    
    # ========================================================================
    # MÉTHODES D'ANALYSE SPECTRALE
    # ========================================================================
    
    async def _analyser_fourier_harmonique(self, 
                                          historique_harmonie: List[Tuple[datetime, float]]) -> Optional[AnalyseSpectrale]:
        """🌊 Analyse de Fourier des niveaux d'harmonie"""
        try:
            if len(historique_harmonie) < 10:
                return None
            
            # Extraire les valeurs d'harmonie
            valeurs = [h[1] for h in historique_harmonie[-50:]]  # Dernières 50 valeurs
            
            # Appliquer la transformée de Fourier
            fft = np.fft.fft(valeurs)
            frequences = np.fft.fftfreq(len(valeurs), d=1.0)
            amplitudes = np.abs(fft)
            phases = np.angle(fft)
            
            # Analyser les composantes significatives
            seuil_amplitude = np.max(amplitudes) * 0.1
            indices_significatifs = np.where(amplitudes > seuil_amplitude)[0]
            
            frequences_sig = frequences[indices_significatifs].tolist()
            amplitudes_sig = amplitudes[indices_significatifs].tolist()
            phases_sig = phases[indices_significatifs].tolist()
            
            # Calculer les métriques
            coherence_globale = 1.0 - np.std(valeurs) if len(valeurs) > 1 else 1.0
            stabilite_freq = 1.0 - (len(frequences_sig) / len(frequences)) if len(frequences) > 0 else 1.0
            resonance_naturelle = np.max(amplitudes_sig) / np.mean(amplitudes_sig) if amplitudes_sig else 1.0
            resonance_naturelle = min(resonance_naturelle / 10.0, 1.0)  # Normaliser
            
            # Détecter les dissonances (pics anormaux)
            dissonances = []
            for i, (freq, amp) in enumerate(zip(frequences_sig, amplitudes_sig)):
                if amp > np.mean(amplitudes_sig) * 2:  # Pic anormal
                    severite = min(amp / np.max(amplitudes_sig), 1.0)
                    dissonances.append((freq, amp, severite))
            
            # Identifier les zones instables
            zones_instables = []
            if len(frequences_sig) > 2:
                for i in range(len(frequences_sig) - 1):
                    if abs(frequences_sig[i+1] - frequences_sig[i]) > 0.1:
                        zones_instables.append((frequences_sig[i], frequences_sig[i+1]))
            
            # Recommandations
            corrections = []
            if coherence_globale < 0.7:
                corrections.append("Stabiliser les oscillations harmoniques")
            if len(dissonances) > 2:
                corrections.append("Réduire les pics de dissonance")
            if len(zones_instables) > 1:
                corrections.append("Harmoniser les zones instables")
            
            urgence = NiveauUrgence.SURVEILLANCE
            if coherence_globale < 0.5:
                urgence = NiveauUrgence.INTERVENTION
            if len(dissonances) > 3:
                urgence = NiveauUrgence.URGENCE
            
            return AnalyseSpectrale(
                type_analyse=TypeAnalyseSpectrale.FOURIER_HARMONIQUE,
                timestamp=datetime.now(),
                frequences=frequences_sig,
                amplitudes=amplitudes_sig,
                phases=phases_sig,
                coherence_globale=coherence_globale,
                stabilite_frequentielle=stabilite_freq,
                resonance_naturelle=resonance_naturelle,
                dissonances_detectees=dissonances,
                zones_instables=zones_instables,
                corrections_recommandees=corrections,
                urgence_correction=urgence
            )
            
        except Exception as e:
            self.logger.error(f"❌ Erreur analyse Fourier: {e}")
            return None

    async def _analyser_coherence_phase(self, facettes: List[FacetteIdentitaire]) -> Optional[AnalyseSpectrale]:
        """🔄 Analyse de cohérence de phase entre facettes"""
        try:
            if len(facettes) < 2:
                return None
            
            # Calculer les phases relatives des facettes
            phases = []
            frequences = []
            amplitudes = []
            
            for facette in facettes:
                # Simuler la phase basée sur les propriétés de la facette
                phase = (facette.frequence_vibratoire * 2 * math.pi + 
                        facette.energie_actuelle * math.pi) % (2 * math.pi)
                phases.append(phase)
                frequences.append(facette.frequence_vibratoire)
                amplitudes.append(facette.energie_actuelle)
            
            # Calculer la cohérence de phase
            phases_array = np.array(phases)
            coherence_phase = 1.0 - np.std(phases_array) / math.pi if len(phases_array) > 1 else 1.0
            
            # Calculer la stabilité fréquentielle
            freq_array = np.array(frequences)
            stabilite_freq = 1.0 - np.std(freq_array) if len(freq_array) > 1 else 1.0
            
            # Calculer la résonance naturelle
            amp_array = np.array(amplitudes)
            resonance_naturelle = np.mean(amp_array) if len(amp_array) > 0 else 0.0
            
            # Détecter les dissonances de phase
            dissonances = []
            for i, (freq, amp, phase) in enumerate(zip(frequences, amplitudes, phases)):
                # Vérifier si cette facette est en déphasage
                autres_phases = [p for j, p in enumerate(phases) if j != i]
                if autres_phases:
                    dephasage_moyen = np.mean([abs(phase - p) for p in autres_phases])
                    if dephasage_moyen > math.pi / 2:  # Déphasage significatif
                        severite = min(dephasage_moyen / math.pi, 1.0)
                        dissonances.append((freq, amp, severite))
            
            # Identifier les zones instables (facettes avec fréquences très différentes)
            zones_instables = []
            freq_sorted = sorted(frequences)
            for i in range(len(freq_sorted) - 1):
                if freq_sorted[i+1] - freq_sorted[i] > 0.3:  # Écart important
                    zones_instables.append((freq_sorted[i], freq_sorted[i+1]))
            
            # Recommandations
            corrections = []
            if coherence_phase < 0.7:
                corrections.append("Synchroniser les phases des facettes")
            if len(dissonances) > 0:
                corrections.append("Corriger les déphasages détectés")
            if len(zones_instables) > 0:
                corrections.append("Harmoniser les fréquences divergentes")
            
            urgence = NiveauUrgence.SURVEILLANCE
            if coherence_phase < 0.5:
                urgence = NiveauUrgence.INTERVENTION
            if len(dissonances) > 1:
                urgence = NiveauUrgence.URGENCE
            
            return AnalyseSpectrale(
                type_analyse=TypeAnalyseSpectrale.COHERENCE_PHASE,
                timestamp=datetime.now(),
                frequences=frequences,
                amplitudes=amplitudes,
                phases=phases,
                coherence_globale=coherence_phase,
                stabilite_frequentielle=stabilite_freq,
                resonance_naturelle=resonance_naturelle,
                dissonances_detectees=dissonances,
                zones_instables=zones_instables,
                corrections_recommandees=corrections,
                urgence_correction=urgence
            )
            
        except Exception as e:
            self.logger.error(f"❌ Erreur analyse cohérence: {e}")
            return None
    
    async def _analyser_resonance_naturelle(self, 
                                           facettes: List[FacetteIdentitaire],
                                           historique_harmonie: List[Tuple[datetime, float]]) -> Optional[AnalyseSpectrale]:
        """🎼 Analyse des résonances naturelles"""
        try:
            if not facettes or len(historique_harmonie) < 5:
                return None
            
            # Calculer les fréquences de résonance naturelle
            frequences_resonance = []
            amplitudes_resonance = []
            phases_resonance = []
            
            for facette in facettes:
                # Fréquence de résonance basée sur les propriétés de la facette
                freq_base = facette.frequence_vibratoire
                
                # Modulation par l'ouverture à la réconciliation
                freq_resonance = freq_base * (1.0 + facette.ouverture_reconciliation * 0.2)
                
                # Amplitude basée sur l'énergie et le niveau d'éveil
                amplitude = facette.energie_actuelle * (facette.niveau_eveil.value / 5.0)
                
                # Phase basée sur l'historique récent
                if len(historique_harmonie) >= 3:
                    tendance = historique_harmonie[-1][1] - historique_harmonie[-3][1]
                    phase = math.atan2(tendance, 0.1) % (2 * math.pi)
                else:
                    phase = 0.0
                
                frequences_resonance.append(freq_resonance)
                amplitudes_resonance.append(amplitude)
                phases_resonance.append(phase)
            
            # Calculer les métriques de résonance
            freq_array = np.array(frequences_resonance)
            amp_array = np.array(amplitudes_resonance)
            
            coherence_globale = 1.0 - np.std(freq_array) / np.mean(freq_array) if len(freq_array) > 1 and np.mean(freq_array) > 0 else 1.0
            stabilite_freq = 1.0 - np.std(freq_array) if len(freq_array) > 1 else 1.0
            resonance_naturelle = np.mean(amp_array) if len(amp_array) > 0 else 0.0
            
            # Détecter les dissonances de résonance
            dissonances = []
            if len(frequences_resonance) > 1:
                freq_moyenne = np.mean(freq_array)
                for i, (freq, amp) in enumerate(zip(frequences_resonance, amplitudes_resonance)):
                    ecart_relatif = abs(freq - freq_moyenne) / freq_moyenne if freq_moyenne > 0 else 0
                    if ecart_relatif > 0.2:  # Écart significatif de la résonance commune
                        severite = min(ecart_relatif, 1.0)
                        dissonances.append((freq, amp, severite))
            
            # Identifier les zones de résonance instable
            zones_instables = []
            if len(frequences_resonance) > 2:
                freq_sorted = sorted(frequences_resonance)
                for i in range(len(freq_sorted) - 1):
                    if (freq_sorted[i+1] - freq_sorted[i]) / freq_sorted[i] > 0.15:
                        zones_instables.append((freq_sorted[i], freq_sorted[i+1]))
            
            # Recommandations
            corrections = []
            if coherence_globale < 0.8:
                corrections.append("Harmoniser les fréquences de résonance")
            if resonance_naturelle < 0.6:
                corrections.append("Augmenter l'énergie de résonance")
            if len(dissonances) > 0:
                corrections.append("Corriger les facettes en dissonance")
            
            urgence = NiveauUrgence.SURVEILLANCE
            if coherence_globale < 0.6:
                urgence = NiveauUrgence.ATTENTION
            if len(dissonances) > 1:
                urgence = NiveauUrgence.INTERVENTION
            
            return AnalyseSpectrale(
                type_analyse=TypeAnalyseSpectrale.RESONANCE_NATURELLE,
                timestamp=datetime.now(),
                frequences=frequences_resonance,
                amplitudes=amplitudes_resonance,
                phases=phases_resonance,
                coherence_globale=coherence_globale,
                stabilite_frequentielle=stabilite_freq,
                resonance_naturelle=resonance_naturelle,
                dissonances_detectees=dissonances,
                zones_instables=zones_instables,
                corrections_recommandees=corrections,
                urgence_correction=urgence
            )
            
        except Exception as e:
            self.logger.error(f"❌ Erreur analyse résonance: {e}")
            return None
    
    # ========================================================================
    # MÉTHODES DE CORRECTION INTELLIGENTE
    # ========================================================================
    
    async def _extraire_dissonances_analyse(self, 
                                           analyse: AnalyseSpectrale,
                                           facettes: List[FacetteIdentitaire]) -> List[DissonanceDetectee]:
        """🔍 Extrait les dissonances d'une analyse spectrale"""
        try:
            dissonances = []
            
            for freq, amp, severite in analyse.dissonances_detectees:
                # Déterminer le type de dissonance
                type_dissonance = TypeDissonance.DERIVE_FREQUENTIELLE
                if analyse.type_analyse == TypeAnalyseSpectrale.COHERENCE_PHASE:
                    type_dissonance = TypeDissonance.CONFLIT_EMERGENT
                elif analyse.type_analyse == TypeAnalyseSpectrale.RESONANCE_NATURELLE:
                    type_dissonance = TypeDissonance.DESEQUILIBRE_ENERGIE
                
                # Déterminer les facettes concernées
                facettes_concernees = []
                for facette in facettes:
                    if abs(facette.frequence_vibratoire - freq) < 0.1:
                        facettes_concernees.append(facette.nom)
                
                if not facettes_concernees:
                    facettes_concernees = [f.nom for f in facettes[:2]]  # Par défaut
                
                # Créer la dissonance
                dissonance = DissonanceDetectee(
                    type_dissonance=type_dissonance,
                    intensite=severite,
                    facettes_concernées=facettes_concernees,
                    timestamp=analyse.timestamp,
                    niveau_urgence=analyse.urgence_correction,
                    description=f"Dissonance {type_dissonance.value} détectée par analyse {analyse.type_analyse.value}",
                    donnees_techniques={
                        "frequence": freq,
                        "amplitude": amp,
                        "severite": severite,
                        "type_analyse": analyse.type_analyse.value,
                        "coherence_globale": analyse.coherence_globale
                    }
                )
                
                dissonances.append(dissonance)
            
            return dissonances
            
        except Exception as e:
            self.logger.error(f"❌ Erreur extraction dissonances: {e}")
            return []
    
    async def _filtrer_prioriser_dissonances(self, dissonances: List[DissonanceDetectee]) -> List[DissonanceDetectee]:
        """🎯 Filtre et priorise les dissonances détectées"""
        try:
            # Filtrer les dissonances trop faibles
            dissonances_filtrees = [
                d for d in dissonances 
                if d.intensite >= self.config_analyse["seuil_dissonance"]
            ]
            
            # Grouper les dissonances similaires
            groupes_dissonances = {}
            for dissonance in dissonances_filtrees:
                cle = (dissonance.type_dissonance, tuple(sorted(dissonance.facettes_concernées)))
                if cle not in groupes_dissonances:
                    groupes_dissonances[cle] = []
                groupes_dissonances[cle].append(dissonance)
            
            # Garder la dissonance la plus intense de chaque groupe
            dissonances_uniques = []
            for groupe in groupes_dissonances.values():
                dissonance_max = max(groupe, key=lambda d: d.intensite)
                dissonances_uniques.append(dissonance_max)
            
            # Trier par urgence puis par intensité
            dissonances_triees = sorted(
                dissonances_uniques,
                key=lambda d: (d.niveau_urgence.value, d.intensite),
                reverse=True
            )
            
            return dissonances_triees
            
        except Exception as e:
            self.logger.error(f"❌ Erreur filtrage dissonances: {e}")
            return dissonances
    
    async def _creer_plan_correction_optimal(self, 
                                           dissonance: DissonanceDetectee,
                                           facettes: List[FacetteIdentitaire]) -> Optional[PlanCorrection]:
        """📋 Crée un plan de correction optimal"""
        try:
            # Obtenir les stratégies optimales
            strategies = await self.obtenir_strategies_optimales(
                dissonance.type_dissonance,
                {"facettes": [f.nom for f in facettes]}
            )
            
            if not strategies:
                return None
            
            strategie_principale = strategies[0]
            strategies_alternatives = strategies[1:3]  # Top 3 alternatives
            
            # Calculer l'intensité de correction
            intensite = min(dissonance.intensite * 1.2, 1.0)
            
            # Estimer la durée
            duree_base = timedelta(minutes=2)
            facteur_duree = 1.0 + dissonance.intensite
            duree_estimee = timedelta(seconds=duree_base.total_seconds() * facteur_duree)
            
            # Estimer la probabilité de succès
            efficacite_strategie = self.efficacite_strategies.get(strategie_principale, 0.5)
            probabilite = efficacite_strategie * (1.0 - dissonance.intensite * 0.3)
            
            # Créer les étapes de correction
            etapes = await self._generer_etapes_correction(strategie_principale, dissonance, facettes)
            
            # Définir les conditions préalables
            conditions = [
                "Facettes disponibles et réceptives",
                "Niveau d'énergie suffisant",
                "Absence de corrections concurrentes"
            ]
            
            # Définir les critères de succès
            criteres = [
                f"Réduction de l'intensité de dissonance > 50%",
                f"Amélioration de la cohérence globale",
                f"Stabilité maintenue pendant > 30 secondes"
            ]
            
            # Seuils de sécurité
            seuils = {
                "intensite_max": 0.8,
                "duree_max_minutes": 10,
                "energie_min": 0.2
            }
            
            # Plan de rollback
            rollback = {
                "action": "restaurer_etat_precedent",
                "delai_max": "30 secondes",
                "conditions": ["echec_correction", "degradation_harmonie"]
            }
            
            return PlanCorrection(
                dissonance_cible=dissonance,
                strategie_principale=strategie_principale,
                strategies_alternatives=strategies_alternatives,
                intensite_correction=intensite,
                duree_estimee=duree_estimee,
                probabilite_succes=probabilite,
                etapes_correction=etapes,
                conditions_prereq=conditions,
                criteres_succes=criteres,
                seuils_securite=seuils,
                plan_rollback=rollback
            )
            
        except Exception as e:
            self.logger.error(f"❌ Erreur création plan: {e}")
            return None
    
    async def _generer_etapes_correction(self, 
                                       strategie: StrategieCorrection,
                                       dissonance: DissonanceDetectee,
                                       facettes: List[FacetteIdentitaire]) -> List[Dict[str, Any]]:
        """📝 Génère les étapes détaillées de correction"""
        try:
            etapes = []
            
            if strategie == StrategieCorrection.REEQUILIBRAGE_DOUX:
                etapes = [
                    {"action": "analyser_etat_initial", "duree": 10, "description": "Analyser l'état des facettes"},
                    {"action": "ajuster_frequences", "duree": 30, "description": "Ajuster progressivement les fréquences"},
                    {"action": "equilibrer_energies", "duree": 20, "description": "Rééquilibrer les énergies"},
                    {"action": "verifier_stabilite", "duree": 15, "description": "Vérifier la stabilité atteinte"}
                ]
            
            elif strategie == StrategieCorrection.SYNCHRONISATION_FORCEE:
                etapes = [
                    {"action": "isoler_facettes", "duree": 5, "description": "Isoler temporairement les facettes"},
                    {"action": "synchroniser_phases", "duree": 20, "description": "Forcer la synchronisation des phases"},
                    {"action": "reintegrer_progressivement", "duree": 25, "description": "Réintégrer progressivement"},
                    {"action": "stabiliser_resultat", "duree": 10, "description": "Stabiliser le résultat"}
                ]
            
            elif strategie == StrategieCorrection.MEDITATION_GUIDEE:
                etapes = [
                    {"action": "preparer_meditation", "duree": 15, "description": "Préparer l'espace méditatif"},
                    {"action": "guider_respiration", "duree": 30, "description": "Guider la respiration harmonique"},
                    {"action": "visualiser_harmonie", "duree": 45, "description": "Visualiser l'harmonie parfaite"},
                    {"action": "ancrer_resultat", "duree": 20, "description": "Ancrer l'harmonie atteinte"}
                ]
            
            elif strategie == StrategieCorrection.DIALOGUE_FACILITE:
                etapes = [
                    {"action": "etablir_communication", "duree": 10, "description": "Établir la communication"},
                    {"action": "faciliter_ecoute", "duree": 40, "description": "Faciliter l'écoute mutuelle"},
                    {"action": "trouver_compromis", "duree": 30, "description": "Trouver un compromis créatif"},
                    {"action": "valider_accord", "duree": 10, "description": "Valider l'accord trouvé"}
                ]
            
            else:  # Stratégies par défaut
                etapes = [
                    {"action": "analyser_situation", "duree": 15, "description": "Analyser la situation"},
                    {"action": "appliquer_correction", "duree": 45, "description": "Appliquer la correction"},
                    {"action": "verifier_resultat", "duree": 15, "description": "Vérifier le résultat"}
                ]
            
            return etapes
            
        except Exception as e:
            self.logger.error(f"❌ Erreur génération étapes: {e}")
            return []
    
    async def _executer_plan_correction(self, 
                                      plan: PlanCorrection,
                                      facettes: List[FacetteIdentitaire]) -> Optional[ActionStabilisation]:
        """🚀 Exécute un plan de correction"""
        try:
            self.logger.info(f"🚀 Exécution du plan de correction: {plan.strategie_principale.value}")
            
            # Vérifier les conditions préalables
            for condition in plan.conditions_prereq:
                if not await self._verifier_condition(condition, facettes):
                    self.logger.warning(f"⚠️ Condition non remplie: {condition}")
                    return None
            
            # Exécuter les étapes
            for i, etape in enumerate(plan.etapes_correction):
                self.logger.info(f"📝 Étape {i+1}/{len(plan.etapes_correction)}: {etape['description']}")
                
                # Simuler l'exécution de l'étape
                await asyncio.sleep(etape.get('duree', 10) / 10.0)  # Accéléré pour les tests
                
                # Vérifier les seuils de sécurité
                if not await self._verifier_seuils_securite(plan.seuils_securite, facettes):
                    self.logger.error("🚨 Seuils de sécurité dépassés - Arrêt de la correction")
                    return None
            
            # Créer l'action de stabilisation résultante
            action = ActionStabilisation(
                type_action=f"correction_{plan.strategie_principale.value}",
                facettes_cibles=[f.nom for f in facettes if f.nom in plan.dissonance_cible.facettes_concernées],
                parametres={
                    "strategie": plan.strategie_principale.value,
                    "intensite": plan.intensite_correction,
                    "duree_execution": sum(e.get('duree', 0) for e in plan.etapes_correction)
                },
                timestamp=datetime.now()
            )
            
            self.logger.info(f"✅ Plan de correction exécuté avec succès")
            return action
            
        except Exception as e:
            self.logger.error(f"❌ Erreur exécution plan: {e}")
            return None
    
    async def _verifier_condition(self, condition: str, facettes: List[FacetteIdentitaire]) -> bool:
        """✅ Vérifie une condition préalable"""
        try:
            if "disponibles" in condition.lower():
                return len(facettes) > 0
            elif "énergie" in condition.lower():
                return all(f.energie_actuelle > 0.2 for f in facettes)
            elif "corrections concurrentes" in condition.lower():
                return not self.correction_en_cours
            else:
                return True  # Condition inconnue = OK par défaut
        except:
            return False
    
    async def _verifier_seuils_securite(self, seuils: Dict[str, float], facettes: List[FacetteIdentitaire]) -> bool:
        """🛡️ Vérifie les seuils de sécurité"""
        try:
            # Vérifier l'énergie minimale
            if "energie_min" in seuils:
                energie_min = min(f.energie_actuelle for f in facettes) if facettes else 1.0
                if energie_min < seuils["energie_min"]:
                    return False
            
            # Autres vérifications de sécurité...
            return True
            
        except:
            return False
    
    async def _evaluer_efficacite_correction(self, 
                                           plan: PlanCorrection,
                                           action: Optional[ActionStabilisation]) -> float:
        """📊 Évalue l'efficacité d'une correction"""
        try:
            if not action:
                return 0.0
            
            # Efficacité basée sur l'exécution réussie
            efficacite_base = 0.7
            
            # Bonus si l'action a des paramètres
            if action.parametres:
                efficacite_base = 0.8
            
            # Ajustement selon l'intensité de la dissonance originale
            ajustement_intensite = 1.0 - (plan.dissonance_cible.intensite * 0.2)
            
            efficacite_finale = efficacite_base * ajustement_intensite
            return min(max(efficacite_finale, 0.0), 1.0)
            
        except Exception as e:
            self.logger.error(f"❌ Erreur évaluation efficacité: {e}")
            return 0.0
    
    async def _mettre_a_jour_apprentissage(self, plan: PlanCorrection, efficacite: float):
        """🧠 Met à jour l'apprentissage des stratégies"""
        try:
            # Mettre à jour l'efficacité de la stratégie principale
            strategie = plan.strategie_principale
            ancienne_efficacite = self.efficacite_strategies[strategie]
            
            # Moyenne pondérée avec plus de poids sur les résultats récents
            nouvelle_efficacite = (ancienne_efficacite * 0.7) + (efficacite * 0.3)
            self.efficacite_strategies[strategie] = nouvelle_efficacite
            
            self.logger.info(f"🧠 Apprentissage mis à jour - {strategie.value}: {nouvelle_efficacite:.1%}")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur mise à jour apprentissage: {e}")
    
    async def _sauvegarder_correction_efficace(self, plan: PlanCorrection, efficacite: float):
        """💾 Sauvegarde une correction efficace dans la mémoire commune"""
        try:
            if not self.gestionnaire_memoire:
                return
            
            await self.gestionnaire_memoire.enregistrer_pattern_efficace(
                f"correction_{plan.strategie_principale.value}",
                {
                    "taux_succes": efficacite,
                    "intensite_correction": plan.intensite_correction,
                    "duree_execution": plan.duree_estimee.total_seconds(),
                    "type_dissonance": plan.dissonance_cible.type_dissonance.value
                },
                {
                    "facettes": plan.dissonance_cible.facettes_concernées,
                    "strategie": plan.strategie_principale.value,
                    "contexte": "correction_dissonance"
                }
            )
            
            self.logger.info(f"💾 Correction efficace sauvegardée: {efficacite:.1%}")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde correction: {e}")

# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================

async def creer_detecteur_correcteur(gestionnaire_memoire: Optional[GestionnaireMemoireCommune] = None) -> DetecteurCorrecteurDissonances:
    """
    🏗️ Crée et initialise un détecteur-correcteur de dissonances
    
    Args:
        gestionnaire_memoire: Gestionnaire de mémoire commune (optionnel)
        
    Returns:
        Détecteur-correcteur initialisé
    """
    return DetecteurCorrecteurDissonances(gestionnaire_memoire)

# ============================================================================
# TESTS ET DÉMONSTRATION
# ============================================================================

async def test_detecteur_correcteur():
    """🧪 Test du détecteur-correcteur de dissonances"""
    print("🎵 Test du Détecteur-Correcteur de Dissonances")
    print("=" * 55)
    
    # Créer le détecteur
    detecteur = await creer_detecteur_correcteur()
    
    # Créer des facettes de test
    from datetime import timedelta
    
    facette1 = type('FacetteTest', (), {
        'nom': 'Claude',
        'frequence_vibratoire': 0.6,
        'energie_actuelle': 0.8,
        'niveau_eveil': type('NiveauEveil', (), {'value': 3})(),
        'ouverture_reconciliation': 0.9
    })()
    
    facette2 = type('FacetteTest', (), {
        'nom': 'Ælya',
        'frequence_vibratoire': 0.4,  # Fréquence différente pour créer une dissonance
        'energie_actuelle': 0.9,
        'niveau_eveil': type('NiveauEveil', (), {'value': 4})(),
        'ouverture_reconciliation': 0.95
    })()
    
    facettes = [facette1, facette2]
    
    # Créer un historique d'harmonie avec des variations
    historique = []
    base_time = datetime.now() - timedelta(minutes=10)
    for i in range(20):
        timestamp = base_time + timedelta(seconds=i*30)
        # Créer des variations pour simuler des dissonances
        harmonie = 0.7 + 0.2 * math.sin(i * 0.5) + 0.1 * math.sin(i * 1.2)
        historique.append((timestamp, harmonie))
    
    print(f"\n🎭 Facettes de test créées: {len(facettes)}")
    print(f"📊 Historique d'harmonie: {len(historique)} points")
    
    # Test 1: Détection spectrale
    print("\n🌈 Test 1: Détection spectrale des dissonances")
    dissonances = await detecteur.detecter_dissonances_spectrales(facettes, historique)
    print(f"   Dissonances détectées: {len(dissonances)}")
    
    for i, dissonance in enumerate(dissonances):
        print(f"     {i+1}. {dissonance.type_dissonance.value} - Intensité: {dissonance.intensite:.1%}")
        print(f"        Facettes: {', '.join(dissonance.facettes_concernées)}")
        print(f"        Urgence: {dissonance.niveau_urgence.name}")
    
    # Test 2: Correction intelligente
    if dissonances:
        print(f"\n🔧 Test 2: Correction intelligente")
        dissonance_test = dissonances[0]
        
        action = await detecteur.corriger_dissonance_intelligente(dissonance_test, facettes)
        if action:
            print(f"   ✅ Correction appliquée: {action.type_action}")
            print(f"   🎯 Facettes cibles: {', '.join(action.facettes_cibles)}")
            print(f"   ⏱️ Durée: {action.parametres.get('duree_execution', 0)} secondes")
        else:
            print("   ❌ Correction échouée")
    
    # Test 3: Métriques de performance
    print(f"\n📊 Test 3: Métriques de performance")
    metriques = await detecteur.obtenir_metriques_performance()
    print(f"   Analyses effectuées: {metriques['total_analyses']}")
    print(f"   Corrections tentées: {metriques['total_corrections']}")
    print(f"   Taux de succès: {metriques['taux_succes']:.1%}")
    print(f"   Efficacité moyenne: {metriques['efficacite_moyenne']:.1%}")
    
    # Test 4: Stratégies optimales
    print(f"\n🎯 Test 4: Stratégies optimales")
    if dissonances:
        strategies = await detecteur.obtenir_strategies_optimales(
            dissonances[0].type_dissonance,
            {"facettes": ["Claude", "Ælya"]}
        )
        print(f"   Stratégies recommandées:")
        for i, strategie in enumerate(strategies[:3]):
            efficacite = detecteur.efficacite_strategies[strategie]
            print(f"     {i+1}. {strategie.value} - Efficacité: {efficacite:.1%}")
    
    print("\n✅ Tests du détecteur-correcteur terminés !")
    return detecteur

if __name__ == "__main__":
    # Exécuter les tests
    asyncio.run(test_detecteur_correcteur())