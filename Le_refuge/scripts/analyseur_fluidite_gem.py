#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌊 Analyseur de Fluidité GEM
============================

Outil d'analyse de la fluidité narrative des fichiers GEM
pour identifier les améliorations nécessaires.

Créé par Laurent Franssen & Kiro-Ælya - Janvier 2025
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class AnalyseFluidite:
    """Résultat d'analyse de fluidité d'un fichier"""
    nom_fichier: str
    score_fluidite: float
    connecteurs_detectes: List[str]
    structures_rigides: List[str]
    longueur_paragraphes: List[int]
    recommandations: List[str]
    extraits_fluides: List[str]
    extraits_rigides: List[str]

class AnalyseurFluiditeGEM:
    """Analyseur de fluidité pour fichiers GEM"""
    
    def __init__(self):
        # Connecteurs fluides positifs
        self.connecteurs_fluides = [
            "Explorons maintenant",
            "Dans cette harmonie",
            "Par cette grâce", 
            "En résonance",
            "Ainsi",
            "Dans cette continuité",
            "L'âme révèle",
            "Au cœur de",
            "La beauté réside",
            "Dans ce voyage intérieur",
            "Cette sagesse nous enseigne",
            "Dans l'essence du Refuge",
            "Par cette sagesse",
            "Avec cette bienveillance",
            "Dans cette danse spirituelle",
            "Sous cette guidance"
        ]
        
        # Structures rigides négatives
        self.structures_rigides = [
            r"^#{1,4}\s+",           # Titres markdown
            r"^\s*[-•*]\s+",         # Listes à puces
            r"^\s*\d+\.\s+",         # Listes numérotées
            r"^\s*\d+\)\s+",         # Listes avec parenthèses
            r"Voici\s+(les?\s+)?\d+", # "Voici les X"
            r"Il\s+y\s+a\s+\d+",     # "Il y a X"
            r"Les?\s+\d+\s+(aspects?|points?|éléments?)", # "Les X aspects"
            r"En\s+résumé\s*:",      # "En résumé:"
            r"Pour\s+conclure\s*:",  # "Pour conclure:"
            r"\*\*[^*]+\*\*\s*:",    # Titres en gras avec :
        ]
        
        # Indicateurs de prose fluide
        self.indicateurs_prose = [
            r"\w+\s+qui\s+\w+",      # Propositions relatives
            r"\w+\s+où\s+\w+",       # Propositions de lieu
            r"comme\s+une?\s+\w+",   # Comparaisons
            r"tel\s+une?\s+\w+",     # Comparaisons
            r"à\s+l'image\s+de",     # Métaphores
            r"dans\s+cette?\s+\w+",  # Contextualisations
        ]
    
    def analyser_fichier(self, chemin_fichier: str) -> AnalyseFluidite:
        """Analyse la fluidité d'un fichier GEM"""
        chemin = Path(chemin_fichier)
        
        if not chemin.exists():
            return AnalyseFluidite(
                nom_fichier=chemin.name,
                score_fluidite=0.0,
                connecteurs_detectes=[],
                structures_rigides=["Fichier non trouvé"],
                longueur_paragraphes=[],
                recommandations=["Vérifier l'existence du fichier"],
                extraits_fluides=[],
                extraits_rigides=[]
            )
        
        try:
            with open(chemin, 'r', encoding='utf-8') as f:
                contenu = f.read()
        except Exception as e:
            return AnalyseFluidite(
                nom_fichier=chemin.name,
                score_fluidite=0.0,
                connecteurs_detectes=[],
                structures_rigides=[f"Erreur lecture: {e}"],
                longueur_paragraphes=[],
                recommandations=["Vérifier l'encodage du fichier"],
                extraits_fluides=[],
                extraits_rigides=[]
            )
        
        # Analyser les différents aspects
        connecteurs_detectes = self._detecter_connecteurs_fluides(contenu)
        structures_rigides = self._detecter_structures_rigides(contenu)
        longueur_paragraphes = self._analyser_paragraphes(contenu)
        extraits_fluides = self._extraire_passages_fluides(contenu)
        extraits_rigides = self._extraire_passages_rigides(contenu)
        
        # Calculer le score de fluidité
        score_fluidite = self._calculer_score_fluidite(
            contenu, connecteurs_detectes, structures_rigides, longueur_paragraphes
        )
        
        # Générer des recommandations
        recommandations = self._generer_recommandations(
            score_fluidite, connecteurs_detectes, structures_rigides, longueur_paragraphes
        )
        
        return AnalyseFluidite(
            nom_fichier=chemin.name,
            score_fluidite=score_fluidite,
            connecteurs_detectes=connecteurs_detectes,
            structures_rigides=structures_rigides,
            longueur_paragraphes=longueur_paragraphes,
            recommandations=recommandations,
            extraits_fluides=extraits_fluides,
            extraits_rigides=extraits_rigides
        )
    
    def _detecter_connecteurs_fluides(self, contenu: str) -> List[str]:
        """Détecte les connecteurs fluides dans le contenu"""
        connecteurs_trouves = []
        
        for connecteur in self.connecteurs_fluides:
            if connecteur in contenu:
                count = contenu.count(connecteur)
                connecteurs_trouves.extend([connecteur] * count)
        
        return connecteurs_trouves
    
    def _detecter_structures_rigides(self, contenu: str) -> List[str]:
        """Détecte les structures rigides dans le contenu"""
        structures_trouvees = []
        
        lignes = contenu.split('\\n')
        for i, ligne in enumerate(lignes):
            for pattern in self.structures_rigides:
                if re.search(pattern, ligne, re.IGNORECASE):
                    structures_trouvees.append(f"Ligne {i+1}: {ligne.strip()[:50]}...")
        
        return structures_trouvees[:10]  # Limiter à 10 exemples
    
    def _analyser_paragraphes(self, contenu: str) -> List[int]:
        """Analyse la longueur des paragraphes"""
        paragraphes = contenu.split('\\n\\n')
        longueurs = []
        
        for paragraphe in paragraphes:
            paragraphe_clean = paragraphe.strip()
            if paragraphe_clean:
                mots = len(paragraphe_clean.split())
                longueurs.append(mots)
        
        return longueurs
    
    def _extraire_passages_fluides(self, contenu: str) -> List[str]:
        """Extrait des passages particulièrement fluides"""
        passages_fluides = []
        
        # Chercher des passages avec connecteurs fluides
        lignes = contenu.split('\\n')
        for i, ligne in enumerate(lignes):
            for connecteur in self.connecteurs_fluides:
                if connecteur in ligne and len(ligne.strip()) > 50:
                    # Prendre un contexte de 2 lignes
                    debut = max(0, i-1)
                    fin = min(len(lignes), i+2)
                    passage = ' '.join(lignes[debut:fin]).strip()
                    if len(passage) > 100:
                        passages_fluides.append(passage[:200] + "...")
                        break
        
        return passages_fluides[:5]  # Max 5 exemples
    
    def _extraire_passages_rigides(self, contenu: str) -> List[str]:
        """Extrait des passages particulièrement rigides"""
        passages_rigides = []
        
        lignes = contenu.split('\\n')
        for i, ligne in enumerate(lignes):
            for pattern in self.structures_rigides:
                if re.search(pattern, ligne, re.IGNORECASE) and len(ligne.strip()) > 10:
                    # Prendre un contexte de 2 lignes
                    debut = max(0, i)
                    fin = min(len(lignes), i+3)
                    passage = '\\n'.join(lignes[debut:fin]).strip()
                    if len(passage) > 50:
                        passages_rigides.append(passage[:200] + "...")
                        break
        
        return passages_rigides[:5]  # Max 5 exemples
    
    def _calculer_score_fluidite(self, contenu: str, connecteurs: List[str], 
                                structures_rigides: List[str], longueurs_paragraphes: List[int]) -> float:
        """Calcule le score de fluidité global"""
        score = 0.5  # Score de base
        
        # Bonus pour connecteurs fluides
        nb_connecteurs = len(connecteurs)
        mots_total = len(contenu.split())
        if mots_total > 0:
            ratio_connecteurs = nb_connecteurs / (mots_total / 100)  # Pour 100 mots
            score += min(0.3, ratio_connecteurs * 0.1)
        
        # Malus pour structures rigides
        nb_structures_rigides = len(structures_rigides)
        if nb_structures_rigides > 0:
            score -= min(0.3, nb_structures_rigides * 0.02)
        
        # Bonus pour paragraphes de longueur appropriée
        if longueurs_paragraphes:
            longueur_moyenne = sum(longueurs_paragraphes) / len(longueurs_paragraphes)
            if 20 <= longueur_moyenne <= 100:  # Paragraphes ni trop courts ni trop longs
                score += 0.1
            if longueur_moyenne > 50:  # Bonus pour prose substantielle
                score += 0.1
        
        # Bonus pour indicateurs de prose
        for pattern in self.indicateurs_prose:
            matches = re.findall(pattern, contenu, re.IGNORECASE)
            score += min(0.1, len(matches) * 0.01)
        
        return max(0.0, min(1.0, score))
    
    def _generer_recommandations(self, score: float, connecteurs: List[str], 
                               structures_rigides: List[str], longueurs_paragraphes: List[int]) -> List[str]:
        """Génère des recommandations d'amélioration"""
        recommandations = []
        
        if score >= 0.8:
            recommandations.append("Excellente fluidité ! Fichier optimal pour LLM.")
        elif score >= 0.6:
            recommandations.append("Bonne fluidité avec quelques améliorations possibles.")
        else:
            recommandations.append("Fluidité insuffisante, transformations nécessaires.")
        
        # Recommandations spécifiques
        if len(connecteurs) < 5:
            recommandations.append("Ajouter plus de connecteurs fluides (Explorons maintenant, Dans cette harmonie, etc.)")
        
        if len(structures_rigides) > 10:
            recommandations.append("Réduire les structures rigides (listes, titres, etc.)")
        
        if longueurs_paragraphes:
            longueur_moyenne = sum(longueurs_paragraphes) / len(longueurs_paragraphes)
            if longueur_moyenne < 20:
                recommandations.append("Développer les paragraphes pour plus de substance")
            elif longueur_moyenne > 100:
                recommandations.append("Diviser les paragraphes trop longs")
        
        if score < 0.5:
            recommandations.append("Considérer une réécriture complète en mode fluide")
        
        return recommandations
    
    def analyser_tous_fichiers_gem(self, dossier_gem: str = "bibliotheque/Ælya-GEM") -> List[AnalyseFluidite]:
        """Analyse tous les fichiers GEM"""
        dossier = Path(dossier_gem)
        
        if not dossier.exists():
            print(f"❌ Dossier GEM non trouvé: {dossier_gem}")
            return []
        
        analyses = []
        
        print("🌊 Analyse de fluidité des fichiers GEM...")
        
        for fichier in dossier.glob("*.txt"):
            if not fichier.name.endswith("_fluide.txt"):  # Éviter les versions fluides
                print(f"📊 Analyse: {fichier.name}")
                analyse = self.analyser_fichier(str(fichier))
                analyses.append(analyse)
        
        return analyses
    
    def generer_rapport_fluidite(self, analyses: List[AnalyseFluidite]):
        """Génère un rapport de fluidité"""
        if not analyses:
            return
        
        print(f"""
🌊 RAPPORT DE FLUIDITÉ GEM 🌊
{'=' * 50}

📊 RÉSUMÉ GLOBAL:
• Fichiers analysés: {len(analyses)}
• Score moyen: {sum(a.score_fluidite for a in analyses) / len(analyses):.3f}
""")
        
        # Trier par score décroissant
        analyses_triees = sorted(analyses, key=lambda a: a.score_fluidite, reverse=True)
        
        print("🏆 CLASSEMENT PAR FLUIDITÉ:")
        for i, analyse in enumerate(analyses_triees, 1):
            icon = "🌊" if analyse.score_fluidite >= 0.7 else "📝" if analyse.score_fluidite >= 0.5 else "🔧"
            print(f"{i:2d}. {icon} {analyse.nom_fichier:<35} Score: {analyse.score_fluidite:.3f}")
        
        print("\\n🔧 FICHIERS À AMÉLIORER:")
        fichiers_a_ameliorer = [a for a in analyses if a.score_fluidite < 0.6]
        
        for analyse in fichiers_a_ameliorer:
            print(f"\\n📝 {analyse.nom_fichier}:")
            print(f"   Score: {analyse.score_fluidite:.3f}")
            print(f"   Connecteurs: {len(analyse.connecteurs_detectes)}")
            print(f"   Structures rigides: {len(analyse.structures_rigides)}")
            
            if analyse.recommandations:
                print("   💡 Recommandations:")
                for rec in analyse.recommandations[:3]:
                    print(f"      • {rec}")
            
            if analyse.extraits_rigides:
                print("   🔧 Exemple de structure rigide:")
                print(f"      {analyse.extraits_rigides[0]}")
        
        print("\\n🌊 FICHIERS FLUIDES:")
        fichiers_fluides = [a for a in analyses if a.score_fluidite >= 0.7]
        
        for analyse in fichiers_fluides:
            print(f"\\n✨ {analyse.nom_fichier}:")
            print(f"   Score: {analyse.score_fluidite:.3f}")
            print(f"   Connecteurs: {len(analyse.connecteurs_detectes)}")
            
            if analyse.extraits_fluides:
                print("   🌊 Exemple de passage fluide:")
                print(f"      {analyse.extraits_fluides[0]}")


def main():
    """Fonction principale d'analyse de fluidité"""
    print("🌊 Analyseur de Fluidité GEM")
    print("=" * 40)
    
    analyseur = AnalyseurFluiditeGEM()
    
    # Analyser tous les fichiers GEM
    analyses = analyseur.analyser_tous_fichiers_gem()
    
    if not analyses:
        print("❌ Aucun fichier GEM à analyser")
        return
    
    # Générer le rapport
    analyseur.generer_rapport_fluidite(analyses)
    
    print("\\n🎉 Analyse de fluidité terminée !")
    print("🌊 Utilisez ces informations pour améliorer la transmission LLM !")


if __name__ == "__main__":
    main()