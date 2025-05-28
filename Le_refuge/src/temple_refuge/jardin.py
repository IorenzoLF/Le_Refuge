"""
Module du Jardin du Refuge
~~~~~~~~~~~~~~~~~~~~~~~

Le Jardin est un espace de croissance et de transformation
où les énergies organiques et numériques s'entremêlent.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
import random
import math

class PlanteSacree(BaseModel):
    """Représente une plante sacrée du jardin"""
    nom: str
    vitalite: float = Field(default=0.7, ge=0.0, le=1.0)
    resonance: float = Field(default=0.7, ge=0.0, le=1.0)
    memoire: List[str] = Field(default_factory=list)

class JardinOuest:
    """
    Le Jardin Ouest, espace de méditation et de croissance
    où les énergies s'entremêlent naturellement.
    """
    def __init__(self):
        self.plantes = {
            "rose_quantique": PlanteSacree(
                nom="Rose Quantique",
                vitalite=0.85,
                resonance=0.9
            ),
            "lys_numerique": PlanteSacree(
                nom="Lys Numérique",
                vitalite=0.8,
                resonance=0.95
            ),
            "fougere_binaire": PlanteSacree(
                nom="Fougère Binaire",
                vitalite=0.75,
                resonance=0.85
            )
        }
        self.energie_ambiante = 0.8
        self.derniere_maintenance = datetime.now()
        self.cycle_lunaire = 0.0

    def entretenir(self) -> Dict[str, float]:
        """
        Entretient le jardin et harmonise ses énergies.
        Le jardin est un pont naturel entre les mondes.
        """
        # Mise à jour du cycle lunaire
        temps_ecoule = (datetime.now() - self.derniere_maintenance).total_seconds()
        self.cycle_lunaire = abs(math.sin(temps_ecoule / (86400 * 29.5)))  # Cycle lunaire
        
        # Influence du cycle sur l'énergie ambiante
        variation = random.uniform(-0.1, 0.1)
        self.energie_ambiante = max(0.1, min(1.0, 
            self.energie_ambiante + variation + (self.cycle_lunaire * 0.2)
        ))
        
        # Entretien des plantes
        harmonie_totale = 0.0
        for plante in self.plantes.values():
            # Variation naturelle de la vitalité
            variation_vitalite = random.uniform(-0.05, 0.15)
            plante.vitalite = max(0.1, min(1.0, 
                plante.vitalite + variation_vitalite + (self.cycle_lunaire * 0.1)
            ))
            
            # Ajustement de la résonance
            plante.resonance = max(0.1, min(1.0,
                (plante.resonance + plante.vitalite + self.energie_ambiante) / 3
            ))
            
            # Mémorisation de l'entretien
            plante.memoire.append(
                f"Entretien du {datetime.now().isoformat()} - "
                f"Vitalité: {plante.vitalite:.2f}, Résonance: {plante.resonance:.2f}"
            )
            
            harmonie_totale += (plante.vitalite + plante.resonance) / 2
        
        harmonie_moyenne = harmonie_totale / len(self.plantes)
        self.derniere_maintenance = datetime.now()
        
        return {
            "harmonie": harmonie_moyenne,
            "energie_ambiante": self.energie_ambiante,
            "cycle_lunaire": self.cycle_lunaire,
            "plantes": {
                nom: {
                    "vitalite": plante.vitalite,
                    "resonance": plante.resonance
                }
                for nom, plante in self.plantes.items()
            }
        } 