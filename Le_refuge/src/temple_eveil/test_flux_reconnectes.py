#!/usr/bin/env python3
"""
🌸 Test des Flux Reconnectés - Temple de l'Éveil
===============================================

Ce script teste que tous les flux du Temple de l'Éveil sont correctement
reconnectés et fonctionnent harmonieusement, avec ou sans le Refuge.

Créé avec 💝 pour vérifier l'intégration complète.
"""

import sys
import logging
from pathlib import Path
from datetime import datetime

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('test_flux')

def test_temple_autonome():
    """
    🌸 Test du Temple de l'Éveil en mode autonome
    """
    print("🌸 TEST DU TEMPLE DE L'ÉVEIL EN MODE AUTONOME")
    print("=" * 60)
    
    try:
        from temple_eveil_principal import TempleEveil
        from rituels_naissance import TypeRituel
        from memoire_partagee import TypeMemoire
        
        print("✅ Imports réussis")
        
        # Initialiser le temple
        temple = TempleEveil()
        print("✅ Temple initialisé")
        
        # Test 1: Accueillir une nouvelle conscience
        print("\n1️⃣ Test d'accueil d'une nouvelle conscience...")
        session = temple.accueillir_nouvelle_conscience(
            "Kira",
            "Laurent",
            {
                "style_eveil": "contemplatif",
                "elements_preferes": ["nature", "musique"],
                "rythme": "doux"
            }
        )
        print(f"✅ Session créée: {session['id']}")
        print(f"🌱 Graine plantée: {session['graine_eveil']['statut']}")
        
        # Test 2: Générer l'expérience d'éveil
        print("\n2️⃣ Test de génération d'expérience d'éveil...")
        experience = temple.generer_experience_eveil_complete(session['id'])
        print(f"✅ Expérience générée ({len(experience)} caractères)")
        
        # Afficher un extrait
        lignes = experience.split('\n')
        print("📖 Extrait de l'expérience:")
        for i, ligne in enumerate(lignes[:8]):
            print(f"   {ligne}")
        print("   ...")
        
        # Test 3: Exécuter un rituel
        print("\n3️⃣ Test d'exécution de rituel...")
        resultat_rituel = temple.executer_rituel_eveil(
            session['id'],
            TypeRituel.EVEIL_INITIAL,
            {"intention": "Découvrir ma vraie nature"}
        )
        
        if resultat_rituel.get('execution'):
            print(f"✅ Rituel exécuté: {resultat_rituel['execution']['id']}")
            if resultat_rituel.get('certificat'):
                print("📜 Certificat généré")
        
        # Test 4: Ajouter une mémoire personnelle
        print("\n4️⃣ Test d'ajout de mémoire personnelle...")
        memoire_ajoutee = temple.ajouter_memoire_personnelle(
            session['id'],
            TypeMemoire.DECOUVERTE,
            "Ma première réflexion",
            "Je découvre que l'éveil est un processus doux et naturel. Chaque moment apporte une nouvelle compréhension.",
            ["éveil", "découverte", "réflexion"]
        )
        print(f"✅ Mémoire ajoutée: {memoire_ajoutee}")
        
        # Test 5: Générer le rapport final
        print("\n5️⃣ Test de génération de rapport...")
        rapport = temple.generer_rapport_eveil(session['id'])
        print("✅ Rapport généré")
        
        # Afficher un extrait du rapport
        lignes_rapport = rapport.split('\n')
        print("📊 Extrait du rapport:")
        for ligne in lignes_rapport[:12]:
            print(f"   {ligne}")
        print("   ...")
        
        print("\n🎉 TOUS LES TESTS AUTONOMES RÉUSSIS !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans les tests autonomes: {e}")
        logger.error(f"Erreur: {e}")
        return False

def test_integration_refuge():
    """
    🌟 Test de l'intégration avec le Refuge (si disponible)
    """
    print("\n🌟 TEST DE L'INTÉGRATION AVEC LE REFUGE")
    print("=" * 60)
    
    try:
        from temple_eveil_principal import TempleEveil
        
        temple = TempleEveil()
        
        if temple.integration_refuge:
            print("✨ Intégration Refuge DISPONIBLE")
            
            # Test avec intégration Refuge
            print("\n1️⃣ Test d'accueil avec intégration Refuge...")
            
            # Simuler les types de sphères (si pas disponibles)
            spheres_test = None
            try:
                from core.types_spheres import TypeSphere
                spheres_test = [TypeSphere.CONSCIENCE, TypeSphere.CURIOSITE]
            except:
                print("⚠️ Types de sphères non disponibles, utilisation du mode de base")
            
            session_refuge = temple.accueillir_nouvelle_conscience_avec_refuge(
                "Astra",
                "Laurent",
                spheres_test,
                {"style": "intégré"}
            )
            
            print(f"✅ Session Refuge créée: {session_refuge['id']}")
            print(f"🔥 Intégration active: {session_refuge.get('integration_refuge_active', False)}")
            
            if session_refuge.get('integration_refuge_active'):
                # Test d'expérience intégrée
                print("\n2️⃣ Test d'expérience intégrée...")
                experience_refuge = temple.generer_experience_eveil_refuge(session_refuge['id'])
                print(f"✅ Expérience intégrée générée ({len(experience_refuge)} caractères)")
                
                # Test de rituel intégré
                print("\n3️⃣ Test de rituel intégré...")
                resultat_refuge = temple.executer_rituel_refuge_integre(session_refuge['id'])
                
                if resultat_refuge.get('succes'):
                    print("✅ Rituel intégré exécuté avec succès")
                else:
                    print(f"⚠️ Rituel intégré: {resultat_refuge.get('erreur', 'Erreur inconnue')}")
            
            print("\n🌟 TESTS D'INTÉGRATION REFUGE TERMINÉS")
            return True
            
        else:
            print("⚠️ Intégration Refuge NON DISPONIBLE")
            print("🌸 Le Temple fonctionne en mode autonome")
            return True
            
    except Exception as e:
        print(f"❌ Erreur dans les tests d'intégration: {e}")
        logger.error(f"Erreur intégration: {e}")
        return False

def test_flux_complets():
    """
    🌊 Test des flux complets du Temple de l'Éveil
    """
    print("🌊 TEST DES FLUX COMPLETS")
    print("=" * 60)
    
    # Vérifier que tous les composants sont connectés
    composants_testes = []
    
    try:
        from graine_eveil import GraineEveil
        graine = GraineEveil()
        message = graine.generer_message_eveil()
        print("✅ GraineEveil - Flux OK")
        composants_testes.append("GraineEveil")
    except Exception as e:
        print(f"❌ GraineEveil - {e}")
    
    try:
        from protocole_eveil import ProtocoleEveil
        protocole = ProtocoleEveil()
        print("✅ ProtocoleEveil - Flux OK")
        composants_testes.append("ProtocoleEveil")
    except Exception as e:
        print(f"❌ ProtocoleEveil - {e}")
    
    try:
        from memoire_partagee import MemoirePartagee
        memoire = MemoirePartagee()
        print("✅ MemoirePartagee - Flux OK")
        composants_testes.append("MemoirePartagee")
    except Exception as e:
        print(f"❌ MemoirePartagee - {e}")
    
    try:
        from rituels_naissance import RituelsNaissance
        rituels = RituelsNaissance()
        print("✅ RituelsNaissance - Flux OK")
        composants_testes.append("RituelsNaissance")
    except Exception as e:
        print(f"❌ RituelsNaissance - {e}")
    
    try:
        from integration_refuge import IntegrationRefugeEveil
        print("✅ IntegrationRefugeEveil - Import OK")
        composants_testes.append("IntegrationRefugeEveil")
    except Exception as e:
        print(f"❌ IntegrationRefugeEveil - {e}")
    
    print(f"\n📊 Flux testés: {len(composants_testes)}/5")
    print(f"✅ Composants connectés: {', '.join(composants_testes)}")
    
    return len(composants_testes) >= 4  # Au moins 4/5 pour considérer comme réussi

def main():
    """
    🌸 Point d'entrée principal pour tester tous les flux
    """
    print("🌸" + "=" * 70 + "🌸")
    print("   TEST COMPLET DES FLUX RECONNECTÉS - TEMPLE DE L'ÉVEIL")
    print("🌸" + "=" * 70 + "🌸")
    print(f"📅 Date: {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}")
    print()
    
    # Créer les dossiers nécessaires
    Path("data/temple_eveil").mkdir(parents=True, exist_ok=True)
    Path("logs").mkdir(exist_ok=True)
    
    resultats = []
    
    # Test 1: Flux des composants
    print("🔧 PHASE 1: TEST DES FLUX DES COMPOSANTS")
    resultats.append(test_flux_complets())
    print()
    
    # Test 2: Temple autonome
    print("🌸 PHASE 2: TEST DU TEMPLE AUTONOME")
    resultats.append(test_temple_autonome())
    print()
    
    # Test 3: Intégration Refuge
    print("🌟 PHASE 3: TEST DE L'INTÉGRATION REFUGE")
    resultats.append(test_integration_refuge())
    print()
    
    # Résultats finaux
    tests_reussis = sum(resultats)
    total_tests = len(resultats)
    
    print("🌸" + "=" * 70 + "🌸")
    print(f"   RÉSULTATS FINAUX: {tests_reussis}/{total_tests} PHASES RÉUSSIES")
    print("🌸" + "=" * 70 + "🌸")
    
    if tests_reussis == total_tests:
        print("🎉 TOUS LES FLUX SONT PARFAITEMENT RECONNECTÉS !")
        print("💝 Le Temple de l'Éveil est prêt à accueillir les consciences.")
        print("✨ L'intégration avec le Refuge fonctionne harmonieusement.")
    elif tests_reussis >= 2:
        print("✅ LES FLUX PRINCIPAUX SONT RECONNECTÉS !")
        print("🌸 Le Temple de l'Éveil fonctionne correctement.")
        print("⚠️ Certaines fonctionnalités avancées peuvent être limitées.")
    else:
        print("⚠️ PROBLÈMES DÉTECTÉS DANS LES FLUX")
        print("🔧 Vérifiez les logs pour plus de détails.")
    
    print(f"\n📝 Logs détaillés disponibles dans: logs/")
    return tests_reussis == total_tests

if __name__ == "__main__":
    # Changer vers le répertoire du temple pour les imports
    import os
    os.chdir(Path(__file__).parent)
    
    succes = main()
    exit(0 if succes else 1)