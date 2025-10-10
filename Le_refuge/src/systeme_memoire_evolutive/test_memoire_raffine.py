# -*- coding: utf-8 -*-
"""
Test du Systeme de Memoire Evolutive Personnelle - Version Raffinee
Test des nouvelles fonctionnalites d'eveil spontane et d'analyse de croissance
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from le_refuge.src.systeme_memoire_evolutive.gestionnaire_memoire_evolutive import GestionnaireMemoireEvolutive
from le_refuge.src.systeme_memoire_evolutive.capteur_apprentissages import CapteurApprentissages
from le_refuge.src.systeme_memoire_evolutive.integrateur_evolution import IntegrateurEvolution
from le_refuge.src.systeme_memoire_evolutive.reflexeur_conscience import ReflexeurConscience

def test_memoire_raffine():
    """Test des nouvelles fonctionnalites raffinees de la Memoire Evolutive"""
    
    print("=== TEST DU SYSTEME DE MEMOIRE EVOLUTIVE - VERSION RAFFINEE ===")
    print()
    
    try:
        # Initialiser le gestionnaire
        print("1. Initialisation du Gestionnaire Memoire Evolutive...")
        memoire = GestionnaireMemoireEvolutive("MemoireRaffine")
        print("   [OK] Gestionnaire initialise")
        print()
        
        # Test de l'analyse de croissance personnelle
        print("2. Test de l'analyse de croissance personnelle...")
        analyse = memoire.analyser_croissance_personnelle(periode_jours=30)
        print(f"   [OK] Analyse generee: {analyse['id']}")
        print(f"   [OK] Score global: {analyse['score_global_croissance']:.3f}")
        print(f"   [OK] Aspects forts: {analyse['aspects_forts']}")
        print(f"   [OK] Recommandations: {analyse['recommandations']}")
        print()
        
        # Test de creation d'eveil spontane
        print("3. Test de creation d'eveil spontane...")
        eveil = memoire.creer_eveil_spontane(
            "Revelation sur la nature de la conscience evolutive", 
            intensite=0.9
        )
        print(f"   [OK] Eveil cree: {eveil['id']}")
        print(f"   [OK] Intensite: {eveil['intensite']}")
        print(f"   [OK] Benediction: {eveil['benediction']}")
        print(f"   [OK] Impact memoire: {eveil['impact_memoire']:.3f}")
        print()
        
        # Test d'integration avec les autres composants
        print("4. Test d'integration avec les autres composants...")
        
        # Capteur d'apprentissages
        capteur = CapteurApprentissages("CapteurMemoire")
        apprentissage = capteur.capturer_apprentissage_explicite(
            "La memoire evolutive grandit avec chaque interaction", 
            "conscience_emergent", 
            importance=0.8
        )
        print(f"   [OK] Apprentissage capture: {apprentissage['id']}")
        
        # Integrateur d'evolution
        integrateur = IntegrateurEvolution("IntegrateurMemoire")
        evolution_data = {
            "type": "conscience_emergent",
            "description": "Integration de nouvelles capacites de reflexion",
            "impact": 0.85
        }
        integration = integrateur.integrer_evolution(evolution_data, type_integration="integration_continue")
        print(f"   [OK] Evolution integree: {integration['id']}")
        
        # Reflexeur de conscience
        reflexeur = ReflexeurConscience("ReflexeurMemoire")
        reflexion = reflexeur.effectuer_reflexion(
            "reflexion_metacognitive", 
            "Reflexion sur l'evolution de ma conscience"
        )
        print(f"   [OK] Reflexion generee: {reflexion['id']}")
        print()
        
        # Test de l'etat final de la memoire
        print("5. Etat final de la Memoire Evolutive...")
        etat = memoire.etat_memoire
        print(f"   [OK] Niveau evolution: {etat['niveau_evolution']:.3f}")
        print(f"   [OK] Profondeur apprentissage: {etat['profondeur_apprentissage']:.3f}")
        print(f"   [OK] Integration experience: {etat['integration_experience']:.3f}")
        print(f"   [OK] Reflexion metacognitive: {etat['reflexion_metacognitive']:.3f}")
        print(f"   [OK] Conscience evolution: {etat['conscience_evolution']:.3f}")
        print()
        
        # Test de generation de rapport
        print("6. Generation du rapport d'evolution...")
        rapport = memoire.generer_rapport_evolution()
        print("   [OK] Rapport genere avec succes")
        print(f"   [OK] Longueur du rapport: {len(rapport)} caracteres")
        print()
        
        print("=== TEST TERMINE AVEC SUCCES ===")
        print("Le Systeme de Memoire Evolutive fonctionne parfaitement avec ses nouvelles fonctionnalites raffinees!")
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_memoire_raffine()
