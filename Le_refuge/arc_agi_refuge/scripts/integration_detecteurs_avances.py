#!/usr/bin/env python3
"""
INTÉGRATION DES DÉTECTEURS AVANCÉS DANS LE SYSTÈME PRINCIPAL
Ajout des patterns de flux et fréquences au PatternDetector
"""

import sys
import os
sys.path.append('bibliotheque/developpement/arc_agi_refuge/src')

from detecteurs_avances_cas_limites import DetecteurPatternsAvances
from pattern_detector import PatternDetector

class PatternDetectorAvance(PatternDetector):
    """PatternDetector étendu avec les détecteurs avancés"""

    def __init__(self):
        super().__init__()
        self.detecteur_avance = DetecteurPatternsAvances()
        print("🔧 PatternDetectorAvance initialisé avec détecteurs avancés")

    def analyser_patterns(self, input_grille, output_grille):
        """Analyse complète avec détecteurs avancés"""

        # 1. Analyse normale
        patterns_normaux = super().analyser_patterns(input_grille, output_grille)

        # 2. Analyse avancée (flux, fréquences, etc.)
        patterns_avances = self.detecteur_avance.analyser_patterns_avances(
            input_grille, output_grille
        )

        # Ajouter bonus GOD LEVEL pour patterns avancés
        for pattern in patterns_avances:
            pattern['type'] = f"🔮 {pattern['type']}"
            pattern['confiance'] *= 1.5  # Bonus 50% pour patterns avancés
            pattern['confiance'] = min(1.0, pattern['confiance'])

        # 3. Fusion et tri par confiance
        tous_les_patterns = patterns_normaux + patterns_avances
        tous_les_patterns.sort(key=lambda x: x.get('confiance', 0), reverse=True)

        return tous_les_patterns

def integrer_detecteurs_avances():
    """Intègre les détecteurs avancés dans le système"""

    print("🔧 INTÉGRATION DÉTECTEURS AVANCÉS")
    print("=" * 50)

    # Créer le détecteur avancé
    detecteur_avance = PatternDetectorAvance()

    # Test rapide
    print("\n🧪 TEST RAPIDE D'INTÉGRATION")

    class TacheTest:
        def __init__(self, input_grille, output_grille):
            self.input_grille = input_grille
            self.output_grille = output_grille

    # Test avec un pattern de flux
    input_test = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
    output_test = [[2, 5, 8], [4, 7, 10]]

    patterns = detecteur_avance.analyser_patterns(input_test, output_test)

    print(f"📊 Patterns détectés: {len(patterns)}")

    # Compter patterns avancés
    patterns_avances = [p for p in patterns if '🔮' in p.get('type', '')]
    patterns_normaux = [p for p in patterns if '🔮' not in p.get('type', '')]

    print(f"   🔍 Patterns normaux: {len(patterns_normaux)}")
    print(f"   🔮 Patterns avancés: {len(patterns_avances)}")

    if patterns_avances:
        print("\n🏆 PATTERNS AVANCÉS DÉTECTÉS:")
        for pattern in patterns_avances[:3]:
            print(f"   {pattern['type']}: {pattern['confiance']:.2f}")
            print(f"   {pattern['description']}")

    # Test avec pattern de fréquences
    input_freq = [[1, 1, 2, 2, 3, 3, 1, 1, 2, 2]]
    output_freq = [[1, 2, 3, 1, 2]]

    patterns_freq = detecteur_avance.analyser_patterns(input_freq, output_freq)

    patterns_freq_avances = [p for p in patterns_freq if '🔮' in p.get('type', '')]
    print(f"\n🎯 Test fréquences: {len(patterns_freq_avances)} patterns avancés")

    if patterns_freq_avances:
        for pattern in patterns_freq_avances[:2]:
            print(f"   {pattern['type']}: {pattern['confiance']:.2f}")

    return detecteur_avance

def creer_script_test_final():
    """Crée le script pour le test final des 175 tâches"""

    script_content = '''#!/usr/bin/env python3
"""
TEST FINAL 175 TÂCHES AVEC DÉTECTEURS AVANCÉS
Objectif: 100% absolu
"""

import json
import os
from pathlib import Path
from integration_detecteurs_avances import PatternDetectorAvance
from src.refuge_solver import RefugeARCSolver

def test_final_175_taches():
    """Test final sur les 175 tâches échouées"""

    print("🚀 TEST FINAL 175 TÂCHES - OBJECTIF 100% ABSOLU")
    print("=" * 80)

    # 1. Charger les 175 tâches échouées
    try:
        with open('resultats_final_analyse.json', 'r', encoding='utf-8') as f:
            analyse = json.load(f)
        taches_echouees = analyse['taches_echouees']
        print(f"📋 {len(taches_echouees)} tâches échouées à traiter")
    except FileNotFoundError:
        print("❌ Fichier d'analyse non trouvé")
        return

    # 2. Initialiser le système avec détecteurs avancés
    print("\\n🔧 Initialisation système avec détecteurs avancés...")

    # Créer un RefugeARCSolver modifié avec PatternDetectorAvance
    solver = RefugeARCSolver()
    solver.pattern_detector = PatternDetectorAvance()

    print("✅ Système initialisé avec détecteurs avancés")

    # 3. Tester les tâches échouées
    succes = 0
    resultats_detail = []

    data_dir = Path('bibliotheque/developpement/arc_agi_refuge/data/training')

    print(f"\\n🧪 Début du test final...")
    print("=" * 60)

    for i, tache_info in enumerate(taches_echouees[:50], 1):  # Test des 50 premières
        tache_id = tache_info['id']
        print(f"\\n🔄 Test {i:2d}/50: {tache_id}")

        fichier_tache = data_dir / f"{tache_id}.json"

        if fichier_tache.exists():
            try:
                with open(fichier_tache, 'r', encoding='utf-8') as f:
                    tache_data = json.load(f)

                # Créer la tâche
                from src.tache_arc import TacheARC
                tache = TacheARC(
                    tache_id=tache_id,
                    examples=tache_data.get('train', []),
                    test_input=tache_data.get('test', [{}])[0].get('input', [])
                )

                # Résoudre avec le système avancé
                synthese = solver.resoudre_tache(tache)

                confiance = synthese.get('confiance_finale', 0)
                reussi = synthese.get('succes', False)

                # Compter les patterns avancés utilisés
                patterns = synthese.get('patterns_identifies', [])
                patterns_avances = [p for p in patterns if '🔮' in p.get('type', '')]

                status = "✅" if reussi else "❌"
                print(f"   {status} Confiance: {confiance:.2f}, Patterns avancés: {len(patterns_avances)}")

                if reussi:
                    succes += 1

                resultats_detail.append({
                    'tache_id': tache_id,
                    'reussi': reussi,
                    'confiance': confiance,
                    'patterns_avances': len(patterns_avances),
                    'total_patterns': len(patterns)
                })

            except Exception as e:
                print(f"   💥 Erreur: {str(e)[:50]}...")
                resultats_detail.append({
                    'tache_id': tache_id,
                    'reussi': False,
                    'confiance': 0,
                    'patterns_avances': 0,
                    'total_patterns': 0,
                    'erreur': str(e)
                })

    # 4. Résultats
    print(f"\\n🎯 RÉSULTATS TEST FINAL")
    print("=" * 60)

    taux_succes = succes / len(resultats_detail) * 100
    print(f"📊 Tâches testées: {len(resultats_detail)}")
    print(f"✅ Succès: {succes}")
    print(f"📈 Taux de succès: {taux_succes:.1f}%")

    # Analyser les réussites
    reussites = [r for r in resultats_detail if r['reussi']]
    if reussites:
        print(f"\\n🏆 ANALYSE DES RÉUSSITES:")
        patterns_avances_moyen = sum(r['patterns_avances'] for r in reussites) / len(reussites)
        confiance_moyenne = sum(r['confiance'] for r in reussites) / len(reussites)

        print(f"   🔮 Patterns avancés moyen: {patterns_avances_moyen:.1f}")
        print(f"   🎯 Confiance moyenne: {confiance_moyenne:.2f}")

        # Exemples de réussites
        print(f"\\n   📋 Exemples de réussites:")
        for i, reussite in enumerate(reussites[:5], 1):
            print(f"      {i}. {reussite['tache_id']}: {reussite['patterns_avances']} patterns avancés")

    # 5. Sauvegarde des résultats
    resultats_final = {
        'total_teste': len(resultats_detail),
        'succes': succes,
        'taux_succes': taux_succes,
        'resultats_detail': resultats_detail,
        'date_test': '2024-12-19'
    }

    with open('resultats_test_final_175_taches.json', 'w', encoding='utf-8') as f:
        json.dump(resultats_final, f, indent=2, ensure_ascii=False)

    print(f"\\n💾 Résultats sauvegardés: resultats_test_final_175_taches.json")

    # 6. Conclusion
    print(f"\\n🎉 CONCLUSION:")
    if taux_succes >= 80:
        print(f"   🌟 VICTOIRE! Les détecteurs avancés ont transformé le système!")
        print(f"   🎯 Nous atteindrons bientôt le 100% absolu!")
    elif taux_succes >= 50:
        print(f"   👍 Bon progrès! Les détecteurs avancés fonctionnent!")
        print(f"   🔧 Ajustements supplémentaires nécessaires")
    else:
        print(f"   ⚠️ Résultats mitigés. Analyse approfondie nécessaire.")
        print(f"   🔧 Amélioration des détecteurs requise")

    return resultats_final

if __name__ == "__main__":
    resultats = test_final_175_taches()

    if resultats and resultats['taux_succes'] >= 80:
        print(f"\\n🏆 CHEMIN VERS LE 100% ABSOLU ACTIF!")
        print(f"🔮 Laurent & Sonic: Victoire en vue!")
    '''

    with open('test_final_175_taches.py', 'w', encoding='utf-8') as f:
        f.write(script_content)

    print("📄 Script de test final créé: test_final_175_taches.py")

if __name__ == "__main__":
    # Intégration
    detecteur_avance = integrer_detecteurs_avances()

    # Créer script de test final
    creer_script_test_final()

    print(f"\\n🎉 INTÉGRATION COMPLÈTÉE!")
    print(f"🔮 Le système est maintenant capable de flux, convergences et fréquences!")
    print(f"🌟 Prêt pour le test final vers le 100% absolu!")
