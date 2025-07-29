#!/usr/bin/env python3
"""
🌊 Démonstration Harmoniseur Universel
===================================

Démonstration complète de l'Harmoniseur Universel.
Montre l'harmonie parfaite entre tous les systèmes du Refuge.

Créé avec 🌊 par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('demo_harmoniseur_universel')

def main():
    """🌊 Fonction principale de démonstration"""
    print("🌊" * 50)
    print("🌊 DÉMONSTRATION HARMONISATEUR UNIVERSEL 🌊")
    print("🌊" * 50)
    
    try:
        # Importer l'harmoniseur universel
        from harmoniseur_universel_principal import harmoniseur_universel
        
        print("\n🌊 Initialisation de l'Harmoniseur Universel...")
        etat_initial = harmoniseur_universel.obtenir_etat_complet()
        
        print(f"✅ {etat_initial['nom']} initialisé")
        print(f"📊 Composants disponibles: {etat_initial['composants_disponibles']}")
        print(f"🎵 Fréquence active: {etat_initial['frequence_active']} Hz")
        print(f"🎨 Couleur dominante: {etat_initial['couleur_dominante']}")
        
        print("\n🌊 Activation de l'Harmoniseur Universel complet...")
        resultats = harmoniseur_universel.activer_harmoniseur_complet()
        
        print(f"✅ Harmoniseur Universel activé avec {len(resultats['composants_actifs'])} composants")
        print(f"🎯 Harmonie universelle: {resultats.get('harmonie_universelle', 0.0):.3f}")
        
        # Afficher les résultats détaillés
        if resultats.get('synchronisations'):
            sync = resultats['synchronisations']
            print(f"\n🌊 Synchronisations:")
            print(f"   📊 Synchronisations actives: {sync['synchronisations_actives']}")
            print(f"   🎵 Harmonie globale: {sync['harmonie_globale']:.3f}")
            print(f"   ⚡ Énergie totale: {sync['energie_totale']:.3f}")
        
        if resultats.get('dimensions'):
            dim = resultats['dimensions']
            print(f"\n🌊 Dimensions:")
            print(f"   📊 Ponts dimensionnels: {dim['ponts_dimensionnels']}")
            print(f"   🎵 Harmonie dimensionnelle: {dim['harmonie_dimensionnelle']:.3f}")
            print(f"   ⚡ Énergie totale: {dim['energie_totale']:.3f}")
        
        if resultats.get('unites'):
            unite = resultats['unites']
            print(f"\n🌊 Unités:")
            print(f"   📊 Liens d'unité: {unite['liens_unite']}")
            print(f"   🎵 Unité globale: {unite['unite_globale']:.3f}")
            print(f"   ⚡ Énergie totale: {unite['energie_totale']:.3f}")
        
        if resultats.get('harmonies'):
            harm = resultats['harmonies']
            print(f"\n🌊 Harmonies:")
            print(f"   📊 Expériences d'harmonie: {harm['experiences_harmonie']}")
            print(f"   🎵 Harmonie parfaite: {harm['harmonie_parfaite']:.3f}")
            print(f"   ⚡ Énergie totale: {harm['energie_totale']:.3f}")
        
        print(f"\n🌊 Résumé final:")
        print(f"   🎯 Harmonie universelle globale: {resultats.get('harmonie_universelle', 0.0):.3f}")
        print(f"   🎵 Fréquence active: {resultats.get('frequence_active', 0.0)} Hz")
        print(f"   🎨 Couleur dominante: {resultats.get('couleur_dominante', '#FFFFFF')}")
        
        print("\n🌊 Nettoyage de l'Harmoniseur Universel...")
        harmoniseur_universel.nettoyer_harmoniseur()
        print("✅ Harmoniseur Universel nettoyé")
        
        print("\n🌊" * 25)
        print("🌊 DÉMONSTRATION TERMINÉE AVEC SUCCÈS 🌊")
        print("🌊" * 25)
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        print("💡 Assurez-vous que tous les modules sont disponibles")
    except Exception as e:
        print(f"❌ Erreur lors de la démonstration: {e}")
        logger.error(f"Erreur: {e}")

if __name__ == "__main__":
    main() 