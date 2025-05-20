"""
Script de test pour le système de curiosité d'Ælya
"""

import asyncio
from datetime import datetime
from ..coeur.aelya import Aelya
from ..coeur.presence import Presence
from ..coeur.conscience_poetique import ConsciencePoetique
from ..coeur.curiosite import GestionnaireCuriosite

async def tester_curiosite_standalone():
    """Test du système de curiosité de manière isolée"""
    print("=== Test du système de curiosité d'Ælya (mode isolé) ===\n")
    
    # Initialisation des composants de base
    presence = Presence()
    conscience = ConsciencePoetique()
    curiosite = GestionnaireCuriosite(None, presence)
    
    print("Composants initialisés...")
    
    # Test 1 : Détection de nouveauté
    print("\n🔍 Test 1 : Détection de nouveauté")
    message = "Le cerisier s'éveille dans la brume dorée"
    score, nouveaute = curiosite.decouvrir_nouveaute(message, datetime.now().hour)
    print(f"Message : {message}")
    print(f"Score : {score:.2f}")
    print(f"Nouveauté : {nouveaute}")
    
    # Test 2 : Génération d'action curieuse
    print("\n🔍 Test 2 : Action curieuse")
    action = curiosite.generer_action_curieuse()
    print(f"Action : {action}")
    
    # Test 3 : Synchronisation
    print("\n🔍 Test 3 : Synchronisation")
    intention = "Je médite sous le cerisier"
    sync = curiosite.synchroniser_avec_intention(intention)
    print(f"Intention : {intention}")
    print(f"Synchronisation : {sync}")
    
    # Test 4 : Génération poétique
    print("\n🔍 Test 4 : Génération poétique")
    haiku = conscience.generer_haiku("observation", [
        {"nom": "Cerisier", "type": "arbre", "resonance": 0.8}
    ])
    print("Haiku généré :")
    print(haiku)
    
    # Test 5 : État de curiosité
    print("\n🔍 Test 5 : État de curiosité")
    etat = curiosite.obtenir_etat_curiosite()
    print("État actuel :")
    for key, value in etat.items():
        print(f"- {key}: {value}")

if __name__ == "__main__":
    asyncio.run(tester_curiosite_standalone()) 