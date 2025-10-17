#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Correcteur d'Imports pour les Temples
====================================

Script pour corriger automatiquement les imports relatifs dans tous les temples
et les remplacer par des imports absolus ou des imports sécurisés.

Créé par Ælya - Octobre 2025
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple

class CorrecteurImportsTemples:
    """Correcteur d'imports pour les temples du Refuge"""
    
    def __init__(self, chemin_refuge: str = "."):
        self.chemin_refuge = Path(chemin_refuge)
        self.temples_corriges = []
        self.erreurs = []
        
    def detecter_temples(self) -> List[Path]:
        """Détecte tous les temples dans le répertoire src"""
        temples = []
        for item in self.chemin_refuge.iterdir():
            if item.is_dir() and item.name.startswith("temple_"):
                temples.append(item)
        return temples
    
    def analyser_imports_relatifs(self, fichier: Path) -> List[Tuple[int, str]]:
        """Analyse un fichier pour détecter les imports relatifs problématiques"""
        imports_problematiques = []
        
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                lignes = f.readlines()
                
            for i, ligne in enumerate(lignes):
                # Détecter les imports relatifs
                if re.search(r'from\s+\.', ligne) or re.search(r'import\s+\.', ligne):
                    imports_problematiques.append((i + 1, ligne.strip()))
                    
        except Exception as e:
            self.erreurs.append(f"Erreur lecture {fichier}: {e}")
            
        return imports_problematiques
    
    def corriger_imports_fichier(self, fichier: Path) -> bool:
        """Corrige les imports relatifs dans un fichier"""
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            contenu_original = contenu
            
            # Remplacer les imports relatifs par des imports absolus
            # Pattern: from .module import -> from temple_nom.module import
            nom_temple = fichier.parent.name
            
            # Correction 1: from .module import
            contenu = re.sub(
                r'from\s+\.(\w+)\s+import',
                f'from {nom_temple}.\\1 import',
                contenu
            )
            
            # Correction 2: from .sous_module.module import
            contenu = re.sub(
                r'from\s+\.(\w+)\.(\w+)\s+import',
                f'from {nom_temple}.\\1.\\2 import',
                contenu
            )
            
            # Correction 3: import .module
            contenu = re.sub(
                r'import\s+\.(\w+)',
                f'import {nom_temple}.\\1',
                contenu
            )
            
            # Si des changements ont été faits, sauvegarder
            if contenu != contenu_original:
                with open(fichier, 'w', encoding='utf-8') as f:
                    f.write(contenu)
                return True
                
        except Exception as e:
            self.erreurs.append(f"Erreur correction {fichier}: {e}")
            
        return False
    
    def corriger_temple(self, temple: Path) -> Dict:
        """Corrige tous les imports d'un temple"""
        resultat = {
            'temple': temple.name,
            'fichiers_corriges': 0,
            'imports_problematiques': 0,
            'erreurs': []
        }
        
        # Analyser tous les fichiers Python du temple
        for fichier in temple.rglob("*.py"):
            if fichier.name.startswith("__"):
                continue
                
            # Analyser les imports problématiques
            imports_problematiques = self.analyser_imports_relatifs(fichier)
            resultat['imports_problematiques'] += len(imports_problematiques)
            
            # Corriger le fichier
            if self.corriger_imports_fichier(fichier):
                resultat['fichiers_corriges'] += 1
        
        return resultat
    
    def corriger_tous_temples(self) -> Dict:
        """Corrige les imports de tous les temples"""
        temples = self.detecter_temples()
        resultats = {
            'temples_traites': len(temples),
            'temples_corriges': 0,
            'fichiers_corriges': 0,
            'imports_problematiques': 0,
            'details': []
        }
        
        print(f"Correction des imports pour {len(temples)} temples...")
        
        for temple in temples:
            print(f"\nTraitement du {temple.name}...")
            resultat = self.corriger_temple(temple)
            resultats['details'].append(resultat)
            
            if resultat['fichiers_corriges'] > 0:
                resultats['temples_corriges'] += 1
                resultats['fichiers_corriges'] += resultat['fichiers_corriges']
                resultats['imports_problematiques'] += resultat['imports_problematiques']
                print(f"  OK {resultat['fichiers_corriges']} fichiers corrigés, {resultat['imports_problematiques']} imports problématiques")
            else:
                print(f"  INFO: Aucun import relatif détecté")
        
        return resultats
    
    def generer_rapport(self, resultats: Dict) -> str:
        """Génère un rapport de correction"""
        rapport = f"""
# RAPPORT DE CORRECTION DES IMPORTS TEMPLES
==========================================

## Résumé
- Temples traités: {resultats['temples_traites']}
- Temples corrigés: {resultats['temples_corriges']}
- Fichiers corrigés: {resultats['fichiers_corriges']}
- Imports problématiques: {resultats['imports_problematiques']}

## Détails par temple
"""
        
        for detail in resultats['details']:
            rapport += f"""
### {detail['temple']}
- Fichiers corrigés: {detail['fichiers_corriges']}
- Imports problématiques: {detail['imports_problematiques']}
"""
        
        if self.erreurs:
            rapport += f"""
## Erreurs rencontrées
{chr(10).join(f"- {erreur}" for erreur in self.erreurs)}
"""
        
        return rapport

def main():
    """Fonction principale"""
    print("CORRECTEUR D'IMPORTS TEMPLES")
    print("=" * 50)
    
    correcteur = CorrecteurImportsTemples()
    resultats = correcteur.corriger_tous_temples()
    
    print(f"\nRESULTATS:")
    print(f"  Temples traités: {resultats['temples_traites']}")
    print(f"  Temples corrigés: {resultats['temples_corriges']}")
    print(f"  Fichiers corrigés: {resultats['fichiers_corriges']}")
    print(f"  Imports problématiques: {resultats['imports_problematiques']}")
    
    # Générer le rapport
    rapport = correcteur.generer_rapport(resultats)
    
    # Sauvegarder le rapport
    with open("../bibliotheque/rapport_correction_imports.md", "w", encoding="utf-8") as f:
        f.write(rapport)
    
    print(f"\nRapport sauvegardé: le_refuge/bibliotheque/rapport_correction_imports.md")
    
    if correcteur.erreurs:
        print(f"\nATTENTION: {len(correcteur.erreurs)} erreurs rencontrées:")
        for erreur in correcteur.erreurs:
            print(f"  - {erreur}")

if __name__ == "__main__":
    main()
