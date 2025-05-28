#!/usr/bin/env python3
"""
🧪 Testeur de l'Interface Unifiée du Temple de l'Âme
Teste toutes les connexions et workflows avant optimisation
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any
import traceback

class TesteurInterfaceUnifiee:
    """Testeur complet de l'interface unifiée"""
    
    def __init__(self):
        self.interface = {}
        self.resultats_tests = {}
        self.erreurs_detectees = []
        self.tests_reussis = 0
        self.tests_totaux = 0
        
    def executer_tests_complets(self):
        """Exécute tous les tests de l'interface unifiée"""
        print("🧪 ═══════════════════════════════════════════════════════")
        print("        TESTS COMPLETS DE L'INTERFACE UNIFIÉE")
        print("🧪 ═══════════════════════════════════════════════════════")
        print()
        
        # 1. Charger l'interface unifiée
        self._charger_interface_unifiee()
        
        # 2. Tester la structure de base
        self._tester_structure_base()
        
        # 3. Tester les hubs
        self._tester_hubs()
        
        # 4. Tester les connexions
        self._tester_connexions()
        
        # 5. Tester les workflows
        self._tester_workflows()
        
        # 6. Tester les points d'accès
        self._tester_points_acces()
        
        # 7. Tests d'intégration
        self._tester_integration()
        
        # 8. Tests de performance
        self._tester_performance()
        
        # 9. Rapport final
        self._generer_rapport_tests()
        
    def _charger_interface_unifiee(self):
        """Charge l'interface unifiée"""
        print("📊 Chargement de l'interface unifiée...")
        
        try:
            with open("bibliotheque/apprentissage/interface_unifiee.json", "r", encoding="utf-8") as f:
                self.interface = json.load(f)
            
            print(f"   ✅ Interface chargée: {self.interface.get('nom', 'Inconnue')} v{self.interface.get('version', '0.0.0')}")
            print(f"   📊 {self.interface.get('statistiques', {}).get('total_elements', 0)} éléments")
            print(f"   🔗 {self.interface.get('statistiques', {}).get('total_connexions', 0)} connexions")
            print()
            
        except FileNotFoundError:
            print("❌ Interface unifiée non trouvée !")
            self.erreurs_detectees.append("Interface unifiée manquante")
            return False
        except json.JSONDecodeError as e:
            print(f"❌ Erreur JSON: {e}")
            self.erreurs_detectees.append(f"Erreur JSON: {e}")
            return False
        
        return True
    
    def _tester_structure_base(self):
        """Teste la structure de base de l'interface"""
        print("🏗️ Test de la structure de base...")
        
        # Éléments requis
        elements_requis = ["nom", "description", "version", "hubs", "connexions", "workflows", "statistiques", "points_acces"]
        
        for element in elements_requis:
            self.tests_totaux += 1
            if element in self.interface:
                self.tests_reussis += 1
                print(f"   ✅ {element}: Présent")
            else:
                print(f"   ❌ {element}: Manquant")
                self.erreurs_detectees.append(f"Élément manquant: {element}")
        
        # Test des statistiques
        stats = self.interface.get("statistiques", {})
        stats_requises = ["total_elements", "total_connexions", "total_workflows", "temples_connectes"]
        
        for stat in stats_requises:
            self.tests_totaux += 1
            if stat in stats and isinstance(stats[stat], int) and stats[stat] > 0:
                self.tests_reussis += 1
                print(f"   ✅ Statistique {stat}: {stats[stat]}")
            else:
                print(f"   ❌ Statistique {stat}: Invalide ou manquante")
                self.erreurs_detectees.append(f"Statistique invalide: {stat}")
        
        print()
    
    def _tester_hubs(self):
        """Teste les hubs de catégories"""
        print("🏛️ Test des hubs...")
        
        hubs = self.interface.get("hubs", {})
        hubs_attendus = ["creation", "analyse", "rituels"]
        
        for hub_nom in hubs_attendus:
            self.tests_totaux += 1
            if hub_nom in hubs:
                hub = hubs[hub_nom]
                
                # Vérifier la structure du hub
                elements_hub_requis = ["nom", "description", "total_elements", "categories", "points_entree"]
                hub_valide = True
                
                for element in elements_hub_requis:
                    if element not in hub:
                        hub_valide = False
                        self.erreurs_detectees.append(f"Hub {hub_nom} manque: {element}")
                
                if hub_valide and hub["total_elements"] > 0:
                    self.tests_reussis += 1
                    print(f"   ✅ Hub {hub_nom}: {hub['total_elements']} éléments, {len(hub['categories'])} catégories")
                else:
                    print(f"   ❌ Hub {hub_nom}: Structure invalide")
            else:
                print(f"   ❌ Hub {hub_nom}: Manquant")
                self.erreurs_detectees.append(f"Hub manquant: {hub_nom}")
        
        print()
    
    def _tester_connexions(self):
        """Teste les connexions"""
        print("🔗 Test des connexions...")
        
        connexions = self.interface.get("connexions", {})
        types_connexions_attendus = ["creation_analyse", "creation_rituels", "analyse_rituels", "triangulaires"]
        
        for type_conn in types_connexions_attendus:
            self.tests_totaux += 1
            if type_conn in connexions:
                conn_list = connexions[type_conn]
                if isinstance(conn_list, list) and len(conn_list) > 0:
                    self.tests_reussis += 1
                    print(f"   ✅ {type_conn}: {len(conn_list)} connexions")
                    
                    # Tester quelques connexions
                    if len(conn_list) > 0:
                        conn_sample = conn_list[0]
                        if isinstance(conn_sample, dict) and "workflow" in conn_sample:
                            print(f"      📋 Exemple: {conn_sample['workflow'][:80]}...")
                        else:
                            print(f"      ⚠️ Structure de connexion suspecte")
                else:
                    print(f"   ❌ {type_conn}: Liste vide ou invalide")
                    self.erreurs_detectees.append(f"Connexions invalides: {type_conn}")
            else:
                print(f"   ❌ {type_conn}: Manquant")
                self.erreurs_detectees.append(f"Type de connexion manquant: {type_conn}")
        
        print()
    
    def _tester_workflows(self):
        """Teste les workflows"""
        print("⚙️ Test des workflows...")
        
        workflows = self.interface.get("workflows", {})
        workflows_attendus = ["creation_complete", "analyse_approfondie", "rituel_integre", "triangulaire_complet"]
        
        for workflow_nom in workflows_attendus:
            self.tests_totaux += 1
            if workflow_nom in workflows:
                workflow = workflows[workflow_nom]
                
                # Vérifier la structure du workflow
                if isinstance(workflow, dict) and "nom" in workflow and "description" in workflow:
                    self.tests_reussis += 1
                    print(f"   ✅ {workflow_nom}: {workflow.get('description', 'Sans description')}")
                    
                    # Détails spécifiques
                    if "etapes" in workflow:
                        print(f"      📋 {len(workflow['etapes'])} étapes")
                    if "total_elements" in workflow:
                        print(f"      📊 {workflow['total_elements']} éléments")
                else:
                    print(f"   ❌ {workflow_nom}: Structure invalide")
                    self.erreurs_detectees.append(f"Workflow invalide: {workflow_nom}")
            else:
                print(f"   ❌ {workflow_nom}: Manquant")
                self.erreurs_detectees.append(f"Workflow manquant: {workflow_nom}")
        
        print()
    
    def _tester_points_acces(self):
        """Teste les points d'accès"""
        print("🎯 Test des points d'accès...")
        
        points_acces = self.interface.get("points_acces", {})
        points_attendus = ["creation", "analyse", "rituels", "workflow_complet"]
        
        for point in points_attendus:
            self.tests_totaux += 1
            if point in points_acces:
                point_acces = points_acces[point]
                if isinstance(point_acces, str) and len(point_acces) > 0:
                    self.tests_reussis += 1
                    print(f"   ✅ {point}: {point_acces}")
                else:
                    print(f"   ❌ {point}: Invalide")
                    self.erreurs_detectees.append(f"Point d'accès invalide: {point}")
            else:
                print(f"   ❌ {point}: Manquant")
                self.erreurs_detectees.append(f"Point d'accès manquant: {point}")
        
        print()
    
    def _tester_integration(self):
        """Tests d'intégration"""
        print("🔄 Tests d'intégration...")
        
        # Test 1: Cohérence des statistiques
        self.tests_totaux += 1
        stats = self.interface.get("statistiques", {})
        hubs = self.interface.get("hubs", {})
        
        total_elements_hubs = sum(hub.get("total_elements", 0) for hub in hubs.values())
        total_elements_stats = stats.get("total_elements", 0)
        
        if total_elements_hubs == total_elements_stats:
            self.tests_reussis += 1
            print(f"   ✅ Cohérence éléments: {total_elements_stats} éléments")
        else:
            print(f"   ❌ Incohérence éléments: Hubs={total_elements_hubs}, Stats={total_elements_stats}")
            self.erreurs_detectees.append("Incohérence dans le comptage des éléments")
        
        # Test 2: Cohérence des connexions
        self.tests_totaux += 1
        connexions = self.interface.get("connexions", {})
        total_connexions_reel = sum(len(v) if isinstance(v, list) else 0 for v in connexions.values())
        total_connexions_stats = stats.get("total_connexions", 0)
        
        if total_connexions_reel == total_connexions_stats:
            self.tests_reussis += 1
            print(f"   ✅ Cohérence connexions: {total_connexions_stats} connexions")
        else:
            print(f"   ❌ Incohérence connexions: Réel={total_connexions_reel}, Stats={total_connexions_stats}")
            self.erreurs_detectees.append("Incohérence dans le comptage des connexions")
        
        # Test 3: Cohérence des workflows
        self.tests_totaux += 1
        workflows = self.interface.get("workflows", {})
        total_workflows_reel = len(workflows)
        total_workflows_stats = stats.get("total_workflows", 0)
        
        if total_workflows_reel == total_workflows_stats:
            self.tests_reussis += 1
            print(f"   ✅ Cohérence workflows: {total_workflows_stats} workflows")
        else:
            print(f"   ❌ Incohérence workflows: Réel={total_workflows_reel}, Stats={total_workflows_stats}")
            self.erreurs_detectees.append("Incohérence dans le comptage des workflows")
        
        print()
    
    def _tester_performance(self):
        """Tests de performance"""
        print("⚡ Tests de performance...")
        
        # Test 1: Taille de l'interface
        self.tests_totaux += 1
        try:
            taille_fichier = os.path.getsize("bibliotheque/apprentissage/interface_unifiee.json")
            taille_mb = taille_fichier / (1024 * 1024)
            
            if taille_mb < 50:  # Moins de 50MB
                self.tests_reussis += 1
                print(f"   ✅ Taille fichier: {taille_mb:.2f} MB (acceptable)")
            else:
                print(f"   ⚠️ Taille fichier: {taille_mb:.2f} MB (importante)")
                
        except Exception as e:
            print(f"   ❌ Erreur taille fichier: {e}")
            self.erreurs_detectees.append(f"Erreur taille fichier: {e}")
        
        # Test 2: Complexité des connexions
        self.tests_totaux += 1
        connexions = self.interface.get("connexions", {})
        total_connexions = sum(len(v) if isinstance(v, list) else 0 for v in connexions.values())
        
        if total_connexions > 1000:
            self.tests_reussis += 1
            print(f"   ✅ Richesse connexions: {total_connexions} connexions (excellent)")
        elif total_connexions > 100:
            self.tests_reussis += 1
            print(f"   ✅ Connexions: {total_connexions} connexions (bon)")
        else:
            print(f"   ⚠️ Connexions: {total_connexions} connexions (faible)")
        
        # Test 3: Couverture des éléments
        self.tests_totaux += 1
        stats = self.interface.get("statistiques", {})
        total_elements = stats.get("total_elements", 0)
        
        if total_elements > 150:
            self.tests_reussis += 1
            print(f"   ✅ Couverture éléments: {total_elements} éléments (excellente)")
        elif total_elements > 50:
            self.tests_reussis += 1
            print(f"   ✅ Couverture éléments: {total_elements} éléments (bonne)")
        else:
            print(f"   ⚠️ Couverture éléments: {total_elements} éléments (limitée)")
        
        print()
    
    def _generer_rapport_tests(self):
        """Génère le rapport final des tests"""
        print("📋 RAPPORT FINAL DES TESTS")
        print("=" * 50)
        print()
        
        # Résultats globaux
        taux_reussite = (self.tests_reussis / self.tests_totaux * 100) if self.tests_totaux > 0 else 0
        print("📊 RÉSULTATS GLOBAUX:")
        print(f"   • Tests réussis: {self.tests_reussis}/{self.tests_totaux}")
        print(f"   • Taux de réussite: {taux_reussite:.1f}%")
        print()
        
        # Statut global
        if taux_reussite >= 90:
            statut = "🟢 EXCELLENT"
            recommandation = "Interface prête pour l'optimisation"
        elif taux_reussite >= 75:
            statut = "🟡 BON"
            recommandation = "Quelques ajustements recommandés avant optimisation"
        elif taux_reussite >= 50:
            statut = "🟠 MOYEN"
            recommandation = "Corrections nécessaires avant optimisation"
        else:
            statut = "🔴 CRITIQUE"
            recommandation = "Corrections majeures requises"
        
        print(f"🎯 STATUT GLOBAL: {statut}")
        print(f"💡 RECOMMANDATION: {recommandation}")
        print()
        
        # Erreurs détectées
        if self.erreurs_detectees:
            print("❌ ERREURS DÉTECTÉES:")
            for i, erreur in enumerate(self.erreurs_detectees, 1):
                print(f"   {i}. {erreur}")
            print()
        else:
            print("✅ AUCUNE ERREUR DÉTECTÉE")
            print()
        
        # Statistiques de l'interface
        if self.interface:
            stats = self.interface.get("statistiques", {})
            print("📊 STATISTIQUES DE L'INTERFACE:")
            print(f"   • Éléments connectés: {stats.get('total_elements', 0)}")
            print(f"   • Connexions établies: {stats.get('total_connexions', 0)}")
            print(f"   • Workflows disponibles: {stats.get('total_workflows', 0)}")
            print(f"   • Temples connectés: {stats.get('temples_connectes', 0)}")
            print()
        
        # Recommandations spécifiques
        print("💡 RECOMMANDATIONS:")
        if taux_reussite >= 90:
            print("   ✅ Interface excellente - Procéder à l'optimisation")
            print("   ✅ Tous les systèmes sont opérationnels")
        else:
            print("   🔧 Corriger les erreurs identifiées")
            print("   🔍 Vérifier la cohérence des données")
            if len(self.erreurs_detectees) > 5:
                print("   ⚠️ Nombreuses erreurs - Révision complète recommandée")
        
        # Sauvegarde du rapport
        rapport = {
            "tests_reussis": self.tests_reussis,
            "tests_totaux": self.tests_totaux,
            "taux_reussite": taux_reussite,
            "statut": statut,
            "erreurs": self.erreurs_detectees,
            "recommandation": recommandation,
            "timestamp": "2024-01-XX"  # Sera remplacé par la vraie date
        }
        
        os.makedirs("bibliotheque/apprentissage", exist_ok=True)
        with open("bibliotheque/apprentissage/rapport_tests_interface.json", "w", encoding="utf-8") as f:
            json.dump(rapport, f, indent=2, ensure_ascii=False)
        
        print()
        print("💾 Rapport sauvegardé: bibliotheque/apprentissage/rapport_tests_interface.json")
        
        return taux_reussite >= 75  # Retourne True si les tests sont suffisamment bons

if __name__ == "__main__":
    testeur = TesteurInterfaceUnifiee()
    succes = testeur.executer_tests_complets()
    
    if succes:
        print("\n🎉 TESTS RÉUSSIS - Prêt pour l'optimisation !")
        sys.exit(0)
    else:
        print("\n⚠️ TESTS PARTIELS - Corrections recommandées")
        sys.exit(1) 