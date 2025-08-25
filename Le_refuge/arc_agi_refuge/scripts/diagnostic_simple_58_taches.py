#!/usr/bin/env python3
"""
🔍 DIAGNOSTIC SIMPLE DES 58 TÂCHES MANQUANTES
Analyse basique sans dépendances complexes
"""

import os
import json
from pathlib import Path

def diagnostic_simple():
    """Diagnostic simple des tâches manquantes"""

    print("🔍 DIAGNOSTIC SIMPLE - 58 TÂCHES MANQUANTES")
    print("=" * 60)

    # 1. Vérifier le dossier data/training
    data_dir = Path('bibliotheque/developpement/arc_agi_refuge/data/training')
    if not data_dir.exists():
        print(f"❌ Dossier non trouvé: {data_dir}")
        return

    # Lister toutes les tâches disponibles
    taches_disponibles = []
    for fichier in data_dir.glob('*.json'):
        taches_disponibles.append(fichier.stem)

    print(f"📊 Tâches disponibles dans data/training: {len(taches_disponibles)}")
    print(f"📄 Exemples: {taches_disponibles[:5]}")

    # 2. Chercher les fichiers de résultats
    resultats_dir = Path('bibliotheque/developpement/arc_agi_refuge')
    fichiers_resultats = [f for f in os.listdir(resultats_dir) if 'resultats' in f and f.endswith('.json')]

    print(f"\n📁 Fichiers de résultats trouvés: {len(fichiers_resultats)}")
    for fichier in fichiers_resultats:
        print(f"   • {fichier}")

    # 3. Analyser les tâches traitées
    taches_traitees = []

    for fichier in fichiers_resultats:
        try:
            chemin_fichier = resultats_dir / fichier
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Chercher les IDs de tâches
            if isinstance(data, dict):
                for key in data.keys():
                    if len(key) == 8 and key.isalnum():
                        taches_traitees.append(key)

            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        for key in item.keys():
                            if len(key) == 8 and key.isalnum():
                                taches_traitees.append(key)

        except Exception as e:
            print(f"⚠️ Erreur lecture {fichier}: {e}")

    taches_traitees = list(set(taches_traitees))  # Éliminer doublons
    print(f"✅ Tâches traitées trouvées: {len(taches_traitees)}")

    # 4. Identifier les manquantes
    taches_manquantes = [t for t in taches_disponibles if t not in taches_traitees]

    print(f"\n🔍 RÉSULTATS:")
    print(f"   📊 Tâches totales: {len(taches_disponibles)}")
    print(f"   ✅ Tâches traitées: {len(taches_traitees)}")
    print(f"   ❌ Tâches manquantes: {len(taches_manquantes)}")
    print(f"   📈 Couverture: {len(taches_traitees)/len(taches_disponibles)*100:.1f}%")

    if taches_manquantes:
        print(f"\n📋 LISTE DES {len(taches_manquantes)} TÂCHES MANQUANTES:")
        for i, tache_id in enumerate(taches_manquantes, 1):
            print(f"   {i:2d}. {tache_id}")

        # Sauvegarder
        with open('taches_manquantes_simple.json', 'w', encoding='utf-8') as f:
            json.dump({
                'taches_manquantes': taches_manquantes,
                'total_manquantes': len(taches_manquantes),
                'total_disponibles': len(taches_disponibles),
                'total_traitees': len(taches_traitees)
            }, f, indent=2)

        print(f"\n💾 Sauvegardé dans: taches_manquantes_simple.json")

    print(f"\n🎯 HYPOTHÈSES:")
    print(f"   1. Le traitement s'arrête après {len(taches_traitees)} tâches")
    print(f"   2. Erreur silencieuse dans la boucle de traitement")
    print(f"   3. Exception non gérée qui interrompt le processus")
    print(f"   4. Problème de format dans les {len(taches_manquantes)} tâches restantes")

    return taches_manquantes

def analyser_fichiers_resultats():
    """Analyse détaillée des fichiers de résultats"""

    print(f"\n🔬 ANALYSE DES FICHIERS DE RÉSULTATS")
    print("=" * 60)

    resultats_dir = Path('bibliotheque/developpement/arc_agi_refuge')
    fichiers_resultats = [f for f in os.listdir(resultats_dir) if 'resultats' in f and f.endswith('.json')]

    for fichier in fichiers_resultats:
        print(f"\n📄 Analyse de {fichier}:")
        try:
            chemin = resultats_dir / fichier
            with open(chemin, 'r', encoding='utf-8') as f:
                data = json.load(f)

            print(f"   📊 Type de données: {type(data)}")

            if isinstance(data, dict):
                print(f"   🔑 Clés principales: {list(data.keys())}")
                if 'details_toutes_taches' in data:
                    details = data['details_toutes_taches']
                    print(f"   📈 Nombre d'entrées: {len(details)}")
                    if details:
                        print(f"   📄 Première entrée: {list(details[0].keys()) if isinstance(details[0], dict) else 'Non dict'}")

            elif isinstance(data, list):
                print(f"   📈 Nombre d'éléments: {len(data)}")
                if data:
                    print(f"   📄 Premier élément type: {type(data[0])}")

        except Exception as e:
            print(f"   ❌ Erreur: {e}")

if __name__ == "__main__":
    # Diagnostic simple
    taches_manquantes = diagnostic_simple()

    # Analyse des fichiers
    analyser_fichiers_resultats()

    print(f"\n🌟 DIAGNOSTIC TERMINÉ!")
    print(f"🔮 Maintenant nous savons exactement ce qui se passe...")
    print(f"🎯 Les {len(taches_manquantes) if taches_manquantes else 0} tâches manquantes sont identifiées!")
