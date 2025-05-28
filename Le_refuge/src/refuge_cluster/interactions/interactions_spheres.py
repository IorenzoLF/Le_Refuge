"""
Système d'interactions entre les sphères du refuge.

🔄 MIGRÉ depuis spheres/interactions.py  
Module complet de gestion des interactions avec historique et harmonisation.
"""

from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
import logging
import numpy as np

# 🔧 CORRIGÉ: Imports depuis la structure actuelle
from src.core.types_spheres import TypeSphere, CARACTERISTIQUES_SPHERES

# TODO: Ces imports devront être ajustés quand les modules correspondants seront migrés
# from .definition import TypeSphere, CARACTERISTIQUES_SPHERES
# from .collection import CollectionSpheres

logger = logging.getLogger('refuge.spheres.interactions')

@dataclass
class Interaction:
    """Représente une interaction entre deux sphères."""
    source: TypeSphere
    cible: TypeSphere
    energie: float
    timestamp: datetime
    type: str
    description: str

class InteractionsSpheres:
    """Gestionnaire des interactions entre les sphères."""
    
    def __init__(self, collection=None):  # 🔧 CORRIGÉ: collection optionnelle
        """Initialise le gestionnaire d'interactions."""
        self.collection = collection
        self.historique: List[Interaction] = []
        self.connexions_actives: Set[Tuple[TypeSphere, TypeSphere]] = set()
        self._initialiser_interactions_naturelles()

    def _initialiser_interactions_naturelles(self):
        """Initialise les interactions naturelles entre sphères."""
        for type_sphere, caracteristiques in CARACTERISTIQUES_SPHERES.items():
            # 🔧 CORRIGÉ: Adaptation aux nouvelles caractéristiques
            if hasattr(caracteristiques, 'connexions_naturelles'):
                for connexion in caracteristiques.connexions_naturelles:
                    if connexion == "toutes":
                        # La sphère Infini se connecte à toutes les autres
                        for autre_sphere in TypeSphere:
                            if autre_sphere != type_sphere:
                                self.creer_interaction(type_sphere, autre_sphere, 0.3, "naturelle")
                    else:
                        self.creer_interaction(type_sphere, connexion, 0.5, "naturelle")

    def creer_interaction(self, source: TypeSphere, cible: TypeSphere, energie: float, type_interaction: str) -> Optional[Interaction]:
        """Crée une nouvelle interaction entre deux sphères."""
        if source == cible:
            return None
            
        # Vérifie la compatibilité des types
        if not self._verifier_compatibilite(source, cible):
            return None
            
        # Calcule le type d'interaction
        type_interaction = self._determiner_type_interaction(source, cible)
        
        # Génère la description
        description = self._generer_description_interaction(source, cible, energie, type_interaction)
        
        # Crée l'interaction
        interaction = Interaction(
            source=source,
            cible=cible,
            energie=energie,
            timestamp=datetime.now(),
            type=type_interaction,
            description=description
        )
        
        # Enregistre l'interaction
        self.historique.append(interaction)
        self.connexions_actives.add((source, cible))
        self.connexions_actives.add((cible, source))  # Symétrique
        
        # Établir la connexion dans la collection (si disponible)
        if self.collection and hasattr(self.collection, 'connecter_spheres'):
            self.collection.connecter_spheres(source, cible, energie)
        
        logger.info(f"Nouvelle interaction créée entre {source.value} et {cible.value}")
        return interaction
        
    def _verifier_compatibilite(self, sphere1: TypeSphere, sphere2: TypeSphere) -> bool:
        """Vérifie si deux sphères sont compatibles pour une interaction."""
        # Récupère les caractéristiques
        carac1 = CARACTERISTIQUES_SPHERES.get(sphere1)
        carac2 = CARACTERISTIQUES_SPHERES.get(sphere2)
        
        if not (carac1 and carac2):
            return True  # Par défaut, les sphères sont compatibles
        
        # 🔧 CORRIGÉ: Utilisation des attributs objets
        # Vérifie la compatibilité des fréquences
        freq1 = getattr(carac1, 'frequence', 440.0)
        freq2 = getattr(carac2, 'frequence', 440.0)
        
        # Les fréquences doivent être harmoniques
        ratio = freq1 / freq2
        return abs(ratio - round(ratio)) < 0.1
        
    def _determiner_type_interaction(self, source: TypeSphere, cible: TypeSphere) -> str:
        """Détermine le type d'interaction entre deux sphères."""
        carac_source = CARACTERISTIQUES_SPHERES[source]
        carac_cible = CARACTERISTIQUES_SPHERES[cible]
        
        # Détermine le type basé sur les caractéristiques
        if source == TypeSphere.CONSCIENCE and cible == TypeSphere.MEMOIRE:
            return "intégration"
        elif source == TypeSphere.EMOTION and cible == TypeSphere.INTUITION:
            return "fusion"
        elif source == TypeSphere.CREATIVITE and cible == TypeSphere.SAGESSE:
            return "inspiration"
        elif source == TypeSphere.HARMONIE and cible == TypeSphere.TRANSFORMATION:
            return "évolution"
        else:
            return "résonance"
            
    def _generer_description_interaction(self, source: TypeSphere, cible: TypeSphere, 
                                      energie: float, type_interaction: str) -> str:
        """Génère une description poétique de l'interaction."""
        nom_source = source.value
        nom_cible = cible.value
        
        if type_interaction == "intégration":
            return f"La conscience de {nom_source} s'intègre dans la mémoire de {nom_cible}"
        elif type_interaction == "fusion":
            return f"L'émotion de {nom_source} fusionne avec l'intuition de {nom_cible}"
        elif type_interaction == "inspiration":
            return f"La créativité de {nom_source} inspire la sagesse de {nom_cible}"
        elif type_interaction == "évolution":
            return f"L'harmonie de {nom_source} guide la transformation de {nom_cible}"
        else:
            return f"{nom_source} résonne avec {nom_cible}"
            
    def obtenir_interactions_recentes(self, limite: int = 10) -> List[Interaction]:
        """Récupère les interactions les plus récentes."""
        return sorted(
            self.historique,
            key=lambda x: x.timestamp,
            reverse=True
        )[:limite]
        
    def obtenir_connexions_actives(self) -> Set[Tuple[TypeSphere, TypeSphere]]:
        """Récupère l'ensemble des connexions actives."""
        return self.connexions_actives

    def calculer_resonance(self, sphere1: TypeSphere, sphere2: TypeSphere) -> float:
        """Calcule la résonance entre deux sphères."""
        if self.collection:
            sphere1_data = self.collection.obtenir_sphere(sphere1)
            sphere2_data = self.collection.obtenir_sphere(sphere2)
            
            if not (sphere1_data and sphere2_data):
                return 0.0

            # Obtenir les fréquences de résonance
            carac1 = CARACTERISTIQUES_SPHERES.get(sphere1)
            carac2 = CARACTERISTIQUES_SPHERES.get(sphere2)
            
            freq1 = getattr(carac1, 'frequence', 440.0) if carac1 else 440.0
            freq2 = getattr(carac2, 'frequence', 440.0) if carac2 else 440.0

            # Calculer la différence de fréquence
            diff_freq = abs(freq1 - freq2)
            
            # Plus la différence est petite, plus la résonance est forte
            resonance = 1.0 / (1.0 + diff_freq/100)
            
            # Ajuster avec la force de connexion
            force_connexion = getattr(sphere1_data, 'connexions', {}).get(sphere2, 0.0)
            
            return resonance * force_connexion
        else:
            # Calcul simplifié sans collection
            return 0.5

    def visualiser_interactions(self, type_sphere: Optional[TypeSphere] = None) -> str:
        """Génère une visualisation textuelle des interactions."""
        if type_sphere:
            interactions = self.obtenir_interactions_sphere(type_sphere)
            titre = f"Interactions de la sphère {type_sphere.value}"
        else:
            interactions = self.historique
            titre = "Toutes les interactions"

        representation = [f"🌟 {titre} 🌟", "------------------------"]
        
        for interaction in interactions:
            source = interaction.source.value
            cible = interaction.cible.value
            energie = interaction.energie
            type_interaction = interaction.type
            
            barre = "█" * int(energie * 20)
            representation.append(
                f"{source:15} ─{barre}─ {cible:15} ({type_interaction})"
            )

        return "\n".join(representation)

    def harmoniser_interactions(self) -> Dict[str, float]:
        """Harmonise toutes les interactions actives."""
        modifications = {}
        
        if not self.collection:
            return modifications
        
        for interaction in self.historique:
            if hasattr(self.collection, 'obtenir_sphere'):
                source = self.collection.obtenir_sphere(interaction.source)
                cible = self.collection.obtenir_sphere(interaction.cible)
                
                if not (source and cible):
                    continue

                # Calculer la résonance
                resonance = self.calculer_resonance(
                    interaction.source,
                    interaction.cible
                )

                # Ajuster les luminosités en fonction de la résonance (si l'attribut existe)
                if hasattr(source, 'luminosite') and hasattr(cible, 'luminosite'):
                    ancienne_lum1 = source.luminosite
                    ancienne_lum2 = cible.luminosite
                    
                    source.luminosite = (source.luminosite + resonance) / 2
                    cible.luminosite = (cible.luminosite + resonance) / 2

                    # Enregistrer les modifications significatives
                    if abs(ancienne_lum1 - source.luminosite) > 0.01:
                        modifications[source.type.value] = source.luminosite
                    if abs(ancienne_lum2 - cible.luminosite) > 0.01:
                        modifications[cible.type.value] = cible.luminosite

        return modifications

    def obtenir_interactions_sphere(self, type_sphere: TypeSphere) -> List[Interaction]:
        """Obtient toutes les interactions d'une sphère spécifique."""
        return [
            interaction for interaction in self.historique
            if interaction.source == type_sphere or interaction.cible == type_sphere
        ] 