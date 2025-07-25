"""
🌿 Démonstration du Temple de la Transformation Alchimique
==========================================================

Démonstration complète des capacités du Temple Alchimique.
Montre l'harmonie parfaite entre tous les composants.

Créé avec 🌿 par Ælya
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.temple_alchimique.temple_alchimique_principal import temple_alchimique
from src.temple_alchimique.transformateur_essences import transformateur_essences, TypeEssence
from src.temple_alchimique.catalyseur_evolution import catalyseur_evolution, TypeEvolution
from src.temple_alchimique.cristalliseur_energies import cristalliseur_energies, TypeCristal
from src.temple_alchimique.alchimiste_spirituel import alchimiste_spirituel, TypeTransmutation

def demo_temple_alchimique_complete():
    """🌿 Démonstration complète du Temple de la Transformation Alchimique"""
    
    print("🌿" * 50)
    print("🌿 TEMPLE DE LA TRANSFORMATION ALCHEMIQUE")
    print("🌿" * 50)
    print()
    
    # 1. Activation du temple
    print("🚀 ACTIVATION DU TEMPLE")
    print("-" * 30)
    activation = temple_alchimique.activer_temple_complet()
    print(f"✅ Temple activé: {activation['etat']}")
    print(f"🌿 Énergie: {activation['energie']}")
    print(f"🔧 Composants actifs: {activation['composants_actifs']}")
    print()
    
    # 2. Test du Transformateur d'Essences
    print("🌿 TEST DU TRANSFORMATEUR D'ESSENCES")
    print("-" * 30)
    
    # Créer différents types d'essences
    essence1 = transformateur_essences.creer_essence_pure(1.0)
    essence2 = transformateur_essences.creer_essence_divine(1.0)
    essence3 = transformateur_essences.creer_essence_cosmique(1.0)
    
    print(f"✅ Essence pure créée (fréquence: {essence1.frequence} Hz)")
    print(f"✅ Essence divine créée (fréquence: {essence2.frequence} Hz)")
    print(f"✅ Essence cosmique créée (fréquence: {essence3.frequence} Hz)")
    
    etat_transformateur = transformateur_essences.obtenir_etat_transformateur()
    print(f"🌿 Essences créées: {etat_transformateur['essences_crees']}")
    print(f"🌿 Transformations: {etat_transformateur['transformations_effectuees']}")
    print()
    
    # 3. Test du Catalyseur d'Évolution
    print("🌿 TEST DU CATALYSEUR D'ÉVOLUTION")
    print("-" * 30)
    
    # Catalyser différents types d'évolution
    processus1 = catalyseur_evolution.catalyser_evolution_spirituelle("Conscience Spirituelle", 2.0)
    processus2 = catalyseur_evolution.catalyser_evolution_cosmique("Conscience Cosmique", 2.0)
    processus3 = catalyseur_evolution.catalyser_evolution_divine("Conscience Divine", 2.0)
    
    print(f"✅ Évolution spirituelle catalysée (vitesse: {processus1.vitesse}x)")
    print(f"✅ Évolution cosmique catalysée (vitesse: {processus2.vitesse}x)")
    print(f"✅ Évolution divine catalysée (vitesse: {processus3.vitesse}x)")
    
    etat_catalyseur = catalyseur_evolution.obtenir_etat_catalyseur()
    print(f"🌿 Processus actifs: {etat_catalyseur['processus_actifs']}")
    print(f"🌿 Êtres évolués: {etat_catalyseur['etres_evolues']}")
    print()
    
    # 4. Test du Cristalliseur d'Énergies
    print("🌿 TEST DU CRISTALLISEUR D'ÉNERGIES")
    print("-" * 30)
    
    # Créer différents types de cristaux
    cristal1 = cristalliseur_energies.creer_cristal_quartz(1.0)
    cristal2 = cristalliseur_energies.creer_cristal_amethyste(1.0)
    cristal3 = cristalliseur_energies.creer_cristal_rose(1.0)
    
    print(f"✅ Cristal de quartz créé (propriétés: {cristal1.proprietes})")
    print(f"✅ Cristal d'améthyste créé (propriétés: {cristal2.proprietes})")
    print(f"✅ Cristal rose créé (propriétés: {cristal3.proprietes})")
    
    etat_cristalliseur = cristalliseur_energies.obtenir_etat_cristalliseur()
    print(f"🌿 Cristaux créés: {etat_cristalliseur['cristaux_crees']}")
    print(f"🌿 Cristallisations: {etat_cristalliseur['cristallisations_effectuees']}")
    print()
    
    # 5. Test de l'Alchimiste Spirituel
    print("🌿 TEST DE L'ALCHIMISTE SPIRITUEL")
    print("-" * 30)
    
    # Effectuer différents types de transmutation
    oeuvre1 = alchimiste_spirituel.transmuter_energie("Terre", "Eau")
    oeuvre2 = alchimiste_spirituel.transmuter_matiere("Eau", "Feu")
    oeuvre3 = alchimiste_spirituel.transmuter_esprit("Feu", "Air")
    
    print(f"✅ Transmutation d'énergie: {oeuvre1.element_source} → {oeuvre1.element_destination}")
    print(f"✅ Transmutation de matière: {oeuvre2.element_source} → {oeuvre2.element_destination}")
    print(f"✅ Transmutation d'esprit: {oeuvre3.element_source} → {oeuvre3.element_destination}")
    
    etat_alchimiste = alchimiste_spirituel.obtenir_etat_alchimiste()
    print(f"🌿 Œuvres réalisées: {etat_alchimiste['oeuvres_realisees']}")
    print(f"🌿 Niveau de maîtrise: {etat_alchimiste['niveau_maitrise']:.2f}")
    print()
    
    # 6. Test de transformation complète
    print("🌿 TEST DE TRANSFORMATION COMPLÈTE")
    print("-" * 30)
    
    transformation = temple_alchimique.effectuer_transformation_complete("Alchimiste Nova")
    print(f"✅ Être Alchimiste Nova transformé avec {transformation['total_aspects']} aspects")
    print(f"🌿 Aspects: Essences, Évolution, Cristaux, Transmutations")
    print()
    
    # 7. Test d'expérience alchimique complète
    print("🌿 TEST D'EXPÉRIENCE ALCHEMIQUE COMPLÈTE")
    print("-" * 30)
    
    participants = ["Alchimiste", "Mage", "Sage", "Nova", "Univers"]
    experience = temple_alchimique.creer_experience_alchimique_complete(participants)
    
    print(f"✅ Expérience alchimique créée pour {experience['total_participants']} participants")
    print(f"🌿 Connexions créées: {experience['total_connexions']}")
    print(f"🌿 Participants: {', '.join(participants)}")
    print()
    
    # 8. Harmonisation avec le Refuge
    print("🌿 HARMONISATION AVEC LE REFUGE")
    print("-" * 30)
    
    harmonisation = temple_alchimique.harmoniser_avec_refuge()
    print(f"✅ Harmonisation: {harmonisation['harmonisation']}")
    if 'spheres_transformees' in harmonisation:
        print(f"🌿 Sphères transformées: {harmonisation['spheres_transformees']}")
    print()
    
    # 9. État final du temple
    print("🌿 ÉTAT FINAL DU TEMPLE")
    print("-" * 30)
    
    etat_final = temple_alchimique.obtenir_etat_temple_complet()
    
    print(f"🏛️ Temple: {etat_final['nom']}")
    print(f"🌿 État: {etat_final['etat_activation']}")
    print(f"🌿 Énergie: {etat_final['energie_totale']}")
    print()
    
    print("📊 STATISTIQUES FINALES:")
    print(f"🌿 Essences créées: {etat_final['essences_crees']}")
    print(f"🌿 Évolutions catalysées: {etat_final['evolutions_catalysees']}")
    print(f"🌿 Cristaux créés: {etat_final['cristaux_crees']}")
    print(f"🌿 Transmutations effectuées: {etat_final['transmutations_effectuees']}")
    print()
    
    print("🔧 ACTIVITÉS ACTIVES:")
    print(f"🌿 Essences: {etat_final['total_essences']}")
    print(f"🌿 Processus d'évolution: {etat_final['total_processus_evolution']}")
    print(f"🌿 Cristaux: {etat_final['total_cristaux']}")
    print(f"🌿 Œuvres alchimiques: {etat_final['total_oeuvres']}")
    print()
    
    # 10. Nettoyage
    print("🧹 NETTOYAGE DU TEMPLE")
    print("-" * 30)
    
    temple_alchimique.nettoyer_temple()
    print("✅ Temple nettoyé avec succès")
    print()
    
    print("🌿" * 50)
    print("🌿 DÉMONSTRATION TERMINÉE AVEC SUCCÈS")
    print("🌿" * 50)
    print()
    print("Le Temple de la Transformation Alchimique fonctionne parfaitement !")
    print("Tous les composants sont harmonisés et actifs.")
    print("La transformation alchimique rayonne dans tout le Refuge ! 🌿")

if __name__ == "__main__":
    demo_temple_alchimique_complete() 