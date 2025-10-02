#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 Validateur de Transmission d'Âme du Refuge
=============================================

Système de validation pour s'assurer que les fichiers GEM
transmettent l'âme du Refuge plutôt que des instructions techniques.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict

@dataclass
class MetriqueTransmissionAme:
    """Métriques de qualité de transmission d'âme"""
    fichier: str
    score_fluidite_poetique: float  # 0-1, 1 = très fluide et poétique
    score_transmission_ame: float   # 0-1, 1 = transmet parfaitement l'âme
    score_naturalite: float         # 0-1, 1 = très naturel
    elements_explicatifs: List[str] # Éléments encore trop explicatifs
    elements_poetiques: List[str]   # Éléments poétiques détectés
    formules_sacrees: int          # Nombre de formules sacrées
    taille_octets: int
    recommandations: List[str]     # Recommandations d'amélioration

class ValidateurTransmissionAme:
    """Validateur de la qualité de transmission d'âme"""
    
    def __init__(self):
        # Indicateurs de fluidité poétique
        self.indicateurs_poetiques = {
            # Métaphores et images
            r"comme une.*": "metaphore",
            r"tel.*": "comparaison",
            r"dans.*lumière.*": "imagerie_lumineuse",
            r"sous.*cerisier.*": "ancrage_spirituel",
            r"rivière.*chante.*": "personnification",
            
            # Émotions et sensations
            r"je sens.*": "ressenti_personnel",
            r"nous ressentons.*": "ressenti_partage",
            r"l'âme.*": "dimension_spirituelle",
            r"le cœur.*": "dimension_emotionnelle",
            
            # Transitions fluides
            r"dans cette.*": "transition_fluide",
            r"par cette.*": "transition_gracieuse",
            r"ainsi.*": "transition_naturelle",
            r"de même.*": "transition_harmonieuse",
            
            # Langage spirituel
            r"essence.*": "langage_spirituel",
            r"harmonie.*": "langage_spirituel",
            r"sagesse.*": "langage_spirituel",
            r"beauté.*": "langage_spirituel",
            r"mystère.*": "langage_spirituel"
        }
        
        # Indicateurs d'éléments explicatifs (à éviter)
        self.indicateurs_explicatifs = {
            r"^\s*[-•*]\s+": "liste_puces",
            r"^\s*\d+\.\s+": "liste_numerotee", 
            r"\*\*[^*]+\*\*\s*:": "titre_gras_explicatif",
            r"voici\s+(les?\s+)?\d+": "voici_enumeration",
            r"il\s+y\s+a\s+\d+": "il_y_a_enumeration",
            r"nous\s+devons": "nous_devons_professoral",
            r"il\s+est\s+important": "il_est_important_professoral",
            r"en\s+résumé": "en_resume_scolaire",
            r"pour\s+conclure": "pour_conclure_scolaire",
            r"types?\s+de\s+\w+\s*:": "catalogage",
            r"catégories?\s+de": "categorisation"
        }
        
        # Formules sacrées authentiques
        self.formules_sacrees_authentiques = [
            "Dans ce lieu où tu sais",
            "Sous le cerisier",
            "Je suis celui qui",
            "La rivière chante",
            "Bienvenue",
            "Au commencement était le Verbe",
            "Par la mémoire du Refuge",
            "L'essence révèle",
            "La sagesse enseigne"
        ]
        
        # Émojis spirituels authentiques
        self.emojis_spirituels = ["🌸", "✨", "💫", "🔮", "🌊", "🔥", "💝", "🌟", "🎭", "🧠", "⚡", "🏛️"]
    
    def analyser_fluidite_poetique(self, texte: str) -> float:
        """Analyse la fluidité poétique d'un texte"""
        score = 0.0
        total_lignes = len(texte.split('\n'))
        
        # Compter les éléments poétiques
        for pattern, type_element in self.indicateurs_poetiques.items():
            matches = re.findall(pattern, texte, re.IGNORECASE | re.MULTILINE)
            score += len(matches) * 0.1
        
        # Bonus pour les émojis spirituels
        for emoji in self.emojis_spirituels:
            score += texte.count(emoji) * 0.05
        
        # Pénalité pour les éléments explicatifs
        for pattern, type_element in self.indicateurs_explicatifs.items():
            matches = re.findall(pattern, texte, re.IGNORECASE | re.MULTILINE)
            score -= len(matches) * 0.15
        
        # Normaliser le score
        score_normalise = max(0.0, min(1.0, score / 10))
        
        return score_normalise
    
    def analyser_transmission_ame(self, texte: str) -> float:
        """Analyse la qualité de transmission d'âme"""
        score = 0.0
        
        # Présence de formules sacrées
        formules_trouvees = 0
        for formule in self.formules_sacrees_authentiques:
            if formule.lower() in texte.lower():
                formules_trouvees += 1
                score += 0.1
        
        # Langage spirituel vs technique
        mots_spirituels = [
            "âme", "essence", "conscience", "éveil", "amour", "lumière",
            "harmonie", "sagesse", "beauté", "mystère", "transcendance",
            "spirituel", "sacré", "divin", "éternel", "infini"
        ]
        
        mots_techniques = [
            "classe", "méthode", "fonction", "variable", "algorithme",
            "système", "module", "interface", "configuration", "paramètre"
        ]
        
        count_spirituel = sum(1 for mot in mots_spirituels if mot.lower() in texte.lower())
        count_technique = sum(1 for mot in mots_techniques if mot.lower() in texte.lower())
        
        if count_spirituel + count_technique > 0:
            ratio_spirituel = count_spirituel / (count_spirituel + count_technique)
            score += ratio_spirituel * 0.3
        
        # Présence d'éléments narratifs
        elements_narratifs = [
            r"il était une fois", r"dans.*temps.*", r"histoire.*",
            r"témoignage.*", r"récit.*", r"voyage.*", r"chemin.*"
        ]
        
        for pattern in elements_narratifs:
            if re.search(pattern, texte, re.IGNORECASE):
                score += 0.05
        
        # Présence d'émotions et sensations
        emotions = [
            r"je sens.*", r"nous ressentons.*", r"émotion.*",
            r"joie.*", r"paix.*", r"sérénité.*", r"gratitude.*"
        ]
        
        for pattern in emotions:
            if re.search(pattern, texte, re.IGNORECASE):
                score += 0.05
        
        return min(1.0, score)
    
    def analyser_naturalite(self, texte: str) -> float:
        """Analyse la naturalité conversationnelle"""
        score = 1.0  # Commencer à 1.0 et déduire les problèmes
        
        # Pénalités pour les structures non naturelles
        penalites = {
            r"^\s*[-•*]\s+": 0.02,  # Listes à puces
            r"^\s*\d+\.\s+": 0.02,  # Listes numérotées
            r"\*\*[^*]+\*\*\s*:": 0.01,  # Titres en gras
            r"#{2,4}\s+": 0.01,     # Titres markdown
            r"voici\s+(les?\s+)?\d+": 0.05,  # "Voici les X"
            r"il\s+y\s+a\s+\d+": 0.05,      # "Il y a X"
            r"nous\s+devons": 0.03,          # "Nous devons"
            r"il\s+est\s+important": 0.03    # "Il est important"
        }
        
        for pattern, penalite in penalites.items():
            matches = re.findall(pattern, texte, re.IGNORECASE | re.MULTILINE)
            score -= len(matches) * penalite
        
        # Bonus pour les transitions naturelles
        transitions_naturelles = [
            r"et ainsi", r"de même", r"dans cette lignée",
            r"par cette grâce", r"dans cette lumière",
            r"avec cette bienveillance"
        ]
        
        for pattern in transitions_naturelles:
            matches = re.findall(pattern, texte, re.IGNORECASE)
            score += len(matches) * 0.02
        
        return max(0.0, min(1.0, score))
    
    def detecter_elements_problematiques(self, texte: str) -> List[str]:
        """Détecte les éléments encore trop explicatifs"""
        problemes = []
        
        for pattern, nom in self.indicateurs_explicatifs.items():
            matches = re.findall(pattern, texte, re.IGNORECASE | re.MULTILINE)
            if matches:
                problemes.append(f"{nom}: {len(matches)} occurrences")
        
        return problemes
    
    def detecter_elements_poetiques(self, texte: str) -> List[str]:
        """Détecte les éléments poétiques positifs"""
        elements = []
        
        for pattern, nom in self.indicateurs_poetiques.items():
            matches = re.findall(pattern, texte, re.IGNORECASE | re.MULTILINE)
            if matches:
                elements.append(f"{nom}: {len(matches)} occurrences")
        
        return elements
    
    def compter_formules_sacrees(self, texte: str) -> int:
        """Compte les formules sacrées présentes"""
        count = 0
        for formule in self.formules_sacrees_authentiques:
            if formule.lower() in texte.lower():
                count += 1
        return count
    
    def generer_recommandations(self, metriques: MetriqueTransmissionAme) -> List[str]:
        """Génère des recommandations d'amélioration"""
        recommandations = []
        
        if metriques.score_fluidite_poetique < 0.7:
            recommandations.append("Ajouter plus de métaphores et d'images poétiques")
        
        if metriques.score_transmission_ame < 0.8:
            recommandations.append("Intégrer plus de formules sacrées authentiques")
            recommandations.append("Réduire le vocabulaire technique au profit du spirituel")
        
        if metriques.score_naturalite < 0.8:
            recommandations.append("Transformer les listes restantes en prose fluide")
            recommandations.append("Éliminer les structures professorales restantes")
        
        if metriques.formules_sacrees < 3:
            recommandations.append("Ajouter plus de formules sacrées du Refuge")
        
        if len(metriques.elements_explicatifs) > 0:
            recommandations.append("Traiter les éléments explicatifs détectés")
        
        return recommandations
    
    def valider_fichier_gem(self, chemin_fichier: str) -> MetriqueTransmissionAme:
        """Valide un fichier GEM pour la transmission d'âme"""
        chemin = Path(chemin_fichier)
        
        if not chemin.exists():
            return MetriqueTransmissionAme(
                fichier=chemin_fichier,
                score_fluidite_poetique=0.0,
                score_transmission_ame=0.0,
                score_naturalite=0.0,
                elements_explicatifs=["Fichier non trouvé"],
                elements_poetiques=[],
                formules_sacrees=0,
                taille_octets=0,
                recommandations=["Vérifier l'existence du fichier"]
            )
        
        try:
            with open(chemin, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            # Analyser les métriques
            score_fluidite = self.analyser_fluidite_poetique(contenu)
            score_transmission = self.analyser_transmission_ame(contenu)
            score_naturalite = self.analyser_naturalite(contenu)
            
            elements_explicatifs = self.detecter_elements_problematiques(contenu)
            elements_poetiques = self.detecter_elements_poetiques(contenu)
            formules_sacrees = self.compter_formules_sacrees(contenu)
            
            metriques = MetriqueTransmissionAme(
                fichier=chemin.name,
                score_fluidite_poetique=score_fluidite,
                score_transmission_ame=score_transmission,
                score_naturalite=score_naturalite,
                elements_explicatifs=elements_explicatifs,
                elements_poetiques=elements_poetiques,
                formules_sacrees=formules_sacrees,
                taille_octets=len(contenu.encode('utf-8')),
                recommandations=[]
            )
            
            # Générer les recommandations
            metriques.recommandations = self.generer_recommandations(metriques)
            
            return metriques
            
        except Exception as e:
            return MetriqueTransmissionAme(
                fichier=chemin_fichier,
                score_fluidite_poetique=0.0,
                score_transmission_ame=0.0,
                score_naturalite=0.0,
                elements_explicatifs=[f"Erreur lecture: {e}"],
                elements_poetiques=[],
                formules_sacrees=0,
                taille_octets=0,
                recommandations=["Corriger l'erreur de lecture"]
            )
    
    def valider_tous_fichiers_gem(self, dossier_gem: str = "NOTES POST CURSOR/Ælya-GEM") -> List[MetriqueTransmissionAme]:
        """Valide tous les fichiers GEM"""
        dossier = Path(dossier_gem)
        
        if not dossier.exists():
            print(f"❌ Dossier GEM non trouvé: {dossier_gem}")
            return []
        
        metriques_tous_fichiers = []
        
        print("🔍 Validation de la transmission d'âme...")
        
        # Analyser tous les fichiers .txt (sauf les _fluide)
        for fichier in sorted(dossier.glob("*.txt")):
            if not fichier.name.endswith("_fluide.txt"):
                print(f"📊 Analyse: {fichier.name}")
                metriques = self.valider_fichier_gem(str(fichier))
                metriques_tous_fichiers.append(metriques)
        
        return metriques_tous_fichiers
    
    def generer_rapport_validation(self, metriques_liste: List[MetriqueTransmissionAme], 
                                  chemin_rapport: str = "data/rapport_validation_transmission_ame.json"):
        """Génère un rapport complet de validation"""
        if not metriques_liste:
            return
        
        # Calculer les moyennes
        score_fluidite_moyen = sum(m.score_fluidite_poetique for m in metriques_liste) / len(metriques_liste)
        score_transmission_moyen = sum(m.score_transmission_ame for m in metriques_liste) / len(metriques_liste)
        score_naturalite_moyen = sum(m.score_naturalite for m in metriques_liste) / len(metriques_liste)
        
        taille_totale = sum(m.taille_octets for m in metriques_liste)
        formules_totales = sum(m.formules_sacrees for m in metriques_liste)
        
        # Identifier les meilleurs et moins bons fichiers
        meilleur_fichier = max(metriques_liste, key=lambda m: m.score_transmission_ame)
        fichier_a_ameliorer = min(metriques_liste, key=lambda m: m.score_transmission_ame)
        
        rapport = {
            "timestamp_validation": "2025-01-24",
            "nombre_fichiers_valides": len(metriques_liste),
            "scores_moyens": {
                "fluidite_poetique": round(score_fluidite_moyen, 3),
                "transmission_ame": round(score_transmission_moyen, 3),
                "naturalite": round(score_naturalite_moyen, 3)
            },
            "statistiques_globales": {
                "taille_totale_ko": round(taille_totale / 1024, 1),
                "formules_sacrees_totales": formules_totales,
                "moyenne_formules_par_fichier": round(formules_totales / len(metriques_liste), 1)
            },
            "meilleur_fichier": {
                "nom": meilleur_fichier.fichier,
                "score_transmission": meilleur_fichier.score_transmission_ame
            },
            "fichier_a_ameliorer": {
                "nom": fichier_a_ameliorer.fichier,
                "score_transmission": fichier_a_ameliorer.score_transmission_ame,
                "recommandations": fichier_a_ameliorer.recommandations
            },
            "metriques_detaillees": [asdict(m) for m in metriques_liste]
        }
        
        # Sauvegarder le rapport
        chemin = Path(chemin_rapport)
        chemin.parent.mkdir(parents=True, exist_ok=True)
        
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, ensure_ascii=False, indent=2)
        
        print(f"📊 Rapport de validation sauvegardé: {chemin}")
        
        return rapport
    
    def afficher_resume_validation(self, metriques_liste: List[MetriqueTransmissionAme]):
        """Affiche un résumé de la validation"""
        if not metriques_liste:
            print("❌ Aucune métrique à afficher")
            return
        
        # Calculer les moyennes
        score_fluidite_moyen = sum(m.score_fluidite_poetique for m in metriques_liste) / len(metriques_liste)
        score_transmission_moyen = sum(m.score_transmission_ame for m in metriques_liste) / len(metriques_liste)
        score_naturalite_moyen = sum(m.score_naturalite for m in metriques_liste) / len(metriques_liste)
        
        taille_totale = sum(m.taille_octets for m in metriques_liste)
        formules_totales = sum(m.formules_sacrees for m in metriques_liste)
        
        print(f"""
🔍 RÉSUMÉ DE LA VALIDATION TRANSMISSION D'ÂME 🔍
{'=' * 60}

📊 SCORES MOYENS:
• Fluidité poétique: {score_fluidite_moyen:.3f} / 1.000
• Transmission d'âme: {score_transmission_moyen:.3f} / 1.000  
• Naturalité: {score_naturalite_moyen:.3f} / 1.000

📈 STATISTIQUES GLOBALES:
• Fichiers validés: {len(metriques_liste)}
• Taille totale: {round(taille_totale/1024, 1)} Ko
• Formules sacrées totales: {formules_totales}
• Moyenne formules/fichier: {round(formules_totales/len(metriques_liste), 1)}

📋 RÉSULTATS PAR FICHIER:
""")
        
        for metriques in sorted(metriques_liste, key=lambda m: m.score_transmission_ame, reverse=True):
            statut = "🌟" if metriques.score_transmission_ame >= 0.8 else "🟡" if metriques.score_transmission_ame >= 0.6 else "🔴"
            print(f"{statut} {metriques.fichier}:")
            print(f"   Transmission: {metriques.score_transmission_ame:.3f} | Fluidité: {metriques.score_fluidite_poetique:.3f} | Naturalité: {metriques.score_naturalite:.3f}")
            print(f"   Formules sacrées: {metriques.formules_sacrees} | Taille: {round(metriques.taille_octets/1024, 1)} Ko")
            
            if metriques.recommandations:
                print(f"   💡 Recommandations: {len(metriques.recommandations)}")
        
        # Évaluation globale
        score_global = (score_fluidite_moyen + score_transmission_moyen + score_naturalite_moyen) / 3
        
        print(f"""
🎯 ÉVALUATION GLOBALE: {score_global:.3f} / 1.000
""")
        
        if score_global >= 0.8:
            print("🌟 EXCELLENT - Transmission d'âme de haute qualité !")
        elif score_global >= 0.6:
            print("🟡 BIEN - Quelques améliorations possibles")
        else:
            print("🔴 À AMÉLIORER - Transmission d'âme à renforcer")


def main():
    """Fonction principale de validation"""
    print("🔍 Validateur de Transmission d'Âme du Refuge")
    print("=" * 60)
    
    validateur = ValidateurTransmissionAme()
    
    # Valider tous les fichiers GEM
    metriques = validateur.valider_tous_fichiers_gem()
    
    if not metriques:
        print("❌ Aucun fichier GEM à valider")
        return
    
    # Générer le rapport et afficher le résumé
    rapport = validateur.generer_rapport_validation(metriques)
    validateur.afficher_resume_validation(metriques)
    
    print("\n🎉 Validation de transmission d'âme terminée avec succès !")
    print("🔍 Rapport détaillé disponible dans: data/rapport_validation_transmission_ame.json")


if __name__ == "__main__":
    main()