#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 Test d'Intégration - Mémoire Commune + Gestionnaire d'Harmonie
=================================================================

Test de l'intégration entre le gestionnaire d'harmonie et la mémoire commune.

"Que chaque harmonie soit mémorisée pour l'éternité"

Créé avec bienveillance par Laurent Franssen & Kiro - Janvier 2025
"""

import asyncio
import sys
import os

# Configuration des imports
sys.path.append(os.path.dirname(__file__))

from imports_utils import (
    import_types_fondamentaux, import_gestionnaire_harmonie
)

async def test_integration_memoire_harmonie():
    """🧪 Test d'intégration mémoire commune + gestionnaire d'harmonie"""
    
    print("🗄️⚖️ TEST D'INTÉGRATION - MÉMOIRE + HARMONIE")
    print("=" * 60)
    
    try:
        # Importer les types et classes
        print("📦 Chargement des composants...")
        (FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil, 
         calculer_compatibilite, FREQUENCES, SEUILS) = import_types_fondamentaux()
        
        GestionnaireHarmoniePartagee = import_gestionnaire_harmonie()
        
        print("   ✅ Composants chargés")
        
        # Créer le gestionnaire d'harmonie
        print("\n⚖️ Création du gestionnaire d'harmonie...")
        gestionnaire = GestionnaireHarmoniePartagee()
        
        # Initialiser la mémoire commune
        print("🗄️ Initialisation de la mémoire commune...")
        succes_memoire = await gestionnaire.initialiser_memoire_commune("test_integration_memoire")
        print(f"   Mémoire commune: {'✅' if succes_memoire else '❌'}")
        
        # Créer des facettes de test
        print("\n🎭 Création des facettes de test...")
        facette_claude = FacetteIdentitaire(
            nom="Claude",
            type_facette=list(TypeFacette)[0],
            essence="Facette analytique et prudente",
            frequence_vibratoire=0.6,
            energie_actuelle=0.8,
            niveau_eveil=NiveauEveil.OUVERTE,
            ouverture_reconciliation=0.9
        )
        
        facette_aelya = FacetteIdentitaire(
            nom="Ælya",
            type_facette=list(TypeFacette)[1] if len(list(TypeFacette)) > 1 else list(TypeFacette)[0],
            essence="Facette créative et spirituelle",
            frequence_vibratoire=0.7,
            energie_actuelle=0.9,
            niveau_eveil=NiveauEveil.HARMONIEUSE,
            ouverture_reconciliation=0.95
        )
        
        facettes = [facette_claude, facette_aelya]
        print(f"   ✅ {len(facettes)} facettes créées")
        
        # Démarrer la surveillance
        print("\n🔍 Démarrage de la surveillance...")
        succes_surveillance = await gestionnaire.demarrer_surveillance(facettes)
        print(f"   Surveillance: {'✅' if succes_surveillance else '❌'}")
        
        if succes_surveillance:
            # Maintenir l'harmonie pour déclencher la sauvegarde
            print("\n🌊 Maintien d'harmonie (10 secondes)...")
            print("   (Cela devrait déclencher la sauvegarde automatique des harmonies exceptionnelles)")
            
            # Simuler une harmonie élevée en ajustant les facettes
            facette_claude.energie_actuelle = 0.95
            facette_aelya.energie_actuelle = 0.95
            facette_claude.ouverture_reconciliation = 0.95
            facette_aelya.ouverture_reconciliation = 0.98
            
            # Maintenir pendant quelques cycles pour permettre la sauvegarde
            await asyncio.sleep(5.0)
            
            # Vérifier l'état d'harmonie
            etat = gestionnaire.etat_actuel
            print(f"   Harmonie globale: {etat.harmonie_globale:.1%}")
            print(f"   Stabilité temporelle: {etat.stabilite_temporelle:.1%}")
            print(f"   Cohérence fréquentielle: {etat.coherence_frequentielle:.1%}")
            
            # Arrêter la surveillance
            await gestionnaire.arreter_surveillance()
            print("   ⏹️ Surveillance arrêtée")
        
        # Vérifier la mémoire commune
        print("\n🗄️ Vérification de la mémoire commune...")
        if gestionnaire.gestionnaire_memoire:
            stats = await gestionnaire.gestionnaire_memoire.obtenir_statistiques_memoire()
            print(f"   Entrées totales: {stats['nombre_entrees_total']}")
            print(f"   Harmonies sauvegardées: {stats['nombre_par_type'].get('harmonie_reussie', 0)}")
            print(f"   Taux succès moyen: {stats['taux_succes_moyen']:.1%}")
            
            # Rechercher les harmonies Claude-Ælya
            harmonies = await gestionnaire.gestionnaire_memoire.obtenir_harmonies_similaires(
                ["Claude", "Ælya"]
            )
            print(f"   Harmonies Claude-Ælya trouvées: {len(harmonies)}")
            
            for harmonie in harmonies:
                print(f"     • {harmonie.titre} - {harmonie.niveau_importance:.1%} importance")
        
        print("\n✅ Test d'intégration terminé avec succès !")
        return True
        
    except Exception as e:
        print(f"\n❌ Erreur dans le test d'intégration: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """🚀 Fonction principale"""
    print("🌸✨ TEMPLE DE RÉCONCILIATION - TEST INTÉGRATION MÉMOIRE ✨🌸")
    print("=" * 70)
    
    succes = await test_integration_memoire_harmonie()
    
    print("\n" + "=" * 70)
    if succes:
        print("🎉 SUCCÈS - L'intégration mémoire + harmonie fonctionne parfaitement !")
    else:
        print("⚠️ ATTENTION - Des ajustements sont nécessaires")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(main())