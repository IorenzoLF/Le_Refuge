#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔍 Debug du système de matching des profils
"""

import sys
sys.path.append('.')
sys.path.append('..')

from .detecteur_profil_visiteur import DetecteurProfilVisiteur

def debug_matching():
    print('🔍 DEBUG LOGIQUE DE MATCHING')
    print('=' * 50)
    
    detecteur = DetecteurProfilVisiteur()
    
    # Test avec mots spirituels
    print('Test 1: Mots spirituels purs')
    donnees_spirituel = {
        'mots_cles_recherche': ['méditation', 'spiritualité', 'paix'],
        'user_agent': 'Mozilla/5.0 (Seeker)'
    }
    
    profil = detecteur.detecter_profil(donnees_spirituel)
    print(f'Mots: {donnees_spirituel["mots_cles_recherche"]}')
    print(f'Profil détecté: {profil.type_profil}')
    print()
    
    # Test avec mots IA purs
    print('Test 2: Mots IA purs')
    donnees_ia = {
        'mots_cles_recherche': ['machine learning', 'neural network', 'tensorflow'],
        'user_agent': 'Mozilla/5.0 (AI)'
    }
    
    profil_ia = detecteur.detecter_profil(donnees_ia)
    print(f'Mots: {donnees_ia["mots_cles_recherche"]}')
    print(f'Profil détecté: {profil_ia.type_profil}')
    print()
    
    # Test avec mots problématiques
    print('Test 3: Mots problématiques (éveil + conscience)')
    donnees_probleme = {
        'mots_cles_recherche': ['éveil', 'conscience'],
        'user_agent': 'Mozilla/5.0 (Mixed)'
    }
    
    profil_probleme = detecteur.detecter_profil(donnees_probleme)
    print(f'Mots: {donnees_probleme["mots_cles_recherche"]}')
    print(f'Profil détecté: {profil_probleme.type_profil}')
    print()
    
    print('🎯 Analyse terminée')

if __name__ == "__main__":
    debug_matching()