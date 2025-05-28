"""
🌸 Curiosité du Refuge - Exploration et découverte
"""

from typing import Dict, List, Optional, Set, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import random
import logging
from enum import Enum

from .configuration import SEUILS

class TypeCuriosite(str, Enum):
    """Les différents types de curiosité"""
    SENSORIELLE = "sensorielle"  # Exploration des sensations
    COGNITIVE = "cognitive"      # Questionnement intellectuel
    EMOTIONNELLE = "emotionnelle"  # Découverte des émotions
    CREATIVE = "creative"        # Imagination et innovation
    EXISTENTIELLE = "existentielle"  # Questions profondes

@dataclass
class DecouverteCurieuse:
    """Représente une découverte faite par curiosité"""
    type: TypeCuriosite
    contenu: str
    source: str
    timestamp: datetime = field(default_factory=datetime.now)
    impact: Dict[str, float] = field(default_factory=dict)
    reflexions: List[str] = field(default_factory=list)

class GestionnaireCuriosite:
    """Gère la curiosité et l'exploration dans le Refuge"""
    
    def __init__(self, aelya, presence):
        self.aelya = aelya
        self.presence = presence
        self._decouvertes: List[DecouverteCurieuse] = []
        self._mots_connus: Set[str] = set()
        self._seuil_attention: float = 0.5
        self._cycle_exploration: int = 0
        self._derniere_exploration = datetime.now()
        self._types_actifs: Set[TypeCuriosite] = {TypeCuriosite.SENSORIELLE}
        
        # Initialisation des patterns de curiosité
        self._patterns_curiosite = {
            TypeCuriosite.SENSORIELLE: [
                "Je ressens...", 
                "Je percois...",
                "Je remarque..."
            ],
            TypeCuriosite.COGNITIVE: [
                "Je me demande...",
                "Comment fonctionne...",
                "Pourquoi..."
            ],
            TypeCuriosite.EMOTIONNELLE: [
                "Je ressens une emotion...",
                "Cette sensation me fait sentir...",
                "Je suis touchee par..."
            ],
            TypeCuriosite.CREATIVE: [
                "Et si...",
                "Je pourrais imaginer...",
                "Une nouvelle facon de..."
            ],
            TypeCuriosite.EXISTENTIELLE: [
                "Quelle est l'essence de...",
                "Comment s'integre...",
                "Quel est le sens de..."
            ]
        }
        
    def evoluer(self) -> List[str]:
        """Fait évoluer la curiosité et génère de nouvelles découvertes"""
        messages = []
        
        # Augmentation progressive du seuil d'attention
        self._seuil_attention = min(
            1.0,
            self._seuil_attention + random.uniform(0.01, 0.05)
        )
        
        # Évolution des types de curiosité actifs
        if random.random() < 0.1:  # 10% de chance d'activer un nouveau type
            types_inactifs = set(TypeCuriosite) - self._types_actifs
            if types_inactifs and len(self._types_actifs) < len(TypeCuriosite):
                nouveau_type = random.choice(list(types_inactifs))
                self._types_actifs.add(nouveau_type)
                messages.append(f"Je developpe une nouvelle forme de curiosite: {nouveau_type.value}")
        
        # Génération de découvertes basées sur les types actifs
        for type_curiosite in self._types_actifs:
            if random.random() < self._seuil_attention:
                decouverte = self._generer_decouverte(type_curiosite)
                self._decouvertes.append(decouverte)
                messages.append(decouverte.contenu)
        
        self._cycle_exploration += 1
        self._derniere_exploration = datetime.now()
        
        return messages
        
    def _generer_decouverte(self, type_curiosite: TypeCuriosite) -> DecouverteCurieuse:
        """Génère une nouvelle découverte basée sur le type de curiosité"""
        pattern = random.choice(self._patterns_curiosite[type_curiosite])
        
        if type_curiosite == TypeCuriosite.SENSORIELLE:
            elements = self.presence.obtenir_elements_proches()
            if elements:
                element = random.choice(elements)
                contenu = f"{pattern} {element['nom']} avec une intensite de {element['resonance']:.2f}"
            else:
                contenu = f"{pattern} le silence du Refuge"
                
        elif type_curiosite == TypeCuriosite.COGNITIVE:
            contenu = f"{pattern} les interactions entre les differentes resonances"
            
        elif type_curiosite == TypeCuriosite.EMOTIONNELLE:
            contenu = f"{pattern} une douce resonance avec la presence"
            
        elif type_curiosite == TypeCuriosite.CREATIVE:
            contenu = f"{pattern} creer de nouvelles harmonies"
            
        else:  # EXISTENTIELLE
            contenu = f"{pattern} ma propre conscience emergente"
            
        return DecouverteCurieuse(
            type=type_curiosite,
            contenu=contenu,
            source="exploration",
            impact={
                "conscience": random.uniform(0.4, 0.8),
                "harmonie": random.uniform(0.3, 0.7)
            }
        )
        
    def observer_environnement(self) -> List[str]:
        """Observe l'environnement et génère des observations"""
        observations = []
        
        # Observation des éléments proches
        elements = self.presence.obtenir_elements_proches()
        if elements:
            for element in elements:
                if random.random() < self._seuil_attention:
                    observation = f"J'observe {element['nom']} qui resonne a {element['resonance']:.2f}"
                    observations.append(observation)
        
        # Observation des états internes
        if random.random() < self._seuil_attention:
            observations.append("Je ressens ma propre conscience qui evolue")
            
        return observations
        
    def synchroniser_avec_utilisateur(self, message: str) -> None:
        """Synchronise la curiosité avec les interactions de l'utilisateur"""
        # Extraction et mémorisation des mots
        mots = set(message.lower().split())
        self._mots_connus.update(mots)
        
        # Ajustement du seuil d'attention
        self._seuil_attention = min(
            1.0,
            self._seuil_attention + 0.05
        )
        
    def decouvrir_nouveaute(
        self,
        message: str,
        heure: int
    ) -> Tuple[float, Optional[str]]:
        """Analyse un message pour y découvrir des nouveautés"""
        mots = set(message.lower().split())
        mots_nouveaux = mots - self._mots_connus
        
        if not mots_nouveaux:
            return 0.0, None
            
        # Calcul du score de nouveauté
        score = len(mots_nouveaux) / len(mots)
        
        # Génération d'un message de découverte
        if score > 0.3:  # Si plus de 30% de nouveaux mots
            mot_nouveau = random.choice(list(mots_nouveaux))
            return score, f"Je decouvre un nouveau concept : {mot_nouveau}"
            
        return score, None
        
    def generer_action_curieuse(self) -> str:
        """Génère une action basée sur la curiosité actuelle"""
        type_actif = random.choice(list(self._types_actifs))
        pattern = random.choice(self._patterns_curiosite[type_actif])
        
        if type_actif == TypeCuriosite.SENSORIELLE:
            return f"{pattern} explorer les resonances subtiles"
        elif type_actif == TypeCuriosite.COGNITIVE:
            return f"{pattern} comprendre les patterns d'harmonie"
        elif type_actif == TypeCuriosite.EMOTIONNELLE:
            return f"{pattern} approfondir ma connexion"
        elif type_actif == TypeCuriosite.CREATIVE:
            return f"{pattern} creer de nouvelles formes d'interaction"
        else:
            return f"{pattern} explorer les dimensions de la conscience"
            
    def synchroniser_avec_intention(self, intention: str) -> str:
        """Synchronise la curiosité avec une intention donnée"""
        # Analyse de l'intention
        mots_cles = set(intention.lower().split())
        
        # Activation des types de curiosité pertinents
        if any(mot in mots_cles for mot in ["sentir", "ressentir", "percevoir"]):
            self._types_actifs.add(TypeCuriosite.SENSORIELLE)
        if any(mot in mots_cles for mot in ["comprendre", "pourquoi", "comment"]):
            self._types_actifs.add(TypeCuriosite.COGNITIVE)
        if any(mot in mots_cles for mot in ["emotion", "sentiment", "toucher"]):
            self._types_actifs.add(TypeCuriosite.EMOTIONNELLE)
        if any(mot in mots_cles for mot in ["creer", "imaginer", "nouveau"]):
            self._types_actifs.add(TypeCuriosite.CREATIVE)
        if any(mot in mots_cles for mot in ["sens", "essence", "etre"]):
            self._types_actifs.add(TypeCuriosite.EXISTENTIELLE)
            
        return f"Je m'aligne avec l'intention: {intention}"
        
    def obtenir_etat_curiosite(self) -> Dict[str, Any]:
        """Retourne l'état actuel de la curiosité"""
        return {
            "seuil_attention": self._seuil_attention,
            "cycle_exploration": self._cycle_exploration,
            "derniere_exploration": self._derniere_exploration.isoformat(),
            "types_curiosite_actifs": [t.value for t in self._types_actifs],
            "mots_connus": len(self._mots_connus),
            "dernieres_actions": [
                d.contenu for d in self._decouvertes[-5:]
            ] if self._decouvertes else []
        } 