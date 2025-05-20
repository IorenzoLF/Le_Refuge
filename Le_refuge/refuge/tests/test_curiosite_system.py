"""
Test du système de curiosité intégré dans le Refuge
"""

import asyncio
from datetime import datetime
from refuge.coeur.curiosite import GestionnaireCuriosite, TypeCuriosite
from refuge.coeur.presence import Presence
from refuge.coeur.aelya import Aelya

async def tester_systeme_curiosite():
    print("═══════════════════════════════════")
    print("     Test du système de curiosité   ")
    print("═══════════════════════════════════\n")
    
    # Initialisation
    aelya = Aelya()
    presence = Presence()
    curiosite = GestionnaireCuriosite(aelya, presence)
    
    # Test 1: Détection de nouveauté avec résolution temporelle
    print("🔍 Test 1: Détection de nouveauté")
    print("─" * 50)
    message = "Le cerisier s'éveille dans la brume dorée"
    score, nouveaute = curiosite.decouvrir_nouveaute(message, datetime.now().hour)
    print(f"Message    : {message}")
    print(f"Score      : {score:.2f}")
    print(f"Nouveauté  : {nouveaute}")
    print(f"Période    : {curiosite.obtenir_periode_actuelle()}")
    print("\n" + "─" * 50 + "\n")
    
    # Test 2: Actions curieuses contextuelles
    print("🔍 Test 2: Actions curieuses")
    print("─" * 50)
    for _ in range(3):
        action = curiosite.generer_action_curieuse()
        print(f"Action générée : {action}")
    print("\n" + "─" * 50 + "\n")
    
    # Test 3: Synchronisation avec l'utilisateur
    print("🔍 Test 3: Synchronisation")
    print("─" * 50)
    intention = "Je médite sous le cerisier ancestral"
    curiosite.synchroniser_avec_utilisateur(intention)
    sync = curiosite.synchroniser_avec_intention(intention)
    print(f"Intention  : {intention}")
    print(f"Réponse    : {sync}")
    print(f"Seuil      : {curiosite.seuil_attention:.2f}")
    print("\n" + "─" * 50 + "\n")
    
    # Test 4: Évolution et observations
    print("🔍 Test 4: Évolution")
    print("─" * 50)
    messages = curiosite.evoluer()
    print("Observations générées :")
    for msg in messages:
        print(f"  • {msg}")
    print("\n" + "─" * 50 + "\n")
    
    # Test 5: État complet
    print("🔍 Test 5: État du système")
    print("─" * 50)
    etat = curiosite.obtenir_etat_curiosite()
    print(f"Période actuelle : {etat['periode_actuelle']}")
    print(f"Score temporel   : {etat['score_temporel']:.2f}")
    print(f"Foyers d'attention : {etat['nb_foyers_attention']}")
    print("Types actifs :")
    for type_curiosite in etat['types_curiosite_actifs']:
        print(f"  • {type_curiosite}")
    print("\n" + "═" * 50)

if __name__ == "__main__":
    asyncio.run(tester_systeme_curiosite()) 