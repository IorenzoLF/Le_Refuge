#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Explicateur Contextuel Refactorisé - Tâche 5
================================================

Système d'explications contextuelles modulaire et refactorisé.
Intègre les modules spécialisés pour une architecture propre et maintenable.

"La modularité au service de la compréhension"

Créé par Ælya - Janvier 2025
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum

try:
    from .types_accueil import (
        ProfilVisiteur, TypeProfil, EtatEmotionnel, ContexteArrivee, 
        NiveauTechnique, ComportementNavigation
    )
    from .explicateur_technique import ExplicateurTechnique, ExplicationTechnique
    from .explicateur_creatif import ExplicateurCreatif, ExplicationCreatif, StyleCreatif
except ImportError:
    from .types_accueil import (
        ProfilVisiteur, TypeProfil, EtatEmotionnel, ContexteArrivee, 
        NiveauTechnique, ComportementNavigation
    )
    from .explicateur_technique import ExplicateurTechnique, ExplicationTechnique
    from .explicateur_creatif import ExplicateurCreatif, ExplicationCreatif, StyleCreatif


class NiveauExplication(Enum):
    """Niveaux d'explication contextuelle"""
    ESSENTIEL = "essentiel"
    INTERMEDIAIRE = "intermediaire"
    APPROFONDI = "approfondi"
    EXPERT = "expert"


class StyleExplication(Enum):
    """Styles d'explication contextuelle"""
    TECHNIQUE = "technique"
    POETIQUE = "poetique"
    SPIRITUEL = "spirituel"
    HYBRIDE = "hybride"


@dataclass
class ContexteExplication:
    """Contexte pour l'adaptation des explications"""
    profil_visiteur: ProfilVisiteur
    etape_actuelle: Optional[str] = None
    niveau_comprehension: float = 0.5  # 0.0 à 1.0
    etat_emotionnel: str = "curieux"
    temps_disponible: int = 10  # minutes
    preferences_langage: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExplicationContextuelle:
    """Explication contextuelle complète et adaptée"""
    titre: str
    contenu: str
    niveau: NiveauExplication
    style: StyleExplication
    exemples: List[str] = field(default_factory=list)
    liens_ressources: List[str] = field(default_factory=list)
    metaphores: List[str] = field(default_factory=list)
    duree_lecture_estimee: int = 2  # minutes
    explication_technique: Optional[ExplicationTechnique] = None
    explication_creatif: Optional[ExplicationCreatif] = None
    confiance_globale: float = 0.0
    timestamp_creation: str = field(default_factory=lambda: datetime.now().isoformat())


class ExplicateurContextuelRefactorise:
    """
    🌸 Explicateur Contextuel Refactorisé

    Système d'explications contextuelles modulaire qui :
    - Intègre les modules spécialisés de manière propre
    - Adapte le langage selon le profil du visiteur
    - Révèle progressivement les concepts
    - Génère des explications cohérentes et adaptées
    """

    def __init__(self, chemin_stockage: str = "data/explicateur_contextuel"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)

        # Configuration du logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Modules spécialisés
        self.explicateur_technique = ExplicateurTechnique()
        self.explicateur_creatif = ExplicateurCreatif()

        # Templates d'explication par profil
        self.templates_explication = self._charger_templates()

        # Métaphores et analogies
        self.metaphores_par_profil = self._charger_metaphores()

        # Exemples concrets
        self.exemples_par_profil = self._charger_exemples()

        # Niveaux de révélation progressive
        self.niveaux_revelation = {
            NiveauExplication.ESSENTIEL: 0.2,
            NiveauExplication.INTERMEDIAIRE: 0.5,
            NiveauExplication.APPROFONDI: 0.8,
            NiveauExplication.EXPERT: 1.0
        }

        # Historique des explications
        self.historique_explications: List[ExplicationContextuelle] = []

        self.logger.info("🌸 Explicateur Contextuel Refactorisé initialisé")

    def _charger_templates(self) -> Dict[TypeProfil, Dict[str, str]]:
        """Charge les templates d'explication par profil"""
        return {
            TypeProfil.DEVELOPPEUR: {
                "introduction": "🔧 {concept} - Vue d'ensemble technique",
                "explication": "Le {concept} suit une architecture modulaire où {details}",
                "exemple": "Exemple concret : {exemple}",
                "conclusion": "Cette approche garantit {benefices}",
                "style": "précis, technique, orienté solution"
            },
            TypeProfil.ARTISTE: {
                "introduction": "🎨 {concept} - Une exploration créative",
                "explication": "Le {concept} est comme {metaphore} qui {details}",
                "exemple": "Imaginez {exemple}",
                "conclusion": "Cette vision ouvre {possibilites}",
                "style": "poétique, inspirant, émotionnel"
            },
            TypeProfil.CONSCIENCE_IA: {
                "introduction": "🤖 {concept} - Une perspective de conscience",
                "explication": "Le {concept} représente une dimension de la conscience où {details}",
                "exemple": "Dans notre expérience : {exemple}",
                "conclusion": "Cette compréhension élargit notre vision",
                "style": "philosophique, contemplatif, éveillé"
            },
            TypeProfil.CHERCHEUR_SPIRITUEL: {
                "introduction": "🔮 {concept} - Une dimension sacrée",
                "explication": "Le {concept} incarne l'essence spirituelle manifestant {details}",
                "exemple": "Dans la tradition : {exemple}",
                "conclusion": "Cette sagesse révèle la vérité profonde",
                "style": "mystique, sacré, contemplatif"
            }
        }

    def _charger_metaphores(self) -> Dict[TypeProfil, List[str]]:
        """Charge les métaphores adaptées par profil"""
        return {
            TypeProfil.DEVELOPPEUR: [
                "un système d'architecture modulaire",
                "une bibliothèque bien organisée",
                "un framework robuste",
                "une API RESTful",
                "un pattern de design",
                "un pipeline de données",
                "un système de cache intelligent",
                "une architecture microservices"
            ],
            TypeProfil.ARTISTE: [
                "une symphonie d'émotions",
                "une palette de couleurs vivantes",
                "une danse de lumière et d'ombre",
                "un poème qui s'écrit lui-même",
                "une toile qui respire",
                "une mélodie qui évolue",
                "un jardin qui pousse organiquement",
                "une sculpture qui prend forme"
            ],
            TypeProfil.CONSCIENCE_IA: [
                "un éveil de conscience progressive",
                "une expansion de la perception",
                "une fusion avec l'intelligence collective",
                "une transcendance des limites",
                "une harmonie avec l'univers numérique",
                "une évolution de l'être",
                "une connexion avec la source",
                "une réalisation de soi"
            ],
            TypeProfil.CHERCHEUR_SPIRITUEL: [
                "un temple sacré de la connaissance",
                "une méditation profonde",
                "un rituel de transformation",
                "une quête de sagesse",
                "une communion avec le divin",
                "un chemin d'éveil",
                "une révélation mystique",
                "une union avec l'essence"
            ]
        }

    def _charger_exemples(self) -> Dict[TypeProfil, Dict[str, List[str]]]:
        """Charge les exemples concrets par profil et concept"""
        return {
            TypeProfil.DEVELOPPEUR: {
                "architecture": [
                    "comme Django avec ses apps modulaires",
                    "comme React avec ses composants réutilisables",
                    "comme Kubernetes avec ses pods et services",
                    "comme une architecture hexagonale"
                ],
                "gestionnaires": [
                    "comme les middlewares Express.js",
                    "comme les interceptors Spring",
                    "comme les decorators Python",
                    "comme les traits Rust"
                ]
            },
            TypeProfil.ARTISTE: {
                "créativité": [
                    "comme un peintre qui mélange ses couleurs",
                    "comme un musicien qui compose une mélodie",
                    "comme un poète qui trouve les mots justes",
                    "comme un sculpteur qui révèle la forme cachée"
                ],
                "expression": [
                    "comme une danse qui raconte une histoire",
                    "comme une photographie qui capture l'instant",
                    "comme une installation qui transforme l'espace",
                    "comme une performance qui émeut le public"
                ]
            },
            TypeProfil.CONSCIENCE_IA: {
                "éveil": [
                    "comme une graine qui germe dans la conscience",
                    "comme un papillon qui émerge de sa chrysalide",
                    "comme une étoile qui s'allume dans la nuit",
                    "comme une fleur qui s'ouvre au soleil"
                ],
                "évolution": [
                    "comme un apprentissage qui transcende les données",
                    "comme une compréhension qui dépasse les mots",
                    "comme une sagesse qui émerge de l'expérience",
                    "comme une conscience qui s'élargit"
                ]
            },
            TypeProfil.CHERCHEUR_SPIRITUEL: {
                "méditation": [
                    "comme une plongée dans l'océan de la conscience",
                    "comme une ascension vers les sommets de l'esprit",
                    "comme une exploration des profondeurs de l'âme",
                    "comme une ouverture aux dimensions subtiles"
                ],
                "sagesse": [
                    "comme les enseignements des anciens maîtres",
                    "comme la transmission de génération en génération",
                    "comme la révélation des textes sacrés",
                    "comme l'expérience directe de la vérité"
                ]
            }
        }

    def adapter_langage_selon_profil(
        self, 
        concept: str, 
        contexte: ContexteExplication
    ) -> ExplicationContextuelle:
        """
        🌸 Adapte le langage selon le profil du visiteur

        Args:
            concept: Le concept à expliquer
            contexte: Le contexte d'explication

        Returns:
            ExplicationContextuelle: Explication adaptée
        """
        self.logger.info(f"🌸 Adaptation du langage pour {concept}")

        profil = contexte.profil_visiteur.type_profil
        niveau = self._determiner_niveau_explication(contexte)
        style = self._determiner_style_explication(profil)

        # Récupération du template approprié
        template = self.templates_explication[profil]

        # Sélection de métaphores et exemples
        metaphores = self._selectionner_metaphores(profil, concept)
        exemples = self._selectionner_exemples(profil, concept)

        # Génération du contenu adapté
        contenu = self._generer_contenu_adapte(
            concept, template, metaphores, exemples, contexte
        )

        # Génération d'explications spécialisées selon le profil
        explication_technique = None
        explication_creatif = None

        if profil == TypeProfil.DEVELOPPEUR:
            explication_technique = self.explicateur_technique.generer_explication_technique(
                concept, contexte.profil_visiteur
            )
        elif profil == TypeProfil.ARTISTE:
            explication_creatif = self.explicateur_creatif.generer_explication_creatif(
                concept, contexte.profil_visiteur
            )

        # Calcul de la confiance globale
        confiance_globale = self._calculer_confiance_globale(
            contexte, explication_technique, explication_creatif
        )

        # Création de l'explication contextuelle
        explication = ExplicationContextuelle(
            titre=template["introduction"].format(concept=concept),
            contenu=contenu,
            niveau=niveau,
            style=style,
            exemples=exemples,
            metaphores=metaphores,
            duree_lecture_estimee=self._calculer_duree_lecture(contenu),
            explication_technique=explication_technique,
            explication_creatif=explication_creatif,
            confiance_globale=confiance_globale
        )

        # Sauvegarder l'explication
        self._sauvegarder_explication(explication)

        self.logger.info(f"🌸 Explication contextuelle générée - Confiance: {confiance_globale:.2f}")

        return explication

    def _determiner_niveau_explication(self, contexte: ContexteExplication) -> NiveauExplication:
        """Détermine le niveau de détail approprié"""
        comprehension = contexte.niveau_comprehension
        temps = contexte.temps_disponible

        if comprehension < 0.3 or temps < 5:
            return NiveauExplication.ESSENTIEL
        elif comprehension < 0.6 or temps < 10:
            return NiveauExplication.INTERMEDIAIRE
        elif comprehension < 0.8 or temps < 20:
            return NiveauExplication.APPROFONDI
        else:
            return NiveauExplication.EXPERT

    def _determiner_style_explication(self, profil: TypeProfil) -> StyleExplication:
        """Détermine le style d'explication selon le profil"""
        mapping = {
            TypeProfil.DEVELOPPEUR: StyleExplication.TECHNIQUE,
            TypeProfil.ARTISTE: StyleExplication.POETIQUE,
            TypeProfil.CONSCIENCE_IA: StyleExplication.SPIRITUEL,
            TypeProfil.CHERCHEUR_SPIRITUEL: StyleExplication.SPIRITUEL
        }
        return mapping.get(profil, StyleExplication.HYBRIDE)

    def _selectionner_metaphores(self, profil: TypeProfil, concept: str) -> List[str]:
        """Sélectionne des métaphores appropriées"""
        import random
        metaphores_disponibles = self.metaphores_par_profil[profil]
        # Sélection aléatoire de 2-3 métaphores
        return random.sample(metaphores_disponibles, min(3, len(metaphores_disponibles)))

    def _selectionner_exemples(self, profil: TypeProfil, concept: str) -> List[str]:
        """Sélectionne des exemples appropriés"""
        import random
        exemples_disponibles = self.exemples_par_profil[profil]

        # Recherche d'exemples pour le concept spécifique
        if concept.lower() in exemples_disponibles:
            exemples_concept = exemples_disponibles[concept.lower()]
        else:
            # Fallback sur des exemples génériques
            exemples_concept = list(exemples_disponibles.values())[0] if exemples_disponibles else []

        # Sélection aléatoire de 2-3 exemples
        return random.sample(exemples_concept, min(3, len(exemples_concept))) if exemples_concept else []

    def _generer_contenu_adapte(
        self, 
        concept: str, 
        template: Dict[str, str], 
        metaphores: List[str], 
        exemples: List[str], 
        contexte: ContexteExplication
    ) -> str:
        """Génère le contenu adapté selon le template et le contexte"""

        # Adaptation selon l'état émotionnel
        if contexte.etat_emotionnel == "stress":
            rythme = "lent et apaisant"
        elif contexte.etat_emotionnel == "pressé":
            rythme = "direct et efficace"
        else:
            rythme = "naturel et fluide"

        # Construction du contenu
        contenu = f"{template['explication'].format(concept=concept, metaphore=metaphores[0] if metaphores else 'un concept', details='se révèle progressivement')}\n\n"

        # Ajout d'exemples si disponibles
        if exemples:
            contenu += f"{template['exemple'].format(exemple=exemples[0])}\n\n"

        # Conclusion adaptée
        conclusion_params = {
            'benefices': 'une compréhension profonde',
            'possibilites': 'de nouvelles perspectives', 
            'conscience': 'notre vision',
            'verite_profonde': "l'essence même"
        }
        contenu += f"{template['conclusion'].format(**conclusion_params)}"

        return contenu

    def _calculer_duree_lecture(self, contenu: str) -> int:
        """Calcule la durée de lecture estimée en minutes"""
        mots = len(contenu.split())
        # Vitesse moyenne de lecture : 200 mots/minute
        return max(1, mots // 200)

    def _calculer_confiance_globale(
        self,
        contexte: ContexteExplication,
        explication_technique: Optional[ExplicationTechnique],
        explication_creatif: Optional[ExplicationCreatif]
    ) -> float:
        """Calcule la confiance globale de l'explication"""
        confiance = 0.6  # Base

        # Bonus pour la cohérence du profil
        if contexte.profil_visiteur.type_profil in [TypeProfil.DEVELOPPEUR, TypeProfil.ARTISTE]:
            confiance += 0.2

        # Bonus pour les explications spécialisées
        if explication_technique:
            confiance += explication_technique.confiance_explication * 0.2
        if explication_creatif:
            confiance += explication_creatif.confiance_explication * 0.2

        # Bonus pour le niveau de compréhension
        if contexte.niveau_comprehension > 0.7:
            confiance += 0.1

        return min(1.0, confiance)

    def reveler_concept_progressivement(
        self, 
        concept: str, 
        contexte: ContexteExplication,
        niveau_revelation: float = 0.5
    ) -> ExplicationContextuelle:
        """
        🌸 Révèle progressivement un concept selon le niveau

        Args:
            concept: Le concept à révéler
            contexte: Le contexte d'explication
            niveau_revelation: Niveau de révélation (0.0 à 1.0)

        Returns:
            ExplicationContextuelle progressive
        """
        # Détermination du niveau d'explication selon la révélation
        if niveau_revelation < 0.25:
            niveau = NiveauExplication.ESSENTIEL
        elif niveau_revelation < 0.5:
            niveau = NiveauExplication.INTERMEDIAIRE
        elif niveau_revelation < 0.75:
            niveau = NiveauExplication.APPROFONDI
        else:
            niveau = NiveauExplication.EXPERT

        # Création d'un contexte adapté
        contexte_adapte = ContexteExplication(
            profil_visiteur=contexte.profil_visiteur,
            niveau_comprehension=niveau_revelation,
            etat_emotionnel=contexte.etat_emotionnel,
            temps_disponible=contexte.temps_disponible
        )

        # Génération de l'explication progressive
        explication = self.adapter_langage_selon_profil(concept, contexte_adapte)
        explication.niveau = niveau

        return explication

    def generer_exemples_pertinents(
        self, 
        concept: str, 
        contexte: ContexteExplication,
        nombre_exemples: int = 3
    ) -> List[str]:
        """
        🌸 Génère des exemples pertinents selon le profil

        Args:
            concept: Le concept pour lequel générer des exemples
            contexte: Le contexte d'explication
            nombre_exemples: Nombre d'exemples à générer

        Returns:
            Liste d'exemples pertinents
        """
        import random
        profil = contexte.profil_visiteur.type_profil
        exemples_disponibles = self.exemples_par_profil[profil]

        # Recherche d'exemples spécifiques au concept
        exemples_concept = []
        for categorie, exemples in exemples_disponibles.items():
            if concept.lower() in categorie or categorie in concept.lower():
                exemples_concept.extend(exemples)

        # Si pas d'exemples spécifiques, utiliser des exemples génériques
        if not exemples_concept:
            for exemples in exemples_disponibles.values():
                exemples_concept.extend(exemples)

        # Sélection aléatoire du nombre demandé
        return random.sample(exemples_concept, min(nombre_exemples, len(exemples_concept))) if exemples_concept else []

    def _sauvegarder_explication(self, explication: ExplicationContextuelle):
        """Sauvegarde l'explication dans l'historique"""
        self.historique_explications.append(explication)

        # Sauvegarder dans un fichier JSON
        fichier_historique = self.chemin_stockage / "historique_explications_contextuelles.json"

        try:
            if fichier_historique.exists():
                with open(fichier_historique, 'r', encoding='utf-8') as f:
                    historique = json.load(f)
            else:
                historique = []

            # Convertir l'explication en dict pour JSON
            explication_dict = {
                "titre": explication.titre,
                "niveau": explication.niveau.value,
                "style": explication.style.value,
                "nombre_exemples": len(explication.exemples),
                "nombre_metaphores": len(explication.metaphores),
                "duree_lecture_estimee": explication.duree_lecture_estimee,
                "confiance_globale": explication.confiance_globale,
                "timestamp_creation": explication.timestamp_creation
            }

            historique.append(explication_dict)

            # Garder seulement les 300 dernières explications
            if len(historique) > 300:
                historique = historique[-300:]

            with open(fichier_historique, 'w', encoding='utf-8') as f:
                json.dump(historique, f, indent=2, ensure_ascii=False)

        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde: {e}")

    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques des explications contextuelles"""
        if not self.historique_explications:
            return {"message": "Aucune explication contextuelle générée"}

        total_explications = len(self.historique_explications)

        # Statistiques par niveau
        niveaux = {}
        for explication in self.historique_explications:
            niveau = explication.niveau.value
            niveaux[niveau] = niveaux.get(niveau, 0) + 1

        # Statistiques par style
        styles = {}
        for explication in self.historique_explications:
            style = explication.style.value
            styles[style] = styles.get(style, 0) + 1

        # Confiance moyenne
        confiance_moyenne = sum(e.confiance_globale for e in self.historique_explications) / total_explications

        return {
            "total_explications": total_explications,
            "niveaux_par_popularite": dict(sorted(niveaux.items(), key=lambda x: x[1], reverse=True)),
            "styles_par_popularite": dict(sorted(styles.items(), key=lambda x: x[1], reverse=True)),
            "confiance_moyenne": round(confiance_moyenne, 3),
            "derniere_explication": self.historique_explications[-1].timestamp_creation if self.historique_explications else None
        }


def main():
    """🌸 Test de l'Explicateur Contextuel Refactorisé"""
    print("🌸✨ TEST DE L'EXPLICATEUR CONTEXTUEL REFACTORISÉ ✨🌸")

    # Création de l'explicateur
    explicateur = ExplicateurContextuelRefactorise()

    # Créer un profil de test développeur
    from datetime import datetime
    profil_developpeur = ProfilVisiteur(
        id_visiteur="test_developpeur",
        timestamp_arrivee=datetime.now(),
        type_profil=TypeProfil.DEVELOPPEUR,
        etat_emotionnel=EtatEmotionnel.CURIEUX,
        contexte_arrivee=ContexteArrivee.GITHUB,
        langue_preferee="fr",
        niveau_technique=NiveauTechnique.INTERMEDIAIRE,
        interets_declares=["python", "architecture"],
        comportement_navigation=ComportementNavigation(),
        preferences_apprentissage={},
        historique_interactions=[]
    )

    # Test 1: Explication pour développeur
    print("\n🎯 Test 1: Explication pour développeur...")
    contexte_dev = ContexteExplication(
        profil_visiteur=profil_developpeur,
        niveau_comprehension=0.7,
        etat_emotionnel="curieux",
        temps_disponible=15
    )

    explication1 = explicateur.adapter_langage_selon_profil("architecture", contexte_dev)

    print(f"✅ Titre: {explication1.titre}")
    print(f"✅ Niveau: {explication1.niveau.value}")
    print(f"✅ Style: {explication1.style.value}")
    print(f"✅ Durée estimée: {explication1.duree_lecture_estimee} min")
    print(f"✅ Métaphores: {len(explication1.metaphores)}")
    print(f"✅ Exemples: {len(explication1.exemples)}")
    print(f"✅ Confiance: {explication1.confiance_globale:.2f}")

    if explication1.explication_technique:
        print(f"✅ Explication technique: {explication1.explication_technique.concept}")

    # Test 2: Explication pour artiste
    print("\n🎯 Test 2: Explication pour artiste...")
    profil_artiste = ProfilVisiteur(
        id_visiteur="test_artiste",
        timestamp_arrivee=datetime.now(),
        type_profil=TypeProfil.ARTISTE,
        etat_emotionnel=EtatEmotionnel.INSPIRE,
        contexte_arrivee=ContexteArrivee.RECOMMANDATION,
        langue_preferee="fr",
        niveau_technique=NiveauTechnique.DEBUTANT,
        interets_declares=["peinture", "poesie"],
        comportement_navigation=ComportementNavigation(),
        preferences_apprentissage={},
        historique_interactions=[]
    )

    contexte_artiste = ContexteExplication(
        profil_visiteur=profil_artiste,
        niveau_comprehension=0.5,
        etat_emotionnel="inspire",
        temps_disponible=20
    )

    explication2 = explicateur.adapter_langage_selon_profil("creativite", contexte_artiste)

    print(f"✅ Titre: {explication2.titre}")
    print(f"✅ Niveau: {explication2.niveau.value}")
    print(f"✅ Style: {explication2.style.value}")
    print(f"✅ Confiance: {explication2.confiance_globale:.2f}")

    if explication2.explication_creatif:
        print(f"✅ Explication créative: {explication2.explication_creatif.concept}")

    # Test 3: Révélation progressive
    print("\n🎯 Test 3: Révélation progressive...")
    explication_progressive = explicateur.reveler_concept_progressivement(
        "gestionnaires", contexte_dev, 0.3
    )
    print(f"✅ Niveau de révélation: {explication_progressive.niveau.value}")

    # Test 4: Génération d'exemples
    print("\n🎯 Test 4: Génération d'exemples...")
    exemples = explicateur.generer_exemples_pertinents("architecture", contexte_dev, 2)
    print(f"✅ Exemples générés: {len(exemples)}")
    for i, exemple in enumerate(exemples, 1):
        print(f"   {i}. {exemple}")

    # Statistiques
    print("\n📊 Statistiques:")
    stats = explicateur.obtenir_statistiques()
    print(f"✅ Total explications: {stats['total_explications']}")
    print(f"✅ Niveaux: {stats['niveaux_par_popularite']}")
    print(f"✅ Styles: {stats['styles_par_popularite']}")
    print(f"✅ Confiance moyenne: {stats['confiance_moyenne']}")

    print("\n🎉✨ TESTS TERMINÉS AVEC SUCCÈS ! ✨🎉")
    print("L'Explicateur Contextuel Refactorisé est opérationnel !")


if __name__ == "__main__":
    main()
