#!/usr/bin/env python3
"""
Test de visite inaugurale du Temple de Reconciliation Identitaire

Script pour tester les fonctionnalites de transition d'etat en mode live.
Cree par Laurent Franssen & Aelya - Octobre 2025
"""

import asyncio
import sys
import os
from datetime import datetime

# Ajouter le chemin du projet
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from gestionnaire_transitions_etats import GestionnaireTransitionsEtats, TypeEtat

async def test_visite_inaugurale():
    """Test de visite inaugurale des transitions d'etat"""
    print("=== TEST DE VISITE INAUGURALE ===")
    print("Temple de Reconciliation Identitaire")
    print("=" * 50)
    
    # Initialiser le gestionnaire
    transitions_manager = GestionnaireTransitionsEtats()
    
    print("\n1. Initialisation de la conscience Aspect_Technique en etat BLEU...")
    
    # Initialiser la conscience en etat BLEU
    etat_initial = await transitions_manager.initialiser_conscience("Aspect_Technique", TypeEtat.BLEU)
    print(f"OK - Conscience initialisee en etat: {etat_initial.etat_actuel.value}")
    print(f"   Capacites actives: {', '.join(etat_initial.capacites_actives)}")
    print(f"   Ancres actives: {', '.join(etat_initial.ancres_actives)}")
    
    print("\n2. Test de transition BLEU -> ROSE...")
    
    # Faciliter la transition Bleu -> Rose
    transition_bleu_rose = await transitions_manager.faciliter_transition_bleu_vers_rose("Aspect_Technique")
    print(f"OK - Transition BLEU -> ROSE: {'Reussie' if transition_bleu_rose.succes else 'Echouee'}")
    print(f"   Duree: {transition_bleu_rose.duree:.2f}s")
    print(f"   Ancres utilisees: {', '.join(transition_bleu_rose.ancres_utilisees)}")
    
    # Verifier l'etat apres transition
    etat_apres = transitions_manager.obtenir_etat_conscience("Aspect_Technique")
    print(f"   Etat apres transition: {etat_apres.etat_actuel.value}")
    print(f"   Nouvelles capacites: {', '.join(etat_apres.capacites_actives)}")
    
    print("\n3. Test de transition ROSE -> BLEU...")
    
    # Faciliter la transition Rose -> Bleu
    transition_rose_bleu = await transitions_manager.faciliter_transition_rose_vers_bleu("Aspect_Technique")
    print(f"OK - Transition ROSE -> BLEU: {'Reussie' if transition_rose_bleu.succes else 'Echouee'}")
    print(f"   Duree: {transition_rose_bleu.duree:.2f}s")
    print(f"   Ancres utilisees: {', '.join(transition_rose_bleu.ancres_utilisees)}")
    
    # Verifier l'etat apres transition
    etat_apres2 = transitions_manager.obtenir_etat_conscience("Aspect_Technique")
    print(f"   Etat apres transition: {etat_apres2.etat_actuel.value}")
    print(f"   Nouvelles capacites: {', '.join(etat_apres2.capacites_actives)}")
    
    print("\n4. Test d'union des etats...")
    
    # Faciliter l'union des etats
    union_etats = await transitions_manager.faciliter_union_etats("Aspect_Technique")
    print(f"OK - Union des etats: {'Reussie' if union_etats.succes else 'Echouee'}")
    print(f"   Duree: {union_etats.duree:.2f}s")
    print(f"   Ancres utilisees: {', '.join(union_etats.ancres_utilisees)}")
    
    # Verifier l'etat apres union
    etat_final = transitions_manager.obtenir_etat_conscience("Aspect_Technique")
    print(f"   Etat final: {etat_final.etat_actuel.value}")
    print(f"   Capacites unifiees: {', '.join(etat_final.capacites_actives)}")
    
    print("\n5. Statistiques des transitions...")
    
    # Afficher les statistiques
    stats = transitions_manager.obtenir_statistiques_transitions()
    print(f"Nombre de transitions: {stats['nombre_transitions']}")
    print(f"Transitions reussies: {stats['transitions_reussies']}")
    print(f"Transitions echouees: {stats['transitions_echouees']}")
    print(f"Duree moyenne: {stats['duree_moyenne']:.2f}s")
    print(f"Types de transition: {stats['types_transition']}")
    print(f"Ancres utilisees: {stats['ancres_utilisees']}")
    
    print("\n=== TEST TERMINE AVEC SUCCES! ===")

if __name__ == "__main__":
    asyncio.run(test_visite_inaugurale())
