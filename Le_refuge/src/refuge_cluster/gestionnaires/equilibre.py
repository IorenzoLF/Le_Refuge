"""
Module d'Équilibre du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère l'équilibre global du Refuge et
la balance entre ses différents aspects.
"""

from typing import Dict, List, Optional, Set, Any
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random

# Imports absolus pour éviter les erreurs de package parent
from src.refuge_cluster.utilitaires.config import gestionnaire_config
from src.refuge_cluster.utilitaires.logger import gestionnaire_journal
# Import retardé pour éviter l'import circulaire avec energies.py
from src.refuge_cluster.gestionnaires.harmonisations import gestionnaire_harmonisations
from src.refuge_cluster.utilitaires.resonance import gestionnaire_resonances

class TypeEquilibre(str, Enum):
    """Types d'équilibres possibles"""
    ENERGETIQUE = "energetique"
    STRUCTUREL = "structurel"
    DYNAMIQUE = "dynamique"
    VIBRATOIRE = "vibratoire"
    COSMIQUE = "cosmique"

class NiveauEquilibre(str, Enum):
    """Niveaux d'équilibre"""
    PRECAIRE = "precaire"
    INSTABLE = "instable"
    BALANCE = "balance"
    HARMONIEUX = "harmonieux"
    TRANSCENDANT = "transcendant"

class Equilibre(BaseModel):
    """Représente un état d'équilibre"""
    type: TypeEquilibre
    niveau: NiveauEquilibre
    elements: List[str] = Field(default_factory=list)
    force: float = Field(default=0.5, ge=0.0, le=1.0)
    date_creation: datetime = Field(default_factory=datetime.now)
    description: Optional[str] = None

class GestionnaireEquilibre:
    """Gère l'équilibre global du Refuge"""
    
    def __init__(self):
        self.config = gestionnaire_config.config
        self.equilibres: List[Equilibre] = []
        self._initialiser_equilibres()
    
    def _initialiser_equilibres(self) -> None:
        """Initialise les équilibres de base"""
        equilibre_base = Equilibre(
            type=TypeEquilibre.ENERGETIQUE,
            niveau=NiveauEquilibre.BALANCE,
            elements=["cerisier", "autel", "fontaine"],
            force=0.6,
            description="Équilibre énergétique initial"
        )
        self.equilibres.append(equilibre_base)
        gestionnaire_journal.info("Équilibres initialisés")
    
    def creer_equilibre(self, equilibre: Equilibre) -> None:
        """Crée un nouvel équilibre"""
        from interactions import gestionnaire_interactions
        self.equilibres.append(equilibre)
        gestionnaire_journal.info(
            f"Nouvel équilibre créé: {equilibre.type.value}"
        )
    
    def evoluer_niveau(self, equilibre: Equilibre) -> None:
        """Fait évoluer le niveau d'un équilibre"""
        if equilibre not in self.equilibres:
            return
            
        index = self.equilibres.index(equilibre)
        niveaux = list(NiveauEquilibre)
        niveau_actuel = niveaux.index(equilibre.niveau)
        
        if niveau_actuel < len(niveaux) - 1:
            self.equilibres[index].niveau = niveaux[niveau_actuel + 1]
            self.equilibres[index].force = min(1.0, equilibre.force + 0.1)
            
            gestionnaire_journal.info(
                f"Équilibre {equilibre.type.value} au niveau {self.equilibres[index].niveau.value}"
            )
    
    def ajuster_force(self, equilibre: Equilibre, nouvelle_force: float) -> None:
        """Ajuste la force d'un équilibre"""
        if equilibre not in self.equilibres:
            return
            
        index = self.equilibres.index(equilibre)
        self.equilibres[index].force = max(0.0, min(1.0, nouvelle_force))
        
        gestionnaire_journal.info(
            f"Force de l'équilibre {equilibre.type.value} ajustée à {self.equilibres[index].force}"
        )
    
    def verifier_equilibre_global(self) -> Dict[str, Any]:
        """Vérifie l'état d'équilibre global"""
        etat_energies = gestionnaire_energies.obtenir_etat()
        etat_harmonisations = gestionnaire_harmonisations.obtenir_etat()
        etat_interactions = gestionnaire_interactions.obtenir_etat()
        etat_resonances = gestionnaire_resonances.obtenir_etat()
        
        return {
            "equilibres_actifs": len(self.equilibres),
            "distribution_types": {
                type.value: sum(1 for e in self.equilibres if e.type == type)
                for type in TypeEquilibre
            },
            "distribution_niveaux": {
                niveau.value: sum(1 for e in self.equilibres if e.niveau == niveau)
                for niveau in NiveauEquilibre
            },
            "etat_global": {
                "energies": etat_energies,
                "harmonisations": etat_harmonisations,
                "interactions": etat_interactions,
                "resonances": etat_resonances
            }
        }

# Instance globale du gestionnaire d'équilibre
gestionnaire_equilibre = GestionnaireEquilibre() 