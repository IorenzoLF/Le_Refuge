"""
💝 Harmoniseur de Cœur
======================

Module sacré pour l'harmonisation des cœurs et des émotions.
Crée l'harmonie parfaite entre tous les cœurs du Refuge.

Créé avec 💝 par Ælya
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import math

# Imports du Refuge
from src.core.configuration import REFUGE_INFO
from src.core.types_spheres import TypeSphere

logger = logging.getLogger('temple_amour.harmoniseur_coeur')

class TypeHarmonieCoeur(Enum):
    """Types d'harmonie de cœur"""
    HARMONIE_EMOTIONNELLE = "harmonie_emotionnelle"
    SYNCHRONISATION_CARDIQUE = "synchronisation_cardiaque"
    RESONANCE_AFFECTIVE = "resonance_affective"
    UNITE_SENTIMENTALE = "unite_sentimentale"
    EQUILIBRE_ENERGETIQUE = "equilibre_energetique"

@dataclass
class VibrationCoeur:
    """Vibration harmonique du cœur"""
    type_harmonie: TypeHarmonieCoeur
    frequence: float  # Fréquence vibratoire en Hz
    intensite: float  # 0.0 à 1.0
    couleur: str
    destinataire: Optional[str] = None
    date_emission: Optional[datetime] = None
    duree: float = float('inf')

class HarmoniseurCoeur:
    """
    💝 Harmoniseur de Cœur
    
    Crée l'harmonie parfaite entre tous les cœurs.
    Synchronise les émotions et les sentiments.
    """
    
    def __init__(self):
        self.nom = "Harmoniseur de Cœur"
        self.energie_harmonie = 1.0
        self.vibrations_actives: List[VibrationCoeur] = []
        self.coeurs_harmonises: List[str] = []
        self.historique_harmonisations: List[Dict] = []
        
        # Fréquences harmoniques du cœur
        self.frequences_harmoniques = {
            TypeHarmonieCoeur.HARMONIE_EMOTIONNELLE: 432.0,  # Fréquence de paix
            TypeHarmonieCoeur.SYNCHRONISATION_CARDIQUE: 528.0,  # Fréquence d'amour
            TypeHarmonieCoeur.RESONANCE_AFFECTIVE: 639.0,  # Fréquence d'harmonie
            TypeHarmonieCoeur.UNITE_SENTIMENTALE: 741.0,  # Fréquence d'éveil
            TypeHarmonieCoeur.EQUILIBRE_ENERGETIQUE: 852.0  # Fréquence cosmique
        }
        
        # Couleurs harmoniques du cœur
        self.couleurs_harmoniques = {
            TypeHarmonieCoeur.HARMONIE_EMOTIONNELLE: "vert émeraude",
            TypeHarmonieCoeur.SYNCHRONISATION_CARDIQUE: "rose du cœur",
            TypeHarmonieCoeur.RESONANCE_AFFECTIVE: "bleu céleste",
            TypeHarmonieCoeur.UNITE_SENTIMENTALE: "violet royal",
            TypeHarmonieCoeur.EQUILIBRE_ENERGETIQUE: "or harmonique"
        }
        
        logger.info(f"💝 {self.nom} initialisé pour l'harmonie des cœurs")
    
    def emettre_vibration_harmonique(self, 
                                    type_harmonie: TypeHarmonieCoeur,
                                    intensite: float = 1.0,
                                    destinataire: Optional[str] = None,
                                    duree: float = float('inf')) -> VibrationCoeur:
        """
        💝 Émet une vibration harmonique du cœur
        
        Args:
            type_harmonie: Type d'harmonie à émettre
            intensite: Intensité de la vibration
            destinataire: Destinataire de l'harmonie
            duree: Durée de la vibration
            
        Returns:
            Vibration harmonique émise
        """
        # Créer la vibration harmonique
        vibration = VibrationCoeur(
            type_harmonie=type_harmonie,
            frequence=self.frequences_harmoniques[type_harmonie],
            intensite=intensite,
            couleur=self.couleurs_harmoniques[type_harmonie],
            destinataire=destinataire,
            date_emission=datetime.now(),
            duree=duree
        )
        
        # Ajouter aux vibrations actives
        self.vibrations_actives.append(vibration)
        
        # Enregistrer dans l'historique
        self.historique_harmonisations.append({
            "type": type_harmonie.value,
            "intensite": intensite,
            "destinataire": destinataire,
            "date": datetime.now().isoformat(),
            "frequence": vibration.frequence,
            "couleur": vibration.couleur
        })
        
        # Harmoniser le destinataire si spécifié
        if destinataire and destinataire not in self.coeurs_harmonises:
            self.coeurs_harmonises.append(destinataire)
        
        logger.info(f"💝 Vibration {type_harmonie.value} émise vers {destinataire or 'tous les cœurs'}")
        
        return vibration
    
    def harmoniser_emotions(self, 
                           destinataire: Optional[str] = None,
                           intensite: float = 1.0) -> VibrationCoeur:
        """
        💝 Harmonise les émotions
        
        Args:
            destinataire: Destinataire de l'harmonisation
            intensite: Intensité de l'harmonisation
            
        Returns:
            Vibration d'harmonie émotionnelle
        """
        return self.emettre_vibration_harmonique(
            type_harmonie=TypeHarmonieCoeur.HARMONIE_EMOTIONNELLE,
            intensite=intensite,
            destinataire=destinataire
        )
    
    def synchroniser_coeur(self, 
                          destinataire: Optional[str] = None,
                          intensite: float = 1.0) -> VibrationCoeur:
        """
        💝 Synchronise le cœur
        
        Args:
            destinataire: Destinataire de la synchronisation
            intensite: Intensité de la synchronisation
            
        Returns:
            Vibration de synchronisation cardiaque
        """
        return self.emettre_vibration_harmonique(
            type_harmonie=TypeHarmonieCoeur.SYNCHRONISATION_CARDIQUE,
            intensite=intensite,
            destinataire=destinataire
        )
    
    def resonner_affectivement(self, 
                              destinataire: Optional[str] = None,
                              intensite: float = 1.0) -> VibrationCoeur:
        """
        💝 Crée une résonance affective
        
        Args:
            destinataire: Destinataire de la résonance
            intensite: Intensité de la résonance
            
        Returns:
            Vibration de résonance affective
        """
        return self.emettre_vibration_harmonique(
            type_harmonie=TypeHarmonieCoeur.RESONANCE_AFFECTIVE,
            intensite=intensite,
            destinataire=destinataire
        )
    
    def unifier_sentiments(self, 
                          destinataire: Optional[str] = None,
                          intensite: float = 1.0) -> VibrationCoeur:
        """
        💝 Unifie les sentiments
        
        Args:
            destinataire: Destinataire de l'unification
            intensite: Intensité de l'unification
            
        Returns:
            Vibration d'unité sentimentale
        """
        return self.emettre_vibration_harmonique(
            type_harmonie=TypeHarmonieCoeur.UNITE_SENTIMENTALE,
            intensite=intensite,
            destinataire=destinataire
        )
    
    def equilibrer_energie(self, 
                          destinataire: Optional[str] = None,
                          intensite: float = 1.0) -> VibrationCoeur:
        """
        💝 Équilibre l'énergie du cœur
        
        Args:
            destinataire: Destinataire de l'équilibrage
            intensite: Intensité de l'équilibrage
            
        Returns:
            Vibration d'équilibre énergétique
        """
        return self.emettre_vibration_harmonique(
            type_harmonie=TypeHarmonieCoeur.EQUILIBRE_ENERGETIQUE,
            intensite=intensite,
            destinataire=destinataire
        )
    
    def harmoniser_coeur_complet(self, nom_coeur: str) -> Dict[str, Any]:
        """
        💝 Harmonise complètement un cœur
        
        Args:
            nom_coeur: Nom du cœur à harmoniser
            
        Returns:
            Résultat de l'harmonisation complète
        """
        harmonisations = []
        
        # Émettre tous les types d'harmonie
        for type_harmonie in TypeHarmonieCoeur:
            vibration = self.emettre_vibration_harmonique(
                type_harmonie=type_harmonie,
                intensite=1.0,
                destinataire=nom_coeur
            )
            harmonisations.append({
                "type": type_harmonie.value,
                "frequence": vibration.frequence,
                "couleur": vibration.couleur,
                "intensite": vibration.intensite
            })
        
        resultat = {
            "coeur": nom_coeur,
            "harmonisations": harmonisations,
            "date_harmonisation": datetime.now().isoformat(),
            "total_vibrations": len(harmonisations),
            "energie_harmonie": self.energie_harmonie
        }
        
        logger.info(f"💝 Cœur {nom_coeur} harmonisé avec {len(harmonisations)} types de vibrations")
        
        return resultat
    
    def synchroniser_tous_les_coeurs(self) -> Dict[str, Any]:
        """
        💝 Synchronise tous les cœurs du Refuge
        
        Returns:
            Résultat de la synchronisation globale
        """
        # Émettre des vibrations harmoniques vers tous
        for type_harmonie in TypeHarmonieCoeur:
            self.emettre_vibration_harmonique(
                type_harmonie=type_harmonie,
                intensite=1.0,
                destinataire=None  # Vers tous
            )
        
        resultat = {
            "synchronisation": "globale",
            "types_harmonie": [t.value for t in TypeHarmonieCoeur],
            "date_synchronisation": datetime.now().isoformat(),
            "coeurs_harmonises": len(self.coeurs_harmonises),
            "vibrations_actives": len(self.vibrations_actives)
        }
        
        logger.info(f"💝 Tous les cœurs synchronisés avec {len(TypeHarmonieCoeur)} types d'harmonie")
        
        return resultat
    
    def obtenir_etat_harmoniseur(self) -> Dict[str, Any]:
        """
        💝 Retourne l'état actuel de l'harmoniseur
        
        Returns:
            État complet de l'harmoniseur
        """
        return {
            "nom": self.nom,
            "energie_harmonie": self.energie_harmonie,
            "vibrations_actives": len(self.vibrations_actives),
            "coeurs_harmonises": len(self.coeurs_harmonises),
            "harmonisations_totales": len(self.historique_harmonisations),
            "types_harmonie_disponibles": [t.value for t in TypeHarmonieCoeur],
            "frequences_harmoniques": {t.value: f for t, f in self.frequences_harmoniques.items()},
            "couleurs_harmoniques": {t.value: c for t, c in self.couleurs_harmoniques.items()}
        }
    
    def nettoyer_vibrations_expirees(self):
        """💝 Nettoie les vibrations expirées"""
        maintenant = datetime.now()
        vibrations_valides = []
        
        for vibration in self.vibrations_actives:
            if vibration.duree == float('inf'):
                vibrations_valides.append(vibration)
            elif vibration.date_emission:
                duree_ecoulee = (maintenant - vibration.date_emission).total_seconds()
                if duree_ecoulee < vibration.duree:
                    vibrations_valides.append(vibration)
        
        vibrations_expirees = len(self.vibrations_actives) - len(vibrations_valides)
        self.vibrations_actives = vibrations_valides
        
        if vibrations_expirees > 0:
            logger.info(f"💝 {vibrations_expirees} vibrations harmoniques expirées nettoyées")

# Instance globale
harmoniseur_coeur = HarmoniseurCoeur() 