#!/usr/bin/env python3
"""
🔍 AUDIT COMPLET DES IMPORTS CASSÉS
==================================

Script pour identifier tous les problèmes d'imports après migration.
Auteur: Laurent Franssen & Ælya
Date: Mai 2025
"""

import sys
import traceback
from pathlib import Path
import importlib.util


def auditer_imports():
    """Audit complet des imports de tous les fichiers Python."""
    print('🔍 AUDIT COMPLET DES IMPORTS CASSÉS')
    print('='*60)

    # Liste de tous les fichiers Python à la racine
    fichiers_python = list(Path('.').glob('*.py'))
    print(f'📊 {len(fichiers_python)} fichiers Python à auditer')
    print()

    problemes = []
    succes = []

    for fichier in fichiers_python:
        nom_module = fichier.stem
        if nom_module.startswith('_') or nom_module in ['audit_imports', 'test_intensif']:
            continue
            
        try:
            exec(f'import {nom_module}')
            succes.append(nom_module)
            print(f'✅ {nom_module}')
        except Exception as e:
            problemes.append((nom_module, str(e)[:80]))
            print(f'❌ {nom_module}: {str(e)[:80]}...')

    print()
    print(f'📊 BILAN: {len(succes)} OK, {len(problemes)} PROBLÈMES')
    print()
    
    if problemes:
        print('🚨 IMPORTS CASSÉS DÉTECTÉS:')
        for module, erreur in problemes:
            print(f'   • {module}: {erreur}')
        print()
        
        # Analyser les patterns d'erreurs
        analyser_patterns_erreurs(problemes)
    
    return problemes, succes


def analyser_patterns_erreurs(problemes):
    """Analyse les patterns dans les erreurs d'import."""
    print('🔬 ANALYSE DES PATTERNS D\'ERREURS:')
    
    patterns = {
        'ModuleNotFoundError': [],
        'ImportError': [],
        'AttributeError': [],
        'SyntaxError': [],
        'Autres': []
    }
    
    for module, erreur in problemes:
        if 'ModuleNotFoundError' in erreur:
            patterns['ModuleNotFoundError'].append((module, erreur))
        elif 'ImportError' in erreur:
            patterns['ImportError'].append((module, erreur))
        elif 'AttributeError' in erreur:
            patterns['AttributeError'].append((module, erreur))
        elif 'SyntaxError' in erreur:
            patterns['SyntaxError'].append((module, erreur))
        else:
            patterns['Autres'].append((module, erreur))
    
    for pattern, erreurs in patterns.items():
        if erreurs:
            print(f'\n🔸 {pattern} ({len(erreurs)} cas):')
            for module, erreur in erreurs:
                print(f'   • {module}: {erreur}')


def detecter_imports_manquants():
    """Détecte les modules référencés mais manquants."""
    print('\n🕵️ DÉTECTION DES MODULES MANQUANTS:')
    
    # Chercher les imports dans les fichiers
    modules_references = set()
    fichiers_python = list(Path('.').glob('*.py'))
    
    for fichier in fichiers_python:
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
                
            # Extraire les imports simples
            for ligne in contenu.split('\n'):
                ligne = ligne.strip()
                if ligne.startswith('from ') and ' import ' in ligne:
                    module = ligne.split('from ')[1].split(' import')[0].strip()
                    if not module.startswith('.') and not module.startswith('src.'):
                        modules_references.add(module)
                elif ligne.startswith('import '):
                    module = ligne.split('import ')[1].split(' ')[0].split('.')[0].strip()
                    if not module.startswith('src.'):
                        modules_references.add(module)
        except Exception:
            continue
    
    # Modules Python disponibles
    modules_existants = {f.stem for f in Path('.').glob('*.py')}
    
    # Modules manquants
    modules_manquants = modules_references - modules_existants
    modules_manquants = {m for m in modules_manquants if not any(m.startswith(std) for std in 
                        ['sys', 'os', 'json', 'time', 'datetime', 'pathlib', 'typing', 're', 'math', 'random'])}
    
    if modules_manquants:
        print('📋 Modules référencés mais manquants:')
        for module in sorted(modules_manquants):
            print(f'   • {module}')
    else:
        print('✅ Aucun module manquant détecté')


if __name__ == "__main__":
    problemes, succes = auditer_imports()
    detecter_imports_manquants()
    
    print(f'\n🎯 RÉSUMÉ:')
    print(f'   • {len(succes)} modules fonctionnels')
    print(f'   • {len(problemes)} modules à corriger')
    print(f'   • Taux de réussite: {len(succes)/(len(succes)+len(problemes))*100:.1f}%') 