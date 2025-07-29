#!/usr/bin/env python3
"""
🌊 Démonstration Synergies Avancées
==============================

Démonstration complète des synergies avancées du Refuge.
Montre les connexions transcendantes entre tous les modules.

Créé avec 🌊 par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('demo_synergies_avancees')

def main():
    """🌊 Fonction principale de démonstration"""
    print("🌊" * 50)
    print("🌊 DÉMONSTRATION SYNERGIES AVANCÉES 🌊")
    print("🌊" * 50)
    
    try:
        # Importer les synergies avancées
        from synergies_avancees import synergies_avancees
        
        print("\n🌊 Initialisation des Synergies Avancées...")
        etat_initial = synergies_avancees.obtenir_etat_complet()
        
        print(f"✅ {etat_initial['nom']} initialisé")
        print(f"📊 Modules disponibles: {len(etat_initial.get('modules_disponibles', []))}")
        print(f"🎵 Effets spéciaux: {len(etat_initial.get('effets_speciaux', []))}")
        
        print("\n🌊 Création de toutes les synergies avancées...")
        resultats = synergies_avancees.creer_toutes_synergies()
        
        print(f"✅ Synergies avancées créées avec {len(synergies_avancees.synergies_actives)} synergies")
        print(f"🎯 Harmonie globale: {resultats.harmonie_globale:.3f}")
        print(f"⚡ Énergie totale: {resultats.energie_totale:.3f}")
        
        # Afficher les synergies créées
        print(f"\n🌊 Synergies créées:")
        for i, synergie in enumerate(synergies_avancees.synergies_actives, 1):
            print(f"   {i}. {synergie.type_synergie.value}")
            print(f"      📊 Modules: {', '.join(synergie.modules_connectes)}")
            print(f"      🎵 Fréquence: {synergie.frequence} Hz")
            print(f"      🎨 Couleur: {synergie.couleur}")
            print(f"      ✨ Effets: {', '.join(synergie.effets_speciaux)}")
            print(f"      ⚡ Énergie: {synergie.energie_synergie:.3f}")
            print()
        
        print(f"🌊 Résumé final:")
        print(f"   🎯 Harmonie globale: {resultats.harmonie_globale:.3f}")
        print(f"   ⚡ Énergie totale: {resultats.energie_totale:.3f}")
        print(f"   ✨ Effets actifs: {len(resultats.effets_actifs)}")
        print(f"   🎵 Fréquence dominante: {resultats.frequence_dominante.value} Hz")
        
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