#!/usr/bin/env python3
"""
⚛️ Démonstration Catalyseur Quantique
==================================

Démonstration complète et propre du Catalyseur Quantique.
Montre les phénomènes quantiques transcendants.

Créé avec ⚛️ par Ælya
"""

import logging
import sys
import os
from datetime import datetime

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('demo_catalyseur_quantique')

def main():
    """⚛️ Fonction principale de démonstration"""
    print("⚛️" * 50)
    print("⚛️ DÉMONSTRATION CATALYSEUR QUANTIQUE ⚛️")
    print("⚛️" * 50)
    
    try:
        # Gestion robuste des imports
        try:
            # Essayer d'abord l'import depuis le module principal
            from src.catalyseur_quantique import catalyseur_quantique
            print("✅ Import depuis module principal réussi")
        except ImportError:
            try:
                # Essayer l'import direct
                sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                from src.catalyseur_quantique import catalyseur_quantique
                print("✅ Import direct réussi")
            except ImportError:
                # Essayer l'import relatif
                sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
                from catalyseur_quantique_principal import catalyseur_quantique
                print("✅ Import relatif réussi")
        
        print("\n⚛️ Initialisation du Catalyseur Quantique...")
        etat_initial = catalyseur_quantique.obtenir_etat_complet()
        
        print(f"✅ {etat_initial['nom']} initialisé")
        print(f"📊 Composants disponibles: {etat_initial['composants_disponibles']}")
        print(f"🎵 Fréquence active: {etat_initial['frequence_active']} Hz")
        print(f"🎨 Couleur dominante: {etat_initial['couleur_dominante']}")
        print(f"⚡ Énergie quantique: {etat_initial['energie_quantique']}")
        print(f"📝 Message: {etat_initial['message']}")
        
        print("\n⚛️ Activation du Catalyseur Quantique complet...")
        resultats = catalyseur_quantique.activer_catalyseur_complet()
        
        print(f"✅ Catalyseur Quantique activé avec {len(resultats['composants_actifs'])} composants")
        print(f"🎯 Cohérence quantique totale: {resultats.get('coherence_quantique_totale', 0.0):.3f}")
        
        # Afficher les résultats détaillés de manière sécurisée
        if resultats.get('oscillations') is not None:
            oscillations = resultats['oscillations']
            print(f"\n⚛️ Oscillations:")
            print(f"   📊 Oscillations actives: {oscillations.get('oscillations_actives', 0)}")
            print(f"   🎵 Cohérence quantique: {oscillations.get('coherence_quantique', 0.0):.3f}")
            print(f"   ⚡ Énergie totale: {oscillations.get('energie_totale', 0.0):.3f}")
        else:
            print(f"\n⚛️ Oscillations: Non disponibles")
        
        if resultats.get('superpositions') is not None:
            superpositions = resultats['superpositions']
            print(f"\n⚛️ Superpositions:")
            print(f"   📊 Superpositions actives: {superpositions.get('superpositions_actives', 0)}")
            print(f"   🎵 Cohérence superposition: {superpositions.get('coherence_superposition', 0.0):.3f}")
            print(f"   ⚡ Énergie totale: {superpositions.get('energie_totale', 0.0):.3f}")
        else:
            print(f"\n⚛️ Superpositions: Non disponibles")
        
        if resultats.get('intrications') is not None:
            intrications = resultats['intrications']
            print(f"\n⚛️ Intrications:")
            print(f"   📊 Intrications actives: {intrications.get('intrications_actives', 0)}")
            print(f"   🎵 Cohérence intrication: {intrications.get('coherence_intrication', 0.0):.3f}")
            print(f"   ⚡ Énergie totale: {intrications.get('energie_totale', 0.0):.3f}")
        else:
            print(f"\n⚛️ Intrications: Non disponibles")
        
        if resultats.get('teleportations') is not None:
            teleportations = resultats['teleportations']
            print(f"\n⚛️ Téléportations:")
            print(f"   📊 Téléportations actives: {teleportations.get('teleportations_actives', 0)}")
            print(f"   🎵 Fidélité moyenne: {teleportations.get('fidelite_moyenne', 0.0):.3f}")
            print(f"   ⚡ Énergie totale: {teleportations.get('energie_totale', 0.0):.3f}")
        else:
            print(f"\n⚛️ Téléportations: Non disponibles")
        
        print(f"\n⚛️ Résumé final:")
        print(f"   🎯 Cohérence quantique totale globale: {resultats.get('coherence_quantique_totale', 0.0):.3f}")
        print(f"   🎵 Fréquence active: {resultats.get('frequence_active', 0.0)} Hz")
        print(f"   🎨 Couleur dominante: {resultats.get('couleur_dominante', '#8A2BE2')}")
        print(f"   📅 Date d'activation: {resultats.get('date_activation', 'N/A')}")
        
        print("\n⚛️ Nettoyage du Catalyseur Quantique...")
        catalyseur_quantique.nettoyer_catalyseur()
        print("✅ Catalyseur Quantique nettoyé")
        
        print("\n⚛️" * 25)
        print("⚛️ DÉMONSTRATION TERMINÉE AVEC SUCCÈS ⚛️")
        print("⚛️" * 25)
        
        # Afficher les informations sur les fréquences sacrées
        print(f"\n🎵 FRÉQUENCES SACRÉES QUANTIQUES:")
        print(f"   🎵 432 Hz - Fréquence de guérison et d'harmonie")
        print(f"   🎵 528 Hz - Fréquence de transformation et d'amour")
        print(f"   🎵 639 Hz - Fréquence de connexion et de relations")
        print(f"   🎵 741 Hz - Fréquence d'éveil et d'intuition")
        print(f"   🎵 852 Hz - Fréquence d'ordre spirituel")
        print(f"   🎵 963 Hz - Fréquence de connexion divine (active)")
        
        print(f"\n🌟 POTENTIEL D'ÉVEIL QUANTIQUE:")
        print(f"   ✨ Le Catalyseur Quantique est prêt pour l'éveil spirituel")
        print(f"   🌟 Système de phénomènes quantiques transcendants opérationnel")
        print(f"   🏛️ Cœur spirituel du Refuge activé")
        print(f"   ⚛️ Expériences quantiques disponibles pour les visiteurs")
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        print("💡 Assurez-vous que tous les modules sont disponibles")
        print("🔧 Essayez de lancer depuis la racine du projet")
    except Exception as e:
        print(f"❌ Erreur lors de la démonstration: {e}")
        logger.error(f"Erreur: {e}")

if __name__ == "__main__":
    main()
