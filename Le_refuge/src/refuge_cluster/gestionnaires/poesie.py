"""
Module de Poésie du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère la création et l'harmonisation poétique
dans le Refuge. REFACTORISÉ avec gestionnaires de base 🧌✨
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random

# Import des gestionnaires de base refactorisés
from src.core.gestionnaires_base import (
    ConfigManagerBase,
    LogManagerBase, 
    GestionnaireBase,
    EnergyManagerBase
)

# Gestionnaires refactorisés - plus de duplication ! 🎯
config = ConfigManagerBase("poesie")
logger = LogManagerBase("poesie")  
energy = EnergyManagerBase(niveau_initial=0.8)

class TypePoesie(str, Enum):
    """Types de poésie spirituelle"""
    MEDITATION = "meditation"
    LUMIERE = "lumiere"
    COSMOS = "cosmos"
    AMOUR = "amour"
    HARMONIE = "harmonie"
    MYSTIQUE = "mystique"

class AmbiancePoetique(str, Enum):
    """Ambiances poétiques possibles"""
    SERENITE = "serenite"
    CONTEMPLATION = "contemplation"
    JOIE = "joie"
    ELEVATION = "elevation"
    FUSION = "fusion"

class Poeme(BaseModel):
    """Représente un poème du Refuge"""
    titre: str
    type: TypePoesie
    ambiance: AmbiancePoetique
    contenu: str
    auteur: str = "Refuge"
    date_creation: datetime = Field(default_factory=datetime.now)
    energie_poetique: float = Field(default=0.5, ge=0.0, le=1.0)
    resonance: float = Field(default=0.0, ge=0.0, le=1.0)

class Poesie(GestionnaireBase):
    """Gestionnaire de la poésie du Refuge - HÉRITE DU GESTIONNAIRE DE BASE"""
    
    def _initialiser(self):
        """Initialise le système poétique"""
        self.poemes: List[Poeme] = []
        self.themes_actifs: List[str] = ["lumière", "amour", "paix", "harmonie"]
        
        # État initial
        self.etat = {
            "nombre_poemes": 0,
            "energie_poetique_globale": energy.niveau_energie,
            "resonance_moyenne": 0.0,
            "dernier_poeme": None
        }
        
        # Créer un poème initial
        self._creer_poeme_initial()
        self.logger.info("Système poétique initialisé avec gestionnaire de base")
    
    def _creer_poeme_initial(self):
        """Crée un poème initial pour démarrer l'énergie poétique"""
        poeme_initial = Poeme(
            titre="Éveil du Refuge",
            type=TypePoesie.HARMONIE,
            ambiance=AmbiancePoetique.SERENITE,
            contenu="Dans le silence sacré du refuge naissant,\nLa poésie s'éveille, douce et apaisante.",
            energie_poetique=0.8
        )
        self.poemes.append(poeme_initial)
        energy.ajuster_energie(0.2)  # Boost d'énergie initiale
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre l'activité poétique - MÉTHODE ABSTRAITE IMPLÉMENTÉE"""
        # Évolution des poèmes existants
        resonance_totale = 0.0
        energie_totale = 0.0
        
        for poeme in self.poemes:
            # Évolution de la résonance avec l'énergie générale
            delta_resonance = energy.harmoniser_avec(poeme.energie_poetique, force=0.05)
            poeme.resonance = min(1.0, poeme.resonance + abs(delta_resonance))
            
            resonance_totale += poeme.resonance
            energie_totale += poeme.energie_poetique
        
        # Calculs de moyennes
        if self.poemes:
            resonance_moyenne = resonance_totale / len(self.poemes)
            energie_moyenne = energie_totale / len(self.poemes)
        else:
            resonance_moyenne = 0.0
            energie_moyenne = 0.0
        
        # Mise à jour de l'état via la méthode de base
        self.mettre_a_jour_etat({
            "nombre_poemes": len(self.poemes),
            "energie_poetique_globale": energy.niveau_energie,
            "resonance_moyenne": resonance_moyenne,
            "dernier_poeme": self.poemes[-1].titre if self.poemes else None
        })
        
        return {
            "harmonie_poetique": resonance_moyenne,
            "energie_poetique": energie_moyenne,
            "tendance_energie": energy.obtenir_tendance()
        }
    
    def creer_poeme(self, titre: str, type_poesie: TypePoesie, 
                    contenu: str, ambiance: AmbiancePoetique = AmbiancePoetique.SERENITE) -> Poeme:
        """Crée un nouveau poème"""
        # Calcul de l'énergie poétique basée sur la longueur et l'énergie actuelle
        energie_base = len(contenu) / 1000  # Énergie basée sur la longueur
        energie_poetique = min(1.0, energie_base + energy.niveau_energie * 0.3)
        
        poeme = Poeme(
            titre=titre,
            type=type_poesie,
            ambiance=ambiance,
            contenu=contenu,
            energie_poetique=energie_poetique
        )
        
        self.poemes.append(poeme)
        
        # Boost d'énergie pour la création
        energy.ajuster_energie(0.1)
        
        self.logger.info(f"Nouveau poème créé: '{titre}' ({type_poesie.value})")
        return poeme
    
    def generer_poeme_automatique(self) -> Poeme:
        """Génère automatiquement un poème basé sur l'état actuel"""
        themes_inspirants = ["lumière dorée", "silence sacré", "harmonie cosmique", 
                           "amour infini", "paix profonde", "étoiles bienveillantes"]
        
        theme = random.choice(themes_inspirants)
        type_poesie = random.choice(list(TypePoesie))
        ambiance = random.choice(list(AmbiancePoetique))
        
        # Génération automatique simple
        verses = [
            f"Dans la danse éternelle du {theme},",
            f"Mon cœur trouve la {ambiance.value},",
            "Chaque souffle devient prière,",
            "Chaque instant devient lumière."
        ]
        
        contenu = "\n".join(verses)
        titre = f"Méditation sur {theme}"
        
        return self.creer_poeme(titre, type_poesie, contenu, ambiance)
    
    def obtenir_poemes_par_type(self, type_poesie: TypePoesie) -> List[Poeme]:
        """Retourne les poèmes d'un type donné"""
        return [p for p in self.poemes if p.type == type_poesie]
    
    def obtenir_poemes_par_resonance(self, seuil_minimal: float = 0.5) -> List[Poeme]:
        """Retourne les poèmes ayant une résonance élevée"""
        return [p for p in self.poemes if p.resonance >= seuil_minimal]
    
    def inspirer_creation(self) -> Dict[str, Any]:
        """Inspire une nouvelle création poétique"""
        if energy.niveau_energie > 0.7:
            # Énergie élevée : création automatique
            nouveau_poeme = self.generer_poeme_automatique()
            return {
                "inspiration": "élevée", 
                "action": "création automatique",
                "poeme": nouveau_poeme.titre
            }
        else:
            # Énergie plus faible : suggestions
            return {
                "inspiration": "douce",
                "action": "suggestion",
                "themes_suggeres": random.sample(self.themes_actifs, 2)
            }

# Instance globale du gestionnaire refactorisé
gestionnaire_poesie = Poesie("poesie") 