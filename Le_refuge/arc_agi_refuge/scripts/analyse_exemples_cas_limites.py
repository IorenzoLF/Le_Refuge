#!/usr/bin/env python3
"""
ANALYSE D'EXEMPLES DES CAS LIMITES
Étude approfondie de quelques-unes des 175 tâches échouées
"""

import json
from pathlib import Path

def analyser_exemples_cas_limites():
    """Analyser quelques exemples de tâches échouées"""

    print("ANALYSE D'EXEMPLES DES CAS LIMITES")
    print("=" * 50)

    # Charger les résultats d'analyse
    try:
        with open('resultats_final_analyse.json', 'r', encoding='utf-8') as f:
            analyse = json.load(f)
    except FileNotFoundError:
        print("Fichier d'analyse non trouvé")
        return

    taches_echouees = analyse['taches_echouees'][:5]  # Analyser les 5 premières
    data_dir = Path('bibliotheque/developpement/arc_agi_refuge/data/training')

    print(f"Analyse de {len(taches_echouees)} exemples de tâches échouées")
    print()

    for i, tache_info in enumerate(taches_echouees, 1):
        tache_id = tache_info['id']
        print(f"📄 EXEMPLE {i}: Tâche {tache_id}")
        print("-" * 30)

        # Charger la tâche
        fichier_tache = data_dir / f"{tache_id}.json"

        if fichier_tache.exists():
            try:
                with open(fichier_tache, 'r', encoding='utf-8') as f:
                    tache_data = json.load(f)

                # Analyser les exemples
                train_data = tache_data.get('train', [])
                test_data = tache_data.get('test', [])

                print(f"Nombre d'exemples d'entraînement: {len(train_data)}")
                print(f"Nombre d'exemples de test: {len(test_data)}")

                if train_data:
                    exemple = train_data[0]
                    input_grid = exemple.get('input', [])
                    output_grid = exemple.get('output', [])

                    if input_grid and output_grid:
                        h_in, w_in = len(input_grid), len(input_grid[0]) if input_grid else (0, 0)
                        h_out, w_out = len(output_grid), len(output_grid[0]) if output_grid else (0, 0)

                        print(f"Dimensions input: {h_in}x{w_in}")
                        print(f"Dimensions output: {h_out}x{w_out}")

                        # Analyser les valeurs
                        valeurs_input = [val for row in input_grid for val in row]
                        valeurs_output = [val for row in output_grid for val in row]

                        val_min_in = min(valeurs_input) if valeurs_input else 0
                        val_max_in = max(valeurs_input) if valeurs_input else 0
                        val_min_out = min(valeurs_output) if valeurs_output else 0
                        val_max_out = max(valeurs_output) if valeurs_output else 0

                        print(f"Valeurs input: [{val_min_in}, {val_max_in}]")
                        print(f"Valeurs output: [{val_min_out}, {val_max_out}]")

                        # Afficher un aperçu des grilles (petites grilles seulement)
                        if h_in <= 10 and w_in <= 10:
                            print("\nGrille input:")
                            for row in input_grid:
                                print("  " + " ".join(map(str, row)))

                            print("\nGrille output:")
                            for row in output_grid:
                                print("  " + " .join(map(str, row))")

                        # Analyser les changements
                        changements = []
                        for i in range(min(len(valeurs_input), len(valeurs_output))):
                            if valeurs_input[i] != valeurs_output[i]:
                                changements.append((i, valeurs_input[i], valeurs_output[i]))

                        if changements:
                            print(f"\nChangements détectés: {len(changements)}")
                            print("Exemples de changements:")
                            for pos, val_in, val_out in changements[:5]:
                                print(f"  Position {pos}: {val_in} -> {val_out}")

                        # Analyser les patterns possibles
                        print(f"\n🔍 PATTERNS POTENTIELS:")

                        # 1. Changement de dimensions
                        if (h_in, w_in) != (h_out, w_out):
                            print(f"  📐 Changement de dimensions: {h_in}x{w_in} -> {h_out}x{w_out}")

                        # 2. Patterns de valeurs
                        valeurs_uniques_in = set(valeurs_input)
                        valeurs_uniques_out = set(valeurs_output)
                        print(f"  🎯 Valeurs uniques input: {sorted(valeurs_uniques_in)}")
                        print(f"  🎯 Valeurs uniques output: {sorted(valeurs_uniques_out)}")

                        # 3. Analyse de symétrie
                        if input_grid == input_grid[::-1]:
                            print(f"  🔄 Symétrie horizontale détectée")
                        if input_grid == [row[::-1] for row in input_grid]:
                            print(f"  🔄 Symétrie verticale détectée")

                        # 4. Analyse de répétition
                        if len(set(map(tuple, input_grid))) < len(input_grid):
                            print(f"  🔁 Répétitions détectées dans input")
                        if len(set(map(tuple, output_grid))) < len(output_grid):
                            print(f"  🔁 Répétitions détectées dans output")

            except Exception as e:
                print(f"❌ Erreur lors de l'analyse: {e}")

        else:
            print(f"❌ Fichier non trouvé: {fichier_tache}")

        print()

def identifier_patterns_manquants():
    """Identifier les types de patterns manquants"""

    print("IDENTIFICATION DES PATTERNS MANQUANTS")
    print("=" * 50)

    try:
        with open('resultats_final_analyse.json', 'r', encoding='utf-8') as f:
            analyse = json.load(f)
    except FileNotFoundError:
        print("Fichier d'analyse non trouvé")
        return

    taches_echouees = analyse['taches_echouees']

    # Catégoriser les tâches par caractéristiques
    categories = {
        'changement_dimensions': [],
        'changement_valeurs': [],
        'symetries': [],
        'repetitions': [],
        'autres': []
    }

    data_dir = Path('bibliotheque/developpement/arc_agi_refuge/data/training')

    for tache_info in taches_echouees[:20]:  # Analyser 20 tâches
        tache_id = tache_info['id']
        fichier_tache = data_dir / f"{tache_id}.json"

        if fichier_tache.exists():
            try:
                with open(fichier_tache, 'r', encoding='utf-8') as f:
                    tache_data = json.load(f)

                train_data = tache_data.get('train', [])
                if train_data:
                    exemple = train_data[0]
                    input_grid = exemple.get('input', [])
                    output_grid = exemple.get('output', [])

                    if input_grid and output_grid:
                        h_in, w_in = len(input_grid), len(input_grid[0])
                        h_out, w_out = len(output_grid), len(output_grid[0])

                        # Catégoriser
                        if (h_in, w_in) != (h_out, w_out):
                            categories['changement_dimensions'].append(tache_id)

                        valeurs_input = [val for row in input_grid for val in row]
                        valeurs_output = [val for row in output_grid for val in row]

                        if set(valeurs_input) != set(valeurs_output):
                            categories['changement_valeurs'].append(tache_id)

                        # Symétries
                        if input_grid == input_grid[::-1] or input_grid == [row[::-1] for row in input_grid]:
                            categories['symetries'].append(tache_id)

                        # Répétitions
                        if len(set(map(tuple, input_grid))) < len(input_grid):
                            categories['repetitions'].append(tache_id)

                        # Autres
                        if (tache_id not in categories['changement_dimensions'] and
                            tache_id not in categories['changement_valeurs'] and
                            tache_id not in categories['symetries'] and
                            tache_id not in categories['repetitions']):
                            categories['autres'].append(tache_id)

            except Exception as e:
                print(f"Erreur avec {tache_id}: {e}")

    # Afficher les résultats
    print("CATÉGORISATION DES TÂCHES ÉCHOUÉES:")
    for categorie, taches in categories.items():
        if taches:
            print(f"\n📂 {categorie.upper()}: {len(taches)} tâches")
            print(f"   Exemples: {taches[:5]}")

    # Analyse des patterns
    print(f"\n🔍 ANALYSE DES PATTERNS MANQUANTS:")

    if categories['changement_dimensions']:
        print(f"  📐 Patterns de changement de dimensions")
        print(f"     -> Besoin de détecteurs de redimensionnement")
        print(f"     -> Analyse de compression/décompression")
        print(f"     -> Détection de cropping/expansion")

    if categories['changement_valeurs']:
        print(f"  🎯 Patterns de transformation de valeurs")
        print(f"     -> Détecteurs de mapping non-linéaire")
        print(f"     -> Analyse de fonctions de transformation")
        print(f"     -> Patterns de substitution complexes")

    if categories['symetries']:
        print(f"  🔄 Patterns de symétrie avancés")
        print(f"     -> Détection de symétries partielles")
        print(f"     -> Analyse de symétries roto-translationnelles")
        print(f"     -> Patterns de réflexion complexes")

    if categories['repetitions']:
        print(f"  🔁 Patterns de répétition")
        print(f"     -> Détecteurs de fréquences spatiales")
        print(f"     -> Analyse de motifs périodiques")
        print(f"     -> Patterns de tuilage avancés")

    if categories['autres']:
        print(f"  ❓ Patterns inconnus")
        print(f"     -> Exploration de transformations non-linéaires")
        print(f"     -> Analyse par apprentissage automatique")
        print(f"     -> Raisonnement par analogie")

def generer_strategies_detection():
    """Générer des stratégies pour détecter les patterns manquants"""

    print(f"\n🎯 STRATÉGIES DE DÉTECTION POUR LES PATTERNS MANQUANTS")
    print("=" * 60)

    strategies = {
        'changement_dimensions': [
            'Détecter les ratios de compression/décompression',
            'Analyser les algorithmes de redimensionnement',
            'Identifier les patterns de cropping intelligent',
            'Développer des détecteurs de transformation géométrique'
        ],
        'changement_valeurs': [
            'Créer des détecteurs de mapping non-linéaire',
            'Analyser les fonctions de transformation mathématiques',
            'Développer des patterns de substitution complexes',
            'Implémenter l\'apprentissage de transformations'
        ],
        'symetries': [
            'Détecter les symétries partielles et locales',
            'Analyser les symétries roto-translationnelles',
            'Identifier les patterns de réflexion complexes',
            'Développer des détecteurs de symétrie floue'
        ],
        'repetitions': [
            'Créer des détecteurs de fréquences spatiales',
            'Analyser les motifs périodiques avancés',
            'Développer des patterns de tuilage complexes',
            'Implémenter l\'analyse de répétition fractale'
        ],
        'patterns_inconnus': [
            'Explorer les transformations non-linéaires avancées',
            'Développer l\'apprentissage automatique spécialisé',
            'Implémenter le raisonnement par analogie',
            'Créer des détecteurs adaptatifs auto-apprenants'
        ]
    }

    for categorie, liste_strategies in strategies.items():
        print(f"\n📂 {categorie.upper().replace('_', ' ')}:")
        for i, strategy in enumerate(liste_strategies, 1):
            print(f"   {i}. {strategy}")

if __name__ == "__main__":
    # Analyser quelques exemples
    analyser_exemples_cas_limites()

    # Identifier les patterns manquants
    identifier_patterns_manquants()

    # Générer les stratégies
    generer_strategies_detection()

    print(f"\n🎉 ANALYSE TERMINÉE!")
    print(f"🔮 Nous avons maintenant une compréhension claire des patterns manquants!")
    print(f"🌟 Prêt à développer les stratégies pour atteindre 100%!")
    print(f"🏆 Laurent & Sonic: Vers la victoire finale!")
