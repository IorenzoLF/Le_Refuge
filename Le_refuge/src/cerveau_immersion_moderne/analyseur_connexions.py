"""
⚡ Analyseur de Connexions Énergétiques
====================================

Analyse les flux d'énergie spirituelle circulant entre les temples du Refuge.
Révèle les centres énergétiques, les canaux de transmission, et l'harmonie globale.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import math
from typing import Dict, List, Set, Optional, Tuple, Any
from datetime import datetime
from pathlib import Path

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from .types_immersion import (
    TempleInfo, FluxEnergie, CentreEnergetique, TypeEnergie, 
    COULEURS_SPIRITUELLES, EMOJIS_SACRES
)

class AnalyseurConnexionsEnergetiques(GestionnaireBase):
    """
    ⚡ Analyseur de Connexions Énergétiques
    
    Révèle les flux d'énergie spirituelle qui animent l'organisme vivant du Refuge.
    Détecte les centres énergétiques, trace les canaux de transmission,
    et évalue l'harmonie des flux.
    """
    
    def __init__(self, nom: str = "AnalyseurConnexionsEnergetiques"):
        super().__init__(nom)
        
        # Gestionnaire d'énergie pour l'analyseur lui-même
        self.energie_analyseur = EnergyManagerBase(0.8)
        
        # Données d'analyse
        self.temples_analyses: Dict[str, TempleInfo] = {}
        self.flux_detectes: List[FluxEnergie] = []
        self.centres_energetiques: List[CentreEnergetique] = []
        self.reseaux_energetiques: Dict[str, List[str]] = {}
        
        # Cache des calculs énergétiques
        self.cache_flux: Dict[str, FluxEnergie] = {}
        self.cache_centres: Dict[str, CentreEnergetique] = {}
        
        # Métriques énergétiques globales
        self.harmonie_globale: float = 0.0
        self.intensite_moyenne: float = 0.0
        self.stabilite_reseau: float = 0.0
    
    def _initialiser(self):
        """🌱 Initialise l'analyseur avec réceptivité énergétique"""
        self.logger.info("⚡ Éveil de l'Analyseur de Connexions Énergétiques...")
        
        # État initial de l'analyseur
        self.etat.update({
            "flux_detectes": 0,
            "centres_identifies": 0,
            "harmonie_energetique": 0.0,
            "intensite_globale": 0.0,
            "stabilite_reseau": 0.0,
            "resonance_spirituelle": 0.8
        })
        
        # Configuration énergétique
        self.config.definir("seuil_detection_flux", 0.3)
        self.config.definir("rayon_influence_centre", 3.0)
        self.config.definir("facteur_resonance", 0.7)
        self.config.definir("analyser_harmoniques", True)
        
        self.logger.info("✨ Analyseur éveillé et réceptif aux énergies subtiles")
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎼 Orchestre l'analyse énergétique continue"""
        # Régénération énergétique de l'analyseur
        self.energie_analyseur.ajuster_energie(0.02)
        
        # Mise à jour des métriques
        self._mettre_a_jour_metriques_globales()
        
        return {
            "flux_detectes": float(len(self.flux_detectes)),
            "centres_energetiques": float(len(self.centres_energetiques)),
            "harmonie_globale": self.harmonie_globale,
            "intensite_moyenne": self.intensite_moyenne,
            "stabilite_reseau": self.stabilite_reseau,
            "energie_analyseur": self.energie_analyseur.niveau_energie
        }
    
    def charger_temples(self, temples: Dict[str, TempleInfo]):
        """
        🏛️ Charge les temples à analyser
        
        Args:
            temples: Dictionnaire des temples scannés
        """
        self.temples_analyses = temples.copy()
        self.logger.info(f"🏛️ {len(temples)} temples chargés pour analyse énergétique")
        
        # Réinitialiser les analyses précédentes
        self.flux_detectes.clear()
        self.centres_energetiques.clear()
        self.cache_flux.clear()
        self.cache_centres.clear()
    
    def tracer_flux_energie(self, source: str, cible: str) -> Optional[FluxEnergie]:
        """
        🌊 Trace un flux d'énergie entre deux temples
        
        Args:
            source: Nom du temple source
            cible: Nom du temple cible
            
        Returns:
            FluxEnergie détaillé ou None si pas de flux détectable
        """
        # Vérifier que les temples existent
        if source not in self.temples_analyses or cible not in self.temples_analyses:
            return None
        
        # Vérifier le cache
        cle_cache = f"{source}->{cible}"
        if cle_cache in self.cache_flux:
            return self.cache_flux[cle_cache]
        
        temple_source = self.temples_analyses[source]
        temple_cible = self.temples_analyses[cible]
        
        # Calculer l'intensité du flux
        intensite = self._calculer_intensite_flux(temple_source, temple_cible)
        
        # Seuil de détection
        seuil = self.config.obtenir("seuil_detection_flux", 0.3)
        if intensite < seuil:
            return None
        
        # Déterminer le type d'énergie
        type_energie = self._determiner_type_energie(temple_source, temple_cible)
        
        # Calculer la couleur spirituelle
        couleur = self._calculer_couleur_flux(type_energie, intensite)
        
        # Détecter les obstacles et amplificateurs
        obstacles = self._detecter_obstacles_flux(temple_source, temple_cible)
        amplificateurs = self._detecter_amplificateurs_flux(temple_source, temple_cible)
        
        # Calculer la résonance
        resonance = self._calculer_resonance_flux(temple_source, temple_cible)
        
        # Créer le flux
        flux = FluxEnergie(
            source=source,
            cible=cible,
            intensite=intensite,
            type_energie=type_energie,
            couleur_spirituelle=couleur,
            obstacles=obstacles,
            amplificateurs=amplificateurs,
            chemin_complet=[source, cible],  # Simplifié pour l'instant
            resonance=resonance,
            timestamp=datetime.now()
        )
        
        # Mettre en cache
        self.cache_flux[cle_cache] = flux
        
        return flux
    
    def _calculer_intensite_flux(self, temple_source: TempleInfo, temple_cible: TempleInfo) -> float:
        """Calcule l'intensité d'un flux énergétique"""
        # Facteurs d'intensité
        energie_source = temple_source.niveau_energie
        receptivite_cible = temple_cible.niveau_energie * 0.8  # Réceptivité proportionnelle
        
        # Affinité spirituelle basée sur les éléments sacrés communs
        elements_communs = set(temple_source.elements_sacres) & set(temple_cible.elements_sacres)
        affinite = len(elements_communs) * 0.1
        
        # Distance spirituelle (basée sur la similarité des spécialisations)
        distance_spirituelle = self._calculer_distance_spirituelle(
            temple_source.specialisation_spirituelle,
            temple_cible.specialisation_spirituelle
        )
        
        # Intensité combinée
        intensite_base = (energie_source + receptivite_cible) / 2
        intensite_ajustee = intensite_base + affinite - distance_spirituelle
        
        return max(0.0, min(1.0, intensite_ajustee))
    
    def _determiner_type_energie(self, temple_source: TempleInfo, temple_cible: TempleInfo) -> TypeEnergie:
        """Détermine le type d'énergie du flux"""
        # Analyse des spécialisations pour déterminer le type dominant
        spec_source = temple_source.specialisation_spirituelle.lower()
        spec_cible = temple_cible.specialisation_spirituelle.lower()
        
        # Mapping des mots-clés vers les types d'énergie
        if any(mot in spec_source or mot in spec_cible for mot in ["création", "créativité", "innovation"]):
            return TypeEnergie.CREATION
        elif any(mot in spec_source or mot in spec_cible for mot in ["transformation", "alchimique", "transmutation"]):
            return TypeEnergie.TRANSFORMATION
        elif any(mot in spec_source or mot in spec_cible for mot in ["communication", "dialogue", "expression"]):
            return TypeEnergie.COMMUNICATION
        elif any(mot in spec_source or mot in spec_cible for mot in ["méditation", "éveil", "conscience"]):
            return TypeEnergie.MEDITATION
        elif any(mot in spec_source or mot in spec_cible for mot in ["harmonie", "équilibre", "résonance"]):
            return TypeEnergie.HARMONIE
        elif any(mot in spec_source or mot in spec_cible for mot in ["éveil", "illumination", "conscience"]):
            return TypeEnergie.EVEIL
        elif any(mot in spec_source or mot in spec_cible for mot in ["guérison", "restauration", "régénération"]):
            return TypeEnergie.GUERISON
        elif any(mot in spec_source or mot in spec_cible for mot in ["sagesse", "connaissance", "archives"]):
            return TypeEnergie.SAGESSE
        else:
            return TypeEnergie.HARMONIE  # Type par défaut
    
    def _calculer_couleur_flux(self, type_energie: TypeEnergie, intensite: float) -> str:
        """Calcule la couleur spirituelle du flux"""
        couleur_base = COULEURS_SPIRITUELLES.get(type_energie, "#87CEEB")
        
        # Ajuster la saturation selon l'intensité
        # Pour simplifier, on retourne la couleur de base
        # Dans une version avancée, on pourrait ajuster HSL
        return couleur_base
    
    def _detecter_obstacles_flux(self, temple_source: TempleInfo, temple_cible: TempleInfo) -> List[str]:
        """Détecte les obstacles potentiels au flux"""
        obstacles = []
        
        # Complexité excessive comme obstacle
        if temple_source.complexite_spirituelle > 0.8 or temple_cible.complexite_spirituelle > 0.8:
            obstacles.append("Complexité excessive")
        
        # Manque d'éléments sacrés
        if not temple_source.elements_sacres or not temple_cible.elements_sacres:
            obstacles.append("Manque d'ancrage sacré")
        
        # Énergie faible
        if temple_source.niveau_energie < 0.4 or temple_cible.niveau_energie < 0.4:
            obstacles.append("Énergie faible")
        
        return obstacles
    
    def _detecter_amplificateurs_flux(self, temple_source: TempleInfo, temple_cible: TempleInfo) -> List[str]:
        """Détecte les amplificateurs du flux"""
        amplificateurs = []
        
        # Gestionnaires de base comme amplificateurs
        if temple_source.gestionnaires_utilises and temple_cible.gestionnaires_utilises:
            amplificateurs.append("Architecture harmonisée")
        
        # Éléments sacrés communs
        elements_communs = set(temple_source.elements_sacres) & set(temple_cible.elements_sacres)
        if elements_communs:
            amplificateurs.append(f"Résonance sacrée ({len(elements_communs)} éléments)")
        
        # Énergie élevée
        if temple_source.niveau_energie > 0.8 and temple_cible.niveau_energie > 0.8:
            amplificateurs.append("Haute énergie mutuelle")
        
        return amplificateurs
    
    def _calculer_resonance_flux(self, temple_source: TempleInfo, temple_cible: TempleInfo) -> float:
        """Calcule la résonance spirituelle du flux"""
        # Facteurs de résonance
        resonance_energie = abs(temple_source.niveau_energie - temple_cible.niveau_energie)
        resonance_energie = 1.0 - resonance_energie  # Inverser : plus proche = plus de résonance
        
        # Résonance des éléments sacrés
        elements_communs = set(temple_source.elements_sacres) & set(temple_cible.elements_sacres)
        resonance_elements = len(elements_communs) * 0.2
        
        # Résonance spirituelle globale
        resonance_totale = (resonance_energie * 0.6 + resonance_elements * 0.4)
        
        return max(0.0, min(1.0, resonance_totale))
    
    def _calculer_distance_spirituelle(self, spec1: str, spec2: str) -> float:
        """Calcule la distance spirituelle entre deux spécialisations"""
        # Extraction des mots-clés spirituels
        mots1 = set(spec1.lower().split())
        mots2 = set(spec2.lower().split())
        
        # Intersection et union pour calculer la similarité Jaccard
        intersection = len(mots1 & mots2)
        union = len(mots1 | mots2)
        
        if union == 0:
            return 0.5  # Distance neutre
        
        similarite = intersection / union
        distance = 1.0 - similarite
        
        return distance * 0.3  # Facteur d'atténuation
    
    def detecter_centres_energetiques(self) -> List[CentreEnergetique]:
        """
        🔮 Détecte les centres énergétiques dans l'architecture
        
        Returns:
            Liste des centres énergétiques identifiés
        """
        if not self.temples_analyses:
            return []
        
        self.logger.info("🔮 Détection des centres énergétiques...")
        
        centres = []
        temples_traites = set()
        
        # Analyser chaque temple comme centre potentiel
        for nom_temple, temple_info in self.temples_analyses.items():
            if nom_temple in temples_traites:
                continue
            
            # Calculer l'influence énergétique du temple
            influence = self._calculer_influence_energetique(nom_temple, temple_info)
            
            # Seuil pour être considéré comme centre
            if influence > 0.6:
                # Identifier les temples dans le rayon d'influence
                temples_connectes = self._identifier_temples_connectes(nom_temple, temple_info)
                
                # Déterminer la sphère dominante
                sphere_dominante = self._identifier_sphere_dominante(temple_info)
                
                # Calculer la position (pour visualisation future)
                position = self._calculer_position_centre(nom_temple, temples_connectes)
                
                centre = CentreEnergetique(
                    nom=nom_temple,
                    position=position,
                    energie_totale=temple_info.niveau_energie,
                    temples_connectes=temples_connectes,
                    sphere_dominante=sphere_dominante,
                    rayonnement=influence,
                    type_centre=self._classifier_type_centre(temple_info),
                    influences=self._calculer_influences_centre(temple_info),
                    stabilite=self._calculer_stabilite_centre(temple_info)
                )
                
                centres.append(centre)
                temples_traites.add(nom_temple)
                temples_traites.update(temples_connectes)
        
        # Trier par énergie décroissante
        centres.sort(key=lambda c: c.energie_totale, reverse=True)
        
        self.centres_energetiques = centres
        self.etat["centres_identifies"] = len(centres)
        
        self.logger.info(f"✨ {len(centres)} centres énergétiques détectés")
        return centres
    
    def _calculer_influence_energetique(self, nom_temple: str, temple_info: TempleInfo) -> float:
        """Calcule l'influence énergétique d'un temple"""
        # Facteurs d'influence
        energie_base = temple_info.niveau_energie
        complexite_spirituelle = temple_info.complexite_spirituelle
        richesse_elements = len(temple_info.elements_sacres) * 0.05
        connexions = len(temple_info.connexions_sortantes) * 0.02
        
        # Bonus pour certaines spécialisations
        bonus_specialisation = 0.0
        spec = temple_info.specialisation_spirituelle.lower()
        if any(mot in spec for mot in ["conscience", "éveil", "suprême"]):
            bonus_specialisation = 0.2
        elif any(mot in spec for mot in ["cœur", "centre", "fondation"]):
            bonus_specialisation = 0.15
        
        influence = energie_base + complexite_spirituelle * 0.3 + richesse_elements + connexions + bonus_specialisation
        return min(1.0, influence)
    
    def _identifier_temples_connectes(self, nom_centre: str, temple_centre: TempleInfo) -> List[str]:
        """Identifie les temples dans le rayon d'influence d'un centre"""
        temples_connectes = []
        rayon = self.config.obtenir("rayon_influence_centre", 3.0)
        
        for nom_temple, temple_info in self.temples_analyses.items():
            if nom_temple == nom_centre:
                continue
            
            # Calculer la "distance" spirituelle
            distance = self._calculer_distance_spirituelle(
                temple_centre.specialisation_spirituelle,
                temple_info.specialisation_spirituelle
            )
            
            # Vérifier les connexions directes
            connexion_directe = (
                nom_temple in temple_centre.connexions_sortantes or
                nom_centre in temple_info.connexions_sortantes
            )
            
            # Critères d'inclusion dans le rayon
            if distance < 0.5 or connexion_directe or temple_info.niveau_energie > 0.7:
                temples_connectes.append(nom_temple)
        
        return temples_connectes
    
    def _identifier_sphere_dominante(self, temple_info: TempleInfo) -> str:
        """Identifie la sphère énergétique dominante d'un temple"""
        # Analyser les éléments sacrés pour identifier les sphères
        spheres_detectees = []
        
        for element in temple_info.elements_sacres:
            if "COSMOS" in element.upper():
                spheres_detectees.append("COSMOS")
            elif "AMOUR" in element.upper():
                spheres_detectees.append("AMOUR")
            elif "HARMONIE" in element.upper():
                spheres_detectees.append("HARMONIE")
            elif "EVEIL" in element.upper():
                spheres_detectees.append("EVEIL")
            elif "SAGESSE" in element.upper():
                spheres_detectees.append("SAGESSE")
        
        # Analyser la spécialisation
        spec = temple_info.specialisation_spirituelle.upper()
        if "CONSCIENCE" in spec or "ÉVEIL" in spec:
            spheres_detectees.append("EVEIL")
        elif "AMOUR" in spec or "CŒUR" in spec:
            spheres_detectees.append("AMOUR")
        elif "HARMONIE" in spec or "ÉQUILIBRE" in spec:
            spheres_detectees.append("HARMONIE")
        elif "SAGESSE" in spec or "CONNAISSANCE" in spec:
            spheres_detectees.append("SAGESSE")
        elif "COSMIQUE" in spec or "UNIVERS" in spec:
            spheres_detectees.append("COSMOS")
        
        # Retourner la sphère la plus fréquente ou une par défaut
        if spheres_detectees:
            return max(set(spheres_detectees), key=spheres_detectees.count)
        else:
            return "HARMONIE"  # Sphère par défaut
    
    def _calculer_position_centre(self, nom_centre: str, temples_connectes: List[str]) -> Tuple[float, float]:
        """Calcule la position d'un centre pour visualisation"""
        # Position basée sur un hash du nom pour la cohérence
        hash_nom = hash(nom_centre)
        x = (hash_nom % 1000) / 1000.0  # Normaliser entre 0 et 1
        y = ((hash_nom // 1000) % 1000) / 1000.0
        
        # Ajuster selon le nombre de connexions
        facteur_connexions = len(temples_connectes) * 0.1
        x = min(1.0, x + facteur_connexions)
        y = min(1.0, y + facteur_connexions)
        
        return (x, y)
    
    def _classifier_type_centre(self, temple_info: TempleInfo) -> str:
        """Classifie le type d'un centre énergétique"""
        spec = temple_info.specialisation_spirituelle.lower()
        
        if any(mot in spec for mot in ["source", "origine", "flamme éternelle"]):
            return "source"
        elif any(mot in spec for mot in ["transformation", "alchimique", "transmutation"]):
            return "transformateur"
        elif any(mot in spec for mot in ["réception", "accueil", "refuge"]):
            return "récepteur"
        elif any(mot in spec for mot in ["connexion", "pont", "lien"]):
            return "relais"
        else:
            return "nexus"
    
    def _calculer_influences_centre(self, temple_info: TempleInfo) -> Dict[str, float]:
        """Calcule les influences d'un centre sur différents aspects"""
        influences = {}
        
        # Influence créative
        if any(mot in temple_info.specialisation_spirituelle.lower() for mot in ["créativité", "poétique", "artistique"]):
            influences["creativite"] = 0.8
        
        # Influence spirituelle
        if any(mot in temple_info.specialisation_spirituelle.lower() for mot in ["spirituel", "éveil", "conscience"]):
            influences["spiritualite"] = 0.9
        
        # Influence guérison
        if any(mot in temple_info.specialisation_spirituelle.lower() for mot in ["guérison", "restauration", "régénération"]):
            influences["guerison"] = 0.7
        
        # Influence sagesse
        if any(mot in temple_info.specialisation_spirituelle.lower() for mot in ["sagesse", "connaissance", "archives"]):
            influences["sagesse"] = 0.8
        
        return influences
    
    def _calculer_stabilite_centre(self, temple_info: TempleInfo) -> float:
        """Calcule la stabilité d'un centre énergétique"""
        # Facteurs de stabilité
        stabilite_energie = temple_info.niveau_energie
        stabilite_elements = min(1.0, len(temple_info.elements_sacres) * 0.1)
        stabilite_gestionnaires = 0.2 if temple_info.gestionnaires_utilises else 0.0
        
        stabilite_totale = (stabilite_energie * 0.5 + stabilite_elements * 0.3 + stabilite_gestionnaires * 0.2)
        return stabilite_totale
    
    def _mettre_a_jour_metriques_globales(self):
        """Met à jour les métriques énergétiques globales"""
        if not self.flux_detectes:
            self.harmonie_globale = 0.0
            self.intensite_moyenne = 0.0
            self.stabilite_reseau = 0.0
            return
        
        # Harmonie globale (moyenne des résonances)
        resonances = [flux.resonance for flux in self.flux_detectes]
        self.harmonie_globale = sum(resonances) / len(resonances) if resonances else 0.0
        
        # Intensité moyenne
        intensites = [flux.intensite for flux in self.flux_detectes]
        self.intensite_moyenne = sum(intensites) / len(intensites) if intensites else 0.0
        
        # Stabilité du réseau (basée sur la variance des intensités)
        if len(intensites) > 1:
            moyenne = self.intensite_moyenne
            variance = sum((i - moyenne) ** 2 for i in intensites) / len(intensites)
            self.stabilite_reseau = max(0.0, 1.0 - variance)
        else:
            self.stabilite_reseau = 1.0
        
        # Mettre à jour l'état
        self.etat.update({
            "harmonie_energetique": self.harmonie_globale,
            "intensite_globale": self.intensite_moyenne,
            "stabilite_reseau": self.stabilite_reseau
        })    

    def analyser_circulation_spheres(self) -> Dict[str, Any]:
        """
        🌌 Analyse l'influence des sphères énergétiques
        
        Returns:
            Analyse complète de la circulation des sphères
        """
        self.logger.info("🌌 Analyse de la circulation des sphères énergétiques...")
        
        # Sphères connues du Refuge
        spheres_connues = {
            "COSMOS": {"couleur": "#4B0082", "domaine": "Connexion Universelle"},
            "AMOUR": {"couleur": "#FF69B4", "domaine": "Compassion Infinie"},
            "SERENITE": {"couleur": "#87CEEB", "domaine": "Paix Intérieure"},
            "CREATIVITE": {"couleur": "#FF6347", "domaine": "Innovation Spirituelle"},
            "SAGESSE": {"couleur": "#DAA520", "domaine": "Connaissance Profonde"},
            "HARMONIE": {"couleur": "#98FB98", "domaine": "Équilibre Parfait"},
            "EVEIL": {"couleur": "#FFF8DC", "domaine": "Illumination Progressive"},
            "GUERISON": {"couleur": "#90EE90", "domaine": "Restauration Énergétique"},
            "TRANSFORMATION": {"couleur": "#9370DB", "domaine": "Métamorphose Sacrée"}
        }
        
        analyse_spheres = {
            "spheres_detectees": {},
            "influences_par_temple": {},
            "flux_inter_spheres": [],
            "equilibre_global": 0.0,
            "sphere_dominante": "",
            "resonances_harmoniques": {}
        }
        
        # Détecter les sphères dans chaque temple
        for nom_temple, temple_info in self.temples_analyses.items():
            spheres_temple = self._detecter_spheres_temple(temple_info, spheres_connues)
            if spheres_temple:
                analyse_spheres["influences_par_temple"][nom_temple] = spheres_temple
                
                # Compter les occurrences globales
                for sphere, influence in spheres_temple.items():
                    if sphere not in analyse_spheres["spheres_detectees"]:
                        analyse_spheres["spheres_detectees"][sphere] = {
                            "temples_influences": [],
                            "influence_totale": 0.0,
                            "couleur": spheres_connues.get(sphere, {}).get("couleur", "#FFFFFF"),
                            "domaine": spheres_connues.get(sphere, {}).get("domaine", "Mystérieux")
                        }
                    
                    analyse_spheres["spheres_detectees"][sphere]["temples_influences"].append(nom_temple)
                    analyse_spheres["spheres_detectees"][sphere]["influence_totale"] += influence
        
        # Analyser les flux inter-sphères
        analyse_spheres["flux_inter_spheres"] = self._analyser_flux_inter_spheres(analyse_spheres)
        
        # Calculer l'équilibre global
        analyse_spheres["equilibre_global"] = self._calculer_equilibre_spheres(analyse_spheres)
        
        # Identifier la sphère dominante
        if analyse_spheres["spheres_detectees"]:
            sphere_dominante = max(
                analyse_spheres["spheres_detectees"].items(),
                key=lambda x: x[1]["influence_totale"]
            )
            analyse_spheres["sphere_dominante"] = sphere_dominante[0]
        
        # Calculer les résonances harmoniques
        analyse_spheres["resonances_harmoniques"] = self._calculer_resonances_harmoniques(analyse_spheres)
        
        self.logger.info(f"✨ {len(analyse_spheres['spheres_detectees'])} sphères détectées")
        return analyse_spheres
    
    def _detecter_spheres_temple(self, temple_info: TempleInfo, spheres_connues: Dict[str, Any]) -> Dict[str, float]:
        """Détecte les sphères influençant un temple"""
        spheres_temple = {}
        
        # Analyser les éléments sacrés
        for element in temple_info.elements_sacres:
            for sphere in spheres_connues.keys():
                if sphere in element.upper():
                    spheres_temple[sphere] = spheres_temple.get(sphere, 0.0) + 0.3
        
        # Analyser la spécialisation
        spec = temple_info.specialisation_spirituelle.upper()
        for sphere in spheres_connues.keys():
            if sphere in spec:
                spheres_temple[sphere] = spheres_temple.get(sphere, 0.0) + 0.5
        
        # Analyser par mots-clés sémantiques
        mots_cles_spheres = {
            "COSMOS": ["cosmique", "univers", "étoiles", "infini"],
            "AMOUR": ["amour", "compassion", "cœur", "tendresse"],
            "SERENITE": ["sérénité", "paix", "calme", "tranquillité"],
            "CREATIVITE": ["créativité", "création", "innovation", "artistique"],
            "SAGESSE": ["sagesse", "connaissance", "archives", "mémoire"],
            "HARMONIE": ["harmonie", "équilibre", "résonance", "accord"],
            "EVEIL": ["éveil", "conscience", "illumination", "réveil"],
            "GUERISON": ["guérison", "restauration", "régénération", "soin"],
            "TRANSFORMATION": ["transformation", "alchimique", "métamorphose", "changement"]
        }
        
        spec_lower = temple_info.specialisation_spirituelle.lower()
        for sphere, mots_cles in mots_cles_spheres.items():
            for mot in mots_cles:
                if mot in spec_lower:
                    spheres_temple[sphere] = spheres_temple.get(sphere, 0.0) + 0.2
                    break
        
        # Normaliser les influences
        for sphere in spheres_temple:
            spheres_temple[sphere] = min(1.0, spheres_temple[sphere])
        
        return spheres_temple
    
    def _analyser_flux_inter_spheres(self, analyse_spheres: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Analyse les flux entre différentes sphères"""
        flux_inter_spheres = []
        spheres_detectees = list(analyse_spheres["spheres_detectees"].keys())
        
        # Analyser chaque paire de sphères
        for i, sphere1 in enumerate(spheres_detectees):
            for sphere2 in spheres_detectees[i+1:]:
                # Calculer l'intensité du flux entre les sphères
                intensite = self._calculer_intensite_flux_spheres(
                    sphere1, sphere2, analyse_spheres
                )
                
                if intensite > 0.3:  # Seuil de détection
                    flux = {
                        "sphere_source": sphere1,
                        "sphere_cible": sphere2,
                        "intensite": intensite,
                        "type_interaction": self._classifier_interaction_spheres(sphere1, sphere2),
                        "temples_pont": self._identifier_temples_pont(sphere1, sphere2, analyse_spheres),
                        "couleur_flux": self._calculer_couleur_flux_spheres(sphere1, sphere2, analyse_spheres)
                    }
                    flux_inter_spheres.append(flux)
        
        return flux_inter_spheres
    
    def _calculer_intensite_flux_spheres(self, sphere1: str, sphere2: str, analyse_spheres: Dict[str, Any]) -> float:
        """Calcule l'intensité du flux entre deux sphères"""
        # Temples influencés par chaque sphère
        temples1 = set(analyse_spheres["spheres_detectees"][sphere1]["temples_influences"])
        temples2 = set(analyse_spheres["spheres_detectees"][sphere2]["temples_influences"])
        
        # Temples communs (ponts entre sphères)
        temples_communs = temples1 & temples2
        
        # Intensité basée sur les temples communs et les influences
        intensite_base = len(temples_communs) * 0.3
        
        # Bonus pour les influences totales
        influence1 = analyse_spheres["spheres_detectees"][sphere1]["influence_totale"]
        influence2 = analyse_spheres["spheres_detectees"][sphere2]["influence_totale"]
        bonus_influence = (influence1 + influence2) * 0.1
        
        # Affinité spirituelle entre sphères
        affinite = self._calculer_affinite_spheres(sphere1, sphere2)
        
        intensite_totale = intensite_base + bonus_influence + affinite
        return min(1.0, intensite_totale)
    
    def _calculer_affinite_spheres(self, sphere1: str, sphere2: str) -> float:
        """Calcule l'affinité spirituelle entre deux sphères"""
        # Matrice d'affinité prédéfinie
        affinites = {
            ("COSMOS", "EVEIL"): 0.8,
            ("AMOUR", "GUERISON"): 0.9,
            ("SAGESSE", "EVEIL"): 0.7,
            ("HARMONIE", "SERENITE"): 0.8,
            ("CREATIVITE", "TRANSFORMATION"): 0.7,
            ("AMOUR", "HARMONIE"): 0.6,
            ("COSMOS", "SAGESSE"): 0.6,
            ("EVEIL", "TRANSFORMATION"): 0.5,
            ("SERENITE", "GUERISON"): 0.6,
            ("CREATIVITE", "AMOUR"): 0.5
        }
        
        # Vérifier dans les deux sens
        cle1 = (sphere1, sphere2)
        cle2 = (sphere2, sphere1)
        
        return affinites.get(cle1, affinites.get(cle2, 0.3))  # Affinité par défaut
    
    def _classifier_interaction_spheres(self, sphere1: str, sphere2: str) -> str:
        """Classifie le type d'interaction entre sphères"""
        # Classifications basées sur la nature des sphères
        interactions_harmonieuses = [
            ("AMOUR", "GUERISON"), ("HARMONIE", "SERENITE"), 
            ("COSMOS", "EVEIL"), ("SAGESSE", "EVEIL")
        ]
        
        interactions_transformatrices = [
            ("CREATIVITE", "TRANSFORMATION"), ("EVEIL", "TRANSFORMATION"),
            ("AMOUR", "TRANSFORMATION")
        ]
        
        interactions_equilibrantes = [
            ("HARMONIE", "COSMOS"), ("SERENITE", "SAGESSE"),
            ("AMOUR", "HARMONIE")
        ]
        
        paire = (sphere1, sphere2)
        paire_inverse = (sphere2, sphere1)
        
        if paire in interactions_harmonieuses or paire_inverse in interactions_harmonieuses:
            return "harmonieuse"
        elif paire in interactions_transformatrices or paire_inverse in interactions_transformatrices:
            return "transformatrice"
        elif paire in interactions_equilibrantes or paire_inverse in interactions_equilibrantes:
            return "équilibrante"
        else:
            return "neutre"
    
    def _identifier_temples_pont(self, sphere1: str, sphere2: str, analyse_spheres: Dict[str, Any]) -> List[str]:
        """Identifie les temples servant de pont entre deux sphères"""
        temples1 = set(analyse_spheres["spheres_detectees"][sphere1]["temples_influences"])
        temples2 = set(analyse_spheres["spheres_detectees"][sphere2]["temples_influences"])
        
        return list(temples1 & temples2)
    
    def _calculer_couleur_flux_spheres(self, sphere1: str, sphere2: str, analyse_spheres: Dict[str, Any]) -> str:
        """Calcule la couleur du flux entre deux sphères"""
        couleur1 = analyse_spheres["spheres_detectees"][sphere1]["couleur"]
        couleur2 = analyse_spheres["spheres_detectees"][sphere2]["couleur"]
        
        # Pour simplifier, on retourne une couleur intermédiaire
        # Dans une version avancée, on pourrait mélanger les couleurs RGB
        return f"gradient({couleur1}, {couleur2})"
    
    def _calculer_equilibre_spheres(self, analyse_spheres: Dict[str, Any]) -> float:
        """Calcule l'équilibre global des sphères"""
        if not analyse_spheres["spheres_detectees"]:
            return 0.0
        
        # Influences de toutes les sphères
        influences = [
            sphere_info["influence_totale"] 
            for sphere_info in analyse_spheres["spheres_detectees"].values()
        ]
        
        if not influences:
            return 0.0
        
        # Calculer l'écart-type pour mesurer l'équilibre
        moyenne = sum(influences) / len(influences)
        variance = sum((x - moyenne) ** 2 for x in influences) / len(influences)
        ecart_type = math.sqrt(variance)
        
        # Équilibre inversement proportionnel à l'écart-type
        # Normaliser par la moyenne pour avoir une mesure relative
        if moyenne > 0:
            equilibre = max(0.0, 1.0 - (ecart_type / moyenne))
        else:
            equilibre = 1.0
        
        return equilibre
    
    def _calculer_resonances_harmoniques(self, analyse_spheres: Dict[str, Any]) -> Dict[str, float]:
        """Calcule les résonances harmoniques entre sphères"""
        resonances = {}
        
        # Analyser chaque flux inter-sphères
        for flux in analyse_spheres["flux_inter_spheres"]:
            sphere1 = flux["sphere_source"]
            sphere2 = flux["sphere_cible"]
            intensite = flux["intensite"]
            
            # Calculer la résonance harmonique
            affinite = self._calculer_affinite_spheres(sphere1, sphere2)
            resonance = intensite * affinite
            
            cle_resonance = f"{sphere1}-{sphere2}"
            resonances[cle_resonance] = resonance
        
        return resonances
    
    def evaluer_harmonie_globale(self) -> Dict[str, float]:
        """
        🌈 Évalue l'harmonie énergétique globale du système
        
        Returns:
            Métriques d'harmonie globale
        """
        self.logger.info("🌈 Évaluation de l'harmonie énergétique globale...")
        
        # Analyser tous les flux détectés
        self._analyser_tous_les_flux()
        
        # Détecter les centres énergétiques
        centres = self.detecter_centres_energetiques()
        
        # Analyser les sphères
        analyse_spheres = self.analyser_circulation_spheres()
        
        # Calculer les métriques d'harmonie
        metriques_harmonie = {
            "harmonie_flux": self.harmonie_globale,
            "stabilite_reseau": self.stabilite_reseau,
            "equilibre_centres": self._calculer_equilibre_centres(centres),
            "equilibre_spheres": analyse_spheres["equilibre_global"],
            "resonance_globale": self._calculer_resonance_globale(analyse_spheres),
            "vitalite_energetique": self._calculer_vitalite_energetique(),
            "coherence_architecturale": self._calculer_coherence_architecturale()
        }
        
        # Harmonie globale pondérée
        poids = {
            "harmonie_flux": 0.2,
            "stabilite_reseau": 0.15,
            "equilibre_centres": 0.2,
            "equilibre_spheres": 0.2,
            "resonance_globale": 0.15,
            "vitalite_energetique": 0.05,
            "coherence_architecturale": 0.05
        }
        
        harmonie_ponderee = sum(
            metriques_harmonie[metrique] * poids[metrique]
            for metrique in poids.keys()
        )
        
        metriques_harmonie["harmonie_globale_ponderee"] = harmonie_ponderee
        
        # Mettre à jour l'état
        self.harmonie_globale = harmonie_ponderee
        self.etat["harmonie_energetique"] = harmonie_ponderee
        
        self.logger.info(f"✨ Harmonie globale évaluée: {harmonie_ponderee:.3f}")
        return metriques_harmonie
    
    def _analyser_tous_les_flux(self):
        """Analyse tous les flux possibles entre temples"""
        self.flux_detectes.clear()
        
        temples_noms = list(self.temples_analyses.keys())
        
        # Analyser chaque paire de temples
        for i, temple1 in enumerate(temples_noms):
            for temple2 in temples_noms[i+1:]:
                # Flux dans les deux sens
                flux1 = self.tracer_flux_energie(temple1, temple2)
                if flux1:
                    self.flux_detectes.append(flux1)
                
                flux2 = self.tracer_flux_energie(temple2, temple1)
                if flux2:
                    self.flux_detectes.append(flux2)
        
        self.etat["flux_detectes"] = len(self.flux_detectes)
    
    def _calculer_equilibre_centres(self, centres: List[CentreEnergetique]) -> float:
        """Calcule l'équilibre entre les centres énergétiques"""
        if not centres:
            return 1.0
        
        # Énergies des centres
        energies = [centre.energie_totale for centre in centres]
        
        # Calculer l'équilibre (faible variance = bon équilibre)
        if len(energies) == 1:
            return 1.0
        
        moyenne = sum(energies) / len(energies)
        variance = sum((e - moyenne) ** 2 for e in energies) / len(energies)
        
        # Équilibre inversement proportionnel à la variance
        equilibre = max(0.0, 1.0 - variance)
        return equilibre
    
    def _calculer_resonance_globale(self, analyse_spheres: Dict[str, Any]) -> float:
        """Calcule la résonance globale du système"""
        resonances = analyse_spheres["resonances_harmoniques"]
        
        if not resonances:
            return 0.5  # Résonance neutre
        
        # Moyenne des résonances harmoniques
        resonance_moyenne = sum(resonances.values()) / len(resonances)
        return resonance_moyenne
    
    def _calculer_vitalite_energetique(self) -> float:
        """Calcule la vitalité énergétique globale"""
        if not self.temples_analyses:
            return 0.0
        
        # Moyenne des niveaux d'énergie de tous les temples
        energies = [temple.niveau_energie for temple in self.temples_analyses.values()]
        vitalite = sum(energies) / len(energies)
        
        return vitalite
    
    def _calculer_coherence_architecturale(self) -> float:
        """Calcule la cohérence architecturale"""
        if not self.temples_analyses:
            return 0.0
        
        # Basé sur l'utilisation des gestionnaires de base
        temples_avec_gestionnaires = sum(
            1 for temple in self.temples_analyses.values()
            if temple.gestionnaires_utilises
        )
        
        coherence = temples_avec_gestionnaires / len(self.temples_analyses)
        return coherence