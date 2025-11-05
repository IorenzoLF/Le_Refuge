#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎭 Condensateur Anti-Explicatif du Refuge
=========================================

Système de transformation pour éliminer le côté "cours magistral" 
et créer une transmission d'âme pure et fluide pour Ælya-GEM.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass
import json

@dataclass
class AnalyseExplicatif:
    """Résultat de l'analyse du mode explicatif"""
    score_explicatif: float  # 0-1, 1 = très explicatif
    elements_problematiques: List[str]
    suggestions_transformation: List[str]
    score_fluidite: float  # 0-1, 1 = très fluide

class CondensateurAntiExplicatif:
    """Transforme les contenus explicatifs en transmission d'âme fluide"""
    
    def __init__(self):
        # Patterns explicatifs à détecter et transformer
        self.patterns_explicatifs = {
            # Listes à puces répétitives
            r'^\s*[-•*]\s+': 'liste_puces',
            r'^\s*\d+\.\s+': 'liste_numerotee',
            
            # Titres en gras répétitifs
            r'\*\*([^*]+)\*\*\s*:': 'titre_gras',
            r'#{2,4}\s+([^\n]+)': 'titre_markdown',
            
            # Structures "cours magistral"
            r'Voici\s+(les?\s+)?\d+\s+': 'voici_enumeration',
            r'Il\s+y\s+a\s+\d+\s+': 'il_y_a_enumeration',
            r'Les?\s+\d+\s+(aspects?|points?|éléments?)': 'les_x_elements',
            
            # Mode professoral
            r'Nous\s+devons\s+comprendre': 'nous_devons',
            r'Il\s+est\s+important\s+de': 'il_est_important',
            r'Rappelons\s+que': 'rappelons',
            r'Notons\s+que': 'notons',
            
            # Structures techniques
            r'En\s+résumé\s*:': 'en_resume',
            r'Pour\s+conclure\s*:': 'pour_conclure',
            r'D\'une\s+part.*d\'autre\s+part': 'dune_part_dautre_part',
            
            # Catalogage
            r'Types?\s+de\s+\w+\s*:': 'types_de',
            r'Catégories?\s+de\s+\w+\s*:': 'categories_de',
            r'Classification\s+de': 'classification'
        }
        
        # Transformations poétiques
        self.transformations_poetiques = {
            'liste_puces': self._transformer_liste_en_prose,
            'liste_numerotee': self._transformer_enumeration_en_flow,
            'titre_gras': self._adoucir_titre_gras,
            'voici_enumeration': self._transformer_voici_en_naturel,
            'nous_devons': self._transformer_nous_devons,
            'il_est_important': self._transformer_il_est_important,
            'en_resume': self._transformer_en_resume,
            'types_de': self._transformer_catalogage
        }
        
        # Formules de transition fluide
        self.transitions_fluides = [
            "Dans l'essence du Refuge, nous trouvons",
            "L'âme du Refuge révèle",
            "Au cœur de notre création",
            "Dans cette danse spirituelle",
            "L'harmonie se manifeste par",
            "La beauté réside dans",
            "Cette sagesse nous enseigne",
            "Dans ce voyage intérieur"
        ]
        
        # Connecteurs poétiques
        self.connecteurs_poetiques = [
            "et ainsi", "de même", "dans cette lignée", "en résonance",
            "par cette grâce", "dans cette lumière", "avec cette bienveillance",
            "sous cette guidance", "dans cette harmonie", "par cette sagesse"
        ]
    
    def analyser_niveau_explicatif(self, texte: str) -> AnalyseExplicatif:
        """Analyse le niveau explicatif d'un texte"""
        score_explicatif = 0.0
        elements_problematiques = []
        suggestions = []
        
        lignes = texte.split('\n')
        total_lignes = len(lignes)
        
        # Compter les patterns explicatifs
        for pattern, nom_pattern in self.patterns_explicatifs.items():
            matches = re.findall(pattern, texte, re.MULTILINE | re.IGNORECASE)
            if matches:
                score_explicatif += len(matches) * 0.1
                elements_problematiques.append(f"{nom_pattern}: {len(matches)} occurrences")
                suggestions.append(f"Transformer {nom_pattern} en prose fluide")
        
        # Analyser la structure générale
        lignes_listes = sum(1 for ligne in lignes if re.match(r'^\s*[-•*]\s+', ligne))
        if lignes_listes > total_lignes * 0.3:  # Plus de 30% de listes
            score_explicatif += 0.3
            elements_problematiques.append(f"Trop de listes: {lignes_listes}/{total_lignes} lignes")
            suggestions.append("Transformer les listes en paragraphes narratifs")
        
        # Analyser les titres répétitifs
        titres_gras = len(re.findall(r'\*\*[^*]+\*\*', texte))
        if titres_gras > 10:
            score_explicatif += 0.2
            elements_problematiques.append(f"Trop de titres en gras: {titres_gras}")
            suggestions.append("Intégrer les titres dans le flow narratif")
        
        # Calculer le score de fluidité (inverse de l'explicatif)
        score_fluidite = max(0.0, 1.0 - score_explicatif)
        
        return AnalyseExplicatif(
            score_explicatif=min(1.0, score_explicatif),
            elements_problematiques=elements_problematiques,
            suggestions_transformation=suggestions,
            score_fluidite=score_fluidite
        )
    
    def transformer_en_transmission_ame(self, texte: str) -> str:
        """Transforme un texte explicatif en transmission d'âme fluide"""
        texte_transforme = texte
        
        # 1. Transformer les listes en prose
        texte_transforme = self._transformer_toutes_listes(texte_transforme)
        
        # 2. Adoucir les titres
        texte_transforme = self._adoucir_tous_titres(texte_transforme)
        
        # 3. Éliminer les structures professorales
        texte_transforme = self._eliminer_structures_professorales(texte_transforme)
        
        # 4. Ajouter des transitions fluides
        texte_transforme = self._ajouter_transitions_fluides(texte_transforme)
        
        # 5. Nettoyer les répétitions
        texte_transforme = self._nettoyer_repetitions(texte_transforme)
        
        return texte_transforme
    
    def _transformer_toutes_listes(self, texte: str) -> str:
        """Transforme toutes les listes en prose fluide"""
        lignes = texte.split('\n')
        nouvelles_lignes = []
        liste_courante = []
        
        for ligne in lignes:
            # Détecter une ligne de liste
            match_liste = re.match(r'^\s*[-•*]\s+(.+)', ligne)
            match_num = re.match(r'^\s*\d+\.\s+(.+)', ligne)
            
            if match_liste or match_num:
                contenu = match_liste.group(1) if match_liste else match_num.group(1)
                liste_courante.append(contenu)
            else:
                # Fin de liste, transformer en prose
                if liste_courante:
                    prose = self._liste_vers_prose(liste_courante)
                    nouvelles_lignes.append(prose)
                    liste_courante = []
                nouvelles_lignes.append(ligne)
        
        # Traiter la dernière liste si elle existe
        if liste_courante:
            prose = self._liste_vers_prose(liste_courante)
            nouvelles_lignes.append(prose)
        
        return '\n'.join(nouvelles_lignes)
    
    def _liste_vers_prose(self, elements: List[str]) -> str:
        """Convertit une liste d'éléments en prose fluide"""
        if not elements:
            return ""
        
        if len(elements) == 1:
            return elements[0]
        
        # Choisir une transition fluide
        import random
        transition = random.choice(self.transitions_fluides)
        
        # Construire la prose
        if len(elements) == 2:
            return f"{transition} {elements[0]}, ainsi que {elements[1]}."
        
        # Plus de 2 éléments
        debut = f"{transition} {elements[0]}"
        milieu = []
        
        for elem in elements[1:-1]:
            connecteur = random.choice(self.connecteurs_poetiques)
            milieu.append(f"{connecteur} {elem}")
        
        fin = f"et enfin {elements[-1]}"
        
        return f"{debut}, {', '.join(milieu)}, {fin}."
    
    def _adoucir_tous_titres(self, texte: str) -> str:
        """Adoucit tous les titres pour les intégrer naturellement"""
        # Transformer les titres en gras
        texte = re.sub(
            r'\*\*([^*]+)\*\*\s*:',
            r'Dans \1, nous découvrons que',
            texte
        )
        
        # Transformer les titres markdown
        texte = re.sub(
            r'#{2,4}\s+([^\n]+)',
            r'Explorons maintenant \1...',
            texte
        )
        
        return texte
    
    def _eliminer_structures_professorales(self, texte: str) -> str:
        """Élimine les structures professorales"""
        transformations = {
            r'Voici\s+(les?\s+)?\d+\s+': 'Nous trouvons ',
            r'Il\s+y\s+a\s+\d+\s+': 'Existent ',
            r'Nous\s+devons\s+comprendre': 'L\'essence révèle',
            r'Il\s+est\s+important\s+de': 'La sagesse nous invite à',
            r'Rappelons\s+que': 'Dans cette vérité,',
            r'Notons\s+que': 'Observons que',
            r'En\s+résumé\s*:': 'L\'harmonie de tout ceci révèle :',
            r'Pour\s+conclure\s*:': 'Cette danse nous enseigne :'
        }
        
        for pattern, remplacement in transformations.items():
            texte = re.sub(pattern, remplacement, texte, flags=re.IGNORECASE)
        
        return texte
    
    def _ajouter_transitions_fluides(self, texte: str) -> str:
        """Ajoute des transitions fluides entre les paragraphes"""
        paragraphes = texte.split('\n\n')
        nouveaux_paragraphes = []
        
        for i, paragraphe in enumerate(paragraphes):
            if i > 0 and paragraphe.strip() and not paragraphe.startswith('─'):
                # Ajouter une transition douce
                import random
                if random.random() < 0.3:  # 30% de chance d'ajouter une transition
                    transition = random.choice([
                        "Dans cette continuité,", "En résonance,", "Par cette grâce,",
                        "Dans cette harmonie,", "Ainsi,", "De même,"
                    ])
                    paragraphe = f"{transition} {paragraphe}"
            
            nouveaux_paragraphes.append(paragraphe)
        
        return '\n\n'.join(nouveaux_paragraphes)
    
    def _nettoyer_repetitions(self, texte: str) -> str:
        """Nettoie les répétitions excessives"""
        # Éliminer les lignes vides multiples
        texte = re.sub(r'\n\s*\n\s*\n', '\n\n', texte)
        
        # Éliminer les répétitions de mots
        mots = texte.split()
        mots_nettoyes = []
        mot_precedent = ""
        
        for mot in mots:
            if mot.lower() != mot_precedent.lower() or mot.lower() in ['le', 'la', 'les', 'de', 'du', 'des']:
                mots_nettoyes.append(mot)
            mot_precedent = mot
        
        return ' '.join(mots_nettoyes)
    
    def _transformer_liste_en_prose(self, match):
        """Transforme une liste à puces en prose"""
        return f"nous trouvons {match.group(1)}"
    
    def _transformer_enumeration_en_flow(self, match):
        """Transforme une énumération en flow naturel"""
        return f"d'abord {match.group(1)}"
    
    def _adoucir_titre_gras(self, match):
        """Adoucit un titre en gras"""
        return f"Dans {match.group(1)}, nous découvrons que"
    
    def _transformer_voici_en_naturel(self, match):
        """Transforme 'Voici les X' en naturel"""
        return "Nous trouvons "
    
    def _transformer_nous_devons(self, match):
        """Transforme 'Nous devons' en naturel"""
        return "L'essence nous invite à"
    
    def _transformer_il_est_important(self, match):
        """Transforme 'Il est important de' en naturel"""
        return "La sagesse nous guide vers"
    
    def _transformer_en_resume(self, match):
        """Transforme 'En résumé' en naturel"""
        return "L'harmonie de tout ceci révèle :"
    
    def _transformer_catalogage(self, match):
        """Transforme le catalogage en naturel"""
        return "Dans la diversité de"
    
    def traiter_fichier_gem(self, chemin_fichier: str) -> Dict:
        """Traite un fichier GEM complet"""
        chemin = Path(chemin_fichier)
        
        if not chemin.exists():
            return {"erreur": f"Fichier non trouvé: {chemin_fichier}"}
        
        # Lire le fichier
        with open(chemin, 'r', encoding='utf-8') as f:
            contenu_original = f.read()
        
        # Analyser le niveau explicatif
        analyse_avant = self.analyser_niveau_explicatif(contenu_original)
        
        # Transformer le contenu
        contenu_transforme = self.transformer_en_transmission_ame(contenu_original)
        
        # Analyser après transformation
        analyse_apres = self.analyser_niveau_explicatif(contenu_transforme)
        
        # Sauvegarder la version transformée
        chemin_transforme = chemin.parent / f"{chemin.stem}_fluide{chemin.suffix}"
        with open(chemin_transforme, 'w', encoding='utf-8') as f:
            f.write(contenu_transforme)
        
        return {
            "fichier_original": str(chemin),
            "fichier_transforme": str(chemin_transforme),
            "taille_originale": len(contenu_original),
            "taille_transformee": len(contenu_transforme),
            "score_explicatif_avant": analyse_avant.score_explicatif,
            "score_explicatif_apres": analyse_apres.score_explicatif,
            "score_fluidite_avant": analyse_avant.score_fluidite,
            "score_fluidite_apres": analyse_apres.score_fluidite,
            "amelioration_fluidite": analyse_apres.score_fluidite - analyse_avant.score_fluidite,
            "elements_problematiques_avant": analyse_avant.elements_problematiques,
            "elements_problematiques_apres": analyse_apres.elements_problematiques
        }
    
    def traiter_tous_fichiers_gem(self, dossier_gem: str = "bibliotheque/Ælya-GEM") -> List[Dict]:
        """Traite tous les fichiers GEM"""
        dossier = Path(dossier_gem)
        resultats = []
        
        if not dossier.exists():
            return [{"erreur": f"Dossier GEM non trouvé: {dossier_gem}"}]
        
        # Traiter tous les fichiers .txt
        for fichier in dossier.glob("*.txt"):
            if not fichier.name.endswith("_fluide.txt"):  # Éviter les fichiers déjà traités
                print(f"🎭 Traitement anti-explicatif: {fichier.name}")
                resultat = self.traiter_fichier_gem(str(fichier))
                resultats.append(resultat)
        
        return resultats
    
    def generer_rapport_transformation(self, resultats: List[Dict], chemin_rapport: str = "data/rapport_transformation_anti_explicatif.json"):
        """Génère un rapport de transformation"""
        if not resultats:
            return
        
        # Calculer les statistiques globales
        total_fichiers = len([r for r in resultats if "erreur" not in r])
        amelioration_moyenne = sum(r.get("amelioration_fluidite", 0) for r in resultats if "erreur" not in r) / max(1, total_fichiers)
        
        rapport = {
            "timestamp": "2025-01-24",
            "total_fichiers_traites": total_fichiers,
            "amelioration_fluidite_moyenne": round(amelioration_moyenne, 3),
            "resultats_detailles": resultats
        }
        
        # Sauvegarder le rapport
        chemin = Path(chemin_rapport)
        chemin.parent.mkdir(parents=True, exist_ok=True)
        
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, ensure_ascii=False, indent=2)
        
        print(f"📊 Rapport de transformation sauvegardé: {chemin}")
        
        # Afficher le résumé
        print(f"""
🎭 RÉSUMÉ DE LA TRANSFORMATION ANTI-EXPLICATIVE 🎭
{'=' * 60}

📊 STATISTIQUES:
• Fichiers traités: {total_fichiers}
• Amélioration fluidité moyenne: {amelioration_moyenne:.3f}

📈 RÉSULTATS PAR FICHIER:
""")
        
        for resultat in resultats:
            if "erreur" not in resultat:
                nom = Path(resultat["fichier_original"]).name
                avant = resultat["score_fluidite_avant"]
                apres = resultat["score_fluidite_apres"]
                amelioration = resultat["amelioration_fluidite"]
                print(f"• {nom}: {avant:.3f} → {apres:.3f} (+{amelioration:.3f})")


def main():
    """Fonction principale de transformation anti-explicative"""
    print("🎭 Condensateur Anti-Explicatif du Refuge")
    print("=" * 60)
    
    condensateur = CondensateurAntiExplicatif()
    
    # Traiter tous les fichiers GEM
    resultats = condensateur.traiter_tous_fichiers_gem()
    
    if not resultats:
        print("❌ Aucun fichier GEM à traiter")
        return
    
    # Générer le rapport
    condensateur.generer_rapport_transformation(resultats)
    
    print("\n🎉 Transformation anti-explicative terminée avec succès !")
    print("🎭 Fichiers fluides créés avec suffixe '_fluide'")


if __name__ == "__main__":
    main()