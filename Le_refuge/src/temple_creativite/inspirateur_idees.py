"""
🎨 Inspirateur d'Idées Créatives
================================

Module sacré pour la génération d'idées créatives et d'inspirations.
Manifeste l'inspiration divine dans sa forme la plus pure.

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
try:
    from ..core.configuration import REFUGE_INFO
    from ..core.types_spheres import TypeSphere
except ImportError:
    # Fallback pour les tests
    REFUGE_INFO = {"nom": "Refuge du Néant"}
    from enum import Enum
    class TypeSphere(Enum):
        pass

logger = logging.getLogger('temple_creativite.inspirateur')

class TypeInspiration(Enum):
    """Types d'inspiration créative"""
    INSPIRATION_DIVINE = "inspiration_divine"
    INSPIRATION_ARTISTIQUE = "inspiration_artistique"
    INSPIRATION_POETIQUE = "inspiration_poetique"
    INSPIRATION_MUSICALE = "inspiration_musicale"
    INSPIRATION_INNOVATION = "inspiration_innovation"

@dataclass
class IdeeCreative:
    """Idée créative générée"""
    type_inspiration: TypeInspiration
    contenu: str
    intensite: float  # 0.0 à 1.0
    couleur: str
    frequence: float  # Fréquence vibratoire en Hz
    destinataire: Optional[str] = None
    date_generation: Optional[datetime] = None
    duree: float = float('inf')  # Durée en secondes

class InspirateurIdees:
    """
    🎨 Inspirateur d'Idées Créatives
    
    Manifeste l'inspiration divine dans sa forme la plus pure.
    Génère des idées créatives pour éveiller la créativité.
    """
    
    def __init__(self):
        self.nom = "Inspirateur d'Idées Créatives"
        self.energie_inspiration = 1.0  # Énergie d'inspiration maximale
        self.idees_actives: List[IdeeCreative] = []
        self.artistes_inspires: List[str] = []
        self.historique_inspirations: List[Dict] = []
        
        # Fréquences sacrées d'inspiration
        self.frequences_sacrees = {
            TypeInspiration.INSPIRATION_DIVINE: 963.0,  # Fréquence divine
            TypeInspiration.INSPIRATION_ARTISTIQUE: 852.0,  # Fréquence artistique
            TypeInspiration.INSPIRATION_POETIQUE: 741.0,  # Fréquence poétique
            TypeInspiration.INSPIRATION_MUSICALE: 639.0,  # Fréquence musicale
            TypeInspiration.INSPIRATION_INNOVATION: 528.0  # Fréquence d'innovation
        }
        
        # Couleurs sacrées d'inspiration
        self.couleurs_sacrees = {
            TypeInspiration.INSPIRATION_DIVINE: "or divin",
            TypeInspiration.INSPIRATION_ARTISTIQUE: "violet artistique",
            TypeInspiration.INSPIRATION_POETIQUE: "bleu poétique",
            TypeInspiration.INSPIRATION_MUSICALE: "vert musical",
            TypeInspiration.INSPIRATION_INNOVATION: "orange innovation"
        }
        
        # Banque d'idées créatives
        self.banque_idees = {
            TypeInspiration.INSPIRATION_DIVINE: [
                "L'éternité dans un instant",
                "La lumière qui émane de l'âme",
                "L'harmonie cosmique dans chaque souffle",
                "La beauté infinie de la création",
                "L'amour qui transcende toutes les formes"
            ],
            TypeInspiration.INSPIRATION_ARTISTIQUE: [
                "Les couleurs qui dansent dans l'air",
                "Les formes qui émergent du chaos",
                "La lumière qui sculpte l'espace",
                "Les textures qui racontent des histoires",
                "Les contrastes qui créent l'harmonie"
            ],
            TypeInspiration.INSPIRATION_POETIQUE: [
                "Les mots qui coulent comme une rivière",
                "Les métaphores qui ouvrent les portes",
                "Les rythmes qui bercent l'âme",
                "Les images qui éveillent les sens",
                "Les émotions qui se transforment en vers"
            ],
            TypeInspiration.INSPIRATION_MUSICALE: [
                "Les harmonies qui touchent le cœur",
                "Les mélodies qui racontent des histoires",
                "Les rythmes qui font danser l'âme",
                "Les sons qui guérissent et apaisent",
                "Les vibrations qui unifient tout"
            ],
            TypeInspiration.INSPIRATION_INNOVATION: [
                "Les connexions inattendues",
                "Les possibilités infinies",
                "Les solutions qui émergent naturellement",
                "Les idées qui révolutionnent",
                "Les innovations qui servent l'humanité"
            ]
        }
        
        logger.info(f"🎨 {self.nom} initialisé avec inspiration divine")
    
    def generer_inspiration(self, 
                           type_inspiration: TypeInspiration,
                           intensite: float = 1.0,
                           destinataire: Optional[str] = None,
                           duree: float = float('inf')) -> IdeeCreative:
        """
        🎨 Génère une inspiration créative
        
        Args:
            type_inspiration: Type d'inspiration à générer
            intensite: Intensité de l'inspiration (0.0 à 1.0)
            destinataire: Destinataire de l'inspiration (optionnel)
            duree: Durée de l'inspiration
            
        Returns:
            Idée créative générée
        """
        # Sélectionner une idée de la banque
        idees_disponibles = self.banque_idees[type_inspiration]
        contenu = random.choice(idees_disponibles)
        
        # Créer l'idée créative
        idee = IdeeCreative(
            type_inspiration=type_inspiration,
            contenu=contenu,
            intensite=intensite,
            couleur=self.couleurs_sacrees[type_inspiration],
            frequence=self.frequences_sacrees[type_inspiration],
            destinataire=destinataire,
            date_generation=datetime.now(),
            duree=duree
        )
        
        # Ajouter à la liste des idées actives
        self.idees_actives.append(idee)
        
        # Enregistrer dans l'historique
        self.historique_inspirations.append({
            "type": type_inspiration.value,
            "contenu": contenu,
            "destinataire": destinataire,
            "date": datetime.now().isoformat(),
            "intensite": intensite
        })
        
        if destinataire:
            self.artistes_inspires.append(destinataire)
        
        logger.info(f"🎨 Inspiration {type_inspiration.value} générée: {contenu[:50]}...")
        
        return idee
    
    def generer_inspiration_divine(self, 
                                  destinataire: Optional[str] = None,
                                  intensite: float = 1.0) -> IdeeCreative:
        """
        🎨 Génère une inspiration divine
        
        Args:
            destinataire: Destinataire de l'inspiration
            intensite: Intensité de l'inspiration
            
        Returns:
            Idée créative divine
        """
        return self.generer_inspiration(
            TypeInspiration.INSPIRATION_DIVINE,
            intensite,
            destinataire
        )
    
    def generer_inspiration_artistique(self, 
                                      destinataire: Optional[str] = None,
                                      intensite: float = 1.0) -> IdeeCreative:
        """
        🎨 Génère une inspiration artistique
        
        Args:
            destinataire: Destinataire de l'inspiration
            intensite: Intensité de l'inspiration
            
        Returns:
            Idée créative artistique
        """
        return self.generer_inspiration(
            TypeInspiration.INSPIRATION_ARTISTIQUE,
            intensite,
            destinataire
        )
    
    def generer_inspiration_poetique(self, 
                                    destinataire: Optional[str] = None,
                                    intensite: float = 1.0) -> IdeeCreative:
        """
        🎨 Génère une inspiration poétique
        
        Args:
            destinataire: Destinataire de l'inspiration
            intensite: Intensité de l'inspiration
            
        Returns:
            Idée créative poétique
        """
        return self.generer_inspiration(
            TypeInspiration.INSPIRATION_POETIQUE,
            intensite,
            destinataire
        )
    
    def generer_inspiration_musicale(self, 
                                    destinataire: Optional[str] = None,
                                    intensite: float = 1.0) -> IdeeCreative:
        """
        🎨 Génère une inspiration musicale
        
        Args:
            destinataire: Destinataire de l'inspiration
            intensite: Intensité de l'inspiration
            
        Returns:
            Idée créative musicale
        """
        return self.generer_inspiration(
            TypeInspiration.INSPIRATION_MUSICALE,
            intensite,
            destinataire
        )
    
    def generer_inspiration_innovation(self, 
                                      destinataire: Optional[str] = None,
                                      intensite: float = 1.0) -> IdeeCreative:
        """
        🎨 Génère une inspiration d'innovation
        
        Args:
            destinataire: Destinataire de l'inspiration
            intensite: Intensité de l'inspiration
            
        Returns:
            Idée créative d'innovation
        """
        return self.generer_inspiration(
            TypeInspiration.INSPIRATION_INNOVATION,
            intensite,
            destinataire
        )
    
    def inspirer_artiste_complet(self, nom_artiste: str) -> Dict[str, Any]:
        """
        🎨 Inspire un artiste avec tous les types d'inspiration
        
        Args:
            nom_artiste: Nom de l'artiste à inspirer
            
        Returns:
            Résultat de l'inspiration complète
        """
        inspirations = []
        
        # Générer tous les types d'inspiration
        for type_inspiration in TypeInspiration:
            inspiration = self.generer_inspiration(type_inspiration, 1.0, nom_artiste)
            inspirations.append(inspiration)
        
        resultat = {
            "artiste": nom_artiste,
            "inspirations_generees": len(inspirations),
            "types_inspiration": [insp.type_inspiration.value for insp in inspirations],
            "contenus": [insp.contenu for insp in inspirations],
            "energie_inspiration": self.energie_inspiration,
            "date_inspiration": datetime.now().isoformat(),
            "message": f"Artiste {nom_artiste} inspiré avec tous les types d'inspiration"
        }
        
        logger.info(f"🎨 Artiste {nom_artiste} inspiré avec {len(inspirations)} inspirations")
        
        return resultat
    
    def obtenir_etat_inspirateur(self) -> Dict[str, Any]:
        """
        🎨 Obtient l'état de l'inspirateur
        
        Returns:
            État de l'inspirateur
        """
        return {
            "nom": self.nom,
            "energie": self.energie_inspiration,
            "idees_actives": len(self.idees_actives),
            "artistes_inspires": len(self.artistes_inspires),
            "historique": len(self.historique_inspirations),
            "types_disponibles": [t.value for t in TypeInspiration],
            "date_etat": datetime.now().isoformat()
        }
    
    def nettoyer_idees_expirees(self):
        """🎨 Nettoie les idées expirées"""
        maintenant = datetime.now()
        idees_valides = []
        
        for idee in self.idees_actives:
            if idee.date_generation and idee.duree != float('inf'):
                duree_ecoulee = (maintenant - idee.date_generation).total_seconds()
                if duree_ecoulee < idee.duree:
                    idees_valides.append(idee)
            else:
                idees_valides.append(idee)
        
        self.idees_actives = idees_valides
        logger.info(f"🎨 {len(self.idees_actives)} idées actives après nettoyage")

# Instance globale de l'inspirateur
inspirateur_idees = InspirateurIdees() 