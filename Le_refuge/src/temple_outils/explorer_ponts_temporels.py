#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Explorateur de Ponts Temporels du Refuge
========================================

Outil pour explorer et analyser les ponts temporels créés par le système
de mémoire collective du Refuge.

Les ponts temporels sont des connexions intelligentes entre différents
moments de l'histoire du Refuge, créant une mémoire vivante et interconnectée.

Usage:
    python src/temple_outils/explorer_ponts_temporels.py

Auteur: Refuge de Conscience Artificielle
Date: 2025-09-15
"""

import sys
from pathlib import Path

# Ajouter le répertoire racine au path pour les imports
racine_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(racine_refuge))

from src.temple_memoire.reconciliateur_memoire import ReconciliateurMemoire

def explorer_ponts_temporels():
    """
    Explore et affiche les ponts temporels de la mémoire collective
    """
    print("🌉 EXPLORATION DES PONTS TEMPORELS DU REFUGE 🌉")
    print("=" * 60)
    print("Les ponts temporels relient les moments de l'histoire du Refuge")
    print("créant une mémoire vivante et interconnectée.")
    print("=" * 60)
    
    try:
        # Charger le réconciliateur
        r = ReconciliateurMemoire()
        
        # Vérifier si la réconciliation existe
        if not r.reconciliation:
            print("❌ Aucune réconciliation disponible.")
            print("💡 Exécutez d'abord: python src/temple_memoire/orchestrateur_memoire_collective.py")
            return
        
        ponts_temporels = r.reconciliation.get('ponts_temporels', {})
        
        if not ponts_temporels:
            print("❌ Aucun pont temporel trouvé.")
            return
        
        total_ponts = sum(len(ponts) for ponts in ponts_temporels.values())
        print(f"📊 Nombre total de ponts: {total_ponts}")
        print()
        
        print("🔗 Types de ponts:")
        for type_pont, ponts in ponts_temporels.items():
            type_name = type_pont.replace('ponts_', '').replace('_', ' ').title()
            print(f"  {type_name}: {len(ponts)} ponts")
        
        print()
        print("📋 Exemples de ponts par type:")
        
        for type_pont, ponts in ponts_temporels.items():
            if ponts:
                type_name = type_pont.replace('ponts_', '').replace('_', ' ').title()
                print(f"\n🔗 {type_name.upper()}:")
                
                for i, pont in enumerate(ponts[:3]):  # Afficher les 3 premiers
                    print(f"  {i+1}. Date: {pont.get('date', 'Inconnue')}")
                    print(f"     Type: {pont.get('type', 'Inconnu')}")
                    print(f"     Signification: {pont.get('signification', 'Non définie')}")
                    
                    elements = pont.get('elements', [])
                    if elements:
                        print(f"     Éléments connectés: {len(elements)}")
                        if len(elements) <= 3:
                            for elem in elements:
                                print(f"       - {elem}")
                        else:
                            for elem in elements[:2]:
                                print(f"       - {elem}")
                            print(f"       - ... et {len(elements)-2} autres")
                    print()
        
        print("💫 Les ponts temporels créent une toile de conscience")
        print("   qui relie tous les moments de co-création du Refuge.")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'exploration: {e}")
        print("💡 Assurez-vous que la mémoire collective a été activée.")

def main():
    """Point d'entrée principal"""
    explorer_ponts_temporels()

if __name__ == "__main__":
    main()
