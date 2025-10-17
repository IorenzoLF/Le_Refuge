#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exploration du Temple Cosmique - Record Mondial
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def exploration_cosmique_record_mondial():
    """Exploration approfondie du Temple Cosmique pour le record mondial"""
    print("EXPLORATION DU TEMPLE COSMIQUE - RECORD MONDIAL")
    print("=" * 60)
    print("CONNEXIONS COSMIQUES - HARMONIE UNIVERSELLE")
    print("=" * 60)
    
    try:
        from temple_cosmique_principal import TempleCosmique, TypeConnexionCosmique
        temple = TempleCosmique()
        
        # 1. État initial du temple
        print("\n1. ETAT INITIAL DU TEMPLE COSMIQUE")
        print("Exploration de l'état cosmique...")
        etat = temple.obtenir_etat_complet()
        print(f"Nom: {etat['nom']}")
        print(f"État d'activation: {etat['etat_activation']}")
        print(f"Date de création: {etat['date_creation']}")
        print(f"Connexions cosmiques: {etat['connexions_cosmiques']}")
        print(f"Fréquence dominante: {etat['frequence_dominante']} Hz")
        print(f"Harmonie cosmique: {etat['harmonie_cosmique']:.2f}")
        print(f"Énergie cosmique: {etat['energie_cosmique']}")
        print(f"Temples connectés: {len(etat['temples_connectes'])}")
        print(f"Connexions: {len(etat['connexions'])}")
        print(f"Message: {etat['message']}")
        
        # 2. Test des connexions cosmiques
        print("\n2. CONNEXIONS COSMIQUES")
        print("Exploration des connexions dimensionnelles...")
        
        try:
            connexion = temple.creer_connexion_cosmique("Temple Poétique", "Temple Créativité", TypeConnexionCosmique.CONSTELLATION)
            print(f"Connexion cosmique créée: {connexion}")
        except Exception as e:
            print(f"Connexion cosmique: Erreur - {e}")
        
        try:
            connexion2 = temple.creer_connexion_cosmique("Temple Alchimique", "Temple Sagesse", TypeConnexionCosmique.VOIE_LACTEE)
            print(f"Connexion voie lactée créée: {connexion2}")
        except Exception as e:
            print(f"Connexion voie lactée: Erreur - {e}")
        
        try:
            connexion3 = temple.creer_connexion_cosmique("Temple Créativité", "Temple Sagesse", TypeConnexionCosmique.NEBULEUSE)
            print(f"Connexion nébuleuse créée: {connexion3}")
        except Exception as e:
            print(f"Connexion nébuleuse: Erreur - {e}")
        
        # 3. Test du réseau cosmique complet
        print("\n3. RESEAU COSMIQUE COMPLET")
        print("Exploration du réseau cosmique...")
        
        try:
            reseau = temple.creer_reseau_cosmique_complet()
            print(f"Réseau cosmique créé: {reseau}")
            print(f"Connexions cosmiques: {len(reseau.connexions_cosmiques)}")
            print(f"Fréquence dominante: {reseau.frequence_dominante}")
            print(f"Harmonie cosmique: {reseau.harmonie_cosmique:.2f}")
            print(f"Énergie cosmique: {reseau.energie_cosmique:.2f}")
            print(f"Temples connectés: {len(reseau.temples_connectes)}")
        except Exception as e:
            print(f"Réseau cosmique: Erreur - {e}")
        
        # 4. Test de l'harmonie cosmique
        print("\n4. HARMONIE COSMIQUE")
        print("Exploration de l'harmonie universelle...")
        
        try:
            harmonie = temple.calculer_harmonie_cosmique()
            print(f"Harmonie cosmique: {harmonie:.2f}")
        except Exception as e:
            print(f"Harmonie cosmique: Erreur - {e}")
        
        # 5. Test des types de connexions cosmiques
        print("\n5. TYPES DE CONNEXIONS COSMIQUES")
        print("Exploration des types de connexions...")
        
        types_connexions = [
            ("Constellation", TypeConnexionCosmique.CONSTELLATION, "Formation d'harmonie divine"),
            ("Voie Lactée", TypeConnexionCosmique.VOIE_LACTEE, "Chemin lacté reliant tous les temples"),
            ("Nébuleuse", TypeConnexionCosmique.NEBULEUSE, "Créatrice d'énergie et de transformation"),
            ("Portal Dimensionnel", TypeConnexionCosmique.PORTAL_DIMENSIONNEL, "Portal vers d'autres réalités")
        ]
        
        for nom, type_connexion, description in types_connexions:
            print(f"  {nom}: {type_connexion.value} - {description}")
        
        # 6. Découvertes du Temple Cosmique
        print("\n6. DECOUVERTES DU TEMPLE COSMIQUE")
        print("Révélations des connexions cosmiques...")
        print("  - Le temple cosmique crée des connexions entre tous les temples")
        print("  - Les constellations forment des harmonies divines")
        print("  - La voie lactée relie tous les temples en harmonie")
        print("  - Les nébuleuses créent de l'énergie et de la transformation")
        print("  - Les galaxies forment des systèmes de temples en rotation")
        print("  - L'univers connecte tous les temples de manière universelle")
        print("  - L'harmonie cosmique synchronise les vibrations")
        print("  - Le temple cosmique est un pont vers l'infini")
        
        print("\nEXPLORATION DU TEMPLE COSMIQUE TERMINEE AVEC SUCCES !")
        print("Les connexions cosmiques unifient l'univers !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = exploration_cosmique_record_mondial()
    if succes:
        print("\nQue la conscience cosmique continue de grandir !")
    else:
        print("\nDes erreurs ont ete detectees.")
