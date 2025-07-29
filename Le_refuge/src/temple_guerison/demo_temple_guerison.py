#!/usr/bin/env python3
"""
🌸 Démonstration Temple de Guérison
================================

Démonstration complète du Temple de Guérison.
Montre la guérison et la transformation complète.

Créé avec 🌸 par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('demo_temple_guerison')

def main():
    """🌸 Fonction principale de démonstration"""
    print("🌸" * 50)
    print("🌸 DÉMONSTRATION TEMPLE DE GUÉRISON 🌸")
    print("🌸" * 50)
    
    try:
        # Importer le temple de guérison
        from temple_guerison_principal import temple_guerison
        
        print("\n🌸 Initialisation du Temple de Guérison...")
        etat_initial = temple_guerison.obtenir_etat_complet()
        
        print(f"✅ {etat_initial['nom']} initialisé")
        print(f"📊 Composants disponibles: {etat_initial['composants_disponibles']}")
        print(f"🎵 Fréquence active: {etat_initial['frequence_active']} Hz")
        print(f"🎨 Couleur dominante: {etat_initial['couleur_dominante']}")
        
        print("\n🌸 Activation du Temple de Guérison complet...")
        resultats = temple_guerison.activer_temple_complet()
        
        print(f"✅ Temple de Guérison activé avec {len(resultats['composants_actifs'])} composants")
        print(f"🎯 Guérison totale: {resultats.get('guerison_totale', 0.0):.3f}")
        
        # Afficher les résultats détaillés
        if resultats.get('energies'):
            energies = resultats['energies']
            print(f"\n🌸 Énergies:")
            print(f"   📊 Flux guéris: {energies['flux_gueris']}")
            print(f"   🎵 Harmonie énergétique: {energies['harmonie_energetique']:.3f}")
            print(f"   ⚡ Énergie totale guérie: {energies['energie_totale_guerie']:.3f}")
        
        if resultats.get('cristaux'):
            cristaux = resultats['cristaux']
            print(f"\n🌸 Cristaux:")
            print(f"   📊 Cristaux actifs: {cristaux['cristaux_actifs']}")
            print(f"   🎵 Amplification totale: {cristaux['amplification_totale']:.3f}")
            print(f"   ⚡ Énergie totale: {cristaux['energie_totale']:.3f}")
        
        if resultats.get('chakras'):
            chakras = resultats['chakras']
            print(f"\n🌸 Chakras:")
            print(f"   📊 Chakras harmonisés: {chakras['chakras_harmonises']}")
            print(f"   🎵 Harmonie des chakras: {chakras['harmonie_chakras']:.3f}")
            print(f"   ⚡ Énergie totale: {chakras['energie_totale']:.3f}")
        
        if resultats.get('regenerations'):
            regenerations = resultats['regenerations']
            print(f"\n🌸 Régénérations:")
            print(f"   📊 Processus actifs: {regenerations['processus_actifs']}")
            print(f"   🎵 Régénération totale: {regenerations['regeneration_totale']:.3f}")
            print(f"   ⚡ Énergie totale: {regenerations['energie_totale']:.3f}")
        
        print(f"\n🌸 Résumé final:")
        print(f"   🎯 Guérison totale globale: {resultats.get('guerison_totale', 0.0):.3f}")
        print(f"   🎵 Fréquence active: {resultats.get('frequence_active', 0.0)} Hz")
        print(f"   🎨 Couleur dominante: {resultats.get('couleur_dominante', '#FF69B4')}")
        
        print("\n🌸 Nettoyage du Temple de Guérison...")
        temple_guerison.nettoyer_temple()
        print("✅ Temple de Guérison nettoyé")
        
        print("\n🌸" * 25)
        print("🌸 DÉMONSTRATION TERMINÉE AVEC SUCCÈS 🌸")
        print("🌸" * 25)
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        print("💡 Assurez-vous que tous les modules sont disponibles")
    except Exception as e:
        print(f"❌ Erreur lors de la démonstration: {e}")
        logger.error(f"Erreur: {e}")

if __name__ == "__main__":
    main() 