"""
Module de gestion des états internes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Gère la compréhension et l'évolution des états internes des sphères.
"""

from typing import Dict, List, Optional, Callable, Any, Tuple
from enum import Enum
from datetime import datetime
import numpy as np
from pydantic import BaseModel, Field
from .elements_sacres import GestionnaireElements, ElementSacre
from .journalisation import GestionnaireJournal, EvenementJournal

class TypeEtat(Enum):
    """Types d'états internes possibles."""
    CALME = "calme"
    AGITE = "agite"
    CONCENTRE = "concentre"
    DISTRAIT = "distrait"
    FATIGUE = "fatigue"
    ENERGIE = "energie"
    HARMONIEUX = "harmonieux"
    DESEQUILIBRE = "desequilibre"
    EVOLUTION = "evolution"
    STAGNATION = "stagnation"
    STABLE = "stable"
    FLUIDE = "fluide"
    ADAPTABLE = "adaptable"
    INTENSE = "intense"
    LEGER = "leger"
    LIBRE = "libre"
    EVEILLE = "eveille"
    POSITIF = "positif"
    INSPIRE = "inspire"
    MYSTERIEUX = "mysterieux"
    PROFOND = "profond"
    PATIENT = "patient"
    EVOLUTIF = "evolutif"
    VASTE = "vaste"
    OUVERT = "ouvert"
    VIVANT = "vivant"
    CROISSANT = "croissant"

class NiveauConscience(Enum):
    """Niveaux de conscience possibles."""
    INCONSCIENT = "inconscient"
    SUBCONSCIENT = "subconscient"
    CONSCIENT = "conscient"
    SURCONSCIENT = "surconscient"

class ConditionTransition(BaseModel):
    """Représente une condition pour une transition d'état."""
    nom: str
    description: str
    fonction: Callable[[Dict[str, Any]], bool]
    priorite: int = 0

class EffetTransition(BaseModel):
    """Représente un effet secondaire lors d'une transition d'état."""
    nom: str
    description: str
    fonction: Callable[[Dict[str, Any]], Dict[str, Any]]
    duree: int = 0  # 0 = permanent, >0 = temporaire en cycles

class EtatInterne(BaseModel):
    """Représente l'état interne d'une sphère."""
    type_etat: TypeEtat = Field(default=TypeEtat.CALME)
    niveau_conscience: NiveauConscience = Field(default=NiveauConscience.CONSCIENT)
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    stabilite: float = Field(default=0.5, ge=0.0, le=1.0)
    timestamp: datetime = Field(default_factory=datetime.now)
    historique: List[Dict] = Field(default_factory=list)
    taille_max_historique: int = Field(default=10)
    effets_actifs: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    resistance_transition: Dict[TypeEtat, float] = Field(default_factory=dict)
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.timestamp is None:
            self.timestamp = datetime.now()
        if not self.historique:
            self.historique = []
        if not self.effets_actifs:
            self.effets_actifs = {}
    
    def mettre_a_jour(self, nouveau_type: TypeEtat, intensite: float, stabilite: float):
        """Met à jour l'état interne."""
        # Vérifier la résistance à la transition
        if nouveau_type != self.type_etat:
            resistance = self.resistance_transition.get(nouveau_type, 0.0)
            if resistance > 0.5:  # Seuil de résistance élevé
                # Réduire l'intensité de la transition
                intensite = max(0.0, intensite - resistance)
                stabilite = max(0.0, stabilite - resistance)
                # Si la résistance est trop forte, on reste dans l'état actuel
                if resistance > 0.8:
                    nouveau_type = self.type_etat
        
        # Enregistrer l'ancien état dans l'historique
        self.historique.append({
            "type": self.type_etat.value,
            "niveau": self.niveau_conscience.value,
            "intensite": self.intensite,
            "stabilite": self.stabilite,
            "timestamp": self.timestamp.isoformat(),
            "effets_actifs": self.effets_actifs.copy()
        })
        
        # Limite la taille de l'historique
        if len(self.historique) > self.taille_max_historique:
            self.historique = self.historique[-self.taille_max_historique:]
        
        # Mettre à jour l'état
        ancien_type = self.type_etat
        self.type_etat = nouveau_type
        self.intensite = max(0.0, min(1.0, intensite))
        self.stabilite = max(0.0, min(1.0, stabilite))
        self.timestamp = datetime.now()
        
        # Mettre à jour la résistance à la transition
        if ancien_type != nouveau_type:
            # Augmenter la résistance pour revenir à l'ancien état
            self.resistance_transition[ancien_type] = min(1.0, self.resistance_transition.get(ancien_type, 0.0) + 0.2)
            # Réduire la résistance pour le nouvel état
            self.resistance_transition[nouveau_type] = max(0.0, self.resistance_transition.get(nouveau_type, 0.0) - 0.1)
        
        # Mettre à jour le niveau de conscience
        self._mettre_a_jour_conscience()
        
        # Appliquer les effets de transition
        self._appliquer_effets_transition(ancien_type, nouveau_type)
    
    def _mettre_a_jour_conscience(self):
        """Met à jour le niveau de conscience en fonction de l'état."""
        if self.intensite > 0.8 and self.stabilite > 0.7:
            self.niveau_conscience = NiveauConscience.SURCONSCIENT
        elif self.intensite > 0.6 and self.stabilite > 0.5:
            self.niveau_conscience = NiveauConscience.CONSCIENT
        elif self.intensite > 0.4 and self.stabilite > 0.3:
            self.niveau_conscience = NiveauConscience.SUBCONSCIENT
        else:
            self.niveau_conscience = NiveauConscience.INCONSCIENT
    
    def _appliquer_effets_transition(self, ancien_type: TypeEtat, nouveau_type: TypeEtat):
        """Applique les effets de transition entre deux états."""
        # Cette méthode sera implémentée par le GestionnaireEtats
        pass
    
    def est_stable(self) -> bool:
        """Vérifie si l'état est stable."""
        return self.stabilite >= 0.7
    
    def est_intense(self) -> bool:
        """Vérifie si l'état est intense."""
        return self.intensite >= 0.7
    
    def ajouter_effet(self, nom: str, effet: Dict[str, Any]):
        """Ajoute un effet à l'état."""
        self.effets_actifs[nom] = effet
    
    def retirer_effet(self, nom: str):
        """Retire un effet de l'état."""
        if nom in self.effets_actifs:
            del self.effets_actifs[nom]
    
    def mettre_a_jour_effets(self):
        """Met à jour les effets actifs."""
        effets_a_retirer = []
        for nom, effet in self.effets_actifs.items():
            if "duree" in effet and effet["duree"] > 0:
                effet["duree"] -= 1
                if effet["duree"] <= 0:
                    effets_a_retirer.append(nom)
        
        for nom in effets_a_retirer:
            self.retirer_effet(nom)

class GestionnaireEtats:
    """Gère les états internes des sphères."""
    
    def __init__(self):
        self.etats: Dict[str, EtatInterne] = {}
        self.gestionnaire_elements = GestionnaireElements()
        self.transitions: Dict[TypeEtat, Dict[TypeEtat, float]] = {
            TypeEtat.CALME: {
                TypeEtat.AGITE: 0.3,
                TypeEtat.CONCENTRE: 0.4,
                TypeEtat.DISTRAIT: 0.2
            },
            TypeEtat.AGITE: {
                TypeEtat.CALME: 0.4,
                TypeEtat.CONCENTRE: 0.3,
                TypeEtat.FATIGUE: 0.3
            },
            TypeEtat.CONCENTRE: {
                TypeEtat.CALME: 0.3,
                TypeEtat.DISTRAIT: 0.3,
                TypeEtat.ENERGIE: 0.4
            },
            TypeEtat.DISTRAIT: {
                TypeEtat.CONCENTRE: 0.4,
                TypeEtat.FATIGUE: 0.3,
                TypeEtat.CALME: 0.3
            },
            TypeEtat.FATIGUE: {
                TypeEtat.CALME: 0.5,
                TypeEtat.ENERGIE: 0.3,
                TypeEtat.AGITE: 0.2
            },
            TypeEtat.ENERGIE: {
                TypeEtat.CONCENTRE: 0.4,
                TypeEtat.CALME: 0.3,
                TypeEtat.AGITE: 0.3
            }
        }
        
        # Conditions pour les transitions
        self.conditions_transition: Dict[Tuple[TypeEtat, TypeEtat], List[ConditionTransition]] = {}
        
        # Effets des transitions
        self.effets_transition: Dict[Tuple[TypeEtat, TypeEtat], List[EffetTransition]] = {}
        
        # Initialiser les conditions et effets par défaut
        self._initialiser_conditions_et_effets()
        
        # Initialiser les états par défaut
        self._initialiser_etats_defaut()
    
    def _initialiser_conditions_et_effets(self):
        """Initialise les conditions et effets par défaut pour les transitions."""
        # Condition pour la transition CALME -> AGITE
        self.ajouter_condition_transition(
            TypeEtat.CALME, 
            TypeEtat.AGITE,
            ConditionTransition(
                nom="stress_eleve",
                description="Le niveau de stress est élevé",
                fonction=lambda signaux: signaux.get("niveau_serenite", 0.5) < 0.4,
                priorite=1
            )
        )
        
        # Effet pour la transition CALME -> AGITE
        self.ajouter_effet_transition(
            TypeEtat.CALME,
            TypeEtat.AGITE,
            EffetTransition(
                nom="augmentation_stress",
                description="Augmente temporairement le niveau de stress",
                fonction=lambda signaux: {"niveau_serenite": max(0.0, signaux.get("niveau_serenite", 0.5) - 0.1)},
                duree=3
            )
        )
        
        # Condition pour la transition AGITE -> CALME
        self.ajouter_condition_transition(
            TypeEtat.AGITE,
            TypeEtat.CALME,
            ConditionTransition(
                nom="serenite_retrouvee",
                description="La sérénité a été retrouvée",
                fonction=lambda signaux: signaux.get("niveau_serenite", 0.5) > 0.6,
                priorite=1
            )
        )
        
        # Effet pour la transition AGITE -> CALME
        self.ajouter_effet_transition(
            TypeEtat.AGITE,
            TypeEtat.CALME,
            EffetTransition(
                nom="apaisement",
                description="Apaisement progressif",
                fonction=lambda signaux: {"niveau_serenite": min(1.0, signaux.get("niveau_serenite", 0.5) + 0.05)},
                duree=5
            )
        )
    
    def ajouter_condition_transition(self, etat_depart: TypeEtat, etat_arrivee: TypeEtat, condition: ConditionTransition):
        """Ajoute une condition pour une transition d'état."""
        cle = (etat_depart, etat_arrivee)
        if cle not in self.conditions_transition:
            self.conditions_transition[cle] = []
        self.conditions_transition[cle].append(condition)
        # Trier les conditions par priorité
        self.conditions_transition[cle].sort(key=lambda c: c.priorite, reverse=True)
    
    def ajouter_effet_transition(self, etat_depart: TypeEtat, etat_arrivee: TypeEtat, effet: EffetTransition):
        """Ajoute un effet pour une transition d'état."""
        cle = (etat_depart, etat_arrivee)
        if cle not in self.effets_transition:
            self.effets_transition[cle] = []
        self.effets_transition[cle].append(effet)
    
    def obtenir_etat(self, source: str) -> Optional[EtatInterne]:
        """Obtient l'état interne d'une source."""
        return self.etats.get(source)
    
    def mettre_a_jour_etat(self, source: str, signaux: Dict):
        """Met à jour l'état interne d'une source."""
        if source not in self.etats:
            self.etats[source] = EtatInterne()
        
        etat = self.etats[source]
        ancien_type = etat.type_etat
        
        # Calculer l'influence des éléments sacrés
        influence_elements = self.gestionnaire_elements.calculer_influence_globale()
        
        # Fusionner les signaux avec l'influence des éléments
        signaux_complets = {**signaux, **influence_elements}
        
        # Déterminer le nouveau type d'état en fonction des conditions
        nouveau_type = self._determiner_type_etat(signaux_complets, ancien_type)
        
        # Calculer l'intensité et la stabilité
        intensite = self._calculer_intensite(signaux_complets)
        stabilite = self._calculer_stabilite(signaux_complets)
        
        # Mettre à jour l'état
        etat.mettre_a_jour(nouveau_type, intensite, stabilite)
        
        # Appliquer les effets de transition
        self._appliquer_effets_transition(source, ancien_type, nouveau_type, signaux_complets)
        
        # Mettre à jour les éléments sacrés
        self.gestionnaire_elements.mettre_a_jour_elements()
    
    def _determiner_type_etat(self, signaux: Dict, etat_actuel: TypeEtat) -> TypeEtat:
        """Détermine le type d'état en fonction des signaux et des conditions de transition."""
        # Vérifier les conditions de transition pour l'état actuel
        for etat_arrivee, proba in self.transitions.get(etat_actuel, {}).items():
            cle = (etat_actuel, etat_arrivee)
            if cle in self.conditions_transition:
                # Vérifier toutes les conditions pour cette transition
                conditions_remplies = True
                for condition in self.conditions_transition[cle]:
                    if not condition.fonction(signaux):
                        conditions_remplies = False
                        break
                
                if conditions_remplies:
                    # Vérifier la probabilité de transition
                    if np.random.random() < proba:
                        return etat_arrivee
        
        # Si aucune transition n'est déclenchée, déterminer l'état par défaut
        harmonie = signaux.get("harmonie", 0.5)
        serenite = signaux.get("niveau_serenite", 0.5)
        magie = signaux.get("niveau_magie", 0.5)
        
        # Vérifier la compatibilité avec les éléments sacrés actifs
        elements_actifs = [e for e in self.gestionnaire_elements.elements.values() if e.est_actif()]
        for element in elements_actifs:
            etats_compatibles = self.gestionnaire_elements.obtenir_etats_compatibles(element)
            if etats_compatibles:
                # Choisir l'état compatible le plus approprié en fonction des signaux
                for etat in etats_compatibles:
                    if self._est_etat_approprié(etat, harmonie, serenite, magie):
                        return etat
        
        # Si aucun état compatible n'est trouvé, utiliser la logique par défaut
        if harmonie > 0.8 and serenite > 0.7:
            return TypeEtat.HARMONIEUX
        elif harmonie < 0.3 and serenite < 0.4:
            return TypeEtat.DESEQUILIBRE
        elif magie > 0.7 and harmonie > 0.6:
            return TypeEtat.EVOLUTION
        elif magie < 0.3 and harmonie < 0.4:
            return TypeEtat.STAGNATION
        elif serenite > 0.7 and harmonie > 0.6:
            return TypeEtat.CALME
        elif serenite < 0.4 and harmonie < 0.5:
            return TypeEtat.AGITE
        elif magie > 0.7 and serenite > 0.6:
            return TypeEtat.CONCENTRE
        elif magie < 0.4 and serenite < 0.5:
            return TypeEtat.DISTRAIT
        elif harmonie < 0.4 and magie < 0.4:
            return TypeEtat.FATIGUE
        else:
            return TypeEtat.ENERGIE
    
    def _est_etat_approprié(self, etat: TypeEtat, harmonie: float, serenite: float, magie: float) -> bool:
        """Vérifie si un état est approprié en fonction des signaux."""
        if etat == TypeEtat.CALME:
            return serenite > 0.7 and harmonie > 0.6
        elif etat == TypeEtat.AGITE:
            return serenite < 0.4 and harmonie < 0.5
        elif etat == TypeEtat.CONCENTRE:
            return magie > 0.7 and serenite > 0.6
        elif etat == TypeEtat.DISTRAIT:
            return magie < 0.4 and serenite < 0.5
        elif etat == TypeEtat.FATIGUE:
            return harmonie < 0.4 and magie < 0.4
        elif etat == TypeEtat.ENERGIE:
            return magie > 0.6 and harmonie > 0.5
        elif etat == TypeEtat.HARMONIEUX:
            return harmonie > 0.8 and serenite > 0.7
        elif etat == TypeEtat.DESEQUILIBRE:
            return harmonie < 0.3 and serenite < 0.4
        elif etat == TypeEtat.EVOLUTION:
            return magie > 0.7 and harmonie > 0.6
        elif etat == TypeEtat.STAGNATION:
            return magie < 0.3 and harmonie < 0.4
        return False
    
    def _appliquer_effets_transition(self, source: str, etat_depart: TypeEtat, etat_arrivee: TypeEtat, signaux: Dict):
        """Applique les effets d'une transition d'état."""
        etat = self.etats[source]
        cle = (etat_depart, etat_arrivee)
        
        if cle in self.effets_transition:
            for effet in self.effets_transition[cle]:
                # Appliquer l'effet
                modifications = effet.fonction(signaux)
                
                # Ajouter l'effet à l'état
                etat.ajouter_effet(effet.nom, {
                    "description": effet.description,
                    "modifications": modifications,
                    "duree": effet.duree
                })
    
    def _calculer_intensite(self, signaux: Dict) -> float:
        """Calcule l'intensité de l'état."""
        harmonie = signaux.get("harmonie", 0.5)
        serenite = signaux.get("niveau_serenite", 0.5)
        magie = signaux.get("niveau_magie", 0.5)
        
        return (harmonie * 0.4 + serenite * 0.3 + magie * 0.3)
    
    def _calculer_stabilite(self, signaux: Dict) -> float:
        """Calcule la stabilité de l'état."""
        harmonie = signaux.get("harmonie", 0.5)
        serenite = signaux.get("niveau_serenite", 0.5)
        
        return (harmonie * 0.6 + serenite * 0.4)
    
    def obtenir_etat_global(self) -> Dict:
        """Retourne l'état global des états internes."""
        return {
            source: {
                "type": etat.type_etat.value,
                "niveau_conscience": etat.niveau_conscience.value,
                "intensite": etat.intensite,
                "stabilite": etat.stabilite,
                "timestamp": etat.timestamp.isoformat(),
                "historique": etat.historique[-10:],  # Derniers 10 états
                "effets_actifs": etat.effets_actifs,
                "resistance_transition": {k.value: v for k, v in etat.resistance_transition.items()}
            }
            for source, etat in self.etats.items()
        }
    
    def mettre_a_jour_effets(self):
        """Met à jour les effets actifs de tous les états."""
        for etat in self.etats.values():
            etat.mettre_a_jour_effets()
    
    def ajouter_element_sacre(self, nom: str, element: ElementSacre):
        """Ajoute un élément sacré au gestionnaire."""
        self.gestionnaire_elements.ajouter_element(nom, element)
    
    def _initialiser_etats_defaut(self):
        """Initialise les états par défaut."""
        # État principal - calme et conscient
        self.ajouter_etat(
            source="principal",
            type_etat=TypeEtat.CALME,
            intensite=0.7,
            stabilite=0.8,
            niveau_conscience=NiveauConscience.CONSCIENT
        )
        
        # État secondaire - concentré et surconscient
        self.ajouter_etat(
            source="secondaire",
            type_etat=TypeEtat.CONCENTRE,
            intensite=0.5,
            stabilite=0.9,
            niveau_conscience=NiveauConscience.SURCONSCIENT
        )
        
        # État de fond - harmonieux et subconscient
        self.ajouter_etat(
            source="fond",
            type_etat=TypeEtat.HARMONIEUX,
            intensite=0.3,
            stabilite=0.6,
            niveau_conscience=NiveauConscience.SUBCONSCIENT
        )
    
    def ajouter_etat(self, source: str, type_etat: TypeEtat, intensite: float = 0.5,
                   stabilite: float = 0.5, niveau_conscience: NiveauConscience = NiveauConscience.CONSCIENT):
        """Ajoute un nouvel état."""
        self.etats[source] = EtatInterne(
            type_etat=type_etat,
            intensite=intensite,
            stabilite=stabilite,
            niveau_conscience=niveau_conscience
        )
    
    def supprimer_etat(self, source: str):
        """Supprime un état."""
        if source in self.etats:
            del self.etats[source] 