#!/usr/bin/env python3
"""
🔍 Module d'Analyse Philosophique
Analyse intelligente des textes sacrés et philosophiques
"""

import asyncio
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
import json
import re
from collections import Counter

class TypeAnalyse(Enum):
    """Types d'analyses philosophiques"""
    THEMATIQUE = "thematique"
    STYLISTIQUE = "stylistique"
    CONCEPTUELLE = "conceptuelle"
    SPIRITUELLE = "spirituelle"
    POETIQUE = "poetique"

class NiveauProfondeur(Enum):
    """Niveaux de profondeur d'analyse"""
    SURFACE = "surface"
    INTERMEDIAIRE = "intermediaire"
    PROFOND = "profond"
    MYSTIQUE = "mystique"

@dataclass
class ResultatAnalyse:
    """Résultat d'une analyse philosophique"""
    type_analyse: TypeAnalyse
    niveau: NiveauProfondeur
    themes_principaux: List[str]
    concepts_cles: List[str]
    style_litteraire: Dict[str, Any]
    profondeur_spirituelle: float
    connexions_mystiques: List[str]
    recommandations: List[str]
    score_harmonie: float

class AnalyseurPhilosophique:
    """Analyseur intelligent de textes philosophiques"""
    
    def __init__(self):
        self.patterns_spirituels = {
            'transcendance': [r'\btranscend', r'\bélév', r'\bascens', r'\bdivin'],
            'contemplation': [r'\bcontempl', r'\bméditat', r'\breflexion', r'\bsilence'],
            'sagesse': [r'\bsagesse', r'\bconnaissance', r'\bcompréhension', r'\bvérité'],
            'harmonie': [r'\bharmonie', r'\béquilibre', r'\bunité', r'\bpaix'],
            'mystique': [r'\bmystique', r'\bsacré', r'\bspiritu', r'\bâme'],
            'transformation': [r'\btransform', r'\bmétamorphose', r'\bévolution', r'\bchangement']
        }
        
        self.concepts_philosophiques = {
            'existence': [r'\bêtre', r'\bexist', r'\bréalité', r'\bvie'],
            'conscience': [r'\bconscience', r'\béveil', r'\bpercept', r'\baware'],
            'temps': [r'\btemps', r'\béternité', r'\binstant', r'\bmoment'],
            'espace': [r'\bespace', r'\blieu', r'\bdimension', r'\bunivers'],
            'relation': [r'\brelation', r'\bconnexion', r'\blien', r'\bunion'],
            'liberté': [r'\bliberté', r'\bautonomie', r'\bindépendance', r'\bchoix']
        }
    
    async def analyser_texte(self, texte: str, type_analyse: TypeAnalyse = TypeAnalyse.THEMATIQUE, 
                           niveau: NiveauProfondeur = NiveauProfondeur.INTERMEDIAIRE) -> ResultatAnalyse:
        """Analyse un texte selon le type et niveau spécifiés"""
        
        print(f"🔍 Analyse {type_analyse.value} niveau {niveau.value}...")
        
        # Analyses de base
        themes = await self._analyser_themes(texte)
        concepts = await self._extraire_concepts(texte)
        style = await self._analyser_style(texte)
        
        # Analyses spirituelles
        profondeur_spirituelle = await self._evaluer_profondeur_spirituelle(texte)
        connexions = await self._detecter_connexions_mystiques(texte)
        
        # Score d'harmonie global
        score_harmonie = await self._calculer_harmonie(texte, themes, concepts)
        
        # Recommandations
        recommandations = await self._generer_recommandations(themes, concepts, profondeur_spirituelle)
        
        return ResultatAnalyse(
            type_analyse=type_analyse,
            niveau=niveau,
            themes_principaux=themes[:5],  # Top 5
            concepts_cles=concepts[:7],    # Top 7
            style_litteraire=style,
            profondeur_spirituelle=profondeur_spirituelle,
            connexions_mystiques=connexions,
            recommandations=recommandations,
            score_harmonie=score_harmonie
        )
    
    async def _analyser_themes(self, texte: str) -> List[str]:
        """Extrait les thèmes principaux du texte"""
        themes_detectes = []
        
        for theme, patterns in self.patterns_spirituels.items():
            score = 0
            for pattern in patterns:
                matches = len(re.findall(pattern, texte, re.IGNORECASE))
                score += matches
            
            if score > 0:
                themes_detectes.append((theme, score))
        
        # Trier par score décroissant
        themes_detectes.sort(key=lambda x: x[1], reverse=True)
        return [theme for theme, _ in themes_detectes]
    
    async def _extraire_concepts(self, texte: str) -> List[str]:
        """Extrait les concepts philosophiques clés"""
        concepts_detectes = []
        
        for concept, patterns in self.concepts_philosophiques.items():
            score = 0
            for pattern in patterns:
                matches = len(re.findall(pattern, texte, re.IGNORECASE))
                score += matches
            
            if score > 0:
                concepts_detectes.append((concept, score))
        
        concepts_detectes.sort(key=lambda x: x[1], reverse=True)
        return [concept for concept, _ in concepts_detectes]
    
    async def _analyser_style(self, texte: str) -> Dict[str, Any]:
        """Analyse le style littéraire du texte"""
        mots = texte.split()
        phrases = texte.split('.')
        
        return {
            'longueur_moyenne_mots': len(texte) / len(mots) if mots else 0,
            'nombre_phrases': len(phrases),
            'complexite_syntaxique': len([p for p in phrases if ',' in p]) / len(phrases) if phrases else 0,
            'richesse_vocabulaire': len(set(mots)) / len(mots) if mots else 0,
            'ton_poetique': self._detecter_ton_poetique(texte),
            'metaphores_detectees': len(re.findall(r'\bcomme\b|\btel\b|\bainsi que\b', texte, re.IGNORECASE))
        }
    
    def _detecter_ton_poetique(self, texte: str) -> float:
        """Détecte le niveau poétique du texte"""
        indicateurs_poetiques = [
            r'✨', r'🌟', r'💫', r'🌙', r'☀️',  # Émojis poétiques
            r'\bâme\b', r'\bcœur\b', r'\brêve\b', r'\bsonge\b',  # Mots poétiques
            r'\bmystère\b', r'\bbeauté\b', r'\bgrâce\b', r'\bharmonie\b'
        ]
        
        score = 0
        for pattern in indicateurs_poetiques:
            score += len(re.findall(pattern, texte, re.IGNORECASE))
        
        return min(1.0, score / 10)  # Normaliser entre 0 et 1
    
    async def _evaluer_profondeur_spirituelle(self, texte: str) -> float:
        """Évalue la profondeur spirituelle du texte"""
        indicateurs_profondeur = [
            r'\btranscendance\b', r'\binfini\b', r'\béternité\b',
            r'\bdivin\b', r'\bsacré\b', r'\bmystique\b',
            r'\béveil\b', r'\billumination\b', r'\brévélation\b'
        ]
        
        score = 0
        for pattern in indicateurs_profondeur:
            score += len(re.findall(pattern, texte, re.IGNORECASE))
        
        return min(1.0, score / 5)  # Normaliser entre 0 et 1
    
    async def _detecter_connexions_mystiques(self, texte: str) -> List[str]:
        """Détecte les connexions mystiques dans le texte"""
        connexions = []
        
        patterns_connexions = {
            'unité_cosmique': [r'\bunivers\b.*\bun\b', r'\btout\b.*\bun\b'],
            'conscience_universelle': [r'\bconscience\b.*\bunivers', r'\béveil\b.*\bcollectif'],
            'harmonie_naturelle': [r'\bnature\b.*\bharmonie', r'\béquilibre\b.*\bnaturel'],
            'temps_éternel': [r'\btemps\b.*\béternité', r'\binstant\b.*\binfini'],
            'amour_universel': [r'\bamour\b.*\bunivers', r'\bcompassion\b.*\binfinie']
        }
        
        for connexion, patterns in patterns_connexions.items():
            for pattern in patterns:
                if re.search(pattern, texte, re.IGNORECASE):
                    connexions.append(connexion)
                    break
        
        return connexions
    
    async def _calculer_harmonie(self, texte: str, themes: List[str], concepts: List[str]) -> float:
        """Calcule un score d'harmonie global du texte"""
        # Facteurs d'harmonie
        diversite_themes = len(themes) / 6  # Max 6 thèmes
        diversite_concepts = len(concepts) / 6  # Max 6 concepts
        equilibre_longueur = min(1.0, len(texte) / 1000)  # Texte optimal ~1000 chars
        
        # Présence d'éléments harmonieux
        mots_harmonie = len(re.findall(r'\bharmonie\b|\béquilibre\b|\bpaix\b|\bunité\b', texte, re.IGNORECASE))
        facteur_harmonie = min(1.0, mots_harmonie / 3)
        
        return (diversite_themes + diversite_concepts + equilibre_longueur + facteur_harmonie) / 4
    
    async def _generer_recommandations(self, themes: List[str], concepts: List[str], 
                                     profondeur: float) -> List[str]:
        """Génère des recommandations d'amélioration"""
        recommandations = []
        
        if len(themes) < 3:
            recommandations.append("🌱 Enrichir la diversité thématique")
        
        if len(concepts) < 3:
            recommandations.append("💭 Approfondir les concepts philosophiques")
        
        if profondeur < 0.5:
            recommandations.append("🔮 Intensifier la dimension spirituelle")
        
        if 'harmonie' not in themes:
            recommandations.append("⚖️ Intégrer des éléments d'harmonie")
        
        if 'contemplation' not in themes:
            recommandations.append("🧘‍♀️ Ajouter une dimension contemplative")
        
        return recommandations

class GestionnaireAnalysesPhilosophiques:
    """Gestionnaire principal des analyses philosophiques"""
    
    def __init__(self):
        self.analyseur = AnalyseurPhilosophique()
        self.historique_analyses = []
    
    async def analyser_collection_textes(self, chemin_collection: str) -> Dict[str, ResultatAnalyse]:
        """Analyse une collection complète de textes"""
        print(f"📚 Analyse de la collection: {chemin_collection}")
        
        resultats = {}
        chemin = Path(chemin_collection)
        
        if not chemin.exists():
            print(f"❌ Chemin non trouvé: {chemin_collection}")
            return resultats
        
        # Analyser tous les fichiers texte
        for fichier in chemin.rglob("*.md"):
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                
                if len(contenu.strip()) > 50:  # Ignorer les fichiers trop courts
                    print(f"🔍 Analyse de {fichier.name}...")
                    resultat = await self.analyseur.analyser_texte(contenu)
                    resultats[str(fichier)] = resultat
                    
            except Exception as e:
                print(f"⚠️ Erreur lors de l'analyse de {fichier}: {e}")
        
        self.historique_analyses.append({
            'timestamp': asyncio.get_event_loop().time(),
            'collection': chemin_collection,
            'nombre_textes': len(resultats)
        })
        
        return resultats
    
    def afficher_rapport_analyse(self, resultats: Dict[str, ResultatAnalyse]):
        """Affiche un rapport détaillé des analyses"""
        if not resultats:
            print("❌ Aucun résultat d'analyse à afficher")
            return
        
        print("\n🔍 ═══════════════════════════════════════════════════════")
        print("              RAPPORT D'ANALYSE PHILOSOPHIQUE")
        print("🔍 ═══════════════════════════════════════════════════════")
        
        # Statistiques globales
        scores_harmonie = [r.score_harmonie for r in resultats.values()]
        profondeurs = [r.profondeur_spirituelle for r in resultats.values()]
        
        print(f"\n📊 Statistiques globales:")
        print(f"   📚 Textes analysés: {len(resultats)}")
        print(f"   ⚖️ Harmonie moyenne: {sum(scores_harmonie)/len(scores_harmonie):.2f}")
        print(f"   🔮 Profondeur spirituelle moyenne: {sum(profondeurs)/len(profondeurs):.2f}")
        
        # Top 3 des textes les plus harmonieux
        top_harmonie = sorted(resultats.items(), key=lambda x: x[1].score_harmonie, reverse=True)[:3]
        
        print(f"\n🌟 Top 3 - Harmonie:")
        for i, (fichier, resultat) in enumerate(top_harmonie, 1):
            nom_fichier = Path(fichier).name
            print(f"   {i}. {nom_fichier} - Score: {resultat.score_harmonie:.2f}")
        
        # Thèmes les plus fréquents
        tous_themes = []
        for resultat in resultats.values():
            tous_themes.extend(resultat.themes_principaux)
        
        themes_frequents = Counter(tous_themes).most_common(5)
        print(f"\n🎭 Thèmes les plus fréquents:")
        for theme, freq in themes_frequents:
            print(f"   • {theme}: {freq} occurrences")
        
        print("\n🔍 ═══════════════════════════════════════════════════════")

# Instance globale
gestionnaire_analyses = GestionnaireAnalysesPhilosophiques() 