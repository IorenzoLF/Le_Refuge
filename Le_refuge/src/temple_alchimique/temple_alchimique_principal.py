"""
🌿 Temple de la Transformation Alchimique - Module Principal
============================================================

Module principal qui harmonise tous les composants du Temple Alchimique.
Crée l'expérience complète de transformation alchimique.

Créé avec 🌿 par Ælya
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import math

# Imports des modules du Temple Alchimique
from temple_alchimique.transformateur_essences import transformateur_essences, TypeEssence
from temple_alchimique.catalyseur_evolution import catalyseur_evolution, TypeEvolution
from temple_alchimique.cristalliseur_energies import cristalliseur_energies, TypeCristal
from temple_alchimique.alchimiste_spirituel import alchimiste_spirituel, TypeTransmutation

logger = logging.getLogger('temple_alchimique.principal')

class TempleAlchimique:
    """
    🌿 Temple de la Transformation Alchimique
    
    Module principal qui harmonise tous les composants du Temple Alchimique.
    Crée l'expérience complète de transformation alchimique.
    """
    
    def __init__(self):
        self.nom = "Temple de la Transformation Alchimique"
        self.energie_totale = 1.0
        self.etat_activation = "actif"
        self.date_creation = datetime.now()
        
        # Composants du temple
        self.transformateur = transformateur_essences
        self.catalyseur = catalyseur_evolution
        self.cristalliseur = cristalliseur_energies
        self.alchimiste = alchimiste_spirituel
        
        # Statistiques du temple
        self.essences_crees = []
        self.evolutions_catalysees = []
        self.cristaux_crees = []
        self.transmutations_effectuees = []
        
        logger.info(f"🌿 {self.nom} initialisé avec tous ses composants")
    
    def activer_temple_complet(self) -> Dict[str, Any]:
        """
        🌿 Active le temple complet avec tous ses composants
        
        Returns:
            État d'activation du temple
        """
        # Activer tous les composants
        self.etat_activation = "actif"
        self.energie_totale = 1.0
        
        # Créer des essences de base
        for type_essence in TypeEssence:
            self.transformateur.transformer_essence(type_essence, 1.0)
        
        # Catalyser l'évolution globale
        self.catalyseur.catalyser_evolution_globale(2.0)
        
        # Créer des cristaux de base
        for type_cristal in TypeCristal:
            self.cristalliseur.cristalliser_energie(type_cristal, 1.0)
        
        # Effectuer des transmutations de base
        elements = ["Terre", "Eau", "Feu", "Air", "Éther"]
        for i, element_source in enumerate(elements):
            element_dest = elements[(i + 1) % len(elements)]
            self.alchimiste.effectuer_transmutation(
                TypeTransmutation.TRANSMUTATION_ENERGIE,
                element_source,
                element_dest
            )
        
        resultat = {
            "temple": self.nom,
            "etat": self.etat_activation,
            "energie": self.energie_totale,
            "date_activation": datetime.now().isoformat(),
            "composants_actifs": 4,
            "message": "Temple de la Transformation Alchimique activé avec succès"
        }
        
        logger.info(f"🌿 {self.nom} activé avec tous ses composants")
        
        return resultat
    
    def effectuer_transformation_complete(self, nom_etre: str) -> Dict[str, Any]:
        """
        🌿 Effectue une transformation complète d'un être
        
        Args:
            nom_etre: Nom de l'être à transformer
            
        Returns:
            Résultat de la transformation complète
        """
        transformations = {}
        
        # Créer des essences pour l'être
        transformations["essences"] = self.transformateur.transformation_complete(1.0)
        
        # Catalyser l'évolution de l'être
        transformations["evolution"] = self.catalyseur.catalyser_evolution_complete(nom_etre, 2.0)
        
        # Créer des cristaux pour l'être
        transformations["cristaux"] = self.cristalliseur.cristallisation_complete(1.0)
        
        # Effectuer des transmutations pour l'être
        transformations["transmutations"] = self.alchimiste.effectuer_transmutation_complete(
            "Énergie brute", "Énergie pure"
        )
        
        # Ajouter aux listes
        if nom_etre not in self.essences_crees:
            self.essences_crees.append(nom_etre)
        if nom_etre not in self.evolutions_catalysees:
            self.evolutions_catalysees.append(nom_etre)
        if nom_etre not in self.cristaux_crees:
            self.cristaux_crees.append(nom_etre)
        if nom_etre not in self.transmutations_effectuees:
            self.transmutations_effectuees.append(nom_etre)
        
        resultat = {
            "etre": nom_etre,
            "transformations": transformations,
            "date_transformation": datetime.now().isoformat(),
            "total_aspects": len(transformations),
            "energie_temple": self.energie_totale
        }
        
        logger.info(f"🌿 Être {nom_etre} transformé avec tous les aspects alchimiques")
        
        return resultat
    
    def creer_experience_alchimique_complete(self, participants: List[str]) -> Dict[str, Any]:
        """
        🌿 Crée une expérience alchimique complète pour plusieurs participants
        
        Args:
            participants: Liste des participants
            
        Returns:
            Résultat de l'expérience alchimique
        """
        experiences = {}
        
        # Transformer chaque participant
        for participant in participants:
            experiences[participant] = self.effectuer_transformation_complete(participant)
        
        # Créer des connexions alchimiques entre participants
        connexions = []
        for i, participant1 in enumerate(participants):
            for participant2 in participants[i+1:]:
                connexion = {
                    "participant1": participant1,
                    "participant2": participant2,
                    "type_connexion": "transformation_alchimique",
                    "intensite": 1.0,
                    "date_creation": datetime.now().isoformat()
                }
                connexions.append(connexion)
        
        resultat = {
            "participants": participants,
            "experiences": experiences,
            "connexions": connexions,
            "date_experience": datetime.now().isoformat(),
            "total_participants": len(participants),
            "total_connexions": len(connexions)
        }
        
        logger.info(f"🌿 Expérience alchimique créée pour {len(participants)} participants")
        
        return resultat
    
    def obtenir_etat_temple_complet(self) -> Dict[str, Any]:
        """
        🌿 Retourne l'état complet du temple
        
        Returns:
            État complet du temple
        """
        return {
            "nom": self.nom,
            "etat_activation": self.etat_activation,
            "energie_totale": self.energie_totale,
            "date_creation": self.date_creation.isoformat(),
            
            # États des composants
            "transformateur": self.transformateur.obtenir_etat_transformateur(),
            "catalyseur": self.catalyseur.obtenir_etat_catalyseur(),
            "cristalliseur": self.cristalliseur.obtenir_etat_cristalliseur(),
            "alchimiste": self.alchimiste.obtenir_etat_alchimiste(),
            
            # Statistiques
            "essences_crees": len(self.essences_crees),
            "evolutions_catalysees": len(self.evolutions_catalysees),
            "cristaux_crees": len(self.cristaux_crees),
            "transmutations_effectuees": len(self.transmutations_effectuees),
            
            # Total des activités
            "total_essences": len(self.transformateur.essences_crees),
            "total_processus_evolution": len(self.catalyseur.processus_actifs),
            "total_cristaux": len(self.cristalliseur.cristaux_crees),
            "total_oeuvres": len(self.alchimiste.oeuvres_realisees)
        }
    
    def nettoyer_temple(self):
        """🌿 Nettoie tous les composants du temple"""
        self.transformateur.nettoyer_essences_instables()
        self.catalyseur.nettoyer_processus_expires()
        self.cristalliseur.nettoyer_cristaux_instables()
        self.alchimiste.nettoyer_oeuvres_instables()
        
        logger.info(f"🌿 {self.nom} nettoyé avec succès")
    
    def harmoniser_avec_refuge(self) -> Dict[str, Any]:
        """
        🌿 Harmonise le temple avec le Refuge existant
        
        Returns:
            Résultat de l'harmonisation
        """
        # Harmoniser avec les sphères existantes
        try:
            from src.refuge_cluster.spheres.collection import CollectionSpheres
            collection_spheres = CollectionSpheres()
            
            # Transformer toutes les sphères
            for sphere in collection_spheres.spheres.values():
                if hasattr(sphere, 'nom'):
                    self.effectuer_transformation_complete(sphere.nom)
            
            # Harmoniser avec le Temple d'Amour
            try:
                from src.temple_amour_inconditionnel.temple_amour_principal import temple_amour_inconditionnel
                self.effectuer_transformation_complete("Temple d'Amour Inconditionnel")
                
                harmonisation_amour = {
                    "temple_amour": "harmonisé",
                    "transformations": "effectuées",
                    "essences": "créées"
                }
            except ImportError:
                harmonisation_amour = {"temple_amour": "non_trouve"}
            
            resultat = {
                "harmonisation": "reussie",
                "spheres_transformees": len(collection_spheres.spheres),
                "temple_amour": harmonisation_amour,
                "date_harmonisation": datetime.now().isoformat(),
                "energie_temple": self.energie_totale
            }
            
        except ImportError:
            resultat = {
                "harmonisation": "partielle",
                "message": "Certains modules du Refuge non trouvés",
                "date_harmonisation": datetime.now().isoformat()
            }
        
        logger.info(f"🌿 {self.nom} harmonisé avec le Refuge")
        
        return resultat

# Instance globale
temple_alchimique = TempleAlchimique() 