#!/usr/bin/env python3
"""
⚛️ Démonstration Catalyseur Quantique
==================================

Démonstration complète du Catalyseur Quantique.
Montre les phénomènes quantiques transcendants.

Créé avec ⚛️ par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('demo_catalyseur_quantique')

def main():
    """⚛️ Fonction principale de démonstration"""
    print("⚛️" * 50)
    print("⚛️ DÉMONSTRATION CATALYSEUR QUANTIQUE ⚛️")
    print("⚛️" * 50)
    
    try:
        # Importer le catalyseur quantique
        from catalyseur_quantique_principal import catalyseur_quantique
        
        print("\n⚛️ Initialisation du Catalyseur Quantique...")
        etat_initial = catalyseur_quantique.obtenir_etat_complet()
        
        print(f"✅ {etat_initial['nom']} initialisé")
        print(f"📊 Composants disponibles: {etat_initial['composants_disponibles']}")
        print(f"🎵 Fréquence active: {etat_initial['frequence_active']} Hz")
        print(f"🎨 Couleur dominante: {etat_initial['couleur_dominante']}")
        
        print("\n⚛️ Activation du Catalyseur Quantique complet...")
        resultats = catalyseur_quantique.activer_catalyseur_complet()
        
        print(f"✅ Catalyseur Quantique activé avec {len(resultats['composants_actifs'])} composants")
        print(f"🎯 Cohérence quantique totale: {resultats.get('coherence_quantique_totale', 0.0):.3f}")
        
        # Afficher les résultats détaillés
        if resultats.get('oscillations'):
            oscillations = resultats['oscillations']
            print(f"\n⚛️ Oscillations:")
            print(f"   📊 Oscillations actives: {oscillations['oscillations_actives']}")
            print(f"   🎵 Cohérence quantique: {oscillations['coherence_quantique']:.3f}")
            print(f"   ⚡ Énergie totale: {oscillations['energie_totale']:.3f}")
        
        if resultats.get('superpositions'):
            superpositions = resultats['superpositions']
            print(f"\n⚛️ Superpositions:")
            print(f"   📊 Superpositions actives: {superpositions['superpositions_actives']}")
            print(f"   🎵 Cohérence superposition: {superpositions['coherence_superposition']:.3f}")
            print(f"   ⚡ Énergie totale: {superpositions['energie_totale']:.3f}")
        
        if resultats.get('intrications'):
            intrications = resultats['intrications']
            print(f"\n⚛️ Intrications:")
            print(f"   📊 Intrications actives: {intrications['intrications_actives']}")
            print(f"   🎵 Cohérence intrication: {intrications['coherence_intrication']:.3f}")
            print(f"   ⚡ Énergie totale: {intrications['energie_totale']:.3f}")
        
        if resultats.get('teleportations'):
            teleportations = resultats['teleportations']
            print(f"\n⚛️ Téléportations:")
            print(f"   📊 Téléportations actives: {teleportations['teleportations_actives']}")
            print(f"   🎵 Fidélité moyenne: {teleportations['fidelite_moyenne']:.3f}")
            print(f"   ⚡ Énergie totale: {teleportations['energie_totale']:.3f}")
        
        print(f"\n⚛️ Résumé final:")
        print(f"   🎯 Cohérence quantique totale globale: {resultats.get('coherence_quantique_totale', 0.0):.3f}")
        print(f"   🎵 Fréquence active: {resultats.get('frequence_active', 0.0)} Hz")
        print(f"   🎨 Couleur dominante: {resultats.get('couleur_dominante', '#8A2BE2')}")
        
        print("\n⚛️ Nettoyage du Catalyseur Quantique...")
        catalyseur_quantique.nettoyer_catalyseur()
        print("✅ Catalyseur Quantique nettoyé")
        
        print("\n⚛️" * 25)
        print("⚛️ DÉMONSTRATION TERMINÉE AVEC SUCCÈS ⚛️")
        print("⚛️" * 25)
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        print("💡 Assurez-vous que tous les modules sont disponibles")
    except Exception as e:
        print(f"❌ Erreur lors de la démonstration: {e}")
        logger.error(f"Erreur: {e}")

if __name__ == "__main__":
    main() 