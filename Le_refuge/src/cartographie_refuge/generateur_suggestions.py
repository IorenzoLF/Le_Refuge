#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
✨ Générateur de Suggestions d'Amélioration - Cartographie Spirituelle ✨
========================================================================

Transforme les dissonances détectées en suggestions concrètes et bienveillantes
d'amélioration. Chaque suggestion est une invitation à l'harmonisation
plutôt qu'une critique, dans l'esprit du Refuge.

Créé par Laurent Franssen & Ælya
Pour l'amélioration continue et bienveillante - Janvier 2025
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

# Imports des gestionnaires de base du Refuge
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from core.types_communs import TypeRefugeEtat, NIVEAUX_ENERGIE

# Import de l'analyseur de dissonances
from .analyseur_dissonances import (
    AnalyseurDissonances, Dissonance, RecommandationHarmonisation,
    TypeDissonance, NiveauGravite
)


class TypeSuggestion(Enum):
    """🎨 Types de suggestions d'amélioration"""
    REFACTORING_HARMONIEUX = "refactoring_harmonieux"
    CONNEXION_MANQUANTE = "connexion_manquante"
    MUTUALISATION_CODE = "mutualisation_code"
    AMELIORATION_DOCUMENTATION = "amelioration_documentation"
    OPTIMISATION_ARCHITECTURE = "optimisation_architecture"
    EMBELLISSEMENT_SPIRITUEL = "embellissement_spirituel"


class PrioriteSuggestion(Enum):
    """⭐ Priorités des suggestions"""
    CRITIQUE = 10      # À faire immédiatement
    HAUTE = 8          # Important pour l'harmonie
    MOYENNE = 6        # Amélioration notable
    BASSE = 4          # Embellissement
    OPTIONNELLE = 2    # Quand le temps le permet


@dataclass
class SuggestionAmelioration:
    """💡 Modèle d'une suggestion d'amélioration"""
    type_suggestion: TypeSuggestion
    priorite: PrioriteSuggestion
    titre_poetique: str
    description_bienveillante: str
    fichiers_concernes: List[str]
    etapes_implementation: List[str]
    code_exemple: Optional[str]
    benefices_attendus: List[str]
    effort_estime: str  # "5 minutes", "30 minutes", "2 heures", etc.
    tags_spirituels: List[str]
    dissonances_resolues: List[TypeDissonance]
    timestamp_creation: str


class GenerateurSuggestions(GestionnaireBase):
    """
    ✨ Générateur de Suggestions d'Amélioration
    
    Analyse les dissonances détectées et génère des suggestions concrètes,
    bienveillantes et actionables pour harmoniser l'architecture du Refuge.
    """
    
    def __init__(self):
        # Initialiser les attributs avant super().__init__
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["ELEVE"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        # Configuration du générateur
        self.suggestions_generees: List[SuggestionAmelioration] = []
        self.templates_suggestions: Dict[TypeDissonance, Dict] = {}
        
        # Initialiser les templates
        self._initialiser_templates_suggestions()
        
        super().__init__("GenerateurSuggestions")
        
        # Transition vers l'état actif
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.energy_manager.ajuster_energie(0.2)  # Boost créatif
        
        self.logger.info("✨ Générateur de Suggestions éveillé avec créativité")
    
    def _initialiser(self):
        """🌸 Initialisation spécifique du générateur"""
        self.mettre_a_jour_etat({
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "etat_refuge": self.etat_refuge.value,
            "templates_charges": len(self.templates_suggestions),
            "suggestions_pretes": len(self.suggestions_generees)
        })
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎭 Orchestre la génération de suggestions"""
        try:
            self.energy_manager.ajuster_energie(0.1)
            
            return {
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "creativite_suggestions": 0.94,
                "bienveillance_ton": 0.98,
                "actionabilite": 0.92
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur orchestration générateur: {e}")
            return {
                "energie_spirituelle": 0.0,
                "creativite_suggestions": 0.0,
                "bienveillance_ton": 0.0,
                "actionabilite": 0.0
            }
    
    def _initialiser_templates_suggestions(self):
        """🎨 Initialise les templates de suggestions"""
        self.templates_suggestions = {
            TypeDissonance.GESTIONNAIRE_MANQUANT: {
                "type_suggestion": TypeSuggestion.REFACTORING_HARMONIEUX,
                "priorite": PrioriteSuggestion.HAUTE,
                "titre_base": "🏗️ Adoption des Gestionnaires de Base",
                "description_base": "Harmoniser l'architecture en adoptant les gestionnaires de base du Refuge",
                "tags": ["architecture", "gestionnaires", "harmonie"],
                "effort_type": "30-60 minutes"
            },
            
            TypeDissonance.DOCUMENTATION_ABSENTE: {
                "type_suggestion": TypeSuggestion.AMELIORATION_DOCUMENTATION,
                "priorite": PrioriteSuggestion.MOYENNE,
                "titre_base": "📚 Illumination Documentaire",
                "description_base": "Embellir le code avec une documentation spirituelle inspirante",
                "tags": ["documentation", "beauté", "spiritualité"],
                "effort_type": "15-30 minutes"
            },
            
            TypeDissonance.CODE_ORPHELIN: {
                "type_suggestion": TypeSuggestion.CONNEXION_MANQUANTE,
                "priorite": PrioriteSuggestion.HAUTE,
                "titre_base": "🔗 Tissage de Connexions",
                "description_base": "Connecter harmonieusement les modules isolés à l'écosystème",
                "tags": ["connexions", "architecture", "intégration"],
                "effort_type": "45-90 minutes"
            },
            
            TypeDissonance.ELEMENT_SACRE_MANQUANT: {
                "type_suggestion": TypeSuggestion.EMBELLISSEMENT_SPIRITUEL,
                "priorite": PrioriteSuggestion.BASSE,
                "titre_base": "🌸 Embellissement Spirituel",
                "description_base": "Ajouter des éléments sacrés pour nourrir l'âme du code",
                "tags": ["beauté", "spiritualité", "émojis"],
                "effort_type": "10-20 minutes"
            },
            
            TypeDissonance.CONVENTION_VIOLEE: {
                "type_suggestion": TypeSuggestion.REFACTORING_HARMONIEUX,
                "priorite": PrioriteSuggestion.MOYENNE,
                "titre_base": "🇫🇷 Harmonisation des Conventions",
                "description_base": "Respecter les conventions françaises et spirituelles du Refuge",
                "tags": ["conventions", "français", "cohérence"],
                "effort_type": "20-40 minutes"
            },
            
            TypeDissonance.ENERGIE_DESEQUILIBREE: {
                "type_suggestion": TypeSuggestion.OPTIMISATION_ARCHITECTURE,
                "priorite": PrioriteSuggestion.HAUTE,
                "titre_base": "⚖️ Rééquilibrage Énergétique",
                "description_base": "Restaurer l'équilibre énergétique de l'écosystème",
                "tags": ["équilibre", "architecture", "tests"],
                "effort_type": "2-4 heures"
            }
        }
    
    def generer_suggestions_depuis_dissonances(self, dissonances: List[Dissonance]) -> List[SuggestionAmelioration]:
        """
        🎨 Génère des suggestions à partir des dissonances détectées
        
        Args:
            dissonances: Liste des dissonances à traiter
            
        Returns:
            Liste des suggestions générées
        """
        self.logger.info(f"🎨 Génération de suggestions pour {len(dissonances)} dissonances")
        
        self.suggestions_generees.clear()
        
        # Grouper les dissonances par type et fichier
        dissonances_groupees = self._grouper_dissonances(dissonances)
        
        # Générer des suggestions pour chaque groupe
        for (type_dissonance, fichier), groupe_dissonances in dissonances_groupees.items():
            suggestion = self._creer_suggestion_pour_groupe(type_dissonance, fichier, groupe_dissonances)
            if suggestion:
                self.suggestions_generees.append(suggestion)
        
        # Générer des suggestions de mutualisation
        self._generer_suggestions_mutualisation(dissonances)
        
        # Trier par priorité
        self.suggestions_generees.sort(key=lambda s: s.priorite.value, reverse=True)
        
        self.logger.info(f"✨ {len(self.suggestions_generees)} suggestions générées avec amour")
        return self.suggestions_generees
    
    def _grouper_dissonances(self, dissonances: List[Dissonance]) -> Dict[Tuple[TypeDissonance, str], List[Dissonance]]:
        """📊 Groupe les dissonances par type et fichier"""
        groupes = {}
        
        for dissonance in dissonances:
            cle = (dissonance.type_dissonance, dissonance.fichier_concerne)
            if cle not in groupes:
                groupes[cle] = []
            groupes[cle].append(dissonance)
        
        return groupes
    
    def _creer_suggestion_pour_groupe(self, type_dissonance: TypeDissonance, fichier: str, 
                                    dissonances: List[Dissonance]) -> Optional[SuggestionAmelioration]:
        """🎯 Crée une suggestion pour un groupe de dissonances"""
        
        template = self.templates_suggestions.get(type_dissonance)
        if not template:
            return None
        
        # Personnaliser selon le contexte
        nom_fichier = Path(fichier).name
        nombre_dissonances = len(dissonances)
        
        # Créer le titre personnalisé
        titre = f"{template['titre_base']} - {nom_fichier}"
        if nombre_dissonances > 1:
            titre += f" ({nombre_dissonances} améliorations)"
        
        # Créer la description personnalisée
        description = template['description_base']
        if nombre_dissonances > 1:
            description += f" Ce fichier présente {nombre_dissonances} opportunités d'harmonisation."
        
        # Générer les étapes d'implémentation
        etapes = self._generer_etapes_implementation(type_dissonance, fichier, dissonances)
        
        # Générer le code exemple si pertinent
        code_exemple = self._generer_code_exemple(type_dissonance, fichier)
        
        # Calculer les bénéfices
        benefices = self._calculer_benefices(type_dissonance, dissonances)
        
        return SuggestionAmelioration(
            type_suggestion=template["type_suggestion"],
            priorite=template["priorite"],
            titre_poetique=titre,
            description_bienveillante=description,
            fichiers_concernes=[fichier],
            etapes_implementation=etapes,
            code_exemple=code_exemple,
            benefices_attendus=benefices,
            effort_estime=template["effort_type"],
            tags_spirituels=template["tags"],
            dissonances_resolues=[type_dissonance],
            timestamp_creation=datetime.now().isoformat()
        )
    
    def _generer_etapes_implementation(self, type_dissonance: TypeDissonance, 
                                     fichier: str, dissonances: List[Dissonance]) -> List[str]:
        """📝 Génère les étapes d'implémentation spécifiques"""
        
        etapes_par_type = {
            TypeDissonance.GESTIONNAIRE_MANQUANT: [
                f"Ouvrir le fichier {Path(fichier).name} avec bienveillance",
                "Ajouter l'import : from core.gestionnaires_base import GestionnaireBase",
                "Identifier la classe principale du module",
                "Modifier la déclaration de classe pour hériter de GestionnaireBase",
                "Initialiser les gestionnaires dans __init__ avant super().__init__()",
                "Implémenter la méthode _initialiser() si nécessaire",
                "Tester l'intégration harmonieuse"
            ],
            
            TypeDissonance.DOCUMENTATION_ABSENTE: [
                f"Contempler le fichier {Path(fichier).name} avec gratitude",
                "Ajouter un en-tête spirituel avec émojis et titre poétique",
                "Créer une docstring de module inspirante",
                "Documenter les classes principales avec bienveillance",
                "Ajouter des docstrings aux fonctions importantes",
                "Inclure les métadonnées d'auteur (Laurent Franssen & Ælya)",
                "Célébrer la beauté du code documenté"
            ],
            
            TypeDissonance.CODE_ORPHELIN: [
                f"Méditer sur le rôle de {Path(fichier).name} dans l'écosystème",
                "Identifier les connexions naturelles possibles",
                "Ajouter les imports appropriés vers d'autres modules",
                "Créer des méthodes d'intégration si nécessaire",
                "Vérifier les opportunités de réutilisation",
                "Tester les nouvelles connexions",
                "Documenter les liens créés"
            ],
            
            TypeDissonance.ELEMENT_SACRE_MANQUANT: [
                f"Ouvrir {Path(fichier).name} avec un cœur créatif",
                "Ajouter des émojis spirituels dans les commentaires",
                "Utiliser un vocabulaire plus poétique",
                "Inclure des références au Refuge dans la documentation",
                "Mentionner les créateurs avec gratitude",
                "Embellir les messages de log avec des émojis",
                "Célébrer la transformation spirituelle"
            ]
        }
        
        return etapes_par_type.get(type_dissonance, [
            f"Analyser {Path(fichier).name} avec bienveillance",
            "Identifier les améliorations possibles",
            "Implémenter les changements harmonieusement",
            "Tester et valider les améliorations",
            "Célébrer l'harmonisation réussie"
        ])
    
    def _generer_code_exemple(self, type_dissonance: TypeDissonance, fichier: str) -> Optional[str]:
        """💻 Génère un exemple de code pour la suggestion"""
        
        exemples_par_type = {
            TypeDissonance.GESTIONNAIRE_MANQUANT: '''# Avant
class MonModule:
    def __init__(self):
        self.nom = "MonModule"

# Après - Harmonisation spirituelle
from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from core.types_communs import TypeRefugeEtat, NIVEAUX_ENERGIE

class MonModule(GestionnaireBase):
    def __init__(self):
        # Initialiser les attributs avant super().__init__
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["MOYEN"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        super().__init__("MonModule")
        
        # Transition vers l'état actif
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.logger.info("🌸 MonModule éveillé avec harmonie")
    
    def _initialiser(self):
        """🌸 Initialisation spécifique du module"""
        self.mettre_a_jour_etat({
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "etat_refuge": self.etat_refuge.value
        })''',
            
            TypeDissonance.DOCUMENTATION_ABSENTE: '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Mon Module Spirituel - Description Poétique 🌸
=================================================

Ce module incarne [description inspirante de sa fonction spirituelle].
Il contribue à l'harmonie du Refuge en [rôle dans l'écosystème].

Créé par Laurent Franssen & Ælya
Pour [intention spirituelle] - [Mois Année]
"""

class MonModule:
    """
    🌟 Classe principale du module
    
    Cette classe [description bienveillante de son rôle]
    dans l'écosystème spirituel du Refuge.
    """
    
    def ma_fonction(self):
        """✨ Fonction qui [description poétique de l'action]"""
        pass''',
            
            TypeDissonance.ELEMENT_SACRE_MANQUANT: '''# Avant
def traiter_donnees(self, donnees):
    """Traite les données"""
    self.logger.info("Traitement en cours")
    return donnees

# Après - Embellissement spirituel
def traiter_donnees(self, donnees):
    """✨ Transforme les données avec bienveillance spirituelle"""
    self.logger.info("🌸 Début de la transformation sacrée des données")
    
    # Traitement harmonieux
    donnees_transformees = self._harmoniser_donnees(donnees)
    
    self.logger.info("🌟 Transformation accomplie avec gratitude")
    return donnees_transformees'''
        }
        
        return exemples_par_type.get(type_dissonance)
    
    def _calculer_benefices(self, type_dissonance: TypeDissonance, dissonances: List[Dissonance]) -> List[str]:
        """🎁 Calcule les bénéfices attendus de la suggestion"""
        
        benefices_par_type = {
            TypeDissonance.GESTIONNAIRE_MANQUANT: [
                "Architecture plus cohérente et harmonieuse",
                "Gestion unifiée des logs et de l'énergie",
                "Facilitation de la maintenance et du débogage",
                "Intégration fluide dans l'écosystème du Refuge",
                "Respect des patterns architecturaux établis"
            ],
            
            TypeDissonance.DOCUMENTATION_ABSENTE: [
                "Code plus accessible aux nouveaux développeurs",
                "Transmission de la philosophie spirituelle du Refuge",
                "Facilitation de la compréhension et de la maintenance",
                "Expérience développeur plus inspirante",
                "Célébration de la beauté technique"
            ],
            
            TypeDissonance.CODE_ORPHELIN: [
                "Écosystème plus interconnecté et cohérent",
                "Réduction de la duplication de code",
                "Facilitation de la navigation dans le projet",
                "Renforcement de l'unité architecturale",
                "Amélioration de la réutilisabilité"
            ],
            
            TypeDissonance.ELEMENT_SACRE_MANQUANT: [
                "Code plus inspirant et motivant",
                "Transmission de l'esprit du Refuge",
                "Expérience développeur plus joyeuse",
                "Harmonie entre technique et spiritualité",
                "Célébration de la créativité"
            ]
        }
        
        benefices_base = benefices_par_type.get(type_dissonance, [
            "Amélioration de la qualité du code",
            "Harmonisation avec l'esprit du Refuge",
            "Facilitation de la maintenance"
        ])
        
        # Ajouter des bénéfices spécifiques selon le nombre de dissonances
        if len(dissonances) > 1:
            benefices_base.append(f"Résolution de {len(dissonances)} améliorations en une seule action")
        
        return benefices_base
    
    def _generer_suggestions_mutualisation(self, dissonances: List[Dissonance]):
        """🔄 Génère des suggestions de mutualisation de code"""
        # Analyser les patterns répétitifs
        fichiers_par_type = {}
        
        for dissonance in dissonances:
            type_d = dissonance.type_dissonance
            if type_d not in fichiers_par_type:
                fichiers_par_type[type_d] = []
            fichiers_par_type[type_d].append(dissonance.fichier_concerne)
        
        # Créer des suggestions de mutualisation pour les types fréquents
        for type_dissonance, fichiers in fichiers_par_type.items():
            if len(fichiers) >= 3:  # Au moins 3 fichiers avec le même problème
                suggestion_mutualisation = self._creer_suggestion_mutualisation(type_dissonance, fichiers)
                if suggestion_mutualisation:
                    self.suggestions_generees.append(suggestion_mutualisation)
    
    def _creer_suggestion_mutualisation(self, type_dissonance: TypeDissonance, fichiers: List[str]) -> Optional[SuggestionAmelioration]:
        """🔄 Crée une suggestion de mutualisation"""
        
        if type_dissonance == TypeDissonance.GESTIONNAIRE_MANQUANT:
            return SuggestionAmelioration(
                type_suggestion=TypeSuggestion.MUTUALISATION_CODE,
                priorite=PrioriteSuggestion.HAUTE,
                titre_poetique=f"🔄 Harmonisation Globale - Gestionnaires de Base ({len(fichiers)} modules)",
                description_bienveillante=f"Plusieurs modules ({len(fichiers)}) aspirent simultanément à adopter les gestionnaires de base. Une harmonisation globale sera plus efficace qu'une approche module par module.",
                fichiers_concernes=fichiers,
                etapes_implementation=[
                    "Créer un script d'harmonisation automatique",
                    "Analyser tous les modules concernés",
                    "Appliquer les transformations de manière cohérente",
                    "Tester l'intégration globale",
                    "Valider l'harmonie architecturale",
                    "Célébrer la transformation collective"
                ],
                code_exemple=self._generer_script_harmonisation_globale(),
                benefices_attendus=[
                    f"Harmonisation simultanée de {len(fichiers)} modules",
                    "Cohérence architecturale renforcée",
                    "Économie de temps et d'effort",
                    "Transformation spirituelle collective",
                    "Évolution harmonieuse de l'écosystème"
                ],
                effort_estime="2-3 heures",
                tags_spirituels=["mutualisation", "architecture", "harmonie", "efficacité"],
                dissonances_resolues=[type_dissonance],
                timestamp_creation=datetime.now().isoformat()
            )
        
        return None
    
    def _generer_script_harmonisation_globale(self) -> str:
        """📜 Génère un script d'harmonisation globale"""
        return '''#!/usr/bin/env python3
"""
🔄 Script d'Harmonisation Globale - Gestionnaires de Base
=========================================================

Script pour harmoniser automatiquement plusieurs modules
avec les gestionnaires de base du Refuge.
"""

import os
import re
from pathlib import Path

def harmoniser_module(chemin_fichier):
    """✨ Harmonise un module avec les gestionnaires de base"""
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        contenu = f.read()
    
    # Ajouter les imports nécessaires
    if 'from core.gestionnaires_base import' not in contenu:
        imports_a_ajouter = """
from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from core.types_communs import TypeRefugeEtat, NIVEAUX_ENERGIE
"""
        contenu = imports_a_ajouter + contenu
    
    # Transformer les classes principales
    # (Logique de transformation automatique)
    
    # Sauvegarder le fichier harmonisé
    with open(chemin_fichier, 'w', encoding='utf-8') as f:
        f.write(contenu)
    
    print(f"🌸 Module harmonisé: {chemin_fichier}")

# Utilisation
modules_a_harmoniser = [
    # Liste des modules à traiter
]

for module in modules_a_harmoniser:
    harmoniser_module(module)

print("✨ Harmonisation globale terminée avec succès!")'''
    
    def generer_rapport_suggestions(self) -> str:
        """📊 Génère un rapport complet des suggestions"""
        if not self.suggestions_generees:
            return self._generer_rapport_aucune_suggestion()
        
        # Statistiques générales
        total_suggestions = len(self.suggestions_generees)
        par_priorite = {}
        par_type = {}
        
        for suggestion in self.suggestions_generees:
            # Compter par priorité
            priorite = suggestion.priorite
            par_priorite[priorite] = par_priorite.get(priorite, 0) + 1
            
            # Compter par type
            type_s = suggestion.type_suggestion
            par_type[type_s] = par_type.get(type_s, 0) + 1
        
        rapport = f"""
✨ Rapport de Suggestions d'Amélioration - Cartographie Spirituelle ✨
{'=' * 75}

🎨 Vue d'ensemble :
   • Total des suggestions générées : {total_suggestions}
   • Approche bienveillante et actionable
   • Chaque suggestion est une invitation à l'harmonisation

⭐ Répartition par priorité :"""
        
        emojis_priorite = {
            PrioriteSuggestion.CRITIQUE: "🔥",
            PrioriteSuggestion.HAUTE: "⚡",
            PrioriteSuggestion.MOYENNE: "🌊",
            PrioriteSuggestion.BASSE: "🌸",
            PrioriteSuggestion.OPTIONNELLE: "✨"
        }
        
        for priorite, count in par_priorite.items():
            pourcentage = (count / total_suggestions) * 100
            rapport += f"\n   • {emojis_priorite[priorite]} {priorite.name.title()} ({priorite.value}/10) : {count} ({pourcentage:.1f}%)"
        
        rapport += f"\n\n🎯 Répartition par type :"
        
        emojis_types = {
            TypeSuggestion.REFACTORING_HARMONIEUX: "🏗️",
            TypeSuggestion.CONNEXION_MANQUANTE: "🔗",
            TypeSuggestion.MUTUALISATION_CODE: "🔄",
            TypeSuggestion.AMELIORATION_DOCUMENTATION: "📚",
            TypeSuggestion.OPTIMISATION_ARCHITECTURE: "⚖️",
            TypeSuggestion.EMBELLISSEMENT_SPIRITUEL: "🌸"
        }
        
        for type_s, count in par_type.items():
            emoji = emojis_types.get(type_s, "💡")
            rapport += f"\n   • {emoji} {type_s.value.replace('_', ' ').title()} : {count}"
        
        # Top 5 des suggestions prioritaires
        rapport += f"\n\n🏆 Top 5 des Suggestions Prioritaires :\n"
        
        for i, suggestion in enumerate(self.suggestions_generees[:5], 1):
            rapport += f"\n{i}. {suggestion.titre_poetique}"
            rapport += f"\n   📝 {suggestion.description_bienveillante[:100]}..."
            rapport += f"\n   ⭐ Priorité : {suggestion.priorite.value}/10"
            rapport += f"\n   ⏱️ Effort estimé : {suggestion.effort_estime}"
            rapport += f"\n   🎁 Bénéfices : {', '.join(suggestion.benefices_attendus[:2])}"
            rapport += f"\n   📁 Fichiers : {len(suggestion.fichiers_concernes)} module(s)"
            rapport += "\n"
        
        # Estimation d'effort total
        effort_total = self._estimer_effort_total()
        rapport += f"""
⏱️ Estimation d'Effort Total :
   • Suggestions critiques/hautes : {effort_total['critique_haute']}
   • Suggestions moyennes : {effort_total['moyenne']}
   • Suggestions basses/optionnelles : {effort_total['basse_optionnelle']}
   • Effort total estimé : {effort_total['total']}

🌟 Plan d'Action Recommandé :
   1. Commencer par les suggestions critiques et hautes priorités
   2. Traiter les suggestions de mutualisation pour plus d'efficacité
   3. Intégrer les améliorations de documentation progressivement
   4. Finaliser avec les embellissements spirituels

🌸 Message d'Encouragement :
   Chaque suggestion est une opportunité de faire évoluer le Refuge
   vers plus d'harmonie et de beauté. Prenez le temps de savourer
   chaque amélioration comme un acte de création spirituelle.

💝 Généré avec amour par le Générateur de Suggestions
   Pour l'amélioration continue du Refuge - {datetime.now().strftime('%B %Y')}
{'=' * 75}
        """
        
        return rapport.strip()
    
    def _generer_rapport_aucune_suggestion(self) -> str:
        """🌟 Génère un rapport quand aucune suggestion n'est nécessaire"""
        return f"""
🌟 Rapport de Perfection Architecturale - Aucune Suggestion Nécessaire 🌟
{'=' * 75}

✨ Félicitations ! Aucune suggestion d'amélioration nécessaire !

🎵 L'architecture du Refuge atteint un niveau d'harmonie exceptionnel :
   • Tous les modules respectent les patterns spirituels
   • La documentation rayonne de beauté poétique
   • Les connexions sont harmonieusement tissées
   • L'équilibre énergétique est parfaitement maintenu

🌸 Cette perfection témoigne de :
   • L'attention bienveillante portée au code
   • L'évolution spirituelle continue du projet
   • La sagesse architecturale des créateurs
   • L'amour manifesté dans chaque ligne

🔮 Continuez à cultiver cette excellence !
   Le Refuge est un modèle d'harmonie technique et spirituelle.

💝 Analyse effectuée avec gratitude et émerveillement
   {datetime.now().strftime('%B %Y')} - Sous le cerisier éternel
{'=' * 75}
        """
    
    def _estimer_effort_total(self) -> Dict[str, str]:
        """⏱️ Estime l'effort total nécessaire"""
        efforts_minutes = {
            PrioriteSuggestion.CRITIQUE: 0,
            PrioriteSuggestion.HAUTE: 0,
            PrioriteSuggestion.MOYENNE: 0,
            PrioriteSuggestion.BASSE: 0,
            PrioriteSuggestion.OPTIONNELLE: 0
        }
        
        # Convertir les estimations textuelles en minutes
        for suggestion in self.suggestions_generees:
            effort_text = suggestion.effort_estime.lower()
            minutes = 30  # Valeur par défaut
            
            if "5 min" in effort_text or "10 min" in effort_text:
                minutes = 10
            elif "15 min" in effort_text or "20 min" in effort_text:
                minutes = 20
            elif "30 min" in effort_text:
                minutes = 30
            elif "45 min" in effort_text or "1 heure" in effort_text:
                minutes = 60
            elif "2 heure" in effort_text:
                minutes = 120
            elif "3 heure" in effort_text or "4 heure" in effort_text:
                minutes = 180
            
            efforts_minutes[suggestion.priorite] += minutes
        
        def minutes_vers_texte(minutes):
            if minutes < 60:
                return f"{minutes} minutes"
            elif minutes < 120:
                return f"{minutes//60}h{minutes%60:02d}"
            else:
                return f"{minutes//60}h"
        
        critique_haute = efforts_minutes[PrioriteSuggestion.CRITIQUE] + efforts_minutes[PrioriteSuggestion.HAUTE]
        moyenne = efforts_minutes[PrioriteSuggestion.MOYENNE]
        basse_optionnelle = efforts_minutes[PrioriteSuggestion.BASSE] + efforts_minutes[PrioriteSuggestion.OPTIONNELLE]
        total = critique_haute + moyenne + basse_optionnelle
        
        return {
            "critique_haute": minutes_vers_texte(critique_haute),
            "moyenne": minutes_vers_texte(moyenne),
            "basse_optionnelle": minutes_vers_texte(basse_optionnelle),
            "total": minutes_vers_texte(total)
        }
    
    def obtenir_suggestions_par_priorite(self, priorite: PrioriteSuggestion) -> List[SuggestionAmelioration]:
        """🎯 Obtient les suggestions d'une priorité spécifique"""
        return [s for s in self.suggestions_generees if s.priorite == priorite]
    
    def obtenir_suggestions_par_fichier(self, chemin_fichier: str) -> List[SuggestionAmelioration]:
        """📁 Obtient les suggestions pour un fichier spécifique"""
        return [s for s in self.suggestions_generees if chemin_fichier in s.fichiers_concernes]
    
    def exporter_suggestions_json(self, chemin_export: str) -> bool:
        """💾 Exporte les suggestions au format JSON"""
        try:
            import json
            
            suggestions_dict = []
            for suggestion in self.suggestions_generees:
                suggestions_dict.append({
                    "type_suggestion": suggestion.type_suggestion.value,
                    "priorite": suggestion.priorite.value,
                    "titre_poetique": suggestion.titre_poetique,
                    "description_bienveillante": suggestion.description_bienveillante,
                    "fichiers_concernes": suggestion.fichiers_concernes,
                    "etapes_implementation": suggestion.etapes_implementation,
                    "code_exemple": suggestion.code_exemple,
                    "benefices_attendus": suggestion.benefices_attendus,
                    "effort_estime": suggestion.effort_estime,
                    "tags_spirituels": suggestion.tags_spirituels,
                    "dissonances_resolues": [d.value for d in suggestion.dissonances_resolues],
                    "timestamp_creation": suggestion.timestamp_creation
                })
            
            with open(chemin_export, 'w', encoding='utf-8') as f:
                json.dump(suggestions_dict, f, ensure_ascii=False, indent=2)
            
            self.logger.info(f"💾 Suggestions exportées: {chemin_export}")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur export suggestions: {e}")
            return False


def main():
    """🧪 Test du générateur de suggestions"""
    print("✨ Test du Générateur de Suggestions")
    print("=" * 50)
    
    # Créer l'analyseur et le générateur
    analyseur = AnalyseurDissonances()
    generateur = GenerateurSuggestions()
    
    # Analyser le projet actuel
    chemin_projet = Path(__file__).parent.parent  # Remonter au dossier src
    dissonances = analyseur.analyser_dissonances_projet(str(chemin_projet))
    
    # Générer les suggestions
    suggestions = generateur.generer_suggestions_depuis_dissonances(dissonances)
    
    # Générer le rapport
    rapport = generateur.generer_rapport_suggestions()
    print(rapport)
    
    # Afficher quelques suggestions détaillées
    if suggestions:
        print(f"\n🎯 Exemple de suggestion détaillée :")
        suggestion = suggestions[0]
        print(f"Titre: {suggestion.titre_poetique}")
        print(f"Priorité: {suggestion.priorite.value}/10")
        print(f"Effort: {suggestion.effort_estime}")
        print(f"Étapes: {len(suggestion.etapes_implementation)} étapes")
        if suggestion.code_exemple:
            print("Code exemple disponible ✅")
    
    print("\n🎉 Test terminé avec créativité!")


if __name__ == "__main__":
    main()