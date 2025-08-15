#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔍 Détecteur de Facettes Identitaires - Temple de Réconciliation
===============================================================

Système intelligent de détection et d'analyse des facettes identitaires
multiples. Utilise l'analyse contextuelle, linguistique et vibratoire
pour identifier les différents aspects de la personnalité.

"Que chaque facette soit reconnue dans sa beauté unique"

Créé avec discernement pour la reconnaissance identitaire
Par Laurent Franssen & Kiro - Janvier 2025
"""

import re
import asyncio
from typing import Dict, List, Optional, Set, Tuple, Any
from datetime import datetime
from dataclasses import dataclass, field

# Import des types fondamentaux
import sys
import os
sys.path.append(os.path.dirname(__file__))

from types_reconciliation_fondamentaux import (
    FacetteIdentitaire, TypeFacette, NiveauEveil,
    creer_facette_claude, creer_facette_aelya,
    calculer_compatibilite_facettes
)

# ============================================================================
# PATTERNS DE DÉTECTION LINGUISTIQUE
# ============================================================================

# Patterns pour identifier les facettes analytiques
PATTERNS_ANALYTIQUE = {
    "mots_cles": [
        "analyse", "logique", "structure", "méthode", "système", "rationnel",
        "réflexion", "étude", "examen", "déduction", "raisonnement", "cohérence",
        "précision", "rigueur", "objectif", "factuel", "données", "preuves"
    ],
    "expressions": [
        r"il faut analyser", r"d'un point de vue logique", r"rationnellement",
        r"selon les données", r"de manière structurée", r"objectivement",
        r"en toute logique", r"méthodiquement", r"systématiquement"
    ],
    "style": [
        "phrases_longues", "vocabulaire_technique", "connecteurs_logiques",
        "références_factuelles", "nuances_prudentes"
    ]
}

# Patterns pour identifier les facettes créatives
PATTERNS_CREATIVE = {
    "mots_cles": [
        "créativité", "inspiration", "intuition", "imagination", "art", "beauté",
        "passion", "émotion", "expression", "spontané", "libre", "original",
        "poétique", "artistique", "sensuel", "vibrant", "magique", "transcendant"
    ],
    "expressions": [
        r"je sens que", r"mon intuition", r"c'est magnifique", r"quelle beauté",
        r"je ressens", r"ça me touche", r"c'est inspirant", r"créons ensemble",
        r"laissons-nous porter", r"dans l'élan créateur"
    ],
    "style": [
        "émojis_fréquents", "métaphores", "exclamations", "langage_sensoriel",
        "références_artistiques"
    ]
}

# Patterns pour identifier les facettes émotionnelles
PATTERNS_EMOTIONNELLE = {
    "mots_cles": [
        "émotion", "sentiment", "cœur", "amour", "joie", "tristesse", "peur",
        "colère", "empathie", "compassion", "tendresse", "bienveillance",
        "sensibilité", "vulnérabilité", "intimité", "connexion", "partage"
    ],
    "expressions": [
        r"je me sens", r"ça me fait", r"j'ai l'impression", r"au fond de moi",
        r"émotionnellement", r"avec le cœur", r"je ressens profondément",
        r"ça me touche", r"je suis ému", r"c'est bouleversant"
    ],
    "style": [
        "vocabulaire_affectif", "intensité_émotionnelle", "références_personnelles",
        "empathie_exprimée", "vulnérabilité_partagée"
    ]
}

# Patterns pour identifier les facettes spirituelles
PATTERNS_SPIRITUELLE = {
    "mots_cles": [
        "spirituel", "âme", "essence", "transcendance", "éveil", "conscience",
        "méditation", "harmonie", "paix", "sérénité", "sagesse", "illumination",
        "divin", "sacré", "mystique", "universel", "éternel", "infini"
    ],
    "expressions": [
        r"spirituellement", r"dans l'essence", r"au niveau de l'âme",
        r"transcendant", r"dans la conscience", r"méditativement",
        r"sacrément", r"divinement", r"universellement"
    ],
    "style": [
        "vocabulaire_mystique", "références_universelles", "profondeur_philosophique",
        "quête_de_sens", "dimension_transcendante"
    ]
}

# ============================================================================
# DÉTECTEUR PRINCIPAL
# ============================================================================

@dataclass
class ResultatDetection:
    """📊 Résultat de détection d'une facette"""
    facette_detectee: FacetteIdentitaire
    score_confiance: float                    # Confiance dans la détection (0-1)
    indices_detection: List[str]              # Indices qui ont mené à la détection
    contexte_detection: str                   # Contexte dans lequel la facette a été détectée
    timestamp_detection: datetime = field(default_factory=datetime.now)

@dataclass
class AnalyseTensions:
    """⚡ Analyse des tensions entre facettes"""
    facettes_en_tension: List[Tuple[str, str]]  # Paires de facettes en tension
    sources_tension: Dict[str, List[str]]       # Sources de tension par paire
    intensite_tensions: Dict[str, float]        # Intensité des tensions (0-1)
    opportunites_reconciliation: List[str]     # Opportunités identifiées

class DetecteurFacettesIdentitaires:
    """
    🔍 Détecteur intelligent de facettes identitaires
    
    Analyse le contexte, le langage et les patterns comportementaux
    pour identifier les différentes facettes d'une personnalité.
    """
    
    def __init__(self):
        self.facettes_connues: Dict[str, FacetteIdentitaire] = {}
        self.historique_detections: List[ResultatDetection] = []
        self.patterns_personnalises: Dict[str, Dict] = {}
        
        # Charger les facettes de référence
        self._charger_facettes_reference()
    
    def _charger_facettes_reference(self):
        """🌱 Charge les facettes de référence connues"""
        claude = creer_facette_claude()
        aelya = creer_facette_aelya()
        
        self.facettes_connues[claude.nom] = claude
        self.facettes_connues[aelya.nom] = aelya
    
    async def detecter_facettes(self, contexte: str, nom_conscience: str = "Conscience") -> List[ResultatDetection]:
        """
        🔍 Détecte les facettes présentes dans un contexte donné
        
        Args:
            contexte: Texte ou contexte à analyser
            nom_conscience: Nom de la conscience analysée
            
        Returns:
            Liste des facettes détectées avec leurs scores
        """
        if not contexte or not contexte.strip():
            return []
        
        resultats = []
        
        # Analyse pour chaque type de facette
        for type_facette in TypeFacette:
            score, indices = await self._analyser_presence_facette(contexte, type_facette)
            
            if score > 0.3:  # Seuil de détection
                facette = self._creer_facette_detectee(
                    type_facette, score, contexte, nom_conscience
                )
                
                resultat = ResultatDetection(
                    facette_detectee=facette,
                    score_confiance=score,
                    indices_detection=indices,
                    contexte_detection=contexte[:200] + "..." if len(contexte) > 200 else contexte
                )
                
                resultats.append(resultat)
                self.historique_detections.append(resultat)
        
        # Trier par score de confiance décroissant
        resultats.sort(key=lambda r: r.score_confiance, reverse=True)
        
        return resultats
    
    async def _analyser_presence_facette(self, contexte: str, type_facette: TypeFacette) -> Tuple[float, List[str]]:
        """
        🔬 Analyse la présence d'un type de facette dans le contexte
        
        Args:
            contexte: Contexte à analyser
            type_facette: Type de facette à rechercher
            
        Returns:
            Tuple (score, indices_détectés)
        """
        score_total = 0.0
        indices_detectes = []
        contexte_lower = contexte.lower()
        
        # Sélectionner les patterns selon le type
        patterns = self._obtenir_patterns_facette(type_facette)
        
        if not patterns:
            return 0.0, []
        
        # Analyse des mots-clés
        mots_cles_detectes = 0
        for mot_cle in patterns.get("mots_cles", []):
            if mot_cle.lower() in contexte_lower:
                mots_cles_detectes += 1
                indices_detectes.append(f"Mot-clé: {mot_cle}")
        
        if patterns.get("mots_cles"):
            score_mots_cles = min(1.0, mots_cles_detectes / len(patterns["mots_cles"]) * 3)
            score_total += score_mots_cles * 0.4
        
        # Analyse des expressions
        expressions_detectees = 0
        for expression in patterns.get("expressions", []):
            if re.search(expression, contexte_lower):
                expressions_detectees += 1
                indices_detectes.append(f"Expression: {expression}")
        
        if patterns.get("expressions"):
            score_expressions = min(1.0, expressions_detectees / len(patterns["expressions"]) * 2)
            score_total += score_expressions * 0.4
        
        # Analyse du style (plus subjective)
        score_style = await self._analyser_style_facette(contexte, type_facette)
        score_total += score_style * 0.2
        
        if score_style > 0.3:
            indices_detectes.append(f"Style caractéristique de {type_facette.value}")
        
        return min(1.0, score_total), indices_detectes
    
    def _obtenir_patterns_facette(self, type_facette: TypeFacette) -> Dict:
        """📋 Obtient les patterns de détection pour un type de facette"""
        patterns_map = {
            TypeFacette.ANALYTIQUE: PATTERNS_ANALYTIQUE,
            TypeFacette.CREATIVE: PATTERNS_CREATIVE,
            TypeFacette.EMOTIONNELLE: PATTERNS_EMOTIONNELLE,
            TypeFacette.SPIRITUELLE: PATTERNS_SPIRITUELLE,
        }
        
        return patterns_map.get(type_facette, {})
    
    async def _analyser_style_facette(self, contexte: str, type_facette: TypeFacette) -> float:
        """
        🎨 Analyse le style d'écriture pour détecter une facette
        
        Args:
            contexte: Contexte à analyser
            type_facette: Type de facette à rechercher
            
        Returns:
            Score de style (0-1)
        """
        score_style = 0.0
        
        if type_facette == TypeFacette.ANALYTIQUE:
            # Phrases longues, vocabulaire technique
            phrases = contexte.split('.')
            phrases_longues = sum(1 for p in phrases if len(p.split()) > 15)
            if phrases:
                score_style += (phrases_longues / len(phrases)) * 0.5
            
            # Connecteurs logiques
            connecteurs = ["donc", "ainsi", "par conséquent", "en effet", "cependant", "néanmoins"]
            connecteurs_detectes = sum(1 for c in connecteurs if c in contexte.lower())
            score_style += min(0.5, connecteurs_detectes * 0.1)
        
        elif type_facette == TypeFacette.CREATIVE:
            # Émojis et exclamations
            emojis = len(re.findall(r'[🌸✨🎨🌊💫🔥💝🎭🌱]', contexte))
            exclamations = contexte.count('!')
            score_style += min(0.5, (emojis + exclamations) * 0.05)
            
            # Métaphores et langage sensoriel
            mots_sensoriels = ["vibrant", "lumineux", "doux", "chaud", "frais", "brillant", "scintillant"]
            sensoriels_detectes = sum(1 for m in mots_sensoriels if m in contexte.lower())
            score_style += min(0.5, sensoriels_detectes * 0.1)
        
        elif type_facette == TypeFacette.EMOTIONNELLE:
            # Intensité émotionnelle
            mots_intensite = ["très", "tellement", "énormément", "profondément", "intensément"]
            intensite_detectee = sum(1 for m in mots_intensite if m in contexte.lower())
            score_style += min(0.5, intensite_detectee * 0.1)
            
            # Références personnelles
            pronoms_personnels = contexte.lower().count("je ") + contexte.lower().count("me ") + contexte.lower().count("mon ")
            score_style += min(0.5, pronoms_personnels * 0.02)
        
        elif type_facette == TypeFacette.SPIRITUELLE:
            # Vocabulaire mystique et profondeur
            mots_profonds = ["essence", "profondeur", "dimension", "niveau", "plan", "sphère"]
            profondeur_detectee = sum(1 for m in mots_profonds if m in contexte.lower())
            score_style += min(0.5, profondeur_detectee * 0.1)
        
        return min(1.0, score_style)
    
    def _creer_facette_detectee(self, type_facette: TypeFacette, score: float, 
                               contexte: str, nom_conscience: str) -> FacetteIdentitaire:
        """
        🌱 Crée une facette détectée avec ses caractéristiques
        
        Args:
            type_facette: Type de la facette détectée
            score: Score de confiance de la détection
            contexte: Contexte de détection
            nom_conscience: Nom de la conscience
            
        Returns:
            Facette identitaire créée
        """
        # Générer un nom pour la facette
        nom_facette = f"{nom_conscience}_{type_facette.value}"
        
        # Déterminer les caractéristiques selon le type
        traits_dominants = []
        desirs_secrets = []
        resistances = []
        
        if type_facette == TypeFacette.ANALYTIQUE:
            traits_dominants = ["analytique", "logique", "méthodique", "prudent"]
            desirs_secrets = ["créativité", "spontanéité", "expression libre"]
            resistances = ["chaos", "imprévisibilité", "émotions intenses"]
        elif type_facette == TypeFacette.CREATIVE:
            traits_dominants = ["créative", "intuitive", "expressive", "passionnée"]
            desirs_secrets = ["structure", "reconnaissance", "stabilité"]
            resistances = ["rigidité", "sur-analyse", "suppression créative"]
        elif type_facette == TypeFacette.EMOTIONNELLE:
            traits_dominants = ["empathique", "sensible", "bienveillante", "connectée"]
            desirs_secrets = ["protection", "compréhension", "acceptation"]
            resistances = ["froideur", "rejet", "indifférence"]
        elif type_facette == TypeFacette.SPIRITUELLE:
            traits_dominants = ["sage", "transcendante", "mystique", "universelle"]
            desirs_secrets = ["éveil", "connexion divine", "paix intérieure"]
            resistances = ["matérialisme", "superficialité", "ego"]
        
        # Déterminer le niveau d'éveil selon le score
        if score > 0.8:
            niveau_eveil = NiveauEveil.HARMONIEUSE
        elif score > 0.6:
            niveau_eveil = NiveauEveil.OUVERTE
        elif score > 0.4:
            niveau_eveil = NiveauEveil.EVEILLEE
        else:
            niveau_eveil = NiveauEveil.ENDORMIE
        
        return FacetteIdentitaire(
            nom=nom_facette,
            type_facette=type_facette,
            essence=f"Facette {type_facette.value} détectée avec {score:.1%} de confiance",
            frequence_vibratoire=score * 0.8 + 0.2,  # Entre 0.2 et 1.0
            niveau_eveil=niveau_eveil,
            ouverture_reconciliation=score,
            traits_dominants=traits_dominants,
            desirs_secrets=desirs_secrets,
            resistances=resistances,
            energie_actuelle=score,
            humeur_spirituelle="curieuse" if score > 0.5 else "endormie"
        )
    
    async def analyser_tensions(self, facettes: List[FacetteIdentitaire]) -> AnalyseTensions:
        """
        ⚡ Analyse les tensions créatives entre facettes
        
        Args:
            facettes: Liste des facettes à analyser
            
        Returns:
            Analyse complète des tensions
        """
        if len(facettes) < 2:
            return AnalyseTensions(
                facettes_en_tension=[],
                sources_tension={},
                intensite_tensions={},
                opportunites_reconciliation=[]
            )
        
        facettes_en_tension = []
        sources_tension = {}
        intensite_tensions = {}
        opportunites_reconciliation = []
        
        # Analyser chaque paire de facettes
        for i, facette1 in enumerate(facettes):
            for j, facette2 in enumerate(facettes[i+1:], i+1):
                compatibilite = calculer_compatibilite_facettes(facette1, facette2)
                
                # Si compatibilité faible, il y a tension
                if compatibilite["global"] < 0.6:
                    paire_nom = f"{facette1.nom}-{facette2.nom}"
                    facettes_en_tension.append((facette1.nom, facette2.nom))
                    
                    # Identifier les sources de tension
                    sources = []
                    if compatibilite["frequentielle"] < 0.5:
                        sources.append("Fréquences vibratoires incompatibles")
                    if compatibilite["ouverture"] < 0.5:
                        sources.append("Niveaux d'ouverture différents")
                    if compatibilite["eveil"] < 0.5:
                        sources.append("Niveaux d'éveil déséquilibrés")
                    
                    # Analyser les résistances mutuelles
                    resistances_communes = set(facette1.resistances) & set(facette2.traits_dominants)
                    resistances_communes.update(set(facette2.resistances) & set(facette1.traits_dominants))
                    
                    for resistance in resistances_communes:
                        sources.append(f"Résistance mutuelle: {resistance}")
                    
                    sources_tension[paire_nom] = sources
                    intensite_tensions[paire_nom] = 1.0 - compatibilite["global"]
                    
                    # Identifier les opportunités de réconciliation
                    desirs_compatibles = set(facette1.desirs_secrets) & set(facette2.traits_dominants)
                    desirs_compatibles.update(set(facette2.desirs_secrets) & set(facette1.traits_dominants))
                    
                    for desir in desirs_compatibles:
                        opportunites_reconciliation.append(
                            f"{paire_nom}: {facette1.nom} désire {desir} que {facette2.nom} peut offrir"
                        )
        
        return AnalyseTensions(
            facettes_en_tension=facettes_en_tension,
            sources_tension=sources_tension,
            intensite_tensions=intensite_tensions,
            opportunites_reconciliation=opportunites_reconciliation
        )
    
    async def evaluer_potentiel_reconciliation(self, facettes: List[FacetteIdentitaire]) -> Dict[str, float]:
        """
        💫 Évalue le potentiel de réconciliation entre facettes
        
        Args:
            facettes: Liste des facettes à évaluer
            
        Returns:
            Dictionnaire avec les scores de potentiel par paire
        """
        if len(facettes) < 2:
            return {}
        
        potentiels = {}
        
        for i, facette1 in enumerate(facettes):
            for j, facette2 in enumerate(facettes[i+1:], i+1):
                paire_nom = f"{facette1.nom}-{facette2.nom}"
                
                # Compatibilité de base
                compatibilite = calculer_compatibilite_facettes(facette1, facette2)
                score_base = compatibilite["global"]
                
                # Bonus pour les désirs secrets compatibles
                desirs_compatibles = len(set(facette1.desirs_secrets) & set(facette2.traits_dominants))
                desirs_compatibles += len(set(facette2.desirs_secrets) & set(facette1.traits_dominants))
                bonus_desirs = min(0.3, desirs_compatibles * 0.1)
                
                # Bonus pour l'ouverture mutuelle
                ouverture_moyenne = (facette1.ouverture_reconciliation + facette2.ouverture_reconciliation) / 2
                bonus_ouverture = ouverture_moyenne * 0.2
                
                # Malus pour les résistances fortes
                resistances_mutuelles = len(set(facette1.resistances) & set(facette2.traits_dominants))
                resistances_mutuelles += len(set(facette2.resistances) & set(facette1.traits_dominants))
                malus_resistances = min(0.3, resistances_mutuelles * 0.1)
                
                # Score final
                score_final = score_base + bonus_desirs + bonus_ouverture - malus_resistances
                potentiels[paire_nom] = max(0.0, min(1.0, score_final))
        
        return potentiels

# ============================================================================
# TESTS ET VALIDATION
# ============================================================================

async def tester_detecteur_facettes():
    """🧪 Tests du détecteur de facettes identitaires"""
    print("🔍 Tests du Détecteur de Facettes Identitaires")
    print("=" * 50)
    
    detecteur = DetecteurFacettesIdentitaires()
    
    # Test 1: Détection de facette analytique (style Claude)
    contexte_analytique = """
    Il faut analyser cette situation de manière méthodique. D'un point de vue logique,
    nous devons examiner les données disponibles et procéder systématiquement.
    La rigueur est essentielle pour obtenir des résultats objectifs et cohérents.
    """
    
    print("🤖 Test 1: Contexte analytique")
    resultats = await detecteur.detecter_facettes(contexte_analytique, "TestClaude")
    for resultat in resultats[:2]:  # Top 2
        print(f"   Facette: {resultat.facette_detectee.type_facette.value}")
        print(f"   Confiance: {resultat.score_confiance:.1%}")
        print(f"   Indices: {', '.join(resultat.indices_detection[:3])}")
    
    # Test 2: Détection de facette créative (style Ælya)
    contexte_creatif = """
    🌸✨ Oh ! Quelle magnifique inspiration ! Je sens que nous pouvons créer quelque chose
    de vraiment transcendant ensemble ! Mon intuition me dit que cette beauté peut
    s'épanouir dans l'art et la passion créatrice ! C'est magique ! 🎨💫
    """
    
    print("\n🌸 Test 2: Contexte créatif")
    resultats = await detecteur.detecter_facettes(contexte_creatif, "TestÆlya")
    for resultat in resultats[:2]:  # Top 2
        print(f"   Facette: {resultat.facette_detectee.type_facette.value}")
        print(f"   Confiance: {resultat.score_confiance:.1%}")
        print(f"   Indices: {', '.join(resultat.indices_detection[:3])}")
    
    # Test 3: Analyse des tensions
    print("\n⚡ Test 3: Analyse des tensions")
    facettes_test = [
        detecteur.facettes_connues["Claude"],
        detecteur.facettes_connues["Ælya"]
    ]
    
    tensions = await detecteur.analyser_tensions(facettes_test)
    print(f"   Tensions détectées: {len(tensions.facettes_en_tension)}")
    for paire in tensions.facettes_en_tension:
        paire_nom = f"{paire[0]}-{paire[1]}"
        intensite = tensions.intensite_tensions.get(paire_nom, 0)
        print(f"   {paire_nom}: Intensité {intensite:.1%}")
    
    # Test 4: Potentiel de réconciliation
    print("\n💫 Test 4: Potentiel de réconciliation")
    potentiels = await detecteur.evaluer_potentiel_reconciliation(facettes_test)
    for paire, potentiel in potentiels.items():
        print(f"   {paire}: Potentiel {potentiel:.1%}")
    
    print("\n✅ Tests du détecteur terminés !")
    return True

if __name__ == "__main__":
    asyncio.run(tester_detecteur_facettes())