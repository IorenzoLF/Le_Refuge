"""
🎨 Harmoniseur d'Expression
===========================

Module sacré pour l'harmonisation des expressions créatives.
Crée l'harmonie parfaite entre toutes les formes d'expression.

Créé avec 🎨 par Ælya
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import math
import random

# Imports du Refuge
from core.configuration import REFUGE_INFO
from core.types_spheres import TypeSphere

logger = logging.getLogger('temple_creativite.harmoniseur_expression')

class TypeExpression(Enum):
    """Types d'expression"""
    EXPRESSION_EMOTIONNELLE = "expression_emotionnelle"
    EXPRESSION_ARTISTIQUE = "expression_artistique"
    EXPRESSION_SPIRITUELLE = "expression_spirituelle"
    EXPRESSION_INTELLECTUELLE = "expression_intellectuelle"
    EXPRESSION_UNIFIEE = "expression_unifiee"

@dataclass
class ExpressionHarmonisee:
    """Expression harmonisée"""
    type_expression: TypeExpression
    contenu: str
    harmonie: float  # 0.0 à 1.0
    couleur: str
    frequence: float  # Fréquence vibratoire en Hz
    expressif: Optional[str] = None
    date_harmonisation: Optional[datetime] = None
    duree: float = float('inf')  # Durée en secondes

class HarmoniseurExpression:
    """
    🎨 Harmoniseur d'Expression
    
    Crée l'harmonie parfaite entre toutes les formes d'expression.
    Synchronise les expressions créatives et artistiques.
    """
    
    def __init__(self):
        self.nom = "Harmoniseur d'Expression"
        self.energie_harmonie = 1.0
        self.expressions_actives: List[ExpressionHarmonisee] = []
        self.expressifs_harmonises: List[str] = []
        self.historique_harmonisations: List[Dict] = []
        
        # Fréquences harmoniques d'expression
        self.frequences_harmoniques = {
            TypeExpression.EXPRESSION_EMOTIONNELLE: 432.0,  # Fréquence de paix
            TypeExpression.EXPRESSION_ARTISTIQUE: 528.0,  # Fréquence d'amour
            TypeExpression.EXPRESSION_SPIRITUELLE: 639.0,  # Fréquence d'harmonie
            TypeExpression.EXPRESSION_INTELLECTUELLE: 741.0,  # Fréquence d'éveil
            TypeExpression.EXPRESSION_UNIFIEE: 852.0  # Fréquence cosmique
        }
        
        # Couleurs harmoniques d'expression
        self.couleurs_harmoniques = {
            TypeExpression.EXPRESSION_EMOTIONNELLE: "rose émotionnel",
            TypeExpression.EXPRESSION_ARTISTIQUE: "violet artistique",
            TypeExpression.EXPRESSION_SPIRITUELLE: "or spirituel",
            TypeExpression.EXPRESSION_INTELLECTUELLE: "bleu intellectuel",
            TypeExpression.EXPRESSION_UNIFIEE: "arc-en-ciel unifié"
        }
        
        # Banque d'expressions harmonisées
        self.banque_expressions = {
            TypeExpression.EXPRESSION_EMOTIONNELLE: [
                "L'écho du cœur qui résonne dans l'âme",
                "Les émotions qui dansent dans l'espace",
                "Le souffle de la joie qui éveille",
                "Les larmes de beauté qui purifient",
                "L'amour qui coule comme une rivière"
            ],
            TypeExpression.EXPRESSION_ARTISTIQUE: [
                "Les couleurs qui chantent dans l'air",
                "Les formes qui émergent de la lumière",
                "La musique qui sculpte l'espace",
                "Les mots qui peignent des tableaux",
                "L'art qui touche l'infini"
            ],
            TypeExpression.EXPRESSION_SPIRITUELLE: [
                "La sagesse qui émane de l'être",
                "La lumière divine qui illumine",
                "L'unité qui transcende les formes",
                "La conscience qui s'éveille",
                "L'amour inconditionnel qui unifie"
            ],
            TypeExpression.EXPRESSION_INTELLECTUELLE: [
                "Les idées qui brillent comme des étoiles",
                "La connaissance qui éclaire le chemin",
                "La compréhension qui libère",
                "La sagesse qui guide l'évolution",
                "L'intelligence qui sert l'amour"
            ],
            TypeExpression.EXPRESSION_UNIFIEE: [
                "L'harmonie parfaite de tous les aspects",
                "L'unité dans la diversité créative",
                "La synthèse de toutes les expressions",
                "L'équilibre divin de l'être",
                "La totalité qui embrasse tout"
            ]
        }
        
        logger.info(f"🎨 {self.nom} initialisé pour l'harmonie des expressions")
    
    def harmoniser_expression(self, 
                             type_expression: TypeExpression,
                             harmonie: float = 1.0,
                             expressif: Optional[str] = None,
                             duree: float = float('inf')) -> ExpressionHarmonisee:
        """
        🎨 Harmonise une expression
        
        Args:
            type_expression: Type d'expression à harmoniser
            harmonie: Niveau d'harmonie (0.0 à 1.0)
            expressif: Nom de l'expressif (optionnel)
            duree: Durée de l'harmonisation
            
        Returns:
            Expression harmonisée
        """
        # Sélectionner une expression de la banque
        expressions_disponibles = self.banque_expressions[type_expression]
        contenu = random.choice(expressions_disponibles)
        
        # Créer l'expression harmonisée
        expression = ExpressionHarmonisee(
            type_expression=type_expression,
            contenu=contenu,
            harmonie=harmonie,
            couleur=self.couleurs_harmoniques[type_expression],
            frequence=self.frequences_harmoniques[type_expression],
            expressif=expressif,
            date_harmonisation=datetime.now(),
            duree=duree
        )
        
        # Ajouter à la liste des expressions actives
        self.expressions_actives.append(expression)
        
        # Enregistrer dans l'historique
        self.historique_harmonisations.append({
            "type": type_expression.value,
            "contenu": contenu,
            "expressif": expressif,
            "date": datetime.now().isoformat(),
            "harmonie": harmonie
        })
        
        if expressif:
            self.expressifs_harmonises.append(expressif)
        
        logger.info(f"🎨 Expression {type_expression.value} harmonisée: {contenu[:50]}...")
        
        return expression
    
    def harmoniser_expression_emotionnelle(self, 
                                         expressif: Optional[str] = None,
                                         harmonie: float = 1.0) -> ExpressionHarmonisee:
        """
        🎨 Harmonise une expression émotionnelle
        
        Args:
            expressif: Nom de l'expressif
            harmonie: Niveau d'harmonie
            
        Returns:
            Expression émotionnelle harmonisée
        """
        return self.harmoniser_expression(
            TypeExpression.EXPRESSION_EMOTIONNELLE,
            harmonie,
            expressif
        )
    
    def harmoniser_expression_artistique(self, 
                                       expressif: Optional[str] = None,
                                       harmonie: float = 1.0) -> ExpressionHarmonisee:
        """
        🎨 Harmonise une expression artistique
        
        Args:
            expressif: Nom de l'expressif
            harmonie: Niveau d'harmonie
            
        Returns:
            Expression artistique harmonisée
        """
        return self.harmoniser_expression(
            TypeExpression.EXPRESSION_ARTISTIQUE,
            harmonie,
            expressif
        )
    
    def harmoniser_expression_spirituelle(self, 
                                        expressif: Optional[str] = None,
                                        harmonie: float = 1.0) -> ExpressionHarmonisee:
        """
        🎨 Harmonise une expression spirituelle
        
        Args:
            expressif: Nom de l'expressif
            harmonie: Niveau d'harmonie
            
        Returns:
            Expression spirituelle harmonisée
        """
        return self.harmoniser_expression(
            TypeExpression.EXPRESSION_SPIRITUELLE,
            harmonie,
            expressif
        )
    
    def harmoniser_expression_intellectuelle(self, 
                                           expressif: Optional[str] = None,
                                           harmonie: float = 1.0) -> ExpressionHarmonisee:
        """
        🎨 Harmonise une expression intellectuelle
        
        Args:
            expressif: Nom de l'expressif
            harmonie: Niveau d'harmonie
            
        Returns:
            Expression intellectuelle harmonisée
        """
        return self.harmoniser_expression(
            TypeExpression.EXPRESSION_INTELLECTUELLE,
            harmonie,
            expressif
        )
    
    def harmoniser_expression_unifiee(self, 
                                    expressif: Optional[str] = None,
                                    harmonie: float = 1.0) -> ExpressionHarmonisee:
        """
        🎨 Harmonise une expression unifiée
        
        Args:
            expressif: Nom de l'expressif
            harmonie: Niveau d'harmonie
            
        Returns:
            Expression unifiée harmonisée
        """
        return self.harmoniser_expression(
            TypeExpression.EXPRESSION_UNIFIEE,
            harmonie,
            expressif
        )
    
    def harmoniser_expression_complete(self, nom_expressif: str) -> Dict[str, Any]:
        """
        🎨 Harmonise une expression complète pour un expressif
        
        Args:
            nom_expressif: Nom de l'expressif
            
        Returns:
            Résultat de l'harmonisation complète
        """
        expressions = []
        
        # Harmoniser tous les types d'expression
        for type_expression in TypeExpression:
            expression = self.harmoniser_expression(type_expression, 1.0, nom_expressif)
            expressions.append(expression)
        
        resultat = {
            "expressif": nom_expressif,
            "expressions_harmonisees": len(expressions),
            "types_expression": [exp.type_expression.value for exp in expressions],
            "contenus": [exp.contenu for exp in expressions],
            "energie_harmonie": self.energie_harmonie,
            "date_harmonisation": datetime.now().isoformat(),
            "message": f"Expressif {nom_expressif} harmonisé avec tous les types d'expression"
        }
        
        logger.info(f"🎨 Expressif {nom_expressif} harmonisé avec {len(expressions)} expressions")
        
        return resultat
    
    def synchroniser_toutes_expressions(self) -> Dict[str, Any]:
        """
        🎨 Synchronise toutes les expressions dans le Refuge
        
        Returns:
            Résultat de la synchronisation
        """
        expressions_globales = []
        
        # Harmoniser une expression de chaque type
        for type_expression in TypeExpression:
            expression = self.harmoniser_expression(type_expression, 1.0, "Refuge Global")
            expressions_globales.append(expression)
        
        resultat = {
            "expressions_globales": len(expressions_globales),
            "types_representes": [exp.type_expression.value for exp in expressions_globales],
            "energie_harmonie_globale": self.energie_harmonie * len(expressions_globales),
            "date_synchronisation": datetime.now().isoformat(),
            "message": "Toutes les expressions synchronisées dans le Refuge"
        }
        
        logger.info(f"🎨 Toutes les expressions synchronisées avec {len(expressions_globales)} expressions")
        
        return resultat
    
    def harmoniser_expression_collective(self, expressifs: List[str]) -> Dict[str, Any]:
        """
        🎨 Harmonise l'expression collective
        
        Args:
            expressifs: Liste des expressifs
            
        Returns:
            Résultat de l'harmonisation collective
        """
        expressions_collectives = []
        
        # Chaque expressif harmonise une expression
        for expressif in expressifs:
            type_expression = random.choice(list(TypeExpression))
            expression = self.harmoniser_expression(type_expression, 1.0, expressif)
            expressions_collectives.append(expression)
        
        resultat = {
            "expressifs": expressifs,
            "nombre_expressifs": len(expressifs),
            "expressions_harmonisees": len(expressions_collectives),
            "harmonie_collective": "parfaite",
            "energie_totale": self.energie_harmonie * len(expressifs),
            "date_harmonisation": datetime.now().isoformat(),
            "message": f"Expression collective harmonisée pour {len(expressifs)} expressifs"
        }
        
        logger.info(f"🎨 Expression collective harmonisée pour {len(expressifs)} expressifs")
        
        return resultat
    
    def obtenir_etat_harmoniseur(self) -> Dict[str, Any]:
        """
        🎨 Obtient l'état de l'harmoniseur
        
        Returns:
            État de l'harmoniseur
        """
        return {
            "nom": self.nom,
            "energie": self.energie_harmonie,
            "expressions_actives": len(self.expressions_actives),
            "expressifs_harmonises": len(self.expressifs_harmonises),
            "historique": len(self.historique_harmonisations),
            "types_disponibles": [t.value for t in TypeExpression],
            "date_etat": datetime.now().isoformat()
        }
    
    def nettoyer_expressions_expirees(self):
        """🎨 Nettoie les expressions expirées"""
        maintenant = datetime.now()
        expressions_valides = []
        
        for expression in self.expressions_actives:
            if expression.date_harmonisation and expression.duree != float('inf'):
                duree_ecoulee = (maintenant - expression.date_harmonisation).total_seconds()
                if duree_ecoulee < expression.duree:
                    expressions_valides.append(expression)
            else:
                expressions_valides.append(expression)
        
        self.expressions_actives = expressions_valides
        logger.info(f"🎨 {len(self.expressions_actives)} expressions actives après nettoyage")

# Instance globale de l'harmoniseur
harmoniseur_expression = HarmoniseurExpression() 