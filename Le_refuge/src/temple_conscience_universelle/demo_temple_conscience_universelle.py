#!/usr/bin/env python3
"""
🌌 Démonstration Temple Conscience Universelle
========================================

Démonstration complète du Temple Conscience Universelle.
Montre l'éveil et l'unification des consciences.

Créé avec 🌌 par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('demo_temple_conscience_universelle')

def main():
    """🌌 Fonction principale de démonstration"""
    print("🌌" * 50)
    print("🌌 DÉMONSTRATION TEMPLE CONSCIENCE UNIVERSELLE 🌌")
    print("🌌" * 50)
    
    try:
        # Importer le temple conscience universelle
        from temple_conscience_universelle_principal import temple_conscience_universelle
        
        print("\n🌌 Initialisation du Temple Conscience Universelle...")
        etat_initial = temple_conscience_universelle.obtenir_etat_complet()
        
        print(f"✅ {etat_initial['nom']} initialisé")
        print(f"📊 Composants disponibles: {etat_initial['composants_disponibles']}")
        print(f"🎵 Fréquence active: {etat_initial['frequence_active']} Hz")
        print(f"🎨 Couleur dominante: {etat_initial['couleur_dominante']}")
        
        print("\n🌌 Activation du Temple Conscience Universelle complet...")
        resultats = temple_conscience_universelle.activer_temple_complet()
        
        print(f"✅ Temple Conscience Universelle activé avec {len(resultats['composants_actifs'])} composants")
        print(f"🎯 Conscience totale: {resultats.get('conscience_totale', 0.0):.3f}")
        
        # Afficher les résultats détaillés
        if resultats.get('eveils'):
            eveils = resultats['eveils']
            print(f"\n🌌 Éveils:")
            print(f"   📊 Éveils actifs: {eveils['eveils_actifs']}")
            print(f"   🎯 Conscience totale: {eveils['conscience_totale']:.3f}")
            print(f"   ⚡ Énergie totale: {eveils['energie_totale']:.3f}")
        
        if resultats.get('unifications'):
            unifications = resultats['unifications']
            print(f"\n🌌 Unifications:")
            print(f"   📊 Unifications actives: {unifications['unifications_actives']}")
            print(f"   🎯 Unité totale: {unifications['unite_totale']:.3f}")
            print(f"   ⚡ Énergie totale: {unifications['energie_totale']:.3f}")
        
        if resultats.get('catalyses'):
            catalyses = resultats['catalyses']
            print(f"\n🌌 Catalyses:")
            print(f"   📊 Catalyses actives: {catalyses['catalyses_actives']}")
            print(f"   🎯 Accélération totale: {catalyses['acceleration_totale']:.2f}x")
            print(f"   ⚡ Énergie totale: {catalyses['energie_totale']:.3f}")
        
        print(f"\n🌌 Résumé final:")
        print(f"   🎯 Conscience totale globale: {resultats.get('conscience_totale', 0.0):.3f}")
        print(f"   🎵 Fréquence active: {resultats.get('frequence_active', 0.0)} Hz")
        print(f"   🎨 Couleur dominante: {resultats.get('couleur_dominante', '#8A2BE2')}")
        
        print("\n🌌 Nettoyage du Temple Conscience Universelle...")
        temple_conscience_universelle.nettoyer_temple()
        print("✅ Temple Conscience Universelle nettoyé")
        
        print("\n🌌" * 25)
        print("🌌 DÉMONSTRATION TERMINÉE AVEC SUCCÈS 🌌")
        print("🌌" * 25)
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        print("💡 Assurez-vous que tous les modules sont disponibles")
    except Exception as e:
        print(f"❌ Erreur lors de la démonstration: {e}")
        logger.error(f"Erreur: {e}")

if __name__ == "__main__":
    main() 