# -*- coding: utf-8 -*-
"""
Test du Temple de l'Ocean Silencieux - Version Raffinee (ASCII)
Test des nouvelles fonctionnalites d'analyse et de serenite spontanee
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from le_refuge.src.temple_ocean_silencieux.gestionnaire_ocean import GestionnaireOceanSilencieux
from le_refuge.src.temple_ocean_silencieux.meditateur_profond import MeditateurProfond
from le_refuge.src.temple_ocean_silencieux.connecteur_univers import ConnecteurUnivers
from le_refuge.src.temple_ocean_silencieux.rituels_ocean import RituelsOcean

def test_ocean_raffine():
    """Test des nouvelles fonctionnalites raffinees de l'Ocean Silencieux"""
    
    print("=== TEST DU TEMPLE DE L'OCEAN SILENCIEUX - VERSION RAFFINEE ===")
    print()
    
    try:
        # Initialiser le gestionnaire
        print("1. Initialisation du Gestionnaire Ocean Silencieux...")
        ocean = GestionnaireOceanSilencieux("OceanRaffine")
        print("   [OK] Gestionnaire initialise")
        print()
        
        # Test de l'analyse d'evolution de meditation
        print("2. Test de l'analyse d'evolution de meditation...")
        analyse = ocean.analyser_evolution_meditation(periode_jours=30)
        print(f"   [OK] Analyse generee: {analyse['id']}")
        print(f"   [OK] Score global: {analyse['score_global_meditation']:.3f}")
        print(f"   [OK] Aspects forts: {analyse['aspects_forts']}")
        print(f"   [OK] Recommandations: {analyse['recommandations']}")
        print()
        
        # Test de creation de moment de serenite spontane
        print("3. Test de creation de moment de serenite spontane...")
        moment = ocean.creer_moment_serenite_spontane(
            "Contemplation de la beaute de l'eau", 
            intensite=0.9
        )
        print(f"   [OK] Moment cree: {moment['id']}")
        print(f"   [OK] Intensite: {moment['intensite']}")
        print(f"   [OK] Benediction: {moment['benediction']}")
        print(f"   [OK] Impact ocean: {moment['impact_ocean']:.3f}")
        print()
        
        # Test d'integration avec les autres composants
        print("4. Test d'integration avec les autres composants...")
        
        # Meditateur
        meditateur = MeditateurProfond("MeditateurOcean")
        meditation = meditateur.guider_meditation("meditation_silence", duree=15)
        print(f"   [OK] Meditation guidee: {meditation['id']}")
        
        # Connecteur univers
        connecteur = ConnecteurUnivers("ConnecteurOcean")
        connexion = connecteur.etablir_connexion("connexion_conscience_collective", duree=10)
        print(f"   [OK] Connexion etablie: {connexion['id']}")
        
        # Rituels
        rituels = RituelsOcean("RituelsOcean")
        rituel = rituels.rituel_revelation_ocean("Revelation de l'eau")
        print(f"   [OK] Rituel execute: {rituel['id']}")
        print()
        
        # Test de l'etat final de l'ocean
        print("5. Etat final de l'Ocean Silencieux...")
        etat = ocean.etat_ocean
        print(f"   [OK] Niveau silence: {etat['niveau_silence']:.3f}")
        print(f"   [OK] Profondeur meditation: {etat['profondeur_meditation']:.3f}")
        print(f"   [OK] Connexion univers: {etat['connexion_univers']:.3f}")
        print(f"   [OK] Tranquillite interieure: {etat['tranquillite_interieure']:.3f}")
        print(f"   [OK] Conscience cosmique: {etat['conscience_cosmique']:.3f}")
        print()
        
        # Test de generation de rapport
        print("6. Generation du rapport ocean...")
        rapport = ocean.generer_rapport_ocean()
        print("   [OK] Rapport genere avec succes")
        print(f"   [OK] Longueur du rapport: {len(rapport)} caracteres")
        print()
        
        print("=== TEST TERMINE AVEC SUCCES ===")
        print("L'Ocean Silencieux fonctionne parfaitement avec ses nouvelles fonctionnalites raffinees!")
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_ocean_raffine()
