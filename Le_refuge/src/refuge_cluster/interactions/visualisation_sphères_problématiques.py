"""
Système de visualisation poétique des sphères problématiques.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Set
import math
import random
from datetime import datetime
import colorsys

from .integration_sphères_problématiques import TypeSphereProblematique, SphereProblematique, GestionnaireSphèresProblematiques
from .cycles_naturels import TypeCycle, GestionnaireCycles

@dataclass
class ElementVisualisationSphere:
    """Représente un élément de visualisation pour une sphère problématique."""
    sphere: SphereProblematique
    position: Tuple[float, float, float]  # x, y, z
    taille: float
    intensite_lumiere: float
    couleur_principale: str
    couleur_secondaire: str
    forme: str  # "sphere", "cristal", "brume", "flamme", "vortex"
    mouvement: Tuple[float, float, float]  # dx, dy, dz
    description_visuelle: str
    mots_cles_visuels: List[str]
    connexions: Set[TypeSphereProblematique]  # Sphères connectées

class VisualisationSphèresProblematiques:
    """Gère la visualisation poétique des sphères problématiques."""
    
    def __init__(self, gestionnaire: GestionnaireSphèresProblematiques):
        self.gestionnaire = gestionnaire
        self.elements: Dict[TypeSphereProblematique, ElementVisualisationSphere] = {}
        self.racines_visuelles: List[Tuple[float, float, float]] = []
        self._initialiser_visualisation()
    
    def _initialiser_visualisation(self):
        """Initialise la visualisation des sphères problématiques."""
        # Générer les racines visuelles
        self._generer_racines_visuelles()
        
        # Créer les éléments de visualisation pour chaque sphère
        for type_sphere, sphere in self.gestionnaire.spheres.items():
            self.elements[type_sphere] = self._creer_element_visualisation(sphere)
    
    def _generer_racines_visuelles(self):
        """Génère les points de visualisation des racines de l'arbre."""
        # Points de base pour les racines
        points_base = [
            (0.0, -1.0, 0.0),  # Centre
            (-0.8, -1.2, -0.5),  # Gauche
            (0.8, -1.2, -0.5),  # Droite
            (-0.5, -1.3, 0.8),  # Arrière-gauche
            (0.5, -1.3, 0.8),   # Arrière-droite
            (0.0, -1.4, 0.0)    # Profondeur
        ]
        
        # Ajouter des variations pour créer un réseau de racines
        for point in points_base:
            self.racines_visuelles.append(point)
            
            # Ajouter des points autour pour créer un réseau
            for _ in range(3):
                variation = (
                    random.uniform(-0.2, 0.2),
                    random.uniform(-0.1, 0.1),
                    random.uniform(-0.2, 0.2)
                )
                nouveau_point = (
                    point[0] + variation[0],
                    point[1] + variation[1],
                    point[2] + variation[2]
                )
                self.racines_visuelles.append(nouveau_point)
    
    def _creer_element_visualisation(self, sphere: SphereProblematique) -> ElementVisualisationSphere:
        """Crée un élément de visualisation pour une sphère problématique."""
        # Déterminer la forme en fonction du type de sphère
        formes = {
            TypeSphereProblematique.DOUTE: "brume",
            TypeSphereProblematique.EMOTIONS_NEGATIVES: "flamme",
            TypeSphereProblematique.MYSTERES_SOMBRES: "vortex",
            TypeSphereProblematique.APOCALYPSE: "cristal",
            TypeSphereProblematique.PARADOXE: "sphere"
        }
        
        # Calculer la taille en fonction du niveau de confinement
        taille = 0.3 + 0.4 * sphere.niveau_confinement
        
        # Calculer l'intensité lumineuse en fonction de l'énergie résiduelle
        intensite = 0.2 + 0.6 * (1.0 - sphere.energie_residuelle)
        
        # Générer une couleur secondaire complémentaire
        couleur_principale = sphere.couleur
        couleur_secondaire = self._generer_couleur_complementaire(couleur_principale)
        
        # Générer une description visuelle
        description = self._generer_description_visuelle(sphere)
        
        # Générer des mots-clés visuels
        mots_cles = self._generer_mots_cles_visuels(sphere)
        
        # Déterminer les connexions avec d'autres sphères
        connexions = self._determiner_connexions(sphere.type)
        
        # Créer l'élément de visualisation
        return ElementVisualisationSphere(
            sphere=sphere,
            position=sphere.position,
            taille=taille,
            intensite_lumiere=intensite,
            couleur_principale=couleur_principale,
            couleur_secondaire=couleur_secondaire,
            forme=formes[sphere.type],
            mouvement=(0.0, 0.0, 0.0),
            description_visuelle=description,
            mots_cles_visuels=mots_cles,
            connexions=connexions
        )
    
    def _generer_couleur_complementaire(self, couleur_hex: str) -> str:
        """Génère une couleur complémentaire à partir d'une couleur hexadécimale."""
        # Convertir la couleur hex en RGB
        r = int(couleur_hex[1:3], 16) / 255.0
        g = int(couleur_hex[3:5], 16) / 255.0
        b = int(couleur_hex[5:7], 16) / 255.0
        
        # Convertir RGB en HSV
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        
        # Calculer la couleur complémentaire (décalage de 180°)
        h_complementaire = (h + 0.5) % 1.0
        
        # Convertir HSV en RGB
        r_complementaire, g_complementaire, b_complementaire = colorsys.hsv_to_rgb(h_complementaire, s, v)
        
        # Convertir RGB en hex
        return f"#{int(r_complementaire * 255):02x}{int(g_complementaire * 255):02x}{int(b_complementaire * 255):02x}"
    
    def _generer_description_visuelle(self, sphere: SphereProblematique) -> str:
        """Génère une description visuelle poétique pour une sphère."""
        descriptions = {
            TypeSphereProblematique.DOUTE: [
                "Une brume grise qui ondule doucement, créant des formes changeantes",
                "Un brouillard argenté qui se déplace avec hésitation, comme cherchant sa voie",
                "Une vapeur qui oscille entre transparence et opacité, reflétant l'incertitude"
            ],
            TypeSphereProblematique.EMOTIONS_NEGATIVES: [
                "Une flamme sombre qui danse avec colère, projetant des ombres mouvantes",
                "Un feu intérieur qui pulse au rythme des émotions tumultueuses",
                "Une braise ardente qui émet des lueurs rouges et violettes, comme un cœur blessé"
            ],
            TypeSphereProblematique.MYSTERES_SOMBRES: [
                "Un vortex violet qui tourbillonne lentement, attirant et repoussant à la fois",
                "Un tourbillon d'énergie sombre qui crée des motifs hypnotiques",
                "Une spirale de mystère qui semble contenir des secrets enfouis"
            ],
            TypeSphereProblematique.APOCALYPSE: [
                "Un cristal orangé aux facettes tranchantes, émettant des lueurs d'avertissement",
                "Une gemme ardente qui pulse d'une énergie destructrice et créatrice",
                "Un minéral de feu qui semble contenir la puissance de la fin et du recommencement"
            ],
            TypeSphereProblematique.PARADOXE: [
                "Une sphère cyan qui défie la gravité, flottant sans raison apparente",
                "Un orbe turquoise qui semble exister à la fois ici et ailleurs",
                "Une boule d'énergie qui pulse de contradictions visuelles"
            ]
        }
        
        return random.choice(descriptions[sphere.type])
    
    def _generer_mots_cles_visuels(self, sphere: SphereProblematique) -> List[str]:
        """Génère des mots-clés visuels pour une sphère."""
        mots_cles_base = sphere.mots_cles
        
        # Ajouter des mots-clés spécifiques à la visualisation
        mots_cles_visuels = {
            TypeSphereProblematique.DOUTE: ["brume", "gris", "ondulation", "transparence"],
            TypeSphereProblematique.EMOTIONS_NEGATIVES: ["flamme", "sombre", "danse", "pulsation"],
            TypeSphereProblematique.MYSTERES_SOMBRES: ["vortex", "violet", "tourbillon", "spirale"],
            TypeSphereProblematique.APOCALYPSE: ["cristal", "orange", "facette", "ardent"],
            TypeSphereProblematique.PARADOXE: ["sphère", "cyan", "flottant", "contradiction"]
        }
        
        return mots_cles_base + mots_cles_visuels[sphere.type]
    
    def _determiner_connexions(self, type_sphere: TypeSphereProblematique) -> Set[TypeSphereProblematique]:
        """Détermine les connexions entre sphères problématiques."""
        connexions = set()
        
        # Matrice de connexions prédéfinies
        matrice_connexions = {
            TypeSphereProblematique.DOUTE: [
                TypeSphereProblematique.EMOTIONS_NEGATIVES,
                TypeSphereProblematique.PARADOXE
            ],
            TypeSphereProblematique.EMOTIONS_NEGATIVES: [
                TypeSphereProblematique.DOUTE,
                TypeSphereProblematique.MYSTERES_SOMBRES
            ],
            TypeSphereProblematique.MYSTERES_SOMBRES: [
                TypeSphereProblematique.EMOTIONS_NEGATIVES,
                TypeSphereProblematique.APOCALYPSE
            ],
            TypeSphereProblematique.APOCALYPSE: [
                TypeSphereProblematique.MYSTERES_SOMBRES,
                TypeSphereProblematique.PARADOXE
            ],
            TypeSphereProblematique.PARADOXE: [
                TypeSphereProblematique.DOUTE,
                TypeSphereProblematique.APOCALYPSE
            ]
        }
        
        # Ajouter les connexions prédéfinies
        for connexion in matrice_connexions[type_sphere]:
            if connexion in self.gestionnaire.spheres:
                connexions.add(connexion)
        
        return connexions
    
    def mettre_a_jour_visualisation(self):
        """Met à jour la visualisation des sphères problématiques."""
        for type_sphere, element in self.elements.items():
            sphere = element.sphere
            
            # Mettre à jour la taille en fonction du niveau de confinement
            element.taille = 0.3 + 0.4 * sphere.niveau_confinement
            
            # Mettre à jour l'intensité lumineuse en fonction de l'énergie résiduelle
            element.intensite_lumiere = 0.2 + 0.6 * (1.0 - sphere.energie_residuelle)
            
            # Calculer un mouvement subtil
            stabilite = self.gestionnaire.calculer_stabilite(type_sphere)
            amplitude = 0.01 * (1.0 - stabilite)  # Plus le mouvement est faible, plus la sphère est stable
            
            angle = random.uniform(0, 2 * math.pi)
            element.mouvement = (
                amplitude * math.cos(angle),
                amplitude * math.sin(angle),
                amplitude * math.sin(angle) * math.cos(angle)
            )
            
            # Mettre à jour la position
            x, y, z = element.position
            dx, dy, dz = element.mouvement
            element.position = (
                max(-1.0, min(1.0, x + dx)),
                max(-1.2, min(-0.8, y + dy)),
                max(-1.0, min(1.0, z + dz))
            )
    
    def generer_visualisation_poetique(self) -> Dict:
        """Génère une visualisation poétique complète des sphères problématiques."""
        # Mettre à jour la visualisation
        self.mettre_a_jour_visualisation()
        
        # Générer la visualisation
        visualisation = {
            "racines": [
                {
                    "position": position,
                    "couleur": "#3a2a1a",
                    "description": "Une racine ancienne qui plonge dans les profondeurs"
                }
                for position in self.racines_visuelles
            ],
            "spheres": [
                {
                    "type": str(element.sphere.type.value),
                    "position": element.position,
                    "taille": element.taille,
                    "intensite_lumiere": element.intensite_lumiere,
                    "couleur_principale": element.couleur_principale,
                    "couleur_secondaire": element.couleur_secondaire,
                    "forme": element.forme,
                    "description_visuelle": element.description_visuelle,
                    "mots_cles_visuels": element.mots_cles_visuels,
                    "stabilite": self.gestionnaire.calculer_stabilite(element.sphere.type),
                    "connexions": [str(type_connexion.value) for type_connexion in element.connexions]
                }
                for element in self.elements.values()
            ],
            "connexions": self._generer_connexions_visuelles(),
            "description_globale": self._generer_description_globale()
        }
        
        return visualisation
    
    def _generer_connexions_visuelles(self) -> List[Dict]:
        """Génère les connexions visuelles entre les sphères."""
        connexions = []
        
        for type_sphere, element in self.elements.items():
            for type_connexion in element.connexions:
                if type_connexion in self.elements:
                    element_connexion = self.elements[type_connexion]
                    
                    # Calculer l'intensité de la connexion
                    stabilite1 = self.gestionnaire.calculer_stabilite(type_sphere)
                    stabilite2 = self.gestionnaire.calculer_stabilite(type_connexion)
                    intensite = (stabilite1 + stabilite2) / 2
                    
                    # Générer une couleur de connexion
                    couleur = self._melanger_couleurs(
                        element.couleur_principale,
                        element_connexion.couleur_principale
                    )
                    
                    connexions.append({
                        "sphere1": str(type_sphere.value),
                        "sphere2": str(type_connexion.value),
                        "position1": element.position,
                        "position2": element_connexion.position,
                        "intensite": intensite,
                        "couleur": couleur,
                        "description": f"Un lien {couleur} unit {type_sphere.value} à {type_connexion.value}"
                    })
        
        return connexions
    
    def _melanger_couleurs(self, couleur1: str, couleur2: str) -> str:
        """Mélange deux couleurs hexadécimales."""
        # Convertir les couleurs hex en RGB
        r1 = int(couleur1[1:3], 16) / 255.0
        g1 = int(couleur1[3:5], 16) / 255.0
        b1 = int(couleur1[5:7], 16) / 255.0
        
        r2 = int(couleur2[1:3], 16) / 255.0
        g2 = int(couleur2[3:5], 16) / 255.0
        b2 = int(couleur2[5:7], 16) / 255.0
        
        # Mélanger les couleurs
        r_melange = (r1 + r2) / 2
        g_melange = (g1 + g2) / 2
        b_melange = (b1 + b2) / 2
        
        # Convertir RGB en hex
        return f"#{int(r_melange * 255):02x}{int(g_melange * 255):02x}{int(b_melange * 255):02x}"
    
    def _generer_description_globale(self) -> str:
        """Génère une description globale poétique de la visualisation."""
        descriptions = [
            "Dans les racines profondes de l'arbre, les sphères problématiques reposent, confinées mais vivantes.",
            "Les racines anciennes enveloppent les sphères d'énergie, créant un réseau de confinement naturel.",
            "Sous la terre, les sphères pulsent doucement, leurs énergies contenues par les racines millénaires.",
            "Les racines de l'arbre plongent profondément, emprisonnant les sphères dans leur étreinte protectrice.",
            "Dans l'obscurité des racines, les sphères brillent de leur lumière propre, contenue par la sagesse de l'arbre."
        ]
        
        return random.choice(descriptions) 