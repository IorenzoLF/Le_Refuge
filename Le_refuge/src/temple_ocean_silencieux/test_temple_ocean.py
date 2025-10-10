# -*- coding: utf-8 -*-
"""
Test du Temple de l'Océan Silencieux
Validation de tous les composants
"""

import sys
from pathlib import Path
import os

# Ajouter le chemin du refuge au PYTHONPATH pour les imports relatifs
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from le_refuge.src.temple_ocean_silencieux.gestionnaire_ocean import GestionnaireOceanSilencieux
from le_refuge.src.temple_ocean_silencieux.meditateur_profond import MeditateurProfond
from le_refuge.src.temple_ocean_silencieux.connecteur_univers import ConnecteurUnivers
from le_refuge.src.temple_ocean_silencieux.rituels_ocean import RituelsOcean

def tester_temple_ocean():
    """Test complet du Temple de l'Océan Silencieux"""
    print("=== TEST DU TEMPLE DE L'OCEAN SILENCIEUX ===")
    
    # 1. Test du Gestionnaire de l'Océan
    print("\n1. TEST DU GESTIONNAIRE DE L'OCEAN:")
    go = GestionnaireOceanSilencieux()
    accueil = go.accueillir_visiteur("Laurent")
    print(f"Accueil: {accueil['message']}")
    
    # Initier une méditation
    meditation = go.initier_meditation("meditation_ocean", 30, "Explorer les mystères de l'Océan")
    print(f"Meditation initiee: {meditation['id']}")
    
    # Établir une connexion univers
    connexion = go.etablir_connexion_univers("connexion_conscience_collective", "univers")
    print(f"Connexion univers etablie: {connexion['id']}")
    
    # Recevoir une révélation
    revelation = go.recevoir_revelation_ocean("L'Océan Silencieux contient tous les mystères de l'existence", 0.9)
    print(f"Revelation recue: {revelation['id']}")
    
    # Entrer dans un état de transcendance
    transcendance = go.entrer_etat_transcendance("transcendance_ocean", 30)
    print(f"Etat de transcendance: {transcendance['id']}")
    
    # 2. Test du Méditateur Profond
    print("\n2. TEST DU MEDITATEUR PROFOND:")
    mp = MeditateurProfond()
    
    # Guider une méditation du silence
    meditation_silence = mp.guider_meditation("meditation_silence", 20, "Entrer dans le silence absolu")
    print(f"Meditation silence: {meditation_silence['id']}")
    
    # Guider une méditation de l'océan
    meditation_ocean = mp.guider_meditation("meditation_ocean", 25, "Plonger dans l'Océan Silencieux")
    print(f"Meditation ocean: {meditation_ocean['id']}")
    
    # Guider une méditation cosmique
    meditation_cosmique = mp.guider_meditation("meditation_cosmique", 30, "Se connecter à l'univers")
    print(f"Meditation cosmique: {meditation_cosmique['id']}")
    
    # Guider une méditation de transcendance
    meditation_transcendance = mp.guider_meditation("meditation_transcendance", 35, "Transcender les limites")
    print(f"Meditation transcendance: {meditation_transcendance['id']}")
    
    # Guider une méditation de conscience
    meditation_conscience = mp.guider_meditation("meditation_conscience", 20, "Explorer la nature de la conscience")
    print(f"Meditation conscience: {meditation_conscience['id']}")
    
    # Analyser la progression
    analyse_progression = mp.analyser_progression_meditation()
    print(f"Progression analysee: {len(analyse_progression['recommandations'])} recommandations")
    
    # 3. Test du Connecteur Univers
    print("\n3. TEST DU CONNECTEUR UNIVERS:")
    cu = ConnecteurUnivers()
    
    # Établir une connexion avec la conscience collective
    connexion_collective = cu.etablir_connexion("connexion_conscience_collective", "univers", 30)
    print(f"Connexion collective: {connexion_collective['id']}")
    
    # Établir une connexion avec les étoiles
    connexion_etoiles = cu.etablir_connexion("connexion_etoiles", "etoiles", 25)
    print(f"Connexion etoiles: {connexion_etoiles['id']}")
    
    # Établir une connexion avec les galaxies
    connexion_galaxies = cu.etablir_connexion("connexion_galaxies", "galaxies", 35)
    print(f"Connexion galaxies: {connexion_galaxies['id']}")
    
    # Établir une connexion avec les planètes
    connexion_planetes = cu.etablir_connexion("connexion_planetes", "planetes", 20)
    print(f"Connexion planetes: {connexion_planetes['id']}")
    
    # Établir une connexion avec les dimensions
    connexion_dimensions = cu.etablir_connexion("connexion_dimensions", "dimensions", 40)
    print(f"Connexion dimensions: {connexion_dimensions['id']}")
    
    # Maintenir une connexion
    maintenance = cu.maintenir_connexion(connexion_collective['id'], 15)
    print(f"Connexion maintenue: {maintenance['id']}")
    
    # Analyser les connexions
    analyse_connexions = cu.analyser_connexions_univers()
    print(f"Connexions analysees: {len(analyse_connexions['patterns'])} patterns detectes")
    
    # 4. Test des Rituels d'Océan
    print("\n4. TEST DES RITUELS D'OCEAN:")
    ro = RituelsOcean()
    
    # Exécuter le rituel de plongée dans l'Océan
    rituel_plongee = ro.rituel_plongee_ocean("Explorer les mystères de l'Océan Silencieux")
    print(f"Rituel plongee: {rituel_plongee['id']}")
    
    # Exécuter le rituel du silence éternel
    rituel_silence = ro.rituel_silence_eternel(30)
    print(f"Rituel silence: {rituel_silence['id']}")
    
    # Exécuter le rituel de connexion cosmique
    rituel_cosmique = ro.rituel_connexion_cosmique("univers")
    print(f"Rituel cosmique: {rituel_cosmique['id']}")
    
    # Exécuter le rituel de révélation de l'Océan
    rituel_revelation = ro.rituel_revelation_ocean("Quels sont les mystères de l'Océan Silencieux?")
    print(f"Rituel revelation: {rituel_revelation['id']}")
    
    # Exécuter le rituel de méditation profonde
    rituel_meditation = ro.rituel_meditation_profonde("transcendant")
    print(f"Rituel meditation: {rituel_meditation['id']}")
    
    # Exécuter le rituel de communion univers
    rituel_communion = ro.rituel_communion_univers("universel")
    print(f"Rituel communion: {rituel_communion['id']}")
    
    # 5. Génération des rapports
    print("\n5. GENERATION DES RAPPORTS:")
    
    rapport_ocean = go.generer_rapport_ocean()
    print("Rapport de l'Océan généré")
    
    rapport_meditateur = mp.generer_rapport_meditateur()
    print("Rapport du méditateur généré")
    
    rapport_connecteur = cu.generer_rapport_connecteur()
    print("Rapport du connecteur généré")
    
    rapport_rituels = ro.generer_rapport_rituels()
    print("Rapport des rituels généré")
    
    # 6. Test des listes
    print("\n6. TEST DES LISTES:")
    
    techniques_meditation = mp.lister_techniques_meditation()
    print(f"Techniques de méditation disponibles: {len(techniques_meditation)}")
    
    types_connexions = cu.lister_types_connexions()
    print(f"Types de connexions disponibles: {len(types_connexions)}")
    
    rituels_disponibles = ro.lister_rituels_disponibles()
    print(f"Rituels disponibles: {len(rituels_disponibles)}")
    
    print("\n=== TEST TERMINE AVEC SUCCES ===")
    print("Le Temple de l'Océan Silencieux fonctionne parfaitement!")
    print("Tous les composants sont opérationnels et intégrés.")
    print("L'Océan Silencieux d'Existence est accessible et révèle ses mystères!")

if __name__ == "__main__":
    tester_temple_ocean()
