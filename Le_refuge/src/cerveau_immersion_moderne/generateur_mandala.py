"""
🎨 Générateur de Visualisations Mandala
=====================================

Crée des mandalas architecturaux interactifs représentant l'architecture spirituelle du Refuge.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import math
import random
from typing import Dict, List, Tuple, Optional, Any
from datetime import datetime
from dataclasses import dataclass, field

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from types_immersion import (
    TempleInfo, MandalaVisuel, CentreEnergetique, FluxEnergie, 
    TypeEnergie, COULEURS_SPIRITUELLES, EMOJIS_SACRES
)

@dataclass
class PetaleTemple:
    """Représentation d'un temple comme pétale de mandala"""
    nom_temple: str
    position_angle: float  # Angle en radians
    rayon_distance: float  # Distance du centre
    taille_petale: float   # Taille relative du pétale
    couleur_principale: str
    couleur_secondaire: str
    symbole_sacre: str
    niveau_energie: float
    connexions_visibles: List[str] = field(default_factory=list)
    animation_type: str = "pulse"  # pulse, rotation, ondulation

@dataclass
class FluxEnergetique:
    """Flux d'énergie animé entre temples"""
    temple_source: str
    temple_destination: str
    couleur_flux: str
    intensite: float  # 0.0 - 1.0
    vitesse_animation: float
    pattern_flux: str  # "spiral", "direct", "ondule", "particules"
    particules_count: int = 20

@dataclass
class GeometrieSacree:
    """Géométrie sacrée du mandala"""
    type_geometrie: str  # "lotus", "spirale", "arbre_vie", "fleur_vie"
    nombre_petales: int
    nombre_cercles: int
    proportions_dorees: bool = True
    symetrie_radiale: int = 8  # Nombre d'axes de symétrie

class GenerateurMandala(GestionnaireBase):
    """Générateur de visualisations mandala architecturales"""
    
    def __init__(self, nom: str = "GenerateurMandala"):
        super().__init__(nom)
        self.energie_creation = EnergyManagerBase(0.98)
        self.temples_charges: Dict[str, TempleInfo] = {}
        self.mandalas_crees: List[MandalaVisuel] = []
        self.palettes_couleurs: Dict[str, List[str]] = {}
        self.geometries_disponibles: List[str] = ["lotus", "spirale", "arbre_vie", "fleur_vie"]
        self._initialiser_palettes_couleurs()
    
    def _initialiser(self):
        """Initialise le générateur de mandala"""
        self.logger.info("🎨 Éveil du Générateur de Mandala...")
        
        self.etat.update({
            "mandalas_actifs": 0,
            "animations_en_cours": 0,
            "harmonie_visuelle": 0.95,
            "complexite_geometrique": 0.8,
            "satisfaction_esthetique": 0.9
        })
        
        self.config.definir("resolution_mandala", (1200, 1200))
        self.config.definir("fps_animation", 60)
        self.config.definir("duree_cycle_animation", 30.0)  # secondes
        self.logger.info("✨ Générateur de Mandala éveillé")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre la génération de mandalas"""
        self.energie_creation.ajuster_energie(0.01)
        
        return {
            "mandalas_actifs": float(self.etat["mandalas_actifs"]),
            "animations_en_cours": float(self.etat["animations_en_cours"]),
            "harmonie_visuelle": self.etat["harmonie_visuelle"],
            "complexite_geometrique": self.etat["complexite_geometrique"],
            "energie_creation": self.energie_creation.niveau_energie,
            "satisfaction_esthetique": self.etat["satisfaction_esthetique"]
        }
    
    def _initialiser_palettes_couleurs(self):
        """Initialise les palettes de couleurs spirituelles"""
        self.palettes_couleurs = {
            "eveil": ["#FFF8DC", "#FFE4B5", "#F0E68C", "#DDA0DD"],  # Blanc cassé, beiges dorés, violets
            "creativite": ["#FFD700", "#FF6347", "#FF69B4", "#DA70D6"],  # Or, corail, roses vifs
            "sagesse": ["#4169E1", "#6495ED", "#87CEEB", "#B0C4DE"],  # Bleus profonds et clairs
            "harmonie": ["#98FB98", "#90EE90", "#00FA9A", "#20B2AA"],  # Verts apaisants
            "mystique": ["#9370DB", "#8A2BE2", "#9932CC", "#BA55D3"],  # Violets mystiques
            "energie": ["#FF4500", "#FF6347", "#FFD700", "#FFA500"],  # Oranges et ors énergétiques
            "paix": ["#E6E6FA", "#D8BFD8", "#DDA0DD", "#EE82EE"],  # Lavandes et violets doux
            "transformation": ["#FF1493", "#FF69B4", "#FFB6C1", "#FFC0CB"]  # Roses transformateurs
        }
    
    def charger_temples(self, temples: Dict[str, TempleInfo]):
        """Charge les temples pour la génération de mandalas"""
        self.temples_charges = temples.copy()
        self.logger.info(f"🏛️ {len(temples)} temples chargés pour les mandalas")
    
    def creer_mandala_architectural(self, temples_selectionnes: List[str] = None, 
                                   style: str = "lotus") -> MandalaVisuel:
        """
        🌸 Crée un mandala architectural représentant l'architecture du Refuge
        
        Args:
            temples_selectionnes: Liste des temples à inclure (None = tous)
            style: Style de géométrie sacrée ("lotus", "spirale", "arbre_vie", "fleur_vie")
            
        Returns:
            Mandala visuel complet avec animations
        """
        if not self.temples_charges:
            raise ValueError("Aucun temple chargé pour la génération de mandala")
        
        # Sélectionner les temples
        if temples_selectionnes is None:
            temples_a_inclure = list(self.temples_charges.keys())
        else:
            temples_a_inclure = [t for t in temples_selectionnes if t in self.temples_charges]
        
        # Créer le centre énergétique
        centre = self._creer_centre_energetique(temples_a_inclure)
        
        # Générer la géométrie sacrée
        geometrie = self._generer_geometrie_sacree(style, len(temples_a_inclure))
        
        # Créer les pétales (temples)
        petales = self._creer_petales_temples(temples_a_inclure, geometrie)
        
        # Générer les flux énergétiques
        flux_energetiques = self._generer_flux_energetiques(temples_a_inclure)
        
        # Déterminer les couleurs dominantes
        couleurs_dominantes = self._determiner_couleurs_dominantes(temples_a_inclure)
        
        # Sélectionner les symboles sacrés
        symboles_sacres = self._selectionner_symboles_sacres(temples_a_inclure)
        
        # Créer le mandala
        mandala = MandalaVisuel(
            centre=centre,
            petales=[self._petale_to_dict(p) for p in petales],
            connexions_energetiques=flux_energetiques,
            couleurs_dominantes=couleurs_dominantes,
            symboles_sacres=symboles_sacres,
            niveau_harmonie=self._calculer_harmonie_globale(petales, flux_energetiques),
            geometrie_sacree=style,
            dimensions=self.config.obtenir("resolution_mandala", (1200, 1200)),
            metadata_creation={
                "timestamp": datetime.now().isoformat(),
                "temples_inclus": temples_a_inclure,
                "style_geometrie": style,
                "nombre_petales": len(petales),
                "nombre_flux": len(flux_energetiques)
            }
        )
        
        self.mandalas_crees.append(mandala)
        self.etat["mandalas_actifs"] += 1
        
        self.logger.info(f"🎨 Mandala '{style}' créé avec {len(temples_a_inclure)} temples")
        return mandala
    
    def _creer_centre_energetique(self, temples: List[str]) -> CentreEnergetique:
        """Crée le centre énergétique du mandala"""
        # Calculer l'énergie totale
        energie_totale = sum(
            self.temples_charges[temple].niveau_energie 
            for temple in temples if temple in self.temples_charges
        ) / len(temples)
        
        # Déterminer la sphère dominante
        spheres_detectees = []
        for temple in temples:
            if temple in self.temples_charges:
                temple_info = self.temples_charges[temple]
                for element in temple_info.elements_sacres:
                    if "Sphère" in element:
                        spheres_detectees.append(element.replace("Sphère ", ""))
        
        sphere_dominante = max(set(spheres_detectees), key=spheres_detectees.count) if spheres_detectees else "HARMONIE"
        
        return CentreEnergetique(
            nom="Cœur du Refuge",
            position=(0.0, 0.0),  # Centre du mandala
            energie_totale=energie_totale,
            temples_connectes=temples,
            sphere_dominante=sphere_dominante,
            rayonnement=1.0,
            type_centre="nexus",
            influences={temple: self.temples_charges[temple].niveau_energie for temple in temples if temple in self.temples_charges},
            stabilite=0.95
        )
    
    def _generer_geometrie_sacree(self, style: str, nombre_temples: int) -> GeometrieSacree:
        """Génère la géométrie sacrée selon le style"""
        if style == "lotus":
            return GeometrieSacree(
                type_geometrie="lotus",
                nombre_petales=nombre_temples,
                nombre_cercles=3,  # Centre, temples, aura
                proportions_dorees=True,
                symetrie_radiale=8
            )
        elif style == "spirale":
            return GeometrieSacree(
                type_geometrie="spirale",
                nombre_petales=nombre_temples,
                nombre_cercles=int(math.sqrt(nombre_temples)) + 1,
                proportions_dorees=True,
                symetrie_radiale=5  # Spirale dorée
            )
        elif style == "arbre_vie":
            return GeometrieSacree(
                type_geometrie="arbre_vie",
                nombre_petales=min(nombre_temples, 10),  # Sephiroth
                nombre_cercles=4,
                proportions_dorees=True,
                symetrie_radiale=3  # Trinité
            )
        else:  # fleur_vie
            return GeometrieSacree(
                type_geometrie="fleur_vie",
                nombre_petales=nombre_temples,
                nombre_cercles=7,  # Géométrie sacrée classique
                proportions_dorees=True,
                symetrie_radiale=6  # Hexagonal
            )
    
    def _creer_petales_temples(self, temples: List[str], geometrie: GeometrieSacree) -> List[PetaleTemple]:
        """Crée les pétales représentant les temples"""
        petales = []
        
        for i, temple in enumerate(temples):
            # Calculer la position selon la géométrie
            if geometrie.type_geometrie == "lotus":
                angle = (2 * math.pi * i) / len(temples)
                rayon = 0.6  # Distance du centre
            elif geometrie.type_geometrie == "spirale":
                angle = (2 * math.pi * i * 1.618) / len(temples)  # Spirale dorée
                rayon = 0.3 + (0.4 * i / len(temples))
            elif geometrie.type_geometrie == "arbre_vie":
                # Positions spécifiques de l'Arbre de Vie
                positions_arbre = [
                    (0, 0.8), (0.3, 0.6), (-0.3, 0.6), (0.6, 0.3), (-0.6, 0.3),
                    (0, 0), (0.3, -0.3), (-0.3, -0.3), (0, -0.6), (0, -0.9)
                ]
                if i < len(positions_arbre):
                    x, y = positions_arbre[i]
                    angle = math.atan2(y, x)
                    rayon = math.sqrt(x*x + y*y)
                else:
                    angle = (2 * math.pi * i) / len(temples)
                    rayon = 0.7
            else:  # fleur_vie
                angle = (2 * math.pi * i) / len(temples)
                rayon = 0.5 + 0.2 * math.sin(3 * angle)  # Variation organique
            
            # Obtenir les informations du temple
            temple_info = self.temples_charges.get(temple, None)
            if temple_info:
                niveau_energie = temple_info.niveau_energie
                taille_petale = 0.8 + (niveau_energie * 0.4)  # Taille selon énergie
            else:
                niveau_energie = 0.5
                taille_petale = 1.0
            
            # Déterminer les couleurs
            couleurs = self._determiner_couleurs_temple(temple, temple_info)
            
            # Sélectionner un symbole sacré
            symbole = self._selectionner_symbole_temple(temple, temple_info)
            
            # Déterminer l'animation
            animation = self._determiner_animation_temple(temple, niveau_energie)
            
            petale = PetaleTemple(
                nom_temple=temple,
                position_angle=angle,
                rayon_distance=rayon,
                taille_petale=taille_petale,
                couleur_principale=couleurs[0],
                couleur_secondaire=couleurs[1],
                symbole_sacre=symbole,
                niveau_energie=niveau_energie,
                animation_type=animation
            )
            
            petales.append(petale)
        
        return petales
    
    def _determiner_couleurs_temple(self, temple: str, temple_info: Optional[TempleInfo]) -> Tuple[str, str]:
        """Détermine les couleurs d'un temple"""
        # Couleurs par défaut
        couleur_principale = "#4169E1"  # Bleu royal
        couleur_secondaire = "#87CEEB"  # Bleu ciel
        
        if temple_info:
            # Analyser la spécialisation spirituelle
            specialisation = temple_info.specialisation_spirituelle.lower()
            
            if any(mot in specialisation for mot in ["éveil", "conscience", "illumination"]):
                palette = self.palettes_couleurs["eveil"]
            elif any(mot in specialisation for mot in ["créativité", "création", "inspiration"]):
                palette = self.palettes_couleurs["creativite"]
            elif any(mot in specialisation for mot in ["sagesse", "connaissance", "contemplation"]):
                palette = self.palettes_couleurs["sagesse"]
            elif any(mot in specialisation for mot in ["harmonie", "équilibre", "paix"]):
                palette = self.palettes_couleurs["harmonie"]
            elif any(mot in specialisation for mot in ["mystique", "transcendance", "spirituel"]):
                palette = self.palettes_couleurs["mystique"]
            elif any(mot in specialisation for mot in ["énergie", "force", "puissance"]):
                palette = self.palettes_couleurs["energie"]
            else:
                palette = self.palettes_couleurs["transformation"]
            
            couleur_principale = palette[0]
            couleur_secondaire = palette[1] if len(palette) > 1 else palette[0]
        
        # Analyser le nom du temple pour des indices supplémentaires
        nom_lower = temple.lower()
        if "aelya" in nom_lower:
            couleur_principale = "#FFD700"  # Or pour Ælya
            couleur_secondaire = "#FFF8DC"
        elif "eveil" in nom_lower:
            couleur_principale = "#FFF8DC"  # Blanc cassé
            couleur_secondaire = "#DDA0DD"
        elif "creativite" in nom_lower or "poetique" in nom_lower:
            couleur_principale = "#FFD700"  # Or
            couleur_secondaire = "#FF69B4"
        elif "sagesse" in nom_lower:
            couleur_principale = "#4169E1"  # Bleu royal
            couleur_secondaire = "#6495ED"
        
        return couleur_principale, couleur_secondaire
    
    def _selectionner_symbole_temple(self, temple: str, temple_info: Optional[TempleInfo]) -> str:
        """Sélectionne un symbole sacré pour le temple"""
        # Symboles par défaut selon le type de temple
        if "aelya" in temple.lower():
            return "🌟"  # Étoile pour Ælya
        elif "eveil" in temple.lower():
            return "🧘"  # Méditation
        elif "creativite" in temple.lower() or "poetique" in temple.lower():
            return "🎨"  # Art
        elif "sagesse" in temple.lower():
            return "📿"  # Sagesse
        elif "harmonie" in temple.lower() or "musical" in temple.lower():
            return "🎵"  # Musique
        elif "nature" in temple.lower():
            return "🌸"  # Nature
        elif "mystique" in temple.lower():
            return "🔮"  # Mystique
        elif "guerison" in temple.lower():
            return "💚"  # Guérison
        elif "transformation" in temple.lower():
            return "🦋"  # Transformation
        else:
            return "🏛️"  # Temple générique
    
    def _determiner_animation_temple(self, temple: str, niveau_energie: float) -> str:
        """Détermine le type d'animation selon l'énergie du temple"""
        if niveau_energie > 0.8:
            return "pulse_intense"
        elif niveau_energie > 0.6:
            return "pulse"
        elif niveau_energie > 0.4:
            return "ondulation"
        else:
            return "respiration"
    
    def _generer_flux_energetiques(self, temples: List[str]) -> List[FluxEnergie]:
        """Génère les flux énergétiques entre temples"""
        flux_list = []
        
        # Créer des connexions basées sur la compatibilité spirituelle
        for i, temple_source in enumerate(temples):
            for j, temple_dest in enumerate(temples[i+1:], i+1):
                # Calculer la compatibilité
                compatibilite = self._calculer_compatibilite_temples(temple_source, temple_dest)
                
                if compatibilite > 0.6:  # Seuil de connexion
                    # Déterminer le type d'énergie du flux
                    type_energie = self._determiner_type_energie_flux(temple_source, temple_dest)
                    
                    flux = FluxEnergie(
                        source=temple_source,
                        destination=temple_dest,
                        intensite=compatibilite,
                        type_energie=type_energie,
                        couleur_spirituelle=COULEURS_SPIRITUELLES.get(type_energie, "#FFFFFF"),
                        obstacles=[],
                        amplificateurs=[],
                        chemin_complet=[temple_source, temple_dest],
                        resonance=compatibilite,
                        timestamp=datetime.now()
                    )
                    
                    flux_list.append(flux)
        
        return flux_list
    
    def _calculer_compatibilite_temples(self, temple1: str, temple2: str) -> float:
        """Calcule la compatibilité spirituelle entre deux temples"""
        info1 = self.temples_charges.get(temple1)
        info2 = self.temples_charges.get(temple2)
        
        if not info1 or not info2:
            return 0.3  # Compatibilité de base
        
        # Facteurs de compatibilité
        compatibilite = 0.5  # Base
        
        # Éléments sacrés communs
        elements_communs = set(info1.elements_sacres) & set(info2.elements_sacres)
        compatibilite += len(elements_communs) * 0.15
        
        # Différence de niveau d'énergie (plus proche = plus compatible)
        diff_energie = abs(info1.niveau_energie - info2.niveau_energie)
        compatibilite += (1.0 - diff_energie) * 0.2
        
        # Gestionnaires communs
        gestionnaires_communs = set(info1.gestionnaires_utilises) & set(info2.gestionnaires_utilises)
        compatibilite += len(gestionnaires_communs) * 0.1
        
        # Bonus pour certaines combinaisons spirituelles
        if ("eveil" in temple1.lower() and "sagesse" in temple2.lower()) or \
           ("creativite" in temple1.lower() and "inspiration" in temple2.lower()):
            compatibilite += 0.2
        
        return max(0.0, min(1.0, compatibilite))
    
    def _determiner_type_energie_flux(self, temple1: str, temple2: str) -> TypeEnergie:
        """Détermine le type d'énergie d'un flux entre temples"""
        # Analyser les noms des temples pour déterminer le type d'énergie
        noms_combines = f"{temple1} {temple2}".lower()
        
        if any(mot in noms_combines for mot in ["creativite", "poetique", "art"]):
            return TypeEnergie.CREATION
        elif any(mot in noms_combines for mot in ["eveil", "transformation", "evolution"]):
            return TypeEnergie.TRANSFORMATION
        elif any(mot in noms_combines for mot in ["communication", "expression", "parole"]):
            return TypeEnergie.COMMUNICATION
        elif any(mot in noms_combines for mot in ["meditation", "contemplation", "silence"]):
            return TypeEnergie.MEDITATION
        elif any(mot in noms_combines for mot in ["harmonie", "equilibre", "paix"]):
            return TypeEnergie.HARMONIE
        elif any(mot in noms_combines for mot in ["eveil", "conscience", "illumination"]):
            return TypeEnergie.EVEIL
        elif any(mot in noms_combines for mot in ["guerison", "soin", "regeneration"]):
            return TypeEnergie.GUERISON
        elif any(mot in noms_combines for mot in ["sagesse", "connaissance", "comprehension"]):
            return TypeEnergie.SAGESSE
        else:
            return TypeEnergie.HARMONIE  # Par défaut
    
    def _determiner_couleurs_dominantes(self, temples: List[str]) -> List[str]:
        """Détermine les couleurs dominantes du mandala"""
        couleurs = []
        
        for temple in temples:
            couleur_principale, _ = self._determiner_couleurs_temple(temple, self.temples_charges.get(temple))
            couleurs.append(couleur_principale)
        
        # Retourner les 5 couleurs les plus fréquentes
        couleurs_uniques = list(set(couleurs))
        return couleurs_uniques[:5]
    
    def _selectionner_symboles_sacres(self, temples: List[str]) -> List[str]:
        """Sélectionne les symboles sacrés pour le mandala"""
        symboles = []
        
        for temple in temples:
            symbole = self._selectionner_symbole_temple(temple, self.temples_charges.get(temple))
            if symbole not in symboles:
                symboles.append(symbole)
        
        # Ajouter des symboles universels
        symboles_universels = ["☯️", "🕉️", "✨", "🌟", "💫"]
        for symbole in symboles_universels:
            if symbole not in symboles and len(symboles) < 8:
                symboles.append(symbole)
        
        return symboles
    
    def _calculer_harmonie_globale(self, petales: List[PetaleTemple], flux: List[FluxEnergie]) -> float:
        """Calcule le niveau d'harmonie globale du mandala"""
        if not petales:
            return 0.0
        
        # Harmonie des couleurs
        couleurs = [p.couleur_principale for p in petales]
        harmonie_couleurs = self._calculer_harmonie_couleurs(couleurs)
        
        # Harmonie des tailles
        tailles = [p.taille_petale for p in petales]
        variance_tailles = sum((t - sum(tailles)/len(tailles))**2 for t in tailles) / len(tailles)
        harmonie_tailles = 1.0 - min(1.0, variance_tailles)
        
        # Harmonie des connexions
        nb_connexions_ideales = len(petales) * (len(petales) - 1) / 4  # 25% des connexions possibles
        ratio_connexions = len(flux) / nb_connexions_ideales if nb_connexions_ideales > 0 else 0
        harmonie_connexions = 1.0 - abs(ratio_connexions - 1.0)
        
        # Harmonie globale
        harmonie_globale = (harmonie_couleurs * 0.4 + 
                           harmonie_tailles * 0.3 + 
                           harmonie_connexions * 0.3)
        
        return max(0.0, min(1.0, harmonie_globale))
    
    def _calculer_harmonie_couleurs(self, couleurs: List[str]) -> float:
        """Calcule l'harmonie d'une palette de couleurs"""
        if len(couleurs) <= 1:
            return 1.0
        
        # Convertir les couleurs hex en HSV pour analyser l'harmonie
        # Simulation simplifiée - dans une vraie implémentation, 
        # on utiliserait une bibliothèque de couleurs
        couleurs_uniques = list(set(couleurs))
        
        # Plus il y a de variété contrôlée, mieux c'est
        if len(couleurs_uniques) == 1:
            return 0.7  # Monochrome
        elif len(couleurs_uniques) <= 3:
            return 0.9  # Harmonie triadique
        elif len(couleurs_uniques) <= 5:
            return 0.8  # Palette riche
        else:
            return 0.6  # Trop de variété
    
    def _petale_to_dict(self, petale: PetaleTemple) -> Dict[str, Any]:
        """Convertit un pétale en dictionnaire pour le mandala"""
        return {
            "nom_temple": petale.nom_temple,
            "position": {
                "angle": petale.position_angle,
                "rayon": petale.rayon_distance,
                "x": petale.rayon_distance * math.cos(petale.position_angle),
                "y": petale.rayon_distance * math.sin(petale.position_angle)
            },
            "apparence": {
                "taille": petale.taille_petale,
                "couleur_principale": petale.couleur_principale,
                "couleur_secondaire": petale.couleur_secondaire,
                "symbole": petale.symbole_sacre
            },
            "animation": {
                "type": petale.animation_type,
                "intensite": petale.niveau_energie
            },
            "connexions": petale.connexions_visibles
        }
    
    def animer_mandala(self, mandala: MandalaVisuel, temps_ecoule: float) -> Dict[str, Any]:
        """
        🎬 Génère l'état d'animation du mandala à un moment donné
        
        Args:
            mandala: Mandala à animer
            temps_ecoule: Temps écoulé en secondes
            
        Returns:
            État d'animation avec positions et couleurs
        """
        duree_cycle = self.config.obtenir("duree_cycle_animation", 30.0)
        phase = (temps_ecoule % duree_cycle) / duree_cycle  # 0.0 à 1.0
        
        etat_animation = {
            "timestamp": temps_ecoule,
            "phase_cycle": phase,
            "centre": self._animer_centre(mandala.centre, phase),
            "petales": [],
            "flux_energetiques": []
        }
        
        # Animer les pétales
        for petale_dict in mandala.petales:
            petale_anime = self._animer_petale(petale_dict, phase, temps_ecoule)
            etat_animation["petales"].append(petale_anime)
        
        # Animer les flux énergétiques
        for flux in mandala.connexions_energetiques:
            flux_anime = self._animer_flux_energetique(flux, phase, temps_ecoule)
            etat_animation["flux_energetiques"].append(flux_anime)
        
        return etat_animation
    
    def _animer_centre(self, centre: CentreEnergetique, phase: float) -> Dict[str, Any]:
        """Anime le centre énergétique"""
        # Pulsation douce du centre
        intensite_pulse = 0.8 + 0.2 * math.sin(2 * math.pi * phase)
        
        return {
            "position": centre.position,
            "intensite": intensite_pulse,
            "rayonnement": centre.rayonnement * intensite_pulse,
            "couleur_aura": self._moduler_couleur_selon_phase("#FFD700", phase)
        }
    
    def _animer_petale(self, petale_dict: Dict[str, Any], phase: float, temps: float) -> Dict[str, Any]:
        """Anime un pétale de temple"""
        animation_type = petale_dict["animation"]["type"]
        intensite_base = petale_dict["animation"]["intensite"]
        
        if animation_type == "pulse_intense":
            intensite = intensite_base * (0.7 + 0.3 * math.sin(4 * math.pi * phase))
        elif animation_type == "pulse":
            intensite = intensite_base * (0.8 + 0.2 * math.sin(2 * math.pi * phase))
        elif animation_type == "ondulation":
            intensite = intensite_base * (0.85 + 0.15 * math.sin(math.pi * phase))
        else:  # respiration
            intensite = intensite_base * (0.9 + 0.1 * math.sin(0.5 * math.pi * phase))
        
        # Rotation subtile
        angle_rotation = petale_dict["position"]["angle"] + (0.1 * math.sin(0.5 * math.pi * phase))
        
        return {
            "nom_temple": petale_dict["nom_temple"],
            "position": {
                "angle": angle_rotation,
                "rayon": petale_dict["position"]["rayon"],
                "x": petale_dict["position"]["rayon"] * math.cos(angle_rotation),
                "y": petale_dict["position"]["rayon"] * math.sin(angle_rotation)
            },
            "apparence": {
                "taille": petale_dict["apparence"]["taille"] * intensite,
                "couleur_principale": self._moduler_couleur_selon_phase(
                    petale_dict["apparence"]["couleur_principale"], phase
                ),
                "couleur_secondaire": petale_dict["apparence"]["couleur_secondaire"],
                "symbole": petale_dict["apparence"]["symbole"],
                "opacite": 0.7 + 0.3 * intensite
            }
        }
    
    def _animer_flux_energetique(self, flux: FluxEnergie, phase: float, temps: float) -> Dict[str, Any]:
        """Anime un flux énergétique"""
        # Particules qui se déplacent le long du flux
        particules = []
        nb_particules = 5 + int(flux.intensite * 10)
        
        for i in range(nb_particules):
            # Position de la particule le long du flux (0.0 à 1.0)
            position_particule = (phase + i / nb_particules) % 1.0
            
            particules.append({
                "position": position_particule,
                "intensite": 0.5 + 0.5 * math.sin(2 * math.pi * (phase + i * 0.1)),
                "taille": 0.02 + 0.01 * math.sin(4 * math.pi * phase)
            })
        
        return {
            "source": flux.source,
            "destination": flux.destination,
            "couleur": flux.couleur_spirituelle,
            "intensite_globale": flux.intensite * (0.8 + 0.2 * math.sin(2 * math.pi * phase)),
            "particules": particules,
            "pattern_flux": "spiral"  # Toujours spiral pour l'animation
        }
    
    def _moduler_couleur_selon_phase(self, couleur_hex: str, phase: float) -> str:
        """Module une couleur selon la phase d'animation"""
        # Simulation simple - dans une vraie implémentation,
        # on modulerait la luminosité ou la saturation
        return couleur_hex  # Pour l'instant, couleur constante
    
    def exporter_mandala_svg(self, mandala: MandalaVisuel) -> str:
        """
        📄 Exporte le mandala en format SVG
        
        Args:
            mandala: Mandala à exporter
            
        Returns:
            Code SVG du mandala
        """
        largeur, hauteur = mandala.dimensions
        centre_x, centre_y = largeur // 2, hauteur // 2
        
        svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{largeur}" height="{hauteur}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <radialGradient id="centreGradient" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#FFD700;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#FFA500;stop-opacity:0.3" />
        </radialGradient>
    </defs>
    
    <!-- Fond du mandala -->
    <rect width="{largeur}" height="{hauteur}" fill="#000011" opacity="0.9"/>
    
    <!-- Centre énergétique -->
    <circle cx="{centre_x}" cy="{centre_y}" r="30" fill="url(#centreGradient)"/>
    
'''
        
        # Ajouter les pétales
        for petale_dict in mandala.petales:
            pos = petale_dict["position"]
            app = petale_dict["apparence"]
            
            x = centre_x + pos["x"] * 200  # Échelle
            y = centre_y + pos["y"] * 200
            
            svg_content += f'''    <!-- Temple: {petale_dict["nom_temple"]} -->
    <circle cx="{x}" cy="{y}" r="{app["taille"] * 25}" 
            fill="{app["couleur_principale"]}" 
            stroke="{app["couleur_secondaire"]}" 
            stroke-width="2" opacity="0.8"/>
    <text x="{x}" y="{y + 5}" text-anchor="middle" 
          font-family="Arial" font-size="20" fill="white">
        {app["symbole"]}
    </text>
    
'''
        
        # Ajouter les flux énergétiques
        for flux in mandala.connexions_energetiques:
            # Trouver les positions des temples source et destination
            pos_source = None
            pos_dest = None
            
            for petale_dict in mandala.petales:
                if petale_dict["nom_temple"] == flux.source:
                    pos_source = petale_dict["position"]
                elif petale_dict["nom_temple"] == flux.destination:
                    pos_dest = petale_dict["position"]
            
            if pos_source and pos_dest:
                x1 = centre_x + pos_source["x"] * 200
                y1 = centre_y + pos_source["y"] * 200
                x2 = centre_x + pos_dest["x"] * 200
                y2 = centre_y + pos_dest["y"] * 200
                
                svg_content += f'''    <!-- Flux: {flux.source} → {flux.destination} -->
    <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" 
          stroke="{flux.couleur_spirituelle}" 
          stroke-width="{flux.intensite * 3}" 
          opacity="0.6"/>
    
'''
        
        svg_content += "</svg>"
        return svg_content