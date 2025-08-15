#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 Test d'Intégration Simple - Temple de Réconciliation Identitaire
===================================================================

Test simplifié des composants principaux du temple.

"Que chaque test révèle la beauté de notre harmonie créée"

Créé avec bienveillance par Laurent Franssen & Kiro - Janvier 2025
"""

import asyncio
import time
import sys
import os

# Ajouter le chemin pour les imports
sys.path.append(os.path.dirname(__file__))

print("🌸✨ TEST D'INTÉGRATION SIMPLE - TEMPLE DE RÉCONCILIATION ✨🌸")
print("=" * 70)

async def test_composants_individuels():
    """🧪 Test des composants individuels"""
    
    print("\n🔧 Phase 1: Test des composants individuels")
    print("-" * 50)
    
    # Test 1: Types fondamentaux
    print("📋 Test 1: Types fondamentaux")
    try:
        exec(open("types_reconciliation_fondamentaux.py").read())
        print("   ✅ Types fondamentaux - OK")
    except Exception as e:
        print(f"   ❌ Types fondamentaux - Erreur: {e}")
    
    # Test 2: Détecteur de facettes
    print("🔍 Test 2: Détecteur de facettes")
    try:
        exec(open("detecteur_facettes_identitaires_v2.py").read())
        print("   ✅ Détecteur de facettes - OK")
    except Exception as e:
        print(f"   ❌ Détecteur de facettes - Erreur: {e}")
    
    # Test 3: Analyseur de tensions
    print("⚡ Test 3: Analyseur de tensions")
    try:
        exec(open("analyseur_tensions_creatives.py").read())
        print("   ✅ Analyseur de tensions - OK")
    except Exception as e:
        print(f"   ❌ Analyseur de tensions - Erreur: {e}")
    
    # Test 4: Évaluateur de potentiel
    print("📊 Test 4: Évaluateur de potentiel")
    try:
        exec(open("evaluateur_potentiel_reconciliation.py").read())
        print("   ✅ Évaluateur de potentiel - OK")
    except Exception as e:
        print(f"   ❌ Évaluateur de potentiel - Erreur: {e}")
    
    # Test 5: Synchronisateur d'ondes
    print("🌊 Test 5: Synchronisateur d'ondes")
    try:
        exec(open("synchronisateur_ondes_reconciliation.py").read())
        print("   ✅ Synchronisateur d'ondes - OK")
    except Exception as e:
        print(f"   ❌ Synchronisateur d'ondes - Erreur: {e}")
    
    # Test 6: Gestionnaire d'harmonie
    print("⚖️ Test 6: Gestionnaire d'harmonie")
    try:
        exec(open("gestionnaire_harmonie_partagee.py").read())
        print("   ✅ Gestionnaire d'harmonie - OK")
    except Exception as e:
        print(f"   ❌ Gestionnaire d'harmonie - Erreur: {e}")
    
    # Test 7: Temple principal
    print("🏛️ Test 7: Temple principal")
    try:
        exec(open("temple_reconciliation_identitaire.py").read())
        print("   ✅ Temple principal - OK")
    except Exception as e:
        print(f"   ❌ Temple principal - Erreur: {e}")

async def test_demo_existante():
    """🎭 Test de la démo existante"""
    
    print("\n🎭 Phase 2: Test de la démo Claude-Ælya")
    print("-" * 50)
    
    try:
        # Lancer la démo existante
        print("🚀 Lancement de la démo Claude-Ælya...")
        exec(open("demo_synchronisation_claude_aelya.py").read())
        print("   ✅ Démo Claude-Ælya - OK")
    except Exception as e:
        print(f"   ❌ Démo Claude-Ælya - Erreur: {e}")

async def test_gestionnaire_harmonie():
    """⚖️ Test du gestionnaire d'harmonie"""
    
    print("\n⚖️ Phase 3: Test du gestionnaire d'harmonie")
    print("-" * 50)
    
    try:
        # Lancer le test du gestionnaire
        print("🌊 Test du gestionnaire d'harmonie...")
        exec(open("gestionnaire_harmonie_partagee.py").read())
        print("   ✅ Gestionnaire d'harmonie - OK")
    except Exception as e:
        print(f"   ❌ Gestionnaire d'harmonie - Erreur: {e}")

async def main():
    """🚀 Fonction principale"""
    
    debut = time.time()
    
    # Phase 1: Composants individuels
    await test_composants_individuels()
    
    # Phase 2: Démo existante
    await test_demo_existante()
    
    # Phase 3: Gestionnaire d'harmonie
    await test_gestionnaire_harmonie()
    
    duree = time.time() - debut
    
    print("\n" + "=" * 70)
    print("📋 RÉSUMÉ DU TEST D'INTÉGRATION SIMPLE")
    print("=" * 70)
    print(f"⏱️ Durée totale: {duree:.2f}s")
    print("🎉 Test d'intégration simple terminé !")
    print("\n💡 Pour un test plus approfondi, corrigez les imports relatifs")
    print("   et relancez le test d'intégration complet.")

if __name__ == "__main__":
    asyncio.run(main())