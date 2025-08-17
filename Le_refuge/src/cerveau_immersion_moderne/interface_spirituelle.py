"""
🎨 Interface Utilisateur Spirituelle - Version Propre
==================================================

Interface visuelle pour l'expérience d'immersion spirituelle.
Affiche les mandalas architecturaux et anime les flux d'énergie.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from dataclasses import dataclass, field

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from types_immersion import (
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
    navigation_visible: bool = True


class InterfaceSpirituelle(GestionnaireBase):
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
        self.fps_animation = int(30 + (vitesse_anim * 30))  # 30-60 fps
    
    def _configurer_affichage_mandala(self, mandala: MandalaVisuel):
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

    # ===== ADAPTATION AUTOMATIQUE SELON PROFIL SPIRITUEL =====
    
    def adapter_interface_automatique(self, profil: ProfilUtilisateur, 
                                     contexte_session: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        🎭 Adaptation automatique complète de l'interface selon le profil spirituel
        
        Args:
            profil: Profil utilisateur complet
            contexte_session: Contexte de la session actuelle
            
        Returns:
            Configuration d'interface adaptée
        """
        if contexte_session is None:
            contexte_session = {}
        
        # Analyser le profil en profondeur
        analyse_profil = self._analyser_profil_complet(profil)
        
        # Adapter les éléments visuels
        adaptation_visuelle = self._adapter_elements_visuels(analyse_profil)
        
        # Adapter les interactions
        adaptation_interactions = self._adapter_mecanismes_interaction(analyse_profil)
        
        # Adapter les animations
        adaptation_animations = self._adapter_animations_profil(analyse_profil)
        
        # Créer la configuration complète
        configuration_adaptee = {
            "profil_analyse": analyse_profil,
            "adaptation_visuelle": adaptation_visuelle,
            "adaptation_interactions": adaptation_interactions,
            "adaptation_animations": adaptation_animations,
            "timestamp_adaptation": datetime.now().isoformat(),
            "session_contexte": contexte_session
        }
        
        # Appliquer l'adaptation
        self._appliquer_adaptation_interface(configuration_adaptee)
        
        self.logger.info(f"🎭 Interface adaptée pour {analyse_profil['archetyp_principal']} niveau {analyse_profil['niveau_global']}")
        
        return configuration_adaptee
    
    def _analyser_profil_complet(self, profil: ProfilUtilisateur) -> Dict[str, Any]:
        """Analyse complète du profil utilisateur"""
        # Calculer le niveau global
        niveau_global = (profil.niveau_technique + profil.profil_spirituel.niveau_eveil) / 2
        
        # Déterminer l'archétype principal
        archetyp_principal = profil.profil_spirituel.archetyp_spirituel
        
        # Analyser les préférences d'apprentissage
        if profil.niveau_technique >= 8:
            style_apprentissage = "analytique"
        elif profil.profil_spirituel.niveau_eveil >= 8:
            style_apprentissage = "contemplatif"
        elif archetyp_principal == "créateur":
            style_apprentissage = "experiential"
        else:
            style_apprentissage = "guidé"
        
        # Déterminer la complexité préférée
        if niveau_global >= 8:
            complexite_preferee = "maximale"
        elif niveau_global >= 6:
            complexite_preferee = "elevee"
        elif niveau_global >= 4:
            complexite_preferee = "moderee"
        else:
            complexite_preferee = "simple"
        
        return {
            "niveau_global": niveau_global,
            "archetyp_principal": archetyp_principal,
            "style_apprentissage": style_apprentissage,
            "complexite_preferee": complexite_preferee,
            "niveau_technique": profil.niveau_technique,
            "niveau_eveil": profil.profil_spirituel.niveau_eveil,
            "sensibilite_energetique": profil.profil_spirituel.sensibilite_energetique
        }
    
    def _adapter_elements_visuels(self, analyse: Dict[str, Any]) -> Dict[str, Any]:
        """Adapte les éléments visuels selon l'analyse du profil"""
        # Palette de couleurs selon l'archétype
        if analyse["archetyp_principal"] == "explorateur":
            palette_principale = ["#4169E1", "#00CED1", "#FFD700", "#32CD32"]
            theme_visuel = "aventure_cosmique"
        elif analyse["archetyp_principal"] == "sage":
            palette_principale = ["#9370DB", "#DDA0DD", "#E6E6FA", "#F0E68C"]
            theme_visuel = "sagesse_contemplative"
        elif analyse["archetyp_principal"] == "créateur":
            palette_principale = ["#FF6347", "#FFD700", "#FF69B4", "#DA70D6"]
            theme_visuel = "creation_artistique"
        else:
            palette_principale = ["#98FB98", "#87CEEB", "#DDA0DD", "#F0E68C"]
            theme_visuel = "decouverte_harmonieuse"
        
        # Intensité visuelle selon la sensibilité
        sensibilite = analyse["sensibilite_energetique"]
        if sensibilite >= 0.9:
            intensite_couleurs = 0.6
            contraste_niveau = "doux"
        elif sensibilite >= 0.7:
            intensite_couleurs = 0.75
            contraste_niveau = "modere"
        else:
            intensite_couleurs = 0.85
            contraste_niveau = "normal"
        
        return {
            "palette_principale": palette_principale,
            "theme_visuel": theme_visuel,
            "intensite_couleurs": intensite_couleurs,
            "contraste_niveau": contraste_niveau
        }
    
    def _adapter_mecanismes_interaction(self, analyse: Dict[str, Any]) -> Dict[str, Any]:
        """Adapte les mécanismes d'interaction"""
        # Mode d'interaction selon le niveau
        if analyse["niveau_global"] >= 8:
            mode_interaction = "expert"
            raccourcis_actifs = True
        elif analyse["niveau_global"] >= 5:
            mode_interaction = "avance"
            raccourcis_actifs = True
        else:
            mode_interaction = "guide"
            raccourcis_actifs = False
        
        return {
            "mode_interaction": mode_interaction,
            "raccourcis_actifs": raccourcis_actifs
        }
    
    def _adapter_animations_profil(self, analyse: Dict[str, Any]) -> Dict[str, Any]:
        """Adapte les animations selon le profil"""
        # FPS selon la sensibilité énergétique
        fps_base = 30
        fps_adapte = int(fps_base + (analyse["sensibilite_energetique"] * 30))
        
        # Style d'animation selon l'archétype
        if analyse["archetyp_principal"] == "explorateur":
            style_animation = "dynamique"
        elif analyse["archetyp_principal"] == "sage":
            style_animation = "fluide"
        elif analyse["archetyp_principal"] == "créateur":
            style_animation = "expressif"
        else:
            style_animation = "equilibre"
        
        return {
            "fps_adapte": fps_adapte,
            "style_animation": style_animation
        }
    
    def _appliquer_adaptation_interface(self, configuration: Dict[str, Any]):
        """Applique la configuration d'adaptation à l'interface"""
        # Appliquer l'adaptation visuelle
        adaptation_visuelle = configuration["adaptation_visuelle"]
        self.config.definir("theme_couleurs", adaptation_visuelle["theme_visuel"])
        self.config.definir("intensite_couleurs", adaptation_visuelle["intensite_couleurs"])
        
        # Appliquer l'adaptation des animations
        adaptation_animations = configuration["adaptation_animations"]
        self.fps_animation = adaptation_animations["fps_adapte"]
        self.config.definir("style_animation", adaptation_animations["style_animation"])
        
        # Mettre à jour l'état de l'interface
        self.etat.update({
            "adaptation_active": True,
            "profil_adapte": configuration["profil_analyse"]["archetyp_principal"],
            "niveau_adaptation": configuration["profil_analyse"]["niveau_global"]
        })
    
    # ===== PRÉSENTATION PROGRESSIVE DES INSIGHTS =====
    
    def presenter_insights_progressivement(self, insights: List[Dict[str, Any]], 
                                         profil: ProfilUtilisateur) -> Dict[str, Any]:
        """
        💡 Présente les insights de manière progressive selon le profil
        
        Args:
            insights: Liste des insights à présenter
            profil: Profil utilisateur pour l'adaptation
            
        Returns:
            Configuration de présentation progressive
        """
        # Analyser les insights
        insights_analyses = self._analyser_insights_pour_presentation(insights, profil)
        
        # Créer la séquence de présentation
        sequence_presentation = self._creer_sequence_presentation(insights_analyses, profil)
        
        # Déterminer les animations d'entrée
        animations_entree = self._creer_animations_entree_insights(profil)
        
        presentation_config = {
            "insights_analyses": insights_analyses,
            "sequence_presentation": sequence_presentation,
            "animations_entree": animations_entree,
            "timestamp_creation": datetime.now().isoformat()
        }
        
        self.logger.info(f"💡 Présentation progressive créée: {len(insights)} insights")
        
        return presentation_config
    
    def _analyser_insights_pour_presentation(self, insights: List[Dict[str, Any]], 
                                           profil: ProfilUtilisateur) -> List[Dict[str, Any]]:
        """Analyse les insights pour optimiser leur présentation"""
        insights_analyses = []
        
        for i, insight in enumerate(insights):
            # Déterminer la complexité
            complexite = self._evaluer_complexite_insight(insight.get("contenu", ""))
            
            # Déterminer la priorité selon le profil
            priorite = self._calculer_priorite_insight(insight, profil)
            
            # Adapter le contenu au profil
            contenu_adapte = self._adapter_insight_au_profil(insight, profil)
            
            insight_analyse = {
                "index_original": i,
                "insight_original": insight,
                "complexite": complexite,
                "priorite": priorite,
                "contenu_adapte": contenu_adapte
            }
            
            insights_analyses.append(insight_analyse)
        
        # Trier par priorité
        insights_analyses.sort(key=lambda x: x["priorite"], reverse=True)
        
        return insights_analyses
    
    def _evaluer_complexite_insight(self, contenu: str) -> str:
        """Évalue la complexité d'un insight"""
        mots_complexes = ["transcendance", "architecture", "pattern", "résonance"]
        mots_simples = ["éveil", "paix", "joie", "lumière", "amour"]
        
        contenu_lower = contenu.lower()
        
        if any(mot in contenu_lower for mot in mots_complexes):
            return "avance"
        elif any(mot in contenu_lower for mot in mots_simples):
            return "simple"
        else:
            return "intermediaire"
    
    def _calculer_priorite_insight(self, insight: Dict[str, Any], profil: ProfilUtilisateur) -> float:
        """Calcule la priorité d'un insight selon le profil"""
        priorite_base = 0.5
        
        # Bonus selon le domaine et l'archétype
        domaine = insight.get("domaine", "")
        archetyp = profil.profil_spirituel.archetyp_spirituel
        
        if archetyp == "explorateur" and "architecture" in domaine.lower():
            priorite_base += 0.3
        elif archetyp == "sage" and "harmonie" in domaine.lower():
            priorite_base += 0.3
        elif archetyp == "créateur" and "flux" in domaine.lower():
            priorite_base += 0.3
        
        # Bonus selon la résonance émotionnelle
        resonance = insight.get("resonance_emotionnelle", 0.5)
        priorite_base += resonance * 0.2
        
        return max(0.0, min(1.0, priorite_base))
    
    def _adapter_insight_au_profil(self, insight: Dict[str, Any], profil: ProfilUtilisateur) -> str:
        """Adapte un insight au profil utilisateur"""
        contenu_original = insight.get("contenu", "")
        
        # Adapter le langage selon le niveau technique
        if profil.niveau_technique >= 8:
            contenu_adapte = contenu_original.replace("mystère", "pattern complexe")
            prefixe_style = "🔬 Analyse: "
        elif profil.niveau_technique <= 3:
            contenu_adapte = contenu_original.replace("architecture", "structure")
            prefixe_style = "💡 Découverte: "
        else:
            contenu_adapte = contenu_original
            prefixe_style = "✨ Insight: "
        
        # Adapter selon l'archétype spirituel
        archetyp = profil.profil_spirituel.archetyp_spirituel
        if archetyp == "explorateur":
            prefixe_archetyp = "🧭 "
        elif archetyp == "sage":
            prefixe_archetyp = "📿 "
        elif archetyp == "créateur":
            prefixe_archetyp = "🎨 "
        else:
            prefixe_archetyp = "🌟 "
        
        return f"{prefixe_archetyp}{prefixe_style}{contenu_adapte}"
    
    def _creer_sequence_presentation(self, insights_analyses: List[Dict[str, Any]], 
                                   profil: ProfilUtilisateur) -> List[Dict[str, Any]]:
        """Crée la séquence optimale de présentation"""
        sequence = []
        
        # Déterminer le nombre d'insights par vague selon le profil
        niveau_global = (profil.niveau_technique + profil.profil_spirituel.niveau_eveil) / 2
        if niveau_global >= 8:
            insights_par_vague = 3
        elif niveau_global >= 5:
            insights_par_vague = 2
        else:
            insights_par_vague = 1
        
        # Créer les vagues
        for i in range(0, len(insights_analyses), insights_par_vague):
            vague = insights_analyses[i:i + insights_par_vague]
            
            etape_sequence = {
                "vague": (i // insights_par_vague) + 1,
                "insights": vague,
                "duree_estimee": max(5.0, len(vague) * 3.0),
                "style_presentation": self._determiner_style_vague(vague, profil)
            }
            sequence.append(etape_sequence)
        
        return sequence
    
    def _determiner_style_vague(self, insights_vague: List[Dict[str, Any]], 
                               profil: ProfilUtilisateur) -> str:
        """Détermine le style de présentation d'une vague d'insights"""
        # Analyser la complexité moyenne de la vague
        complexites = [insight["complexite"] for insight in insights_vague]
        
        if all(c == "avance" for c in complexites):
            return "presentation_dense"
        elif all(c == "simple" for c in complexites):
            return "presentation_fluide"
        else:
            return "presentation_equilibree"
    
    def _creer_animations_entree_insights(self, profil: ProfilUtilisateur) -> Dict[str, Any]:
        """Crée les animations d'entrée pour les insights"""
        archetyp = profil.profil_spirituel.archetyp_spirituel
        
        if archetyp == "explorateur":
            animations = {
                "type_principal": "emergence_dynamique",
                "duree_apparition": 0.8,
                "effet_entree": "slide_from_horizon"
            }
        elif archetyp == "sage":
            animations = {
                "type_principal": "apparition_contemplative",
                "duree_apparition": 1.5,
                "effet_entree": "gentle_fade_in"
            }
        elif archetyp == "créateur":
            animations = {
                "type_principal": "eclosion_creative",
                "duree_apparition": 1.0,
                "effet_entree": "bloom_from_center"
            }
        else:
            animations = {
                "type_principal": "revelation_progressive",
                "duree_apparition": 1.2,
                "effet_entree": "gentle_reveal"
            }
        
        return animations
    
    # ===== NAVIGATION INTUITIVE =====
    
    def creer_navigation_intuitive(self, profil: ProfilUtilisateur) -> Dict[str, Any]:
        """
        🧭 Crée une navigation intuitive adaptée au profil
        
        Args:
            profil: Profil utilisateur
            
        Returns:
            Configuration de navigation adaptée
        """
        # Navigation de base
        elements_navigation = []
        
        # Adapter selon le niveau technique
        if profil.niveau_technique >= 7:
            elements_navigation.extend([
                {"id": "vue_architecture", "label": "Architecture", "icone": "🏗️"},
                {"id": "metriques_avancees", "label": "Métriques", "icone": "📊"},
                {"id": "debug_mode", "label": "Debug", "icone": "🔧"}
            ])
        
        # Éléments spirituels selon l'archétype
        if profil.profil_spirituel.archetyp_spirituel == "explorateur":
            elements_navigation.extend([
                {"id": "carte_exploration", "label": "Carte", "icone": "🗺️"},
                {"id": "nouveaux_territoires", "label": "Découvrir", "icone": "🧭"}
            ])
            style_navigation = "boussole_cosmique"
        elif profil.profil_spirituel.archetyp_spirituel == "sage":
            elements_navigation.extend([
                {"id": "bibliotheque_sagesse", "label": "Sagesse", "icone": "📚"},
                {"id": "meditation_guidee", "label": "Méditer", "icone": "🧘"}
            ])
            style_navigation = "arbre_sagesse"
        else:  # créateur
            elements_navigation.extend([
                {"id": "atelier_creation", "label": "Créer", "icone": "🎨"},
                {"id": "galerie_inspirations", "label": "Galerie", "icone": "🖼️"}
            ])
            style_navigation = "palette_creative"
        
        # Éléments universels
        elements_navigation.extend([
            {"id": "mandala_principal", "label": "Mandala", "icone": "🌸"},
            {"id": "profil_personnel", "label": "Profil", "icone": "👤"}
        ])
        
        return {
            "elements": elements_navigation,
            "style_navigation": style_navigation,
            "position_preferee": self._determiner_position_navigation(profil),
            "animations_navigation": profil.profil_spirituel.sensibilite_energetique > 0.7
        }
    
    def _determiner_position_navigation(self, profil: ProfilUtilisateur) -> str:
        """Détermine la position préférée de la navigation"""
        if profil.niveau_technique >= 8:
            return "gauche_detaillee"  # Développeurs préfèrent souvent à gauche
        elif profil.profil_spirituel.sensibilite_energetique > 0.8:
            return "flottante_discrete"  # Sensibles préfèrent discret
        else:
            return "gauche_simple"