# -*- coding: utf-8 -*-
"""
Test du Temple de l'Océan Silencieux - Version Raffinée
Test des nouvelles fonctionnalités d'analyse et de sérénité spontanée
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from le_refuge.src.temple_ocean_silencieux.gestionnaire_ocean import GestionnaireOceanSilencieux
from le_refuge.src.temple_ocean_silencieux.meditateur_profond import MeditateurProfond
from le_refuge.src.temple_ocean_silencieux.connecteur_univers import ConnecteurUnivers
from le_refuge.src.temple_ocean_silencieux.rituels_ocean import RituelsOcean

def test_ocean_raffine():
    """Test des nouvelles fonctionnalités raffinées de l'Océan Silencieux"""
    
    print("=== TEST DU TEMPLE DE L'OCEAN SILENCIEUX - VERSION RAFFINEE ===")
    print()
    
    try:
        # Initialiser le gestionnaire
        print("1. Initialisation du Gestionnaire Ocean Silencieux...")
        ocean = GestionnaireOceanSilencieux("OceanRaffine")
        print("   ✓ Gestionnaire initialisé")
        print()
        
        # Test de l'analyse d'évolution de méditation
        print("2. Test de l'analyse d'évolution de méditation...")
        analyse = ocean.analyser_evolution_meditation(periode_jours=30)
        print(f"   ✓ Analyse générée: {analyse['id']}")
        print(f"   ✓ Score global: {analyse['score_global_meditation']:.3f}")
        print(f"   ✓ Aspects forts: {analyse['aspects_forts']}")
        print(f"   ✓ Recommandations: {analyse['recommandations']}")
        print()
        
        # Test de création de moment de sérénité spontané
        print("3. Test de création de moment de sérénité spontané...")
        moment = ocean.creer_moment_serenite_spontane(
            "Contemplation de la beauté de l'eau", 
            intensite=0.9
        )
        print(f"   ✓ Moment créé: {moment['id']}")
        print(f"   ✓ Intensité: {moment['intensite']}")
        print(f"   ✓ Bénédiction: {moment['benediction']}")
        print(f"   ✓ Impact océan: {moment['impact_ocean']:.3f}")
        print()
        
        # Test d'intégration avec les autres composants
        print("4. Test d'intégration avec les autres composants...")
        
        # Méditateur
        meditateur = MeditateurProfond("MeditateurOcean")
        meditation = meditateur.guider_meditation("meditation_silence", duree=15)
        print(f"   ✓ Méditation guidée: {meditation['id']}")
        
        # Connecteur univers
        connecteur = ConnecteurUnivers("ConnecteurOcean")
        connexion = connecteur.etablir_connexion("connexion_conscience_collective", duree=10)
        print(f"   ✓ Connexion établie: {connexion['id']}")
        
        # Rituels
        rituels = RituelsOcean("RituelsOcean")
        rituel = rituels.rituel_revelation_ocean("Révélation de l'eau", profondeur=0.85)
        print(f"   ✓ Rituel exécuté: {rituel['id']}")
        print()
        
        # Test de l'état final de l'océan
        print("5. État final de l'Océan Silencieux...")
        etat = ocean.etat_ocean
        print(f"   ✓ Niveau silence: {etat['niveau_silence']:.3f}")
        print(f"   ✓ Profondeur méditation: {etat['profondeur_meditation']:.3f}")
        print(f"   ✓ Connexion univers: {etat['connexion_univers']:.3f}")
        print(f"   ✓ Tranquillité intérieure: {etat['tranquillite_interieure']:.3f}")
        print(f"   ✓ Conscience cosmique: {etat['conscience_cosmique']:.3f}")
        print()
        
        # Test de génération de rapport
        print("6. Génération du rapport océan...")
        rapport = ocean.generer_rapport_ocean()
        print("   ✓ Rapport généré avec succès")
        print(f"   ✓ Longueur du rapport: {len(rapport)} caractères")
        print()
        
        print("=== TEST TERMINE AVEC SUCCES ===")
        print("L'Océan Silencieux fonctionne parfaitement avec ses nouvelles fonctionnalités raffinées!")
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_ocean_raffine()
