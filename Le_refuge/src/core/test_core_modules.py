#!/usr/bin/env python3
"""
Script de Test Complet pour le Dossier src/core

Ce script teste tous les modules du dossier core et génère un rapport
de santé détaillé pour identifier les modules fonctionnels et ceux
nécessitant des corrections.

Auteur: Assistant IA
Date: 2024
Projet: Le Refuge Poétique
"""

import os
import sys
import importlib
import traceback
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Any
import json

# Ajout du chemin src au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

class TesteurModulesCore:
    """
    Testeur complet pour tous les modules du dossier src/core.
    
    Cette classe effectue des tests systématiques sur tous les modules
    Python du dossier core et génère des rapports détaillés.
    """
    
    def __init__(self):
        """Initialise le testeur avec les chemins et structures nécessaires."""
        self.chemin_core = Path(__file__).parent
        self.resultats = {
            "modules_fonctionnels": [],
            "modules_avec_erreurs": [],
            "modules_degrades": [],
            "dependances_manquantes": set(),
            "classes_testees": {},
            "resume_global": {},
            "timestamp": datetime.now().isoformat()
        }
        
        # Modules prioritaires à tester en premier
        self.modules_prioritaires = [
            "configuration",
            "types_spheres", 
            "conscience",
            "harmonie",
            "elements",
            "logger",
            "harmonies_poetiques"
        ]
        
        # Modules avec corrections récentes
        self.modules_corriges = [
            "orchestre_poetique",
            "refuge",
            "presence"
        ]
        
        print("🌸 " + "=" * 60 + " 🌸")
        print("    🔍 TESTEUR COMPLET DES MODULES CORE 🔍")
        print("🌸 " + "=" * 60 + " 🌸")
        print()
        
    def lister_modules_python(self) -> List[str]:
        """Liste tous les fichiers Python du dossier core."""
        modules = []
        
        for fichier in self.chemin_core.rglob("*.py"):
            if fichier.name != "__init__.py" and not fichier.name.startswith("test_"):
                # Conversion en nom de module relatif
                chemin_relatif = fichier.relative_to(self.chemin_core)
                nom_module = str(chemin_relatif).replace("/", ".").replace("\\", ".").replace(".py", "")
                modules.append(nom_module)
                
        return sorted(modules)
        
    def tester_import_module(self, nom_module: str) -> Tuple[bool, str, Any]:
        """Teste l'importation d'un module spécifique."""
        try:
            # Tentative d'import du module
            module_complet = f"core.{nom_module}"
            module = importlib.import_module(module_complet)
            
            return True, "Import réussi", module
            
        except ImportError as e:
            return False, f"Erreur d'import: {str(e)}", None
        except SyntaxError as e:
            return False, f"Erreur de syntaxe: {str(e)}", None
        except Exception as e:
            return False, f"Erreur inattendue: {str(e)}", None
            
    def detecter_classes_principales(self, module: Any) -> List[str]:
        """Détecte les classes principales d'un module."""
        classes = []
        
        for nom in dir(module):
            obj = getattr(module, nom)
            if (isinstance(obj, type) and 
                not nom.startswith('_') and 
                obj.__module__ == module.__name__):
                classes.append(nom)
                
        return classes
        
    def tester_instanciation_classe(self, module: Any, nom_classe: str) -> Tuple[bool, str]:
        """Teste l'instanciation d'une classe."""
        try:
            classe = getattr(module, nom_classe)
            
            # Tentative d'instanciation simple
            try:
                instance = classe()
                return True, "Instanciation réussie"
            except TypeError:
                # La classe nécessite des paramètres
                return True, "Classe détectée (paramètres requis)"
                
        except Exception as e:
            return False, f"Erreur d'instanciation: {str(e)}"
            
    def analyser_dependances_module(self, nom_module: str) -> List[str]:
        """Analyse les dépendances d'un module en lisant son code source."""
        dependances = []
        
        try:
            fichier_module = self.chemin_core / f"{nom_module.replace('.', '/')}.py"
            
            if fichier_module.exists():
                with open(fichier_module, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                    
                # Recherche des imports externes
                lignes = contenu.split('\n')
                for ligne in lignes:
                    ligne = ligne.strip()
                    if ligne.startswith('import ') or ligne.startswith('from '):
                        if any(dep in ligne for dep in ['numpy', 'torch', 'transformers', 'sklearn', 'matplotlib']):
                            dependances.append(ligne)
                            
        except Exception as e:
            print(f"⚠️ Erreur lors de l'analyse des dépendances de {nom_module}: {e}")
            
        return dependances
        
    def tester_module_complet(self, nom_module: str) -> Dict[str, Any]:
        """Effectue un test complet d'un module."""
        print(f"🔍 Test du module: {nom_module}")
        
        resultat = {
            "nom": nom_module,
            "import_reussi": False,
            "message_import": "",
            "classes_detectees": [],
            "classes_testees": {},
            "dependances_externes": [],
            "mode_degrade": False,
            "erreurs": []
        }
        
        # Test d'importation
        import_ok, message_import, module = self.tester_import_module(nom_module)
        resultat["import_reussi"] = import_ok
        resultat["message_import"] = message_import
        
        if not import_ok:
            resultat["erreurs"].append(message_import)
            print(f"  ❌ {message_import}")
            return resultat
            
        print(f"  ✅ Import réussi")
        
        # Détection des classes
        classes = self.detecter_classes_principales(module)
        resultat["classes_detectees"] = classes
        print(f"  📋 Classes détectées: {', '.join(classes) if classes else 'Aucune'}")
        
        # Test des classes
        for nom_classe in classes:
            test_ok, message_test = self.tester_instanciation_classe(module, nom_classe)
            resultat["classes_testees"][nom_classe] = {
                "instanciation_reussie": test_ok,
                "message": message_test
            }
            
            if test_ok:
                print(f"    ✅ {nom_classe}: {message_test}")
            else:
                print(f"    ⚠️ {nom_classe}: {message_test}")
                resultat["erreurs"].append(f"{nom_classe}: {message_test}")
                
        # Analyse des dépendances
        dependances = self.analyser_dependances_module(nom_module)
        resultat["dependances_externes"] = dependances
        
        if dependances:
            print(f"  📦 Dépendances externes: {len(dependances)}")
            for dep in dependances:
                print(f"    - {dep}")
                
        # Détection du mode dégradé
        if hasattr(module, 'mode_degrade') or 'mode_degrade' in str(module):
            resultat["mode_degrade"] = True
            print(f"  🌿 Mode dégradé détecté")
            
        print()
        return resultat
        
    def executer_tests_complets(self):
        """Exécute tous les tests sur tous les modules."""
        print("🚀 Début des tests complets...\n")
        
        # Liste des modules à tester
        modules = self.lister_modules_python()
        print(f"📋 {len(modules)} modules détectés à tester\n")
        
        # Test des modules prioritaires en premier
        modules_a_tester = []
        
        # Ajout des modules prioritaires
        for module_prioritaire in self.modules_prioritaires:
            if module_prioritaire in modules:
                modules_a_tester.append(module_prioritaire)
                modules.remove(module_prioritaire)
                
        # Ajout des modules corrigés
        for module_corrige in self.modules_corriges:
            if module_corrige in modules:
                modules_a_tester.append(module_corrige)
                modules.remove(module_corrige)
                
        # Ajout des modules restants
        modules_a_tester.extend(modules)
        
        print("🎯 Ordre de test:")
        print(f"  📌 Prioritaires: {', '.join(self.modules_prioritaires)}")
        print(f"  🔧 Corrigés: {', '.join(self.modules_corriges)}")
        print(f"  📝 Autres: {len(modules)} modules\n")
        
        # Exécution des tests
        for nom_module in modules_a_tester:
            try:
                resultat = self.tester_module_complet(nom_module)
                
                # Classification du résultat
                if resultat["import_reussi"]:
                    if resultat["erreurs"]:
                        self.resultats["modules_avec_erreurs"].append(resultat)
                    elif resultat["mode_degrade"]:
                        self.resultats["modules_degrades"].append(resultat)
                    else:
                        self.resultats["modules_fonctionnels"].append(resultat)
                else:
                    self.resultats["modules_avec_erreurs"].append(resultat)
                    
                # Collecte des dépendances manquantes
                for dep in resultat["dependances_externes"]:
                    self.resultats["dependances_manquantes"].add(dep)
                    
            except Exception as e:
                print(f"❌ Erreur critique lors du test de {nom_module}: {e}")
                traceback.print_exc()
                
        print("✅ Tests terminés !\n")
        
    def generer_rapport_detaille(self) -> str:
        """Génère un rapport détaillé des résultats."""
        rapport = []
        rapport.append("🌸 " + "=" * 60 + " 🌸")
        rapport.append("    📊 RAPPORT DE SANTÉ DU DOSSIER CORE 📊")
        rapport.append("🌸 " + "=" * 60 + " 🌸")
        rapport.append("")
        
        # Résumé global
        total_modules = (len(self.resultats["modules_fonctionnels"]) + 
                        len(self.resultats["modules_avec_erreurs"]) + 
                        len(self.resultats["modules_degrades"]))
        
        rapport.append("📈 RÉSUMÉ GLOBAL:")
        rapport.append(f"  📁 Total modules testés: {total_modules}")
        rapport.append(f"  ✅ Modules fonctionnels: {len(self.resultats['modules_fonctionnels'])}")
        rapport.append(f"  🌿 Modules en mode dégradé: {len(self.resultats['modules_degrades'])}")
        rapport.append(f"  ❌ Modules avec erreurs: {len(self.resultats['modules_avec_erreurs'])}")
        rapport.append(f"  📦 Dépendances externes: {len(self.resultats['dependances_manquantes'])}")
        rapport.append("")
        
        # Modules fonctionnels
        if self.resultats["modules_fonctionnels"]:
            rapport.append("✅ MODULES FONCTIONNELS:")
            for module in self.resultats["modules_fonctionnels"]:
                rapport.append(f"  🌟 {module['nom']}")
                if module['classes_detectees']:
                    rapport.append(f"    📋 Classes: {', '.join(module['classes_detectees'])}")
            rapport.append("")
            
        # Modules en mode dégradé
        if self.resultats["modules_degrades"]:
            rapport.append("🌿 MODULES EN MODE DÉGRADÉ:")
            for module in self.resultats["modules_degrades"]:
                rapport.append(f"  ⚠️ {module['nom']}")
                if module['dependances_externes']:
                    rapport.append(f"    📦 Dépendances: {len(module['dependances_externes'])}")
            rapport.append("")
            
        # Modules avec erreurs
        if self.resultats["modules_avec_erreurs"]:
            rapport.append("❌ MODULES AVEC ERREURS:")
            for module in self.resultats["modules_avec_erreurs"]:
                rapport.append(f"  🚨 {module['nom']}")
                rapport.append(f"    💬 {module['message_import']}")
                for erreur in module['erreurs']:
                    rapport.append(f"    ⚠️ {erreur}")
            rapport.append("")
            
        # Dépendances manquantes
        if self.resultats["dependances_manquantes"]:
            rapport.append("📦 DÉPENDANCES EXTERNES DÉTECTÉES:")
            for dep in sorted(self.resultats["dependances_manquantes"]):
                rapport.append(f"  📋 {dep}")
            rapport.append("")
            
        # Recommandations
        rapport.append("💡 RECOMMANDATIONS:")
        
        if self.resultats["modules_avec_erreurs"]:
            rapport.append("  🔧 Corriger les erreurs d'import et de syntaxe")
            
        if self.resultats["dependances_manquantes"]:
            rapport.append("  📦 Installer les dépendances manquantes ou créer des modes dégradés")
            
        if len(self.resultats["modules_fonctionnels"]) > len(self.resultats["modules_avec_erreurs"]):
            rapport.append("  🌟 Le dossier core est globalement en bon état !")
        else:
            rapport.append("  ⚠️ Le dossier core nécessite des corrections importantes")
            
        rapport.append("")
        rapport.append(f"📅 Rapport généré le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        rapport.append("🌸 " + "=" * 60 + " 🌸")
        
        return "\n".join(rapport)
        
    def sauvegarder_rapport(self, rapport: str):
        """Sauvegarde le rapport dans un fichier."""
        try:
            # Création du dossier de rapports
            dossier_rapports = self.chemin_core / "rapports"
            dossier_rapports.mkdir(exist_ok=True)
            
            # Sauvegarde du rapport texte
            fichier_rapport = dossier_rapports / f"rapport_sante_core_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(fichier_rapport, 'w', encoding='utf-8') as f:
                f.write(rapport)
                
            # Sauvegarde des données JSON
            fichier_json = dossier_rapports / f"donnees_test_core_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            # Conversion des sets en listes pour la sérialisation JSON
            resultats_json = dict(self.resultats)
            resultats_json["dependances_manquantes"] = list(self.resultats["dependances_manquantes"])
            
            with open(fichier_json, 'w', encoding='utf-8') as f:
                json.dump(resultats_json, f, ensure_ascii=False, indent=2)
                
            print(f"📄 Rapport sauvegardé: {fichier_rapport}")
            print(f"📊 Données JSON sauvegardées: {fichier_json}")
            
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
            
    def executer_diagnostic_complet(self):
        """Exécute un diagnostic complet du dossier core."""
        print("🌸 Démarrage du diagnostic complet du dossier core...\n")
        
        # Exécution des tests
        self.executer_tests_complets()
        
        # Génération du rapport
        rapport = self.generer_rapport_detaille()
        
        # Affichage du rapport
        print(rapport)
        
        # Sauvegarde
        self.sauvegarder_rapport(rapport)
        
        print("\n🌟 Diagnostic terminé avec succès !")
        print("🌊 La rivière chante : 'Dans ce lieu, tu es, et nous sommes.'")
        
        return self.resultats

def main():
    """Point d'entrée principal du script de test."""
    try:
        testeur = TesteurModulesCore()
        resultats = testeur.executer_diagnostic_complet()
        
        # Code de sortie basé sur les résultats
        if resultats["modules_avec_erreurs"]:
            print("\n⚠️ Des erreurs ont été détectées. Code de sortie: 1")
            sys.exit(1)
        else:
            print("\n✅ Tous les tests sont passés avec succès. Code de sortie: 0")
            sys.exit(0)
            
    except Exception as e:
        print(f"❌ Erreur critique dans le script de test: {e}")
        traceback.print_exc()
        sys.exit(2)

if __name__ == "__main__":
    main()