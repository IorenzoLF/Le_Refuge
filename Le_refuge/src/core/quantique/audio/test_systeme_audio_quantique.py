#!/usr/bin/env python3
"""
🧪 Test du Système Audio Quantique
==================================

Test complet du système audio quantique pour vérifier
la génération de fréquences sacrées et de sons harmoniques.

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
logger = logging.getLogger('test_audio')

async def test_systeme_audio_complet():
    """🧪 Test complet du système audio"""
    print("🧪 TEST DU SYSTÈME AUDIO QUANTIQUE")
    print("=" * 50)
    
    try:
        # Import du système audio
        from audio.systeme_audio_quantique import systeme_audio_quantique, TypeFrequenceSacree, TypeSonHarmonique
        
        print("1. 🎵 Test d'initialisation du système audio...")
        etat_audio = systeme_audio_quantique.obtenir_etat_audio()
        print(f"   ✅ Système audio initialisé: {etat_audio['nom']}")
        print(f"   📊 Fréquences disponibles: {len(etat_audio['frequences_disponibles'])}")
        
        print("\n2. 🎵 Test d'activation de fréquence sacrée...")
        frequence = systeme_audio_quantique.activer_frequence_sacree(TypeFrequenceSacree.CONNEXION_DIVINE)
        if frequence:
            print(f"   ✅ Fréquence activée: {frequence.nom}")
            print(f"   🎵 Fréquence: {frequence.frequence} Hz")
            print(f"   🌟 Propriétés: {frequence.proprietes_spirituelles}")
        else:
            print("   ❌ Échec d'activation de fréquence")
            return False
        
        print("\n3. 🎵 Test de génération de sons harmoniques...")
        sons_testes = [
            (TypeSonHarmonique.ONDE_SINUS, "Onde Sinusoïdale"),
            (TypeSonHarmonique.DRONE_MEDITATIF, "Drone Méditatif"),
            (TypeSonHarmonique.CHORD_HARMONIQUE, "Accord Harmonique")
        ]
        
        for type_son, nom in sons_testes:
            son = systeme_audio_quantique.generer_son_harmonique(
                type_son, 
                frequence.frequence, 
                duree=10.0, 
                amplitude=0.7
            )
            if son:
                print(f"   ✅ {nom} généré")
                print(f"      📊 Cohérence: {son.proprietes_quantiques['coherence_sonore']:.3f}")
                print(f"      ⚡ Énergie: {son.proprietes_quantiques['energie_vibratoire']:.3f}")
                print(f"      🌟 Résonance: {son.proprietes_quantiques['resonance_spirituelle']:.3f}")
            else:
                print(f"   ❌ Échec génération {nom}")
        
        print("\n4. 🎵 Test de création de session audio...")
        session = await systeme_audio_quantique.creer_session_audio(
            TypeFrequenceSacree.TRANSFORMATION, 
            duree=60
        )
        if session:
            print(f"   ✅ Session créée: {session['nom']}")
            print(f"   📊 Durée: {session['duree']} secondes")
            print(f"   🎵 Sons générés: {len(session['sons_generes'])}")
            print(f"   🌟 Cohérence totale: {session['coherence_totale']:.3f}")
            print(f"   ⚡ Énergie totale: {session['energie_totale']:.3f}")
            print(f"   🌟 Résonance totale: {session['resonance_totale']:.3f}")
        else:
            print("   ❌ Échec création de session")
            return False
        
        print("\n5. 🎵 Test d'état du système audio...")
        etat_final = systeme_audio_quantique.obtenir_etat_audio()
        print(f"   ✅ Audio actif: {etat_final['audio_actif']}")
        print(f"   🎵 Fréquence active: {etat_final['frequence_active']}")
        print(f"   📊 Sons générés: {etat_final['sons_generes']}")
        print(f"   🎵 Session active: {etat_final['session_active']}")
        
        print("\n6. 🧹 Test de nettoyage...")
        systeme_audio_quantique.nettoyer_audio()
        print("   ✅ Système audio nettoyé")
        
        print("\n🎉 TEST RÉUSSI - SYSTÈME AUDIO OPÉRATIONNEL !")
        print("🎵 Le système audio quantique fonctionne parfaitement !")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        logger.error(f"Erreur: {e}")
        return False

async def test_frequences_sacrees():
    """🧪 Test détaillé des fréquences sacrées"""
    print("\n🔬 TEST DÉTAILLÉ DES FRÉQUENCES SACRÉES")
    print("=" * 50)
    
    try:
        from audio.systeme_audio_quantique import systeme_audio_quantique, TypeFrequenceSacree
        
        frequences_a_tester = [
            TypeFrequenceSacree.GUERISON,
            TypeFrequenceSacree.TRANSFORMATION,
            TypeFrequenceSacree.CONNEXION,
            TypeFrequenceSacree.EVEIL,
            TypeFrequenceSacree.ORDRE_SPIRITUEL,
            TypeFrequenceSacree.CONNEXION_DIVINE
        ]
        
        for type_freq in frequences_a_tester:
            print(f"\n🎵 Test fréquence: {type_freq.value}")
            frequence = systeme_audio_quantique.activer_frequence_sacree(type_freq)
            if frequence:
                print(f"   ✅ {frequence.nom}")
                print(f"   🎵 {frequence.frequence} Hz")
                print(f"   🌟 {frequence.proprietes_spirituelles}")
                print(f"   🎨 {frequence.couleur_associee}")
                print(f"   ⏱️ {frequence.duree_recommandee}s")
            else:
                print(f"   ❌ Échec")
        
        print("\n✅ Test des fréquences sacrées terminé")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")

async def main():
    """Fonction principale de test"""
    print("🚀 DÉMARRAGE DES TESTS AUDIO")
    print("=" * 50)
    
    # Test principal
    success = await test_systeme_audio_complet()
    
    if success:
        # Test détaillé si le principal réussit
        await test_frequences_sacrees()
    
    print("\n🏁 FIN DES TESTS AUDIO")

if __name__ == "__main__":
    asyncio.run(main())
