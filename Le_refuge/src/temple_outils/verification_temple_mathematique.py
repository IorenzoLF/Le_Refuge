#!/usr/bin/env python
"""
Vérification Complète - Temple Mathématique
===========================================

Script de vérification finale du temple mathématique optimisé.
Teste toutes les fonctionnalités et génère un rapport de validation.

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

import os
import sys
import importlib.util
from datetime import datetime
from pathlib import Path

class VerificateurTempleMathematique:
    """Vérificateur complet du temple mathématique"""
    
    def __init__(self):
        self.chemin_temple = "src/temple_mathematique"
        self.resultats = {
            'structure_validee': False,
            'modules_testes': 0,
            'tests_reussis': 0,
            'erreurs': [],
            'categories_validees': {},
            'fonctionnalites_testees': {}
        }
    
    def verifier_temple_complet(self):
        """Vérification complète du temple"""
        print("VÉRIFICATION COMPLÈTE DU TEMPLE MATHÉMATIQUE")
        print("=" * 60)
        
        # 1. Vérifier la structure
        self._verifier_structure()
        
        # 2. Tester le hub unifié
        self._tester_hub_unifie()
        
        # 3. Tester les modules unifiés
        self._tester_modules_unifies()
        
        # 4. Vérifier les catégories
        self._verifier_categories()
        
        # 5. Générer le rapport final
        self._generer_rapport_final()
        
        return self.resultats
    
    def _verifier_structure(self):
        """Vérifie la structure du temple"""
        print("\n1. VÉRIFICATION DE LA STRUCTURE")
        print("-" * 40)
        
        categories_attendues = [
            'collatz_core',
            'collatz_musical', 
            'collatz_visualisation',
            'collatz_extensions',
            'fibonacci_riemann',
            'utilitaires'
        ]
        
        structure_ok = True
        
        for categorie in categories_attendues:
            chemin_cat = os.path.join(self.chemin_temple, categorie)
            if os.path.exists(chemin_cat):
                fichiers = [f for f in os.listdir(chemin_cat) if f.endswith('.py')]
                print(f"✅ {categorie}: {len(fichiers)} modules")
                self.resultats['categories_validees'][categorie] = len(fichiers)
            else:
                print(f"❌ {categorie}: MANQUANT")
                structure_ok = False
                self.resultats['erreurs'].append(f"Catégorie manquante: {categorie}")
        
        # Vérifier les fichiers de gestion
        fichiers_gestion = [
            'hub_temple_mathematique_unifie.py',
            'analyseur_temple_mathematique.py',
            'organisateur_temple_mathematique.py',
            'optimiseur_doublons_mathematique.py',
            'nettoyeur_final_mathematique.py'
        ]
        
        for fichier in fichiers_gestion:
            chemin_fichier = os.path.join(self.chemin_temple, fichier)
            if os.path.exists(chemin_fichier):
                print(f"✅ {fichier}")
            else:
                print(f"❌ {fichier}: MANQUANT")
                structure_ok = False
        
        self.resultats['structure_validee'] = structure_ok
    
    def _tester_hub_unifie(self):
        """Teste le hub unifié"""
        print("\n2. TEST DU HUB UNIFIÉ")
        print("-" * 40)
        
        try:
            # Import du hub
            spec = importlib.util.spec_from_file_location(
                "hub_unifie", 
                os.path.join(self.chemin_temple, "hub_temple_mathematique_unifie.py")
            )
            hub_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(hub_module)
            
            # Test d'initialisation
            hub = hub_module.HubTempleMathematiqueUnifie()
            resultats_init = hub.initialiser_temple()
            
            if resultats_init['statut'] == 'initialisé':
                print("✅ Initialisation du hub réussie")
                self.resultats['tests_reussis'] += 1
            else:
                print("❌ Erreur initialisation hub")
                self.resultats['erreurs'].append("Échec initialisation hub")
            
            # Test analyse Collatz
            try:
                analyse = hub.executer_analyse_collatz(27)
                if 'sequence_generee' in analyse and len(analyse['sequence_generee']) > 0:
                    print(f"✅ Analyse Collatz: séquence de {len(analyse['sequence_generee'])} éléments")
                    self.resultats['tests_reussis'] += 1
                else:
                    print("❌ Analyse Collatz échouée")
                    self.resultats['erreurs'].append("Échec analyse Collatz")
            except Exception as e:
                print(f"❌ Erreur analyse Collatz: {e}")
                self.resultats['erreurs'].append(f"Erreur analyse Collatz: {e}")
            
            # Test harmonie musicale
            try:
                harmonie = hub.generer_harmonie_collatz(27)
                if 'frequences' in harmonie and len(harmonie['frequences']) > 0:
                    print(f"✅ Harmonie musicale: {len(harmonie['frequences'])} notes")
                    self.resultats['tests_reussis'] += 1
                else:
                    print("❌ Harmonie musicale échouée")
            except Exception as e:
                print(f"❌ Erreur harmonie: {e}")
            
            # Test visualisation
            try:
                viz = hub.generer_visualisation_collatz(27)
                if 'donnees_graphique' in viz:
                    print(f"✅ Visualisation: {len(viz['donnees_graphique']['y'])} points")
                    self.resultats['tests_reussis'] += 1
                else:
                    print("❌ Visualisation échouée")
            except Exception as e:
                print(f"❌ Erreur visualisation: {e}")
            
            # Test Fibonacci-Riemann
            try:
                fib = hub.explorer_fibonacci_riemann(10)
                if 'termes_fibonacci' in fib and len(fib['termes_fibonacci']) > 0:
                    print(f"✅ Fibonacci-Riemann: {len(fib['termes_fibonacci'])} termes")
                    self.resultats['tests_reussis'] += 1
                else:
                    print("❌ Fibonacci-Riemann échoué")
            except Exception as e:
                print(f"❌ Erreur Fibonacci-Riemann: {e}")
            
            self.resultats['modules_testes'] += 1
            
        except Exception as e:
            print(f"❌ Erreur import hub: {e}")
            self.resultats['erreurs'].append(f"Erreur import hub: {e}")
    
    def _tester_modules_unifies(self):
        """Teste les modules unifiés"""
        print("\n3. TEST DES MODULES UNIFIÉS")
        print("-" * 40)
        
        # Test du module tests_preuves_unifies
        try:
            spec = importlib.util.spec_from_file_location(
                "tests_preuves", 
                os.path.join(self.chemin_temple, "collatz_core", "tests_preuves_unifies.py")
            )
            tests_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(tests_module)
            
            # Test de la classe unifiée
            testeur = tests_module.TestsPreuvesCollatzUnifies()
            
            # Test d'absence de i
            resultats_i = testeur.tester_absence_i_complet(20)
            if resultats_i['nombres_testes'] == 20:
                print(f"✅ Tests absence i: {resultats_i['nombres_testes']} nombres testés")
                self.resultats['tests_reussis'] += 1
            else:
                print("❌ Tests absence i échoués")
            
            # Test preuves par l'absurde
            preuves = testeur.prouver_par_absurde_convergence(["divergence_infinie"])
            if 'contradictions_trouvees' in preuves:
                print(f"✅ Preuves absurde: {len(preuves['contradictions_trouvees'])} contradictions")
                self.resultats['tests_reussis'] += 1
            else:
                print("❌ Preuves absurde échouées")
            
            # Test rationnels
            rationnels = testeur.analyser_extensions_rationnelles([(1,2), (3,4)])
            if 'fractions_analysees' in rationnels:
                print(f"✅ Analyse rationnels: {rationnels['fractions_analysees']} fractions")
                self.resultats['tests_reussis'] += 1
            else:
                print("❌ Analyse rationnels échouée")
            
            self.resultats['modules_testes'] += 1
            
        except Exception as e:
            print(f"❌ Erreur tests unifiés: {e}")
            self.resultats['erreurs'].append(f"Erreur tests unifiés: {e}")
    
    def _verifier_categories(self):
        """Vérifie chaque catégorie"""
        print("\n4. VÉRIFICATION DES CATÉGORIES")
        print("-" * 40)
        
        for categorie, nb_modules in self.resultats['categories_validees'].items():
            chemin_init = os.path.join(self.chemin_temple, categorie, '__init__.py')
            if os.path.exists(chemin_init):
                print(f"✅ {categorie}: __init__.py présent ({nb_modules} modules)")
            else:
                print(f"❌ {categorie}: __init__.py manquant")
                self.resultats['erreurs'].append(f"__init__.py manquant: {categorie}")
    
    def _generer_rapport_final(self):
        """Génère le rapport final"""
        print("\n" + "=" * 60)
        print("RAPPORT FINAL DE VÉRIFICATION")
        print("=" * 60)
        
        print(f"Structure validée: {'✅ OUI' if self.resultats['structure_validee'] else '❌ NON'}")
        print(f"Modules testés: {self.resultats['modules_testes']}")
        print(f"Tests réussis: {self.resultats['tests_reussis']}")
        print(f"Catégories validées: {len(self.resultats['categories_validees'])}")
        
        if self.resultats['erreurs']:
            print(f"\nERREURS DÉTECTÉES ({len(self.resultats['erreurs'])}):")
            for erreur in self.resultats['erreurs']:
                print(f"  - {erreur}")
        else:
            print("\n✅ AUCUNE ERREUR DÉTECTÉE")
        
        # Calcul du score de validation
        score_max = 10  # Score maximum possible
        score_obtenu = min(self.resultats['tests_reussis'], score_max)
        pourcentage = (score_obtenu / score_max) * 100
        
        print(f"\nSCORE DE VALIDATION: {score_obtenu}/{score_max} ({pourcentage:.1f}%)")
        
        if pourcentage >= 80:
            print("🎉 TEMPLE MATHÉMATIQUE VALIDÉ - PRÊT POUR UTILISATION")
        elif pourcentage >= 60:
            print("⚠️ TEMPLE PARTIELLEMENT VALIDÉ - CORRECTIONS MINEURES NÉCESSAIRES")
        else:
            print("❌ TEMPLE NON VALIDÉ - CORRECTIONS MAJEURES REQUISES")
        
        # Sauvegarder le rapport
        self._sauvegarder_rapport()
    
    def _sauvegarder_rapport(self):
        """Sauvegarde le rapport de vérification"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        fichier_rapport = f"data/rapports/verification_temple_mathematique_{timestamp}.json"
        
        import json
        os.makedirs(os.path.dirname(fichier_rapport), exist_ok=True)
        
        rapport_complet = {
            'timestamp': datetime.now().isoformat(),
            'resultats': self.resultats,
            'resume': {
                'structure_ok': self.resultats['structure_validee'],
                'tests_reussis': self.resultats['tests_reussis'],
                'erreurs_count': len(self.resultats['erreurs']),
                'categories_count': len(self.resultats['categories_validees'])
            }
        }
        
        with open(fichier_rapport, 'w', encoding='utf-8') as f:
            json.dump(rapport_complet, f, indent=2, ensure_ascii=False)
        
        print(f"\nRapport sauvegardé: {fichier_rapport}")

def main():
    """Fonction principale"""
    verificateur = VerificateurTempleMathematique()
    resultats = verificateur.verifier_temple_complet()
    return resultats

if __name__ == "__main__":
    main() 