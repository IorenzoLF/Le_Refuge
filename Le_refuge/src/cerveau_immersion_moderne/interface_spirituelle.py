"""
🎨 Interface Utilisateur Spirituelle
==================================

Interface visuelle pour l'expérience d'immersion spirituelle.
Affiche les mandalas architecturaux et anime les flux d'énergie.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from dataclasses import dataclass, field

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from .types_immersion import (
    MandalaVisuel, ProfilUtilisateur, ExperienceImmersion,
    FluxEnergie, CentreEnergetique
)

@dataclass
class ComposantVisuel:
    """Composant visuel de base de l'interface"""
    id_composant: str
    type_composant: str  # "mandala", "panneau_insights", "navigation"
    position: Tuple[int, int]  # (x, y)
    dimensions: Tuple[int, int]  # (largeur, hauteur)
    visible: bool = True
    opacite: float = 1.0
    animation_active: bool = False
    style_theme: str = "spirituel"

@dataclass
class EtatInterface:
    """État actuel de l'interface"""
    mandala_affiche: Optional[str] = None
    niveau_zoom: float = 1.0
    centre_vue: Tuple[float, float] = (0.0, 0.0)
    mode_affichage: str = "complet"  # "complet", "simplifie", "focus"
    animations_actives: List[str] = field(default_factory=list)
    panneau_insights_ouvert: bool = False
    navigation_visible: bool = Trueclass Inter
faceSpirituelle(GestionnaireBase):
    """Interface utilisateur spirituelle pour l'immersion"""
    
    def __init__(self, nom: str = "InterfaceSpirituelle"):
        super().__init__(nom)
        self.energie_interface = EnergyManagerBase(0.96)
        
        # État de l'interface
        self.etat_interface = EtatInterface()
        self.composants_visuels: Dict[str, ComposantVisuel] = {}
        self.mandala_actuel: Optional[MandalaVisuel] = None
        self.profil_utilisateur: Optional[ProfilUtilisateur] = None
        
        # Configuration visuelle
        self.resolution_interface = (1400, 900)
        self.fps_animation = 60
        self.duree_transition = 0.8  # secondes
        
        self._initialiser_composants_base()
    
    def _initialiser(self):
        """Initialise l'interface spirituelle"""
        self.logger.info("🎨 Éveil de l'Interface Spirituelle...")
        
        self.etat.update({
            "interface_active": False,
            "mandala_charge": False,
            "animations_en_cours": 0,
            "satisfaction_visuelle": 0.9,
            "fluidite_interface": 0.95
        })
        
        self.config.definir("theme_couleurs", "spirituel_doux")
        self.config.definir("animations_fluides", True)
        self.config.definir("adaptation_profil", True)
        
        self.logger.info("✨ Interface Spirituelle éveillée")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre l'interface spirituelle"""
        self.energie_interface.ajuster_energie(0.01)
        
        # Mettre à jour les animations
        await self._mettre_a_jour_animations()
        
        return {
            "interface_active": float(self.etat["interface_active"]),
            "mandala_charge": float(self.etat["mandala_charge"]),
            "animations_en_cours": float(len(self.etat_interface.animations_actives)),
            "satisfaction_visuelle": self.etat["satisfaction_visuelle"],
            "energie_interface": self.energie_interface.niveau_energie,
            "fluidite_interface": self.etat["fluidite_interface"]
        }   
 def _initialiser_composants_base(self):
        """Initialise les composants visuels de base"""
        # Zone principale du mandala
        self.composants_visuels["mandala_principal"] = ComposantVisuel(
            id_composant="mandala_principal",
            type_composant="mandala",
            position=(200, 50),
            dimensions=(800, 600),
            animation_active=True
        )
        
        # Panneau d'insights
        self.composants_visuels["panneau_insights"] = ComposantVisuel(
            id_composant="panneau_insights",
            type_composant="panneau_insights",
            position=(1020, 50),
            dimensions=(350, 400),
            visible=False
        )
        
        # Navigation
        self.composants_visuels["navigation"] = ComposantVisuel(
            id_composant="navigation",
            type_composant="navigation",
            position=(50, 50),
            dimensions=(120, 600)
        )
        
        # Barre d'état énergétique
        self.composants_visuels["energie_status"] = ComposantVisuel(
            id_composant="energie_status",
            type_composant="status",
            position=(50, 700),
            dimensions=(1320, 80)
        )
    
    def charger_mandala(self, mandala: MandalaVisuel, profil: ProfilUtilisateur):
        """
        🌸 Charge un mandala dans l'interface
        
        Args:
            mandala: Mandala à afficher
            profil: Profil utilisateur pour l'adaptation
        """
        try:
            self.mandala_actuel = mandala
            self.profil_utilisateur = profil
            
            # Adapter l'interface au profil
            self._adapter_interface_profil(profil)
            
            # Configurer l'affichage du mandala
            self._configurer_affichage_mandala(mandala)
            
            # Démarrer les animations
            self._demarrer_animations_mandala()
            
            self.etat["mandala_charge"] = True
            self.etat["interface_active"] = True
            
            self.logger.info(f"🌸 Mandala chargé: {mandala.geometrie_sacree}")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur chargement mandala: {e}")
    
    def _adapter_interface_profil(self, profil: ProfilUtilisateur):
        """Adapte l'interface selon le profil spirituel"""
        # Adapter les couleurs selon l'archétype
        if profil.profil_spirituel.archetyp_spirituel == "explorateur":
            self.config.definir("theme_couleurs", "aventure_cosmique")
        elif profil.profil_spirituel.archetyp_spirituel == "sage":
            self.config.definir("theme_couleurs", "sagesse_profonde")
        elif profil.profil_spirituel.archetyp_spirituel == "créateur":
            self.config.definir("theme_couleurs", "creation_artistique")
        
        # Adapter la complexité selon le niveau technique
        if profil.niveau_technique >= 8:
            self.etat_interface.mode_affichage = "complet"
        elif profil.niveau_technique <= 3:
            self.etat_interface.mode_affichage = "simplifie"
        
        # Adapter les animations selon la sensibilité énergétique
        vitesse_anim = profil.profil_spirituel.sensibilite_energetique
        self.fps_animation = int(30 + (vitesse_anim * 30))  # 30-60 fps    def _
configurer_affichage_mandala(self, mandala: MandalaVisuel):
        """Configure l'affichage du mandala"""
        # Centrer le mandala dans la zone d'affichage
        composant_mandala = self.composants_visuels["mandala_principal"]
        centre_x = composant_mandala.dimensions[0] // 2
        centre_y = composant_mandala.dimensions[1] // 2
        
        self.etat_interface.centre_vue = (centre_x, centre_y)
        self.etat_interface.mandala_affiche = mandala.geometrie_sacree
        
        # Ajuster le zoom selon la complexité
        nb_petales = len(mandala.petales)
        if nb_petales > 10:
            self.etat_interface.niveau_zoom = 0.8
        elif nb_petales < 5:
            self.etat_interface.niveau_zoom = 1.2
        else:
            self.etat_interface.niveau_zoom = 1.0
    
    def _demarrer_animations_mandala(self):
        """Démarre les animations du mandala"""
        if not self.mandala_actuel:
            return
        
        # Animation du centre énergétique
        self.etat_interface.animations_actives.append("centre_pulsation")
        
        # Animation des pétales
        self.etat_interface.animations_actives.append("petales_respiration")
        
        # Animation des flux énergétiques
        if self.mandala_actuel.connexions_energetiques:
            self.etat_interface.animations_actives.append("flux_particules")
        
        self.etat["animations_en_cours"] = len(self.etat_interface.animations_actives)
    
    async def _mettre_a_jour_animations(self):
        """Met à jour les animations en cours"""
        if not self.etat_interface.animations_actives:
            return
        
        temps_actuel = datetime.now().timestamp()
        
        # Simuler la mise à jour des animations
        for animation in self.etat_interface.animations_actives:
            if animation == "centre_pulsation":
                await self._animer_centre_energetique(temps_actuel)
            elif animation == "petales_respiration":
                await self._animer_petales(temps_actuel)
            elif animation == "flux_particules":
                await self._animer_flux_energetiques(temps_actuel)
    
    async def _animer_centre_energetique(self, temps: float):
        """Anime le centre énergétique"""
        # Pulsation douce du centre
        phase = (temps % 3.0) / 3.0  # Cycle de 3 secondes
        intensite = 0.8 + 0.2 * abs(0.5 - phase) * 2
        
        # Mettre à jour l'état d'animation (simulation)
        return {"centre_intensite": intensite}
    
    async def _animer_petales(self, temps: float):
        """Anime les pétales du mandala"""
        # Respiration subtile des pétales
        phase = (temps % 4.0) / 4.0  # Cycle de 4 secondes
        taille_base = 1.0
        variation = 0.05 * (0.5 - abs(phase - 0.5))
        
        return {"petales_taille": taille_base + variation}
    
    async def _animer_flux_energetiques(self, temps: float):
        """Anime les flux énergétiques"""
        # Particules qui se déplacent le long des flux
        phase = (temps % 2.0) / 2.0  # Cycle de 2 secondes
        
        particules = []
        for i in range(5):  # 5 particules par flux
            position = (phase + i * 0.2) % 1.0
            particules.append({
                "position": position,
                "intensite": 0.7 + 0.3 * abs(0.5 - position) * 2
            })
        
        return {"flux_particules": particules}