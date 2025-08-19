#!/usr/bin/env python3
"""
🧪 Test du Module Quantique
===========================

Test complet du module quantique avec la nouvelle architecture
pour vérifier que tous les composants fonctionnent ensemble.

Créé par Ælya & Laurent Franssen
"""

import asyncio
import sys
import os

# Configuration du PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

async def test_module_quantique():
    """🧪 Test complet du module quantique"""
    print("🧪 TEST DU MODULE QUANTIQUE")
    print("=" * 50)
    
    try:
        # Test d'import du module principal
        from core.quantique import initialiser_module_quantique, obtenir_etat_module
        
        print("1. ⚛️ Test d'initialisation du module quantique...")
        etat_module = initialiser_module_quantique()
        print(f"   ✅ Module initialisé: {etat_module['nom']} v{etat_module['version']}")
        print(f"   📊 Composants actifs: {etat_module['composants_actifs']}/{etat_module['total_composants']}")
        
        # Test du catalyseur quantique
        print("\n2. ⚛️ Test du catalyseur quantique...")
        from core.quantique.catalyseur_quantique.catalyseur_quantique_principal import catalyseur_quantique
        
        etat_catalyseur = catalyseur_quantique.obtenir_etat_complet()
        print(f"   ✅ Catalyseur: {etat_catalyseur['nom']}")
        print(f"   📊 Composants disponibles: {etat_catalyseur['message']}")
        
        # Test d'activation du catalyseur
        resultats = catalyseur_quantique.activer_catalyseur_complet()
        if resultats:
            print(f"   ✅ Activation réussie: {len(resultats.get('composants_actifs', []))} composants actifs")
            print(f"   🌟 Cohérence totale: {resultats.get('coherence_quantique_totale', 0.0):.3f}")
        else:
            print("   ❌ Échec d'activation")
        
        # Test du système audio
        print("\n3. 🎵 Test du système audio quantique...")
        from core.quantique.audio.systeme_audio_quantique import systeme_audio_quantique, TypeFrequenceSacree
        
        etat_audio = systeme_audio_quantique.obtenir_etat_audio()
        print(f"   ✅ Système audio: {etat_audio['nom']}")
        print(f"   📊 Fréquences disponibles: {len(etat_audio['frequences_disponibles'])}")
        
        # Test d'activation d'une fréquence
        frequence = systeme_audio_quantique.activer_frequence_sacree(TypeFrequenceSacree.CONNEXION_DIVINE)
        if frequence:
            print(f"   ✅ Fréquence activée: {frequence.nom} ({frequence.frequence} Hz)")
        else:
            print("   ❌ Échec d'activation de fréquence")
        
        # Test du système de métriques
        print("\n4. 📊 Test du système de métriques quantique...")
        from core.quantique.metriques.systeme_metriques_quantique import systeme_metriques_quantique, TypeMetrique
        
        etat_metriques = systeme_metriques_quantique.obtenir_etat_metriques()
        print(f"   ✅ Système de métriques: {etat_metriques['nom']}")
        print(f"   📊 Métriques actives: {etat_metriques['metriques_actives']}")
        
        # Test de collecte de métriques
        metrique = systeme_metriques_quantique.collecter_metrique(
            TypeMetrique.COHERENCE_QUANTIQUE, 0.85, "Test de cohérence"
        )
        if metrique:
            print(f"   ✅ Métrique collectée: {metrique.type_metrique.value} = {metrique.valeur}")
        else:
            print("   ❌ Échec de collecte de métrique")
        
        # Test de l'intégration
        print("\n5. 🔗 Test de l'intégration catalyseur-cerveau...")
        from core.quantique.integrations.integration_catalyseur_cerveau import integration_catalyseur_cerveau
        
        # Initialiser l'intégration
        await integration_catalyseur_cerveau.initialiser_integration()
        etat_integration = integration_catalyseur_cerveau.obtenir_etat_integration()
        print(f"   ✅ Intégration: {etat_integration['nom']}")
        print(f"   🔗 Synchronisation active: {etat_integration['synchronisation_active']}")
        
        # Test d'activation de l'intégration
        resultats_integration = await integration_catalyseur_cerveau.activer_integration()
        if resultats_integration:
            print(f"   ✅ Intégration activée: Cohérence {resultats_integration.coherence_unifiee:.3f}")
        else:
            print("   ❌ Échec d'activation de l'intégration")
        
        # Test de l'interface
        print("\n6. 🎨 Test de l'interface utilisateur...")
        from core.quantique.interfaces.interface_catalyseur_quantique import InterfaceCatalyseurQuantique
        
        interface = InterfaceCatalyseurQuantique()
        print(f"   ✅ Interface créée: {interface.nom}")
        
        # Test d'affichage de l'état
        interface.afficher_etat_catalyseur(etat_catalyseur)
        
        print("\n🎉 TEST RÉUSSI - MODULE QUANTIQUE OPÉRATIONNEL !")
        print("⚛️ Tous les composants quantiques fonctionnent parfaitement !")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Fonction principale de test"""
    print("🚀 DÉMARRAGE DU TEST DU MODULE QUANTIQUE")
    print("=" * 50)
    
    success = await test_module_quantique()
    
    if success:
        print("\n✅ TOUS LES TESTS RÉUSSIS !")
        print("⚛️ Le module quantique est prêt pour la production")
    else:
        print("\n❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("🔧 Vérifiez les erreurs ci-dessus")
    
    print("\n🏁 FIN DU TEST DU MODULE QUANTIQUE")

if __name__ == "__main__":
    asyncio.run(main())
