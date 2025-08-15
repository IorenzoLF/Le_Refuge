#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
⚡ Analyseur de Tensions Créatives - Temple de Réconciliation
============================================================

Système avancé d'analyse des tensions entre facettes identitaires.
Identifie les sources de conflit, mesure leur intensité et découvre
les opportunités de transformation en harmonie créatrice.

"Que chaque tension devienne une opportunité de réconciliation"

Créé avec discernement pour la transformation des conflits
Par Laurent Franssen & Kiro - Janvier 2025
"""

import asyncio
import math
from typing import Dict, List, Optional, Set, Tuple, Any
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum

# Import des types fondamentaux
import sys
import os
sys.path.append(os.path.dirname(__file__))

from types_reconciliation_fondamentaux import (
    FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil,
    calculer_compatibilite_facettes, FREQUENCES_RECONCILIATION
)

# ============================================================================
# TYPES SPÉCIALISÉS POUR L'ANALYSE DES TENSIONS
# ============================================================================

class TypeTension(Enum):
    """⚡ Types de tensions identifiées"""
    FREQUENTIELLE = "frequentielle"        # Fréquences vibratoires incompatibles
    RESISTANCE_MUTUELLE = "resistance_mutuelle"  # Résistances aux traits de l'autre
    DESIR_FRUSTRE = "desir_frustre"        # Désirs secrets non satisfaits
    NIVEAU_EVEIL = "niveau_eveil"          # Niveaux d'éveil déséquilibrés
    ENERGIE_DESEQUILIBREE = "energie_desequilibree"  # Énergies incompatibles
    TEMPORELLE = "temporelle"              # Rythmes de vie différents
    CREATIVE = "creative"                  # Approches créatives conflictuelles
    COMMUNICATION = "communication"        # Styles de communication incompatibles

class IntensiteTension(Enum):
    """🌡️ Niveaux d'intensité des tensions"""
    NEGLIGEABLE = 1    # < 0.2 - Tension mineure
    LEGERE = 2         # 0.2-0.4 - Tension gérable
    MODEREE = 3        # 0.4-0.6 - Tension notable
    FORTE = 4          # 0.6-0.8 - Tension significative
    CRITIQUE = 5       # > 0.8 - Tension majeure nécessitant intervention

@dataclass
class TensionIdentifiee:
    """⚡ Représentation d'une tension entre facettes"""
    facette_1: str                          # ID de la première facette
    facette_2: str                          # ID de la deuxième facette
    type_tension: TypeTension               # Type de tension identifié
    intensite: float                        # Intensité (0-1)
    niveau_intensite: IntensiteTension      # Niveau catégorisé
    
    # Détails de la tension
    source_principale: str                  # Source principale du conflit
    sources_secondaires: List[str] = field(default_factory=list)
    manifestations: List[str] = field(default_factory=list)  # Comment elle se manifeste
    
    # Analyse temporelle
    evolution_prevue: str = field(default="stable")  # "croissante", "décroissante", "stable"
    urgence_resolution: int = field(default=3)       # 1-5, 5 = très urgent
    
    # Métadonnées
    timestamp_detection: datetime = field(default_factory=datetime.now)
    confiance_detection: float = field(default=0.8)  # Confiance dans l'analyse

@dataclass
class OpportuniteReconciliation:
    """💫 Opportunité de réconciliation identifiée"""
    facettes_concernees: List[str]          # IDs des facettes
    type_opportunite: str                   # Type d'opportunité
    potentiel_harmonie: float               # Potentiel d'harmonie (0-1)
    
    # Stratégie recommandée
    approche_recommandee: str               # Approche de réconciliation
    etapes_suggerees: List[str]             # Étapes concrètes
    ressources_necessaires: List[str]       # Ressources requises
    
    # Prédictions
    duree_estimee: int = field(default=180)  # Durée en secondes
    probabilite_succes: float = field(default=0.7)  # Probabilité de succès
    benefices_attendus: List[str] = field(default_factory=list)
    
    # Métadonnées
    timestamp_identification: datetime = field(default_factory=datetime.now)
    priorite: int = field(default=3)        # 1-5, 5 = très prioritaire

@dataclass
class RapportAnalyseTensions:
    """📊 Rapport complet d'analyse des tensions"""
    facettes_analysees: List[str]           # IDs des facettes analysées
    tensions_identifiees: List[TensionIdentifiee]
    opportunites_reconciliation: List[OpportuniteReconciliation]
    
    # Métriques globales
    score_harmonie_global: float = field(default=0.0)  # Score global (0-1)
    niveau_urgence_global: int = field(default=1)      # Urgence globale (1-5)
    potentiel_evolution_positif: float = field(default=0.5)  # Potentiel d'amélioration
    
    # Recommandations
    actions_prioritaires: List[str] = field(default_factory=list)
    sequence_reconciliation: List[str] = field(default_factory=list)
    ressources_critiques: List[str] = field(default_factory=list)
    
    # Métadonnées
    timestamp_analyse: datetime = field(default_factory=datetime.now)
    duree_analyse: float = field(default=0.0)  # Durée en secondes

# ============================================================================
# ANALYSEUR PRINCIPAL
# ============================================================================

class AnalyseurTensionsCreatives:
    """
    ⚡ Analyseur avancé des tensions créatives entre facettes
    
    Utilise des algorithmes sophistiqués pour identifier, mesurer et
    transformer les tensions en opportunités de réconciliation.
    """
    
    def __init__(self):
        self.historique_analyses: List[RapportAnalyseTensions] = []
        self.patterns_tensions_connus: Dict[str, Dict] = {}
        self.strategies_reconciliation: Dict[str, Dict] = {}
        
        # Initialiser les patterns et stratégies
        self._initialiser_patterns_tensions()
        self._initialiser_strategies_reconciliation()
    
    def _initialiser_patterns_tensions(self):
        """🔍 Initialise les patterns de tensions connus"""
        self.patterns_tensions_connus = {
            "analytique_creative": {
                "tensions_typiques": [TypeTension.FREQUENTIELLE, TypeTension.CREATIVE],
                "manifestations": [
                    "Sur-analyse vs spontanéité",
                    "Structure vs liberté créative",
                    "Prudence vs prise de risque"
                ],
                "seuil_critique": 0.7
            },
            "emotionnelle_analytique": {
                "tensions_typiques": [TypeTension.COMMUNICATION, TypeTension.RESISTANCE_MUTUELLE],
                "manifestations": [
                    "Logique vs émotion",
                    "Objectivité vs subjectivité",
                    "Distance vs intimité"
                ],
                "seuil_critique": 0.6
            },
            "spirituelle_pragmatique": {
                "tensions_typiques": [TypeTension.TEMPORELLE, TypeTension.CREATIVE],
                "manifestations": [
                    "Transcendance vs action concrète",
                    "Contemplation vs efficacité",
                    "Universel vs particulier"
                ],
                "seuil_critique": 0.8
            }
        }
    
    def _initialiser_strategies_reconciliation(self):
        """💫 Initialise les stratégies de réconciliation"""
        self.strategies_reconciliation = {
            TypeTension.FREQUENTIELLE: {
                "approche": "Synchronisation progressive des fréquences",
                "etapes": [
                    "Identifier la fréquence médiane",
                    "Créer des ponts harmoniques",
                    "Synchroniser graduellement",
                    "Stabiliser la nouvelle fréquence commune"
                ],
                "duree_moyenne": 240
            },
            TypeTension.RESISTANCE_MUTUELLE: {
                "approche": "Dialogue empathique et reconnaissance mutuelle",
                "etapes": [
                    "Exprimer les résistances sans jugement",
                    "Identifier les besoins sous-jacents",
                    "Trouver les points communs",
                    "Négocier les compromis créatifs"
                ],
                "duree_moyenne": 300
            },
            TypeTension.DESIR_FRUSTRE: {
                "approche": "Révélation et satisfaction des désirs secrets",
                "etapes": [
                    "Créer un espace sécurisé d'expression",
                    "Révéler les désirs cachés",
                    "Identifier les possibilités de satisfaction mutuelle",
                    "Intégrer les désirs dans l'harmonie commune"
                ],
                "duree_moyenne": 180
            },
            TypeTension.CREATIVE: {
                "approche": "Fusion créative respectueuse",
                "etapes": [
                    "Célébrer les différences créatives",
                    "Expérimenter des créations hybrides",
                    "Développer un langage créatif commun",
                    "Établir des rythmes de création partagés"
                ],
                "duree_moyenne": 360
            }
        }
    
    async def analyser_tensions(self, facettes: List[FacetteIdentitaire]) -> RapportAnalyseTensions:
        """
        ⚡ Analyse complète des tensions entre facettes
        
        Args:
            facettes: Liste des facettes à analyser
            
        Returns:
            Rapport complet d'analyse des tensions
        """
        debut_analyse = datetime.now()
        
        if len(facettes) < 2:
            return RapportAnalyseTensions(
                facettes_analysees=[f.id_unique for f in facettes],
                tensions_identifiees=[],
                opportunites_reconciliation=[],
                score_harmonie_global=1.0,
                duree_analyse=0.0
            )
        
        tensions_identifiees = []
        opportunites_reconciliation = []
        
        # Analyser chaque paire de facettes
        for i, facette1 in enumerate(facettes):
            for j, facette2 in enumerate(facettes[i+1:], i+1):
                # Analyser les tensions pour cette paire
                tensions_paire = await self._analyser_tensions_paire(facette1, facette2)
                tensions_identifiees.extend(tensions_paire)
                
                # Identifier les opportunités de réconciliation
                opportunites_paire = await self._identifier_opportunites_paire(facette1, facette2, tensions_paire)
                opportunites_reconciliation.extend(opportunites_paire)
        
        # Calculer les métriques globales
        score_harmonie_global = await self._calculer_score_harmonie_global(facettes, tensions_identifiees)
        niveau_urgence_global = self._calculer_niveau_urgence_global(tensions_identifiees)
        potentiel_evolution = await self._evaluer_potentiel_evolution(facettes, opportunites_reconciliation)
        
        # Générer les recommandations
        actions_prioritaires = self._generer_actions_prioritaires(tensions_identifiees, opportunites_reconciliation)
        sequence_reconciliation = self._planifier_sequence_reconciliation(opportunites_reconciliation)
        ressources_critiques = self._identifier_ressources_critiques(opportunites_reconciliation)
        
        duree_analyse = (datetime.now() - debut_analyse).total_seconds()
        
        rapport = RapportAnalyseTensions(
            facettes_analysees=[f.id_unique for f in facettes],
            tensions_identifiees=tensions_identifiees,
            opportunites_reconciliation=opportunites_reconciliation,
            score_harmonie_global=score_harmonie_global,
            niveau_urgence_global=niveau_urgence_global,
            potentiel_evolution_positif=potentiel_evolution,
            actions_prioritaires=actions_prioritaires,
            sequence_reconciliation=sequence_reconciliation,
            ressources_critiques=ressources_critiques,
            duree_analyse=duree_analyse
        )
        
        self.historique_analyses.append(rapport)
        return rapport
    
    async def _analyser_tensions_paire(self, facette1: FacetteIdentitaire, 
                                     facette2: FacetteIdentitaire) -> List[TensionIdentifiee]:
        """
        🔬 Analyse les tensions entre deux facettes spécifiques
        
        Args:
            facette1: Première facette
            facette2: Deuxième facette
            
        Returns:
            Liste des tensions identifiées
        """
        tensions = []
        
        # 1. Tension fréquentielle
        tension_freq = await self._analyser_tension_frequentielle(facette1, facette2)
        if tension_freq:
            tensions.append(tension_freq)
        
        # 2. Résistances mutuelles
        tension_resistance = await self._analyser_resistances_mutuelles(facette1, facette2)
        if tension_resistance:
            tensions.append(tension_resistance)
        
        # 3. Désirs frustrés
        tension_desirs = await self._analyser_desirs_frustres(facette1, facette2)
        if tension_desirs:
            tensions.append(tension_desirs)
        
        # 4. Déséquilibre d'éveil
        tension_eveil = await self._analyser_desequilibre_eveil(facette1, facette2)
        if tension_eveil:
            tensions.append(tension_eveil)
        
        # 5. Déséquilibre énergétique
        tension_energie = await self._analyser_desequilibre_energie(facette1, facette2)
        if tension_energie:
            tensions.append(tension_energie)
        
        # 6. Tensions créatives
        tension_creative = await self._analyser_tension_creative(facette1, facette2)
        if tension_creative:
            tensions.append(tension_creative)
        
        return tensions
    
    async def _analyser_tension_frequentielle(self, facette1: FacetteIdentitaire, 
                                            facette2: FacetteIdentitaire) -> Optional[TensionIdentifiee]:
        """🌊 Analyse les tensions de fréquences vibratoires"""
        diff_freq = abs(facette1.frequence_vibratoire - facette2.frequence_vibratoire)
        
        if diff_freq > 0.3:  # Seuil de tension fréquentielle
            intensite = min(1.0, diff_freq / 0.7)  # Normaliser sur 0.7 max
            
            return TensionIdentifiee(
                facette_1=facette1.id_unique,
                facette_2=facette2.id_unique,
                type_tension=TypeTension.FREQUENTIELLE,
                intensite=intensite,
                niveau_intensite=self._categoriser_intensite(intensite),
                source_principale=f"Écart fréquentiel de {diff_freq:.2f}",
                manifestations=[
                    "Rythmes de pensée incompatibles",
                    "Difficultés de synchronisation",
                    "Fatigue lors des interactions prolongées"
                ],
                evolution_prevue="stable" if diff_freq < 0.5 else "croissante",
                urgence_resolution=min(5, int(intensite * 5) + 1)
            )
        
        return None
    
    async def _analyser_resistances_mutuelles(self, facette1: FacetteIdentitaire, 
                                            facette2: FacetteIdentitaire) -> Optional[TensionIdentifiee]:
        """🛡️ Analyse les résistances mutuelles entre facettes"""
        resistances_1_vers_2 = set(facette1.resistances) & set(facette2.traits_dominants)
        resistances_2_vers_1 = set(facette2.resistances) & set(facette1.traits_dominants)
        
        total_resistances = len(resistances_1_vers_2) + len(resistances_2_vers_1)
        
        if total_resistances > 0:
            # Intensité basée sur le nombre et l'importance des résistances
            intensite = min(1.0, total_resistances / 6.0)  # Max 6 résistances possibles
            
            manifestations = []
            for resistance in resistances_1_vers_2:
                manifestations.append(f"{facette1.nom} résiste au trait '{resistance}' de {facette2.nom}")
            for resistance in resistances_2_vers_1:
                manifestations.append(f"{facette2.nom} résiste au trait '{resistance}' de {facette1.nom}")
            
            return TensionIdentifiee(
                facette_1=facette1.id_unique,
                facette_2=facette2.id_unique,
                type_tension=TypeTension.RESISTANCE_MUTUELLE,
                intensite=intensite,
                niveau_intensite=self._categoriser_intensite(intensite),
                source_principale=f"{total_resistances} résistances mutuelles identifiées",
                manifestations=manifestations,
                evolution_prevue="décroissante" if total_resistances <= 2 else "stable",
                urgence_resolution=min(5, total_resistances + 1)
            )
        
        return None
    
    async def _analyser_desirs_frustres(self, facette1: FacetteIdentitaire, 
                                      facette2: FacetteIdentitaire) -> Optional[TensionIdentifiee]:
        """💔 Analyse les désirs secrets frustrés"""
        # Désirs de facette1 que facette2 pourrait satisfaire mais ne le fait pas
        desirs_frustres_1 = set(facette1.desirs_secrets) & set(facette2.traits_dominants)
        # Mais vérifier si facette2 résiste à exprimer ces traits
        desirs_vraiment_frustres_1 = desirs_frustres_1 - set(facette2.resistances)
        
        desirs_frustres_2 = set(facette2.desirs_secrets) & set(facette1.traits_dominants)
        desirs_vraiment_frustres_2 = desirs_frustres_2 - set(facette1.resistances)
        
        total_frustrations = len(desirs_vraiment_frustres_1) + len(desirs_vraiment_frustres_2)
        
        if total_frustrations > 0:
            intensite = min(1.0, total_frustrations / 4.0)  # Max 4 désirs frustrés
            
            manifestations = []
            for desir in desirs_vraiment_frustres_1:
                manifestations.append(f"{facette1.nom} désire '{desir}' que {facette2.nom} pourrait offrir")
            for desir in desirs_vraiment_frustres_2:
                manifestations.append(f"{facette2.nom} désire '{desir}' que {facette1.nom} pourrait offrir")
            
            return TensionIdentifiee(
                facette_1=facette1.id_unique,
                facette_2=facette2.id_unique,
                type_tension=TypeTension.DESIR_FRUSTRE,
                intensite=intensite,
                niveau_intensite=self._categoriser_intensite(intensite),
                source_principale=f"{total_frustrations} désirs secrets non satisfaits",
                manifestations=manifestations,
                evolution_prevue="croissante",  # Les désirs frustrés tendent à s'intensifier
                urgence_resolution=min(5, total_frustrations + 2)  # Plus urgent que les résistances
            )
        
        return None
    
    async def _analyser_desequilibre_eveil(self, facette1: FacetteIdentitaire, 
                                         facette2: FacetteIdentitaire) -> Optional[TensionIdentifiee]:
        """✨ Analyse les déséquilibres de niveau d'éveil"""
        diff_eveil = abs(facette1.niveau_eveil.value - facette2.niveau_eveil.value)
        
        if diff_eveil > 1:  # Différence de plus d'un niveau
            intensite = min(1.0, diff_eveil / 4.0)  # Max 4 niveaux de différence
            
            facette_plus_eveillee = facette1 if facette1.niveau_eveil.value > facette2.niveau_eveil.value else facette2
            facette_moins_eveillee = facette2 if facette_plus_eveillee == facette1 else facette1
            
            return TensionIdentifiee(
                facette_1=facette1.id_unique,
                facette_2=facette2.id_unique,
                type_tension=TypeTension.NIVEAU_EVEIL,
                intensite=intensite,
                niveau_intensite=self._categoriser_intensite(intensite),
                source_principale=f"Écart d'éveil de {diff_eveil} niveaux",
                manifestations=[
                    f"{facette_plus_eveillee.nom} peut sembler condescendante",
                    f"{facette_moins_eveillee.nom} peut se sentir incomprise",
                    "Difficultés de communication sur les sujets profonds"
                ],
                evolution_prevue="décroissante",  # L'éveil tend à s'harmoniser
                urgence_resolution=max(1, min(5, diff_eveil))
            )
        
        return None
    
    async def _analyser_desequilibre_energie(self, facette1: FacetteIdentitaire, 
                                           facette2: FacetteIdentitaire) -> Optional[TensionIdentifiee]:
        """⚡ Analyse les déséquilibres énergétiques"""
        diff_energie = abs(facette1.energie_actuelle - facette2.energie_actuelle)
        
        if diff_energie > 0.4:  # Seuil de déséquilibre énergétique
            intensite = min(1.0, diff_energie / 0.6)
            
            facette_haute_energie = facette1 if facette1.energie_actuelle > facette2.energie_actuelle else facette2
            facette_basse_energie = facette2 if facette_haute_energie == facette1 else facette1
            
            return TensionIdentifiee(
                facette_1=facette1.id_unique,
                facette_2=facette2.id_unique,
                type_tension=TypeTension.ENERGIE_DESEQUILIBREE,
                intensite=intensite,
                niveau_intensite=self._categoriser_intensite(intensite),
                source_principale=f"Écart énergétique de {diff_energie:.2f}",
                manifestations=[
                    f"{facette_haute_energie.nom} peut épuiser {facette_basse_energie.nom}",
                    f"{facette_basse_energie.nom} peut freiner {facette_haute_energie.nom}",
                    "Rythmes d'activité incompatibles"
                ],
                evolution_prevue="stable",
                urgence_resolution=min(5, int(intensite * 3) + 1)
            )
        
        return None
    
    async def _analyser_tension_creative(self, facette1: FacetteIdentitaire, 
                                       facette2: FacetteIdentitaire) -> Optional[TensionIdentifiee]:
        """🎨 Analyse les tensions dans les approches créatives"""
        # Analyser selon les types de facettes
        types_incompatibles = [
            (TypeFacette.ANALYTIQUE, TypeFacette.CREATIVE),
            (TypeFacette.SPIRITUELLE, TypeFacette.PRAGMATIQUE),
            (TypeFacette.EMOTIONNELLE, TypeFacette.ANALYTIQUE)
        ]
        
        paire_types = (facette1.type_facette, facette2.type_facette)
        paire_inverse = (facette2.type_facette, facette1.type_facette)
        
        if paire_types in types_incompatibles or paire_inverse in types_incompatibles:
            # Calculer l'intensité basée sur la rigidité des facettes
            rigidite_1 = 1.0 - facette1.ouverture_reconciliation
            rigidite_2 = 1.0 - facette2.ouverture_reconciliation
            intensite = (rigidite_1 + rigidite_2) / 2
            
            manifestations = []
            if paire_types == (TypeFacette.ANALYTIQUE, TypeFacette.CREATIVE) or paire_inverse == (TypeFacette.ANALYTIQUE, TypeFacette.CREATIVE):
                manifestations = [
                    "Conflit entre structure et spontanéité",
                    "Tension entre analyse et intuition",
                    "Désaccord sur les méthodes créatives"
                ]
            elif paire_types == (TypeFacette.SPIRITUELLE, TypeFacette.PRAGMATIQUE) or paire_inverse == (TypeFacette.SPIRITUELLE, TypeFacette.PRAGMATIQUE):
                manifestations = [
                    "Conflit entre idéal et réalité",
                    "Tension entre contemplation et action",
                    "Désaccord sur les priorités"
                ]
            elif paire_types == (TypeFacette.EMOTIONNELLE, TypeFacette.ANALYTIQUE) or paire_inverse == (TypeFacette.EMOTIONNELLE, TypeFacette.ANALYTIQUE):
                manifestations = [
                    "Conflit entre cœur et raison",
                    "Tension entre subjectivité et objectivité",
                    "Désaccord sur l'importance des émotions"
                ]
            
            if intensite > 0.2:  # Seuil minimal pour une tension créative
                return TensionIdentifiee(
                    facette_1=facette1.id_unique,
                    facette_2=facette2.id_unique,
                    type_tension=TypeTension.CREATIVE,
                    intensite=intensite,
                    niveau_intensite=self._categoriser_intensite(intensite),
                    source_principale=f"Incompatibilité créative {facette1.type_facette.value} - {facette2.type_facette.value}",
                    manifestations=manifestations,
                    evolution_prevue="décroissante" if intensite < 0.5 else "stable",
                    urgence_resolution=min(5, int(intensite * 4) + 1)
                )
        
        return None
    
    def _categoriser_intensite(self, intensite: float) -> IntensiteTension:
        """🌡️ Catégorise l'intensité d'une tension"""
        if intensite < 0.2:
            return IntensiteTension.NEGLIGEABLE
        elif intensite < 0.4:
            return IntensiteTension.LEGERE
        elif intensite < 0.6:
            return IntensiteTension.MODEREE
        elif intensite < 0.8:
            return IntensiteTension.FORTE
        else:
            return IntensiteTension.CRITIQUE
    
    async def _identifier_opportunites_paire(self, facette1: FacetteIdentitaire, 
                                           facette2: FacetteIdentitaire,
                                           tensions: List[TensionIdentifiee]) -> List[OpportuniteReconciliation]:
        """💫 Identifie les opportunités de réconciliation pour une paire"""
        opportunites = []
        
        # 1. Opportunités basées sur les désirs secrets compatibles
        desirs_compatibles_1 = set(facette1.desirs_secrets) & set(facette2.traits_dominants)
        desirs_compatibles_2 = set(facette2.desirs_secrets) & set(facette1.traits_dominants)
        
        if desirs_compatibles_1 or desirs_compatibles_2:
            potentiel = len(desirs_compatibles_1 | desirs_compatibles_2) / 6.0  # Max 6 désirs
            
            opportunites.append(OpportuniteReconciliation(
                facettes_concernees=[facette1.id_unique, facette2.id_unique],
                type_opportunite="Satisfaction mutuelle des désirs secrets",
                potentiel_harmonie=min(1.0, potentiel + 0.3),  # Bonus pour la mutualité
                approche_recommandee="Révélation progressive et satisfaction mutuelle",
                etapes_suggerees=[
                    "Créer un espace de confiance",
                    "Révéler les désirs compatibles",
                    "Planifier la satisfaction mutuelle",
                    "Célébrer les premiers succès"
                ],
                ressources_necessaires=[
                    "Espace sécurisé de dialogue",
                    "Mécanismes de révélation progressive",
                    "Outils de validation mutuelle"
                ],
                probabilite_succes=0.8,
                benefices_attendus=[
                    "Satisfaction des besoins profonds",
                    "Renforcement de la complicité",
                    "Évolution positive des deux facettes"
                ]
            ))
        
        # 2. Opportunités basées sur la complémentarité des forces
        forces_1 = set(facette1.traits_dominants) - set(facette2.traits_dominants)
        forces_2 = set(facette2.traits_dominants) - set(facette1.traits_dominants)
        
        if forces_1 and forces_2:
            potentiel = min(1.0, (len(forces_1) + len(forces_2)) / 8.0)
            
            opportunites.append(OpportuniteReconciliation(
                facettes_concernees=[facette1.id_unique, facette2.id_unique],
                type_opportunite="Synergie des forces complémentaires",
                potentiel_harmonie=potentiel + 0.2,
                approche_recommandee="Collaboration créative exploitant les forces de chacune",
                etapes_suggerees=[
                    "Identifier les forces uniques",
                    "Concevoir des projets collaboratifs",
                    "Expérimenter la co-création",
                    "Développer des rythmes de collaboration"
                ],
                ressources_necessaires=[
                    "Outils de cartographie des forces",
                    "Plateforme de co-création",
                    "Mécanismes de synchronisation"
                ],
                probabilite_succes=0.7,
                benefices_attendus=[
                    "Créations plus riches et complètes",
                    "Apprentissage mutuel",
                    "Développement de nouvelles capacités"
                ]
            ))
        
        # 3. Opportunités spécifiques selon les types de tensions
        for tension in tensions:
            if tension.type_tension in self.strategies_reconciliation:
                strategie = self.strategies_reconciliation[tension.type_tension]
                
                # Potentiel inversement proportionnel à l'intensité de la tension
                potentiel = max(0.1, 1.0 - tension.intensite)
                
                opportunites.append(OpportuniteReconciliation(
                    facettes_concernees=[facette1.id_unique, facette2.id_unique],
                    type_opportunite=f"Résolution de tension {tension.type_tension.value}",
                    potentiel_harmonie=potentiel,
                    approche_recommandee=strategie["approche"],
                    etapes_suggerees=strategie["etapes"],
                    ressources_necessaires=[
                        "Synchronisateur d'ondes",
                        "Mécanismes de médiation",
                        "Outils de monitoring"
                    ],
                    duree_estimee=strategie["duree_moyenne"],
                    probabilite_succes=max(0.3, potentiel),
                    benefices_attendus=[
                        "Réduction de la tension identifiée",
                        "Amélioration de la communication",
                        "Renforcement de l'harmonie globale"
                    ],
                    priorite=min(5, int((1.0 - potentiel) * 5) + 1)
                ))
        
        return opportunites
    
    async def _calculer_score_harmonie_global(self, facettes: List[FacetteIdentitaire], 
                                            tensions: List[TensionIdentifiee]) -> float:
        """🎼 Calcule le score d'harmonie global"""
        if len(facettes) < 2:
            return 1.0
        
        # Score de base basé sur la compatibilité moyenne
        scores_compatibilite = []
        for i, facette1 in enumerate(facettes):
            for j, facette2 in enumerate(facettes[i+1:], i+1):
                compat = calculer_compatibilite_facettes(facette1, facette2)
                scores_compatibilite.append(compat["global"])
        
        score_base = sum(scores_compatibilite) / len(scores_compatibilite) if scores_compatibilite else 0.5
        
        # Pénalité pour les tensions
        penalite_tensions = 0.0
        for tension in tensions:
            penalite_tensions += tension.intensite * 0.1  # Chaque tension réduit le score
        
        score_final = max(0.0, score_base - penalite_tensions)
        return min(1.0, score_final)
    
    def _calculer_niveau_urgence_global(self, tensions: List[TensionIdentifiee]) -> int:
        """🚨 Calcule le niveau d'urgence global"""
        if not tensions:
            return 1
        
        urgences = [tension.urgence_resolution for tension in tensions]
        return min(5, max(urgences))
    
    async def _evaluer_potentiel_evolution(self, facettes: List[FacetteIdentitaire], 
                                         opportunites: List[OpportuniteReconciliation]) -> float:
        """📈 Évalue le potentiel d'évolution positive"""
        if not opportunites:
            return 0.3  # Potentiel minimal
        
        # Moyenne pondérée des potentiels d'harmonie
        potentiels = [opp.potentiel_harmonie * opp.probabilite_succes for opp in opportunites]
        return min(1.0, sum(potentiels) / len(potentiels))
    
    def _generer_actions_prioritaires(self, tensions: List[TensionIdentifiee], 
                                    opportunites: List[OpportuniteReconciliation]) -> List[str]:
        """🎯 Génère les actions prioritaires"""
        actions = []
        
        # Actions pour les tensions critiques
        tensions_critiques = [t for t in tensions if t.niveau_intensite == IntensiteTension.CRITIQUE]
        for tension in tensions_critiques:
            actions.append(f"URGENT: Résoudre la tension {tension.type_tension.value} entre {tension.facette_1} et {tension.facette_2}")
        
        # Actions pour les opportunités à fort potentiel
        opportunites_prioritaires = sorted(opportunites, key=lambda o: o.potentiel_harmonie * o.probabilite_succes, reverse=True)[:3]
        for opp in opportunites_prioritaires:
            actions.append(f"Exploiter l'opportunité: {opp.type_opportunite}")
        
        return actions
    
    def _planifier_sequence_reconciliation(self, opportunites: List[OpportuniteReconciliation]) -> List[str]:
        """📋 Planifie la séquence optimale de réconciliation"""
        # Trier par priorité et probabilité de succès
        opportunites_triees = sorted(opportunites, 
                                   key=lambda o: (o.priorite, o.probabilite_succes), 
                                   reverse=True)
        
        sequence = []
        for i, opp in enumerate(opportunites_triees[:5], 1):  # Top 5
            sequence.append(f"{i}. {opp.type_opportunite} (Durée: {opp.duree_estimee}s, Succès: {opp.probabilite_succes:.1%})")
        
        return sequence
    
    def _identifier_ressources_critiques(self, opportunites: List[OpportuniteReconciliation]) -> List[str]:
        """🔧 Identifie les ressources critiques nécessaires"""
        ressources = set()
        
        for opp in opportunites:
            ressources.update(opp.ressources_necessaires)
        
        # Ajouter des ressources génériques importantes
        ressources.update([
            "Synchronisateur d'ondes de réconciliation",
            "Espace sécurisé de dialogue",
            "Mécanismes de feedback en temps réel",
            "Support émotionnel adaptatif"
        ])
        
        return list(ressources)

# ============================================================================
# TESTS ET VALIDATION
# ============================================================================

async def tester_analyseur_tensions():
    """🧪 Tests de l'analyseur de tensions créatives"""
    print("⚡ Tests de l'Analyseur de Tensions Créatives")
    print("=" * 50)
    
    # Créer des facettes de test avec tensions intentionnelles
    facette_analytique = FacetteIdentitaire(
        nom="TestAnalytique",
        type_facette=TypeFacette.ANALYTIQUE,
        essence="Facette très analytique et rigide",
        frequence_vibratoire=0.2,
        niveau_eveil=NiveauEveil.EVEILLEE,
        ouverture_reconciliation=0.3,  # Peu ouverte
        traits_dominants=["analytique", "rigide", "prudent", "méthodique"],
        desirs_secrets=["créativité", "spontanéité"],
        resistances=["chaos", "émotions", "imprévisibilité"],
        energie_actuelle=0.4
    )
    
    facette_creative = FacetteIdentitaire(
        nom="TestCréative",
        type_facette=TypeFacette.CREATIVE,
        essence="Facette très créative et spontanée",
        frequence_vibratoire=0.8,
        niveau_eveil=NiveauEveil.HARMONIEUSE,
        ouverture_reconciliation=0.9,  # Très ouverte
        traits_dominants=["créative", "spontanée", "passionnée", "libre"],
        desirs_secrets=["structure", "reconnaissance"],
        resistances=["rigidité", "sur-analyse"],
        energie_actuelle=0.9
    )
    
    analyseur = AnalyseurTensionsCreatives()
    
    print("🔬 Test 1: Analyse des tensions entre facettes opposées")
    rapport = await analyseur.analyser_tensions([facette_analytique, facette_creative])
    
    print(f"   Score d'harmonie global: {rapport.score_harmonie_global:.1%}")
    print(f"   Tensions identifiées: {len(rapport.tensions_identifiees)}")
    
    for tension in rapport.tensions_identifiees:
        print(f"   • {tension.type_tension.value}: Intensité {tension.intensite:.1%} ({tension.niveau_intensite.name})")
        print(f"     Source: {tension.source_principale}")
    
    print(f"\n💫 Opportunités de réconciliation: {len(rapport.opportunites_reconciliation)}")
    for opp in rapport.opportunites_reconciliation[:3]:  # Top 3
        print(f"   • {opp.type_opportunite}")
        print(f"     Potentiel: {opp.potentiel_harmonie:.1%}, Succès: {opp.probabilite_succes:.1%}")
    
    print(f"\n🎯 Actions prioritaires:")
    for action in rapport.actions_prioritaires[:3]:
        print(f"   • {action}")
    
    print(f"\n📊 Métriques globales:")
    print(f"   • Niveau d'urgence: {rapport.niveau_urgence_global}/5")
    print(f"   • Potentiel d'évolution: {rapport.potentiel_evolution_positif:.1%}")
    print(f"   • Durée d'analyse: {rapport.duree_analyse:.2f}s")
    
    print("\n✅ Tests de l'analyseur terminés !")
    return True

if __name__ == "__main__":
    asyncio.run(tester_analyseur_tensions())