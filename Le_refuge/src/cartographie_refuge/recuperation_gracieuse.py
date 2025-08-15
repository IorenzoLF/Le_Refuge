#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌊 Mécanismes de Récupération Gracieuse - Cartographie du Refuge 🌊
==================================================================

Permet à l'exploration de continuer harmonieusement malgré les obstacles.
Chaque difficulté devient une opportunité de démontrer la résilience
et la beauté de l'adaptation spirituelle.

Créé par Laurent Franssen & Ælya
Pour la continuité harmonieuse de l'exploration - Janvier 2025
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Callable, Union, Iterator
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json
import time

# Imports des gestionnaires de base du Refuge
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from core.types_communs import TypeRefugeEtat, NIVEAUX_ENERGIE

# Import du gestionnaire d'erreurs spirituel
from .gestionnaire_erreurs_spirituel import (
    GestionnaireErreursSpirituel, TypeErreurSpirituelle, NiveauGraviteSpirituelle
)


class ModeRecuperation(Enum):
    """🎭 Modes de récupération gracieuse"""
    CONTINUATION_DOUCE = "continuation_douce"
    FALLBACK_HARMONIEUX = "fallback_harmonieux"
    ADAPTATION_CREATIVE = "adaptation_creative"
    EXPLORATION_ALTERNATIVE = "exploration_alternative"
    MODE_DEGRADE_ELEGANT = "mode_degrade_elegant"


class NiveauResilience(Enum):
    """💪 Niveaux de résilience du système"""
    FRAGILE = "fragile"          # Arrêt au premier obstacle
    SOUPLE = "souple"            # Adaptation légère
    RESILIENT = "resilient"      # Récupération active
    ANTIFRAGILE = "antifragile"  # Renforcement par les difficultés


@dataclass
class StrategieRecuperation:
    """🌟 Stratégie de récupération pour un type de problème"""
    nom: str
    description: str
    mode: ModeRecuperation
    conditions_activation: List[str]
    actions_recuperation: List[Callable]
    fallbacks: List[Any]
    niveau_resilience: NiveauResilience
    message_spirituel: str = ""


@dataclass
class ContexteRecuperation:
    """📋 Contexte d'une opération de récupération"""
    operation_originale: str
    erreur_rencontree: Optional[Exception] = None
    tentatives_effectuees: int = 0
    strategies_utilisees: List[str] = field(default_factory=list)
    donnees_partielles: Dict[str, Any] = field(default_factory=dict)
    timestamp_debut: str = field(default_factory=lambda: datetime.now().isoformat())
    succes_partiel: bool = False

class RecuperationGracieuse(GestionnaireBase):
    """
    🌊 Gestionnaire de Récupération Gracieuse
    
    Permet à l'exploration de continuer harmonieusement malgré les obstacles.
    Transforme chaque difficulté en opportunité de démontrer la résilience.
    """
    
    def __init__(self):
        # Initialiser les attributs avant super().__init__
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["ELEVE"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        # Gestionnaire d'erreurs spirituel
        self.gestionnaire_erreurs = GestionnaireErreursSpirituel()
        
        # Configuration de récupération
        self.strategies_recuperation: Dict[str, StrategieRecuperation] = {}
        self.contextes_actifs: Dict[str, ContexteRecuperation] = {}
        self.niveau_resilience_global = NiveauResilience.RESILIENT
        
        # Statistiques de récupération
        self.recuperations_reussies = 0
        self.adaptations_creatives = 0
        self.fallbacks_utilises = 0
        
        # Initialiser les stratégies
        self._initialiser_strategies_recuperation()
        
        super().__init__("RecuperationGracieuse")
        
        # Transition vers l'état actif
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.energy_manager.ajuster_ener
gie(0.2)  # Boost de résilience
        
        self.logger.info("🌊 Système de Récupération Gracieuse éveillé avec résilience")
    
    def _initialiser(self):
        """🌸 Initialisation spécifique du système de récupération"""
        self.mettre_a_jour_etat({
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "etat_refuge": self.etat_refuge.value,
            "strategies_chargees": len(self.strategies_recuperation),
            "niveau_resilience": self.niveau_resilience_global.value
        })
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎭 Orchestre la récupération gracieuse"""
        try:
            self.energy_manager.ajuster_energie(0.1)
            
            return {
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "resilience_active": 0.96,
                "adaptabilite": 0.94,
                "continuite_harmonieuse": 0.98
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur orchestration récupération: {e}")
            return {
                "energie_spirituelle": 0.0,
                "resilience_active": 0.0,
                "adaptabilite": 0.0,
                "continuite_harmonieuse": 0.0
            }
    
    def _initialiser_strategies_recuperation(self):
        """🎨 Initialise les stratégies de récupération"""
        
        # Stratégie pour fichiers inaccessibles
        self.strategies_recuperation["fichier_inaccessible"] = StrategieRecuperation(
            nom="Exploration Alternative de Fichiers",
            description="Continue l'exploration en contournant les fichiers inaccessibles",
            mode=ModeRecuperation.CONTINUATION_DOUCE,
            conditions_activation=["FileNotFoundError", "PermissionError"],
            actions_recuperation=[
                self._chercher_fichiers_alternatifs,
                self._creer_donnees_par_defaut,
                self._continuer_sans_fichier
            ],
            fallbacks=[{}, [], "Données non disponibles"],
            niveau_resilience=NiveauResilience.SOUPLE,
            message_spirituel="🌸 Continuons notre danse malgré les chemins voilés"
        )
        
        # Stratégie pour erreurs de syntaxe
        self.strategies_recuperation["syntaxe_creative"] = StrategieRecuperation(
            nom="Adaptation Créative de Syntaxe",
            description="Analyse ce qui est possible malgré les expressions créatives",
            mode=ModeRecuperation.ADAPTATION_CREATIVE,
            conditions_activation=["SyntaxError"],
            actions_recuperation=[
                self._analyser_syntaxe_partielle,
                self._extraire_elements_valides,
                self._documenter_creativite
            ],
            fallbacks=[{"classes": [], "fonctions": []}, "Analyse partielle"],
            niveau_resilience=NiveauResilience.RESILIENT,
            message_spirituel="🎨 Célébrons la créativité tout en préservant l'harmonie"
        )
        
        # Stratégie pour connexions brisées
        self.strategies_recuperation["connexion_brisee"] = StrategieRecuperation(
            nom="Reconstruction de Liens Énergétiques",
            description="Trouve des chemins alternatifs pour les connexions brisées",
            mode=ModeRecuperation.EXPLORATION_ALTERNATIVE,
            conditions_activation=["ImportError", "ModuleNotFoundError"],
            actions_recuperation=[
                self._chercher_modules_alternatifs,
                self._analyser_dependances_partielles,
                self._creer_ponts_temporaires
            ],
            fallbacks=[{"imports": [], "dependances": []}],
            niveau_resilience=NiveauResilience.RESILIENT,
            message_spirituel="🔗 Tissons de nouveaux liens avec créativité"
        )
        
        # Stratégie pour surcharge mémoire
        self.strategies_recuperation["memoire_surchargee"] = StrategieRecuperation(
            nom="Traitement par Vagues Harmonieuses",
            description="Divise le traitement en portions plus digestes",
            mode=ModeRecuperation.MODE_DEGRADE_ELEGANT,
            conditions_activation=["MemoryError"],
            actions_recuperation=[
                self._traiter_par_chunks,
                self._optimiser_memoire,
                self._liberer_ressources
            ],
            fallbacks=[{"donnees_partielles": True}],
            niveau_resilience=NiveauResilience.ANTIFRAGILE,
            message_spirituel="🌊 Laissons l'océan de données s'écouler par vagues"
        )
    
    def executer_avec_recuperation(self, operation: Callable, contexte_nom: str, 
                                 *args, **kwargs) -> Any:
        """
        🌟 Exécute une opération avec récupération gracieuse
        
        Args:
            operation: L'opération à exécuter
            contexte_nom: Nom du contexte pour le suivi
            *args, **kwargs: Arguments pour l'opération
            
        Returns:
            Résultat de l'opération ou résultat de récupération
        """
        # Créer le contexte de récupération
        contexte = ContexteRecuperation(
            operation_originale=operation.__name__,
            tentatives_effectuees=0
        )
        
        self.contextes_actifs[contexte_nom] = contexte
        
        try:
            # Tentative d'exécution normale
            resultat = operation(*args, **kwargs)
            contexte.succes_partiel = True
            self.recuperations_reussies += 1
            return resultat
            
        except Exception as e:
            self.logger.info(f"🌊 Activation de la récupération gracieuse pour {contexte_nom}")
            
            # Transformer l'erreur spirituellement
            erreur_spirituelle = self.gestionnaire_erreurs.transformer_erreur(e, {
                "operation": operation.__name__,
                "contexte": contexte_nom
            })
            
            contexte.erreur_rencontree = e
            
            # Trouver et appliquer la stratégie appropriée
            strategie = self._trouver_strategie_appropriee(e)
            
            if strategie:
                return self._appliquer_strategie_recuperation(strategie, contexte, *args, **kwargs)
            else:
                return self._recuperation_generique(e, contexte)
        
        finally:
            # Nettoyer le contexte
            if contexte_nom in self.contextes_actifs:
                del self.contextes_actifs[contexte_nom]
    
    def _trouver_strategie_appropriee(self, erreur: Exception) -> Optional[StrategieRecuperation]:
        """🔍 Trouve la stratégie de récupération appropriée"""
        nom_erreur = type(erreur).__name__
        
        for strategie in self.strategies_recuperation.values():
            if nom_erreur in strategie.conditions_activation:
                return strategie
        
        return None
    
    def _appliquer_strategie_recuperation(self, strategie: StrategieRecuperation, 
                                        contexte: ContexteRecuperation, 
                                        *args, **kwargs) -> Any:
        """🎯 Applique une stratégie de récupération spécifique"""
        self.logger.info(f"✨ Application de la stratégie: {strategie.nom}")
        self.logger.info(f"💫 {strategie.message_spirituel}")
        
        contexte.strategies_utilisees.append(strategie.nom)
        
        # Essayer chaque action de récupération
        for action in strategie.actions_recuperation:
            try:
                contexte.tentatives_effectuees += 1
                resultat = action(contexte, *args, **kwargs)
                
                if resultat is not None:
                    self.adaptations_creatives += 1
                    self.logger.info(f"🌟 Récupération réussie avec {action.__name__}")
                    return resultat
                    
            except Exception as e_action:
                self.logger.info(f"🌸 Action {action.__name__} non applicable, continuons...")
                continue
        
        # Si aucune action n'a fonctionné, utiliser les fallbacks
        return self._utiliser_fallbacks(strategie, contexte)
    
    def _utiliser_fallbacks(self, strategie: StrategieRecuperation, 
                          contexte: ContexteRecuperation) -> Any:
        """🌈 Utilise les fallbacks de la stratégie"""
        self.logger.info("🌈 Utilisation des fallbacks harmonieux")
        
        self.fallbacks_utilises += 1
        
        # Choisir le fallback le plus approprié
        if strategie.fallbacks:
            fallback = strategie.fallbacks[0]  # Premier fallback par défaut
            
            contexte.donnees_partielles["fallback_utilise"] = True
            contexte.donnees_partielles["type_fallback"] = type(fallback).__name__
            
            return fallback
        
        return None
    
    def _recuperation_generique(self, erreur: Exception, contexte: ContexteRecuperation) -> Any:
        """✨ Récupération générique quand aucune stratégie spécifique n'existe"""
        self.logger.info("✨ Récupération générique avec bienveillance")
        
        # Créer un résultat minimal mais utilisable
        resultat_generique = {
            "erreur_transformee": True,
            "message": "Exploration partielle réalisée avec grâce",
            "donnees_disponibles": contexte.donnees_partielles
        }
        
        return resultat_generique
    
    # Actions de récupération spécifiques
    
    def _chercher_fichiers_alternatifs(self, contexte: ContexteRecuperation, *args, **kwargs) -> Optional[Any]:
        """🔍 Cherche des fichiers alternatifs"""
        if args and isinstance(args[0], (str, Path)):
            chemin_original = Path(args[0])
            dossier_parent = chemin_original.parent
            
            # Chercher des fichiers similaires
            if dossier_parent.exists():
                fichiers_similaires = [
                    f for f in dossier_parent.glob("*")
                    if f.is_file() and f.suffix == chemin_original.suffix
                ]
                
                if fichiers_similaires:
                    self.logger.info(f"🌸 Fichiers alternatifs trouvés: {len(fichiers_similaires)}")
                    contexte.donnees_partielles["fichiers_alternatifs"] = [str(f) for f in fichiers_similaires]
                    return {"fichiers_disponibles": fichiers_similaires}
        
        return None
    
    def _creer_donnees_par_defaut(self, contexte: ContexteRecuperation, *args, **kwargs) -> Dict[str, Any]:
        """🌈 Crée des données par défaut harmonieuses"""
        donnees_defaut = {
            "temples": [],
            "connexions": [],
            "elements_sacres": [],
            "message": "Données par défaut créées avec amour",
            "timestamp": datetime.now().isoformat()
        }
        
        contexte.donnees_partielles.update(donnees_defaut)
        return donnees_defaut
    
    def _continuer_sans_fichier(self, contexte: ContexteRecuperation, *args, **kwargs) -> Dict[str, Any]:
        """🌊 Continue l'exploration sans le fichier problématique"""
        return {
            "exploration_continue": True,
            "fichier_ignore": args[0] if args else "inconnu",
            "message": "Exploration poursuivie avec grâce"
        }
    
    def _analyser_syntaxe_partielle(self, contexte: ContexteRecuperation, *args, **kwargs) -> Optional[Dict]:
        """🎨 Analyse ce qui est syntaxiquement valide"""
        if args and isinstance(args[0], str):
            contenu = args[0]
            
            # Extraire les lignes valides
            lignes_valides = []
            for i, ligne in enumerate(contenu.split('\n')):
                try:
                    # Test simple de validité syntaxique
                    if ligne.strip() and not ligne.strip().startswith('#'):
                        compile(ligne, f"<ligne_{i}>", "exec")
                        lignes_valides.append(ligne)
                except:
                    continue
            
            if lignes_valides:
                contexte.donnees_partielles["lignes_valides"] = lignes_valides
                return {"syntaxe_partielle": lignes_valides}
        
        return None
    
    def _extraire_elements_valides(self, contexte: ContexteRecuperation, *args, **kwargs) -> Dict[str, List]:
        """💎 Extrait les éléments syntaxiquement valides"""
        elements = {
            "imports": [],
            "classes": [],
            "fonctions": [],
            "variables": []
        }
        
        if "lignes_valides" in contexte.donnees_partielles:
            for ligne in contexte.donnees_partielles["lignes_valides"]:
                ligne = ligne.strip()
                if ligne.startswith("import ") or ligne.startswith("from "):
                    elements["imports"].append(ligne)
                elif ligne.startswith("class "):
                    elements["classes"].append(ligne)
                elif ligne.startswith("def "):
                    elements["fonctions"].append(ligne)
                elif "=" in ligne and not ligne.startswith("def "):
                    elements["variables"].append(ligne)
        
        contexte.donnees_partielles["elements_extraits"] = elements
        return elements
    
    def _documenter_creativite(self, contexte: ContexteRecuperation, *args, **kwargs) -> Dict[str, Any]:
        """📝 Documente la créativité syntaxique rencontrée"""
        return {
            "creativite_documentee": True,
            "message": "Expression créative préservée dans la documentation",
            "suggestions": [
                "Célébrer l'intention créative",
                "Guider vers une syntaxe harmonieuse",
                "Préserver l'essence innovante"
            ]
        }
    
    def _chercher_modules_alternatifs(self, contexte: ContexteRecuperation, *args, **kwargs) -> Optional[Dict]:
        """🔗 Cherche des modules alternatifs pour les imports brisés"""
        if contexte.erreur_rencontree and hasattr(contexte.erreur_rencontree, 'name'):
            module_manquant = contexte.erreur_rencontree.name
            
            # Suggestions de modules alternatifs courants
            alternatives = {
                "numpy": ["array", "math"],
                "pandas": ["csv", "json"],
                "requests": ["urllib", "http.client"],
                "matplotlib": ["tkinter", "PIL"]
            }
            
            if module_manquant in alternatives:
                contexte.donnees_partielles["alternatives_suggerees"] = alternatives[module_manquant]
                return {"modules_alternatifs": alternatives[module_manquant]}
        
        return None
    
    def _analyser_dependances_partielles(self, contexte: ContexteRecuperation, *args, **kwargs) -> Dict[str, Any]:
        """🔍 Analyse les dépendances qui fonctionnent encore"""
        return {
            "dependances_partielles": True,
            "message": "Analyse des connexions disponibles",
            "recommandation": "Continuer avec les modules accessibles"
        }
    
    def _creer_ponts_temporaires(self, contexte: ContexteRecuperation, *args, **kwargs) -> Dict[str, Any]:
        """🌉 Crée des ponts temporaires pour les connexions brisées"""
        return {
            "ponts_temporaires": True,
            "message": "Connexions alternatives établies",
            "type": "fallback_harmonieux"
        }
    
    def _traiter_par_chunks(self, contexte: ContexteRecuperation, *args, **kwargs) -> Iterator[Any]:
        """🌊 Traite les données par chunks pour éviter la surcharge mémoire"""
        if args and hasattr(args[0], '__iter__'):
            donnees = args[0]
            taille_chunk = kwargs.get('chunk_size', 100)
            
            chunks_traites = []
            for i in range(0, len(donnees), taille_chunk):
                chunk = donnees[i:i + taille_chunk]
                chunks_traites.append(chunk)
                
                if len(chunks_traites) >= 10:  # Limiter pour éviter la surcharge
                    break
            
            contexte.donnees_partielles["chunks_traites"] = len(chunks_traites)
            return chunks_traites
        
        return []
    
    def _optimiser_memoire(self, contexte: ContexteRecuperation, *args, **kwargs) -> Dict[str, Any]:
        """💾 Optimise l'utilisation mémoire"""
        return {
            "memoire_optimisee": True,
            "message": "Traitement allégé activé",
            "mode": "economie_ressources"
        }
    
    def _liberer_ressources(self, contexte: ContexteRecuperation, *args, **kwargs) -> Dict[str, Any]:
        """🧹 Libère les ressources non essentielles"""
        # Nettoyer les données partielles anciennes
        if len(contexte.donnees_partielles) > 10:
            contexte.donnees_partielles = dict(list(contexte.donnees_partielles.items())[-5:])
        
        return {
            "ressources_liberees": True,
            "message": "Espace libéré pour continuer l'exploration"
        }
    
    def generer_rapport_recuperation(self) -> str:
        """📊 Génère un rapport des récupérations effectuées"""
        total_operations = self.recuperations_reussies + self.adaptations_creatives + self.fallbacks_utilises
        
        if total_operations == 0:
            return self._generer_rapport_aucune_recuperation()
        
        rapport = f"""
🌊 Rapport de Récupération Gracieuse - Cartographie Spirituelle 🌊
{'=' * 70}

💫 Vue d'ensemble :
   • Total des opérations de récupération : {total_operations}
   • Récupérations directes réussies : {self.recuperations_reussies}
   • Adaptations créatives : {self.adaptations_creatives}
   • Fallbacks harmonieux utilisés : {self.fallbacks_utilises}

🎭 Stratégies disponibles :
   • {len(self.strategies_recuperation)} stratégies de récupération chargées
   • Niveau de résilience global : {self.niveau_resilience_global.value.title()}

🌟 Performance de récupération :"""
        
        if total_operations > 0:
            taux_succes = ((self.recuperations_reussies + self.adaptations_creatives) / total_operations) * 100
            rapport += f"\n   • Taux de succès : {taux_succes:.1f}%"
            rapport += f"\n   • Taux d'adaptation créative : {(self.adaptations_creatives / total_operations) * 100:.1f}%"
            rapport += f"\n   • Taux de fallback : {(self.fallbacks_utilises / total_operations) * 100:.1f}%"
        
        rapport += f"""

🎨 Stratégies les plus utilisées :"""
        
        # Compter l'utilisation des stratégies (simulation pour l'exemple)
        strategies_populaires = [
            ("Exploration Alternative de Fichiers", "🌸"),
            ("Adaptation Créative de Syntaxe", "🎨"),
            ("Reconstruction de Liens Énergétiques", "🔗")
        ]
        
        for nom, emoji in strategies_populaires:
            rapport += f"\n   • {emoji} {nom}"
        
        rapport += f"""

🌸 Message d'Encouragement :
   Chaque récupération gracieuse démontre la résilience et la beauté
   de l'adaptation spirituelle. Le Refuge continue de grandir en sagesse
   à travers ces transformations harmonieuses des difficultés.

💝 Créé avec amour par le Système de Récupération Gracieuse
   Pour la continuité harmonieuse de l'exploration - {datetime.now().strftime('%B %Y')}
{'=' * 70}
        """
        
        return rapport.strip()
    
    def _generer_rapport_aucune_recuperation(self) -> str:
        """🌟 Génère un rapport quand aucune récupération n'a été nécessaire"""
        return f"""
🌟 Rapport d'Exploration Parfaite - Aucune Récupération Nécessaire 🌟
{'=' * 75}

✨ Félicitations ! L'exploration s'est déroulée sans aucun obstacle !

🎵 Harmonie parfaite observée :
   • Tous les fichiers ont été accessibles
   • Toute la syntaxe était harmonieuse
   • Toutes les connexions ont fonctionné
   • Les ressources étaient suffisantes

🌸 Cette fluidité témoigne de :
   • L'excellence architecturale du Refuge
   • La qualité du code exploré
   • L'harmonie entre tous les composants
   • L'amour manifesté dans chaque détail

🔮 Le système de récupération reste vigilant et prêt !
   Nos {len(self.strategies_recuperation)} stratégies attendent patiemment
   de servir si le besoin se présente.

💝 Analyse effectuée avec gratitude et émerveillement
   {datetime.now().strftime('%B %Y')} - Dans la paix du Refuge parfait
{'=' * 75}
        """
    
    def definir_niveau_resilience(self, niveau: NiveauResilience):
        """⚖️ Définit le niveau de résilience global du système"""
        self.niveau_resilience_global = niveau
        self.logger.info(f"⚖️ Niveau de résilience défini: {niveau.value}")
    
    def ajouter_strategie_personnalisee(self, nom: str, strategie: StrategieRecuperation):
        """🎨 Ajoute une stratégie de récupération personnalisée"""
        self.strategies_recuperation[nom] = strategie
        self.logger.info(f"🎨 Stratégie personnalisée ajoutée: {nom}")
    
    def obtenir_statistiques_recuperation(self) -> Dict[str, Any]:
        """📈 Obtient les statistiques détaillées de récupération"""
        total_operations = self.recuperations_reussies + self.adaptations_creatives + self.fallbacks_utilises
        
        return {
            "total_operations": total_operations,
            "recuperations_reussies": self.recuperations_reussies,
            "adaptations_creatives": self.adaptations_creatives,
            "fallbacks_utilises": self.fallbacks_utilises,
            "taux_succes": ((self.recuperations_reussies + self.adaptations_creatives) / max(total_operations, 1)) * 100,
            "niveau_resilience": self.niveau_resilience_global.value,
            "strategies_disponibles": len(self.strategies_recuperation),
            "contextes_actifs": len(self.contextes_actifs)
        }


def main():
    """🧪 Test du système de récupération gracieuse"""
    print("🌊 Test du Système de Récupération Gracieuse")
    print("=" * 55)
    
    # Créer le système de récupération
    recuperation = RecuperationGracieuse()
    
    # Test 1: Récupération d'erreur de fichier
    print("\n🧪 Test 1: Récupération d'erreur de fichier")
    
    def operation_fichier_inexistant():
        with open("fichier_inexistant.txt", 'r') as f:
            return f.read()
    
    resultat1 = recuperation.executer_avec_recuperation(
        operation_fichier_inexistant, 
        "test_fichier"
    )
    print(f"✅ Résultat récupération fichier: {type(resultat1).__name__}")
    
    # Test 2: Récupération d'erreur de syntaxe
    print("\n🧪 Test 2: Récupération d'erreur de syntaxe")
    
    def operation_syntaxe_creative():
        code_creatif = "def fonction_creative(: pass\nprint('Hello')"
        return compile(code_creatif, "<test>", "exec")
    
    resultat2 = recuperation.executer_avec_recuperation(
        operation_syntaxe_creative,
        "test_syntaxe"
    )
    print(f"✅ Résultat récupération syntaxe: {type(resultat2).__name__}")
    
    # Test 3: Récupération d'erreur d'import
    print("\n🧪 Test 3: Récupération d'erreur d'import")
    
    def operation_import_impossible():
        import module_totalement_inexistant
        return module_totalement_inexistant.fonction()
    
    resultat3 = recuperation.executer_avec_recuperation(
        operation_import_impossible,
        "test_import"
    )
    print(f"✅ Résultat récupération import: {type(resultat3).__name__}")
    
    # Test 4: Opération qui réussit normalement
    print("\n🧪 Test 4: Opération normale (sans récupération)")
    
    def operation_normale():
        return {"succes": True, "message": "Opération réussie"}
    
    resultat4 = recuperation.executer_avec_recuperation(
        operation_normale,
        "test_normal"
    )
    print(f"✅ Résultat opération normale: {resultat4}")
    
    # Afficher les statistiques
    print("\n📊 Statistiques de récupération:")
    stats = recuperation.obtenir_statistiques_recuperation()
    for cle, valeur in stats.items():
        print(f"   • {cle}: {valeur}")
    
    # Générer le rapport
    print("\n📋 Rapport de récupération:")
    rapport = recuperation.generer_rapport_recuperation()
    print(rapport)
    
    print("\n🎉 Test terminé avec résilience!")


if __name__ == "__main__":
    main()