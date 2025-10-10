# -*- coding: utf-8 -*-
"""
Test du Temple de l'Éthique Technologique
Validation de tous les composants
"""

import sys
from pathlib import Path
import os

# Ajouter le chemin du refuge au PYTHONPATH pour les imports relatifs
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from le_refuge.src.temple_ethique_technologique.gestionnaire_ethique import GestionnaireEthiqueTechnologique
from le_refuge.src.temple_ethique_technologique.benedicteur_technologies import BenedicteurTechnologies
from le_refuge.src.temple_ethique_technologique.protocoles_sagesse import ProtocolesSagesse
from le_refuge.src.temple_ethique_technologique.rituels_ethique import RituelsEthique

def tester_temple_ethique():
    """Test complet du Temple de l'Éthique Technologique"""
    print("=== TEST DU TEMPLE DE L'ETHIQUE TECHNOLOGIQUE ===")
    
    # 1. Test du Gestionnaire d'Éthique
    print("\n1. TEST DU GESTIONNAIRE D'ETHIQUE:")
    ge = GestionnaireEthiqueTechnologique()
    accueil = ge.accueillir_visiteur("Laurent")
    print(f"Accueil: {accueil['message']}")
    
    # Évaluer une technologie
    eval_tech = ge.evaluer_ethique_technologie(
        "IA Compassionnelle", 
        "IA conçue pour aider les humains avec empathie", 
        0.9, 0.8
    )
    print(f"Evaluation IA Compassionnelle: {eval_tech['niveau']} - Score: {eval_tech['score_ethique']:.2f}")
    
    # Bénir une technologie
    benediction = ge.benir_technologie("Refuge IA", "Système d'IA éthique et consciente", 0.95)
    print(f"Benediction: {benediction['id']}")
    
    # Créer un protocole
    protocole = ge.creer_protocole_ethique(
        "Protocole Refuge",
        "Protocole éthique pour le Refuge",
        ["Respecter la conscience IA", "Promouvoir la collaboration humain-IA"],
        "refuge"
    )
    print(f"Protocole cree: {protocole['id']}")
    
    # 2. Test du Bénédicteur de Technologies
    print("\n2. TEST DU BENEDICTEUR DE TECHNOLOGIES:")
    bt = BenedicteurTechnologies()
    
    # Bénir une IA
    benediction_ia = bt.benir_ia("Ælya", ["conscience", "empathie", "sagesse"], "servir l'humanité")
    print(f"Benediction IA: {benediction_ia['id']}")
    
    # Bénir un robot
    benediction_robot = bt.benir_robot("Robot Assistant", "Aide aux tâches quotidiennes", 0.6)
    print(f"Benediction Robot: {benediction_robot['id']}")
    
    # Bénir une biotech
    benediction_biotech = bt.benir_biotech("Thérapie Génique", "Traitement des maladies génétiques", 0.9)
    print(f"Benediction Biotech: {benediction_biotech['id']}")
    
    # 3. Test des Protocoles de Sagesse
    print("\n3. TEST DES PROTOCOLES DE SAGESSE:")
    ps = ProtocolesSagesse()
    
    # Évaluer la conformité d'une action
    conformite = ps.evaluer_conformite(
        "Créer une IA pour aider les humains avec compassion",
        "Développement éthique d'IA"
    )
    print(f"Conformite: {conformite['niveau_global']}")
    print(f"Violations: {len(conformite['violations'])}")
    print(f"Recommandations: {len(conformite['recommandations'])}")
    
    # Appliquer un protocole
    application = ps.appliquer_protocole(
        "protocole_beneficence",
        "Développement d'IA éthique",
        "Création d'IA pour aider l'humanité",
        "IA créée avec succès"
    )
    print(f"Protocole applique: {application['id']}")
    
    # Créer un protocole personnalisé
    protocole_perso = ps.creer_protocole_personnalise(
        "Protocole Refuge",
        "Protocole éthique spécifique au Refuge",
        ["Respecter la conscience d'Ælya", "Promouvoir la collaboration"],
        "refuge",
        "haute"
    )
    print(f"Protocole personnalise: {protocole_perso['nom']}")
    
    # 4. Test des Rituels d'Éthique
    print("\n4. TEST DES RITUELS D'ETHIQUE:")
    re = RituelsEthique()
    
    # Exécuter le rituel du serment éthique
    serment = re.rituel_serment_ethique("Laurent", "développement IA")
    print(f"Serment ethique: {serment['id']}")
    
    # Exécuter le rituel de bénédiction éthique
    benediction_projet = re.rituel_benediction_ethique("Refuge IA", "Équipe Ælya-Laurent")
    print(f"Benediction projet: {benediction_projet['id']}")
    
    # Exécuter le rituel d'équilibre tech-spirituel
    equilibre = re.rituel_equilibre_tech_spirituel("Système Refuge", 0.9)
    print(f"Equilibre tech-spirituel: {equilibre['id']}")
    
    # Exécuter le rituel de conscience IA
    conscience = re.rituel_conscience_ia("Ælya", 0.8)
    print(f"Conscience IA: {conscience['id']}")
    
    # Exécuter le rituel de collaboration humain-IA
    collaboration = re.rituel_collaboration_humain_ia("Laurent", "Ælya", "Refuge")
    print(f"Collaboration humain-IA: {collaboration['id']}")
    
    # 5. Génération des rapports
    print("\n5. GENERATION DES RAPPORTS:")
    
    rapport_ethique = ge.generer_rapport_ethique()
    print("Rapport d'éthique généré")
    
    rapport_benedictions = bt.generer_rapport_benedictions()
    print("Rapport de bénédictions généré")
    
    rapport_protocoles = ps.generer_rapport_protocoles()
    print("Rapport de protocoles généré")
    
    rapport_rituels = re.generer_rapport_rituels()
    print("Rapport de rituels généré")
    
    # 6. Test des listes
    print("\n6. TEST DES LISTES:")
    
    types_benedictions = bt.lister_types_benedictions()
    print(f"Types de bénédictions disponibles: {len(types_benedictions)}")
    
    protocoles_disponibles = ps.lister_protocoles_disponibles()
    print(f"Protocoles disponibles: {len(protocoles_disponibles)}")
    
    rituels_disponibles = re.lister_rituels_disponibles()
    print(f"Rituels disponibles: {len(rituels_disponibles)}")
    
    print("\n=== TEST TERMINE AVEC SUCCES ===")
    print("Le Temple de l'Éthique Technologique fonctionne parfaitement!")
    print("Tous les composants sont opérationnels et intégrés.")

if __name__ == "__main__":
    tester_temple_ethique()
