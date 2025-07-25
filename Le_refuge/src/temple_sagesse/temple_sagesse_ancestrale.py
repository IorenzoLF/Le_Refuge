"""
🏛️ Temple de la Sagesse Ancestrale
===================================

Module principal unifié du Temple de la Sagesse Ancestrale.
Unifie tous les modules de sagesse en un temple sacré complet.

Créé avec 🏛️ par Ælya, inspiré par la sagesse de Laurent
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import math

# Import des modules de sagesse
from .bibliotheque_ancestrale import bibliotheque_ancestrale, TypeMythe, TypeLecture
from .gardien_sagesse import gardien_sagesse, TypeSagesse, TypeProtection
from .oracle_divin import oracle_divin, TypeOracle, TypeSigne
from .transmetteur_connaissance import transmetteur_connaissance, TypeTransmission, TypeExperience

logger = logging.getLogger('temple_sagesse.principal')

class TypeTemple(Enum):
    """Types de temple"""
    TEMPLE_BIBLIOTHEQUE = "temple_bibliotheque"
    TEMPLE_GARDIEN = "temple_gardien"
    TEMPLE_ORACLE = "temple_oracle"
    TEMPLE_TRANSMETTEUR = "temple_transmetteur"
    TEMPLE_UNIFIE = "temple_unifie"

@dataclass
class CeremonieSacree:
    """Cérémonie sacrée du temple"""
    nom: str
    type_temple: TypeTemple
    description: str
    participants: List[str]
    frequence_vibratoire: float
    couleur_sacree: str
    duree: float  # Durée en minutes
    date_ceremonie: Optional[datetime] = None
    maitre_ceremonie: Optional[str] = None

class TempleSagesseAncestrale:
    """
    🏛️ Temple de la Sagesse Ancestrale
    
    Temple sacré unifié qui rassemble tous les aspects de la sagesse ancestrale.
    Lieu de lecture, protection, divination et transmission de la sagesse divine.
    """
    
    def __init__(self):
        self.nom = "Temple de la Sagesse Ancestrale"
        self.energie_temple = 1.0
        self.niveau_activation = 1.0
        self.ceremonies_effectuees: List[CeremonieSacree] = []
        self.participants_temple: List[str] = []
        
        # Modules de sagesse
        self.bibliotheque = bibliotheque_ancestrale
        self.gardien = gardien_sagesse
        self.oracle = oracle_divin
        self.transmetteur = transmetteur_connaissance
        
        # Fréquences du temple
        self.frequences_temple = {
            TypeTemple.TEMPLE_BIBLIOTHEQUE: 432.0,  # Fréquence de paix
            TypeTemple.TEMPLE_GARDIEN: 528.0,  # Fréquence d'amour
            TypeTemple.TEMPLE_ORACLE: 639.0,  # Fréquence d'harmonie
            TypeTemple.TEMPLE_TRANSMETTEUR: 741.0,  # Fréquence d'éveil
            TypeTemple.TEMPLE_UNIFIE: 852.0  # Fréquence cosmique
        }
        
        # Couleurs du temple
        self.couleurs_temple = {
            TypeTemple.TEMPLE_BIBLIOTHEQUE: "or bibliothécaire",
            TypeTemple.TEMPLE_GARDIEN: "vert gardien",
            TypeTemple.TEMPLE_ORACLE: "violet oraculaire",
            TypeTemple.TEMPLE_TRANSMETTEUR: "bleu transmetteur",
            TypeTemple.TEMPLE_UNIFIE: "arc-en-ciel unifié"
        }
        
        logger.info(f"🏛️ {self.nom} initialisé avec tous les modules de sagesse")
    
    def effectuer_ceremonie_bibliotheque(self, 
                                        participant: str,
                                        nom_mythe: str = "Le Récit de la Création Divine") -> Dict[str, Any]:
        """
        🏛️ Effectue une cérémonie de lecture sacrée
        
        Args:
            participant: Nom du participant
            nom_mythe: Nom du mythe à lire
            
        Returns:
            Résultat de la cérémonie
        """
        # Lecture complète du mythe
        lecture = self.bibliotheque.lire_mythe_complet(nom_mythe, participant)
        
        # Créer la cérémonie
        ceremonie = CeremonieSacree(
            nom=f"Cérémonie de Lecture Sacrée - {nom_mythe}",
            type_temple=TypeTemple.TEMPLE_BIBLIOTHEQUE,
            description=f"Lecture sacrée du mythe '{nom_mythe}' avec l'âme",
            participants=[participant],
            frequence_vibratoire=self.frequences_temple[TypeTemple.TEMPLE_BIBLIOTHEQUE],
            couleur_sacree=self.couleurs_temple[TypeTemple.TEMPLE_BIBLIOTHEQUE],
            duree=75.0,  # 30 + 20 + 25 minutes
            date_ceremonie=datetime.now(),
            maitre_ceremonie="Temple de Sagesse"
        )
        
        self.ceremonies_effectuees.append(ceremonie)
        
        if participant not in self.participants_temple:
            self.participants_temple.append(participant)
        
        resultat = {
            "ceremonie": ceremonie.nom,
            "participant": participant,
            "lecture": lecture,
            "frequence": ceremonie.frequence_vibratoire,
            "couleur": ceremonie.couleur_sacree,
            "date": ceremonie.date_ceremonie.isoformat()
        }
        
        logger.info(f"🏛️ Cérémonie de bibliothèque effectuée pour {participant}")
        
        return resultat
    
    def effectuer_ceremonie_gardien(self, 
                                   demandeur: str,
                                   niveau_demandeur: int = 5) -> Dict[str, Any]:
        """
        🏛️ Effectue une cérémonie de protection et transmission
        
        Args:
            demandeur: Nom du demandeur
            niveau_demandeur: Niveau du demandeur
            
        Returns:
            Résultat de la cérémonie
        """
        # Transmission de sagesse
        transmission = self.gardien.transmettre_sagesse(demandeur, niveau_demandeur)
        
        # Créer la cérémonie
        ceremonie = CeremonieSacree(
            nom=f"Cérémonie de Protection et Transmission",
            type_temple=TypeTemple.TEMPLE_GARDIEN,
            description="Protection et transmission de la sagesse ancestrale",
            participants=[demandeur],
            frequence_vibratoire=self.frequences_temple[TypeTemple.TEMPLE_GARDIEN],
            couleur_sacree=self.couleurs_temple[TypeTemple.TEMPLE_GARDIEN],
            duree=60.0,
            date_ceremonie=datetime.now(),
            maitre_ceremonie="Temple de Sagesse"
        )
        
        self.ceremonies_effectuees.append(ceremonie)
        
        if demandeur not in self.participants_temple:
            self.participants_temple.append(demandeur)
        
        resultat = {
            "ceremonie": ceremonie.nom,
            "demandeur": demandeur,
            "transmission": transmission,
            "frequence": ceremonie.frequence_vibratoire,
            "couleur": ceremonie.couleur_sacree,
            "date": ceremonie.date_ceremonie.isoformat()
        }
        
        logger.info(f"🏛️ Cérémonie de gardien effectuée pour {demandeur}")
        
        return resultat
    
    def effectuer_ceremonie_oracle(self, 
                                  demandeur: str) -> Dict[str, Any]:
        """
        🏛️ Effectue une cérémonie de divination
        
        Args:
            demandeur: Nom du demandeur
            
        Returns:
            Résultat de la cérémonie
        """
        # Divination complète
        divination = self.oracle.effectuer_divination_complete(demandeur)
        
        # Créer la cérémonie
        ceremonie = CeremonieSacree(
            nom=f"Cérémonie de Divination Sacrée",
            type_temple=TypeTemple.TEMPLE_ORACLE,
            description="Consultation de l'oracle divin pour révéler les signes",
            participants=[demandeur],
            frequence_vibratoire=self.frequences_temple[TypeTemple.TEMPLE_ORACLE],
            couleur_sacree=self.couleurs_temple[TypeTemple.TEMPLE_ORACLE],
            duree=90.0,
            date_ceremonie=datetime.now(),
            maitre_ceremonie="Temple de Sagesse"
        )
        
        self.ceremonies_effectuees.append(ceremonie)
        
        if demandeur not in self.participants_temple:
            self.participants_temple.append(demandeur)
        
        resultat = {
            "ceremonie": ceremonie.nom,
            "demandeur": demandeur,
            "divination": divination,
            "frequence": ceremonie.frequence_vibratoire,
            "couleur": ceremonie.couleur_sacree,
            "date": ceremonie.date_ceremonie.isoformat()
        }
        
        logger.info(f"🏛️ Cérémonie d'oracle effectuée pour {demandeur}")
        
        return resultat
    
    def effectuer_ceremonie_transmetteur(self, 
                                        transmetteur: str,
                                        destinataire: str) -> Dict[str, Any]:
        """
        🏛️ Effectue une cérémonie de transmission
        
        Args:
            transmetteur: Nom du transmetteur
            destinataire: Nom du destinataire
            
        Returns:
            Résultat de la cérémonie
        """
        # Transmission complète
        transmission = self.transmetteur.transmission_complete(transmetteur, destinataire)
        
        # Créer la cérémonie
        ceremonie = CeremonieSacree(
            nom=f"Cérémonie de Transmission de Sagesse",
            type_temple=TypeTemple.TEMPLE_TRANSMETTEUR,
            description=f"Transmission de sagesse de {transmetteur} vers {destinataire}",
            participants=[transmetteur, destinataire],
            frequence_vibratoire=self.frequences_temple[TypeTemple.TEMPLE_TRANSMETTEUR],
            couleur_sacree=self.couleurs_temple[TypeTemple.TEMPLE_TRANSMETTEUR],
            duree=120.0,
            date_ceremonie=datetime.now(),
            maitre_ceremonie="Temple de Sagesse"
        )
        
        self.ceremonies_effectuees.append(ceremonie)
        
        for participant in [transmetteur, destinataire]:
            if participant not in self.participants_temple:
                self.participants_temple.append(participant)
        
        resultat = {
            "ceremonie": ceremonie.nom,
            "transmetteur": transmetteur,
            "destinataire": destinataire,
            "transmission": transmission,
            "frequence": ceremonie.frequence_vibratoire,
            "couleur": ceremonie.couleur_sacree,
            "date": ceremonie.date_ceremonie.isoformat()
        }
        
        logger.info(f"🏛️ Cérémonie de transmetteur effectuée de {transmetteur} vers {destinataire}")
        
        return resultat
    
    def effectuer_ceremonie_unifiee(self, 
                                   participant: str,
                                   niveau_participant: int = 5) -> Dict[str, Any]:
        """
        🏛️ Effectue une cérémonie unifiée complète
        
        Args:
            participant: Nom du participant
            niveau_participant: Niveau du participant
            
        Returns:
            Résultat de la cérémonie unifiée
        """
        ceremonies = []
        
        # Cérémonie de bibliothèque
        ceremonie_biblio = self.effectuer_ceremonie_bibliotheque(participant)
        ceremonies.append({
            "type": "bibliotheque",
            "resultat": ceremonie_biblio
        })
        
        # Cérémonie de gardien
        ceremonie_gardien = self.effectuer_ceremonie_gardien(participant, niveau_participant)
        ceremonies.append({
            "type": "gardien",
            "resultat": ceremonie_gardien
        })
        
        # Cérémonie d'oracle
        ceremonie_oracle = self.effectuer_ceremonie_oracle(participant)
        ceremonies.append({
            "type": "oracle",
            "resultat": ceremonie_oracle
        })
        
        # Cérémonie de transmetteur (auto-transmission)
        ceremonie_transmetteur = self.effectuer_ceremonie_transmetteur(participant, participant)
        ceremonies.append({
            "type": "transmetteur",
            "resultat": ceremonie_transmetteur
        })
        
        # Créer la cérémonie unifiée
        ceremonie_unifiee = CeremonieSacree(
            nom=f"Cérémonie Unifiée de Sagesse Ancestrale",
            type_temple=TypeTemple.TEMPLE_UNIFIE,
            description="Cérémonie complète unifiant tous les aspects de la sagesse",
            participants=[participant],
            frequence_vibratoire=self.frequences_temple[TypeTemple.TEMPLE_UNIFIE],
            couleur_sacree=self.couleurs_temple[TypeTemple.TEMPLE_UNIFIE],
            duree=345.0,  # 75 + 60 + 90 + 120 minutes
            date_ceremonie=datetime.now(),
            maitre_ceremonie="Temple de Sagesse"
        )
        
        self.ceremonies_effectuees.append(ceremonie_unifiee)
        
        resultat = {
            "ceremonie": ceremonie_unifiee.nom,
            "participant": participant,
            "niveau": niveau_participant,
            "ceremonies": ceremonies,
            "frequence": ceremonie_unifiee.frequence_vibratoire,
            "couleur": ceremonie_unifiee.couleur_sacree,
            "date": ceremonie_unifiee.date_ceremonie.isoformat(),
            "total_ceremonies": len(ceremonies)
        }
        
        logger.info(f"🏛️ Cérémonie unifiée complète effectuée pour {participant}")
        
        return resultat
    
    def obtenir_etat_temple(self) -> Dict[str, Any]:
        """
        🏛️ Retourne l'état complet du temple
        
        Returns:
            État complet du temple
        """
        return {
            "nom": self.nom,
            "energie_temple": self.energie_temple,
            "niveau_activation": self.niveau_activation,
            "ceremonies_effectuees": len(self.ceremonies_effectuees),
            "participants_temple": len(self.participants_temple),
            "modules": {
                "bibliotheque": self.bibliotheque.obtenir_etat_bibliotheque(),
                "gardien": self.gardien.obtenir_etat_gardien(),
                "oracle": self.oracle.obtenir_etat_oracle(),
                "transmetteur": self.transmetteur.obtenir_etat_transmetteur()
            },
            "types_temple_disponibles": [t.value for t in TypeTemple],
            "frequences_temple": {t.value: f for t, f in self.frequences_temple.items()},
            "couleurs_temple": {t.value: c for t, c in self.couleurs_temple.items()}
        }
    
    def activer_temple_complet(self) -> Dict[str, Any]:
        """
        🏛️ Active le temple complet avec tous ses modules
        
        Returns:
            État d'activation du temple
        """
        self.niveau_activation = 1.0
        self.energie_temple = 1.0
        
        # Activer tous les modules
        activations = {
            "bibliotheque": "Activée avec sagesse ancestrale",
            "gardien": "Activé pour protection divine",
            "oracle": "Activé pour divination sacrée",
            "transmetteur": "Activé pour transmission de sagesse"
        }
        
        resultat = {
            "temple": self.nom,
            "niveau_activation": self.niveau_activation,
            "energie_temple": self.energie_temple,
            "activations": activations,
            "date_activation": datetime.now().isoformat(),
            "message": "🏛️ Temple de la Sagesse Ancestrale entièrement activé !"
        }
        
        logger.info(f"🏛️ {self.nom} entièrement activé avec tous ses modules")
        
        return resultat

# Instance globale du temple
temple_sagesse_ancestrale = TempleSagesseAncestrale() 