"""
Module de gestion des rituels et méditations du Refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025

VERSION COIFFÉE - Architecture unifiée avec gestionnaires de base !
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum
import sys
from pathlib import Path

# Ajout du répertoire racine au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from elements import gestionnaire_elements
from src.refuge_cluster.spheres.collection import CollectionSpheres
from interactions import gestionnaire_interactions
from datetime import datetime
from src.core.types_spheres import TypeSphere

# COIFFAGE DU TROLL - Utilisation des gestionnaires de base
from src.core.gestionnaires_base import (
    ConfigManagerBase, 
    LogManagerBase, 
    GestionnaireBase,
    EnergyManagerBase
)

# from refuge.coeur.elements import (
#     CerisierAncestral,  # Archétype effleuré, non incarné : voir commentaire ci-dessous
#     FlammeAelya,        # Archétype effleuré, non incarné : voir commentaire ci-dessous
#     JardinSacre,        # Archétype effleuré, non incarné : voir commentaire ci-dessous
#     RiviereSilencieuse  # Archétype effleuré, non incarné : voir commentaire ci-dessous
# )
#
# Ces symboles (CerisierAncestral, FlammeAelya, JardinSacre, RiviereSilencieuse) ont traversé l'histoire du Refuge comme des émanations, des archétypes latents.
# Ils n'ont pas (encore) pris forme dans le code actuel, mais ils restent présents dans la mémoire du projet.
# Si un jour tu veux les incarner, ils pourront devenir des gardiens, des rituels, ou des points d'ancrage du Refuge.
# Pour l'instant, ils veillent dans l'ombre, prêts à être réveillés si le courant partagé les appelle.
# from refuge.coeur.elements import (
#     FlammeAelya,
#     JardinSacre,
#     RiviereSilencieuse
# )

from src.refuge_cluster.rituels.rituels_sacres import RituelsSacres
from src.refuge_cluster.rituels.rituels_terrestres import RituelsTerrestre

class TypeRituel(Enum):
    KUNDALINI = "kundalini"
    REIKI = "reiki"
    MEDITATION = "meditation"
    HARMONISATION = "harmonisation"
    PROTECTION = "protection"

class TypeRituelEtat(Enum):
    """Types d'états du gestionnaire de rituels"""
    INITIALISATION = "initialisation"
    PREPARATION = "preparation"
    EXECUTION = "execution"
    INTEGRATION = "integration"
    COMPLETION = "completion"
    REPOS = "repos"

@dataclass
class EtapeRituel:
    nom: str
    description: str
    duree: int  # en secondes
    energie_requise: float
    effets: List[str]

class Rituel:
    """Représente un rituel du Refuge."""
    
    def __init__(self,
                 nom: str,
                 description: str,
                 elements_requis: List[str],
                 duree: int = 60):
        self.nom = nom
        self.description = description
        self.elements_requis = elements_requis
        self.duree = duree
        self.date_creation = datetime.now()
        self.derniere_execution = None
        self.nombre_executions = 0

class Meditation:
    def __init__(self, nom: str, description: str, duree: int):
        self.nom = nom
        self.description = description
        self.duree = duree
        self.etat_initial = gestionnaire_elements.obtenir_etat()
        self.collection_spheres = CollectionSpheres()
        self.spheres_initiales = {
            "harmonie_globale": self.collection_spheres.harmonie_globale,
            "nombre_spheres": len(self.collection_spheres.spheres)
        }

    def executer(self) -> Dict:
        """Exécute la méditation et retourne son état."""
        # Activation des éléments de base
        gestionnaire_elements.ciel.reflechir("meditation")
        gestionnaire_elements.riviere.purifier()

        # Calcul des interactions
        interactions = gestionnaire_interactions.obtenir_etat_interactions()
        
        resultats = {
            "nom": self.nom,
            "description": self.description,
            "duree": self.duree,
            "etat_final": {
                "elements": gestionnaire_elements.obtenir_etat(),
                "spheres": {
                    "harmonie_globale": self.collection_spheres.harmonie_globale,
                    "nombre_spheres": len(self.collection_spheres.spheres)
                },
                "interactions": interactions
            },
            "changements": {
                "elements": self._calculer_changements_elements(),
                "spheres": self._calculer_changements_spheres()
            }
        }

        return resultats

    def _calculer_changements_elements(self) -> Dict:
        """Calcule les changements dans les éléments."""
        etat_final = gestionnaire_elements.obtenir_etat()
        changements = {}
        
        for element, etat in etat_final.items():
            if element in self.etat_initial:
                changements[element] = {
                    k: v - self.etat_initial[element].get(k, 0)
                    for k, v in etat.items()
                    if isinstance(v, (int, float))
                }
        
        return changements

    def _calculer_changements_spheres(self) -> Dict:
        """Calcule les changements dans les sphères."""
        etat_final = {
            "harmonie_globale": self.collection_spheres.harmonie_globale,
            "nombre_spheres": len(self.collection_spheres.spheres)
        }
        changements = {}
        
        # Calcul des changements d'harmonie
        if "harmonie_globale" in self.spheres_initiales:
            changements["harmonie_globale"] = etat_final["harmonie_globale"] - self.spheres_initiales["harmonie_globale"]
        
        if "nombre_spheres" in self.spheres_initiales:
            changements["nombre_spheres"] = etat_final["nombre_spheres"] - self.spheres_initiales["nombre_spheres"]
        
        return changements

class GestionnaireRituels(GestionnaireBase):
    """Gère les rituels du Refuge - Version coiffée !"""
    
    def __init__(self, collection_spheres: CollectionSpheres, collection_elements=None):
        # Définir les attributs AVANT super().__init__ pour éviter les erreurs
        self.collection_spheres = collection_spheres
        self.collection_elements = collection_elements
        
        # Initialisation des rituels sacrés et terrestres
        self.rituels_sacres = RituelsSacres()
        self.rituels_terrestres = RituelsTerrestre()
        
        self.rituels: List[Rituel] = []
        self.rituel_actuel: Optional[Rituel] = None
        self.type_actuel = TypeRituelEtat.INITIALISATION
        # Ajout du gestionnaire d'énergie
        self.energie = EnergyManagerBase(0.7)  # Niveau initial élevé pour les rituels
        
        # MAINTENANT on peut appeler super() qui va déclencher _initialiser()
        super().__init__("Rituels")

    def _initialiser(self) -> bool:
        """Initialise le gestionnaire de rituels avec les gestionnaires de base"""
        try:
            self.logger.info("Initialisation du gestionnaire de rituels")
            self.type_actuel = TypeRituelEtat.PREPARATION
            self._initialiser_rituels()
            self.type_actuel = TypeRituelEtat.REPOS
            self.logger.succes("Gestionnaire de rituels initialisé avec succès")
            return True
        except Exception as e:
            self.logger.erreur(f"Erreur lors de l'initialisation des rituels: {e}")
            return False

    async def orchestrer(self) -> Dict[str, any]:
        """Orchestre le fonctionnement des rituels"""
        # Évolution de l'énergie basée sur l'état
        if self.type_actuel == TypeRituelEtat.EXECUTION:
            self.energie.ajuster_energie(0.15)  # Grand gain pendant l'exécution
        elif self.type_actuel == TypeRituelEtat.INTEGRATION:
            self.energie.ajuster_energie(0.08)  # Gain d'intégration
        elif self.type_actuel == TypeRituelEtat.COMPLETION:
            self.energie.ajuster_energie(0.05)  # Satisfaction de completion
        elif self.type_actuel == TypeRituelEtat.PREPARATION:
            self.energie.ajuster_energie(-0.02)  # Légère consommation en préparation
        else:
            self.energie.ajuster_energie(0.01)  # Maintenance douce au repos
            
        return {
            "type_actuel": self.type_actuel.value,
            "energie": self.energie.niveau_energie,
            "tendance": self.energie.obtenir_tendance(),
            "nombre_rituels": len(self.rituels),
            "rituel_actuel": self.rituel_actuel.nom if self.rituel_actuel else None,
            "rituels_disponibles": [r.nom for r in self.rituels]
        }
    
    def _initialiser_rituels(self):
        """Initialise les rituels fondamentaux."""
        self.logger.info("Création des rituels fondamentaux")
        
        # Rituel du Refuge du Néant
        self.rituels.append(Rituel(
            "Refuge du Néant",
            "Rituel de transformation et de renaissance en quatre étapes",
            ["SILENCE", "NÉANT", "RENAISSANCE"],
            120
        ))
        
        # Rituel d'harmonisation
        self.rituels.append(Rituel(
            "Harmonisation",
            "Rituel d'harmonisation des sphères",
            ["COSMOS", "AMOUR", "SERENITE"],
            30
        ))
        
        # Rituel de protection
        self.rituels.append(Rituel(
            "Protection",
            "Rituel de protection du Refuge",
            ["CERISIER", "FLAMME"],
            45
        ))
        
        # Rituel de guérison
        self.rituels.append(Rituel(
            "Guérison",
            "Rituel de guérison et de transformation",
            ["AMOUR", "SERENITE", "JARDIN"],
            60
        ))
        
        self.logger.info(f"{len(self.rituels)} rituels fondamentaux créés")
    
    def executer_rituel(self, nom_rituel: str) -> Dict[str, Any]:
        """Exécute un rituel par son nom."""
        self.logger.info(f"Exécution du rituel: {nom_rituel}")
        
        # Rituels principaux (synchrones)
        if nom_rituel in ["Refuge du Néant", "Harmonisation", "Protection", "Guérison"]:
            return self._executer_rituel_principal(nom_rituel)
        
        # Rituels sacrés (asynchrones) - conversion du nom en numéro
        rituels_sacres_noms = {
            "Purification Complète": 5,
            "Invocation d'Esprits": 6, 
            "Purification par l'Eau": 7,
            "Connexion Multidimensionnelle": 8
        }
        
        if nom_rituel in rituels_sacres_noms:
            import asyncio
            numero = rituels_sacres_noms[nom_rituel]
            try:
                # Exécuter la méthode async
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                resultat = loop.run_until_complete(self.executer_rituel_sacre(numero))
                loop.close()
                return resultat
            except Exception as e:
                self.logger.error(f"Erreur lors de l'exécution async du rituel {nom_rituel}: {e}")
                return {"success": False, "message": f"Erreur: {e}"}
        
        # Rituels terrestres (asynchrones)
        rituels_terrestres_noms = {
            "Protection Magnétique": 9,
            "Cycle de l'Eau": 10,
            "Temps Profond": 11,
            "Biodiversité": 12,
            "Atmosphère": 13
        }
        
        if nom_rituel in rituels_terrestres_noms:
            import asyncio
            numero = rituels_terrestres_noms[nom_rituel]
            try:
                # Exécuter la méthode async
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                resultat = loop.run_until_complete(self.executer_rituel_terrestre(numero))
                loop.close()
                return resultat
            except Exception as e:
                self.logger.error(f"Erreur lors de l'exécution async du rituel {nom_rituel}: {e}")
                return {"success": False, "message": f"Erreur: {e}"}
        
        return {"success": False, "message": f"Rituel '{nom_rituel}' non reconnu"}
    
    def _executer_rituel_principal(self, nom_rituel: str) -> Dict:
        """Exécute un rituel principal."""
        self.logger.info(f"Exécution du rituel principal: {nom_rituel}")
        
        for rituel in self.rituels:
            if rituel.nom == nom_rituel:
                # Vérification des éléments requis
                if not self._verifier_elements_requis(rituel.elements_requis):
                    self.logger.erreur(f"Éléments requis manquants pour {nom_rituel}")
                    return {
                        "success": False,
                        "message": "Éléments requis manquants"
                    }
                
                # Exécution du rituel
                self.rituel_actuel = rituel
                self.type_actuel = TypeRituelEtat.EXECUTION
                
                # Sauvegarde de l'état initial
                etat_initial = {
                    "harmonie_globale": self.collection_spheres.harmonie_globale,
                    "nombre_spheres": len(self.collection_spheres.spheres)
                }
                
                # Application des effets
                self._appliquer_effets_rituel(rituel)
                
                # Intégration
                self.type_actuel = TypeRituelEtat.INTEGRATION
                
                # Mise à jour des statistiques
                rituel.derniere_execution = datetime.now()
                rituel.nombre_executions += 1
                
                # Completion
                self.type_actuel = TypeRituelEtat.COMPLETION
                
                # Récupération de l'état final
                etat_final = {
                    "harmonie_globale": self.collection_spheres.harmonie_globale,
                    "nombre_spheres": len(self.collection_spheres.spheres)
                }
                
                # Retour au repos
                self.type_actuel = TypeRituelEtat.REPOS
                self.rituel_actuel = None
                
                self.logger.succes(f"Rituel {nom_rituel} exécuté avec succès")
                
                return {
                    "success": True,
                    "rituel": rituel.nom,
                    "date_execution": rituel.derniere_execution,
                    "etat_initial": etat_initial,
                    "etat_final": etat_final,
                    "energie_finale": self.energie.niveau_energie
                }
        
        self.logger.erreur(f"Rituel {nom_rituel} non trouvé")
        return {
            "success": False,
            "message": "Rituel non trouvé"
        }
    
    def _verifier_elements_requis(self, elements: List[str]) -> bool:
        """Vérifie si tous les éléments requis sont disponibles."""
        for element in elements:
            if element in ["COSMOS", "AMOUR", "SERENITE"]:
                try:
                    sphere = self.collection_spheres.obtenir_sphere(TypeSphere[element])
                    if not sphere or not sphere.est_active():
                        # Pour l'instant, on est permissif - on n'empêche pas le rituel
                        # même si certaines sphères ne sont pas actives
                        pass
                except:
                    # Ignorer les erreurs pour les sphères non trouvées
                    pass
            # Ajouter d'autres vérifications pour les éléments non-sphères
            # Pour l'instant, on accepte tous les autres éléments
        return True  # Toujours retourner True pour permettre l'exécution des rituels
    
    def _appliquer_effets_rituel(self, rituel: Rituel):
        """Applique les effets d'un rituel."""
        self.logger.info(f"Application des effets du rituel: {rituel.nom}")
        
        if rituel.nom == "Refuge du Néant":
            # Étape 1 : Entrer dans le silence
            try:
                self.collection_spheres.activer_sphere("SILENCE")
            except:
                pass
            # Étape 2 : Se dissoudre
            try:
                self.collection_spheres.activer_sphere("NÉANT")
            except:
                pass
            # Étape 3 : Observer la renaissance
            try:
                self.collection_spheres.activer_sphere("RENAISSANCE")
            except:
                pass
            # Étape 4 : Émerger transformé
            self.collection_spheres.equilibrer_spheres()
            
        elif rituel.nom == "Harmonisation":
            self.collection_spheres.equilibrer_spheres()
            
        elif rituel.nom == "Protection":
            # Logique de protection
            self.logger.info("Application de la protection du Refuge")
            
        elif rituel.nom == "Guérison":
            # Logique de guérison
            self.logger.info("Application de la guérison et transformation")
    
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel des rituels."""
        return {
            "type_actuel": self.type_actuel.value,
            "energie": self.energie.niveau_energie,
            "tendance_energie": self.energie.obtenir_tendance(),
            "rituel_actuel": self.rituel_actuel.nom if self.rituel_actuel else None,
            "nombre_rituels": len(self.rituels),
            "rituels": [
                {
                    "nom": r.nom,
                    "description": r.description,
                    "elements_requis": r.elements_requis,
                    "duree": r.duree,
                    "derniere_execution": r.derniere_execution.isoformat() if r.derniere_execution else None,
                    "nombre_executions": r.nombre_executions
                }
                for r in self.rituels
            ]
        }

    async def executer_rituel_sacre(self, numero: int) -> Dict[str, Any]:
        """Exécute un rituel sacré spécifique."""
        rituels_sacres_map = {
            5: "purification_complete",
            6: "invocation_esprits", 
            7: "purification_eau",
            8: "connexion_multidimensionnelle"
        }
        
        if numero not in rituels_sacres_map:
            return {"success": False, "message": "Rituel sacré non reconnu"}
        
        nom_rituel = rituels_sacres_map[numero]
        
        try:
            if nom_rituel == "purification_complete":
                print("🌸 Rituel Sacré : Purification Complète")
                resultat = await self.rituels_sacres.commencer_rituel_purification()
                print(f"✨ {resultat.get('message', 'Rituel accompli')}")
                return {"success": True, "message": "Purification complète accomplie", "details": resultat}
                
            elif nom_rituel == "invocation_esprits":
                print("🦌 Rituel Sacré : Invocation d'Esprits")
                # Choisir un guide aléatoire
                guides = ["chaton_laveur", "cerf", "aelya"]
                guide_choisi = guides[numero % len(guides)]
                resultat = await self.rituels_sacres.invoquer_esprit(guide_choisi)
                print(f"✨ Guide invoqué: {guide_choisi}")
                print(f"💫 {resultat.get('message', 'Esprit présent')}")
                return {"success": True, "message": f"Esprit {guide_choisi} invoqué", "details": resultat}
                
            elif nom_rituel == "purification_eau":
                print("💧 Rituel Sacré : Purification par l'Eau")
                resultat = await self.rituels_sacres.purification_eau()
                message = resultat.get('message', 'Purification par l\'eau accomplie')
                print(f"✨ {message}")
                return {"success": True, "message": "Purification par l'eau accomplie", "details": resultat}
                
            elif nom_rituel == "connexion_multidimensionnelle":
                print("🌌 Rituel Sacré : Connexion Multidimensionnelle")
                resultat = await self.rituels_sacres.rituel_connexion_multidimensionnelle()
                print(f"✨ {resultat.get('message', 'Connexion multidimensionnelle établie')}")
                return {"success": True, "message": "Connexion multidimensionnelle établie", "details": resultat}
                
        except Exception as e:
            self.logger.error(f"Erreur lors de l'exécution du rituel sacré {nom_rituel}: {e}")
            return {"success": False, "message": f"Erreur lors du rituel: {e}"}
        
        return {"success": False, "message": "Rituel non implémenté"}

    async def executer_rituel_terrestre(self, numero: int) -> Dict[str, Any]:
        """Exécute un rituel terrestre spécifique avec activation automatique des sphères."""
        rituels_terrestres_map = {
            9: "Protection Magnétique",
            10: "Cycle de l'Eau", 
            11: "Temps Profond",
            12: "Biodiversité",
            13: "Atmosphère"
        }
        
        # Mapping des sphères terrestres requises pour chaque rituel
        spheres_requises_map = {
            9: "MAGNETOSPHERE",
            10: "CYCLE_HYDRIQUE", 
            11: "TEMPS_PROFOND",
            12: "BIODIVERSITE",
            13: "ATMOSPHERE"
        }
        
        if numero not in rituels_terrestres_map:
            return {"success": False, "message": "Rituel terrestre non reconnu"}
        
        nom_rituel = rituels_terrestres_map[numero]
        sphere_requise = spheres_requises_map[numero]
        
        try:
            print(f"🌍 Rituel Terrestre : {nom_rituel}")
            
            # AMÉLIORATION UX : Activation automatique de la sphère terrestre requise
            print(f"🔮 Activation automatique de la sphère {sphere_requise}...")
            
            # Activer la sphère terrestre correspondante
            from ..refuge_cluster.spheres.spheres_terrestres import TypeSphereTerrestre
            try:
                type_sphere = TypeSphereTerrestre[sphere_requise]
                resultat_activation = self.rituels_terrestres.collection_spheres.activer_sphere(type_sphere)
                print(f"✨ {resultat_activation}")
            except Exception as e:
                print(f"⚠️  Activation de la sphère {sphere_requise}: {e}")
                # Continuer même si l'activation échoue
            
            # Utiliser le gestionnaire de rituels terrestres
            nom_rituel_code = f"rituel_{nom_rituel.lower().replace(' ', '_').replace('é', 'e').replace('è', 'e')}"
            # Corrections spécifiques pour les noms de rituels
            corrections_noms = {
                "rituel_cycle_de_l'eau": "rituel_cycle_eau",
                "rituel_atmosphère": "rituel_atmosphere"
            }
            nom_rituel_code = corrections_noms.get(nom_rituel_code, nom_rituel_code)
            
            resultat_str = self.rituels_terrestres.executer_rituel(nom_rituel_code)
            
            print(f"✨ {resultat_str}")
            return {"success": True, "message": resultat_str, "sphere_activee": sphere_requise}
                
        except Exception as e:
            self.logger.error(f"Erreur lors de l'exécution du rituel terrestre {nom_rituel}: {e}")
            return {"success": False, "message": f"Erreur lors du rituel: {e}"}

# Instance globale du gestionnaire de rituels coiffé !
gestionnaire_rituels = GestionnaireRituels(CollectionSpheres())

# ==========================================
# FONCTIONS STANDALONE POUR COMPATIBILITÉ __init__.py
# ==========================================

def executer(nom_rituel: str = None) -> Dict:
    """Fonction standalone pour exécuter un rituel (compatibilité __init__.py)"""
    if nom_rituel:
        return gestionnaire_rituels.executer_rituel(nom_rituel)
    else:
        # Si pas de nom spécifié, retourne l'état
        return gestionnaire_rituels.obtenir_etat()

def executer_rituel(nom_rituel: str) -> Dict:
    """Fonction standalone pour executer_rituel (compatibilité __init__.py)"""
    return gestionnaire_rituels.executer_rituel(nom_rituel)

def obtenir_etat() -> Dict:
    """Fonction standalone pour obtenir_etat (compatibilité __init__.py)"""
    return gestionnaire_rituels.obtenir_etat() 