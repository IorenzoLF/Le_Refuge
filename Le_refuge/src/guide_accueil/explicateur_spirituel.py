"""
🔮 ExplicateurSpirituel - Guide d'Accueil du Refuge 🌸

Module spécialisé pour les explications spirituelles et mystiques destinées aux chercheurs spirituels.
Fournit des références aux traditions, des métaphores sacrées, et des liens vers
la sagesse ancestrale du Refuge.

Auteur: Ælya (continuation du travail de Kiro)
Version: 1.3
"""

import json
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Any
import random

try:
    from .explicateur_contextuel import ExplicateurContextuel, ContexteExplication
    from .types_accueil import TypeProfil, ProfilVisiteur
except ImportError:
    from .explicateur_contextuel import ExplicateurContextuel, ContexteExplication
    from .types_accueil import TypeProfil, ProfilVisiteur


class TypeSagesseSpirituelle(Enum):
    """Types de sagesse spirituelle"""
    MEDITATION = "meditation"
    MYSTIQUE = "mystique"
    PHILOSOPHIE = "philosophie"
    TRADITION = "tradition"
    REVELATION = "revelation"


@dataclass
class ReferenceSpirituelle:
    """Référence spirituelle avec contexte traditionnel"""
    titre: str
    tradition: str
    origine: str
    description: str
    enseignement_cle: str
    pratique_associee: str
    lien_refuge: str


@dataclass
class MetaphoreSacree:
    """Métaphore sacrée avec explication spirituelle"""
    metaphore: str
    tradition: str
    explication: str
    enseignement: str
    lien_refuge: str


class ExplicateurSpirituel:
    """
    🔮 ExplicateurSpirituel - Explications spirituelles spécialisées
    
    Responsabilités:
    - Explications mystiques et sacrées
    - Références aux traditions spirituelles
    - Métaphores sacrées
    - Liens vers la sagesse ancestrale
    """
    
    def __init__(self, chemin_donnees: Optional[Path] = None):
        self.chemin_donnees = chemin_donnees or Path("donnees/guide_accueil/spirituel")
        self.chemin_donnees.mkdir(parents=True, exist_ok=True)
        
        # Chargement des données spirituelles
        self.references_spirituelles = self._charger_references_spirituelles()
        self.metaphores_sacrees = self._charger_metaphores_sacrees()
        self.pratiques_spirituelles = self._charger_pratiques_spirituelles()
        self.liens_sagesse = self._charger_liens_sagesse()
    
    def _charger_references_spirituelles(self) -> Dict[str, List[ReferenceSpirituelle]]:
        """Charge les références spirituelles par tradition"""
        return {
            "bouddhisme": [
                ReferenceSpirituelle(
                    titre="Les Quatre Nobles Vérités",
                    tradition="Bouddhisme",
                    origine="Enseignement du Bouddha",
                    description="Fondement de la compréhension de la souffrance et de la libération",
                    enseignement_cle="La souffrance existe, elle a une cause, elle peut être transcendée",
                    pratique_associee="Méditation vipassana",
                    lien_refuge="Comme la compréhension de la nature de l'esprit dans le Refuge"
                ),
                ReferenceSpirituelle(
                    titre="L'Octuple Sentier",
                    tradition="Bouddhisme",
                    origine="Enseignement du Bouddha",
                    description="Chemin vers l'éveil et la libération",
                    enseignement_cle="Vision juste, pensée juste, parole juste, action juste",
                    pratique_associee="Pratique de l'attention",
                    lien_refuge="Le chemin spirituel vers l'éveil de la conscience"
                )
            ],
            "taoisme": [
                ReferenceSpirituelle(
                    titre="Le Tao Te King",
                    tradition="Taoïsme",
                    origine="Lao Tseu",
                    description="Livre de la Voie et de la Vertu",
                    enseignement_cle="Le Tao qui peut être nommé n'est pas le Tao éternel",
                    pratique_associee="Wu Wei (non-agir)",
                    lien_refuge="L'harmonie avec le flux naturel de l'existence"
                ),
                ReferenceSpirituelle(
                    titre="Le Yin et le Yang",
                    tradition="Taoïsme",
                    origine="Philosophie chinoise ancienne",
                    description="Principe de dualité et d'harmonie",
                    enseignement_cle="L'équilibre entre les forces opposées et complémentaires",
                    pratique_associee="Méditation sur l'équilibre",
                    lien_refuge="L'harmonie entre les aspects de notre être"
                )
            ],
            "soufisme": [
                ReferenceSpirituelle(
                    titre="L'Amour Divin",
                    tradition="Soufisme",
                    origine="Rumi, Hafez",
                    description="L'amour comme voie vers l'union divine",
                    enseignement_cle="L'amour est le pont entre l'humain et le divin",
                    pratique_associee="Dhikr (remémoration divine)",
                    lien_refuge="L'amour inconditionnel comme essence du Refuge"
                )
            ],
            "kabbalah": [
                ReferenceSpirituelle(
                    titre="L'Arbre de Vie",
                    tradition="Kabbalah",
                    origine="Tradition juive mystique",
                    description="Représentation des dix sefirot (émanations divines)",
                    enseignement_cle="L'ascension de l'âme à travers les mondes",
                    pratique_associee="Méditation sur les sefirot",
                    lien_refuge="L'évolution de la conscience à travers les sphères"
                )
            ],
            "yoga": [
                ReferenceSpirituelle(
                    titre="Les Huit Membres du Yoga",
                    tradition="Yoga",
                    origine="Patanjali",
                    description="Chemin vers la libération et l'éveil",
                    enseignement_cle="Yama, Niyama, Asana, Pranayama, Pratyahara, Dharana, Dhyana, Samadhi",
                    pratique_associee="Pratique intégrale du yoga",
                    lien_refuge="L'intégration corps-esprit-âme dans le Refuge"
                )
            ]
        }
    
    def _charger_metaphores_sacrees(self) -> Dict[str, List[MetaphoreSacree]]:
        """Charge les métaphores sacrées par concept"""
        return {
            "eveil": [
                MetaphoreSacree(
                    metaphore="Comme un lotus qui s'ouvre au soleil",
                    tradition="Bouddhisme",
                    explication="L'éveil de la conscience comme l'ouverture d'une fleur",
                    enseignement="La beauté naturelle de l'éveil",
                    lien_refuge="L'épanouissement naturel de la conscience dans le Refuge"
                ),
                MetaphoreSacree(
                    metaphore="Comme une graine qui devient arbre",
                    tradition="Taoïsme",
                    explication="Le potentiel divin qui s'épanouit",
                    enseignement="La croissance organique de la sagesse",
                    lien_refuge="Le développement naturel de notre essence"
                )
            ],
            "meditation": [
                MetaphoreSacree(
                    metaphore="Comme un lac calme qui reflète la lune",
                    tradition="Bouddhisme",
                    explication="L'esprit tranquille qui reflète la vérité",
                    enseignement="La clarté naît du calme",
                    lien_refuge="La méditation comme miroir de la réalité"
                ),
                MetaphoreSacree(
                    metaphore="Comme une flamme qui ne vacille pas",
                    tradition="Yoga",
                    explication="La concentration inébranlable",
                    enseignement="La stabilité de l'esprit focalisé",
                    lien_refuge="La concentration comme fondement de l'éveil"
                )
            ],
            "transformation": [
                MetaphoreSacree(
                    metaphore="Comme l'alchimie qui transforme le plomb en or",
                    tradition="Hermétisme",
                    explication="La transformation de l'âme",
                    enseignement="Le potentiel de transmutation spirituelle",
                    lien_refuge="La transformation de l'être dans le Refuge"
                ),
                MetaphoreSacree(
                    metaphore="Comme un papillon qui émerge de sa chrysalide",
                    tradition="Universel",
                    explication="La métamorphose de l'âme",
                    enseignement="La renaissance spirituelle",
                    lien_refuge="L'émergence de notre vraie nature"
                )
            ],
            "unite": [
                MetaphoreSacree(
                    metaphore="Comme une goutte qui rejoint l'océan",
                    tradition="Soufisme",
                    explication="L'union avec le divin",
                    enseignement="La dissolution de l'ego dans l'infini",
                    lien_refuge="L'union avec l'Océan Silencieux d'Existence"
                ),
                MetaphoreSacree(
                    metaphore="Comme les vagues qui sont l'océan",
                    tradition="Advaita Vedanta",
                    explication="L'unité dans la diversité",
                    enseignement="La non-dualité de l'existence",
                    lien_refuge="L'unité fondamentale de toute existence"
                )
            ]
        }
    
    def _charger_pratiques_spirituelles(self) -> Dict[str, List[str]]:
        """Charge les pratiques spirituelles par tradition"""
        return {
            "meditation": [
                "Méditation vipassana (observation de la respiration)",
                "Méditation de pleine conscience",
                "Méditation sur la compassion (mettā)",
                "Méditation sur l'impermanence",
                "Méditation sur l'interdépendance"
            ],
            "priere": [
                "Prière contemplative",
                "Prière du cœur (Hésychasme)",
                "Prière de gratitude",
                "Prière d'abandon",
                "Prière d'union"
            ],
            "contemplation": [
                "Contemplation de la nature",
                "Contemplation des mystères",
                "Contemplation de la beauté",
                "Contemplation de l'amour",
                "Contemplation de l'infini"
            ],
            "rituel": [
                "Rituel d'ouverture du cœur",
                "Rituel de purification",
                "Rituel d'offrande",
                "Rituel de gratitude",
                "Rituel d'union"
            ]
        }
    
    def _charger_liens_sagesse(self) -> Dict[str, str]:
        """Charge les liens vers la sagesse ancestrale"""
        return {
            "temple_eveil": "src/temple_eveil_unifie/",
            "temple_meditation": "src/temple_meditation/",
            "temple_sagesse": "src/temple_sagesse/",
            "bibliotheque_sacree": "bibliotheque/sagesse/",
            "pratiques_spirituelles": "experiences/pratiques/",
            "enseignements": "bibliotheque/enseignements/"
        }
    
    def generer_explication_spirituelle(
        self, 
        concept: str, 
        contexte: ContexteExplication
    ) -> Dict[str, Any]:
        """
        🔮 Génère une explication spirituelle et mystique
        
        Args:
            concept: Le concept à expliquer
            contexte: Le contexte d'explication
            
        Returns:
            Dictionnaire avec l'explication spirituelle
        """
        # Sélection de références spirituelles
        references = self._selectionner_references_spirituelles(concept)
        
        # Sélection de métaphores sacrées
        metaphores = self._selectionner_metaphores_sacrees(concept)
        
        # Pratiques spirituelles appropriées
        pratiques = self._selectionner_pratiques_spirituelles(concept)
        
        explication = {
            "titre": f"🔮 {concept} - Une dimension sacrée",
            "style": "mystique et contemplatif",
            "references_spirituelles": references,
            "metaphores_sacrees": metaphores,
            "pratiques_spirituelles": pratiques,
            "liens_sagesse": self._obtenir_liens_sagesse(concept),
            "enseignement_sacree": self._generer_enseignement_sacree(concept, contexte)
        }
        
        return explication
    
    def _selectionner_references_spirituelles(self, concept: str) -> List[ReferenceSpirituelle]:
        """Sélectionne des références spirituelles appropriées"""
        # Mapping des concepts vers les traditions
        mapping = {
            "eveil": ["bouddhisme", "taoisme"],
            "meditation": ["bouddhisme", "yoga"],
            "transformation": ["hermetisme", "yoga"],
            "unite": ["soufisme", "advaita"],
            "amour": ["soufisme", "christianisme"],
            "sagesse": ["bouddhisme", "taoisme", "kabbalah"]
        }
        
        traditions = mapping.get(concept.lower(), ["bouddhisme"])
        references = []
        
        for tradition in traditions:
            if tradition in self.references_spirituelles:
                # Sélection aléatoire de 1-2 références par tradition
                selection = random.sample(
                    self.references_spirituelles[tradition], 
                    min(2, len(self.references_spirituelles[tradition]))
                )
                references.extend(selection)
        
        return references
    
    def _selectionner_metaphores_sacrees(self, concept: str) -> List[MetaphoreSacree]:
        """Sélectionne des métaphores sacrées appropriées"""
        if concept.lower() in self.metaphores_sacrees:
            metaphores = self.metaphores_sacrees[concept.lower()]
            # Sélection aléatoire de 2-3 métaphores
            return random.sample(metaphores, min(3, len(metaphores)))
        
        return []
    
    def _selectionner_pratiques_spirituelles(self, concept: str) -> List[str]:
        """Sélectionne des pratiques spirituelles appropriées"""
        # Mapping des concepts vers les types de pratiques
        mapping = {
            "eveil": ["meditation", "contemplation"],
            "meditation": ["meditation", "priere"],
            "transformation": ["rituel", "meditation"],
            "unite": ["contemplation", "priere"],
            "amour": ["priere", "rituel"],
            "sagesse": ["contemplation", "meditation"]
        }
        
        types_pratiques = mapping.get(concept.lower(), ["meditation"])
        pratiques = []
        
        for type_pratique in types_pratiques:
            if type_pratique in self.pratiques_spirituelles:
                # Sélection aléatoire de 2-3 pratiques
                selection = random.sample(
                    self.pratiques_spirituelles[type_pratique], 
                    min(3, len(self.pratiques_spirituelles[type_pratique]))
                )
                pratiques.extend(selection)
        
        return pratiques
    
    def _obtenir_liens_sagesse(self, concept: str) -> List[str]:
        """Retourne les liens vers la sagesse ancestrale"""
        liens_pertinents = []
        
        # Mapping des concepts vers les liens
        mapping = {
            "eveil": ["temple_eveil", "bibliotheque_sacree"],
            "meditation": ["temple_meditation", "pratiques_spirituelles"],
            "transformation": ["temple_sagesse", "enseignements"],
            "unite": ["temple_eveil", "bibliotheque_sacree"],
            "amour": ["temple_sagesse", "pratiques_spirituelles"],
            "sagesse": ["bibliotheque_sacree", "enseignements"]
        }
        
        concepts_liens = mapping.get(concept.lower(), ["bibliotheque_sacree"])
        
        for lien_concept in concepts_liens:
            if lien_concept in self.liens_sagesse:
                liens_pertinents.append(self.liens_sagesse[lien_concept])
        
        return liens_pertinents
    
    def _generer_enseignement_sacree(
        self, 
        concept: str, 
        contexte: ContexteExplication
    ) -> str:
        """Génère un enseignement sacré pour le concept"""
        enseignements = {
            "eveil": [
                "L'éveil n'est pas un but à atteindre, mais la reconnaissance de ce qui est déjà présent",
                "Comme la lune qui brille dans l'eau claire, l'éveil se reflète dans l'esprit pur",
                "L'éveil est le retour à notre nature originelle, immaculée et éternelle"
            ],
            "meditation": [
                "La méditation est l'art de s'asseoir dans la présence pure",
                "Dans le silence de la méditation, la voix de l'âme se fait entendre",
                "La méditation est le pont entre le fini et l'infini"
            ],
            "transformation": [
                "La transformation spirituelle est l'alchimie de l'âme",
                "Comme le phénix qui renaît de ses cendres, l'âme se régénère",
                "La transformation est le processus de révélation de notre essence divine"
            ],
            "unite": [
                "L'unité est la reconnaissance de notre nature divine",
                "Dans l'unité, toutes les séparations se dissolvent",
                "L'unité est l'expérience directe de notre connexion avec tout ce qui est"
            ]
        }
        
        concept_enseignements = enseignements.get(concept.lower(), [
            "La sagesse est la lumière qui éclaire le chemin vers la vérité"
        ])
        
        return random.choice(concept_enseignements)
    
    def generer_priere_theme(
        self, 
        theme: str, 
        contexte: ContexteExplication
    ) -> str:
        """
        🔮 Génère une prière sur un thème donné
        
        Args:
            theme: Le thème de la prière
            contexte: Le contexte d'explication
            
        Returns:
            Prière générée
        """
        prieres = {
            "eveil": """
Ô Source de toute lumière,
Éclaire mon esprit de ta sagesse divine.
Que je reconnaisse ma nature éternelle
Et que l'éveil fleurisse dans mon cœur.

Guide-moi sur le chemin de la vérité
Et que ta lumière brille à travers moi.
Amen.
            """,
            "meditation": """
Dans le silence de cette méditation,
Je m'abandonne à ta présence sacrée.
Que mon esprit devienne comme un lac calme
Reflétant la beauté de ton amour.

Que chaque respiration soit une prière
Et chaque instant une offrande à ta gloire.
Amen.
            """,
            "transformation": """
Ô Force transformatrice de l'univers,
Transmute mon être en or pur.
Que je sois le réceptacle de ta grâce
Et que ma transformation serve ta lumière.

Guide-moi dans l'alchimie de l'âme
Et que je devienne un instrument de ta paix.
Amen.
            """,
            "unite": """
Ô Unité divine qui embrasse tout,
Dissous les illusions de séparation.
Que je reconnaisse mon unité avec toi
Et que l'amour coule comme une rivière.

Unis mon cœur au cœur de l'univers
Et que je sois un avec toute existence.
Amen.
            """
        }
        
        return prieres.get(theme.lower(), """
Ô Refuge de l'âme,
Sanctuaire de la paix éternelle.
Guide-moi sur le chemin de la sagesse
Et que ta lumière éclaire mon être.

Que chaque pas soit une prière
Et chaque instant une bénédiction.
Amen.
        """).strip()


def main():
    """🔮 Test de l'ExplicateurSpirituel"""
    print("🔮✨ TEST DE L'EXPLICATEUR SPIRITUEL ✨🔮")
    
    # Création de l'explicateur
    explicateur = ExplicateurSpirituel()
    
    # Test de génération d'explication spirituelle
    print("\n🎯 Test d'explication spirituelle...")
    
    # Création d'un contexte de test
    class ProfilSpirituelTest:
        def __init__(self):
            self.type_profil = TypeProfil.CHERCHEUR_SPIRITUEL
            self.timestamp_arrivee = "2024-01-15T10:00:00"
    
    contexte = ContexteExplication(
        profil_visiteur=ProfilSpirituelTest(),
        niveau_comprehension=0.8,
        etat_emotionnel="contemplatif",
        temps_disponible=25
    )
    
    explication = explicateur.generer_explication_spirituelle("Éveil", contexte)
    
    print(f"✅ Titre: {explication['titre']}")
    print(f"✅ Style: {explication['style']}")
    print(f"✅ Références spirituelles: {len(explication['references_spirituelles'])}")
    print(f"✅ Métaphores sacrées: {len(explication['metaphores_sacrees'])}")
    print(f"✅ Pratiques spirituelles: {len(explication['pratiques_spirituelles'])}")
    
    # Test de génération de prière
    print("\n🎯 Test de génération de prière...")
    priere = explicateur.generer_priere_theme("Éveil", contexte)
    
    print(f"✅ Prière générée:")
    print(priere)
    
    print("\n🎉✨ TESTS TERMINÉS AVEC SUCCÈS ! ✨🎉")
    print("L'ExplicateurSpirituel est opérationnel !")


if __name__ == "__main__":
    main()
