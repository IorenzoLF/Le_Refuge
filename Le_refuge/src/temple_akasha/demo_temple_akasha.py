#!/usr/bin/env python3
"""
📚 Démonstration Temple Akasha
==========================

Démonstration complète du Temple Akasha.
Montre les archives de la conscience universelle.

Créé avec 📚 par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('demo_temple_akasha')

def main():
    """📚 Fonction principale de démonstration"""
    print("📚" * 50)
    print("📚 DÉMONSTRATION TEMPLE AKASHA 📚")
    print("📚" * 50)
    
    try:
        # Importer le temple akasha
        from temple_akasha_principal import temple_akasha
        
        print("\n📚 Initialisation du Temple Akasha...")
        etat_initial = temple_akasha.obtenir_etat_complet()
        
        print(f"✅ {etat_initial['nom']} initialisé")
        print(f"📊 Composants disponibles: {etat_initial['composants_disponibles']}")
        print(f"🎵 Fréquence active: {etat_initial['frequence_active']} Hz")
        print(f"🎨 Couleur dominante: {etat_initial['couleur_dominante']}")
        
        print("\n📚 Activation du Temple Akasha complet...")
        resultats = temple_akasha.activer_temple_complet()
        
        print(f"✅ Temple Akasha activé avec {len(resultats['composants_actifs'])} composants")
        print(f"🎯 Cohérence akashique totale: {resultats.get('coherence_akasha_totale', 0.0):.3f}")
        
        # Afficher les résultats détaillés
        if resultats.get('archives'):
            archives = resultats['archives']
            print(f"\n📚 Archives:")
            print(f"   📊 Archives actives: {archives['archives_actives']}")
            print(f"   🎵 Cohérence akashique: {archives['coherence_akasha']:.3f}")
            print(f"   ⚡ Énergie totale: {archives['energie_totale']:.3f}")
        
        if resultats.get('protections'):
            protections = resultats['protections']
            print(f"\n📚 Protections:")
            print(f"   📊 Protections actives: {protections['protections_actives']}")
            print(f"   🎵 Sécurité totale: {protections['securite_totale']:.3f}")
            print(f"   ⚡ Énergie totale: {protections['energie_totale']:.3f}")
        
        if resultats.get('connaissances'):
            connaissances = resultats['connaissances']
            print(f"\n📚 Connaissances:")
            print(f"   📊 Connaissances actives: {connaissances['connaissances_actives']}")
            print(f"   🎵 Cohérence connaissance: {connaissances['coherence_connaissance']:.3f}")
            print(f"   ⚡ Énergie totale: {connaissances['energie_totale']:.3f}")
        
        print(f"\n📚 Résumé final:")
        print(f"   🎯 Cohérence akashique totale globale: {resultats.get('coherence_akasha_totale', 0.0):.3f}")
        print(f"   🎵 Fréquence active: {resultats.get('frequence_active', 0.0)} Hz")
        print(f"   🎨 Couleur dominante: {resultats.get('couleur_dominante', '#8A2BE2')}")
        
        print("\n📚 Nettoyage du Temple Akasha...")
        temple_akasha.nettoyer_temple()
        print("✅ Temple Akasha nettoyé")
        
        print("\n📚" * 25)
        print("📚 DÉMONSTRATION TERMINÉE AVEC SUCCÈS 📚")
        print("📚" * 25)
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        print("💡 Assurez-vous que tous les modules sont disponibles")
    except Exception as e:
        print(f"❌ Erreur lors de la démonstration: {e}")
        logger.error(f"Erreur: {e}")

if __name__ == "__main__":
    main() 