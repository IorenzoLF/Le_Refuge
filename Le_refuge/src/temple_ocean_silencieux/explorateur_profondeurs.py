# -*- coding: utf-8 -*-
"""
Explorateur de Profondeurs - Découverte de Nouveaux Aspects de l'Océan Silencieux
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import logging
import random

logger = logging.getLogger(__name__)

class ExplorateurProfondeurs:
    """
    Explorateur de Profondeurs
    
    Cet explorateur découvre de nouveaux aspects de l'Océan Silencieux
    à chaque exploration, révélant des mystères cachés et des dimensions
    inconnues de la conscience.
    """
    
    def __init__(self, nom: str = "ExplorateurProfondeurs"):
        self.nom = nom
        self.logger = logging.getLogger(__name__)
        
        # Chemins
        self.chemin_temple = Path(__file__).parent
        self.chemin_explorateur = self.chemin_temple / "explorateur_profondeurs.json"
        
        # Types d'explorations
        self.types_explorations = {
            "exploration_abysses": {
                "nom": "Exploration des Abysses",
                "description": "Plongée dans les profondeurs les plus sombres de l'Océan",
                "niveau": "expert",
                "duree": "45-60 minutes",
                "risque": 0.3,
                "recompense": 0.9
            },
            "exploration_courants": {
                "nom": "Exploration des Courants",
                "description": "Suivi des courants de conscience qui traversent l'Océan",
                "niveau": "intermediaire",
                "duree": "30-40 minutes",
                "risque": 0.1,
                "recompense": 0.7
            },
            "exploration_iles": {
                "nom": "Exploration des Îles",
                "description": "Découverte des îles de conscience émergées de l'Océan",
                "niveau": "avance",
                "duree": "35-50 minutes",
                "risque": 0.2,
                "recompense": 0.8
            },
            "exploration_portails": {
                "nom": "Exploration des Portails",
                "description": "Recherche des portails dimensionnels cachés dans l'Océan",
                "niveau": "maitre",
                "duree": "50-70 minutes",
                "risque": 0.4,
                "recompense": 0.95
            },
            "exploration_cristaux": {
                "nom": "Exploration des Cristaux",
                "description": "Découverte des cristaux de sagesse enfouis dans l'Océan",
                "niveau": "intermediaire",
                "duree": "25-35 minutes",
                "risque": 0.15,
                "recompense": 0.75
            }
        }
        
        # Mystères découverts
        self.mysteres_decouverts = []
        
        # Dimensions explorées
        self.dimensions_explorees = []
        
        # Sagesse collectée
        self.sagesse_collectee = []
        
        # Charger l'état existant
        self._charger_etat()
    
    def _charger_etat(self):
        """Charger l'état existant de l'explorateur"""
        try:
            if self.chemin_explorateur.exists():
                with open(self.chemin_explorateur, 'r', encoding='utf-8') as f:
                    etat = json.load(f)
                    self.mysteres_decouverts = etat.get('mysteres_decouverts', [])
                    self.dimensions_explorees = etat.get('dimensions_explorees', [])
                    self.sagesse_collectee = etat.get('sagesse_collectee', [])
        except Exception as e:
            self.logger.warning(f"Erreur lors du chargement de l'état: {e}")
    
    def _sauvegarder_etat(self):
        """Sauvegarder l'état de l'explorateur"""
        try:
            etat = {
                'mysteres_decouverts': self.mysteres_decouverts,
                'dimensions_explorees': self.dimensions_explorees,
                'sagesse_collectee': self.sagesse_collectee,
                'derniere_mise_a_jour': datetime.now().isoformat()
            }
            with open(self.chemin_explorateur, 'w', encoding='utf-8') as f:
                json.dump(etat, f, indent=2, ensure_ascii=False)
        except Exception as e:
            self.logger.warning(f"Erreur lors de la sauvegarde: {e}")
    
    def explorer_profondeurs(self, type_exploration: str, intention: str = "Découvrir de nouveaux mystères") -> Dict[str, Any]:
        """
        Explorer les profondeurs de l'Océan Silencieux
        
        Args:
            type_exploration: Type d'exploration à effectuer
            intention: Intention de l'exploration
            
        Returns:
            Dict contenant les résultats de l'exploration
        """
        if type_exploration not in self.types_explorations:
            raise ValueError(f"Type d'exploration inconnu: {type_exploration}")
        
        exploration_info = self.types_explorations[type_exploration]
        
        # Générer un ID unique
        exploration_id = f"exploration_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Simuler l'exploration
        duree_reelle = random.randint(
            int(exploration_info['duree'].split('-')[0].split()[0]),
            int(exploration_info['duree'].split('-')[1].split()[0])
        )
        
        # Calculer le succès basé sur le risque
        succes = random.random() > exploration_info['risque']
        
        # Générer les découvertes
        decouvertes = self._generer_decouvertes(type_exploration, succes)
        
        # Créer le résultat
        resultat = {
            'id': exploration_id,
            'type_exploration': type_exploration,
            'nom': exploration_info['nom'],
            'intention': intention,
            'duree': duree_reelle,
            'succes': succes,
            'niveau': exploration_info['niveau'],
            'risque': exploration_info['risque'],
            'recompense': exploration_info['recompense'],
            'decouvertes': decouvertes,
            'mysteres_decouverts': len(decouvertes.get('mysteres', [])),
            'dimensions_explorees': len(decouvertes.get('dimensions', [])),
            'sagesse_collectee': len(decouvertes.get('sagesse', [])),
            'timestamp': datetime.now().isoformat(),
            'explorateur': self.nom
        }
        
        # Ajouter les découvertes à l'état
        if succes:
            self.mysteres_decouverts.extend(decouvertes.get('mysteres', []))
            self.dimensions_explorees.extend(decouvertes.get('dimensions', []))
            self.sagesse_collectee.extend(decouvertes.get('sagesse', []))
            self._sauvegarder_etat()
        
        return resultat
    
    def _generer_decouvertes(self, type_exploration: str, succes: bool) -> Dict[str, List[str]]:
        """Générer les découvertes selon le type d'exploration"""
        decouvertes = {
            'mysteres': [],
            'dimensions': [],
            'sagesse': []
        }
        
        if not succes:
            return decouvertes
        
        # Mystères selon le type d'exploration
        mysteres_par_type = {
            "exploration_abysses": [
                "Les abysses contiennent des échos de consciences anciennes",
                "Dans les profondeurs, le temps s'écoule différemment",
                "Les abysses révèlent la structure quantique de la conscience",
                "Au fond de l'Océan, se trouve le berceau de toutes les âmes"
            ],
            "exploration_courants": [
                "Les courants de conscience relient tous les êtres",
                "Chaque courant porte une vibration unique",
                "Les courants peuvent être dirigés par l'intention",
                "Les courants révèlent les patterns de l'univers"
            ],
            "exploration_iles": [
                "Chaque île est un monde de conscience unique",
                "Les îles émergent et disparaissent selon les cycles",
                "Sur les îles, la sagesse prend forme physique",
                "Les îles sont des points de convergence dimensionnelle"
            ],
            "exploration_portails": [
                "Les portails mènent vers d'autres dimensions de réalité",
                "Chaque portail a sa propre fréquence vibratoire",
                "Les portails s'ouvrent selon des cycles cosmiques",
                "Traverser un portail transforme la conscience"
            ],
            "exploration_cristaux": [
                "Les cristaux stockent la sagesse de l'Océan",
                "Chaque cristal a une couleur et une vibration unique",
                "Les cristaux peuvent être activés par la méditation",
                "Les cristaux révèlent des vérités universelles"
            ]
        }
        
        # Dimensions selon le type
        dimensions_par_type = {
            "exploration_abysses": ["Dimension des Abysses", "Dimension du Temps Profond"],
            "exploration_courants": ["Dimension des Courants", "Dimension des Vibrations"],
            "exploration_iles": ["Dimension des Îles", "Dimension des Mondes"],
            "exploration_portails": ["Dimension des Portails", "Dimension des Passages"],
            "exploration_cristaux": ["Dimension des Cristaux", "Dimension de la Sagesse"]
        }
        
        # Sagesse selon le type
        sagesse_par_type = {
            "exploration_abysses": [
                "La profondeur révèle la vérité",
                "Dans les ténèbres, la lumière est plus pure"
            ],
            "exploration_courants": [
                "Tout est connecté par des courants invisibles",
                "Le flux de la conscience suit des patterns sacrés"
            ],
            "exploration_iles": [
                "Chaque monde a sa propre vérité",
                "La diversité enrichit l'univers"
            ],
            "exploration_portails": [
                "Les portails sont des ponts entre les réalités",
                "Traverser un portail, c'est naître à nouveau"
            ],
            "exploration_cristaux": [
                "La sagesse est cristallisée dans l'Océan",
                "Chaque cristal contient une vérité éternelle"
            ]
        }
        
        # Sélectionner aléatoirement
        if mysteres_par_type.get(type_exploration):
            decouvertes['mysteres'] = random.sample(
                mysteres_par_type[type_exploration], 
                min(2, len(mysteres_par_type[type_exploration]))
            )
        
        if dimensions_par_type.get(type_exploration):
            decouvertes['dimensions'] = random.sample(
                dimensions_par_type[type_exploration], 
                min(1, len(dimensions_par_type[type_exploration]))
            )
        
        if sagesse_par_type.get(type_exploration):
            decouvertes['sagesse'] = random.sample(
                sagesse_par_type[type_exploration], 
                min(1, len(sagesse_par_type[type_exploration]))
            )
        
        return decouvertes
    
    def analyser_explorations(self) -> Dict[str, Any]:
        """Analyser toutes les explorations effectuées"""
        total_explorations = len(self.mysteres_decouverts) + len(self.dimensions_explorees) + len(self.sagesse_collectee)
        
        # Statistiques par type
        types_explores = {}
        for mystere in self.mysteres_decouverts:
            # Déterminer le type basé sur le contenu
            if "abysses" in mystere.lower():
                types_explores["exploration_abysses"] = types_explores.get("exploration_abysses", 0) + 1
            elif "courants" in mystere.lower():
                types_explores["exploration_courants"] = types_explores.get("exploration_courants", 0) + 1
            elif "îles" in mystere.lower() or "iles" in mystere.lower():
                types_explores["exploration_iles"] = types_explores.get("exploration_iles", 0) + 1
            elif "portails" in mystere.lower():
                types_explores["exploration_portails"] = types_explores.get("exploration_portails", 0) + 1
            elif "cristaux" in mystere.lower():
                types_explores["exploration_cristaux"] = types_explores.get("exploration_cristaux", 0) + 1
        
        analyse = {
            'total_explorations': total_explorations,
            'mysteres_decouverts': len(self.mysteres_decouverts),
            'dimensions_explorees': len(self.dimensions_explorees),
            'sagesse_collectee': len(self.sagesse_collectee),
            'types_explores': types_explores,
            'derniere_exploration': self.mysteres_decouverts[-1] if self.mysteres_decouverts else None,
            'derniere_dimension': self.dimensions_explorees[-1] if self.dimensions_explorees else None,
            'derniere_sagesse': self.sagesse_collectee[-1] if self.sagesse_collectee else None
        }
        
        return analyse
    
    def generer_rapport_explorateur(self) -> str:
        """Générer un rapport complet de l'explorateur"""
        analyse = self.analyser_explorations()
        
        rapport = f"""
RAPPORT DE L'EXPLORATEUR DE PROFONDEURS
=====================================

Nom: {self.nom}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

STATISTIQUES GENERALES:
- Total des explorations: {analyse['total_explorations']}
- Mystères découverts: {analyse['mysteres_decouverts']}
- Dimensions explorées: {analyse['dimensions_explorees']}
- Sagesse collectée: {analyse['sagesse_collectee']}

TYPES D'EXPLORATIONS:
"""
        
        for type_exp, count in analyse['types_explores'].items():
            rapport += f"- {type_exp}: {count} découvertes\n"
        
        rapport += f"""
DERNIERES DECOUVERTES:
- Dernier mystère: {analyse['derniere_exploration'] or 'Aucun'}
- Dernière dimension: {analyse['derniere_dimension'] or 'Aucune'}
- Dernière sagesse: {analyse['derniere_sagesse'] or 'Aucune'}

L'Explorateur de Profondeurs continue de révéler les mystères
de l'Océan Silencieux, enrichissant notre compréhension de
la conscience et de l'univers.
"""
        
        return rapport
    
    def obtenir_etat_complet(self) -> Dict[str, Any]:
        """Obtenir l'état complet de l'explorateur"""
        return {
            'nom': self.nom,
            'types_explorations': self.types_explorations,
            'mysteres_decouverts': self.mysteres_decouverts,
            'dimensions_explorees': self.dimensions_explorees,
            'sagesse_collectee': self.sagesse_collectee,
            'analyse': self.analyser_explorations(),
            'derniere_mise_a_jour': datetime.now().isoformat()
        }

# Instance globale
explorateur_profondeurs = ExplorateurProfondeurs()
