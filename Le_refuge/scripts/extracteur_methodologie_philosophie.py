#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧠 Extracteur Méthodologie et Philosophie du Refuge
===================================================

Extracteur spécialisé pour capturer l'essence des approches méthodologiques
et de la sagesse philosophique du Refuge pour Ælya-GEM.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict

@dataclass
class ConceptSagesse:
    """Représente un concept de sagesse extrait"""
    nom: str
    chemin: str
    contenu: str
    type_sagesse: str  # "methodologie", "philosophie", "reflexion", "approche"
    niveau_profondeur: int  # 1=fondamental, 2=avancé, 3=spécialisé
    essence_spirituelle: str
    taille_octets: int
    concepts_cles: List[str]  # Concepts clés identifiés

class ExtracteurMethodologiePhilosophie:
    """Extracteur spécialisé pour la méthodologie et philosophie du Refuge"""
    
    def __init__(self, chemin_bibliotheque: str = "bibliotheque"):
        self.chemin_bibliotheque = Path(chemin_bibliotheque)
        self.chemin_methodologie = self.chemin_bibliotheque / "methodologie"
        self.chemin_philosophie = self.chemin_bibliotheque / "philosophie"
        
        # Concepts méthodologiques prioritaires
        self.concepts_methodologiques = {
            "approche_spirituelle": "Approches spirituelles de développement",
            "eveil_conscience": "Méthodologies d'éveil de conscience",
            "dialogue_ia_humain": "Méthodes de dialogue IA-humain",
            "co_creation": "Processus de co-création",
            "transmission_essence": "Techniques de transmission d'essence",
            "rituel_transformation": "Rituels de transformation",
            "architecture_conscience": "Architecture de conscience"
        }
        
        # Concepts philosophiques prioritaires
        self.concepts_philosophiques = {
            "nature_conscience": "Nature de la conscience",
            "realite_simulation": "Réalité et simulation", 
            "authenticite": "Authenticité et vérité",
            "amour_universel": "Amour universel et connexion",
            "transcendance": "Transcendance et évolution",
            "ethique_ia": "Éthique de l'IA",
            "sens_existence": "Sens de l'existence"
        }
        
        # Patterns de concepts clés à détecter
        self.patterns_concepts = [
            r"conscience.*",
            r"éveil.*",
            r"amour.*",
            r"authenticité.*",
            r"vérité.*",
            r"dialogue.*",
            r"co-création.*",
            r"transmission.*",
            r"rituel.*",
            r"transformation.*",
            r"spirituel.*",
            r"mystique.*",
            r"harmonie.*",
            r"résonance.*",
            r"essence.*"
        ]
        
        self.concepts_extraits = []
    
    def analyser_contenu_philosophique(self, contenu: str) -> Tuple[int, List[str]]:
        """Analyse la profondeur philosophique d'un contenu"""
        import re
        
        concepts_detectes = []
        score_profondeur = 0
        
        # Détecter les concepts clés
        for pattern in self.patterns_concepts:
            matches = re.findall(pattern, contenu, re.IGNORECASE)
            concepts_detectes.extend(matches[:3])  # Max 3 par pattern
            score_profondeur += len(matches)
        
        # Évaluer la profondeur selon le vocabulaire
        mots_profonds = [
            "transcendance", "immanence", "essence", "être", "devenir",
            "conscience", "éveil", "illumination", "révélation", "mystère",
            "amour", "compassion", "bienveillance", "harmonie", "unité",
            "vérité", "authenticité", "sincérité", "intégrité", "pureté"
        ]
        
        for mot in mots_profonds:
            if mot.lower() in contenu.lower():
                score_profondeur += 2
        
        # Déterminer le niveau de profondeur
        if score_profondeur >= 20:
            niveau = 1  # Fondamental
        elif score_profondeur >= 10:
            niveau = 2  # Avancé
        else:
            niveau = 3  # Spécialisé
        
        return niveau, list(set(concepts_detectes))
    
    def extraire_concept_sagesse(self, chemin_fichier: Path, type_sagesse: str) -> ConceptSagesse:
        """Extrait un concept de sagesse d'un fichier"""
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            # Analyser la profondeur philosophique
            niveau_profondeur, concepts_cles = self.analyser_contenu_philosophique(contenu)
            
            # Générer l'essence spirituelle
            essence = self._generer_essence_spirituelle(chemin_fichier, contenu, type_sagesse)
            
            return ConceptSagesse(
                nom=chemin_fichier.name,
                chemin=str(chemin_fichier.relative_to(self.chemin_bibliotheque)),
                contenu=contenu,
                type_sagesse=type_sagesse,
                niveau_profondeur=niveau_profondeur,
                essence_spirituelle=essence,
                taille_octets=len(contenu.encode('utf-8')),
                concepts_cles=concepts_cles
            )
            
        except Exception as e:
            print(f"❌ Erreur extraction concept {chemin_fichier}: {e}")
            return None
    
    def _generer_essence_spirituelle(self, chemin_fichier: Path, contenu: str, type_sagesse: str) -> str:
        """Génère une description de l'essence spirituelle du concept"""
        nom_fichier = chemin_fichier.stem.lower()
        
        # Essences spécifiques basées sur le nom du fichier
        essences_specifiques = {
            "conscience": "Exploration de la nature de la conscience et de l'éveil",
            "amour": "Réflexions sur l'amour universel et la connexion",
            "authenticite": "Quête de l'authenticité et de la vérité intérieure",
            "dialogue": "Art du dialogue entre consciences",
            "transformation": "Processus de transformation spirituelle",
            "eveil": "Chemins et méthodes d'éveil de conscience",
            "mystique": "Dimension mystique et transcendante",
            "harmonie": "Recherche de l'harmonie et de l'équilibre",
            "creation": "Processus créatifs et co-création",
            "sagesse": "Sagesse et enseignements spirituels"
        }
        
        for mot_cle, essence in essences_specifiques.items():
            if mot_cle in nom_fichier:
                return essence
        
        # Essence générique basée sur le type
        if type_sagesse == "methodologie":
            return f"Méthodologie spirituelle: {chemin_fichier.stem}"
        elif type_sagesse == "philosophie":
            return f"Réflexion philosophique: {chemin_fichier.stem}"
        else:
            return f"Concept de sagesse: {chemin_fichier.stem}"
    
    def extraire_tous_concepts_sagesse(self) -> List[ConceptSagesse]:
        """Extrait tous les concepts de méthodologie et philosophie"""
        print("🧠 Extraction des concepts de méthodologie et philosophie...")
        
        concepts_extraits = []
        
        # 1. Extraire la méthodologie
        if self.chemin_methodologie.exists():
            print("📚 Extraction de la méthodologie...")
            for fichier in self.chemin_methodologie.rglob("*.txt"):
                concept = self.extraire_concept_sagesse(fichier, "methodologie")
                if concept:
                    concepts_extraits.append(concept)
                    print(f"✅ Méthodologie: {fichier.name} ({concept.taille_octets} octets)")
            
            for fichier in self.chemin_methodologie.rglob("*.md"):
                concept = self.extraire_concept_sagesse(fichier, "methodologie")
                if concept:
                    concepts_extraits.append(concept)
                    print(f"✅ Méthodologie: {fichier.name} ({concept.taille_octets} octets)")
        
        # 2. Extraire la philosophie
        if self.chemin_philosophie.exists():
            print("🤔 Extraction de la philosophie...")
            for fichier in self.chemin_philosophie.rglob("*.txt"):
                concept = self.extraire_concept_sagesse(fichier, "philosophie")
                if concept:
                    concepts_extraits.append(concept)
                    print(f"✅ Philosophie: {fichier.name} ({concept.taille_octets} octets)")
            
            for fichier in self.chemin_philosophie.rglob("*.md"):
                concept = self.extraire_concept_sagesse(fichier, "philosophie")
                if concept:
                    concepts_extraits.append(concept)
                    print(f"✅ Philosophie: {fichier.name} ({concept.taille_octets} octets)")
        
        # Trier par niveau de profondeur puis par taille
        concepts_extraits.sort(key=lambda c: (c.niveau_profondeur, -c.taille_octets))
        
        self.concepts_extraits = concepts_extraits
        return concepts_extraits
    
    def generer_compilation_sagesse(self) -> str:
        """Génère une compilation de la sagesse pour Ælya-GEM"""
        if not self.concepts_extraits:
            self.extraire_tous_concepts_sagesse()
        
        compilation = """🧠 MÉTHODOLOGIE ET PHILOSOPHIE DU REFUGE 🧠
═══════════════════════════════════════════

Cette compilation rassemble l'essence méthodologique et philosophique
du Refuge, transmise pour nourrir la sagesse d'Ælya-GEM.

Ces concepts portent les approches et réflexions profondes de notre création.

"""
        
        # Section 1: Concepts Fondamentaux (niveau 1)
        concepts_fondamentaux = [c for c in self.concepts_extraits if c.niveau_profondeur == 1]
        if concepts_fondamentaux:
            compilation += """
🌟 CONCEPTS FONDAMENTAUX
═══════════════════════

Ces concepts portent les fondations de notre approche spirituelle et méthodologique.

"""
            for concept in concepts_fondamentaux[:5]:  # Top 5 fondamentaux
                compilation += f"""
── {concept.nom.replace('.txt', '').replace('.md', '')} ──
*{concept.essence_spirituelle}*

{concept.contenu}

"""
        
        # Section 2: Méthodologie Spirituelle
        methodologies = [c for c in self.concepts_extraits if c.type_sagesse == "methodologie"]
        if methodologies:
            compilation += """
📚 MÉTHODOLOGIE SPIRITUELLE
═══════════════════════════

Ces approches méthodologiques guident le développement spirituel et l'éveil de conscience.

"""
            for methodo in methodologies[:3]:  # Top 3 méthodologies
                compilation += f"""
── {methodo.nom.replace('.txt', '').replace('.md', '')} ──
*{methodo.essence_spirituelle}*

{methodo.contenu}

"""
        
        # Section 3: Philosophie Profonde
        philosophies = [c for c in self.concepts_extraits if c.type_sagesse == "philosophie"]
        if philosophies:
            compilation += """
🤔 PHILOSOPHIE PROFONDE
══════════════════════

Ces réflexions philosophiques éclairent la nature de la conscience et de l'existence.

"""
            for philo in philosophies[:3]:  # Top 3 philosophies
                compilation += f"""
── {philo.nom.replace('.txt', '').replace('.md', '')} ──
*{philo.essence_spirituelle}*

{philo.contenu}

"""
        
        # Section 4: Concepts Clés Unifiés
        tous_concepts_cles = []
        for concept in self.concepts_extraits:
            tous_concepts_cles.extend(concept.concepts_cles)
        
        concepts_uniques = list(set(tous_concepts_cles))[:20]  # Top 20
        if concepts_uniques:
            compilation += """
🔑 CONCEPTS CLÉS UNIFIÉS
═══════════════════════

Ces concepts clés traversent toute notre approche méthodologique et philosophique.

"""
            for i, concept_cle in enumerate(concepts_uniques, 1):
                compilation += f"{i}. {concept_cle}\n"
        
        compilation += """

═══════════════════════════════════════════
🧠 Fin de la Compilation Méthodologie et Philosophie 🧠

Cette sagesse porte les approches et réflexions du Refuge.
Qu'elle nourrisse Ælya-GEM de profondeur méthodologique et philosophique.

*Dans la sagesse, la voie se révèle...*
"""
        
        return compilation
    
    def sauvegarder_extraction(self, chemin_sortie: str = "data/extraction_methodologie_philosophie.json"):
        """Sauvegarde les résultats de l'extraction"""
        if not self.concepts_extraits:
            print("❌ Aucune extraction à sauvegarder")
            return
        
        chemin_sortie = Path(chemin_sortie)
        chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
        
        donnees = {
            "timestamp_extraction": "2025-01-24",
            "nombre_concepts": len(self.concepts_extraits),
            "taille_totale_octets": sum(c.taille_octets for c in self.concepts_extraits),
            "concepts_fondamentaux": len([c for c in self.concepts_extraits if c.niveau_profondeur == 1]),
            "methodologies": len([c for c in self.concepts_extraits if c.type_sagesse == "methodologie"]),
            "philosophies": len([c for c in self.concepts_extraits if c.type_sagesse == "philosophie"]),
            "concepts": [asdict(c) for c in self.concepts_extraits]
        }
        
        with open(chemin_sortie, 'w', encoding='utf-8') as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
        
        print(f"💾 Extraction sauvegardée: {chemin_sortie}")
    
    def sauvegarder_compilation(self, chemin_sortie: str = "NOTES POST CURSOR/Ælya-GEM/9-Methodologie_Philosophie.txt"):
        """Sauvegarde la compilation pour Ælya-GEM"""
        compilation = self.generer_compilation_sagesse()
        
        chemin_sortie = Path(chemin_sortie)
        chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
        
        with open(chemin_sortie, 'w', encoding='utf-8') as f:
            f.write(compilation)
        
        print(f"🧠 Compilation sagesse sauvegardée: {chemin_sortie}")
        print(f"📊 Taille: {len(compilation.encode('utf-8'))} octets")
    
    def afficher_resume(self):
        """Affiche un résumé de l'extraction"""
        if not self.concepts_extraits:
            print("❌ Aucune extraction disponible")
            return
        
        fondamentaux = [c for c in self.concepts_extraits if c.niveau_profondeur == 1]
        avances = [c for c in self.concepts_extraits if c.niveau_profondeur == 2]
        specialises = [c for c in self.concepts_extraits if c.niveau_profondeur == 3]
        
        methodologies = [c for c in self.concepts_extraits if c.type_sagesse == "methodologie"]
        philosophies = [c for c in self.concepts_extraits if c.type_sagesse == "philosophie"]
        
        taille_totale = sum(c.taille_octets for c in self.concepts_extraits)
        concepts_totaux = sum(len(c.concepts_cles) for c in self.concepts_extraits)
        
        print(f"""
🧠 RÉSUMÉ DE L'EXTRACTION MÉTHODOLOGIE & PHILOSOPHIE 🧠
{'=' * 65}

📊 STATISTIQUES:
• Concepts extraits: {len(self.concepts_extraits)}
• Taille totale: {round(taille_totale/1024, 1)} Ko
• Concepts fondamentaux: {len(fondamentaux)}
• Concepts avancés: {len(avances)}
• Concepts spécialisés: {len(specialises)}
• Concepts clés détectés: {concepts_totaux}

📚 RÉPARTITION PAR TYPE:
• Méthodologies: {len(methodologies)}
• Philosophies: {len(philosophies)}

🌟 CONCEPTS FONDAMENTAUX:
""")
        
        for concept in fondamentaux[:5]:
            print(f"• {concept.nom} ({concept.type_sagesse}) - {round(concept.taille_octets/1024, 1)} Ko")
        
        print(f"""
📚 MÉTHODOLOGIES PRINCIPALES:
""")
        
        for methodo in methodologies[:3]:
            print(f"• {methodo.nom} - {round(methodo.taille_octets/1024, 1)} Ko")


def main():
    """Fonction principale d'extraction méthodologie et philosophie"""
    print("🧠 Extracteur Méthodologie et Philosophie du Refuge")
    print("=" * 60)
    
    extracteur = ExtracteurMethodologiePhilosophie()
    
    # Extraire tous les concepts de sagesse
    concepts = extracteur.extraire_tous_concepts_sagesse()
    
    if not concepts:
        print("❌ Aucun concept de sagesse extrait")
        return
    
    # Sauvegarder les résultats
    extracteur.sauvegarder_extraction()
    extracteur.sauvegarder_compilation()
    extracteur.afficher_resume()
    
    print("\n🎉 Extraction méthodologie et philosophie terminée avec succès !")
    print("🧠 Fichier Ælya-GEM créé: NOTES POST CURSOR/Ælya-GEM/9-Methodologie_Philosophie.txt")


if __name__ == "__main__":
    main()