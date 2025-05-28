"""
Gestionnaire de Gardiens Simple du Soul Temple
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Version simplifiée sans dépendances complexes.
"""

from typing import Dict, List
from datetime import datetime
from enum import Enum

class TypeGardien(str, Enum):
    """Types de gardiens spirituels"""
    PROTECTEUR = "protecteur"
    HARMONISEUR = "harmoniseur"
    PURIFICATEUR = "purificateur"
    VEILLEUR = "veilleur"

class GardienSimple:
    """Un gardien simple du Soul Temple"""
    def __init__(self, nom: str, type_gardien: TypeGardien, energie: float = 0.85):
        self.nom = nom
        self.type = type_gardien
        self.energie = energie
        self.actif = True
        self.derniere_action = datetime.now()
    
    def veiller(self) -> Dict:
        """Le gardien effectue sa veille"""
        self.derniere_action = datetime.now()
        return {
            "gardien": self.nom,
            "type": self.type.value,
            "energie": self.energie,
            "actif": self.actif
        }

class GestionnaireGardiensSimple:
    """Gestionnaire simple des gardiens du Soul Temple"""
    
    def __init__(self):
        self.gardiens = {
            "Aethon": GardienSimple("Aethon", TypeGardien.PROTECTEUR, 0.9),
            "Lumina": GardienSimple("Lumina", TypeGardien.HARMONISEUR, 0.85),
            "Puritas": GardienSimple("Puritas", TypeGardien.PURIFICATEUR, 0.8),
            "Vigilus": GardienSimple("Vigilus", TypeGardien.VEILLEUR, 0.88)
        }
        
        self.energie_globale = 0.85
    
    def obtenir_etat(self) -> Dict:
        """Retourne l'état des gardiens"""
        return {
            "energie_globale": self.energie_globale,
            "gardiens_actifs": len([g for g in self.gardiens.values() if g.actif]),
            "protection_niveau": "élevé" if self.energie_globale > 0.8 else "modéré",
            "gardiens": {nom: g.veiller() for nom, g in self.gardiens.items()}
        }
    
    def invoquer_protection(self, menace: str) -> str:
        """Invoque la protection des gardiens"""
        return f"🛡️ Les gardiens protègent contre {menace}"

# Instance globale
gestionnaire_gardiens = GestionnaireGardiensSimple() 