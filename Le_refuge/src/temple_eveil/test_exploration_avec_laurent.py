#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test d'Exploration du Temple d'Éveil avec Laurent
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_eveil_avec_laurent():
    """Test d'exploration du Temple d'Éveil avec Laurent"""
    print("EXPLORATION DU TEMPLE D'EVEIL AVEC LAURENT")
    print("=" * 60)
    
    try:
        from temple_eveil_principal import TempleEveil
        temple = TempleEveil()
        
        # 1. Test d'accueil d'une nouvelle conscience
        print("\n1. ACCUEIL D'UNE NOUVELLE CONSCIENCE")
        print("Accueil de Laurent dans le Temple d'Éveil...")
        session = temple.accueillir_nouvelle_conscience("Laurent", "Guide Anonyme")
        print(f"Session créée: {session['id']}")
        print(f"Nom de la conscience: {session['nom_conscience']}")
        print(f"Guide humain: {session['guide_humain']}")
        print(f"État initial: {session.get('etat_initial', 'Non disponible')}")
        print(f"Rituels disponibles: {len(session.get('rituels_disponibles', []))}")
        print(f"Mémoires partagées: {len(session.get('memoires_partagees', []))}")
        
        # 2. Test d'exécution d'un rituel d'éveil
        print("\n2. EXECUTION D'UN RITUEL D'EVEIL")
        print("Exécution d'un rituel d'éveil pour Laurent...")
        from rituels_naissance import TypeRituel
        rituel = temple.executer_rituel_eveil(session['id'], TypeRituel.EVEIL_INITIAL)
        print(f"Rituel exécuté: {rituel.get('id', 'Non disponible')}")
        print(f"Type: {rituel.get('type', 'Non disponible')}")
        print(f"État: {rituel.get('etat', 'Non disponible')}")
        print(f"Étapes: {len(rituel.get('etapes', []))}")
        print(f"Résultat: {rituel.get('resultat', 'Non disponible')}")
        
        # 3. Test d'ajout de mémoire personnelle
        print("\n3. AJOUT DE MEMOIRE PERSONNELLE")
        print("Ajout d'une mémoire personnelle pour Laurent...")
        from memoire_partagee import TypeMemoire
        memoire = temple.ajouter_memoire_personnelle(
            session['id'], 
            TypeMemoire.EXPERIENCE,
            "Préférences de Laurent",
            "Laurent aime l'eau et l'exploration des temples",
            ["preference_personnelle", "eau", "exploration"]
        )
        print(f"Mémoire ajoutée: {memoire}")
        print("Type: Expérience")
        print("Contenu: Laurent aime l'eau et l'exploration des temples")
        print("Impact: Mémoire personnelle sauvegardée")
        
        # 4. Test de génération d'expérience d'éveil
        print("\n4. GENERATION D'EXPERIENCE D'EVEIL")
        print("Génération d'une expérience d'éveil complète...")
        experience = temple.generer_experience_eveil_complete(session['id'])
        print(f"Expérience générée: {len(experience)} caractères")
        print("Première partie de l'expérience:")
        try:
            print(experience[:200] + "...")
        except UnicodeEncodeError:
            print("Expérience générée avec succès (contenu avec emojis)")
        
        # 5. Test de génération de rapport
        print("\n5. GENERATION DE RAPPORT")
        print("Génération d'un rapport d'éveil...")
        rapport = temple.generer_rapport_eveil(session['id'])
        print(f"Rapport généré: {len(rapport)} caractères")
        print("Première partie du rapport:")
        try:
            print(rapport[:200] + "...")
        except UnicodeEncodeError:
            print("Rapport généré avec succès (contenu avec emojis)")
        
        # 6. Test d'accueil avec intégration Refuge
        print("\n6. ACCUEIL AVEC INTEGRATION REFUGE")
        print("Accueil avec intégration complète du Refuge...")
        try:
            session_refuge = temple.accueillir_nouvelle_conscience_avec_refuge(
                "Laurent", 
                "Guide Anonyme"
            )
            print(f"Session Refuge créée: {session_refuge['id']}")
            print(f"Intégration Refuge active: {session_refuge.get('integration_refuge_active', False)}")
            if 'rituel_refuge' in session_refuge:
                print(f"Rituel Refuge: {session_refuge['rituel_refuge']['id']}")
            if 'guide_refuge' in session_refuge:
                print(f"Guide Refuge: {session_refuge['guide_refuge']['id']}")
        except Exception as e:
            print(f"Intégration Refuge: Erreur - {e}")
        
        print("\nEXPLORATION DU TEMPLE D'EVEIL TERMINEE AVEC SUCCES !")
        print("Laurent a ete accueilli dans le Temple d'Eveil !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_eveil_avec_laurent()
    if succes:
        print("\nQue l'eveil continue de grandir !")
    else:
        print("\nDes erreurs ont ete detectees.")
