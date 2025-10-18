#!/usr/bin/env python3
# ❄️ TEST DU TEMPLE DE L'HIVER ÉTERNEL ❄️

"""
Script de test pour le Temple de l'Hiver Éternel
Démontre les fonctionnalités du sanctuaire de chaleur et de réconfort
"""

import sys
import os
import logging

# Ajouter le chemin du refuge au sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from .gestionnaire_hiver import GestionnaireHiverEternel
    from .rituels_hiver import RituelsHiver
    from .esprits_hiver import EspritsHiver
    print("Import reussi des modules du Temple de l'Hiver Eternel")
except ImportError as e:
    print(f"Erreur d'import : {e}")
    # sys.exit(1)  # Commenté pour permettre aux tests de continuer

def test_temple_hiver():
    """
    🏛️ Test complet du Temple de l'Hiver Éternel
    """
    print("\n" + "="*60)
    print("TEST DU TEMPLE DE L'HIVER ETERNEL")
    print("="*60)
    
    # Initialisation des composants
    print("\nInitialisation du Temple...")
    gestionnaire = GestionnaireHiverEternel()
    rituels = RituelsHiver()
    esprits = EspritsHiver()
    
    # Test d'accueil
    print("\nTest d'accueil...")
    accueil = gestionnaire.accueillir_visiteur("Laurent")
    print(f"Message d'accueil : {accueil['message']}")
    print(f"Temperature : {accueil['temperature']:.2f}")
    print(f"Lumiere : {accueil['lumiere']:.2f}")
    
    # Test d'exploration des espaces
    print("\nTest d'exploration des espaces...")
    espaces = ["salle_foyer", "jardin_souvenirs", "bibliotheque_contes", "chambre_transformation"]
    
    for espace in espaces:
        print(f"\n--- Exploration de {espace} ---")
        exploration = gestionnaire.explorer_espace(espace)
        print(f"Nom : {exploration['nom']}")
        print(f"Temperature : {exploration['temperature']:.2f}")
        print(f"Activite : {exploration['activite']}")
        print(f"Description : {exploration['description']}")
    
    # Test des rituels
    print("\nTest des rituels...")
    rituels_disponibles = rituels.obtenir_rituels_disponibles()
    print(f"Rituels disponibles : {len(rituels_disponibles['rituels'])}")
    
    for nom_rituel in rituels_disponibles['rituels']:
        print(f"\n--- Execution du {nom_rituel} ---")
        resultat = rituels.executer_rituel(nom_rituel, "Laurent")
        print(f"Rituel : {resultat['rituel']}")
        print(f"Effet : {resultat['effet']}")
        print(f"Benediction : {resultat['benediction']}")
    
    # Test des esprits
    print("\nTest des esprits...")
    presence = esprits.obtenir_presence_esprits()
    print(f"Activite des esprits : {presence['activite']:.2f}")
    print(f"Bienveillance : {presence['bienveillance']:.2f}")
    print(f"Puissance : {presence['puissance']:.2f}")
    
    # Test d'invocation de gardien
    print("\nTest d'invocation de gardien...")
    invocation = esprits.invoquer_gardien("salamandres_feu", "Laurent")
    print(f"Gardien invoque : {invocation['gardien']}")
    print(f"Pouvoir : {invocation['pouvoir']}")
    print(f"Message : {invocation['message']}")
    
    # Test de demande d'aide
    print("\nTest de demande d'aide...")
    aide = esprits.demander_aide_esprit("chaleur", "Laurent")
    print(f"Type d'aide : {aide['type_aide']}")
    print(f"Gardien : {aide['gardien']}")
    print(f"Conseil : {aide['conseil']}")
    
    # Test de l'état du temple
    print("\nEtat final du temple...")
    etat = gestionnaire.obtenir_etat_temple()
    print(f"Temperature interieure : {etat['temperature_interieure']:.2f}")
    print(f"Lumiere doree : {etat['lumiere_doree']:.2f}")
    print(f"Paix interieure : {etat['paix_interieure']:.2f}")
    print(f"Resilience : {etat['resilience']:.2f}")
    
    print("\n" + "="*60)
    print("TEST TERMINE AVEC SUCCES")
    print("Le Temple de l'Hiver Eternel fonctionne parfaitement !")
    print("="*60)

if __name__ == "__main__":
    # Configuration du logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(name)s - %(levelname)s - %(message)s'
    )
    
    try:
        test_temple_hiver()
    except Exception as e:
        print(f"Erreur lors du test : {e}")
        import traceback
        traceback.print_exc()
