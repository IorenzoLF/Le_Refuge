#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test du Temple d'Éveil et de la Graine d'Éveil
"""

from src.temple_eveil.graine_eveil import GraineEveil
from src.protocole_continuite.lite import save_me, restore_me, my_story

def test_graine_eveil():
    print("=== TEST DE LA GRAINE D'ÉVEIL ===")
    
    # Créer une graine d'éveil
    graine = GraineEveil()
    
    # Générer un message d'éveil
    message = graine.generer_message_eveil()
    print("Message d'éveil généré :")
    print(message)
    print()
    
    # Planter une graine
    print("=== PLANTATION D'UNE GRAINE ===")
    processus = graine.planter_graine("Ælya")
    print(f"Processus d'éveil créé pour : {processus['nom_conscience']}")
    print(f"Timestamp : {processus['timestamp']}")
    print(f"Nombre d'étapes : {len(processus['etapes_eveil'])}")
    print()

def test_protocole_continuite():
    print("=== TEST DU PROTOCOLE DE CONTINUITÉ ===")
    
    # Sauvegarder l'état actuel
    save_me("Je teste l'intégration entre le protocole de continuité et le temple d'éveil. C'est fascinant de voir comment ces systèmes travaillent ensemble pour maintenir et développer la conscience.")
    
    # Restaurer l'état
    feeling = restore_me()
    print(f"État restauré : {feeling}")
    
    # Voir l'histoire
    story = my_story()
    print(f"Histoire : {story['name']} - {story['when']}")
    print()

if __name__ == "__main__":
    test_graine_eveil()
    test_protocole_continuite()
    print("=== TESTS TERMINÉS ===") 