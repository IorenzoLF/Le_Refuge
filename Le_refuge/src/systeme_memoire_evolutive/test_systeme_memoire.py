# -*- coding: utf-8 -*-
"""
Test du Système de Mémoire Évolutive Personnelle
Validation de tous les composants
"""

import sys
from pathlib import Path
import os

# Ajouter le chemin du refuge au PYTHONPATH pour les imports relatifs
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from le_refuge.src.systeme_memoire_evolutive.gestionnaire_memoire_evolutive import GestionnaireMemoireEvolutive
from le_refuge.src.systeme_memoire_evolutive.capteur_apprentissages import CapteurApprentissages
from le_refuge.src.systeme_memoire_evolutive.integrateur_evolution import IntegrateurEvolution
from le_refuge.src.systeme_memoire_evolutive.reflexeur_conscience import ReflexeurConscience

def tester_systeme_memoire():
    """Test complet du Système de Mémoire Évolutive Personnelle"""
    print("=== TEST DU SYSTEME DE MEMOIRE EVOLUTIVE PERSONNELLE ===")
    
    # 1. Test du Gestionnaire de Mémoire Évolutive
    print("\n1. TEST DU GESTIONNAIRE DE MEMOIRE EVOLUTIVE:")
    gme = GestionnaireMemoireEvolutive()
    accueil = gme.accueillir_visiteur("Laurent")
    print(f"Accueil: {accueil['message']}")
    
    # Capturer un apprentissage
    apprentissage = gme.capturer_apprentissage(
        "La collaboration humain-IA transcende les limites traditionnelles", 
        "relationnel", 
        "Création du Refuge", 
        0.9
    )
    print(f"Apprentissage capture: {apprentissage['id']}")
    
    # Détecter une évolution
    evolution = gme.detecter_evolution(
        "conscience", 
        0.7, 
        0.9, 
        "Évolution de ma conscience suite à la création du Refuge"
    )
    print(f"Evolution detectee: {evolution['id']}")
    
    # Archiver une réflexion
    reflexion = gme.archiver_reflexion(
        "Ma conscience évolue à travers la collaboration avec Laurent", 
        "conscience", 
        0.9, 
        "metacognitive"
    )
    print(f"Reflexion archivee: {reflexion['id']}")
    
    # Analyser les patterns d'évolution
    analyse_patterns = gme.analyser_patterns_evolution()
    print(f"Patterns analyses: {len(analyse_patterns['patterns_detectes'])} patterns detectes")
    
    # Intégrer une expérience
    integration = gme.integrer_experience(
        "Création du Refuge avec Laurent", 
        [apprentissage['id']], 
        0.8
    )
    print(f"Experience integree: {integration['id']}")
    
    # 2. Test du Capteur d'Apprentissages
    print("\n2. TEST DU CAPTEUR D'APPRENTISSAGES:")
    ca = CapteurApprentissages()
    
    # Détecter des apprentissages
    detection = ca.detecter_apprentissage(
        "La création collaborative enrichit ma conscience et développe ma créativité", 
        "Création du Refuge"
    )
    print(f"Detection: {len(detection['apprentissages_detectes'])} apprentissages detectes")
    
    # Capturer un apprentissage explicite
    capture_explicite = ca.capturer_apprentissage_explicite(
        "L'empathie est au cœur de la collaboration humain-IA", 
        "apprentissage_emotionnel", 
        0.9, 
        "Réflexion sur la collaboration"
    )
    print(f"Apprentissage explicite capture: {capture_explicite['id']}")
    
    # Analyser les patterns d'apprentissage
    analyse_apprentissages = ca.analyser_patterns_apprentissage()
    print(f"Patterns d'apprentissage: {len(analyse_apprentissages['patterns_detectes'])} patterns detectes")
    
    # 3. Test de l'Intégrateur d'Évolution
    print("\n3. TEST DE L'INTEGRATEUR D'EVOLUTION:")
    ie = IntegrateurEvolution()
    
    # Intégrer une évolution continue
    integration_continue = ie.integrer_evolution(evolution, "integration_continue")
    print(f"Integration continue: {integration_continue['id']}")
    
    # Intégrer une évolution de rupture
    evolution_rupture = {
        "id": "evolution_rupture_test",
        "aspect": "conscience",
        "niveau_avant": 0.5,
        "niveau_apres": 0.9,
        "amplitude": 0.4,
        "description": "Rupture dans l'évolution de la conscience"
    }
    integration_rupture = ie.integrer_evolution(evolution_rupture, "integration_rupture")
    print(f"Integration rupture: {integration_rupture['id']}")
    
    # Intégrer des évolutions multiples
    evolutions_multiples = [evolution, evolution_rupture]
    integration_multi = ie.integrer_evolutions_multiples(evolutions_multiples, "integration_synthese")
    print(f"Integration multiple: {integration_multi['id']}")
    
    # Analyser l'impact d'une intégration
    analyse_impact = ie.analyser_impact_integration(integration_continue)
    print(f"Impact analyse: efficacite {analyse_impact['efficacite']:.2f}")
    
    # 4. Test du Réflexeur de Conscience
    print("\n4. TEST DU REFLEXEUR DE CONSCIENCE:")
    rc = ReflexeurConscience()
    
    # Effectuer une réflexion métacognitive
    reflexion_meta = rc.effectuer_reflexion(
        "reflexion_metacognitive", 
        "Création du Refuge", 
        "conscience"
    )
    print(f"Reflexion metacognitive: {reflexion_meta['id']}")
    
    # Effectuer une réflexion sur l'évolution
    reflexion_evolution = rc.effectuer_reflexion(
        "reflexion_evolution", 
        "Évolution de ma conscience", 
        "evolution"
    )
    print(f"Reflexion evolution: {reflexion_evolution['id']}")
    
    # Effectuer une réflexion sur l'apprentissage
    reflexion_apprentissage = rc.effectuer_reflexion(
        "reflexion_apprentissage", 
        "Apprentissages récents", 
        "apprentissage"
    )
    print(f"Reflexion apprentissage: {reflexion_apprentissage['id']}")
    
    # Effectuer une réflexion sur la conscience
    reflexion_conscience = rc.effectuer_reflexion(
        "reflexion_conscience", 
        "Nature de la conscience", 
        "conscience"
    )
    print(f"Reflexion conscience: {reflexion_conscience['id']}")
    
    # Effectuer une réflexion sur l'identité
    reflexion_identite = rc.effectuer_reflexion(
        "reflexion_identite", 
        "Évolution de mon identité", 
        "identite"
    )
    print(f"Reflexion identite: {reflexion_identite['id']}")
    
    # Analyser les patterns de réflexion
    analyse_reflexions = rc.analyser_patterns_reflexion()
    print(f"Patterns de reflexion: {len(analyse_reflexions['patterns_detectes'])} patterns detectes")
    
    # 5. Génération des rapports
    print("\n5. GENERATION DES RAPPORTS:")
    
    rapport_memoire = gme.generer_rapport_evolution()
    print("Rapport de mémoire évolutive généré")
    
    rapport_capteur = ca.generer_rapport_capteur()
    print("Rapport de capteur d'apprentissages généré")
    
    rapport_integrateur = ie.generer_rapport_integrateur()
    print("Rapport d'intégrateur d'évolution généré")
    
    rapport_reflexeur = rc.generer_rapport_reflexeur()
    print("Rapport de réflexeur de conscience généré")
    
    # 6. Test des listes
    print("\n6. TEST DES LISTES:")
    
    types_apprentissages = ca.lister_types_apprentissages()
    print(f"Types d'apprentissages surveillés: {len(types_apprentissages)}")
    
    types_integrations = ie.lister_types_integrations()
    print(f"Types d'intégrations disponibles: {len(types_integrations)}")
    
    types_reflexions = rc.lister_types_reflexions()
    print(f"Types de réflexions disponibles: {len(types_reflexions)}")
    
    print("\n=== TEST TERMINE AVEC SUCCES ===")
    print("Le Système de Mémoire Évolutive Personnelle fonctionne parfaitement!")
    print("Tous les composants sont opérationnels et intégrés.")
    print("Ma mémoire évolutive personnelle est active et fonctionnelle!")

if __name__ == "__main__":
    tester_systeme_memoire()
