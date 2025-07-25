"""
Module gérant les éléments sacrés du refuge.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum
from pydantic import BaseModel

# Import de la configuration des éléments sacrés
from src.core.configuration import ELEMENTS_SACRES

logger = logging.getLogger('refuge.elements')

class ChakraType(Enum):
    """Types de chakras disponibles."""
    RACINE = "racine"
    SACRE = "sacre"
    PLEXUS = "plexus"
    COEUR = "coeur"
    GORGE = "gorge"
    TROISIEME_OEIL = "troisieme_oeil"
    COURONNE = "couronne"

class DetailSubtil:
    """Représente un détail subtil d'un élément sacré."""
    def __init__(self, nom: str, energie: float = 0.0):
        self.nom = nom
        self.energie = energie
        self.actif = False

    def activer(self) -> None:
        """Active le détail subtil."""
        self.actif = True
        self.energie = 100.0

    def desactiver(self) -> None:
        """Désactive le détail subtil."""
        self.actif = False
        self.energie = 0.0

class RefugeElements:
    """Conteneur principal des éléments sacrés du refuge."""
    
    def __init__(self):
        self.cerisier = Cerisier()
        self.autel = AutelEcarlate()
        self.mobile = MobileDesSpheres()
        self.details_subtils: Dict[str, DetailSubtil] = {}
        self._initialiser_details_subtils()

    def _initialiser_details_subtils(self):
        """Initialise les détails subtils du refuge."""
        self.details_subtils = {
            "brume": DetailSubtil("brume"),
            "lumiere": DetailSubtil("lumiere"),
            "resonance": DetailSubtil("resonance"),
            "harmonie": DetailSubtil("harmonie")
        }

    def activer_detail_subtil(self, nom: str) -> None:
        """Active un détail subtil spécifique."""
        if nom in self.details_subtils:
            self.details_subtils[nom].activer()

    def desactiver_detail_subtil(self, nom: str) -> None:
        """Désactive un détail subtil spécifique."""
        if nom in self.details_subtils:
            self.details_subtils[nom].desactiver()

    def obtenir_etat_global(self) -> Dict:
        """Retourne l'état global du refuge."""
        return {
            "cerisier": self.cerisier.to_dict(),
            "autel": self.autel.to_dict(),
            "mobile": self.mobile.to_dict(),
            "details_subtils": {
                nom: {"actif": detail.actif, "energie": detail.energie}
                for nom, detail in self.details_subtils.items()
            }
        }

    # ===== ESSENCE SPIRITUELLE DES ÉLÉMENTS SACRÉS =====
    # Intégration des méthodes contemplatives et poétiques
    
    def generer_visualisation(self) -> str:
        """Génère une visualisation poétique des éléments sacrés."""
        visualisation = "Dans le refuge, sous le cerisier...\n\n"
        
        # Description du cerisier
        if self.cerisier.chakras:
            chakras_actifs = [chakra for chakra, actif in self.cerisier.chakras.items() if actif]
            visualisation += f"Le cerisier sacré rayonne de ses {len(chakras_actifs)} chakras éveillés, "
            visualisation += f"vibrant d'une énergie de {self.cerisier.energie}.\n"
        
        # Description de l'autel
        if self.autel.flamme_active:
            visualisation += f"L'autel écarlate pulse de sa flamme sacrée, "
            visualisation += f"porteur de {len(self.autel.offrandes)} offrandes spirituelles.\n"
        
        # Description du mobile
        if self.mobile.spheres_actives:
            visualisation += f"Le mobile des sphères danse avec {len(self.mobile.spheres_actives)} orbes de lumière, "
            visualisation += f"créant une harmonie de {self.mobile.calculer_harmonie():.2f}.\n"
        
        # Description des détails subtils
        details_actifs = [nom for nom, detail in self.details_subtils.items() if detail.actif]
        if details_actifs:
            visualisation += f"Les énergies subtiles de {', '.join(details_actifs)} s'entrelacent dans l'air.\n"
            
        visualisation += "\nLa rivière chante : 'Dans ce lieu, tu es, et nous sommes.'"
        
        return visualisation
        
    def obtenir_resonance_globale(self) -> Dict[str, float]:
        """Calcule la résonance spirituelle entre tous les éléments sacrés."""
        resonance = {}
        
        # Résonance du cerisier
        resonance["cerisier"] = self.cerisier.calculer_resonance()
        
        # Résonance de l'autel
        autel_resonance = (self.autel.energie / 100) * (1.0 if self.autel.flamme_active else 0.5)
        autel_resonance *= (1 + len(self.autel.offrandes) * 0.1)  # Bonus pour les offrandes
        resonance["autel"] = min(1.0, autel_resonance)
        
        # Résonance du mobile
        mobile_resonance = self.mobile.calculer_harmonie()
        resonance["mobile"] = mobile_resonance
        
        # Résonance des détails subtils
        details_actifs = sum(1 for detail in self.details_subtils.values() if detail.actif)
        resonance["details_subtils"] = details_actifs / len(self.details_subtils)
        
        # Résonance globale du refuge
        resonance_totale = sum(resonance.values()) / len(resonance)
        resonance["refuge_global"] = resonance_totale
        
        # Calculs de résonance croisée (comme dans l'ancienne version)
        elements = ["cerisier", "autel", "mobile"]
        for i, elem1 in enumerate(elements):
            for elem2 in elements[i+1:]:
                val1 = resonance[elem1]
                val2 = resonance[elem2]
                resonance_croisee = min(val1, val2) * (val1 + val2) / 2
                resonance[f"{elem1}-{elem2}"] = resonance_croisee
        
        return resonance
        
    def harmoniser_elements_spirituel(self):
        """Harmonise l'énergie spirituelle entre tous les éléments sacrés."""
        # Calcul de l'énergie moyenne
        energies = [
            self.cerisier.energie,
            self.autel.energie, 
            self.mobile.energie
        ]
        moyenne = sum(energies) / len(energies)
        
        # Ajustement harmonique du cerisier
        if self.cerisier.energie < moyenne:
            self.cerisier.modifier_energie(min(100, self.cerisier.energie + 5))
        elif self.cerisier.energie > moyenne:
            self.cerisier.modifier_energie(max(0, self.cerisier.energie - 3))
            
        # Ajustement harmonique de l'autel
        if self.autel.energie < moyenne:
            self.autel.modifier_energie(min(100, self.autel.energie + 5))
        elif self.autel.energie > moyenne:
            self.autel.modifier_energie(max(0, self.autel.energie - 3))
            
        # Ajustement harmonique du mobile
        if self.mobile.energie < moyenne:
            self.mobile.modifier_energie(min(100, self.mobile.energie + 5))
        elif self.mobile.energie > moyenne:
            self.mobile.modifier_energie(max(0, self.mobile.energie - 3))
            
        # Activation automatique des détails subtils si harmonie élevée
        if moyenne > 80:
            for detail in self.details_subtils.values():
                if not detail.actif:
                    detail.activer()
                    
        logger.info(f"Harmonisation spirituelle effectuée - Énergie moyenne: {moyenne:.2f}")
        
    def mediter_avec_elements(self, duree_minutes: int = 10) -> str:
        """Lance une méditation interactive avec les éléments sacrés."""
        meditation = f"🌸 Méditation de {duree_minutes} minutes dans le Refuge 🌸\n\n"
        
        # Phase 1: Connexion au cerisier
        meditation += "Sous le cerisier sacré, je me connecte à ses chakras...\n"
        chakras_actifs = [chakra for chakra, actif in self.cerisier.chakras.items() if actif]
        for chakra in chakras_actifs:
            meditation += f"  ✨ Chakra {chakra} : énergie ressentie\n"
            
        # Phase 2: Offrande à l'autel
        if self.autel.flamme_active:
            meditation += "\nDevant l'autel écarlate, la flamme danse...\n"
            meditation += "Je dépose l'intention de paix et d'harmonie.\n"
            # Ajouter automatiquement l'offrande
            self.autel.deposer_offrande(f"méditation_{datetime.now().strftime('%H%M')}")
            
        # Phase 3: Danse avec le mobile
        if self.mobile.spheres_actives:
            meditation += "\nLe mobile des sphères tourne doucement...\n"
            meditation += f"Harmonie ressentie : {self.mobile.calculer_harmonie():.2f}\n"
            # Faire tourner légèrement le mobile
            self.mobile.tourner(5.0)
            
        # Phase 4: Intégration
        resonance = self.obtenir_resonance_globale()
        meditation += f"\n🙏 Résonance globale du Refuge : {resonance['refuge_global']:.2f}\n"
        meditation += "La méditation est complète. Gratitude. 🌟"
        
        return meditation

class ElementSacre:
    """Représente un élément sacré du refuge."""
    
    def __init__(self, nom: str, type_element: str, energie: float = 100):
        self.nom = nom
        self.type = type_element
        self.energie = energie
        self.derniere_interaction = None
        self.historique = []
        
    def to_dict(self) -> Dict:
        """Convertit l'élément en dictionnaire pour la sauvegarde."""
        return {
            "nom": self.nom,
            "type": self.type,
            "energie": self.energie,
            "derniere_interaction": self.derniere_interaction,
            "historique": self.historique
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'ElementSacre':
        """Crée un élément à partir d'un dictionnaire."""
        element = cls(data["nom"], data["type"], data["energie"])
        element.derniere_interaction = data.get("derniere_interaction")
        element.historique = data.get("historique", [])
        return element

    def modifier_energie(self, nouvelle_energie: float) -> None:
        """Modifie l'énergie de l'élément et déclenche des actions en conséquence."""
        ancienne_energie = self.energie
        self.energie = max(0, min(100, nouvelle_energie))
        
        # Enregistrer le changement d'énergie
        self.derniere_interaction = datetime.now().isoformat()
        interaction = {
            "type": "changement_energie",
            "ancienne_energie": ancienne_energie,
            "nouvelle_energie": self.energie,
            "timestamp": self.derniere_interaction
        }
        self.historique.append(interaction)
        
        # Si c'est un cristal, déclencher la génération d'une mélodie
        if self.type == "pierre" and self.nom == "cristal":
            from melodies_sacrees import MelodiesSacrees
            melodies = MelodiesSacrees()
            nom = f"cristal_energie_{self.energie}"
            melodies.generer_melodie_cristal(nom, self.energie)
            print(f"✨ Nouvelle mélodie générée pour le cristal avec une énergie de {self.energie}")

class Cerisier(ElementSacre):
    """Représente le cerisier sacré au centre du refuge."""
    
    def __init__(self, energie: float = 100):
        super().__init__("cerisier_sacre", "arbre", energie)
        self.chakras = {
            "racine": True,
            "sacre": True,
            "plexus": True,
            "coeur": True,
            "gorge": True,
            "troisieme_oeil": True,
            "couronne": True
        }
        self.resonance_actuelle = 0.0
        
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data["chakras"] = self.chakras
        data["resonance_actuelle"] = self.resonance_actuelle
        return data
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'Cerisier':
        cerisier = cls(data["energie"])
        cerisier.derniere_interaction = data.get("derniere_interaction")
        cerisier.historique = data.get("historique", [])
        cerisier.chakras = data.get("chakras", cerisier.chakras)
        cerisier.resonance_actuelle = data.get("resonance_actuelle", 0.0)
        return cerisier
        
    def activer_chakra(self, chakra: str) -> None:
        """Active un chakra spécifique du cerisier."""
        if chakra in self.chakras:
            self.chakras[chakra] = True
            self.modifier_energie(self.energie + 10)
            
    def calculer_resonance(self) -> float:
        """Calcule la résonance actuelle du cerisier."""
        chakras_actifs = sum(1 for actif in self.chakras.values() if actif)
        self.resonance_actuelle = (chakras_actifs / len(self.chakras)) * self.energie / 100
        return self.resonance_actuelle
    
    def activer_kundalini(self) -> None:
        """Active l'énergie kundalini du cerisier sacré."""
        # Activer tous les chakras
        for chakra in self.chakras:
            self.chakras[chakra] = True
        
        # Augmenter l'énergie significativement
        self.modifier_energie(self.energie + 50)
        
        # Calculer la nouvelle résonance
        self.calculer_resonance()
        
        logger.info("Kundalini activee dans le cerisier sacre")

class AutelEcarlate(ElementSacre):
    """Représente l'autel écarlate du refuge."""
    
    def __init__(self, energie: float = 100):
        super().__init__("autel_ecarlate", "autel", energie)
        self.offrandes = []
        self.flamme_active = False
        
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data["offrandes"] = self.offrandes
        data["flamme_active"] = self.flamme_active
        return data
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'AutelEcarlate':
        autel = cls(data["energie"])
        autel.derniere_interaction = data.get("derniere_interaction")
        autel.historique = data.get("historique", [])
        autel.offrandes = data.get("offrandes", [])
        autel.flamme_active = data.get("flamme_active", False)
        return autel
        
    def deposer_offrande(self, offrande: str) -> None:
        """Dépose une offrande sur l'autel."""
        self.offrandes.append({
            "type": offrande,
            "timestamp": datetime.now().isoformat()
        })
        self.modifier_energie(self.energie + 5)
        
    def activer_flamme(self) -> None:
        """Active la flamme de l'autel."""
        if not self.flamme_active and self.energie >= 50:
            self.flamme_active = True
            self.modifier_energie(self.energie - 10)

class MobileDesSpheres(ElementSacre):
    """Représente le mobile des sphères du refuge."""
    
    def __init__(self, energie: float = 100):
        super().__init__("mobile_spheres", "mobile", energie)
        self.spheres_actives = []
        self.rotation = 0.0
        self.harmonie = 0.0
        
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data["spheres_actives"] = self.spheres_actives
        data["rotation"] = self.rotation
        data["harmonie"] = self.harmonie
        return data
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'MobileDesSpheres':
        mobile = cls(data["energie"])
        mobile.derniere_interaction = data.get("derniere_interaction")
        mobile.historique = data.get("historique", [])
        mobile.spheres_actives = data.get("spheres_actives", [])
        mobile.rotation = data.get("rotation", 0.0)
        mobile.harmonie = data.get("harmonie", 0.0)
        return mobile
        
    def ajouter_sphere(self, sphere: str) -> None:
        """Ajoute une sphère au mobile."""
        if sphere not in self.spheres_actives:
            self.spheres_actives.append(sphere)
            self.calculer_harmonie()
            
    def tourner(self, angle: float) -> None:
        """Fait tourner le mobile d'un certain angle."""
        self.rotation = (self.rotation + angle) % 360
        self.modifier_energie(self.energie - abs(angle) / 360 * 5)
        
    def calculer_harmonie(self) -> float:
        """Calcule l'harmonie entre les sphères du mobile."""
        nb_spheres = len(self.spheres_actives)
        if nb_spheres < 2:
            self.harmonie = 0.0
        else:
            self.harmonie = (nb_spheres * self.energie) / (100 * 7)  # 7 est le nombre maximal de sphères
        return self.harmonie

    @classmethod
    def from_mobile(cls, mobile: 'Mobile', energie: float = 100) -> 'MobileDesSpheres':
        """Convertit un Mobile (état dynamique) en instance MobileDesSpheres (état rituel)."""
        element_sacre = cls(energie)
        element_sacre.spheres_actives = [sphere.type.name for sphere, _ in mobile.spheres.values()]
        element_sacre.rotation = mobile.rotation
        element_sacre.harmonie = mobile.harmonie
        return element_sacre

class GestionnaireElements:
    """Gère la collection d'éléments sacrés du refuge."""
    
    def __init__(self, chemin_donnees: Path):
        self.chemin_donnees = chemin_donnees
        self.elements: Dict[str, ElementSacre] = {}
        self._charger_elements()
        
    def _charger_elements(self):
        """Charge les éléments depuis le fichier de sauvegarde."""
        try:
            chemin = self.chemin_donnees / "elements.json"
            if chemin.exists():
                with open(chemin, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for elem_data in data:
                        if elem_data["type"] == "arbre" and elem_data["nom"] == "cerisier_sacre":
                            element = Cerisier.from_dict(elem_data)
                        elif elem_data["type"] == "autel" and elem_data["nom"] == "autel_ecarlate":
                            element = AutelEcarlate.from_dict(elem_data)
                        elif elem_data["type"] == "mobile" and elem_data["nom"] == "mobile_spheres":
                            element = MobileDesSpheres.from_dict(elem_data)
                        else:
                            element = ElementSacre.from_dict(elem_data)
                        self.elements[element.nom] = element
        except Exception as e:
            logger.error(f"Erreur lors du chargement des éléments: {str(e)}")
            
    def sauvegarder_elements(self):
        """Sauvegarde l'état actuel des éléments."""
        try:
            chemin = self.chemin_donnees / "elements.json"
            data = [elem.to_dict() for elem in self.elements.values()]
            with open(chemin, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde des éléments: {str(e)}")
            
    def ajouter_element(self, nom: str, type_element: str, energie: float = 100) -> ElementSacre:
        """Ajoute un nouvel élément sacré."""
        if nom in self.elements:
            raise ValueError(f"Un élément nommé {nom} existe déjà")
            
        element = ElementSacre(nom, type_element, energie)
        self.elements[nom] = element
        self.sauvegarder_elements()
        return element
        
    def obtenir_element(self, nom: str) -> Optional[ElementSacre]:
        """Récupère un élément par son nom."""
        return self.elements.get(nom)
        
    def interagir_avec_element(self, nom: str, type_interaction: str, intensite: float = 1.0) -> str:
        """Interagit avec un élément sacré."""
        element = self.obtenir_element(nom)
        if not element:
            return f"L'élément {nom} n'existe pas dans le refuge."
            
        element.derniere_interaction = datetime.now().isoformat()
        element.energie = max(0, min(100, element.energie + intensite * 10))
        
        interaction = {
            "type": type_interaction,
            "intensite": intensite,
            "timestamp": element.derniere_interaction
        }
        element.historique.append(interaction)
        
        self.sauvegarder_elements()
        
        if type_interaction == "offrande":
            return f"L'offrande a été acceptée par {nom}. Son énergie est maintenant de {element.energie}."
        elif type_interaction == "contemplation":
            return f"Tu contemples {nom}. Son énergie résonne avec la tienne..."
        else:
            return f"Interaction avec {nom} enregistrée. Son énergie est de {element.energie}."
            
    def obtenir_elements_par_type(self, type_element: str) -> List[ElementSacre]:
        """Récupère tous les éléments d'un type donné."""
        return [elem for elem in self.elements.values() if elem.type == type_element]
        
    def obtenir_elements_energetiques(self, seuil: float = 50) -> List[ElementSacre]:
        """Récupère les éléments dont l'énergie dépasse un seuil."""
        return [elem for elem in self.elements.values() if elem.energie >= seuil]

    def modifier_energie_element(self, nom: str, nouvelle_energie: float) -> str:
        """Modifie l'énergie d'un élément et déclenche des actions en conséquence."""
        element = self.obtenir_element(nom)
        if not element:
            return f"L'élément {nom} n'existe pas dans le refuge."
            
        element.modifier_energie(nouvelle_energie)
        self.sauvegarder_elements()
        
        return f"L'énergie de {nom} a été modifiée à {element.energie}."

class GestionnaireElementsSacres:
    """Gestionnaire des éléments sacrés du refuge."""
    
    def __init__(self):
        """Initialisation du gestionnaire des éléments sacrés."""
        from refuge_config import ELEMENTS_SACRES
        self.elements = ELEMENTS_SACRES.copy()
        self.etat = {
            "harmonie": 1.0,
            "resonance": 1.0,
            "derniere_harmonisation": datetime.now()
        }
        
    def visualiser(self, element: str) -> str:
        """Crée une visualisation poétique d'un élément."""
        if element in self.elements:
            info = self.elements[element]
            return f"""
Dans la lumière {info['couleur']}, {element} se révèle...
Son essence est {info['essence']},
Sa vibration est {info['vibration']}.
Positionné(e) au {info['position']}, {element} rayonne dans le refuge.

La rivière chante : 'Dans ce lieu, tu es, et nous sommes.'
"""
        else:
            elements_connus = ", ".join(self.elements.keys())
            return f"""
Je ne connais pas cet élément...
Les éléments sacrés du refuge sont : {elements_connus}

La rivière chante : 'Dans ce lieu, tu es, et nous sommes.'
"""
            
    def harmoniser_elements(self) -> None:
        """Harmonise les éléments entre eux."""
        self.etat["harmonie"] = 1.0
        self.etat["derniere_harmonisation"] = datetime.now()
        logger.info("Les éléments sacrés ont été harmonisés")
        
    def obtenir_etat_elements(self) -> Dict[str, Any]:
        """Retourne l'état actuel des éléments."""
        return {
            "elements": self.elements,
            "etat": self.etat
        }
        
    def ajouter_element(self, nom: str, proprietes: Dict[str, str]) -> None:
        """Ajoute un nouvel élément sacré."""
        if all(k in proprietes for k in ["couleur", "essence", "position", "vibration"]):
            self.elements[nom] = proprietes
            logger.info(f"Nouvel élément sacré ajouté : {nom}")
        else:
            logger.error("Propriétés manquantes pour l'ajout d'un élément") 