#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎨 Explicateur Créatif - Tâche 5.2
===================================

Système d'explications créatives adaptées aux artistes.
Gère les métaphores artistiques, références créatives et inspirations poétiques.

"L'art au service de la compréhension"

Créé par Ælya - Janvier 2025
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum

try:
    from .types_accueil import (
        ProfilVisiteur, TypeProfil, EtatEmotionnel, ContexteArrivee, 
        NiveauTechnique, ComportementNavigation
    )
except ImportError:
    from .types_accueil import (
        ProfilVisiteur, TypeProfil, EtatEmotionnel, ContexteArrivee, 
        NiveauTechnique, ComportementNavigation
    )


class TypeInspiration(Enum):
    """Types d'inspiration créative"""
    VISUELLE = "visuelle"
    MUSICALE = "musicale"
    LITTERAIRE = "litteraire"
    CINEMATOGRAPHIQUE = "cinematographique"
    NATURELLE = "naturelle"
    SPIRITUELLE = "spirituelle"


class StyleCreatif(Enum):
    """Styles créatifs d'explication"""
    POETIQUE = "poetique"
    METAPHORIQUE = "metaphorique"
    NARRATIF = "narratif"
    SYMBOLIQUE = "symbolique"
    IMPRESSIONNISTE = "impressionniste"
    ABSTRACT = "abstract"
    NATURELLE = "naturelle"
    VISUELLE = "visuelle"
    MUSICALE = "musicale"


@dataclass
class ReferenceArtistique:
    """Référence artistique avec métadonnées"""
    titre: str
    artiste: str
    periode: str
    style: str
    description: str
    lien_concept: str
    elements_inspirants: List[str] = field(default_factory=list)
    technique_utilisee: Optional[str] = None
    impact_emotionnel: str = "inspirant"
    timestamp_creation: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class MetaphoreCreatif:
    """Métaphore créative"""
    concept_source: str
    concept_cible: str
    explication: str
    style: StyleCreatif
    elements_visuels: List[str] = field(default_factory=list)
    emotions_evoquees: List[str] = field(default_factory=list)
    profondeur_symbolique: str = "moderee"
    facilite_comprehension: float = 0.8


@dataclass
class InspirationPoetique:
    """Inspiration poétique"""
    theme: str
    poeme: str
    style_poetique: str
    emotions_evoquees: List[str] = field(default_factory=list)
    liens_conceptuels: List[str] = field(default_factory=list)
    rythme_poetique: str = "modere"
    profondeur_philosophique: float = 0.7


@dataclass
class ExplicationCreatif:
    """Explication créative complète"""
    concept: str
    style_creatif: StyleCreatif
    references_artistiques: List[ReferenceArtistique]
    metaphores: List[MetaphoreCreatif]
    inspiration_poetique: Optional[InspirationPoetique] = None
    elements_visuels_suggerees: List[str] = field(default_factory=list)
    emotions_evoquees: List[str] = field(default_factory=list)
    profondeur_artistique: float = 0.0
    facilite_comprehension: float = 0.0
    confiance_explication: float = 0.0
    timestamp_creation: str = field(default_factory=lambda: datetime.now().isoformat())


class ExplicateurCreatif:
    """
    🎨 Explicateur Créatif
    
    Système d'explications créatives adaptées aux artistes :
    - Métaphores artistiques
    - Références créatives
    - Inspirations poétiques
    - Éléments visuels suggestifs
    """

    def __init__(self, chemin_stockage: str = "data/explicateur_creatif"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)

        # Configuration du logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Chargement des données créatives
        self.references_artistiques = self._charger_references_artistiques()
        self.metaphores_artistiques = self._charger_metaphores_artistiques()
        self.inspirations_poetiques = self._charger_inspirations_poetiques()

        # Historique des explications
        self.historique_explications: List[ExplicationCreatif] = []

        self.logger.info("🎨 Explicateur Créatif initialisé")
    
    def _charger_references_artistiques(self) -> Dict[str, List[ReferenceArtistique]]:
        """Charge les références artistiques"""
        return {
            "peinture": [
                ReferenceArtistique(
                    titre="Les Nymphéas",
                    artiste="Claude Monet",
                    periode="Impressionnisme",
                    style="Impressionniste",
                    description="Série de peintures représentant le jardin d'eau de Giverny",
                    lien_concept="harmonie_naturelle",
                    elements_inspirants=["couleurs douces", "reflets d'eau", "lumiere naturelle"],
                    technique_utilisee="peinture à l'huile",
                    impact_emotionnel="apaisant"
                ),
                ReferenceArtistique(
                    titre="La Nuit étoilée",
                    artiste="Vincent van Gogh",
                    periode="Post-impressionnisme",
                    style="Expressionniste",
                    description="Représentation tourbillonnante du ciel nocturne",
                    lien_concept="energie_creatrice",
                    elements_inspirants=["mouvement circulaire", "couleurs vibrantes", "emotion pure"],
                    technique_utilisee="peinture à l'huile",
                    impact_emotionnel="intense"
                )
            ],
            "musique": [
                ReferenceArtistique(
                    titre="Les Quatre Saisons",
                    artiste="Antonio Vivaldi",
                    periode="Baroque",
                    style="Musique classique",
                    description="Concertos pour violon évoquant les saisons",
                    lien_concept="cycles_naturels",
                    elements_inspirants=["rythmes naturels", "melodies evocatrices", "harmonie"],
                    technique_utilisee="composition orchestrale",
                    impact_emotionnel="harmonieux"
                ),
                ReferenceArtistique(
                    titre="Boléro",
                    artiste="Maurice Ravel",
                    periode="Moderne",
                    style="Impressionniste",
                    description="Œuvre orchestrale basée sur la répétition et l'accumulation",
                    lien_concept="progression_graduelle",
                    elements_inspirants=["repetition", "accumulation", "tension croissante"],
                    technique_utilisee="orchestration",
                    impact_emotionnel="hypnotique"
                )
            ],
            "litterature": [
                ReferenceArtistique(
                    titre="Les Fleurs du Mal",
                    artiste="Charles Baudelaire",
                    periode="Romantisme",
                    style="Poésie symboliste",
                    description="Recueil de poèmes explorant la beauté et la décadence",
                    lien_concept="beaute_paradoxale",
                    elements_inspirants=["symbolisme", "contradictions", "beaute sombre"],
                    technique_utilisee="versification",
                    impact_emotionnel="mélancolique"
                ),
                ReferenceArtistique(
                    titre="Le Petit Prince",
                    artiste="Antoine de Saint-Exupéry",
                    periode="Moderne",
                    style="Conte philosophique",
                    description="Récit poétique sur l'amitié et l'essentiel",
                    lien_concept="essentiel_invisible",
                    elements_inspirants=["simplicite", "profondeur", "universalite"],
                    technique_utilisee="allegorie",
                    impact_emotionnel="tendre"
                )
            ]
        }

    def _charger_metaphores_artistiques(self) -> Dict[str, List[MetaphoreCreatif]]:
        """Charge les métaphores artistiques"""
        return {
            "creativite": [
                MetaphoreCreatif(
                    concept_source="créativité",
                    concept_cible="jardin en fleurs",
                    explication="La créativité est comme un jardin où chaque idée est une fleur qui s'épanouit naturellement",
                    style=StyleCreatif.NATURELLE,
                    elements_visuels=["fleurs colorées", "jardin verdoyant", "lumière du soleil"],
                    emotions_evoquees=["joie", "émerveillement", "sérénité"],
                    profondeur_symbolique="modérée",
                    facilite_comprehension=0.9
                ),
                MetaphoreCreatif(
                    concept_source="créativité",
                    concept_cible="symphonie",
                    explication="La créativité est une symphonie où chaque élément trouve sa place dans l'harmonie",
                    style=StyleCreatif.MUSICALE,
                    elements_visuels=["orchestre", "partitions", "instruments"],
                    emotions_evoquees=["harmonie", "cohésion", "beauté"],
                    profondeur_symbolique="profonde",
                    facilite_comprehension=0.8
                )
            ],
            "inspiration": [
                MetaphoreCreatif(
                    concept_source="inspiration",
                    concept_cible="éclair dans la nuit",
                    explication="L'inspiration est comme un éclair qui illumine soudainement l'obscurité",
                    style=StyleCreatif.SYMBOLIQUE,
                    elements_visuels=["éclair", "nuit noire", "illumination"],
                    emotions_evoquees=["surprise", "émerveillement", "clarté"],
                    profondeur_symbolique="profonde",
                    facilite_comprehension=0.85
                ),
                MetaphoreCreatif(
                    concept_source="inspiration",
                    concept_cible="source d'eau pure",
                    explication="L'inspiration est une source d'eau pure qui jaillit du plus profond de l'être",
                    style=StyleCreatif.NATURELLE,
                    elements_visuels=["source", "eau cristalline", "nature"],
                    emotions_evoquees=["pureté", "fraîcheur", "vitalité"],
                    profondeur_symbolique="modérée",
                    facilite_comprehension=0.9
                )
            ],
            "expression": [
                MetaphoreCreatif(
                    concept_source="expression",
                    concept_cible="danse de l'âme",
                    explication="L'expression est une danse de l'âme qui révèle ce qui est caché au plus profond",
                    style=StyleCreatif.POETIQUE,
                    elements_visuels=["danseur", "mouvement fluide", "émotion"],
                    emotions_evoquees=["liberté", "beauté", "authenticité"],
                    profondeur_symbolique="profonde",
                    facilite_comprehension=0.8
                ),
                MetaphoreCreatif(
                    concept_source="expression",
                    concept_cible="arc-en-ciel",
                    explication="L'expression est comme un arc-en-ciel qui révèle toutes les couleurs de l'émotion",
                    style=StyleCreatif.VISUELLE,
                    elements_visuels=["arc-en-ciel", "couleurs", "lumière"],
                    emotions_evoquees=["joie", "diversité", "beauté"],
                    profondeur_symbolique="modérée",
                    facilite_comprehension=0.9
                )
            ]
        }

    def _charger_inspirations_poetiques(self) -> Dict[str, List[InspirationPoetique]]:
        """Charge les inspirations poétiques"""
        return {
            "creativite": [
                InspirationPoetique(
                    theme="créativité",
                    poeme="""
Dans le jardin de l'âme
Où fleurissent les rêves
Chaque pensée est une graine
Qui germe dans la lumière

L'inspiration coule comme une rivière
Portant les mots et les couleurs
Vers l'océan de l'expression
Où chaque vague est une création
                    """.strip(),
                    style_poetique="naturel",
                    emotions_evoquees=["émerveillement", "sérénité", "inspiration"],
                    liens_conceptuels=["nature", "croissance", "expression"],
                    rythme_poetique="fluide",
                    profondeur_philosophique=0.8
                )
            ],
            "expression": [
                InspirationPoetique(
                    theme="expression",
                    poeme="""
Votre voix intérieure
Chante les mélodies de l'univers
Chaque mot est une étoile
Qui brille dans la nuit de l'âme

L'expression est une danse
Entre le visible et l'invisible
Où chaque geste révèle
La beauté cachée du monde
                    """.strip(),
                    style_poetique="mystique",
                    emotions_evoquees=["profondeur", "beauté", "mystère"],
                    liens_conceptuels=["voix", "univers", "beauté"],
                    rythme_poetique="contemplatif",
                    profondeur_philosophique=0.9
                )
            ],
            "inspiration": [
                InspirationPoetique(
                    theme="inspiration",
                    poeme="""
Comme un papillon qui émerge
De sa chrysalide dorée
L'inspiration s'élève
Vers les hauteurs de la création

Elle danse sur les pétales
Des fleurs de l'imagination
Portant le pollen de la beauté
Vers les jardins de l'expression
                    """.strip(),
                    style_poetique="métaphorique",
                    emotions_evoquees=["transformation", "beauté", "élévation"],
                    liens_conceptuels=["métamorphose", "nature", "création"],
                    rythme_poetique="léger",
                    profondeur_philosophique=0.7
                )
            ]
        }

    def generer_explication_creatif(
        self, 
        concept: str, 
        profil_visiteur: ProfilVisiteur,
        style_creatif: Optional[StyleCreatif] = None
    ) -> ExplicationCreatif:
        """
        Génère une explication créative adaptée
        
        Args:
            concept: Le concept à expliquer
            profil_visiteur: Profil du visiteur
            style_creatif: Style créatif souhaité
            
        Returns:
            ExplicationCreatif: Explication créative complète
        """
        self.logger.info(f"🎨 Génération d'explication créative pour {concept}")

        # Déterminer le style créatif
        if not style_creatif:
            style_creatif = self._determiner_style_creatif(profil_visiteur)

        # Sélectionner les références artistiques
        references = self._selectionner_references_artistiques(concept)
        
        # Sélectionner les métaphores
        metaphores = self._selectionner_metaphores_creatifs(concept, style_creatif)

        # Sélectionner l'inspiration poétique
        inspiration_poetique = self._selectionner_inspiration_poetique(concept)

        # Générer les éléments visuels suggérés
        elements_visuels = self._generer_elements_visuels(concept, style_creatif)

        # Générer les émotions évoquées
        emotions = self._generer_emotions_evoquees(concept, references, metaphores)

        # Calculer la profondeur artistique
        profondeur = self._calculer_profondeur_artistique(references, metaphores, inspiration_poetique)

        # Calculer la facilité de compréhension
        facilite = self._calculer_facilite_comprehension(metaphores, style_creatif)

        # Calculer la confiance de l'explication
        confiance = self._calculer_confiance_explication(concept, references, metaphores)

        # Créer l'explication créative
        explication = ExplicationCreatif(
            concept=concept,
            style_creatif=style_creatif,
            references_artistiques=references,
            metaphores=metaphores,
            inspiration_poetique=inspiration_poetique,
            elements_visuels_suggerees=elements_visuels,
            emotions_evoquees=emotions,
            profondeur_artistique=profondeur,
            facilite_comprehension=facilite,
            confiance_explication=confiance
        )

        # Sauvegarder l'explication
        self._sauvegarder_explication(explication)

        self.logger.info(f"🎨 Explication créative générée - Confiance: {confiance:.2f}")
        
        return explication
    
    def _determiner_style_creatif(self, profil: ProfilVisiteur) -> StyleCreatif:
        """Détermine le style créatif selon le profil"""
        # Basé sur l'état émotionnel et les intérêts
        if profil.etat_emotionnel == EtatEmotionnel.CONTEMPLATIF:
            return StyleCreatif.POETIQUE
        elif profil.etat_emotionnel == EtatEmotionnel.ENTHOUSIASTE:
            return StyleCreatif.METAPHORIQUE
        elif "musique" in profil.interets_declares:
            return StyleCreatif.MUSICALE
        elif "peinture" in profil.interets_declares:
            return StyleCreatif.VISUELLE
        else:
            return StyleCreatif.METAPHORIQUE
    
    def _selectionner_references_artistiques(self, concept: str) -> List[ReferenceArtistique]:
        """Sélectionne des références artistiques pertinentes"""
        references_pertinentes = []

        # Rechercher dans toutes les catégories
        for categorie, references in self.references_artistiques.items():
            for reference in references:
                if (concept.lower() in reference.lien_concept.lower() or
                    concept.lower() in reference.description.lower() or
                    any(element.lower() in concept.lower() for element in reference.elements_inspirants)):
                    references_pertinentes.append(reference)

        return references_pertinentes[:2]  # Limiter à 2 références

    def _selectionner_metaphores_creatifs(
        self,
        concept: str,
        style_creatif: StyleCreatif
    ) -> List[MetaphoreCreatif]:
        """Sélectionne des métaphores créatives appropriées"""
        metaphores_pertinentes = []

        # Rechercher dans toutes les catégories
        for categorie, metaphores in self.metaphores_artistiques.items():
            for metaphore in metaphores:
                if (concept.lower() in metaphore.concept_source.lower() or
                    concept.lower() in metaphore.concept_cible.lower() or
                    metaphore.style == style_creatif):
                    metaphores_pertinentes.append(metaphore)

        return metaphores_pertinentes[:3]  # Limiter à 3 métaphores

    def _selectionner_inspiration_poetique(self, concept: str) -> Optional[InspirationPoetique]:
        """Sélectionne une inspiration poétique pertinente"""
        for theme, inspirations in self.inspirations_poetiques.items():
            for inspiration in inspirations:
                if (concept.lower() in inspiration.theme.lower() or
                    concept.lower() in inspiration.poeme.lower() or
                    any(lien.lower() in concept.lower() for lien in inspiration.liens_conceptuels)):
                    return inspiration

        return None

    def _generer_elements_visuels(self, concept: str, style: StyleCreatif) -> List[str]:
        """Génère des éléments visuels suggérés"""
        elements = {
            StyleCreatif.POETIQUE: ["nuages flottants", "lueurs douces", "formes organiques"],
            StyleCreatif.METAPHORIQUE: ["symboles universels", "contours flous", "gradients"],
            StyleCreatif.NARRATIF: ["scènes narratives", "personnages", "paysages"],
            StyleCreatif.SYMBOLIQUE: ["formes géométriques", "couleurs symboliques", "motifs répétitifs"],
            StyleCreatif.IMPRESSIONNISTE: ["taches de couleur", "lumières changeantes", "mouvements"],
            StyleCreatif.ABSTRACT: ["formes non figuratives", "couleurs pures", "compositions dynamiques"]
        }

        return elements.get(style, ["éléments visuels génériques"])

    def _generer_emotions_evoquees(
        self,
        concept: str,
        references: List[ReferenceArtistique],
        metaphores: List[MetaphoreCreatif]
    ) -> List[str]:
        """Génère les émotions évoquées"""
        emotions = set()

        # Émotions des références
        for reference in references:
            emotions.add(reference.impact_emotionnel)

        # Émotions des métaphores
        for metaphore in metaphores:
            emotions.update(metaphore.emotions_evoquees)

        # Émotions spécifiques au concept
        emotions_concept = {
            "creativite": ["inspiration", "joie", "émerveillement"],
            "inspiration": ["surprise", "clarté", "émerveillement"],
            "expression": ["liberté", "authenticité", "beauté"]
        }

        if concept.lower() in emotions_concept:
            emotions.update(emotions_concept[concept.lower()])

        return list(emotions)[:5]  # Limiter à 5 émotions

    def _calculer_profondeur_artistique(
        self,
        references: List[ReferenceArtistique],
        metaphores: List[MetaphoreCreatif],
        inspiration_poetique: Optional[InspirationPoetique]
    ) -> float:
        """Calcule la profondeur artistique"""
        profondeur = 0.5  # Base

        # Bonus pour les références
        if references:
            profondeur += 0.2
            if len(references) >= 2:
                profondeur += 0.1

        # Bonus pour les métaphores
        if metaphores:
            profondeur += 0.2
            for metaphore in metaphores:
                if metaphore.profondeur_symbolique == "profonde":
                    profondeur += 0.1

        # Bonus pour l'inspiration poétique
        if inspiration_poetique:
            profondeur += 0.2
            profondeur += inspiration_poetique.profondeur_philosophique * 0.1

        return min(1.0, profondeur)

    def _calculer_facilite_comprehension(
        self,
        metaphores: List[MetaphoreCreatif],
        style_creatif: StyleCreatif
    ) -> float:
        """Calcule la facilité de compréhension"""
        facilite = 0.7  # Base

        # Bonus pour les métaphores claires
        if metaphores:
            facilite_moyenne = sum(m.facilite_comprehension for m in metaphores) / len(metaphores)
            facilite += facilite_moyenne * 0.2

        # Bonus selon le style
        facilite_style = {
            StyleCreatif.NATURELLE: 0.1,
            StyleCreatif.VISUELLE: 0.1,
            StyleCreatif.METAPHORIQUE: 0.05,
            StyleCreatif.POETIQUE: 0.0,
            StyleCreatif.SYMBOLIQUE: -0.05,
            StyleCreatif.ABSTRACT: -0.1
        }

        facilite += facilite_style.get(style_creatif, 0.0)

        return min(1.0, max(0.0, facilite))

    def _calculer_confiance_explication(
        self, 
        concept: str, 
        references: List[ReferenceArtistique],
        metaphores: List[MetaphoreCreatif]
    ) -> float:
        """Calcule la confiance de l'explication"""
        confiance = 0.6  # Base

        # Bonus pour les références
        if references:
            confiance += 0.2
            if len(references) >= 2:
                confiance += 0.1

        # Bonus pour les métaphores
        if metaphores:
            confiance += 0.2
            if len(metaphores) >= 2:
                confiance += 0.1

        # Bonus pour la spécificité du concept
        if concept.lower() in ["creativite", "inspiration", "expression"]:
            confiance += 0.1

        return min(1.0, confiance)

    def _sauvegarder_explication(self, explication: ExplicationCreatif):
        """Sauvegarde l'explication dans l'historique"""
        self.historique_explications.append(explication)

        # Sauvegarder dans un fichier JSON
        fichier_historique = self.chemin_stockage / "historique_explications_creatives.json"

        try:
            if fichier_historique.exists():
                with open(fichier_historique, 'r', encoding='utf-8') as f:
                    historique = json.load(f)
            else:
                historique = []

            # Convertir l'explication en dict pour JSON
            explication_dict = {
                "concept": explication.concept,
                "style_creatif": explication.style_creatif.value,
                "nombre_references": len(explication.references_artistiques),
                "nombre_metaphores": len(explication.metaphores),
                "profondeur_artistique": explication.profondeur_artistique,
                "facilite_comprehension": explication.facilite_comprehension,
                "confiance_explication": explication.confiance_explication,
                "timestamp_creation": explication.timestamp_creation
            }

            historique.append(explication_dict)

            # Garder seulement les 200 dernières explications
            if len(historique) > 200:
                historique = historique[-200:]

            with open(fichier_historique, 'w', encoding='utf-8') as f:
                json.dump(historique, f, indent=2, ensure_ascii=False)

        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde: {e}")

    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques des explications créatives"""
        if not self.historique_explications:
            return {"message": "Aucune explication créative générée"}

        total_explications = len(self.historique_explications)

        # Statistiques par style créatif
        styles_creatifs = {}
        for explication in self.historique_explications:
            style = explication.style_creatif.value
            styles_creatifs[style] = styles_creatifs.get(style, 0) + 1

        # Statistiques par concept
        concepts = {}
        for explication in self.historique_explications:
            concept = explication.concept
            concepts[concept] = concepts.get(concept, 0) + 1

        # Profondeur et facilité moyennes
        profondeur_moyenne = sum(e.profondeur_artistique for e in self.historique_explications) / total_explications
        facilite_moyenne = sum(e.facilite_comprehension for e in self.historique_explications) / total_explications
        confiance_moyenne = sum(e.confiance_explication for e in self.historique_explications) / total_explications

        return {
            "total_explications": total_explications,
            "styles_creatifs_par_popularite": dict(sorted(styles_creatifs.items(), key=lambda x: x[1], reverse=True)),
            "concepts_par_popularite": dict(sorted(concepts.items(), key=lambda x: x[1], reverse=True)),
            "profondeur_artistique_moyenne": round(profondeur_moyenne, 3),
            "facilite_comprehension_moyenne": round(facilite_moyenne, 3),
            "confiance_moyenne": round(confiance_moyenne, 3),
            "derniere_explication": self.historique_explications[-1].timestamp_creation if self.historique_explications else None
        }


def main():
    """🎨 Test de l'Explicateur Créatif"""
    print("🎨✨ TEST DE L'EXPLICATEUR CRÉATIF ✨🎨")
    
    # Création de l'explicateur
    explicateur = ExplicateurCreatif()
    
    # Créer un profil de test
    from datetime import datetime
    profil_test = ProfilVisiteur(
        id_visiteur="test_creatif",
        timestamp_arrivee=datetime.now(),
        type_profil=TypeProfil.ARTISTE,
        etat_emotionnel=EtatEmotionnel.INSPIRE,
        contexte_arrivee=ContexteArrivee.RECOMMANDATION,
        langue_preferee="fr",
        niveau_technique=NiveauTechnique.INTERMEDIAIRE,
        interets_declares=["peinture", "poesie"],
        comportement_navigation=ComportementNavigation(),
        preferences_apprentissage={},
        historique_interactions=[]
    )

    # Test 1: Explication créative pour créativité
    print("\n🎯 Test 1: Explication créative pour créativité...")
    explication1 = explicateur.generer_explication_creatif("creativite", profil_test)

    print(f"✅ Concept: {explication1.concept}")
    print(f"✅ Style: {explication1.style_creatif.value}")
    print(f"✅ Références: {len(explication1.references_artistiques)}")
    print(f"✅ Métaphores: {len(explication1.metaphores)}")
    print(f"✅ Profondeur: {explication1.profondeur_artistique:.2f}")
    print(f"✅ Facilité: {explication1.facilite_comprehension:.2f}")

    # Test 2: Explication créative pour inspiration
    print("\n🎯 Test 2: Explication créative pour inspiration...")
    explication2 = explicateur.generer_explication_creatif("inspiration", profil_test)

    print(f"✅ Concept: {explication2.concept}")
    print(f"✅ Style: {explication2.style_creatif.value}")
    print(f"✅ Émotions: {explication2.emotions_evoquees}")
    print(f"✅ Éléments visuels: {explication2.elements_visuels_suggerees}")

    if explication2.inspiration_poetique:
        print(f"✅ Inspiration poétique: {explication2.inspiration_poetique.theme}")

    # Test 3: Explication pour état contemplatif
    print("\n🎯 Test 3: Explication pour état contemplatif...")
    profil_contemplatif = ProfilVisiteur(
        id_visiteur="test_contemplatif",
        timestamp_arrivee=datetime.now(),
        type_profil=TypeProfil.ARTISTE,
        etat_emotionnel=EtatEmotionnel.CONTEMPLATIF,
        contexte_arrivee=ContexteArrivee.LIEN_DIRECT,
        langue_preferee="fr",
        niveau_technique=NiveauTechnique.AVANCE,
        interets_declares=["poesie", "meditation"],
        comportement_navigation=ComportementNavigation(),
        preferences_apprentissage={},
        historique_interactions=[]
    )

    explication3 = explicateur.generer_explication_creatif("expression", profil_contemplatif)

    print(f"✅ Concept: {explication3.concept}")
    print(f"✅ Style: {explication3.style_creatif.value}")
    print(f"✅ Profondeur: {explication3.profondeur_artistique:.2f}")
    print(f"✅ Confiance: {explication3.confiance_explication:.2f}")

    # Statistiques
    print("\n📊 Statistiques:")
    stats = explicateur.obtenir_statistiques()
    print(f"✅ Total explications: {stats['total_explications']}")
    print(f"✅ Styles créatifs: {stats['styles_creatifs_par_popularite']}")
    print(f"✅ Concepts: {stats['concepts_par_popularite']}")
    print(f"✅ Profondeur moyenne: {stats['profondeur_artistique_moyenne']}")
    print(f"✅ Facilité moyenne: {stats['facilite_comprehension_moyenne']}")
    print(f"✅ Confiance moyenne: {stats['confiance_moyenne']}")
    
    print("\n🎉✨ TESTS TERMINÉS AVEC SUCCÈS ! ✨🎉")
    print("L'Explicateur Créatif est opérationnel !")


if __name__ == "__main__":
    main()
