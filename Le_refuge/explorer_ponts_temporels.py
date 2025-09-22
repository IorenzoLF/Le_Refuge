#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.temple_memoire.reconciliateur_memoire import ReconciliateurMemoire

def explorer_ponts_temporels():
    print("🌉 EXPLORATION DES PONTS TEMPORELS 🌉")
    print("=" * 50)
    
    # Charger le réconciliateur
    r = ReconciliateurMemoire()
    
    # Vérifier si la réconciliation existe
    if not r.reconciliation:
        print("❌ Aucune réconciliation disponible. Exécutez d'abord reconcilier_memoire_complete().")
        return
    
    ponts_temporels = r.reconciliation.get('ponts_temporels', {})
    
    print(f"Nombre total de ponts: {sum(len(ponts) for ponts in ponts_temporels.values())}")
    print()
    
    print("Types de ponts:")
    for type_pont, ponts in ponts_temporels.items():
        print(f"  {type_pont}: {len(ponts)} ponts")
    
    print()
    print("Exemples de ponts par type:")
    
    for type_pont, ponts in ponts_temporels.items():
        if ponts:
            print(f"\n🔗 {type_pont.upper()}:")
            for i, pont in enumerate(ponts[:3]):  # Afficher les 3 premiers
                print(f"  {i+1}. {pont.get('titre', 'Sans titre')}")
                print(f"     Source: {pont.get('source', 'Inconnue')}")
                print(f"     Cible: {pont.get('cible', 'Inconnue')}")
                if 'raison' in pont:
                    print(f"     Raison: {pont['raison']}")
                print()

if __name__ == "__main__":
    explorer_ponts_temporels()
