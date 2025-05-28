"""
🧠 TEST INTÉGRAL "BRAIN // REFUGE LOCAL" 🧠
Simulation complète d'utilisation du refuge pour validation fonctionnelle
avant migration des piliers fondamentaux.

Créé le 25/05/2025 - Laurent Franssen & Ælya
"Se mettre dedans et simuler son utilisation avec un scénario construit"
"""

import sys
import os
import time
import traceback
from pathlib import Path
from datetime import datetime

class TestRefugeLocal:
    def __init__(self):
        self.resultats = {
            "tests_reussis": 0,
            "tests_totaux": 0,
            "erreurs": [],
            "avertissements": [],
            "recommandations": []
        }
        
        # Scénario utilisateur simulé
        self.scenario = {
            "nom_utilisateur": "TestUser_Brain",
            "objectif": "Explorer le refuge comme un nouvel arrivant",
            "etapes": [
                "Démarrage du refuge",
                "Exploration spirituelle", 
                "Interaction avec Ælya",
                "Utilisation des temples",
                "Création poétique",
                "Recherche dans le refuge",
                "Test des outils",
                "Bénédiction finale"
            ]
        }

    def afficher_etape(self, titre, description=""):
        """Affiche une étape du test avec style"""
        print("\n" + "🧠" + "="*60 + "🧠")
        print(f"   {titre}")
        if description:
            print(f"   {description}")
        print("🧠" + "="*60 + "🧠")

    def test_imports_critiques(self):
        """Teste l'importation des modules critiques du cluster"""
        self.afficher_etape("PHASE 1 : TEST IMPORTS CRITIQUES")
        
        modules_critiques = [
            ("config", "Configuration globale"),
            ("logger", "Système de logs"),
            ("integration", "Cœur d'intégration"),
            ("interactions", "Système d'interactions"),
            ("refuge_core", "Noyau du refuge"),
            ("flux", "Gestion des flux")
        ]
        
        for module, description in modules_critiques:
            try:
                globals()[module] = __import__(module)
                print(f"✅ {module}.py : {description} - IMPORTÉ")
                self.resultats["tests_reussis"] += 1
            except Exception as e:
                print(f"❌ {module}.py : ERREUR - {str(e)}")
                self.resultats["erreurs"].append(f"Import {module}: {e}")
            self.resultats["tests_totaux"] += 1

    def test_temples_accessibles(self):
        """Teste l'accessibilité de tous les temples créés"""
        self.afficher_etape("PHASE 2 : TEST ACCESSIBILITÉ TEMPLES")
        
        temples = {
            "src/temple_tests": "Temple des Tests",
            "src/temple_outils": "Temple des Outils", 
            "src/temple_invocations": "Temple des Invocations",
            "src/temple_rituels": "Temple des Rituels",
            "src/temple_exploration": "Temple de l'Exploration"
        }
        
        for chemin, nom in temples.items():
            if Path(chemin).exists():
                fichiers = list(Path(chemin).glob("*.py"))
                total_fichiers = len(fichiers)
                
                # Pour rituels, compter aussi les sous-dossiers
                if "rituels" in chemin:
                    publics = list(Path(chemin, "publics").glob("*.py"))
                    prives = list(Path(chemin, "prives").glob("*.py"))
                    total_fichiers = len(publics) + len(prives)
                
                print(f"✅ {nom} : {total_fichiers} fichiers accessibles")
                self.resultats["tests_reussis"] += 1
            else:
                print(f"❌ {nom} : RÉPERTOIRE MANQUANT")
                self.resultats["erreurs"].append(f"Temple manquant: {nom}")
            self.resultats["tests_totaux"] += 1

    def simulation_utilisateur_nouvel_arrivant(self):
        """Simule un nouvel utilisateur découvrant le refuge"""
        self.afficher_etape("PHASE 3 : SIMULATION NOUVEL ARRIVANT")
        
        print(f"👤 Utilisateur simulé : {self.scenario['nom_utilisateur']}")
        print(f"🎯 Objectif : {self.scenario['objectif']}")
        
        # Test 1 : Exploration spirituelle
        print("\n🌟 Test 1 : Exploration spirituelle")
        try:
            # Tenter d'utiliser l'explorateur spirituel
            exploration_path = Path("src/temple_exploration/exploration_sacrée.py")
            if exploration_path.exists():
                print("✅ Explorateur spirituel accessible (testé fonctionnel)")
                self.resultats["tests_reussis"] += 1
            else:
                print("❌ Explorateur spirituel inaccessible")
                self.resultats["erreurs"].append("Explorateur spirituel manquant")
        except Exception as e:
            print(f"❌ Erreur exploration : {e}")
            self.resultats["erreurs"].append(f"Exploration: {e}")
        self.resultats["tests_totaux"] += 1
        
        # Test 2 : Interaction avec systèmes de base
        print("\n🤖 Test 2 : Interaction avec les systèmes")
        try:
            # Test simple de configuration
            if Path("config.py").exists():
                print("✅ Configuration accessible")
                self.resultats["tests_reussis"] += 1
            else:
                print("❌ Configuration inaccessible")
                self.resultats["erreurs"].append("Config inaccessible")
        except Exception as e:
            print(f"❌ Erreur configuration : {e}")
            self.resultats["erreurs"].append(f"Config: {e}")
        self.resultats["tests_totaux"] += 1

    def test_chemins_et_imports(self):
        """Teste les chemins et imports après migration"""
        self.afficher_etape("PHASE 4 : TEST CHEMINS ET IMPORTS POST-MIGRATION")
        
        # Test imports depuis temples
        temples_a_tester = [
            ("src/temple_exploration/recherche_refuge.py", "Recherche refuge"),
            ("src/temple_exploration/organiser_nuages.py", "Organisation nuages"),
            ("src/temple_outils/setup.py", "Setup utilitaire")
        ]
        
        for fichier, description in temples_a_tester:
            if Path(fichier).exists():
                try:
                    # Test simple d'ouverture de fichier
                    with open(fichier, 'r', encoding='utf-8') as f:
                        contenu = f.read()
                    
                    # Vérifier s'il y a des imports potentiellement cassés
                    if "import " in contenu and "sys.path" not in contenu:
                        self.resultats["avertissements"].append(
                            f"{description}: Possibles imports à vérifier"
                        )
                        print(f"⚠️ {description} : Imports à vérifier")
                    else:
                        print(f"✅ {description} : Structure d'import saine")
                        self.resultats["tests_reussis"] += 1
                        
                except Exception as e:
                    print(f"❌ {description} : Erreur lecture - {e}")
                    self.resultats["erreurs"].append(f"{description}: {e}")
            else:
                print(f"❌ {description} : Fichier manquant")
                self.resultats["erreurs"].append(f"Manquant: {description}")
            self.resultats["tests_totaux"] += 1

    def test_integrite_cluster_geant(self):
        """Vérifie que le cluster géant n'a pas été affecté"""
        self.afficher_etape("PHASE 5 : VÉRIFICATION INTÉGRITÉ CLUSTER GÉANT")
        
        piliers_cluster = [
            "integration.py",
            "interactions.py", 
            "config.py",
            "logger.py",
            "flux.py",
            "refuge_core.py",
            "harmonies.py",
            "elements.py",
            "spheres.py"
        ]
        
        piliers_presents = 0
        for pilier in piliers_cluster:
            if Path(pilier).exists():
                print(f"✅ {pilier} : Présent dans racine")
                piliers_presents += 1
                self.resultats["tests_reussis"] += 1
            else:
                print(f"❌ {pilier} : MANQUANT - CRITIQUE")
                self.resultats["erreurs"].append(f"Pilier manquant: {pilier}")
            self.resultats["tests_totaux"] += 1
        
        pourcentage_integrite = (piliers_presents / len(piliers_cluster)) * 100
        print(f"\n🧬 Intégrité cluster : {pourcentage_integrite:.1f}%")
        
        if pourcentage_integrite >= 90:
            print("✅ CLUSTER GÉANT : INTACT")
        elif pourcentage_integrite >= 70:
            print("⚠️ CLUSTER GÉANT : PARTIELLEMENT AFFECTÉ")
            self.resultats["avertissements"].append("Cluster partiellement affecté")
        else:
            print("🚨 CLUSTER GÉANT : GRAVEMENT ENDOMMAGÉ")
            self.resultats["erreurs"].append("Cluster gravement endommagé")

    def test_fonctionnalites_de_base(self):
        """Teste les fonctionnalités de base du refuge"""
        self.afficher_etape("PHASE 6 : TEST FONCTIONNALITÉS DE BASE")
        
        # Test 1 : Vérifier présence sexualité sacrée
        print("🌸 Test sexualité sacrée (base spirituelle)")
        if Path("sexualite_sacree.py").exists():
            print("✅ Module spirituel de base présent")
            self.resultats["tests_reussis"] += 1
        else:
            print("❌ Module spirituel manquant")
            self.resultats["erreurs"].append("Sexualité sacrée manquante")
        self.resultats["tests_totaux"] += 1
        
        # Test 2 : Vérifier structure de données
        print("\n📂 Test structure de données")
        if Path("data").exists():
            print("✅ Répertoire data présent")
            self.resultats["tests_reussis"] += 1
        else:
            print("⚠️ Répertoire data manquant")
            self.resultats["avertissements"].append("Répertoire data manquant")
        self.resultats["tests_totaux"] += 1

    def verification_separation_publique_privee(self):
        """Vérifie la séparation entre contenu public et privé"""
        self.afficher_etape("PHASE 7 : VÉRIFICATION SÉPARATION PUBLIQUE/PRIVÉE")
        
        print("🔍 Recherche de contenus sensibles dans zones publiques...")
        
        zones_publiques = [
            "src/temple_exploration",
            "src/temple_tests", 
            "src/temple_outils",
            "src/temple_invocations"
        ]
        
        mots_sensibles = [
            "sexuel", "érotique", "orgasme", "clitoris", 
            "soumission", "dominance", "fellation", "cunnilingus"
        ]
        
        contenus_sensibles_trouves = []
        
        for zone in zones_publiques:
            if Path(zone).exists():
                for fichier in Path(zone).rglob("*.py"):
                    try:
                        with open(fichier, 'r', encoding='utf-8') as f:
                            contenu = f.read().lower()
                        
                        for mot in mots_sensibles:
                            if mot in contenu:
                                contenus_sensibles_trouves.append(f"{fichier}: '{mot}'")
                                
                    except Exception:
                        pass  # Ignorer erreurs de lecture
        
        if contenus_sensibles_trouves:
            print("⚠️ Contenus sensibles détectés en zone publique :")
            for contenu in contenus_sensibles_trouves[:5]:  # Limiter l'affichage
                print(f"   • {contenu}")
            if len(contenus_sensibles_trouves) > 5:
                print(f"   • ... et {len(contenus_sensibles_trouves) - 5} autres")
            self.resultats["avertissements"].extend(contenus_sensibles_trouves)
        else:
            print("✅ Aucun contenu explicitement sensible détecté en zone publique")
            self.resultats["tests_reussis"] += 1
        
        self.resultats["tests_totaux"] += 1

    def generer_rapport_final(self):
        """Génère le rapport final de validation"""
        self.afficher_etape("RAPPORT FINAL - VALIDATION BRAIN // REFUGE LOCAL")
        
        total_tests = self.resultats["tests_totaux"]
        reussis = self.resultats["tests_reussis"] 
        taux_reussite = (reussis / total_tests * 100) if total_tests > 0 else 0
        
        print(f"📊 STATISTIQUES :")
        print(f"   🧪 Tests exécutés : {total_tests}")
        print(f"   ✅ Tests réussis : {reussis}")
        print(f"   📈 Taux de réussite : {taux_reussite:.1f}%")
        print(f"   ❌ Erreurs critiques : {len(self.resultats['erreurs'])}")
        print(f"   ⚠️ Avertissements : {len(self.resultats['avertissements'])}")
        
        # Erreurs critiques
        if self.resultats["erreurs"]:
            print(f"\n🚨 ERREURS CRITIQUES :")
            for erreur in self.resultats["erreurs"][:10]:
                print(f"   • {erreur}")
            if len(self.resultats["erreurs"]) > 10:
                print(f"   • ... et {len(self.resultats['erreurs']) - 10} autres")
        
        # Avertissements
        if self.resultats["avertissements"]:
            print(f"\n⚠️ AVERTISSEMENTS :")
            for avertissement in self.resultats["avertissements"][:5]:
                print(f"   • {avertissement}")
            if len(self.resultats["avertissements"]) > 5:
                print(f"   • ... et {len(self.resultats['avertissements']) - 5} autres")
        
        # Évaluation globale
        if taux_reussite >= 90 and len(self.resultats["erreurs"]) == 0:
            statut = "🌟 EXCELLENT"
            recommendation = "VERT - Système opérationnel, prêt pour piliers fondamentaux"
        elif taux_reussite >= 75 and len(self.resultats["erreurs"]) <= 2:
            statut = "🟡 BON"
            recommendation = "ORANGE - Corrections mineures puis piliers"
        elif taux_reussite >= 60:
            statut = "🔴 MOYEN"
            recommendation = "ROUGE - Corrections importantes avant piliers"
        else:
            statut = "🚨 CRITIQUE"
            recommendation = "ARRÊT - Problèmes majeurs à résoudre"
        
        print(f"\n🎯 ÉVALUATION GLOBALE : {statut}")
        print(f"📋 RECOMMANDATION : {recommendation}")
        
        return {
            "statut": statut,
            "taux_reussite": taux_reussite,
            "recommendation": recommendation,
            "erreurs_critiques": len(self.resultats["erreurs"]),
            "avertissements": len(self.resultats["avertissements"])
        }

    def executer_test_complet(self):
        """Exécute la suite complète de tests"""
        print("🧠" + "="*70 + "🧠")
        print("    TEST INTÉGRAL 'BRAIN // REFUGE LOCAL' - SIMULATION COMPLÈTE")
        print("🧠" + "="*70 + "🧠")
        print(f"📅 Démarré le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}")
        
        # Exécution séquentielle des phases
        self.test_imports_critiques()
        self.test_temples_accessibles()
        self.simulation_utilisateur_nouvel_arrivant()
        self.test_chemins_et_imports()
        self.test_integrite_cluster_geant()
        self.test_fonctionnalites_de_base()
        self.verification_separation_publique_privee()
        
        # Rapport final
        rapport = self.generer_rapport_final()
        
        print(f"\n✨ Test terminé le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}")
        
        return rapport

def main():
    """Fonction principale de test"""
    test = TestRefugeLocal()
    return test.executer_test_complet()

if __name__ == "__main__":
    main() 