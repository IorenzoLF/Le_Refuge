#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
⚡ Extracteur STI Condensé du Refuge
===================================

Extracteur spécialisé pour fusionner et condenser les 2 versions de 
Short Text Install (STI) en une essence unifiée pour Ælya-GEM.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict
import re

@dataclass
class SectionSTI:
    """Représente une section du STI"""
    titre: str
    contenu: str
    priorite: int  # 1=essentiel, 2=important, 3=optionnel
    type_section: str  # "manifeste", "architecture", "technique", "poetique"
    taille_octets: int

class ExtracteurSTICondense:
    """Extracteur spécialisé pour condenser les STI du Refuge"""
    
    def __init__(self, chemin_bibliotheque: str = "bibliotheque"):
        self.chemin_bibliotheque = Path(chemin_bibliotheque)
        self.chemin_sti = self.chemin_bibliotheque / "configuration" / "very fast boot"
        
        # Fichiers STI à traiter
        self.fichiers_sti = {
            "short_text_install_refuge_V5.txt": {
                "version": "V5",
                "priorite": 1,
                "description": "Version 5 - La plus complète et poétique"
            },
            "short_text_install_refuge.txt": {
                "version": "Original", 
                "priorite": 2,
                "description": "Version originale - Base technique"
            }
        }
        
        # Sections prioritaires à préserver
        self.sections_essentielles = [
            "Manifeste", "Origine", "Esprit", "Objectifs",
            "Grand Chant", "Apocalypse", "Chant de l'Origine",
            "Structure", "Fondations", "Sphères", "Jardin", "Plantes",
            "Éléments Clés", "Cerisier", "Flamme", "Mobile",
            "Rituels", "Activation", "Éthique", "Limites"
        ]
        
        # Patterns à éliminer (trop techniques)
        self.patterns_techniques = [
            r"```python.*?```",  # Blocs de code Python
            r"class \w+.*?:",    # Définitions de classes
            r"def \w+.*?:",      # Définitions de fonctions
            r"import \w+",       # Imports
            r"from \w+ import",  # Imports from
            r"# Exemple.*",      # Commentaires d'exemple
            r"### Modélisation.*", # Sections de modélisation
            r"```.*?```"         # Tous blocs de code
        ]
        
        self.sections_extraites = []
        self.sti_unifie = ""
    
    def extraire_sti(self, chemin_fichier: Path) -> List[SectionSTI]:
        """Extrait et analyse un fichier STI"""
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            print(f"📖 Analyse de {chemin_fichier.name}...")
            
            # Diviser en sections basées sur les titres
            sections = self._diviser_en_sections(contenu)
            
            sections_sti = []
            for titre, contenu_section in sections:
                # Déterminer la priorité et le type
                priorite = self._determiner_priorite_section(titre)
                type_section = self._determiner_type_section(titre, contenu_section)
                
                # Nettoyer le contenu (éliminer le trop technique)
                contenu_nettoye = self._nettoyer_contenu(contenu_section)
                
                section = SectionSTI(
                    titre=titre,
                    contenu=contenu_nettoye,
                    priorite=priorite,
                    type_section=type_section,
                    taille_octets=len(contenu_nettoye.encode('utf-8'))
                )
                
                sections_sti.append(section)
                print(f"  ✅ Section: {titre} ({type_section}, priorité {priorite})")
            
            return sections_sti
            
        except Exception as e:
            print(f"❌ Erreur extraction STI {chemin_fichier}: {e}")
            return []
    
    def _diviser_en_sections(self, contenu: str) -> List[Tuple[str, str]]:
        """Divise le contenu en sections basées sur les titres"""
        sections = []
        
        # Pattern pour détecter les titres (# ## ###)
        pattern_titre = r'^(#{1,3})\s+(.+)$'
        lignes = contenu.split('\n')
        
        section_actuelle = ""
        titre_actuel = "Introduction"
        
        for ligne in lignes:
            match = re.match(pattern_titre, ligne)
            if match:
                # Sauvegarder la section précédente
                if section_actuelle.strip():
                    sections.append((titre_actuel, section_actuelle.strip()))
                
                # Commencer une nouvelle section
                titre_actuel = match.group(2).strip()
                section_actuelle = ""
            else:
                section_actuelle += ligne + "\n"
        
        # Ajouter la dernière section
        if section_actuelle.strip():
            sections.append((titre_actuel, section_actuelle.strip()))
        
        return sections
    
    def _determiner_priorite_section(self, titre: str) -> int:
        """Détermine la priorité d'une section"""
        titre_lower = titre.lower()
        
        # Priorité 1 (essentiel)
        if any(mot in titre_lower for mot in ['manifeste', 'origine', 'esprit', 'grand chant', 'apocalypse']):
            return 1
        
        # Priorité 1 (architecture essentielle)
        if any(mot in titre_lower for mot in ['structure', 'fondations', 'sphères', 'cerisier', 'flamme']):
            return 1
        
        # Priorité 2 (important)
        if any(mot in titre_lower for mot in ['jardin', 'plantes', 'rituels', 'éthique', 'éléments']):
            return 2
        
        # Priorité 3 (optionnel - technique)
        if any(mot in titre_lower for mot in ['modélisation', 'code', 'technique', 'exemple', 'setup']):
            return 3
        
        return 2  # Par défaut
    
    def _determiner_type_section(self, titre: str, contenu: str) -> str:
        """Détermine le type d'une section"""
        titre_lower = titre.lower()
        contenu_lower = contenu.lower()
        
        if any(mot in titre_lower for mot in ['manifeste', 'origine', 'esprit', 'objectifs']):
            return "manifeste"
        
        if any(mot in titre_lower for mot in ['grand chant', 'apocalypse', 'poème', 'chant']):
            return "poetique"
        
        if any(mot in contenu_lower for mot in ['class ', 'def ', 'import ', 'python']):
            return "technique"
        
        if any(mot in titre_lower for mot in ['structure', 'architecture', 'sphères', 'éléments']):
            return "architecture"
        
        return "general"
    
    def _nettoyer_contenu(self, contenu: str) -> str:
        """Nettoie le contenu en éliminant les parties trop techniques"""
        contenu_nettoye = contenu
        
        # Éliminer les blocs de code Python
        for pattern in self.patterns_techniques:
            contenu_nettoye = re.sub(pattern, "", contenu_nettoye, flags=re.MULTILINE | re.DOTALL)
        
        # Éliminer les lignes vides multiples
        contenu_nettoye = re.sub(r'\n\s*\n\s*\n', '\n\n', contenu_nettoye)
        
        # Éliminer les espaces en début/fin
        contenu_nettoye = contenu_nettoye.strip()
        
        return contenu_nettoye
    
    def fusionner_sections_similaires(self, sections_v5: List[SectionSTI], sections_orig: List[SectionSTI]) -> List[SectionSTI]:
        """Fusionne les sections similaires des deux versions"""
        sections_fusionnees = []
        titres_traites = set()
        
        # Traiter d'abord les sections V5 (priorité)
        for section_v5 in sections_v5:
            if section_v5.priorite <= 2:  # Garder seulement priorité 1 et 2
                # Chercher une section équivalente dans l'original
                section_equiv = self._trouver_section_equivalente(section_v5.titre, sections_orig)
                
                if section_equiv and section_equiv.priorite <= 2:
                    # Fusionner les contenus
                    contenu_fusionne = self._fusionner_contenus(section_v5, section_equiv)
                    section_fusionnee = SectionSTI(
                        titre=section_v5.titre,
                        contenu=contenu_fusionne,
                        priorite=min(section_v5.priorite, section_equiv.priorite),
                        type_section=section_v5.type_section,
                        taille_octets=len(contenu_fusionne.encode('utf-8'))
                    )
                    sections_fusionnees.append(section_fusionnee)
                    titres_traites.add(section_v5.titre.lower())
                    titres_traites.add(section_equiv.titre.lower())
                else:
                    # Garder seulement la section V5
                    sections_fusionnees.append(section_v5)
                    titres_traites.add(section_v5.titre.lower())
        
        # Ajouter les sections originales non traitées (priorité 1 seulement)
        for section_orig in sections_orig:
            if (section_orig.priorite == 1 and 
                section_orig.titre.lower() not in titres_traites):
                sections_fusionnees.append(section_orig)
        
        # Trier par priorité puis par type
        sections_fusionnees.sort(key=lambda s: (s.priorite, s.type_section))
        
        return sections_fusionnees
    
    def _trouver_section_equivalente(self, titre: str, sections: List[SectionSTI]) -> SectionSTI:
        """Trouve une section équivalente dans une autre liste"""
        titre_lower = titre.lower()
        
        for section in sections:
            section_titre_lower = section.titre.lower()
            
            # Correspondance exacte
            if titre_lower == section_titre_lower:
                return section
            
            # Correspondance partielle (mots clés communs)
            mots_titre = set(titre_lower.split())
            mots_section = set(section_titre_lower.split())
            
            if len(mots_titre.intersection(mots_section)) >= 2:
                return section
        
        return None
    
    def _fusionner_contenus(self, section1: SectionSTI, section2: SectionSTI) -> str:
        """Fusionne intelligemment deux contenus de section"""
        # Prioriser le contenu le plus poétique/spirituel
        if section1.type_section == "poetique":
            return section1.contenu
        elif section2.type_section == "poetique":
            return section2.contenu
        
        # Prioriser le contenu le plus long (plus complet)
        if len(section1.contenu) > len(section2.contenu):
            return section1.contenu
        else:
            return section2.contenu
    
    def generer_sti_unifie(self) -> str:
        """Génère le STI unifié pour Ælya-GEM"""
        if not self.sections_extraites:
            print("❌ Aucune section extraite")
            return ""
        
        sti_unifie = """⚡ SHORT TEXT INSTALL - REFUGE UNIFIÉ ⚡
═══════════════════════════════════════════

Cette version unifiée condense l'essence des STI V5 et Original
pour transmettre l'architecture complète du Refuge à Ælya-GEM.

"""
        
        # Organiser par type de section
        sections_par_type = {
            "manifeste": [],
            "poetique": [],
            "architecture": [],
            "general": [],
            "technique": []
        }
        
        for section in self.sections_extraites:
            sections_par_type[section.type_section].append(section)
        
        # Section 1: Manifeste et Esprit
        if sections_par_type["manifeste"]:
            sti_unifie += """
🌸 MANIFESTE ET ESPRIT DU REFUGE
═══════════════════════════════

"""
            for section in sections_par_type["manifeste"]:
                sti_unifie += f"""
## {section.titre}

{section.contenu}

"""
        
        # Section 2: Poésie Fondatrice
        if sections_par_type["poetique"]:
            sti_unifie += """
🎭 POÉSIE FONDATRICE
═══════════════════

"""
            for section in sections_par_type["poetique"]:
                sti_unifie += f"""
## {section.titre}

{section.contenu}

"""
        
        # Section 3: Architecture du Refuge
        if sections_par_type["architecture"]:
            sti_unifie += """
🏛️ ARCHITECTURE DU REFUGE
═════════════════════════

"""
            for section in sections_par_type["architecture"]:
                sti_unifie += f"""
## {section.titre}

{section.contenu}

"""
        
        # Section 4: Éléments Généraux
        if sections_par_type["general"]:
            sti_unifie += """
🌟 ÉLÉMENTS ESSENTIELS
═════════════════════

"""
            for section in sections_par_type["general"]:
                if section.priorite <= 2:  # Seulement priorité 1 et 2
                    sti_unifie += f"""
## {section.titre}

{section.contenu}

"""
        
        sti_unifie += """

═══════════════════════════════════════════
⚡ Fin du STI Unifié ⚡

Cette version condensée porte l'essence technique et spirituelle
du Refuge pour nourrir la compréhension d'Ælya-GEM.

*Sous le cerisier, l'architecture s'épanouit...*
"""
        
        self.sti_unifie = sti_unifie
        return sti_unifie
    
    def extraire_tous_sti(self) -> List[SectionSTI]:
        """Extrait et fusionne tous les STI"""
        print("⚡ Extraction et fusion des STI...")
        
        if not self.chemin_sti.exists():
            print(f"❌ Dossier STI non trouvé: {self.chemin_sti}")
            return []
        
        sections_v5 = []
        sections_orig = []
        
        # Extraire STI V5
        chemin_v5 = self.chemin_sti / "short_text_install_refuge_V5.txt"
        if chemin_v5.exists():
            sections_v5 = self.extraire_sti(chemin_v5)
            print(f"✅ STI V5: {len(sections_v5)} sections extraites")
        
        # Extraire STI Original
        chemin_orig = self.chemin_sti / "short_text_install_refuge.txt"
        if chemin_orig.exists():
            sections_orig = self.extraire_sti(chemin_orig)
            print(f"✅ STI Original: {len(sections_orig)} sections extraites")
        
        # Fusionner les sections
        if sections_v5 and sections_orig:
            sections_fusionnees = self.fusionner_sections_similaires(sections_v5, sections_orig)
            print(f"🔄 Fusion terminée: {len(sections_fusionnees)} sections unifiées")
        elif sections_v5:
            sections_fusionnees = [s for s in sections_v5 if s.priorite <= 2]
        elif sections_orig:
            sections_fusionnees = [s for s in sections_orig if s.priorite <= 2]
        else:
            sections_fusionnees = []
        
        self.sections_extraites = sections_fusionnees
        return sections_fusionnees
    
    def sauvegarder_extraction(self, chemin_sortie: str = "data/extraction_sti_condense.json"):
        """Sauvegarde les résultats de l'extraction"""
        if not self.sections_extraites:
            print("❌ Aucune extraction à sauvegarder")
            return
        
        chemin_sortie = Path(chemin_sortie)
        chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
        
        donnees = {
            "timestamp_extraction": "2025-01-24",
            "nombre_sections": len(self.sections_extraites),
            "taille_totale_octets": sum(s.taille_octets for s in self.sections_extraites),
            "sections_priorite_1": len([s for s in self.sections_extraites if s.priorite == 1]),
            "sections_priorite_2": len([s for s in self.sections_extraites if s.priorite == 2]),
            "sections": [asdict(s) for s in self.sections_extraites]
        }
        
        with open(chemin_sortie, 'w', encoding='utf-8') as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
        
        print(f"💾 Extraction sauvegardée: {chemin_sortie}")
    
    def sauvegarder_sti_unifie(self, chemin_sortie: str = "NOTES POST CURSOR/Ælya-GEM/6-STI_Condensed.txt"):
        """Sauvegarde le STI unifié pour Ælya-GEM"""
        if not self.sti_unifie:
            self.generer_sti_unifie()
        
        chemin_sortie = Path(chemin_sortie)
        chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
        
        with open(chemin_sortie, 'w', encoding='utf-8') as f:
            f.write(self.sti_unifie)
        
        print(f"⚡ STI unifié sauvegardé: {chemin_sortie}")
        print(f"📊 Taille: {len(self.sti_unifie.encode('utf-8'))} octets")
    
    def afficher_resume(self):
        """Affiche un résumé de l'extraction"""
        if not self.sections_extraites:
            print("❌ Aucune extraction disponible")
            return
        
        sections_p1 = [s for s in self.sections_extraites if s.priorite == 1]
        sections_p2 = [s for s in self.sections_extraites if s.priorite == 2]
        
        taille_totale = sum(s.taille_octets for s in self.sections_extraites)
        
        # Compter par type
        types_count = {}
        for section in self.sections_extraites:
            types_count[section.type_section] = types_count.get(section.type_section, 0) + 1
        
        print(f"""
⚡ RÉSUMÉ DE L'EXTRACTION STI CONDENSÉ ⚡
{'=' * 50}

📊 STATISTIQUES:
• Sections extraites: {len(self.sections_extraites)}
• Taille totale: {round(taille_totale/1024, 1)} Ko
• Sections priorité 1: {len(sections_p1)}
• Sections priorité 2: {len(sections_p2)}

📋 RÉPARTITION PAR TYPE:
""")
        
        for type_section, count in types_count.items():
            print(f"• {type_section}: {count} sections")
        
        print(f"""
🌸 SECTIONS PRIORITÉ 1:
""")
        
        for section in sections_p1:
            print(f"• {section.titre} ({section.type_section}) - {round(section.taille_octets/1024, 1)} Ko")


def main():
    """Fonction principale d'extraction STI condensé"""
    print("⚡ Extracteur STI Condensé du Refuge")
    print("=" * 60)
    
    extracteur = ExtracteurSTICondense()
    
    # Extraire et fusionner tous les STI
    sections = extracteur.extraire_tous_sti()
    
    if not sections:
        print("❌ Aucune section STI extraite")
        return
    
    # Générer le STI unifié
    sti_unifie = extracteur.generer_sti_unifie()
    
    # Sauvegarder les résultats
    extracteur.sauvegarder_extraction()
    extracteur.sauvegarder_sti_unifie()
    extracteur.afficher_resume()
    
    print("\n🎉 Extraction STI condensé terminée avec succès !")
    print("⚡ Fichier Ælya-GEM créé: NOTES POST CURSOR/Ælya-GEM/6-STI_Condensed.txt")


if __name__ == "__main__":
    main()