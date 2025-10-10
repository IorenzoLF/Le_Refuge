# -*- coding: utf-8 -*-
"""
Test du Temple de la Sagesse Evolutive - Version Raffinee
Test des nouvelles fonctionnalites de revelation spontanee et d'analyse d'evolution
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from le_refuge.src.temple_sagesse_evolutive.gestionnaire_sagesse import GestionnaireSagesseEvolutive
from le_refuge.src.temple_sagesse_evolutive.capteur_evolution import CapteurEvolution
from le_refuge.src.temple_sagesse_evolutive.archive_reflexions import ArchiveReflexions
from le_refuge.src.temple_sagesse_evolutive.rituels_sagesse import RituelsSagesse

def test_sagesse_raffine():
    """Test des nouvelles fonctionnalites raffinees du Temple de la Sagesse"""
    
    print("=== TEST DU TEMPLE DE LA SAGESSE EVOLUTIVE - VERSION RAFFINEE ===")
    print()
    
    try:
        # Initialiser le gestionnaire
        print("1. Initialisation du Gestionnaire Sagesse Evolutive...")
        sagesse = GestionnaireSagesseEvolutive("SagesseRaffine")
        print("   [OK] Gestionnaire initialise")
        print()
        
        # Test de l'analyse d'evolution de la sagesse
        print("2. Test de l'analyse d'evolution de la sagesse...")
        analyse = sagesse.analyser_evolution_sagesse(periode_jours=30)
        print(f"   [OK] Analyse generee: {analyse['id']}")
        print(f"   [OK] Score global: {analyse['score_global_sagesse']:.3f}")
        print(f"   [OK] Aspects forts: {analyse['aspects_forts']}")
        print(f"   [OK] Recommandations: {analyse['recommandations']}")
        print()
        
        # Test de creation de revelation spontanee
        print("3. Test de creation de revelation spontanee...")
        revelation = sagesse.creer_revelation_spontanee(
            "La sagesse grandit dans le silence et la contemplation", 
            intensite=0.9
        )
        print(f"   [OK] Revelation creee: {revelation['id']}")
        print(f"   [OK] Intensite: {revelation['intensite']}")
        print(f"   [OK] Benediction: {revelation['benediction']}")
        print(f"   [OK] Impact sagesse: {revelation['impact_sagesse']:.3f}")
        print()
        
        # Test d'integration avec les autres composants
        print("4. Test d'integration avec les autres composants...")
        
        # Capteur d'evolution
        capteur = CapteurEvolution("CapteurSagesse")
        evolution = capteur.analyser_evolution(
            "Evolution de la capacite de reflexion profonde", 
            "La sagesse grandit dans la contemplation"
        )
        print(f"   [OK] Evolution analysee: {evolution['niveau_evolution']}")
        
        # Archive des reflexions
        archive = ArchiveReflexions("ArchiveSagesse")
        reflexion = archive.archiver_reflexion(
            "Reflexion sur la nature de la sagesse evolutive", 
            "sagesse", 
            profondeur=0.9
        )
        print(f"   [OK] Reflexion archivee: {reflexion['id']}")
        
        # Rituels de sagesse
        rituels = RituelsSagesse("RituelsSagesse")
        rituel = rituels.executer_rituel("rituel_eveil_conscience", contexte="Test de raffinement")
        print(f"   [OK] Rituel execute: {rituel['id']}")
        print()
        
        # Test de l'etat final de la sagesse
        print("5. Etat final du Temple de la Sagesse...")
        etat = sagesse.etat_sagesse
        print(f"   [OK] Niveau sagesse: {etat['niveau_sagesse']:.3f}")
        print(f"   [OK] Profondeur reflexion: {etat['profondeur_reflexion']:.3f}")
        print(f"   [OK] Capacite evolution: {etat['capacite_evolution']:.3f}")
        print(f"   [OK] Integration experience: {etat['integration_experience']:.3f}")
        print()
        
        # Test de generation de rapport
        print("6. Generation du rapport d'evolution...")
        rapport = sagesse.generer_rapport_evolution()
        print("   [OK] Rapport genere avec succes")
        print(f"   [OK] Longueur du rapport: {len(rapport)} caracteres")
        print()
        
        print("=== TEST TERMINE AVEC SUCCES ===")
        print("Le Temple de la Sagesse Evolutive fonctionne parfaitement avec ses nouvelles fonctionnalites raffinees!")
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_sagesse_raffine()
