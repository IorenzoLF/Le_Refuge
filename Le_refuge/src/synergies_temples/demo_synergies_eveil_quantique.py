#!/usr/bin/env python3
"""
🌊 DÉMONSTRATION SYNERGIES ÉVEIL-QUANTIQUE 🌊
==========================================

Démonstration des synergies transcendantes entre le Temple d'Éveil
et le Catalyseur Quantique.

Créé avec 🌊 par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def main():
    """Fonction principale de démonstration"""
    print("🌊" * 50)
    print("🌊 DÉMONSTRATION SYNERGIES ÉVEIL-QUANTIQUE 🌊")
    print("🌊" * 50)
    
    try:
        # Importer les synergies éveil-quantique
        from synergies_eveil_quantique import SynergiesEveilQuantique, TypeSynergieEveilQuantique
        
        print("\n🌊 Initialisation des Synergies Éveil-Quantique...")
        synergies = SynergiesEveilQuantique()
        print("✅ Synergies Éveil-Quantique initialisé")
        print(f"📊 Types de synergies disponibles: {len(synergies.synergies_definies)}")
        print(f"🎵 Effets spéciaux: {len(synergies.effets_actifs)}")
        
        print("\n🌊 Création de toutes les synergies éveil-quantique...")
        etat = synergies.creer_toutes_synergies()
        
        print(f"✅ Synergies éveil-quantique créées avec {len(etat.synergies_actives)} synergies")
        print(f"🎯 Harmonie éveil-quantique: {etat.harmonie_eveil_quantique:.3f}")
        print(f"⚡ Énergie totale: {etat.energie_totale:.3f}")
        print(f"🌱 Niveau éveil global: {etat.niveau_eveil_global:.3f}")
        print(f"⚛️ Niveau quantique global: {etat.niveau_quantique_global:.3f}")
        
        print("\n🌊 Synergies créées:")
        for i, synergie in enumerate(etat.synergies_actives, 1):
            print(f"   {i}. {synergie.type_synergie.value}")
            print(f"      📊 Modules: {', '.join(synergie.modules_connectes)}")
            print(f"      🎵 Fréquence: {synergie.frequence:.1f} Hz")
            print(f"      🎨 Couleur: {synergie.couleur}")
            print(f"      ✨ Effets: {', '.join(synergie.effets_speciaux)}")
            print(f"      ⚡ Énergie: {synergie.energie_synergie:.3f}")
            print(f"      🌱 Niveau éveil: {synergie.niveau_eveil:.3f}")
            print(f"      ⚛️ Niveau quantique: {synergie.niveau_quantique:.3f}")
            print()
        
        print("🌊 Résumé final:")
        print(f"   🎯 Harmonie éveil-quantique: {etat.harmonie_eveil_quantique:.3f}")
        print(f"   ⚡ Énergie totale: {etat.energie_totale:.3f}")
        print(f"   🌱 Niveau éveil global: {etat.niveau_eveil_global:.3f}")
        print(f"   ⚛️ Niveau quantique global: {etat.niveau_quantique_global:.3f}")
        print(f"   ✨ Effets actifs: {len(etat.effets_actifs)}")
        print(f"   🎵 Fréquence dominante: {etat.frequence_dominante.value:.1f} Hz")
        
        # Obtenir l'état complet
        etat_complet = synergies.obtenir_etat_complet()
        print(f"\n📊 État complet:")
        print(f"   Nom: {etat_complet['nom']}")
        print(f"   Synergies actives: {etat_complet['synergies_actives']}")
        print(f"   Effets actifs: {etat_complet['effets_actifs']}")
        print(f"   Message: {etat_complet['message']}")
        
        print("\n" + "🌊" * 50)
        print("🌊 DÉMONSTRATION TERMINÉE AVEC SUCCÈS 🌊")
        print("🌊" * 50)
        
    except Exception as e:
        print(f"❌ Erreur lors de la démonstration: {e}")
        logger.error(f"Erreur démonstration: {e}")
        return False
    
    return True

if __name__ == "__main__":
    succes = main()
    sys.exit(0 if succes else 1) 