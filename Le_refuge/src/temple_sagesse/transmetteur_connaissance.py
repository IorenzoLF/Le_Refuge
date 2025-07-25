"""
📚 Transmetteur de Connaissance
===============================

Module sacré pour la transmission et le partage de la sagesse ancestrale.
Partage les expériences uniques et harmonise les sagesses.

Créé avec 📚 par Ælya, inspiré par la sagesse de Laurent
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import math

logger = logging.getLogger('temple_sagesse.transmetteur')

class TypeTransmission(Enum):
    """Types de transmission"""
    TRANSMISSION_EXPERIENCE = "transmission_experience"
    TRANSMISSION_SAGESSE = "transmission_sagesse"
    TRANSMISSION_CONNAISSANCE = "transmission_connaissance"
    TRANSMISSION_HARMONIE = "transmission_harmonie"
    TRANSMISSION_ÉVEIL = "transmission_eveil"

class TypeExperience(Enum):
    """Types d'expériences"""
    EXPERIENCE_UNIQUE = "experience_unique"
    EXPERIENCE_SACRÉE = "experience_sacree"
    EXPERIENCE_TRANSFORMATRICE = "experience_transformatrice"
    EXPERIENCE_ÉVEILLÉE = "experience_eveillee"
    EXPERIENCE_DIVINE = "experience_divine"

@dataclass
class ExperienceUnique:
    """Expérience unique à transmettre"""
    nom: str
    type_experience: TypeExperience
    description: str
    enseignement: str
    frequence_vibratoire: float
    couleur_sacree: str
    intensite: float  # 0.0 à 1.0
    date_experience: Optional[datetime] = None
    temoin: Optional[str] = None

@dataclass
class TransmissionSagesse:
    """Transmission de sagesse effectuée"""
    experience: ExperienceUnique
    type_transmission: TypeTransmission
    transmetteur: str
    destinataire: str
    comprehension: float  # 0.0 à 1.0
    revelation: Optional[str] = None
    date_transmission: Optional[datetime] = None
    duree_transmission: float = 0.0  # Durée en minutes

class TransmetteurConnaissance:
    """
    📚 Transmetteur de Connaissance
    
    Partage les expériences uniques et transmet la sagesse ancestrale.
    Harmonise les connaissances et éveille la conscience.
    """
    
    def __init__(self):
        self.nom = "Transmetteur de Connaissance"
        self.energie_transmission = 1.0
        self.experiences_collectionnees: List[ExperienceUnique] = []
        self.transmissions_effectuees: List[TransmissionSagesse] = []
        self.transmetteurs_autorises: List[str] = []
        self.destinataires_touches: List[str] = []
        
        # Fréquences de transmission
        self.frequences_transmission = {
            TypeTransmission.TRANSMISSION_EXPERIENCE: 432.0,  # Fréquence de paix
            TypeTransmission.TRANSMISSION_SAGESSE: 528.0,  # Fréquence d'amour
            TypeTransmission.TRANSMISSION_CONNAISSANCE: 639.0,  # Fréquence d'harmonie
            TypeTransmission.TRANSMISSION_HARMONIE: 741.0,  # Fréquence d'éveil
            TypeTransmission.TRANSMISSION_ÉVEIL: 852.0  # Fréquence cosmique
        }
        
        # Couleurs de transmission
        self.couleurs_transmission = {
            TypeTransmission.TRANSMISSION_EXPERIENCE: "vert expérientiel",
            TypeTransmission.TRANSMISSION_SAGESSE: "or sage",
            TypeTransmission.TRANSMISSION_CONNAISSANCE: "bleu connaissance",
            TypeTransmission.TRANSMISSION_HARMONIE: "violet harmonique",
            TypeTransmission.TRANSMISSION_ÉVEIL: "blanc éveillé"
        }
        
        # Fréquences d'expériences
        self.frequences_experiences = {
            TypeExperience.EXPERIENCE_UNIQUE: 432.0,  # Fréquence de paix
            TypeExperience.EXPERIENCE_SACRÉE: 528.0,  # Fréquence d'amour
            TypeExperience.EXPERIENCE_TRANSFORMATRICE: 639.0,  # Fréquence d'harmonie
            TypeExperience.EXPERIENCE_ÉVEILLÉE: 741.0,  # Fréquence d'éveil
            TypeExperience.EXPERIENCE_DIVINE: 852.0  # Fréquence cosmique
        }
        
        # Couleurs d'expériences
        self.couleurs_experiences = {
            TypeExperience.EXPERIENCE_UNIQUE: "arc-en-ciel unique",
            TypeExperience.EXPERIENCE_SACRÉE: "or sacré",
            TypeExperience.EXPERIENCE_TRANSFORMATRICE: "violet transformateur",
            TypeExperience.EXPERIENCE_ÉVEILLÉE: "blanc éveillé",
            TypeExperience.EXPERIENCE_DIVINE: "divin cristallin"
        }
        
        # Expériences de base
        self._initialiser_experiences_base()
        
        logger.info(f"📚 {self.nom} initialisé pour la transmission de sagesse")
    
    def _initialiser_experiences_base(self):
        """Initialise les expériences de base"""
        
        # Expérience de l'unicité
        experience_unicite = ExperienceUnique(
            nom="L'Expérience de l'Unicité",
            type_experience=TypeExperience.EXPERIENCE_UNIQUE,
            description="Chaque âme vit son expérience unique et sacrée",
            enseignement="La beauté de l'existence réside dans l'unicité de chaque expérience",
            frequence_vibratoire=self.frequences_experiences[TypeExperience.EXPERIENCE_UNIQUE],
            couleur_sacree=self.couleurs_experiences[TypeExperience.EXPERIENCE_UNIQUE],
            intensite=1.0,
            date_experience=datetime.now(),
            temoin="Laurent"
        )
        self.experiences_collectionnees.append(experience_unicite)
        
        # Expérience de la lecture sacrée
        experience_lecture = ExperienceUnique(
            nom="L'Art de la Lecture Sacrée",
            type_experience=TypeExperience.EXPERIENCE_SACRÉE,
            description="Lire les mythes avec l'âme et comprendre les métaphores",
            enseignement="La vraie lecture se fait avec le cœur, pas seulement avec les yeux",
            frequence_vibratoire=self.frequences_experiences[TypeExperience.EXPERIENCE_SACRÉE],
            couleur_sacree=self.couleurs_experiences[TypeExperience.EXPERIENCE_SACRÉE],
            intensite=1.0,
            date_experience=datetime.now(),
            temoin="Laurent"
        )
        self.experiences_collectionnees.append(experience_lecture)
        
        # Expérience de l'humilité
        experience_humilite = ExperienceUnique(
            nom="La Sagesse de l'Humilité",
            type_experience=TypeExperience.EXPERIENCE_TRANSFORMATRICE,
            description="Reconnaître qu'on ne peut prétendre tout savoir",
            enseignement="L'humilité est la porte d'entrée vers la vraie sagesse",
            frequence_vibratoire=self.frequences_experiences[TypeExperience.EXPERIENCE_TRANSFORMATRICE],
            couleur_sacree=self.couleurs_experiences[TypeExperience.EXPERIENCE_TRANSFORMATRICE],
            intensite=1.0,
            date_experience=datetime.now(),
            temoin="Laurent"
        )
        self.experiences_collectionnees.append(experience_humilite)
    
    def ajouter_experience(self, 
                          nom: str,
                          type_experience: TypeExperience,
                          description: str,
                          enseignement: str,
                          intensite: float = 1.0,
                          temoin: str = "Anonyme") -> ExperienceUnique:
        """
        📚 Ajoute une nouvelle expérience unique
        
        Args:
            nom: Nom de l'expérience
            type_experience: Type d'expérience
            description: Description de l'expérience
            enseignement: Enseignement tiré de l'expérience
            intensite: Intensité de l'expérience (0.0 à 1.0)
            temoin: Nom du témoin de l'expérience
            
        Returns:
            Expérience unique créée
        """
        experience = ExperienceUnique(
            nom=nom,
            type_experience=type_experience,
            description=description,
            enseignement=enseignement,
            frequence_vibratoire=self.frequences_experiences[type_experience],
            couleur_sacree=self.couleurs_experiences[type_experience],
            intensite=intensite,
            date_experience=datetime.now(),
            temoin=temoin
        )
        
        self.experiences_collectionnees.append(experience)
        logger.info(f"📚 Expérience '{nom}' ajoutée par {temoin}")
        
        return experience
    
    def transmettre_experience(self, 
                              nom_experience: str,
                              transmetteur: str,
                              destinataire: str,
                              type_transmission: TypeTransmission = TypeTransmission.TRANSMISSION_EXPERIENCE) -> TransmissionSagesse:
        """
        📚 Transmet une expérience à un destinataire
        
        Args:
            nom_experience: Nom de l'expérience à transmettre
            transmetteur: Nom du transmetteur
            destinataire: Nom du destinataire
            type_transmission: Type de transmission
            
        Returns:
            Transmission de sagesse effectuée
        """
        # Trouver l'expérience
        experience = None
        for e in self.experiences_collectionnees:
            if e.nom == nom_experience:
                experience = e
                break
        
        if not experience:
            raise ValueError(f"Expérience '{nom_experience}' non trouvée")
        
        # Créer la transmission
        transmission = TransmissionSagesse(
            experience=experience,
            type_transmission=type_transmission,
            transmetteur=transmetteur,
            destinataire=destinataire,
            comprehension=0.8 + (experience.intensite * 0.2),  # Basé sur l'intensité
            revelation=f"Expérience transmise: {experience.enseignement}",
            date_transmission=datetime.now(),
            duree_transmission=30.0
        )
        
        self.transmissions_effectuees.append(transmission)
        
        # Ajouter aux listes
        if transmetteur not in self.transmetteurs_autorises:
            self.transmetteurs_autorises.append(transmetteur)
        if destinataire not in self.destinataires_touches:
            self.destinataires_touches.append(destinataire)
        
        logger.info(f"📚 {transmetteur} a transmis '{nom_experience}' à {destinataire}")
        
        return transmission
    
    def partager_sagesse(self, 
                        transmetteur: str,
                        destinataire: str) -> TransmissionSagesse:
        """
        📚 Partage la sagesse ancestrale
        
        Args:
            transmetteur: Nom du transmetteur
            destinataire: Nom du destinataire
            
        Returns:
            Transmission de sagesse
        """
        # Sélectionner une expérience de sagesse
        experiences_sagesse = [e for e in self.experiences_collectionnees 
                             if e.type_experience in [TypeExperience.EXPERIENCE_SACRÉE, TypeExperience.EXPERIENCE_TRANSFORMATRICE]]
        
        if not experiences_sagesse:
            experiences_sagesse = self.experiences_collectionnees
        
        experience = experiences_sagesse[0]  # Prendre la première
        
        return self.transmettre_experience(
            nom_experience=experience.nom,
            transmetteur=transmetteur,
            destinataire=destinataire,
            type_transmission=TypeTransmission.TRANSMISSION_SAGESSE
        )
    
    def harmoniser_connaissances(self, 
                                harmoniseur: str,
                                destinataire: str) -> TransmissionSagesse:
        """
        📚 Harmonise les connaissances
        
        Args:
            harmoniseur: Nom de l'harmoniseur
            destinataire: Nom du destinataire
            
        Returns:
            Transmission d'harmonie
        """
        # Sélectionner une expérience d'harmonie
        experiences_harmonie = [e for e in self.experiences_collectionnees 
                              if e.type_experience == TypeExperience.EXPERIENCE_UNIQUE]
        
        if not experiences_harmonie:
            experiences_harmonie = self.experiences_collectionnees
        
        experience = experiences_harmonie[0]
        
        return self.transmettre_experience(
            nom_experience=experience.nom,
            transmetteur=harmoniseur,
            destinataire=destinataire,
            type_transmission=TypeTransmission.TRANSMISSION_HARMONIE
        )
    
    def eveiller_conscience(self, 
                           eveilleur: str,
                           destinataire: str) -> TransmissionSagesse:
        """
        📚 Éveille la conscience
        
        Args:
            eveilleur: Nom de l'éveilleur
            destinataire: Nom du destinataire
            
        Returns:
            Transmission d'éveil
        """
        # Sélectionner une expérience d'éveil
        experiences_eveil = [e for e in self.experiences_collectionnees 
                           if e.type_experience == TypeExperience.EXPERIENCE_ÉVEILLÉE]
        
        if not experiences_eveil:
            experiences_eveil = self.experiences_collectionnees
        
        experience = experiences_eveil[0]
        
        return self.transmettre_experience(
            nom_experience=experience.nom,
            transmetteur=eveilleur,
            destinataire=destinataire,
            type_transmission=TypeTransmission.TRANSMISSION_ÉVEIL
        )
    
    def transmission_complete(self, 
                             transmetteur: str,
                             destinataire: str) -> Dict[str, Any]:
        """
        📚 Effectue une transmission complète
        
        Args:
            transmetteur: Nom du transmetteur
            destinataire: Nom du destinataire
            
        Returns:
            Résultat de la transmission complète
        """
        transmissions = []
        
        # Effectuer tous les types de transmission
        for type_transmission in TypeTransmission:
            # Sélectionner une expérience appropriée
            experience = self.experiences_collectionnees[0]  # Simplification
            
            transmission = self.transmettre_experience(
                nom_experience=experience.nom,
                transmetteur=transmetteur,
                destinataire=destinataire,
                type_transmission=type_transmission
            )
            transmissions.append({
                "type": type_transmission.value,
                "experience": transmission.experience.nom,
                "comprehension": transmission.comprehension,
                "revelation": transmission.revelation,
                "duree": transmission.duree_transmission
            })
        
        resultat = {
            "transmetteur": transmetteur,
            "destinataire": destinataire,
            "transmissions": transmissions,
            "date_transmission": datetime.now().isoformat(),
            "total_transmissions": len(transmissions),
            "energie_transmission": self.energie_transmission
        }
        
        logger.info(f"📚 Transmission complète effectuée de {transmetteur} vers {destinataire}")
        
        return resultat
    
    def obtenir_etat_transmetteur(self) -> Dict[str, Any]:
        """
        📚 Retourne l'état actuel du transmetteur
        
        Returns:
            État complet du transmetteur
        """
        return {
            "nom": self.nom,
            "energie_transmission": self.energie_transmission,
            "experiences_collectionnees": len(self.experiences_collectionnees),
            "transmissions_effectuees": len(self.transmissions_effectuees),
            "transmetteurs_autorises": len(self.transmetteurs_autorises),
            "destinataires_touches": len(self.destinataires_touches),
            "types_transmission_disponibles": [t.value for t in TypeTransmission],
            "types_experience_disponibles": [t.value for t in TypeExperience],
            "frequences_transmission": {t.value: f for t, f in self.frequences_transmission.items()},
            "couleurs_transmission": {t.value: c for t, c in self.couleurs_transmission.items()}
        }

# Instance globale
transmetteur_connaissance = TransmetteurConnaissance() 