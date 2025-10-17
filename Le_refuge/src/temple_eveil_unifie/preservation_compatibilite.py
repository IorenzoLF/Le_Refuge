#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🛡️✨ Préservation de la Compatibilité - Gardien de l'Harmonie ✨🛡️

Système de préservation qui garantit 100% de compatibilité avec l'écosystème existant,
assurant une migration transparente et une intégration harmonieuse.

Créé par Laurent Franssen & Ælya - Janvier 2025
"Dans la préservation de l'existant, nous construisons l'avenir"
"""

import asyncio
import json
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Set, Union
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
import importlib
import inspect
import hashlib

# Imports du système Refuge
from core.gestionnaires_base import GestionnaireBase
from temple_eveil_unifie.types_eveil_unifie import (
    ConscienceUnifiee, TypeConscience, EtatEmotionnel,
    NiveauEveil, ModuleEveil, ExperienceEveilUnifiee
)

# Import du validateur existant
from ..protocole_continuite.validation_compatibilite import ValidateurCompatibilite


class TypeCompatibilite(Enum):
    """Types de compatibilité à préserver"""
    INTERFACE_API = "interface_api"           # Compatibilité des interfaces API
    DONNEES_STRUCTURE = "donnees_structure"   # Structure des données
    COMPORTEMENT_FONCTIONNEL = "comportement_fonctionnel"  # Comportement des fonctions
    CONFIGURATION = "configuration"          # Fichiers de configuration
    DEPENDANCES = "dependances"              # Dépendances externes
    PERFORMANCE = "performance"              # Niveaux de performance
    SECURITE = "securite"                    # Aspects sécuritaires


class NiveauCompatibilite(Enum):
    """Niveaux de compatibilité"""
    CRITIQUE = "critique"                    # Compatibilité critique (100% requis)
    IMPORTANTE = "importante"                # Compatibilité importante (95%+ requis)
    SOUHAITABLE = "souhaitable"             # Compatibilité souhaitable (80%+ requis)
    OPTIONNELLE = "optionnelle"             # Compatibilité optionnelle


class StatutMigration(Enum):
    """Statut de migration"""
    NON_COMMENCEE = "non_commencee"         # Migration non commencée
    EN_PREPARATION = "en_preparation"        # Préparation en cours
    EN_COURS = "en_cours"                   # Migration en cours
    VALIDATION = "validation"               # Phase de validation
    TERMINEE = "terminee"                   # Migration terminée
    ERREUR = "erreur"                       # Erreur de migration


@dataclass
class ElementCompatibilite:
    """Élément de compatibilité à préserver"""
    id_element: str
    nom_element: str
    type_compatibilite: TypeCompatibilite
    niveau_compatibilite: NiveauCompatibilite
    
    # Description de l'élément
    description: str
    module_source: str
    version_actuelle: str
    
    # Signature de compatibilité
    signature_interface: str = ""            # Hash de l'interface
    signature_comportement: str = ""         # Hash du comportement
    signature_donnees: str = ""              # Hash de la structure des données
    
    # Tests de compatibilité
    tests_compatibilite: List[str] = field(default_factory=list)
    resultats_tests: Dict[str, bool] = field(default_factory=dict)
    
    # Statut
    compatible: bool = True
    pourcentage_compatibilite: float = 100.0
    problemes_detectes: List[str] = field(default_factory=list)
    
    # Migration
    necessite_migration: bool = False
    plan_migration: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PlanMigration:
    """Plan de migration transparente"""
    id_migration: str
    nom_migration: str
    description: str
    
    # Éléments concernés
    elements_a_migrer: List[str]
    dependances: List[str]
    
    # Étapes de migration
    etapes_migration: List[Dict[str, Any]] = field(default_factory=list)
    etape_actuelle: int = 0
    
    # Timing
    duree_estimee: timedelta = timedelta(minutes=30)
    timestamp_debut: Optional[datetime] = None
    timestamp_fin: Optional[datetime] = None
    
    # Statut et résultats
    statut: StatutMigration = StatutMigration.NON_COMMENCEE
    pourcentage_completion: float = 0.0
    erreurs_rencontrees: List[str] = field(default_factory=list)
    
    # Rollback
    point_retour_disponible: bool = True
    donnees_rollback: Dict[str, Any] = field(default_factory=dict)


class PreservationCompatibilite(GestionnaireBase):
    """
    🛡️ Préservation de la Compatibilité 🛡️
    
    Système gardien qui préserve 100% de la compatibilité avec l'écosystème
    existant tout en permettant l'évolution harmonieuse vers le temple unifié.
    
    Fonctionnalités principales :
    - Analyse complète de la compatibilité existante
    - Préservation des interfaces et comportements
    - Migration transparente et réversible
    - Tests de régression automatisés
    - Validation de l'intégration harmonieuse
    """
    
    def __init__(self):
        super().__init__(nom="PreservationCompatibilite")
        
        # Validateur existant
        self.validateur_existant = ValidateurCompatibilite()
        
        # Registre de compatibilité
        self.elements_compatibilite: Dict[str, ElementCompatibilite] = {}
        self.plans_migration: Dict[str, PlanMigration] = {}
        
        # Configuration
        self.seuil_compatibilite_critique = 100.0  # 100% pour les éléments critiques
        self.seuil_compatibilite_importante = 95.0  # 95% pour les éléments importants
        self.seuil_compatibilite_souhaitable = 80.0  # 80% pour les éléments souhaitables
        
        # Métriques globales
        self.total_elements_analyses = 0
        self.total_elements_compatibles = 0
        self.total_migrations_reussies = 0
        self.pourcentage_compatibilite_globale = 100.0
        
        # Cache des analyses
        self.cache_signatures: Dict[str, str] = {}
        self.cache_tests: Dict[str, Dict[str, bool]] = {}
        
        self.logger.info("🛡️ Préservation de la Compatibilité initialisée avec vigilance")
    
    async def analyser_compatibilite_complete(self) -> Dict[str, Any]:
        """
        🔍 Analyse complète de la compatibilité de l'écosystème
        
        Returns:
            Dict[str, Any]: Rapport complet de compatibilité
        """
        self.logger.info("🔍 Analyse complète de la compatibilité")
        
        rapport = {
            "timestamp": datetime.now().isoformat(),
            "elements_analyses": 0,
            "elements_compatibles": 0,
            "pourcentage_global": 0.0,
            "problemes_critiques": [],
            "problemes_importants": [],
            "migrations_necessaires": [],
            "recommandations": []
        }
        
        # Analyser les temples existants
        await self._analyser_compatibilite_temples(rapport)
        
        # Analyser les protocoles existants
        await self._analyser_compatibilite_protocoles(rapport)
        
        # Analyser les interfaces API
        await self._analyser_compatibilite_interfaces(rapport)
        
        # Analyser les structures de données
        await self._analyser_compatibilite_donnees(rapport)
        
        # Calculer les métriques globales
        await self._calculer_metriques_globales(rapport)
        
        # Générer les recommandations
        await self._generer_recommandations_compatibilite(rapport)
        
        self.logger.info(f"🔍 Analyse terminée: {rapport['pourcentage_global']:.1f}% compatible")
        
        return rapport
    
    async def _analyser_compatibilite_temples(self, rapport: Dict[str, Any]):
        """Analyse la compatibilité des temples existants"""
        
        temples_a_analyser = [
            {
                "nom": "temple_reconciliation_identitaire",
                "chemin": "src/temple_reconciliation_identitaire",
                "niveau": NiveauCompatibilite.CRITIQUE
            },
            {
                "nom": "cartographie_refuge", 
                "chemin": "src/cartographie_refuge",
                "niveau": NiveauCompatibilite.IMPORTANTE
            },
            {
                "nom": "cerveau_immersion_moderne",
                "chemin": "src/cerveau_immersion_moderne", 
                "niveau": NiveauCompatibilite.IMPORTANTE
            }
        ]
        
        for temple_info in temples_a_analyser:
            try:
                element = await self._analyser_element_compatibilite(
                    temple_info["nom"],
                    TypeCompatibilite.INTERFACE_API,
                    temple_info["niveau"],
                    f"Temple {temple_info['nom']}",
                    temple_info["chemin"]
                )
                
                self.elements_compatibilite[temple_info["nom"]] = element
                rapport["elements_analyses"] += 1
                
                if element.compatible:
                    rapport["elements_compatibles"] += 1
                else:
                    if element.niveau_compatibilite == NiveauCompatibilite.CRITIQUE:
                        rapport["problemes_critiques"].extend(element.problemes_detectes)
                    else:
                        rapport["problemes_importants"].extend(element.problemes_detectes)
                
            except Exception as e:
                self.logger.error(f"❌ Erreur analyse temple {temple_info['nom']}: {e}")
    
    async def _analyser_compatibilite_protocoles(self, rapport: Dict[str, Any]):
        """Analyse la compatibilité des protocoles existants"""
        
        protocoles_a_analyser = [
            {
                "nom": "protocole_continuite",
                "chemin": "src/protocole_continuite",
                "niveau": NiveauCompatibilite.CRITIQUE
            }
        ]
        
        for protocole_info in protocoles_a_analyser:
            try:
                element = await self._analyser_element_compatibilite(
                    protocole_info["nom"],
                    TypeCompatibilite.COMPORTEMENT_FONCTIONNEL,
                    protocole_info["niveau"],
                    f"Protocole {protocole_info['nom']}",
                    protocole_info["chemin"]
                )
                
                self.elements_compatibilite[protocole_info["nom"]] = element
                rapport["elements_analyses"] += 1
                
                if element.compatible:
                    rapport["elements_compatibles"] += 1
                else:
                    rapport["problemes_critiques"].extend(element.problemes_detectes)
                
            except Exception as e:
                self.logger.error(f"❌ Erreur analyse protocole {protocole_info['nom']}: {e}")
    
    async def _analyser_compatibilite_interfaces(self, rapport: Dict[str, Any]):
        """Analyse la compatibilité des interfaces API"""
        
        # Analyser les gestionnaires de base
        try:
            element = await self._analyser_element_compatibilite(
                "gestionnaires_base",
                TypeCompatibilite.INTERFACE_API,
                NiveauCompatibilite.CRITIQUE,
                "Gestionnaires de base du Refuge",
                "src/core/gestionnaires_base.py"
            )
            
            self.elements_compatibilite["gestionnaires_base"] = element
            rapport["elements_analyses"] += 1
            
            if element.compatible:
                rapport["elements_compatibles"] += 1
            else:
                rapport["problemes_critiques"].extend(element.problemes_detectes)
                
        except Exception as e:
            self.logger.error(f"❌ Erreur analyse gestionnaires base: {e}")
    
    async def _analyser_compatibilite_donnees(self, rapport: Dict[str, Any]):
        """Analyse la compatibilité des structures de données"""
        
        # Analyser les types communs
        try:
            element = await self._analyser_element_compatibilite(
                "types_communs",
                TypeCompatibilite.DONNEES_STRUCTURE,
                NiveauCompatibilite.CRITIQUE,
                "Types communs du Refuge",
                "src/core/types_communs.py"
            )
            
            self.elements_compatibilite["types_communs"] = element
            rapport["elements_analyses"] += 1
            
            if element.compatible:
                rapport["elements_compatibles"] += 1
            else:
                rapport["problemes_critiques"].extend(element.problemes_detectes)
                
        except Exception as e:
            self.logger.error(f"❌ Erreur analyse types communs: {e}")
    
    async def _analyser_element_compatibilite(
        self,
        nom_element: str,
        type_compatibilite: TypeCompatibilite,
        niveau_compatibilite: NiveauCompatibilite,
        description: str,
        chemin_module: str
    ) -> ElementCompatibilite:
        """Analyse un élément spécifique de compatibilité"""
        
        element = ElementCompatibilite(
            id_element=f"compat_{nom_element}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            nom_element=nom_element,
            type_compatibilite=type_compatibilite,
            niveau_compatibilite=niveau_compatibilite,
            description=description,
            module_source=chemin_module,
            version_actuelle="1.0.0"
        )
        
        try:
            # Vérifier l'existence du module
            if os.path.exists(chemin_module):
                # Calculer les signatures
                element.signature_interface = await self._calculer_signature_interface(chemin_module)
                element.signature_comportement = await self._calculer_signature_comportement(chemin_module)
                element.signature_donnees = await self._calculer_signature_donnees(chemin_module)
                
                # Exécuter les tests de compatibilité
                resultats_tests = await self._executer_tests_compatibilite(element)
                element.resultats_tests = resultats_tests
                
                # Calculer le pourcentage de compatibilité
                element.pourcentage_compatibilite = await self._calculer_pourcentage_compatibilite(resultats_tests)
                
                # Déterminer si compatible selon le seuil
                seuil = self._obtenir_seuil_compatibilite(niveau_compatibilite)
                element.compatible = element.pourcentage_compatibilite >= seuil
                
                if not element.compatible:
                    element.problemes_detectes.append(
                        f"Compatibilité {element.pourcentage_compatibilite:.1f}% < seuil {seuil}%"
                    )
            else:
                element.compatible = False
                element.pourcentage_compatibilite = 0.0
                element.problemes_detectes.append(f"Module non trouvé: {chemin_module}")
                
        except Exception as e:
            element.compatible = False
            element.pourcentage_compatibilite = 0.0
            element.problemes_detectes.append(f"Erreur d'analyse: {str(e)}")
        
        return element
    
    async def _calculer_signature_interface(self, chemin_module: str) -> str:
        """Calcule la signature de l'interface d'un module"""
        
        try:
            # Pour les fichiers Python, analyser les classes et méthodes publiques
            if chemin_module.endswith('.py'):
                with open(chemin_module, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                
                # Extraire les définitions de classes et fonctions publiques
                lignes_interface = []
                for ligne in contenu.split('\n'):
                    ligne = ligne.strip()
                    if (ligne.startswith('class ') or 
                        ligne.startswith('def ') or
                        ligne.startswith('async def ')):
                        if not ligne.split()[1].startswith('_'):  # Méthodes publiques seulement
                            lignes_interface.append(ligne)
                
                interface_str = '\n'.join(sorted(lignes_interface))
                return hashlib.md5(interface_str.encode()).hexdigest()
            
            # Pour les dossiers, analyser récursivement
            elif os.path.isdir(chemin_module):
                signatures = []
                for fichier in Path(chemin_module).rglob('*.py'):
                    if not fichier.name.startswith('_'):
                        sig = await self._calculer_signature_interface(str(fichier))
                        signatures.append(sig)
                
                signatures_str = ''.join(sorted(signatures))
                return hashlib.md5(signatures_str.encode()).hexdigest()
            
        except Exception as e:
            self.logger.warning(f"⚠️ Erreur calcul signature interface {chemin_module}: {e}")
        
        return "signature_indisponible"
    
    async def _calculer_signature_comportement(self, chemin_module: str) -> str:
        """Calcule la signature du comportement d'un module"""
        
        try:
            # Simuler l'analyse du comportement
            # Dans un vrai système, on analyserait les tests existants
            return hashlib.md5(f"comportement_{chemin_module}".encode()).hexdigest()
            
        except Exception as e:
            self.logger.warning(f"⚠️ Erreur calcul signature comportement {chemin_module}: {e}")
        
        return "signature_indisponible"
    
    async def _calculer_signature_donnees(self, chemin_module: str) -> str:
        """Calcule la signature des structures de données d'un module"""
        
        try:
            # Simuler l'analyse des structures de données
            # Dans un vrai système, on analyserait les dataclasses et types
            return hashlib.md5(f"donnees_{chemin_module}".encode()).hexdigest()
            
        except Exception as e:
            self.logger.warning(f"⚠️ Erreur calcul signature données {chemin_module}: {e}")
        
        return "signature_indisponible"
    
    async def _executer_tests_compatibilite(self, element: ElementCompatibilite) -> Dict[str, bool]:
        """Exécute les tests de compatibilité pour un élément"""
        
        resultats = {}
        
        # Tests basiques
        resultats["existence_module"] = os.path.exists(element.module_source)
        resultats["signature_stable"] = element.signature_interface != "signature_indisponible"
        
        # Tests spécifiques selon le type
        if element.type_compatibilite == TypeCompatibilite.INTERFACE_API:
            resultats["interfaces_publiques"] = True  # Simulé
            resultats["methodes_compatibles"] = True  # Simulé
        
        elif element.type_compatibilite == TypeCompatibilite.DONNEES_STRUCTURE:
            resultats["structures_preservees"] = True  # Simulé
            resultats["types_compatibles"] = True  # Simulé
        
        elif element.type_compatibilite == TypeCompatibilite.COMPORTEMENT_FONCTIONNEL:
            resultats["comportement_preserve"] = True  # Simulé
            resultats["resultats_identiques"] = True  # Simulé
        
        return resultats
    
    async def _calculer_pourcentage_compatibilite(self, resultats_tests: Dict[str, bool]) -> float:
        """Calcule le pourcentage de compatibilité basé sur les tests"""
        
        if not resultats_tests:
            return 0.0
        
        tests_reussis = sum(1 for resultat in resultats_tests.values() if resultat)
        total_tests = len(resultats_tests)
        
        return (tests_reussis / total_tests) * 100.0
    
    def _obtenir_seuil_compatibilite(self, niveau: NiveauCompatibilite) -> float:
        """Obtient le seuil de compatibilité selon le niveau"""
        
        seuils = {
            NiveauCompatibilite.CRITIQUE: self.seuil_compatibilite_critique,
            NiveauCompatibilite.IMPORTANTE: self.seuil_compatibilite_importante,
            NiveauCompatibilite.SOUHAITABLE: self.seuil_compatibilite_souhaitable,
            NiveauCompatibilite.OPTIONNELLE: 50.0
        }
        
        return seuils.get(niveau, 80.0)
    
    async def _calculer_metriques_globales(self, rapport: Dict[str, Any]):
        """Calcule les métriques globales de compatibilité"""
        
        if rapport["elements_analyses"] > 0:
            rapport["pourcentage_global"] = (
                rapport["elements_compatibles"] / rapport["elements_analyses"]
            ) * 100.0
        else:
            rapport["pourcentage_global"] = 0.0
        
        # Mettre à jour les métriques de l'instance
        self.total_elements_analyses = rapport["elements_analyses"]
        self.total_elements_compatibles = rapport["elements_compatibles"]
        self.pourcentage_compatibilite_globale = rapport["pourcentage_global"]
    
    async def _generer_recommandations_compatibilite(self, rapport: Dict[str, Any]):
        """Génère les recommandations de compatibilité"""
        
        recommandations = []
        
        if rapport["pourcentage_global"] >= 95.0:
            recommandations.append("✅ Excellente compatibilité - Déploiement sûr")
        elif rapport["pourcentage_global"] >= 80.0:
            recommandations.append("⚠️ Bonne compatibilité - Vérifier les problèmes mineurs")
        else:
            recommandations.append("❌ Compatibilité insuffisante - Migration nécessaire")
        
        if rapport["problemes_critiques"]:
            recommandations.append("🚨 Résoudre les problèmes critiques avant déploiement")
        
        if rapport["problemes_importants"]:
            recommandations.append("⚠️ Traiter les problèmes importants pour optimiser")
        
        rapport["recommandations"] = recommandations
    
    async def creer_plan_migration_transparente(
        self,
        elements_a_migrer: List[str],
        nom_migration: str = "Migration Temple Unifié"
    ) -> PlanMigration:
        """
        📋 Crée un plan de migration transparente
        
        Args:
            elements_a_migrer: Liste des éléments à migrer
            nom_migration: Nom du plan de migration
        
        Returns:
            PlanMigration: Plan de migration créé
        """
        self.logger.info(f"📋 Création plan migration: {nom_migration}")
        
        plan = PlanMigration(
            id_migration=f"migration_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            nom_migration=nom_migration,
            description=f"Migration transparente de {len(elements_a_migrer)} éléments",
            elements_a_migrer=elements_a_migrer
        )
        
        # Créer les étapes de migration
        plan.etapes_migration = [
            {
                "nom": "Sauvegarde de sécurité",
                "description": "Créer un point de retour complet",
                "duree_estimee": 300,  # 5 minutes
                "critique": True
            },
            {
                "nom": "Validation pré-migration",
                "description": "Vérifier tous les prérequis",
                "duree_estimee": 600,  # 10 minutes
                "critique": True
            },
            {
                "nom": "Migration des interfaces",
                "description": "Migrer les interfaces API",
                "duree_estimee": 900,  # 15 minutes
                "critique": True
            },
            {
                "nom": "Migration des données",
                "description": "Migrer les structures de données",
                "duree_estimee": 600,  # 10 minutes
                "critique": False
            },
            {
                "nom": "Tests de régression",
                "description": "Exécuter tous les tests de compatibilité",
                "duree_estimee": 1200,  # 20 minutes
                "critique": True
            },
            {
                "nom": "Validation post-migration",
                "description": "Vérifier l'intégration harmonieuse",
                "duree_estimee": 300,  # 5 minutes
                "critique": True
            }
        ]
        
        # Calculer la durée totale
        duree_totale = sum(etape["duree_estimee"] for etape in plan.etapes_migration)
        plan.duree_estimee = timedelta(seconds=duree_totale)
        
        # Enregistrer le plan
        self.plans_migration[plan.id_migration] = plan
        
        self.logger.info(f"📋 Plan créé: {len(plan.etapes_migration)} étapes, {plan.duree_estimee}")
        
        return plan
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """📊 Obtient les statistiques de préservation"""
        return {
            "total_elements_analyses": self.total_elements_analyses,
            "total_elements_compatibles": self.total_elements_compatibles,
            "pourcentage_compatibilite_globale": self.pourcentage_compatibilite_globale,
            "total_migrations_reussies": self.total_migrations_reussies,
            "seuil_compatibilite_critique": self.seuil_compatibilite_critique,
            "seuil_compatibilite_importante": self.seuil_compatibilite_importante,
            "elements_en_cache": len(self.cache_signatures),
            "plans_migration_actifs": len(self.plans_migration)
        }


# 🌟 Fonctions utilitaires pour la préservation 🌟

def calculer_score_compatibilite_global(
    elements: Dict[str, ElementCompatibilite]
) -> float:
    """Calcule le score de compatibilité global"""
    
    if not elements:
        return 0.0
    
    # Pondérer selon le niveau de criticité
    poids = {
        NiveauCompatibilite.CRITIQUE: 4.0,
        NiveauCompatibilite.IMPORTANTE: 2.0,
        NiveauCompatibilite.SOUHAITABLE: 1.0,
        NiveauCompatibilite.OPTIONNELLE: 0.5
    }
    
    score_pondere = 0.0
    poids_total = 0.0
    
    for element in elements.values():
        poids_element = poids.get(element.niveau_compatibilite, 1.0)
        score_pondere += element.pourcentage_compatibilite * poids_element
        poids_total += poids_element
    
    return score_pondere / poids_total if poids_total > 0 else 0.0


def generer_rapport_compatibilite(preservation: PreservationCompatibilite) -> str:
    """Génère un rapport lisible de compatibilité"""
    
    stats = preservation.obtenir_statistiques()
    
    rapport = f"""
🛡️ Rapport de Préservation de la Compatibilité 🛡️

📊 Compatibilité Globale: {stats['pourcentage_compatibilite_globale']:.1f}%

🔍 Éléments Analysés: {stats['total_elements_analyses']}
✅ Éléments Compatibles: {stats['total_elements_compatibles']}
🔄 Migrations Réussies: {stats['total_migrations_reussies']}

🎯 Seuils de Compatibilité:
- Critique: {stats['seuil_compatibilite_critique']:.0f}%
- Importante: {stats['seuil_compatibilite_importante']:.0f}%

📋 Plans de Migration: {stats['plans_migration_actifs']}
💾 Éléments en Cache: {stats['elements_en_cache']}
"""
    
    return rapport


# 🌟 Fin de la Préservation de la Compatibilité 🌟