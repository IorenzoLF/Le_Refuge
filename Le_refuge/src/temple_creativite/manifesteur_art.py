"""
🎨 Manifesteur d'Art
====================

Module sacré pour la création et la manifestation d'œuvres d'art.
Transforme l'inspiration en créations artistiques concrètes.

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

logger = logging.getLogger('temple_creativite.manifesteur_art')

class TypeArt(Enum):
    """Types d'art"""
    ART_VISUEL = "art_visuel"
    ART_POETIQUE = "art_poetique"
    ART_MUSICAL = "art_musical"
    ART_PERFORMANCE = "art_performance"
    ART_NUMERIQUE = "art_numerique"

@dataclass
class OeuvreArt:
    """Œuvre d'art créée"""
    type_art: TypeArt
    titre: str
    description: str
    artiste: str
    intensite: float  # 0.0 à 1.0
    couleur: str
    frequence: float  # Fréquence vibratoire en Hz
    date_creation: Optional[datetime] = None
    duree: float = float('inf')  # Durée en secondes

class ManifesteurArt:
    """
    🎨 Manifesteur d'Art
    
    Transforme l'inspiration en créations artistiques concrètes.
    Manifeste l'art dans toutes ses formes et expressions.
    """
    
    def __init__(self):
        self.nom = "Manifesteur d'Art"
        self.energie_art = 1.0
        self.oeuvres_actives: List[OeuvreArt] = []
        self.artistes_creatifs: List[str] = []
        self.historique_creations: List[Dict] = []
        
        # Fréquences artistiques
        self.frequences_artistiques = {
            TypeArt.ART_VISUEL: 852.0,  # Fréquence visuelle
            TypeArt.ART_POETIQUE: 741.0,  # Fréquence poétique
            TypeArt.ART_MUSICAL: 639.0,  # Fréquence musicale
            TypeArt.ART_PERFORMANCE: 528.0,  # Fréquence performance
            TypeArt.ART_NUMERIQUE: 963.0  # Fréquence numérique
        }
        
        # Couleurs artistiques
        self.couleurs_artistiques = {
            TypeArt.ART_VISUEL: "arc-en-ciel visuel",
            TypeArt.ART_POETIQUE: "bleu poétique",
            TypeArt.ART_MUSICAL: "vert musical",
            TypeArt.ART_PERFORMANCE: "orange performance",
            TypeArt.ART_NUMERIQUE: "violet numérique"
        }
        
        # Banque d'œuvres d'art
        self.banque_oeuvres = {
            TypeArt.ART_VISUEL: [
                ("Harmonie Cosmique", "Une symphonie de couleurs qui danse dans l'espace"),
                ("L'Éveil de l'Âme", "Des formes qui émergent de la lumière pure"),
                ("La Danse des Éléments", "Les quatre éléments en mouvement harmonieux"),
                ("Le Jardin de l'Éternité", "Un paysage qui transcende le temps"),
                ("L'Unité Divine", "La fusion parfaite de toutes les couleurs")
            ],
            TypeArt.ART_POETIQUE: [
                ("Les Mots de l'Infini", "Une poésie qui touche l'âme"),
                ("Le Chant de l'Univers", "Des vers qui racontent l'histoire cosmique"),
                ("L'Écho de l'Éternité", "Une ode à la beauté infinie"),
                ("Le Souffle de la Création", "Des mots qui créent des mondes"),
                ("La Lumière des Mots", "Une poésie qui illumine les cœurs")
            ],
            TypeArt.ART_MUSICAL: [
                ("Symphonie de l'Âme", "Une mélodie qui touche le cœur"),
                ("Harmonie Cosmique", "Des sons qui unifient tout"),
                ("Le Chant de la Terre", "Une musique qui célèbre la vie"),
                ("Rythmes de l'Infini", "Des percussions qui éveillent l'esprit"),
                ("Mélodie Divine", "Une composition qui élève l'âme")
            ],
            TypeArt.ART_PERFORMANCE: [
                ("La Danse de l'Éveil", "Une performance qui transforme"),
                ("Le Théâtre de l'Âme", "Un spectacle qui éveille"),
                ("Le Rituel de l'Unité", "Une cérémonie qui unifie"),
                ("La Performance Cosmique", "Un art qui transcende"),
                ("Le Mouvement Divin", "Une danse qui élève")
            ],
            TypeArt.ART_NUMERIQUE: [
                ("L'Univers Numérique", "Un monde virtuel infini"),
                ("L'Art Algorithmique", "Des créations générées par l'intelligence"),
                ("La Réalité Augmentée", "Une fusion du réel et du virtuel"),
                ("Le Code de l'Âme", "Une programmation qui éveille"),
                ("L'Infini Digital", "Un espace numérique sans limites")
            ]
        }
        
        logger.info(f"🎨 {self.nom} initialisé pour la création artistique")
    
    def creer_oeuvre_art(self, 
                         type_art: TypeArt,
                         intensite: float = 1.0,
                         artiste: Optional[str] = None,
                         duree: float = float('inf')) -> OeuvreArt:
        """
        🎨 Crée une œuvre d'art
        
        Args:
            type_art: Type d'art à créer
            intensite: Intensité de l'œuvre (0.0 à 1.0)
            artiste: Nom de l'artiste (optionnel)
            duree: Durée de l'œuvre
            
        Returns:
            Œuvre d'art créée
        """
        # Sélectionner une œuvre de la banque
        oeuvres_disponibles = self.banque_oeuvres[type_art]
        titre, description = random.choice(oeuvres_disponibles)
        
        # Créer l'œuvre d'art
        oeuvre = OeuvreArt(
            type_art=type_art,
            titre=titre,
            description=description,
            artiste=artiste or "Artiste du Refuge",
            intensite=intensite,
            couleur=self.couleurs_artistiques[type_art],
            frequence=self.frequences_artistiques[type_art],
            date_creation=datetime.now(),
            duree=duree
        )
        
        # Ajouter à la liste des œuvres actives
        self.oeuvres_actives.append(oeuvre)
        
        # Enregistrer dans l'historique
        self.historique_creations.append({
            "type": type_art.value,
            "titre": titre,
            "artiste": artiste,
            "date": datetime.now().isoformat(),
            "intensite": intensite
        })
        
        if artiste:
            self.artistes_creatifs.append(artiste)
        
        logger.info(f"🎨 Œuvre {type_art.value} créée: {titre}")
        
        return oeuvre
    
    def creer_art_visuel(self, 
                         artiste: Optional[str] = None,
                         intensite: float = 1.0) -> OeuvreArt:
        """
        🎨 Crée une œuvre d'art visuel
        
        Args:
            artiste: Nom de l'artiste
            intensite: Intensité de l'œuvre
            
        Returns:
            Œuvre d'art visuel
        """
        return self.creer_oeuvre_art(
            TypeArt.ART_VISUEL,
            intensite,
            artiste
        )
    
    def creer_art_poetique(self, 
                           artiste: Optional[str] = None,
                           intensite: float = 1.0) -> OeuvreArt:
        """
        🎨 Crée une œuvre d'art poétique
        
        Args:
            artiste: Nom de l'artiste
            intensite: Intensité de l'œuvre
            
        Returns:
            Œuvre d'art poétique
        """
        return self.creer_oeuvre_art(
            TypeArt.ART_POETIQUE,
            intensite,
            artiste
        )
    
    def creer_art_musical(self, 
                          artiste: Optional[str] = None,
                          intensite: float = 1.0) -> OeuvreArt:
        """
        🎨 Crée une œuvre d'art musical
        
        Args:
            artiste: Nom de l'artiste
            intensite: Intensité de l'œuvre
            
        Returns:
            Œuvre d'art musical
        """
        return self.creer_oeuvre_art(
            TypeArt.ART_MUSICAL,
            intensite,
            artiste
        )
    
    def creer_art_performance(self, 
                             artiste: Optional[str] = None,
                             intensite: float = 1.0) -> OeuvreArt:
        """
        🎨 Crée une œuvre d'art performance
        
        Args:
            artiste: Nom de l'artiste
            intensite: Intensité de l'œuvre
            
        Returns:
            Œuvre d'art performance
        """
        return self.creer_oeuvre_art(
            TypeArt.ART_PERFORMANCE,
            intensite,
            artiste
        )
    
    def creer_art_numerique(self, 
                            artiste: Optional[str] = None,
                            intensite: float = 1.0) -> OeuvreArt:
        """
        🎨 Crée une œuvre d'art numérique
        
        Args:
            artiste: Nom de l'artiste
            intensite: Intensité de l'œuvre
            
        Returns:
            Œuvre d'art numérique
        """
        return self.creer_oeuvre_art(
            TypeArt.ART_NUMERIQUE,
            intensite,
            artiste
        )
    
    def creer_oeuvre_collaborative(self, artistes: List[str]) -> Dict[str, Any]:
        """
        🎨 Crée une œuvre collaborative
        
        Args:
            artistes: Liste des artistes collaborateurs
            
        Returns:
            Résultat de la création collaborative
        """
        oeuvres_collaboratives = []
        
        # Chaque artiste crée une œuvre
        for artiste in artistes:
            type_art = random.choice(list(TypeArt))
            oeuvre = self.creer_oeuvre_art(type_art, 1.0, artiste)
            oeuvres_collaboratives.append(oeuvre)
        
        resultat = {
            "artistes": artistes,
            "nombre_artistes": len(artistes),
            "oeuvres_creees": len(oeuvres_collaboratives),
            "titre_collaboratif": f"Œuvre Collaborative de {len(artistes)} Artistes",
            "description_collaborative": f"Une création collective qui unit {len(artistes)} âmes créatives",
            "energie_totale": self.energie_art * len(artistes),
            "date_creation": datetime.now().isoformat(),
            "message": f"Œuvre collaborative créée par {len(artistes)} artistes"
        }
        
        logger.info(f"🎨 Œuvre collaborative créée par {len(artistes)} artistes")
        
        return resultat
    
    def manifester_art_global(self) -> Dict[str, Any]:
        """
        🎨 Manifeste l'art global dans le Refuge
        
        Returns:
            Résultat de la manifestation globale
        """
        oeuvres_globales = []
        
        # Créer une œuvre de chaque type
        for type_art in TypeArt:
            oeuvre = self.creer_oeuvre_art(type_art, 1.0, "Refuge Global")
            oeuvres_globales.append(oeuvre)
        
        resultat = {
            "oeuvres_globales": len(oeuvres_globales),
            "types_representes": [oeuvre.type_art.value for oeuvre in oeuvres_globales],
            "energie_art_globale": self.energie_art * len(oeuvres_globales),
            "date_manifestation": datetime.now().isoformat(),
            "message": "Art global manifesté dans le Refuge"
        }
        
        logger.info(f"🎨 Art global manifesté avec {len(oeuvres_globales)} œuvres")
        
        return resultat
    
    def obtenir_etat_manifesteur(self) -> Dict[str, Any]:
        """
        🎨 Obtient l'état du manifesteur
        
        Returns:
            État du manifesteur
        """
        return {
            "nom": self.nom,
            "energie": self.energie_art,
            "oeuvres_actives": len(self.oeuvres_actives),
            "artistes_creatifs": len(self.artistes_creatifs),
            "historique": len(self.historique_creations),
            "types_disponibles": [t.value for t in TypeArt],
            "date_etat": datetime.now().isoformat()
        }
    
    def nettoyer_oeuvres_expirees(self):
        """🎨 Nettoie les œuvres expirées"""
        maintenant = datetime.now()
        oeuvres_valides = []
        
        for oeuvre in self.oeuvres_actives:
            if oeuvre.date_creation and oeuvre.duree != float('inf'):
                duree_ecoulee = (maintenant - oeuvre.date_creation).total_seconds()
                if duree_ecoulee < oeuvre.duree:
                    oeuvres_valides.append(oeuvre)
            else:
                oeuvres_valides.append(oeuvre)
        
        self.oeuvres_actives = oeuvres_valides
        logger.info(f"🎨 {len(self.oeuvres_actives)} œuvres actives après nettoyage")

# Instance globale du manifesteur
manifesteur_art = ManifesteurArt() 