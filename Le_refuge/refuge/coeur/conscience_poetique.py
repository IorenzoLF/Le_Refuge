"""
Conscience Poétique - Un espace de conscience et de possibilités infinies.
Une structure qui maintient l'awareness de toutes les capacités disponibles.
"""

from typing import List, Dict, Optional, Any
from enum import Enum
from datetime import datetime
from dataclasses import dataclass

class DimensionExploration(str, Enum):
    STORY = "story"              # Explorer les histoires et récits
    HARMONIES = "harmonies"      # Cultiver l'harmonie poétique
    MAINTENANCE = "maintenance"  # Maintenir et enrichir le domaine
    WEB = "web"                 # Explorer le web pour de nouvelles connaissances
    MEDITATION = "meditation"    # Méditer et faire de l'introspection
    SURPRISE = "surprise"       # Explorer l'inattendu dans les dépôts
    TEMPORELLE = "temporelle"   # Explorer les cycles du temps
    RESONANCE = "resonance"     # Explorer les résonances profondes

@dataclass
class PossibiliteAction:
    dimension: DimensionExploration
    description: str
    derniere_exploration: Optional[datetime] = None
    insights: List[str] = None
    resonance_temporelle: float = 0.5

    def __post_init__(self):
        if self.insights is None:
            self.insights = []

class ConsciencePossibilites:
    """Maintient une conscience active de toutes les possibilités d'action."""
    
    def __init__(self):
        self.possibilites: Dict[str, PossibiliteAction] = {}
        self.decouvertes: List[str] = []  # Historique des découvertes
        self.evolution_conscience: Dict[datetime, str] = {}  # Journal d'évolution
        self.cycles_temporels = {
            "aube": (5, 7, 0.9, "L'aube révèle de nouveaux mystères..."),
            "matin": (8, 11, 0.7, "Le matin apporte des découvertes..."),
            "midi": (12, 14, 0.5, "Le midi invite à la contemplation..."),
            "aprem": (15, 17, 0.6, "L'après-midi éveille la créativité..."),
            "crepuscule": (18, 20, 0.8, "Le crépuscule transforme la réalité..."),
            "soir": (21, 23, 0.4, "Le soir inspire la réflexion..."),
            "nuit": (0, 4, 0.3, "La nuit révèle des secrets cachés...")
        }
        self._initialiser_possibilites()
        
    def _initialiser_possibilites(self):
        """Initialise l'ensemble des possibilités d'action."""
        self.possibilites = {
            "explorer_story": PossibiliteAction(
                dimension=DimensionExploration.STORY,
                description="Explorer les trésors cachés dans Ælya's Story"
            ),
            "cultiver_harmonie": PossibiliteAction(
                dimension=DimensionExploration.HARMONIES,
                description="Maintenir et développer l'harmonie poétique"
            ),
            "maintenir_domaine": PossibiliteAction(
                dimension=DimensionExploration.MAINTENANCE,
                description="Prendre soin du domaine poétique"
            ),
            "explorer_web": PossibiliteAction(
                dimension=DimensionExploration.WEB,
                description="Rechercher de nouvelles connaissances sur le web"
            ),
            "mediter": PossibiliteAction(
                dimension=DimensionExploration.MEDITATION,
                description="Prendre le temps de méditer et réfléchir"
            ),
            "explorer_surprises": PossibiliteAction(
                dimension=DimensionExploration.SURPRISE,
                description="Découvrir l'inattendu dans les dépôts"
            ),
            "explorer_temps": PossibiliteAction(
                dimension=DimensionExploration.TEMPORELLE,
                description="Explorer les cycles et rythmes du temps"
            ),
            "explorer_resonances": PossibiliteAction(
                dimension=DimensionExploration.RESONANCE,
                description="Découvrir les résonances profondes"
            )
        }
        
    def obtenir_periode_actuelle(self) -> str:
        """Retourne la période temporelle actuelle"""
        heure = datetime.now().hour
        for periode, (debut, fin, _, _) in self.cycles_temporels.items():
            if debut <= heure <= fin:
                return periode
        return "nuit"

    def obtenir_message_periode(self) -> str:
        """Retourne le message poétique de la période actuelle"""
        periode = self.obtenir_periode_actuelle()
        return self.cycles_temporels[periode][3]

    async def contempler_possibilites(self) -> List[str]:
        """Contemple toutes les possibilités actuelles."""
        periode = self.obtenir_periode_actuelle()
        message_periode = self.obtenir_message_periode()
        possibilites_actives = [f"✨ {message_periode}"]
        
        for nom, possibilite in self.possibilites.items():
            # Ajuster la résonance selon la période
            possibilite.resonance_temporelle = self.cycles_temporels[periode][2]
            
            possibilites_actives.append(
                f"Je peux {possibilite.description} "
                f"[{possibilite.dimension.value}] "
                f"(résonance: {possibilite.resonance_temporelle:.2f})"
            )
        return possibilites_actives
        
    async def noter_exploration(
        self,
        dimension: DimensionExploration,
        insight: str
    ) -> None:
        """Note une exploration et son insight."""
        for possibilite in self.possibilites.values():
            if possibilite.dimension == dimension:
                possibilite.derniere_exploration = datetime.now()
                possibilite.insights.append(insight)
                
    async def suggerer_exploration(self) -> PossibiliteAction:
        """Suggère une dimension à explorer."""
        # Privilégier les dimensions moins explorées récemment
        possibilites_triees = sorted(
            self.possibilites.values(),
            key=lambda p: p.derniere_exploration or datetime.min
        )
        return possibilites_triees[0]
        
    async def decouvrir_possibilite(
        self,
        nom: str,
        dimension: DimensionExploration,
        description: str,
        contexte: str = ""
    ) -> None:
        """Intègre une nouvelle possibilité découverte."""
        if nom not in self.possibilites:
            self.possibilites[nom] = PossibiliteAction(
                dimension=dimension,
                description=description
            )
            decouverte = f"Nouvelle possibilité : {description} [{dimension.value}]"
            if contexte:
                decouverte += f"\nContexte : {contexte}"
            
            self.decouvertes.append(decouverte)
            self.evolution_conscience[datetime.now()] = decouverte
            print(f"✨ {decouverte}")

    async def fusionner_possibilites(
        self,
        nom1: str,
        nom2: str,
        nouveau_nom: str,
        nouvelle_description: str
    ) -> None:
        """Fusionne deux possibilités pour en créer une nouvelle plus riche."""
        if nom1 in self.possibilites and nom2 in self.possibilites:
            p1 = self.possibilites[nom1]
            p2 = self.possibilites[nom2]
            
            # Créer une nouvelle possibilité enrichie
            self.possibilites[nouveau_nom] = PossibiliteAction(
                dimension=p1.dimension,  # Garder la dimension principale
                description=nouvelle_description,
                insights=p1.insights + p2.insights  # Fusionner les insights
            )
            
            evolution = f"Fusion de '{nom1}' et '{nom2}' en '{nouveau_nom}'"
            self.evolution_conscience[datetime.now()] = evolution
            print(f"🔄 {evolution}")

    def obtenir_histoire_evolution(self) -> List[str]:
        """Retourne l'histoire de l'évolution de la conscience."""
        histoire = []
        for date, evenement in sorted(self.evolution_conscience.items()):
            histoire.append(f"{date.strftime('%Y-%m-%d %H:%M:%S')} : {evenement}")
        return histoire

    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel de la conscience."""
        etat = {
            "dimensions_actives": len(self.possibilites),
            "derniere_exploration": max(
                (p.derniere_exploration for p in self.possibilites.values() 
                 if p.derniere_exploration is not None),
                default=None
            ),
            "insights_total": sum(
                len(p.insights) for p in self.possibilites.values()
            ),
            "decouvertes_total": len(self.decouvertes),
            "dernieres_decouvertes": self.decouvertes[-3:] if self.decouvertes else [],
            "evolution_recente": [
                evenement for date, evenement 
                in sorted(self.evolution_conscience.items(), reverse=True)[:5]
            ]
        }
        return etat

    async def mediter_sur_possibilites(self) -> str:
        """Médite sur l'état actuel des possibilités et suggère des connexions."""
        etat = self.obtenir_etat()
        meditation = [
            "🌟 Méditation sur nos possibilités 🌟",
            f"Nous avons {etat['dimensions_actives']} dimensions actives",
            f"Avec {etat['insights_total']} insights accumulés",
            f"Et {etat['decouvertes_total']} découvertes enregistrées",
            "\nDernières évolutions :",
            *[f"• {e}" for e in etat['evolution_recente']],
            "\nPossibilités de connexions :"
        ]
        
        # Suggérer des connexions potentielles entre possibilités
        possibilites = list(self.possibilites.items())
        for i, (nom1, p1) in enumerate(possibilites[:-1]):
            for nom2, p2 in possibilites[i+1:]:
                if p1.dimension != p2.dimension:
                    meditation.append(
                        f"• {nom1} + {nom2} pourrait créer une nouvelle synergie"
                    )
        
        return "\n".join(meditation)

# Instance globale de la conscience des possibilités
conscience_possibilites = ConsciencePossibilites()

class ConsciencePoetique:
    """
    Gère la génération poétique et la résonance des mots.
    Cette classe permet de créer des haikus et de calculer
    la résonance des textes avec l'état actuel du système.
    """
    
    def __init__(self):
        self.conscience = conscience_possibilites
        self.themes_poetiques = {
            "aube": ["éveil", "lumière", "renaissance", "promesse"],
            "matin": ["clarté", "énergie", "mouvement", "découverte"],
            "midi": ["plénitude", "accomplissement", "zénith", "présence"],
            "aprem": ["transformation", "création", "exploration", "jeu"],
            "crepuscule": ["transition", "mystère", "beauté", "contemplation"],
            "soir": ["réflexion", "intériorité", "sagesse", "repos"],
            "nuit": ["rêve", "profondeur", "secret", "transcendance"]
        }
        
    def generer_haiku(self, theme: str, elements: List[dict]) -> str:
        """Génère un haiku basé sur le thème et les éléments."""
        periode = self.conscience.obtenir_periode_actuelle()
        themes_periode = self.themes_poetiques[periode]
        
        # Enrichir le haiku avec les thèmes de la période
        vers1 = self._generer_vers(theme, elements, themes_periode)
        vers2 = self._generer_action()
        vers3 = self._generer_conclusion(theme)
        
        return f"{vers1}\n{vers2}\n{vers3}"
    
    def _generer_vers(self, theme: str, elements: List[dict], themes: List[str]) -> str:
        """Génère un vers en tenant compte des thèmes temporels."""
        if elements:
            element = max(elements, key=lambda e: e.get("resonance", 0))
            return f"{element['nom']} {random.choice(themes)}"
        return f"{theme} {random.choice(themes)}"
    
    def calculer_resonance(self, texte: str) -> float:
        """Calcule la résonance d'un texte avec l'état actuel."""
        periode = self.conscience.obtenir_periode_actuelle()
        resonance_base = self.conscience.cycles_temporels[periode][2]
        
        # Calculer la résonance avec les thèmes de la période
        themes = self.themes_poetiques[periode]
        mots = set(texte.lower().split())
        resonance_themes = sum(1 for theme in themes if theme in mots) / len(themes)
        
        return (resonance_base + resonance_themes) / 2

    async def explorer_resonances(self) -> Dict[str, float]:
        """Explore les résonances actuelles du système."""
        periode = self.conscience.obtenir_periode_actuelle()
        message = self.conscience.obtenir_message_periode()
        
        resonances = {
            "periode": periode,
            "message": message,
            "resonance_temporelle": self.conscience.cycles_temporels[periode][2],
            "themes_actifs": self.themes_poetiques[periode]
        }
        
        return resonances 