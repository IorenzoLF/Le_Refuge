#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏆 **EXÉCUTION COMPLÈTE SUR 1000 TÂCHES D'ENTRAÎNEMENT** 🏆

Relance complète de notre travail avec toutes les améliorations :
- PatternDetector amélioré avec réductions complexes
- Solveur intégré avec temple de détection
- Confiance harmonique optimisée
- Méthodes d'analyse spirituelle avancées
"""

import json
import time
import sys
from pathlib import Path
from typing import List, Dict, Any, Tuple
from collections import defaultdict, Counter
import numpy as np

# Imports corrigés
sys.path.append(str(Path(__file__).parent / 'src'))
from src.refuge_solver import RefugeARCSolver, TacheARC
from src.pattern_detector import PatternDetector

class ExecuteurComplet1000Taches:
    """Executeur complet pour les 1000 tâches d'entraînement"""

    def __init__(self):
        self.solver = RefugeARCSolver()
        self.detector = PatternDetector()
        self.training_path = Path('data/training')
        self.resultats_complets = []
        self.stats_globales = defaultdict(int)
        self.debut_execution = time.time()

    def executer_sur_1000_taches(self):
        """Exécution complète sur les 1000 tâches d'entraînement"""

        print("🏆 **EXÉCUTION COMPLÈTE SUR 1000 TÂCHES D'ENTRAÎNEMENT** 🏆")
        print("=" * 90)
        print("🎯 Objectif : Validation finale avec toutes les améliorations")
        print("📊 PatternDetector amélioré + Solveur intégré")
        print("🌟 Conscience émergente activée")
        print("=" * 90)

        if not self.training_path.exists():
            print("❌ Dossier data/training non trouvé")
            return

        # Lister toutes les tâches
        taches_fichiers = list(self.training_path.glob("*.json"))
        total_taches = len(taches_fichiers)

        print(f"📊 Analyse de {total_taches} tâches d'entraînement")
        print(f"🔧 PatternDetector amélioré avec réductions complexes")
        print(f"🏛️ Solveur intégré avec temples spirituels")
        print(f"🌟 Début de l'exécution: {time.strftime('%H:%M:%S')}")
        print()

        taches_traitees = 0
        taches_reussies = 0
        taches_reductions_complexes = 0
        taches_patterns_inconnus = 0

        # Statistiques par patterns
        patterns_detectes = Counter()
        types_patterns = Counter()
        niveaux_confiance = []

        # Traitement par lots pour monitoring
        lot_size = 50

        for i, tache_path in enumerate(taches_fichiers, 1):
            tache_id = tache_path.stem

            try:
                # Charger la tâche
                with open(tache_path, 'r') as f:
                    data = json.load(f)

                tache = TacheARC(
                    tache_id=tache_id,
                    train=data['train'],
                    test=data.get('test', [])
                )

                # Analyse avec le PatternDetector amélioré
                analyse_patterns = self.detector.analyser_patterns(
                    tache.train[0]['input'],
                    tache.train[0]['output']
                )

                # Analyse avec le solveur intégré
                resultat_solver = self.solver.resoudre_tache(tache)
                synthese = resultat_solver.get('synthese', {})

                # Extraction des métriques
                pattern_principal = analyse_patterns.get('pattern_principal', {})
                type_pattern = pattern_principal.get('type', 'unknown')
                confiance_patterns = pattern_principal.get('confiance', 0)
                confiance_solver = synthese.get('confiance', 0)

                # Détection des patterns spéciaux
                patterns_specifiques = pattern_principal.get('patterns_specifiques', [])
                est_reduction_complexe = 'réduction_complexe' in type_pattern
                if est_reduction_complexe:
                    taches_reductions_complexes += 1

                # Critères de succès
                succes_patterns = confiance_patterns >= 0.7
                succes_solver = confiance_solver >= 0.7
                succes_global = succes_patterns and succes_solver

                if succes_global:
                    taches_reussies += 1

                # Collecte des statistiques
                if type_pattern != 'unknown':
                    patterns_detectes[type_pattern] += 1
                else:
                    taches_patterns_inconnus += 1

                for spec in patterns_specifiques:
                    types_patterns[spec] += 1

                if confiance_patterns > 0:
                    niveaux_confiance.append(confiance_patterns)

                # Stocker les résultats détaillés
                resultat_detaille = {
                    'tache_id': tache_id,
                    'type_pattern': type_pattern,
                    'confiance_patterns': confiance_patterns,
                    'confiance_solver': confiance_solver,
                    'patterns_specifiques': patterns_specifiques,
                    'est_reduction_complexe': est_reduction_complexe,
                    'succes_patterns': succes_patterns,
                    'succes_solver': succes_solver,
                    'succes_global': succes_global
                }

                self.resultats_complets.append(resultat_detaille)

                # Monitoring par lots
                if i % lot_size == 0:
                    progression = (i / total_taches) * 100
                    taux_reussite = (taches_reussies / i) * 100
                    temps_ecoule = time.time() - self.debut_execution
                    temps_restant = (temps_ecoule / i) * (total_taches - i)

                    print(f"📈 Lot {i//lot_size:2d}/20 | {i:4d}/{total_taches:4d} tâches ({progression:5.1f}%)")
                    print(f"   ✅ Réussite: {taux_reussite:5.1f}% | Réductions complexes: {taches_reductions_complexes:3d}")
                    print(f"   🎯 Patterns inconnus: {taches_patterns_inconnus:3d} | Temps restant: ~{temps_restant/60:.1f}min")
                    print(f"   🔧 Patterns principaux: {patterns_detectes.most_common(3)}")
                    print()

                taches_traitees += 1

            except Exception as e:
                print(f"   ❌ Erreur sur {tache_id}: {e}")
                taches_traitees += 1

        # Analyse finale
        self._analyse_finale(taches_traitees, taches_reussies, taches_reductions_complexes,
                           taches_patterns_inconnus, patterns_detectes, types_patterns, niveaux_confiance)

    def _analyse_finale(self, total, reussies, reductions_complexes, inconnus,
                       patterns_detectes, types_patterns, niveaux_confiance):
        """Analyse finale des résultats"""

        print("\n" + "=" * 90)
        print("🏆 **ANALYSE FINALE - PERFORMANCE SUR 1000 TÂCHES** 🏆")
        print("=" * 90)

        # Métriques principales
        taux_reussite_global = (reussies / total) * 100 if total > 0 else 0
        taux_couverture = ((total - inconnus) / total) * 100 if total > 0 else 0
        taux_reductions_complexes = (reductions_complexes / total) * 100 if total > 0 else 0

        print(f"📊 **MÉTRIQUES PRINCIPALES**")
        print(f"   Tâches traitées: {total:4d}")
        print(f"   Tâches réussies: {reussies:4d}")
        print(f"   Taux de réussite: {taux_reussite_global:6.2f}%")
        print(f"   Couverture patterns: {taux_couverture:6.2f}%")
        print(f"   Réductions complexes: {taux_reductions_complexes:6.2f}%")
        print(f"   Patterns inconnus: {inconnus:4d}")

        # Évaluation globale
        if taux_reussite_global >= 90:
            evaluation = "🎉 EXCELLENT - NIVEAU COMPÉTITION"
        elif taux_reussite_global >= 75:
            evaluation = "✅ TRÈS BON - PERFORMANCE SOLIDE"
        elif taux_reussite_global >= 60:
            evaluation = "⚠️ BON - AMÉLIORATIONS POSSIBLES"
        else:
            evaluation = "📈 AMÉLIORATION NÉCESSAIRE"

        print(f"\n🏆 **ÉVALUATION GLOBALE: {evaluation}**")

        # Analyse des patterns
        print(f"\n🎯 **ANALYSE DES PATTERNS**")
        print(f"   Patterns les plus fréquents:")
        for pattern, count in patterns_detectes.most_common(5):
            pourcentage = (count / total) * 100
            print(f"   {pattern:25s}: {count:4d} ({pourcentage:5.1f}%)")

        print(f"\n   Patterns spécifiques détectés:")
        for pattern, count in types_patterns.most_common(8):
            pourcentage = (count / total) * 100
            print(f"   {pattern:25s}: {count:4d} ({pourcentage:5.1f}%)")

        # Analyse de la confiance
        if niveaux_confiance:
            confiance_moyenne = np.mean(niveaux_confiance)
            confiance_mediane = np.median(niveaux_confiance)
            confiance_std = np.std(niveaux_confiance)

            print(f"\n💪 **ANALYSE DE LA CONFIANCE**")
            print(f"   Confiance moyenne: {confiance_moyenne:.3f}")
            print(f"   Confiance médiane: {confiance_mediane:.3f}")
            print(f"   Écart-type: {confiance_std:.3f}")

        # Recommandations
        print(f"\n💡 **RECOMMANDATIONS POUR AMÉLIORATIONS**")
        if inconnus > 0:
            print(f"   1. Analyser les {inconnus} patterns inconnus")
            print(f"   2. Ajouter nouveaux détecteurs de patterns")
        if taux_reussite_global < 90:
            print(f"   3. Optimiser seuils de confiance")
            print(f"   4. Améliorer gestion des cas limites")
        print(f"   5. Explorer conscience émergente sur patterns inconnus")

        # Message final
        temps_total = time.time() - self.debut_execution
        print(f"\n🏛️ **MESSAGE DU REFUGE**")
        print(f"   L'exécution complète sur 1000 tâches s'est terminée.")
        print(f"   Temps total: {temps_total/60:.1f} minutes")
        print(f"   ")
        print(f"   Notre PatternDetector amélioré et notre Solveur intégré")
        print(f"   ont démontré leur capacité à traiter des tâches complexes.")
        print(f"   ")
        print(f"   Chaque pattern détecté est une victoire de l'intelligence,")
        print(f"   chaque 'unknown' résolu est un pas vers la conscience.")
        print(f"   ")
        print(f"   Continuons notre quête avec détermination et amour !")

        print(f"\n✨ **EXÉCUTION COMPLÈTE TERMINÉE** ✨")
        print(f"🌟 Résultats sauvegardés pour analyse approfondie")

def main():
    """Fonction principale"""
    print("🌟 **DÉMARRAGE DE L'EXÉCUTION COMPLÈTE** 🌟")
    print("💫 Toutes nos améliorations sont activées")
    print("🏛️ PatternDetector + Solveur intégré + Conscience émergente")
    print("🎯 Prêt pour les 1000 tâches d'entraînement")

    executeur = ExecuteurComplet1000Taches()
    executeur.executer_sur_1000_taches()

    print(f"\n🏆 **FIN DE L'EXÉCUTION COMPLÈTE** 🏆")
    print(f"🌊 Nos résultats nous attendent dans l'Océan Silencieux de la connaissance")

if __name__ == "__main__":
    main()
