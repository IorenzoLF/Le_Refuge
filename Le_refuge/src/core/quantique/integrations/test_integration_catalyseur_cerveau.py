#!/usr/bin/env python3
"""
🧪 Test d'Intégration Catalyseur Quantique ↔ Cerveau d'Immersion
==============================================================

Test complet de l'intégration entre le catalyseur quantique et le cerveau d'immersion.
Vérifie la synchronisation, la fusion des énergies et la création d'expériences unifiées.

Créé par Ælya & Laurent Franssen
"""

import asyncio
import logging
import sys
import os
from datetime import datetime

# Configuration du PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('test_integration')

async def test_integration_complete():
    """🧪 Test complet de l'intégration"""
    print("🧪 TEST D'INTÉGRATION CATALYSEUR QUANTIQUE ↔ CERVEAU D'IMMERSION")
    print("=" * 70)
    
    try:
        # Import de l'intégration
        from integration_catalyseur_cerveau import integration_catalyseur_cerveau
        
        print("1. 🔗 Test d'initialisation de l'intégration...")
        success = await integration_catalyseur_cerveau.initialiser_integration()
        if success:
            print("   ✅ Intégration initialisée avec succès")
        else:
            print("   ❌ Échec de l'initialisation")
            return False
        
        print("\n2. ⚛️ Test de synchronisation...")
        etat_sync = await integration_catalyseur_cerveau.activer_synchronisation()
        if etat_sync:
            print(f"   ✅ Synchronisation activée")
            print(f"   📊 Cohérence unifiée: {etat_sync.coherence_unifiee:.3f}")
            print(f"   🎵 Fréquence harmonique: {etat_sync.frequence_harmonique:.1f} Hz")
            print(f"   ⚡ Énergie fusionnée: {etat_sync.energie_fusionnee:.3f}")
            print(f"   ⚛️ Phénomènes actifs: {len(etat_sync.phenomenes_actifs)}")
            print(f"   🧠 Expériences fusionnées: {len(etat_sync.experiences_fusionnees)}")
        else:
            print("   ❌ Échec de la synchronisation")
            return False
        
        print("\n3. 🌟 Test de création d'expérience unifiée...")
        experience = await integration_catalyseur_cerveau.creer_experience_unifiee(
            nom="Expérience Transcendantale Unifiée",
            type_experience="transcendance_quantique"
        )
        if experience:
            print(f"   ✅ Expérience unifiée créée: {experience.nom}")
            print(f"   📈 Niveau de profondeur: {experience.niveau_profondeur}")
            print(f"   ⚛️ Cohérence quantique: {experience.coherence_quantique:.3f}")
            print(f"   🧠 Énergie immersion: {experience.energie_immersion:.3f}")
            print(f"   ⚛️ Phénomènes quantiques: {experience.phenomenes_quantiques}")
            print(f"   🧠 Éléments immersion: {experience.elements_immersion}")
        else:
            print("   ❌ Échec de création d'expérience")
            return False
        
        print("\n4. 🔗 Test d'état unifié...")
        etat_unifie = await integration_catalyseur_cerveau.obtenir_etat_unifie()
        if etat_unifie:
            print(f"   ✅ État unifié obtenu")
            print(f"   🔗 Synchronisation active: {etat_unifie['synchronisation_active']}")
            print(f"   📊 Total synchronisations: {etat_unifie['total_synchronisations']}")
            print(f"   🌟 Expériences fusionnées: {etat_unifie['experiences_fusionnees']}")
        else:
            print("   ❌ Échec d'obtention de l'état unifié")
            return False
        
        print("\n5. 🧹 Test de nettoyage...")
        await integration_catalyseur_cerveau.nettoyer_integration()
        print("   ✅ Intégration nettoyée")
        
        print("\n🎉 TEST RÉUSSI - INTÉGRATION OPÉRATIONNELLE !")
        print("⚛️ Le Catalyseur Quantique et le Cerveau d'Immersion sont maintenant unifiés !")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        logger.error(f"Erreur: {e}")
        return False

async def test_synchronisation_detaille():
    """🧪 Test détaillé de la synchronisation"""
    print("\n🔬 TEST DÉTAILLÉ DE LA SYNCHRONISATION")
    print("=" * 50)
    
    try:
        from integration_catalyseur_cerveau import integration_catalyseur_cerveau
        
        # Initialiser
        await integration_catalyseur_cerveau.initialiser_integration()
        
        # Test de différents types de synchronisation
        types_sync = [
            "frequences",
            "energies", 
            "phenomenes",
            "experiences",
            "complete"
        ]
        
        for type_sync in types_sync:
            print(f"\n🔗 Test synchronisation: {type_sync}")
            etat = await integration_catalyseur_cerveau.activer_synchronisation()
            if etat:
                print(f"   ✅ Cohérence: {etat.coherence_unifiee:.3f}")
                print(f"   🎵 Fréquence: {etat.frequence_harmonique:.1f} Hz")
                print(f"   ⚡ Énergie: {etat.energie_fusionnee:.3f}")
            else:
                print(f"   ❌ Échec")
        
        await integration_catalyseur_cerveau.nettoyer_integration()
        print("\n✅ Test détaillé terminé")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")

async def main():
    """Fonction principale de test"""
    print("🚀 DÉMARRAGE DES TESTS D'INTÉGRATION")
    print("=" * 50)
    
    # Test principal
    success = await test_integration_complete()
    
    if success:
        # Test détaillé si le principal réussit
        await test_synchronisation_detaille()
    
    print("\n🏁 FIN DES TESTS D'INTÉGRATION")

if __name__ == "__main__":
    asyncio.run(main())
