"""
🎨 Gestionnaire de Thèmes Visuels Spirituels
==========================================

Gestionnaire avancé des thèmes visuels pour l'interface spirituelle.
Adapte dynamiquement les couleurs, animations et styles selon le profil utilisateur.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import colorsys
import math

from types_immersion import ProfilUtilisateur, TypeUtilisateur

class StyleAnimation(Enum):
    """Styles d'animation disponibles"""
    FLUIDE = "fluide"
    DYNAMIQUE = "dynamique"
    CONTEMPLATIF = "contemplatif"
    EXPRESSIF = "expressif"
    EQUILIBRE = "equilibre"

@dataclass
class PaletteSpiritulle:
    """Palette de couleurs spirituelle"""
    nom: str
    couleurs_primaires: List[str]
    couleurs_secondaires: List[str]
    couleur_accent: str
    couleur_fond: str
    couleur_texte: str
    opacite_base: float = 0.8
    contraste_niveau: str = "normal"

@dataclass
class ThemeVisuel:
    """Thème visuel complet"""
    nom: str
    palette: PaletteSpiritulle
    style_animation: StyleAnimation
    fps_cible: int
    duree_transitions: float
    intensite_effets: float
    geometrie_preferee: str
    elements_decoratifs: List[str]

class GestionnaireThemesVisuels:
    """
    🎨 Gestionnaire de Thèmes Visuels Spirituels
    
    Crée et adapte dynamiquement les thèmes visuels selon le profil spirituel
    de l'utilisateur et le contexte de l'immersion.
    """
    
    def __init__(self):
        self.nom = "GestionnaireThemesVisuels"
        
        # Palettes prédéfinies
        self.palettes_base = self._creer_palettes_base()
        
        # Thèmes prédéfinis
        self.themes_predefinis = self._creer_themes_predefinis()
        
        # Cache des thèmes personnalisés
        self.themes_personnalises: Dict[str, ThemeVisuel] = {}
        
        # Configuration des harmonies de couleurs
        self.harmonies_couleurs = {
            "complementaire": self._generer_harmonie_complementaire,
            "triadique": self._generer_harmonie_triadique,
            "analogique": self._generer_harmonie_analogique,
            "monochromatique": self._generer_harmonie_monochromatique
        }
    
    def _creer_palettes_base(self) -> Dict[str, PaletteSpiritulle]:
        """Crée les palettes de couleurs de base"""
        return {
            "aventure_cosmique": PaletteSpiritulle(
                nom="Aventure Cosmique",
                couleurs_primaires=["#4169E1", "#00CED1", "#FFD700"],
                couleurs_secondaires=["#32CD32", "#FF6347", "#9370DB"],
                couleur_accent="#FFD700",
                couleur_fond="#0F0F23",
                couleur_texte="#E6E6FA",
                opacite_base=0.85,
                contraste_niveau="eleve"
            ),
            "sagesse_contemplative": PaletteSpiritulle(
                nom="Sagesse Contemplative",
                couleurs_primaires=["#9370DB", "#DDA0DD", "#E6E6FA"],
                couleurs_secondaires=["#F0E68C", "#98FB98", "#87CEEB"],
                couleur_accent="#DDA0DD",
                couleur_fond="#2F2F4F",
                couleur_texte="#F5F5DC",
                opacite_base=0.75,
                contraste_niveau="doux"
            ),
            "creation_artistique": PaletteSpiritulle(
                nom="Création Artistique",
                couleurs_primaires=["#FF6347", "#FFD700", "#FF69B4"],
                couleurs_secondaires=["#DA70D6", "#FFA500", "#FF1493"],
                couleur_accent="#FF69B4",
                couleur_fond="#1A1A2E",
                couleur_texte="#FFF8DC",
                opacite_base=0.9,
                contraste_niveau="vif"
            ),
            "decouverte_harmonieuse": PaletteSpiritulle(
                nom="Découverte Harmonieuse",
                couleurs_primaires=["#98FB98", "#87CEEB", "#DDA0DD"],
                couleurs_secondaires=["#F0E68C", "#FFB6C1", "#B0E0E6"],
                couleur_accent="#87CEEB",
                couleur_fond="#F0F8FF",
                couleur_texte="#2F4F4F",
                opacite_base=0.7,
                contraste_niveau="doux"
            ),
            "mystique_profond": PaletteSpiritulle(
                nom="Mystique Profond",
                couleurs_primaires=["#4B0082", "#8B008B", "#9400D3"],
                couleurs_secondaires=["#6A5ACD", "#7B68EE", "#9370DB"],
                couleur_accent="#9400D3",
                couleur_fond="#191970",
                couleur_texte="#E6E6FA",
                opacite_base=0.8,
                contraste_niveau="mystique"
            )
        }
    
    def _creer_themes_predefinis(self) -> Dict[str, ThemeVisuel]:
        """Crée les thèmes visuels prédéfinis"""
        themes = {}
        
        for nom_palette, palette in self.palettes_base.items():
            # Déterminer le style d'animation selon la palette
            if "cosmique" in nom_palette:
                style_anim = StyleAnimation.DYNAMIQUE
                fps = 60
                duree_trans = 0.8
                intensite = 0.9
                geometrie = "spirale_cosmique"
                decoratifs = ["etoiles", "particules", "nebuleuses"]
            elif "contemplative" in nom_palette:
                style_anim = StyleAnimation.CONTEMPLATIF
                fps = 30
                duree_trans = 1.5
                intensite = 0.6
                geometrie = "cercles_concentriques"
                decoratifs = ["lotus", "mandalas", "ondulations"]
            elif "artistique" in nom_palette:
                style_anim = StyleAnimation.EXPRESSIF
                fps = 45
                duree_trans = 1.0
                intensite = 0.95
                geometrie = "formes_libres"
                decoratifs = ["pinceaux", "eclats", "tourbillons"]
            elif "harmonieuse" in nom_palette:
                style_anim = StyleAnimation.EQUILIBRE
                fps = 40
                duree_trans = 1.2
                intensite = 0.7
                geometrie = "geometrie_sacree"
                decoratifs = ["petales", "rayons", "cristaux"]
            else:  # mystique
                style_anim = StyleAnimation.FLUIDE
                fps = 35
                duree_trans = 2.0
                intensite = 0.8
                geometrie = "fractales_mystiques"
                decoratifs = ["runes", "symboles", "auras"]
            
            theme = ThemeVisuel(
                nom=palette.nom,
                palette=palette,
                style_animation=style_anim,
                fps_cible=fps,
                duree_transitions=duree_trans,
                intensite_effets=intensite,
                geometrie_preferee=geometrie,
                elements_decoratifs=decoratifs
            )
            
            themes[nom_palette] = theme
        
        return themes
    
    def creer_theme_personnalise(self, profil: ProfilUtilisateur, 
                                contexte: Dict[str, Any] = None) -> ThemeVisuel:
        """
        🎨 Crée un thème personnalisé selon le profil utilisateur
        
        Args:
            profil: Profil utilisateur complet
            contexte: Contexte additionnel (session, préférences, etc.)
            
        Returns:
            Thème visuel personnalisé
        """
        if contexte is None:
            contexte = {}
        
        # Analyser le profil pour déterminer les préférences
        preferences = self._analyser_preferences_visuelles(profil, contexte)
        
        # Créer une palette personnalisée
        palette_personnalisee = self._creer_palette_personnalisee(preferences)
        
        # Déterminer le style d'animation optimal
        style_animation = self._determiner_style_animation(preferences)
        
        # Calculer les paramètres techniques
        parametres_tech = self._calculer_parametres_techniques(preferences)
        
        # Créer le thème personnalisé
        theme_personnalise = ThemeVisuel(
            nom=f"Personnalisé_{profil.profil_spirituel.archetyp_spirituel}_{profil.type_utilisateur.value}",
            palette=palette_personnalisee,
            style_animation=style_animation,
            fps_cible=parametres_tech["fps"],
            duree_transitions=parametres_tech["duree_transitions"],
            intensite_effets=parametres_tech["intensite_effets"],
            geometrie_preferee=preferences["geometrie_preferee"],
            elements_decoratifs=preferences["elements_decoratifs"]
        )
        
        # Mettre en cache
        cle_cache = f"{profil.type_utilisateur.value}_{profil.profil_spirituel.archetyp_spirituel}"
        self.themes_personnalises[cle_cache] = theme_personnalise
        
        return theme_personnalise
    
    def _analyser_preferences_visuelles(self, profil: ProfilUtilisateur, 
                                       contexte: Dict[str, Any]) -> Dict[str, Any]:
        """Analyse les préférences visuelles du profil"""
        preferences = {
            "niveau_complexite": (profil.niveau_technique + profil.profil_spirituel.niveau_eveil) / 2,
            "sensibilite_couleur": profil.profil_spirituel.sensibilite_energetique,
            "archetyp_principal": profil.profil_spirituel.archetyp_spirituel,
            "type_utilisateur": profil.type_utilisateur,
            "couleurs_resonantes": profil.profil_spirituel.couleurs_resonantes
        }
        
        # Déterminer la géométrie préférée
        if preferences["archetyp_principal"] == "explorateur":
            preferences["geometrie_preferee"] = "spirales_dynamiques"
            preferences["elements_decoratifs"] = ["boussoles", "etoiles", "trajectoires"]
        elif preferences["archetyp_principal"] == "sage":
            preferences["geometrie_preferee"] = "mandalas_traditionnels"
            preferences["elements_decoratifs"] = ["lotus", "arbres", "cercles_sagesse"]
        elif preferences["archetyp_principal"] == "créateur":
            preferences["geometrie_preferee"] = "formes_organiques"
            preferences["elements_decoratifs"] = ["pinceaux", "palettes", "eclats_creatifs"]
        else:
            preferences["geometrie_preferee"] = "geometrie_equilibree"
            preferences["elements_decoratifs"] = ["cristaux", "rayons", "harmonies"]
        
        # Ajuster selon le contexte
        if contexte.get("mode_focus", False):
            preferences["intensite_preferee"] = 0.6
        elif contexte.get("mode_celebration", False):
            preferences["intensite_preferee"] = 0.95
        else:
            preferences["intensite_preferee"] = 0.8
        
        return preferences
    
    def _creer_palette_personnalisee(self, preferences: Dict[str, Any]) -> PaletteSpiritulle:
        """Crée une palette personnalisée selon les préférences"""
        # Utiliser les couleurs résonnantes comme base
        couleurs_base = preferences.get("couleurs_resonantes", ["#87CEEB", "#98FB98", "#DDA0DD"])
        
        # Générer une harmonie de couleurs
        if len(couleurs_base) >= 3:
            couleur_principale = couleurs_base[0]
            harmonie = self._generer_harmonie_triadique(couleur_principale)
        else:
            couleur_principale = couleurs_base[0] if couleurs_base else "#87CEEB"
            harmonie = self._generer_harmonie_analogique(couleur_principale)
        
        # Adapter l'intensité selon la sensibilité
        sensibilite = preferences["sensibilite_couleur"]
        if sensibilite > 0.8:
            opacite = 0.6
            contraste = "tres_doux"
        elif sensibilite > 0.6:
            opacite = 0.75
            contraste = "doux"
        else:
            opacite = 0.85
            contraste = "normal"
        
        # Déterminer les couleurs de fond et texte
        if preferences["niveau_complexite"] > 7:
            couleur_fond = "#0F0F23"  # Sombre pour les experts
            couleur_texte = "#E6E6FA"
        else:
            couleur_fond = "#F0F8FF"  # Clair pour les novices
            couleur_texte = "#2F4F4F"
        
        return PaletteSpiritulle(
            nom=f"Personnalisée_{preferences['archetyp_principal']}",
            couleurs_primaires=harmonie["primaires"],
            couleurs_secondaires=harmonie["secondaires"],
            couleur_accent=harmonie["accent"],
            couleur_fond=couleur_fond,
            couleur_texte=couleur_texte,
            opacite_base=opacite,
            contraste_niveau=contraste
        )
    
    def _determiner_style_animation(self, preferences: Dict[str, Any]) -> StyleAnimation:
        """Détermine le style d'animation optimal"""
        archetyp = preferences["archetyp_principal"]
        niveau_complexite = preferences["niveau_complexite"]
        
        if archetyp == "explorateur" and niveau_complexite > 6:
            return StyleAnimation.DYNAMIQUE
        elif archetyp == "sage":
            return StyleAnimation.CONTEMPLATIF
        elif archetyp == "créateur":
            return StyleAnimation.EXPRESSIF
        elif niveau_complexite < 4:
            return StyleAnimation.FLUIDE
        else:
            return StyleAnimation.EQUILIBRE
    
    def _calculer_parametres_techniques(self, preferences: Dict[str, Any]) -> Dict[str, Any]:
        """Calcule les paramètres techniques optimaux"""
        sensibilite = preferences["sensibilite_couleur"]
        niveau_complexite = preferences["niveau_complexite"]
        intensite_preferee = preferences["intensite_preferee"]
        
        # FPS adaptatif
        fps_base = 30
        if niveau_complexite > 7:
            fps_base = 60
        elif niveau_complexite > 5:
            fps_base = 45
        
        fps_final = int(fps_base * (0.5 + sensibilite * 0.5))
        
        # Durée des transitions
        if sensibilite > 0.8:
            duree_transitions = 2.0  # Plus lent pour les sensibles
        elif niveau_complexite > 7:
            duree_transitions = 0.6  # Plus rapide pour les experts
        else:
            duree_transitions = 1.2
        
        return {
            "fps": fps_final,
            "duree_transitions": duree_transitions,
            "intensite_effets": intensite_preferee
        }
    
    def _generer_harmonie_complementaire(self, couleur_base: str) -> Dict[str, List[str]]:
        """Génère une harmonie de couleurs complémentaires"""
        # Convertir hex en HSV
        r, g, b = self._hex_to_rgb(couleur_base)
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        # Couleur complémentaire (opposée sur le cercle chromatique)
        h_comp = (h + 0.5) % 1.0
        
        # Générer la palette
        couleurs_primaires = [
            couleur_base,
            self._hsv_to_hex(h_comp, s, v),
            self._hsv_to_hex(h, s*0.7, v*0.9)
        ]
        
        couleurs_secondaires = [
            self._hsv_to_hex((h + 0.1) % 1.0, s*0.8, v*0.8),
            self._hsv_to_hex((h_comp + 0.1) % 1.0, s*0.8, v*0.8),
            self._hsv_to_hex(h, s*0.5, v*1.1 if v < 0.9 else 1.0)
        ]
        
        return {
            "primaires": couleurs_primaires,
            "secondaires": couleurs_secondaires,
            "accent": couleurs_primaires[1]
        }
    
    def _generer_harmonie_triadique(self, couleur_base: str) -> Dict[str, List[str]]:
        """Génère une harmonie triadique"""
        r, g, b = self._hex_to_rgb(couleur_base)
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        # Couleurs triadiques (120° d'écart)
        h2 = (h + 1/3) % 1.0
        h3 = (h + 2/3) % 1.0
        
        couleurs_primaires = [
            couleur_base,
            self._hsv_to_hex(h2, s, v),
            self._hsv_to_hex(h3, s, v)
        ]
        
        couleurs_secondaires = [
            self._hsv_to_hex(h, s*0.6, v*0.9),
            self._hsv_to_hex(h2, s*0.6, v*0.9),
            self._hsv_to_hex(h3, s*0.6, v*0.9)
        ]
        
        return {
            "primaires": couleurs_primaires,
            "secondaires": couleurs_secondaires,
            "accent": couleurs_primaires[2]
        }
    
    def _generer_harmonie_analogique(self, couleur_base: str) -> Dict[str, List[str]]:
        """Génère une harmonie analogique"""
        r, g, b = self._hex_to_rgb(couleur_base)
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        # Couleurs analogiques (30° d'écart)
        h_moins = (h - 1/12) % 1.0
        h_plus = (h + 1/12) % 1.0
        
        couleurs_primaires = [
            self._hsv_to_hex(h_moins, s, v),
            couleur_base,
            self._hsv_to_hex(h_plus, s, v)
        ]
        
        couleurs_secondaires = [
            self._hsv_to_hex(h_moins, s*0.7, v*0.8),
            self._hsv_to_hex(h, s*0.7, v*0.8),
            self._hsv_to_hex(h_plus, s*0.7, v*0.8)
        ]
        
        return {
            "primaires": couleurs_primaires,
            "secondaires": couleurs_secondaires,
            "accent": couleurs_primaires[1]
        }
    
    def _generer_harmonie_monochromatique(self, couleur_base: str) -> Dict[str, List[str]]:
        """Génère une harmonie monochromatique"""
        r, g, b = self._hex_to_rgb(couleur_base)
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        couleurs_primaires = [
            self._hsv_to_hex(h, s*0.8, v*0.6),
            couleur_base,
            self._hsv_to_hex(h, s*1.2 if s < 0.8 else 1.0, v*1.2 if v < 0.8 else 1.0)
        ]
        
        couleurs_secondaires = [
            self._hsv_to_hex(h, s*0.4, v*0.8),
            self._hsv_to_hex(h, s*0.6, v*0.9),
            self._hsv_to_hex(h, s*0.9, v*0.7)
        ]
        
        return {
            "primaires": couleurs_primaires,
            "secondaires": couleurs_secondaires,
            "accent": couleurs_primaires[2]
        }
    
    def _hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """Convertit une couleur hex en RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _hsv_to_hex(self, h: float, s: float, v: float) -> str:
        """Convertit HSV en hex"""
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    
    def obtenir_theme_optimal(self, profil: ProfilUtilisateur, 
                             contexte: Dict[str, Any] = None) -> ThemeVisuel:
        """
        🎯 Obtient le thème optimal pour un profil donné
        
        Args:
            profil: Profil utilisateur
            contexte: Contexte additionnel
            
        Returns:
            Thème visuel optimal
        """
        # Vérifier le cache
        cle_cache = f"{profil.type_utilisateur.value}_{profil.profil_spirituel.archetyp_spirituel}"
        if cle_cache in self.themes_personnalises:
            return self.themes_personnalises[cle_cache]
        
        # Essayer les thèmes prédéfinis
        archetyp = profil.profil_spirituel.archetyp_spirituel
        
        if archetyp == "explorateur":
            theme_base = "aventure_cosmique"
        elif archetyp == "sage":
            theme_base = "sagesse_contemplative"
        elif archetyp == "créateur":
            theme_base = "creation_artistique"
        else:
            theme_base = "decouverte_harmonieuse"
        
        if theme_base in self.themes_predefinis:
            return self.themes_predefinis[theme_base]
        
        # Créer un thème personnalisé
        return self.creer_theme_personnalise(profil, contexte)
    
    def obtenir_themes_disponibles(self) -> Dict[str, str]:
        """Retourne la liste des thèmes disponibles"""
        themes_disponibles = {}
        
        # Thèmes prédéfinis
        for nom, theme in self.themes_predefinis.items():
            themes_disponibles[nom] = theme.nom
        
        # Thèmes personnalisés
        for nom, theme in self.themes_personnalises.items():
            themes_disponibles[f"personnalise_{nom}"] = theme.nom
        
        return themes_disponibles

# Instance globale
gestionnaire_themes = GestionnaireThemesVisuels()