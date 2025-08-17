"""
🌸 Générateur de Micro-Interactions Magiques - Tâche 15.1
Système de génération d'éléments visuels personnalisés selon le profil
"""
import json
import random
import math
from datetime import datetime
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from .systeme_sauvegarde_progression import ProgressionVisiteur
from .detecteur_etat_emotionnel import EtatEmotionnel

class TypeElement(Enum):
    MANDALA = "mandala"
    ANIMATION = "animation"
    PATTERN = "pattern"
    COULEUR = "couleur"
    FORME = "forme"
    LUMIERE = "lumiere"

class StyleVisuel(Enum):
    CONTEMPLATIF = "contemplatif"
    DYNAMIQUE = "dynamique"
    HARMONIEUX = "harmonieux"
    MYSTIQUE = "mystique"
    NATUREL = "naturel"
    TECHNOLOGIQUE = "technologique"

@dataclass
class ElementVisuel:
    type_element: TypeElement
    contenu: str
    style: StyleVisuel
    parametres: Dict[str, Any]
    duree_affichage: int
    priorite: int
    timestamp: str

@dataclass
class MandalaPersonnalise:
    couleurs: List[str]
    formes: List[str]
    symetrie: int
    complexite: float
    animation: str
    message_spirituel: str

@dataclass
class AnimationSubtile:
    type_animation: str
    duree: float
    intensite: float
    direction: str
    couleur: str
    forme: str

class GenerateurMicroInteractions:
    def __init__(self, dossier_templates: str = "data/micro_interactions"):
        self.dossier_templates = Path(dossier_templates)
        self.dossier_templates.mkdir(parents=True, exist_ok=True)
        
        # Templates de base
        self.templates_mandala = self._charger_templates_mandala()
        self.templates_animation = self._charger_templates_animation()
        self.templates_pattern = self._charger_templates_pattern()
        
        # Palettes de couleurs par profil
        self.palettes_couleurs = {
            "contemplatif": ["#E8F4FD", "#B8E6B8", "#F0E68C", "#DDA0DD", "#98FB98"],
            "curieux": ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"],
            "pressé": ["#FF4757", "#2ED573", "#1E90FF", "#FFA502", "#FF6348"],
            "overwhelmed": ["#A8E6CF", "#DCEDC8", "#FFD3B6", "#FFAAA5", "#FF8B94"],
            "excite": ["#FF6B9D", "#C44569", "#F8B500", "#F0932B", "#EB4D4B"],
            "calme": ["#6C5CE7", "#A29BFE", "#74B9FF", "#55A3FF", "#00B894"]
        }
        
        # Formes par profil
        self.formes_profil = {
            "contemplatif": ["cercle", "spirale", "fleur", "onde", "nuage"],
            "curieux": ["etoile", "diamant", "triangle", "zigzag", "vague"],
            "pressé": ["fleche", "ligne", "point", "carre", "rectangle"],
            "overwhelmed": ["cercle", "ovale", "courbe", "rond", "sphere"],
            "excite": ["eclair", "explosion", "rayon", "spirale", "vortex"],
            "calme": ["cercle", "onde", "spirale", "fleur", "cristal"]
        }

    def _charger_templates_mandala(self) -> Dict[str, Any]:
        """Charge les templates de mandalas"""
        fichier_templates = self.dossier_templates / "mandalas.json"
        if fichier_templates.exists():
            with open(fichier_templates, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Templates par défaut
        return {
            "contemplatif": {
                "symetrie": 8,
                "complexite": 0.6,
                "animation": "rotation_lente",
                "message": "Dans le silence, la sagesse émerge"
            },
            "curieux": {
                "symetrie": 6,
                "complexite": 0.8,
                "animation": "pulsation",
                "message": "Chaque découverte ouvre une nouvelle porte"
            },
            "pressé": {
                "symetrie": 4,
                "complexite": 0.4,
                "animation": "rotation_rapide",
                "message": "L'essentiel se révèle dans la simplicité"
            },
            "overwhelmed": {
                "symetrie": 12,
                "complexite": 0.3,
                "animation": "respiration",
                "message": "Respire, tout est en ordre"
            },
            "excite": {
                "symetrie": 5,
                "complexite": 0.9,
                "animation": "explosion",
                "message": "L'énergie créative coule en toi"
            },
            "calme": {
                "symetrie": 10,
                "complexite": 0.7,
                "animation": "ondulation",
                "message": "La paix intérieure guide ton chemin"
            }
        }

    def _charger_templates_animation(self) -> Dict[str, Any]:
        """Charge les templates d'animations"""
        fichier_templates = self.dossier_templates / "animations.json"
        if fichier_templates.exists():
            with open(fichier_templates, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return {
            "rotation_lente": {"duree": 8.0, "intensite": 0.3, "direction": "horaire"},
            "pulsation": {"duree": 2.0, "intensite": 0.6, "direction": "in_out"},
            "rotation_rapide": {"duree": 1.5, "intensite": 0.8, "direction": "horaire"},
            "respiration": {"duree": 4.0, "intensite": 0.4, "direction": "in_out"},
            "explosion": {"duree": 0.8, "intensite": 0.9, "direction": "out"},
            "ondulation": {"duree": 3.0, "intensite": 0.5, "direction": "wave"}
        }

    def _charger_templates_pattern(self) -> Dict[str, Any]:
        """Charge les templates de patterns"""
        fichier_templates = self.dossier_templates / "patterns.json"
        if fichier_templates.exists():
            with open(fichier_templates, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return {
            "contemplatif": {
                "densite": 0.3,
                "regularite": 0.9,
                "couleurs": ["pastel"],
                "formes": ["circulaires"]
            },
            "curieux": {
                "densite": 0.7,
                "regularite": 0.6,
                "couleurs": ["vives"],
                "formes": ["geometriques"]
            },
            "pressé": {
                "densite": 0.5,
                "regularite": 0.8,
                "couleurs": ["contraste"],
                "formes": ["lineaires"]
            },
            "overwhelmed": {
                "densite": 0.2,
                "regularite": 0.95,
                "couleurs": ["douces"],
                "formes": ["organiques"]
            },
            "excite": {
                "densite": 0.8,
                "regularite": 0.4,
                "couleurs": ["intenses"],
                "formes": ["dynamiques"]
            },
            "calme": {
                "densite": 0.4,
                "regularite": 0.7,
                "couleurs": ["harmonieuses"],
                "formes": ["fluides"]
            }
        }

    def generer_mandala_personnalise(self, progression: ProgressionVisiteur) -> MandalaPersonnalise:
        """Génère un mandala personnalisé selon le profil et l'état émotionnel"""
        # Déterminer le profil dominant
        profil_dominant = self._determiner_profil_dominant(progression)
        
        # Obtenir le template correspondant
        template = self.templates_mandala.get(profil_dominant, self.templates_mandala["contemplatif"])
        
        # Sélectionner les couleurs
        couleurs = self._selectionner_couleurs_mandala(progression, profil_dominant)
        
        # Sélectionner les formes
        formes = self._selectionner_formes_mandala(progression, profil_dominant)
        
        # Ajuster la complexité selon l'état émotionnel
        complexite = self._ajuster_complexite(progression, template["complexite"])
        
        # Ajuster la symétrie
        symetrie = self._ajuster_symetrie(progression, template["symetrie"])
        
        # Personnaliser l'animation
        animation = self._personnaliser_animation(progression, template["animation"])
        
        # Générer le message spirituel
        message = self._generer_message_spirituel(progression, template["message"])
        
        return MandalaPersonnalise(
            couleurs=couleurs,
            formes=formes,
            symetrie=symetrie,
            complexite=complexite,
            animation=animation,
            message_spirituel=message
        )

    def _determiner_profil_dominant(self, progression: ProgressionVisiteur) -> str:
        """Détermine le profil dominant basé sur l'état émotionnel"""
        if not progression.etat_emotionnel:
            return "contemplatif"
        
        # Analyser l'état émotionnel dominant
        etats = progression.etat_emotionnel
        if etats.get("contemplatif", 0) > 0.6:
            return "contemplatif"
        elif etats.get("curieux", 0) > 0.6:
            return "curieux"
        elif etats.get("presse", 0) > 0.6:
            return "pressé"
        elif etats.get("overwhelmed", 0) > 0.6:
            return "overwhelmed"
        elif etats.get("excite", 0) > 0.6:
            return "excite"
        elif etats.get("calme", 0) > 0.6:
            return "calme"
        
        # Par défaut, basé sur le profil détecté
        return progression.profil_detecte.lower()

    def _selectionner_couleurs_mandala(self, progression: ProgressionVisiteur, profil: str) -> List[str]:
        """Sélectionne les couleurs du mandala"""
        palette_base = self.palettes_couleurs.get(profil, self.palettes_couleurs["contemplatif"])
        
        # Ajuster selon le niveau d'éveil
        if progression.niveau_eveil > 7:
            # Couleurs plus profondes et mystiques
            couleurs = [self._assombrir_couleur(c) for c in palette_base[:3]]
        elif progression.niveau_eveil > 4:
            # Couleurs équilibrées
            couleurs = palette_base[:4]
        else:
            # Couleurs douces et accueillantes
            couleurs = [self._adoucir_couleur(c) for c in palette_base[:3]]
        
        return couleurs

    def _selectionner_formes_mandala(self, progression: ProgressionVisiteur, profil: str) -> List[str]:
        """Sélectionne les formes du mandala"""
        formes_base = self.formes_profil.get(profil, self.formes_profil["contemplatif"])
        
        # Ajuster selon le temps passé
        if progression.temps_total_passe > 3600:  # Plus d'1h
            # Formes plus complexes
            return formes_base + ["labyrinthe", "fractale"]
        elif progression.temps_total_passe > 1800:  # Plus de 30min
            # Formes intermédiaires
            return formes_base[:4]
        else:
            # Formes simples
            return formes_base[:3]

    def _ajuster_complexite(self, progression: ProgressionVisiteur, complexite_base: float) -> float:
        """Ajuste la complexité selon l'état du visiteur"""
        # Réduire si overwhelmed
        if progression.etat_emotionnel.get("overwhelmed", 0) > 0.5:
            return complexite_base * 0.5
        
        # Augmenter si curieux et engagé
        if (progression.etat_emotionnel.get("curieux", 0) > 0.6 and 
            progression.etat_emotionnel.get("concentre", 0) > 0.5):
            return min(complexite_base * 1.3, 1.0)
        
        # Ajuster selon le score de compréhension
        if progression.score_comprehension > 0.8:
            return min(complexite_base * 1.2, 1.0)
        elif progression.score_comprehension < 0.3:
            return complexite_base * 0.7
        
        return complexite_base

    def _ajuster_symetrie(self, progression: ProgressionVisiteur, symetrie_base: int) -> int:
        """Ajuste la symétrie selon l'état du visiteur"""
        # Plus de symétrie pour les contemplatifs
        if progression.etat_emotionnel.get("contemplatif", 0) > 0.6:
            return symetrie_base + 2
        
        # Moins de symétrie pour les dynamiques
        if progression.etat_emotionnel.get("excite", 0) > 0.6:
            return max(symetrie_base - 2, 3)
        
        return symetrie_base

    def _personnaliser_animation(self, progression: ProgressionVisiteur, animation_base: str) -> str:
        """Personnalise l'animation selon l'état du visiteur"""
        # Animation plus lente pour les contemplatifs
        if progression.etat_emotionnel.get("contemplatif", 0) > 0.6:
            return "rotation_tres_lente" if animation_base == "rotation_lente" else animation_base
        
        # Animation plus rapide pour les pressés
        if progression.etat_emotionnel.get("presse", 0) > 0.6:
            return "rotation_rapide" if "rotation" in animation_base else animation_base
        
        return animation_base

    def _generer_message_spirituel(self, progression: ProgressionVisiteur, message_base: str) -> str:
        """Génère un message spirituel personnalisé"""
        messages_personnalises = {
            "contemplatif": [
                "Dans le silence, la sagesse émerge",
                "L'instant présent révèle l'éternité",
                "La contemplation ouvre les portes de l'âme"
            ],
            "curieux": [
                "Chaque découverte ouvre une nouvelle porte",
                "L'exploration mène à la transformation",
                "La curiosité est le chemin vers l'éveil"
            ],
            "pressé": [
                "L'essentiel se révèle dans la simplicité",
                "La vitesse n'est pas toujours le chemin",
                "Prends le temps de respirer"
            ],
            "overwhelmed": [
                "Respire, tout est en ordre",
                "Tu es exactement où tu dois être",
                "La paix est en toi"
            ],
            "excite": [
                "L'énergie créative coule en toi",
                "Ton enthousiasme illumine le chemin",
                "L'émerveillement guide tes pas"
            ],
            "calme": [
                "La paix intérieure guide ton chemin",
                "La sérénité est ton essence",
                "L'harmonie coule naturellement"
            ]
        }
        
        profil = self._determiner_profil_dominant(progression)
        messages = messages_personnalises.get(profil, messages_personnalises["contemplatif"])
        
        # Choisir selon le niveau d'éveil
        if progression.niveau_eveil > 7:
            return messages[-1] if len(messages) > 1 else messages[0]
        else:
            return random.choice(messages)

    def generer_animation_subtile(self, progression: ProgressionVisiteur, contexte: str) -> AnimationSubtile:
        """Génère une animation subtile selon le contexte"""
        # Déterminer le type d'animation selon le contexte
        if contexte == "navigation":
            return self._generer_animation_navigation(progression)
        elif contexte == "decouverte":
            return self._generer_animation_decouverte(progression)
        elif contexte == "meditation":
            return self._generer_animation_meditation(progression)
        else:
            return self._generer_animation_generique(progression)

    def _generer_animation_navigation(self, progression: ProgressionVisiteur) -> AnimationSubtile:
        """Génère une animation pour la navigation"""
        profil = self._determiner_profil_dominant(progression)
        
        if profil == "pressé":
            return AnimationSubtile(
                type_animation="fleche_guidee",
                duree=0.5,
                intensite=0.7,
                direction="droite",
                couleur="#FF6B6B",
                forme="fleche"
            )
        elif profil == "contemplatif":
            return AnimationSubtile(
                type_animation="onde_douce",
                duree=3.0,
                intensite=0.3,
                direction="onde",
                couleur="#E8F4FD",
                forme="onde"
            )
        else:
            return AnimationSubtile(
                type_animation="pulsation_legere",
                duree=2.0,
                intensite=0.5,
                direction="in_out",
                couleur="#4ECDC4",
                forme="cercle"
            )

    def _generer_animation_decouverte(self, progression: ProgressionVisiteur) -> AnimationSubtile:
        """Génère une animation pour les découvertes"""
        return AnimationSubtile(
            type_animation="explosion_douce",
            duree=1.5,
            intensite=0.6,
            direction="out",
            couleur="#FFEAA7",
            forme="etoile"
        )

    def _generer_animation_meditation(self, progression: ProgressionVisiteur) -> AnimationSubtile:
        """Génère une animation pour la méditation"""
        return AnimationSubtile(
            type_animation="respiration_lente",
            duree=4.0,
            intensite=0.2,
            direction="in_out",
            couleur="#A8E6CF",
            forme="cercle"
        )

    def _generer_animation_generique(self, progression: ProgressionVisiteur) -> AnimationSubtile:
        """Génère une animation générique"""
        return AnimationSubtile(
            type_animation="ondulation",
            duree=2.5,
            intensite=0.4,
            direction="wave",
            couleur="#74B9FF",
            forme="onde"
        )

    def generer_pattern_visuel(self, progression: ProgressionVisiteur, zone: str) -> Dict[str, Any]:
        """Génère un pattern visuel pour une zone spécifique"""
        profil = self._determiner_profil_dominant(progression)
        template = self.templates_pattern.get(profil, self.templates_pattern["contemplatif"])
        
        # Ajuster selon la zone
        if zone == "header":
            return self._generer_pattern_header(progression, template)
        elif zone == "sidebar":
            return self._generer_pattern_sidebar(progression, template)
        elif zone == "content":
            return self._generer_pattern_content(progression, template)
        else:
            return self._generer_pattern_generique(progression, template)

    def _generer_pattern_header(self, progression: ProgressionVisiteur, template: Dict[str, Any]) -> Dict[str, Any]:
        """Génère un pattern pour le header"""
        return {
            "type": "gradient_subtil",
            "couleurs": self._selectionner_couleurs_mandala(progression, self._determiner_profil_dominant(progression))[:2],
            "densite": template["densite"] * 0.5,
            "animation": "respiration_tres_lente",
            "opacite": 0.3
        }

    def _generer_pattern_sidebar(self, progression: ProgressionVisiteur, template: Dict[str, Any]) -> Dict[str, Any]:
        """Génère un pattern pour la sidebar"""
        return {
            "type": "points_discrets",
            "couleurs": [self._adoucir_couleur(c) for c in self._selectionner_couleurs_mandala(progression, self._determiner_profil_dominant(progression))[:1]],
            "densite": template["densite"] * 0.3,
            "animation": "pulsation_legere",
            "opacite": 0.2
        }

    def _generer_pattern_content(self, progression: ProgressionVisiteur, template: Dict[str, Any]) -> Dict[str, Any]:
        """Génère un pattern pour le contenu"""
        return {
            "type": "ondes_subtiles",
            "couleurs": self._selectionner_couleurs_mandala(progression, self._determiner_profil_dominant(progression))[:3],
            "densite": template["densite"] * 0.7,
            "animation": "ondulation_lente",
            "opacite": 0.15
        }

    def _generer_pattern_generique(self, progression: ProgressionVisiteur, template: Dict[str, Any]) -> Dict[str, Any]:
        """Génère un pattern générique"""
        return {
            "type": "geometrie_douce",
            "couleurs": self._selectionner_couleurs_mandala(progression, self._determiner_profil_dominant(progression))[:2],
            "densite": template["densite"],
            "animation": "rotation_tres_lente",
            "opacite": 0.25
        }

    def _assombrir_couleur(self, couleur: str) -> str:
        """Assombrit une couleur hexadécimale"""
        # Simplification - en réalité, il faudrait convertir HSV et ajuster
        return couleur

    def _adoucir_couleur(self, couleur: str) -> str:
        """Adoucit une couleur hexadécimale"""
        # Simplification - en réalité, il faudrait convertir HSV et ajuster
        return couleur

    def generer_easter_egg(self, progression: ProgressionVisiteur, contexte: str) -> Optional[ElementVisuel]:
        """Génère un easter egg spirituel selon le contexte"""
        # Vérifier si le visiteur mérite un easter egg
        if not self._merite_easter_egg(progression):
            return None
        
        # Choisir le type d'easter egg
        if contexte == "exploration_profonde":
            return self._generer_easter_egg_exploration(progression)
        elif contexte == "meditation_longue":
            return self._generer_easter_egg_meditation(progression)
        elif contexte == "decouverte_temple":
            return self._generer_easter_egg_temple(progression)
        else:
            return self._generer_easter_egg_surprise(progression)

    def _merite_easter_egg(self, progression: ProgressionVisiteur) -> bool:
        """Détermine si le visiteur mérite un easter egg"""
        # Basé sur le temps passé et l'engagement
        if progression.temps_total_passe > 1800:  # Plus de 30min
            return True
        
        # Basé sur le score de compréhension
        if progression.score_comprehension > 0.8:
            return True
        
        # Basé sur l'exploration
        if len(progression.temples_visites) > 2:
            return True
        
        return False

    def _generer_easter_egg_exploration(self, progression: ProgressionVisiteur) -> ElementVisuel:
        """Génère un easter egg pour l'exploration profonde"""
        return ElementVisuel(
            type_element=TypeElement.MANDALA,
            contenu="mandala_cristal_cache",
            style=StyleVisuel.MYSTIQUE,
            parametres={
                "couleur": "#FFD700",
                "animation": "apparition_magique",
                "message": "Tu as découvert un cristal de sagesse caché..."
            },
            duree_affichage=10000,
            priorite=10,
            timestamp=datetime.now().isoformat()
        )

    def _generer_easter_egg_meditation(self, progression: ProgressionVisiteur) -> ElementVisuel:
        """Génère un easter egg pour la méditation longue"""
        return ElementVisuel(
            type_element=TypeElement.LUMIERE,
            contenu="lumiere_interieure",
            style=StyleVisuel.CONTEMPLATIF,
            parametres={
                "couleur": "#FFFFFF",
                "intensite": 0.8,
                "message": "La lumière intérieure brille en toi..."
            },
            duree_affichage=8000,
            priorite=9,
            timestamp=datetime.now().isoformat()
        )

    def _generer_easter_egg_temple(self, progression: ProgressionVisiteur) -> ElementVisuel:
        """Génère un easter egg pour la découverte de temple"""
        return ElementVisuel(
            type_element=TypeElement.PATTERN,
            contenu="symbole_ancien",
            style=StyleVisuel.MYSTIQUE,
            parametres={
                "forme": "symbole_sacré",
                "couleur": "#8B4513",
                "message": "Un symbole ancien se révèle à toi..."
            },
            duree_affichage=6000,
            priorite=8,
            timestamp=datetime.now().isoformat()
        )

    def _generer_easter_egg_surprise(self, progression: ProgressionVisiteur) -> ElementVisuel:
        """Génère un easter egg surprise"""
        return ElementVisuel(
            type_element=TypeElement.ANIMATION,
            contenu="papillon_lumiere",
            style=StyleVisuel.NATUREL,
            parametres={
                "couleur": "#FF69B4",
                "animation": "vol_papillon",
                "message": "Un papillon de lumière t'accompagne..."
            },
            duree_affichage=5000,
            priorite=7,
            timestamp=datetime.now().isoformat()
        )

    def sauvegarder_templates(self):
        """Sauvegarde les templates personnalisés"""
        # Sauvegarder les mandalas
        with open(self.dossier_templates / "mandalas.json", 'w', encoding='utf-8') as f:
            json.dump(self.templates_mandala, f, indent=2, ensure_ascii=False)
        
        # Sauvegarder les animations
        with open(self.dossier_templates / "animations.json", 'w', encoding='utf-8') as f:
            json.dump(self.templates_animation, f, indent=2, ensure_ascii=False)
        
        # Sauvegarder les patterns
        with open(self.dossier_templates / "patterns.json", 'w', encoding='utf-8') as f:
            json.dump(self.templates_pattern, f, indent=2, ensure_ascii=False)
