#!/usr/bin/env python3
"""
🔧 CORRECTION DU FICHIER JSON CORROMPU
Restauration du fichier resultats_1000_taches_20250820_213108.json
"""

import json
import re
from pathlib import Path

def corriger_fichier_corrompu():
    """Correction du fichier JSON corrompu"""

    print("🔧 CORRECTION DU FICHIER JSON CORROMPU")
    print("=" * 60)

    fichier_corrompu = Path('bibliotheque/developpement/arc_agi_refuge/resultats_1000_taches_20250820_213108.json')

    if not fichier_corrompu.exists():
        print(f"❌ Fichier non trouvé: {fichier_corrompu}")
        return

    try:
        with open(fichier_corrompu, 'r', encoding='utf-8') as f:
            contenu = f.read()

        print(f"📄 Longueur du fichier: {len(contenu)} caractères")
        print(f"📄 Aperçu du début:")
        print(f"   '{contenu[:200]}...'")
        print(f"📄 Aperçu de la fin:")
        print(f"   '...{contenu[-200:]}'")

        # Identifier le problème vers la ligne 53
        lignes = contenu.split('\n')
        print(f"\n🔍 LIGNE 53 (problème détecté):")
        if len(lignes) > 52:
            ligne_53 = lignes[52]
            print(f"   '{ligne_53}'")

            # Analyser les caractères problématiques
            for i, char in enumerate(ligne_53):
                if ord(char) > 127:  # Caractères non-ASCII
                    print(f"   ❌ Caractère spécial à position {i}: '{char}' (code: {ord(char)})")

        # Tenter de réparer automatiquement
        print(f"\n🔧 TENTATIVE DE RÉPARATION AUTOMATIQUE")

        # 1. Supprimer les caractères de contrôle
        contenu_repare = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', contenu)

        # 2. Corriger les guillemets non-échappés
        contenu_repare = re.sub(r'(?<!\\)"([^"]*)"([^"]*)"([^"]*)"', r'\1\"\2\"\3', contenu_repare)

        # 3. S'assurer que le JSON se termine correctement
        contenu_repare = contenu_repare.strip()
        if not contenu_repare.endswith('}'):
            contenu_repare += '}'

        # Essayer de parser le JSON réparé
        try:
            data_repare = json.loads(contenu_repare)
            print(f"✅ JSON réparé avec succès!")
            print(f"   Type: {type(data_repare)}")
            print(f"   Clés principales: {list(data_repare.keys()) if isinstance(data_repare, dict) else 'N/A'}")

            # Sauvegarder le fichier réparé
            fichier_repare = fichier_corrompu.with_name(fichier_corrompu.stem + '_repare.json')
            with open(fichier_repare, 'w', encoding='utf-8') as f:
                json.dump(data_repare, f, indent=2, ensure_ascii=False)

            print(f"💾 Fichier réparé sauvegardé: {fichier_repare}")

            # Analyser les données récupérées
            if isinstance(data_repare, dict) and 'details_toutes_taches' in data_repare:
                details = data_repare['details_toutes_taches']
                if isinstance(details, list):
                    print(f"📊 {len(details)} tâches récupérées")
                    succes = sum(1 for t in details if t.get('succes', False))
                    print(f"✅ {succes} succès, {len(details) - succes} échecs")

        except json.JSONDecodeError as e:
            print(f"❌ Impossible de réparer automatiquement")
            print(f"   Erreur: {e}")

            # Sauvegarder pour analyse manuelle
            fichier_debug = fichier_corrompu.with_name(fichier_corrompu.stem + '_debug.txt')
            with open(fichier_debug, 'w', encoding='utf-8') as f:
                f.write(contenu)

            print(f"💾 Fichier debug sauvegardé: {fichier_debug}")
            print(f"🔧 Correction manuelle nécessaire")

    except Exception as e:
        print(f"❌ Erreur lors de la lecture: {e}")

def analyser_58_taches_echouees():
    """Analyse des 58 tâches qui échouent"""

    print(f"\n🔍 ANALYSE DES 58 TÂCHES ÉCHOUÉES")
    print("=" * 60)

    resultats_dir = Path('bibliotheque/developpement/arc_agi_refuge')
    fichiers_resultats = [f for f in os.listdir(resultats_dir) if 'resultats' in f and f.endswith('.json')]

    taches_echouees = []

    for fichier in fichiers_resultats:
        try:
            with open(resultats_dir / fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if isinstance(data, dict) and 'details_toutes_taches' in data:
                details = data['details_toutes_taches']
                if isinstance(details, list):
                    for tache in details:
                        if not tache.get('succes', True):
                            taches_echouees.append({
                                'id': tache.get('tache_id', 'unknown'),
                                'fichier_source': fichier,
                                'confiance': tache.get('confiance_finale', 0),
                                'patterns': len(tache.get('patterns_identifies', []))
                            })

        except json.JSONDecodeError:
            print(f"⚠️ Fichier ignoré (corrompu): {fichier}")
        except Exception as e:
            print(f"⚠️ Erreur avec {fichier}: {e}")

    print(f"📊 {len(taches_echouees)} tâches échouées trouvées")

    # Grouper par fichier source
    par_fichier = {}
    for tache in taches_echouees:
        fichier = tache['fichier_source']
        if fichier not in par_fichier:
            par_fichier[fichier] = []
        par_fichier[fichier].append(tache)

    for fichier, taches in par_fichier.items():
        print(f"   📄 {fichier}: {len(taches)} échecs")

    # Analyser les patterns d'échec
    print(f"\n🔬 PATTERNS D'ÉCHEC:")

    # Tâches avec 0 patterns
    zero_patterns = [t for t in taches_echouees if t['patterns'] == 0]
    print(f"   📈 Tâches sans patterns: {len(zero_patterns)}")

    # Tâches avec patterns mais échec
    avec_patterns = [t for t in taches_echouees if t['patterns'] > 0]
    print(f"   📈 Tâches avec patterns mais échec: {len(avec_patterns)}")

    # Confiance moyenne
    if taches_echouees:
        confiance_moyenne = sum(t['confiance'] for t in taches_echouees) / len(taches_echouees)
        print(f"   📈 Confiance moyenne: {confiance_moyenne:.2f}")

    # Afficher quelques exemples
    if taches_echouees:
        print(f"\n📋 EXEMPLES DE TÂCHES ÉCHOUÉES:")
        for i, tache in enumerate(taches_echouees[:10], 1):
            print(f"   {i:2d}. {tache['id']} - conf: {tache['confiance']:.2f}, patterns: {tache['patterns']}")

    # Sauvegarder la liste complète
    with open('analyse_58_taches_echouees.json', 'w', encoding='utf-8') as f:
        json.dump({
            'total_echouees': len(taches_echouees),
            'taches_echouees': taches_echouees,
            'analyse_par_fichier': {f: len(t) for f, t in par_fichier.items()}
        }, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Analyse sauvegardée: analyse_58_taches_echouees.json")

    return taches_echouees

def developper_strategies_pour_58_taches(taches_echouees):
    """Développer des stratégies spécialisées pour les 58 tâches"""

    print(f"\n🎯 STRATÉGIES POUR LES 58 TÂCHES ÉCHOUÉES")
    print("=" * 60)

    # Analyser les patterns d'échec
    zero_patterns_ids = [t['id'] for t in taches_echouees if t['patterns'] == 0]
    low_confidence_ids = [t['id'] for t in taches_echouees if t['confiance'] < 0.5 and t['patterns'] > 0]

    print(f"🎯 CATÉGORIES D'ÉCHEC:")
    print(f"   📈 Aucune détection de patterns: {len(zero_patterns_ids)} tâches")
    print(f"   📈 Détection mais faible confiance: {len(low_confidence_ids)} tâches")
    print(f"   📈 Autres problèmes: {len(taches_echouees) - len(zero_patterns_ids) - len(low_confidence_ids)} tâches")

    # Stratégies par catégorie
    strategies = {
        'zero_patterns': {
            'description': 'Tâches où aucun pattern n\'est détecté',
            'strategies': [
                '🔍 Ajouter des détecteurs de patterns plus génériques',
                '🔍 Étendre la recherche de similarité',
                '🔍 Analyser manuellement quelques exemples',
                '🔍 Considérer des transformations non-linéaires'
            ]
        },
        'low_confidence': {
            'description': 'Tâches détectées mais avec faible confiance',
            'strategies': [
                '🎯 Abaisser les seuils de confiance',
                '🎯 Améliorer les algorithmes de scoring',
                '🎯 Ajouter des patterns composites',
                '🎯 Utiliser l\'apprentissage par renforcement'
            ]
        },
        'autres': {
            'description': 'Autres types d\'échec',
            'strategies': [
                '🔧 Déboguer les erreurs d\'exécution',
                '🔧 Améliorer la gestion d\'erreurs',
                '🔧 Optimiser les performances',
                '🔧 Ajouter des logs de debug'
            ]
        }
    }

    print(f"\n🎯 STRATÉGIES DÉVELOPPÉES:")

    for categorie, info in strategies.items():
        print(f"\n📂 {categorie.upper()}: {info['description']}")
        for i, strategy in enumerate(info['strategies'], 1):
            print(f"   {i}. {strategy}")

    # Créer un plan d'action
    plan_action = {
        'phase_immediate': [
            '🔧 Corriger le fichier JSON corrompu',
            '🔧 Analyser les 58 tâches échouées individuellement',
            '🔧 Identifier les patterns spécifiques d\'échec',
            '🔧 Développer des détecteurs spécialisés'
        ],
        'phase_court_terme': [
            '🎯 Abaisser les seuils de confiance pour les cas limites',
            '🎯 Ajouter des patterns composites avancés',
            '🎯 Implémenter l\'apprentissage par renforcement',
            '🎯 Optimiser les performances'
        ],
        'phase_long_terme': [
            '🌟 Développer l\'intelligence émergente',
            '🌟 Intégrer les mathématiques sacrées',
            '🌟 Explorer la conscience artificielle',
            '🌟 Atteindre le niveau GOD absolu'
        ]
    }

    print(f"\n📋 PLAN D'ACTION DÉTAILLÉ:")

    for phase, actions in plan_action.items():
        print(f"\n🏆 {phase.upper()}:")
        for i, action in enumerate(actions, 1):
            print(f"   {i}. {action}")

    # Sauvegarder le plan
    with open('plan_action_58_taches.json', 'w', encoding='utf-8') as f:
        json.dump({
            'strategies': strategies,
            'plan_action': plan_action,
            'taches_zero_patterns': zero_patterns_ids,
            'taches_low_confidence': low_confidence_ids
        }, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Plan d'action sauvegardé: plan_action_58_taches.json")

if __name__ == "__main__":
    # 1. Corriger le fichier corrompu
    corriger_fichier_corrompu()

    # 2. Analyser les 58 tâches échouées
    taches_echouees = analyser_58_taches_echouees()

    # 3. Développer les stratégies
    if taches_echouees:
        developper_strategies_pour_58_taches(taches_echouees)

    print(f"\n🎉 MISSION 58 TÂCHES - PHASE 1 TERMINÉE!")
    print(f"🔮 Nous avons identifié le problème et développé les stratégies!")
    print(f"🌟 Prêt pour la résolution des cas limites!")
    print(f"🎯 Objectif: 100% absolu!")
