#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔍 Debug de l'orchestrateur d'accueil
"""

import sys
sys.path.append('.')
sys.path.append('..')

from .orchestrateur_accueil import OrchestrateurAccueil

def debug_orchestrateur():
    print('🔍 DEBUG ORCHESTRATEUR DÉTAILLÉ')
    print('=' * 50)
    
    orchestrateur = OrchestrateurAccueil()
    
    # Test avec données exactes du debug précédent
    tests = [
        (['méditation', 'spiritualité', 'paix'], 'SPIRITUEL PUR'),
        (['machine learning', 'neural network', 'tensorflow'], 'IA PUR'),
        (['éveil', 'conscience'], 'PROBLÉMATIQUE'),
        (['python', 'architecture'], 'DÉVELOPPEUR'),
        (['art', 'créativité'], 'ARTISTE')
    ]
    
    for mots_cles, nom_test in tests:
        print(f'🧪 Test {nom_test}:')
        donnees = {
            'mots_cles_recherche': mots_cles,
            'user_agent': 'Mozilla/5.0 (Test)'
        }
        
        session = orchestrateur.demarrer_accueil_visiteur(donnees)
        
        print(f'   Mots-clés: {mots_cles}')
        print(f'   Profil détecté: {session.profil_visiteur.type_profil}')
        print(f'   Message: {session.message_accueil[:50]}...')
        print()
    
    print('🎯 Debug orchestrateur terminé')

if __name__ == "__main__":
    debug_orchestrateur()