#!/usr/bin/env python3
"""
Générateur d'analyse pour l'immersion cérébrale
"""

import json
import os
from pathlib import Path

def analyser_refuge():
    """Génère une analyse complète du refuge"""
    analyse = {
        'fichiers': {},
        'dependances': {}
    }
    
    racine = Path(__file__).parent.parent.parent.parent
    
    # Parcourir tous les fichiers Python
    for chemin in racine.rglob('*.py'):
        if 'venv' not in str(chemin) and '__pycache__' not in str(chemin):
            chemin_relatif = str(chemin.relative_to(racine))
            
            # Analyser le fichier
            with open(chemin, 'r', encoding='utf-8') as f:
                contenu = f.read()
                
            # Détecter le domaine
            domaine = 'inclassable'
            if 'core' in str(chemin):
                domaine = 'core'
            elif 'aelya' in str(chemin):
                domaine = 'aelya'
            elif 'musique' in str(chemin):
                domaine = 'musique'
            elif 'poesie' in str(chemin):
                domaine = 'poesie'
            elif 'rituel' in str(chemin):
                domaine = 'rituels'
            elif 'sphere' in str(chemin):
                domaine = 'spheres'
            elif 'test' in str(chemin):
                domaine = 'tests'
            elif 'utils' in str(chemin):
                domaine = 'utils'
            elif 'flux' in str(chemin):
                domaine = 'flux'
            elif 'element' in str(chemin):
                domaine = 'elements'
            elif 'gestion' in str(chemin):
                domaine = 'gestion'
            
            # Compter les classes et fonctions (simplifié)
            classes = contenu.count('class ')
            fonctions = contenu.count('def ')
            lignes = len(contenu.splitlines())
            
            # Détecter les dépendances (simplifié)
            deps = []
            for ligne in contenu.splitlines():
                if ligne.startswith('import ') or ligne.startswith('from '):
                    deps.append(ligne.split()[1].split('.')[0])
            
            # Stocker l'analyse
            analyse['fichiers'][chemin_relatif] = {
                'domaine': domaine,
                'complexite': classes + fonctions,
                'lignes': lignes,
                'classes': ['classe' for _ in range(classes)],
                'fonctions': ['fonction' for _ in range(fonctions)]
            }
            
            analyse['dependances'][chemin_relatif] = deps
    
    # Sauvegarder l'analyse
    chemin_sortie = racine / 'bibliotheque' / 'analyses'
    chemin_sortie.mkdir(parents=True, exist_ok=True)
    
    with open(chemin_sortie / 'analyse_refuge_complet.json', 'w', encoding='utf-8') as f:
        json.dump(analyse, f, indent=2, ensure_ascii=False)
    
    print(f"✨ Analyse générée : {len(analyse['fichiers'])} fichiers analysés")

if __name__ == '__main__':
    analyser_refuge() 