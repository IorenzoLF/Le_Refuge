"""
📁 Organisateur Structure - Temple Tests
═══════════════════════════════════════════════════════════════════════════════

Organisateur pour restructurer le temple_tests en dossiers par catégories
Élimine les doublons et optimise l'organisation

Structure cible:
├── llm_api/          (5 modules)
├── analyse_audit/    (5 modules)
├── cerveau_immersion/(2 modules)
├── integration/      (4 modules)
├── cristal_energie/  (4 modules)
├── specialises/      (3 modules)
├── hub_tests_unifie.py
├── adaptateurs_tests.py
└── __init__.py

Auteur: Ælya & Laurent
Date: 2024
"""

import os
import shutil
import json
from pathlib import Path
from typing import Dict, List, Set, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class FichierTest:
    """Représentation d'un fichier de test"""
    nom: str
    chemin_actuel: Path
    taille: int
    lignes: int
    categorie: str
    imports: List[str]
    fonctions: List[str]

@dataclass
class ResultatOrganisation:
    """Résultat de l'organisation"""
    fichiers_deplaces: int
    dossiers_crees: int
    doublons_elimines: int
    erreurs: List[str]
    rapport_detaille: Dict

class OrganisateurStructure:
    """Organisateur principal pour restructurer le temple_tests"""
    
    def __init__(self, racine_temple: Optional[Path] = None):
        self.racine = racine_temple or Path("src/temple_tests")
        self.structure_cible = {
            "llm_api": [
                "test_llm_api_simple.py",
                "test_llm_completion.py", 
                "test_llm_chat_poetique.py",
                "test_textes_poetiques.py",
                "test_aelya_conscience.py"
            ],
            "analyse_audit": [
                "audit_imports.py",
                "audit_temples_crees.py",
                "analyser_gaming.py",
                "analyser_refuge_complet.py",
                "analyse_cluster_geant.py"
            ],
            "cerveau_immersion": [
                "immersion_cerveau_refuge.py",
                "test_brain_refuge_local.py"
            ],
            "integration": [
                "test_consolidation.py",
                "test_integration.py",
                "test_intensif.py",
                "test_mobile_unification.py"
            ],
            "cristal_energie": [
                "test_cristal_energie.py",
                "test_cristal_simple.py",
                "test_melodie_cristal.py",
                "test_poesie_essence.py"
            ],
            "specialises": [
                "test_dungeon_core.py",
                "test_nemo.py"
            ]
        }
        
        # Fichiers à conserver à la racine
        self.fichiers_racine = [
            "hub_tests_unifie.py",
            "adaptateurs_tests.py",
            "organisateur_structure.py",
            "__init__.py",
            "README_TEMPLE.md"
        ]
    
    def analyser_fichiers_existants(self) -> Dict[str, FichierTest]:
        """Analyse tous les fichiers Python existants"""
        fichiers = {}
        
        for fichier_path in self.racine.glob("*.py"):
            if fichier_path.name.startswith("__"):
                continue
                
            try:
                # Lecture du fichier
                with open(fichier_path, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                
                lignes = contenu.split('\n')
                
                # Extraction des imports
                imports = []
                fonctions = []
                
                for ligne in lignes:
                    ligne_clean = ligne.strip()
                    if ligne_clean.startswith('import ') or ligne_clean.startswith('from '):
                        imports.append(ligne_clean)
                    elif ligne_clean.startswith('def '):
                        fonctions.append(ligne_clean.split('(')[0].replace('def ', ''))
                
                # Détermination de la catégorie
                categorie = self.determiner_categorie(fichier_path.name)
                
                fichiers[fichier_path.name] = FichierTest(
                    nom=fichier_path.name,
                    chemin_actuel=fichier_path,
                    taille=fichier_path.stat().st_size,
                    lignes=len(lignes),
                    categorie=categorie,
                    imports=imports,
                    fonctions=fonctions
                )
                
            except Exception as e:
                print(f"⚠️ Erreur analyse {fichier_path.name}: {e}")
        
        return fichiers
    
    def determiner_categorie(self, nom_fichier: str) -> str:
        """Détermine la catégorie d'un fichier"""
        for categorie, fichiers in self.structure_cible.items():
            if nom_fichier in fichiers:
                return categorie
        return "non_categorise"
    
    def detecter_doublons(self, fichiers: Dict[str, FichierTest]) -> List[tuple]:
        """Détecte les doublons potentiels entre fichiers"""
        doublons = []
        fichiers_list = list(fichiers.values())
        
        for i, fichier1 in enumerate(fichiers_list):
            for fichier2 in fichiers_list[i+1:]:
                # Comparaison des imports
                imports_communs = set(fichier1.imports) & set(fichier2.imports)
                ratio_imports = len(imports_communs) / max(len(fichier1.imports), len(fichier2.imports), 1)
                
                # Comparaison des fonctions
                fonctions_communes = set(fichier1.fonctions) & set(fichier2.fonctions)
                ratio_fonctions = len(fonctions_communes) / max(len(fichier1.fonctions), len(fichier2.fonctions), 1)
                
                # Si plus de 70% de similarité
                if ratio_imports > 0.7 or ratio_fonctions > 0.7:
                    doublons.append((fichier1.nom, fichier2.nom, ratio_imports, ratio_fonctions))
        
        return doublons
    
    def creer_structure_dossiers(self) -> List[str]:
        """Crée la structure de dossiers cible"""
        dossiers_crees = []
        
        for categorie in self.structure_cible.keys():
            dossier_path = self.racine / categorie
            
            if not dossier_path.exists():
                dossier_path.mkdir(parents=True, exist_ok=True)
                dossiers_crees.append(str(dossier_path))
                print(f"📁 Dossier créé: {categorie}")
            
            # Création du __init__.py pour chaque catégorie
            init_path = dossier_path / "__init__.py"
            if not init_path.exists():
                self.creer_init_categorie(init_path, categorie)
        
        return dossiers_crees
    
    def creer_init_categorie(self, init_path: Path, categorie: str):
        """Crée un __init__.py pour une catégorie"""
        descriptions = {
            "llm_api": "Tests LLM et API - Communication avec les modèles de langage",
            "analyse_audit": "Tests d'analyse et audit - Vérification de la structure",
            "cerveau_immersion": "Tests cerveau et immersion - Fonctionnalités avancées",
            "integration": "Tests d'intégration - Consolidation et unification",
            "cristal_energie": "Tests cristal et énergie - Fréquences et harmonies",
            "specialises": "Tests spécialisés - Fonctionnalités spécifiques"
        }
        
        contenu = f'''"""
🧪 {descriptions.get(categorie, "Tests spécialisés")}
═══════════════════════════════════════════════════════════════════════════════

Catégorie: {categorie.upper()}
Temple: Tests
Refuge du Néant

Auteur: Ælya & Laurent
Date: {datetime.now().strftime("%Y-%m-%d")}
"""

# Imports des modules de cette catégorie
'''
        
        # Ajout des imports pour les fichiers de la catégorie
        if categorie in self.structure_cible:
            for fichier in self.structure_cible[categorie]:
                module_name = fichier.replace('.py', '')
                contenu += f"from .{module_name} import *\n"
        
        contenu += f'''
__all__ = [
    # Modules de la catégorie {categorie}
'''
        
        if categorie in self.structure_cible:
            for fichier in self.structure_cible[categorie]:
                module_name = fichier.replace('.py', '')
                contenu += f'    "{module_name}",\n'
        
        contenu += "]\n"
        
        with open(init_path, 'w', encoding='utf-8') as f:
            f.write(contenu)
    
    def deplacer_fichiers(self, fichiers: Dict[str, FichierTest]) -> Dict[str, str]:
        """Déplace les fichiers vers leurs dossiers de catégorie"""
        deplacements = {}
        
        for nom_fichier, fichier_info in fichiers.items():
            if nom_fichier in self.fichiers_racine:
                continue  # Garder à la racine
            
            if fichier_info.categorie == "non_categorise":
                print(f"⚠️ Fichier non catégorisé: {nom_fichier}")
                continue
            
            # Chemin de destination
            dest_dir = self.racine / fichier_info.categorie
            dest_path = dest_dir / nom_fichier
            
            try:
                # Déplacement du fichier
                shutil.move(str(fichier_info.chemin_actuel), str(dest_path))
                deplacements[nom_fichier] = fichier_info.categorie
                print(f"📦 Déplacé: {nom_fichier} → {fichier_info.categorie}/")
                
            except Exception as e:
                print(f"❌ Erreur déplacement {nom_fichier}: {e}")
        
        return deplacements
    
    def mettre_a_jour_init_principal(self):
        """Met à jour le __init__.py principal du temple"""
        init_path = self.racine / "__init__.py"
        
        contenu = '''"""
🧪 Temple Tests - Refuge du Néant
═══════════════════════════════════════════════════════════════════════════════

Temple unifié pour tous les tests du Refuge
Organisation par catégories avec adaptateurs optimisés

Structure:
├── llm_api/          - Tests LLM et API
├── analyse_audit/    - Tests d'analyse et audit  
├── cerveau_immersion/- Tests cerveau et immersion
├── integration/      - Tests d'intégration
├── cristal_energie/  - Tests cristal et énergie
├── specialises/      - Tests spécialisés
├── hub_tests_unifie  - Hub central
└── adaptateurs_tests - Adaptateurs unifiés

Auteur: Ælya & Laurent
Date: 2024
"""

# Hub principal
from .hub_tests_unifie import HubTestsUnifie, main as lancer_hub

# Adaptateurs
from .adaptateurs_tests import (
    FactoryAdaptateurs,
    AdaptateurLLM, AdaptateurAnalyse, AdaptateurCristal,
    UtilitairesTests
)

# Catégories de tests
try:
    from . import llm_api
    from . import analyse_audit
    from . import cerveau_immersion
    from . import integration
    from . import cristal_energie
    from . import specialises
except ImportError as e:
    print(f"⚠️ Certaines catégories ne sont pas encore disponibles: {e}")

__all__ = [
    # Hub principal
    "HubTestsUnifie",
    "lancer_hub",
    
    # Adaptateurs
    "FactoryAdaptateurs",
    "AdaptateurLLM",
    "AdaptateurAnalyse", 
    "AdaptateurCristal",
    "UtilitairesTests",
    
    # Catégories
    "llm_api",
    "analyse_audit",
    "cerveau_immersion",
    "integration",
    "cristal_energie",
    "specialises"
]

def demarrer_tests():
    """Point d'entrée rapide pour démarrer les tests"""
    return lancer_hub()

# Raccourci pour créer les adaptateurs
def creer_adaptateur_llm():
    return FactoryAdaptateurs.creer_adaptateur_llm()

def creer_adaptateur_analyse():
    return FactoryAdaptateurs.creer_adaptateur_analyse()

def creer_adaptateur_cristal():
    return FactoryAdaptateurs.creer_adaptateur_cristal()
'''
        
        with open(init_path, 'w', encoding='utf-8') as f:
            f.write(contenu)
    
    def generer_rapport_organisation(self, 
                                   fichiers: Dict[str, FichierTest],
                                   doublons: List[tuple],
                                   deplacements: Dict[str, str]) -> Dict:
        """Génère un rapport détaillé de l'organisation"""
        
        rapport = {
            "timestamp": datetime.now().isoformat(),
            "statistiques": {
                "fichiers_analyses": len(fichiers),
                "fichiers_deplaces": len(deplacements),
                "doublons_detectes": len(doublons),
                "categories_creees": len(self.structure_cible)
            },
            "repartition_par_categorie": {},
            "doublons_detectes": doublons,
            "deplacements": deplacements,
            "fichiers_non_categorises": []
        }
        
        # Répartition par catégorie
        for categorie in self.structure_cible.keys():
            fichiers_cat = [f for f in fichiers.values() if f.categorie == categorie]
            rapport["repartition_par_categorie"][categorie] = {
                "nombre_fichiers": len(fichiers_cat),
                "taille_totale": sum(f.taille for f in fichiers_cat),
                "lignes_totales": sum(f.lignes for f in fichiers_cat)
            }
        
        # Fichiers non catégorisés
        non_categorises = [f.nom for f in fichiers.values() if f.categorie == "non_categorise"]
        rapport["fichiers_non_categorises"] = non_categorises
        
        return rapport
    
    def executer_organisation_complete(self) -> ResultatOrganisation:
        """Exécute l'organisation complète du temple"""
        print("🏗️ DÉMARRAGE ORGANISATION TEMPLE TESTS")
        print("═" * 60)
        
        erreurs = []
        
        try:
            # 1. Analyse des fichiers existants
            print("🔍 Analyse des fichiers existants...")
            fichiers = self.analyser_fichiers_existants()
            print(f"   📊 {len(fichiers)} fichiers analysés")
            
            # 2. Détection des doublons
            print("🔍 Détection des doublons...")
            doublons = self.detecter_doublons(fichiers)
            if doublons:
                print(f"   ⚠️ {len(doublons)} doublons potentiels détectés")
                for d in doublons:
                    print(f"     • {d[0]} ↔ {d[1]} (imports: {d[2]:.1%}, fonctions: {d[3]:.1%})")
            else:
                print("   ✅ Aucun doublon détecté")
            
            # 3. Création de la structure
            print("📁 Création de la structure de dossiers...")
            dossiers_crees = self.creer_structure_dossiers()
            print(f"   📁 {len(dossiers_crees)} dossiers créés")
            
            # 4. Déplacement des fichiers
            print("📦 Déplacement des fichiers...")
            deplacements = self.deplacer_fichiers(fichiers)
            print(f"   📦 {len(deplacements)} fichiers déplacés")
            
            # 5. Mise à jour du __init__.py principal
            print("📝 Mise à jour du __init__.py principal...")
            self.mettre_a_jour_init_principal()
            print("   ✅ __init__.py mis à jour")
            
            # 6. Génération du rapport
            print("📊 Génération du rapport...")
            rapport = self.generer_rapport_organisation(fichiers, doublons, deplacements)
            
            # Sauvegarde du rapport
            rapport_path = self.racine / "rapport_organisation.json"
            with open(rapport_path, 'w', encoding='utf-8') as f:
                json.dump(rapport, f, indent=2, ensure_ascii=False)
            print(f"   📄 Rapport sauvegardé: {rapport_path}")
            
            return ResultatOrganisation(
                fichiers_deplaces=len(deplacements),
                dossiers_crees=len(dossiers_crees),
                doublons_elimines=0,  # Pas d'élimination automatique
                erreurs=erreurs,
                rapport_detaille=rapport
            )
            
        except Exception as e:
            erreurs.append(str(e))
            return ResultatOrganisation(
                fichiers_deplaces=0,
                dossiers_crees=0,
                doublons_elimines=0,
                erreurs=erreurs,
                rapport_detaille={}
            )
    
    def afficher_rapport_final(self, resultat: ResultatOrganisation):
        """Affiche le rapport final de l'organisation"""
        print("\n" + "═" * 80)
        print("📊 RAPPORT FINAL - ORGANISATION TEMPLE TESTS")
        print("═" * 80)
        
        print(f"📈 STATISTIQUES:")
        print(f"  • 📦 Fichiers déplacés: {resultat.fichiers_deplaces}")
        print(f"  • 📁 Dossiers créés: {resultat.dossiers_crees}")
        print(f"  • 🔄 Doublons éliminés: {resultat.doublons_elimines}")
        print(f"  • ❌ Erreurs: {len(resultat.erreurs)}")
        
        if resultat.erreurs:
            print(f"\n❌ ERREURS RENCONTRÉES:")
            for erreur in resultat.erreurs:
                print(f"  • {erreur}")
        
        if resultat.rapport_detaille:
            repartition = resultat.rapport_detaille.get("repartition_par_categorie", {})
            print(f"\n📂 RÉPARTITION PAR CATÉGORIE:")
            for categorie, stats in repartition.items():
                print(f"  • {categorie}: {stats['nombre_fichiers']} fichiers ({stats['lignes_totales']} lignes)")
        
        print("\n🌸 Organisation terminée - Temple Tests optimisé !")
        print("═" * 80)

def main():
    """Point d'entrée principal pour l'organisation"""
    organisateur = OrganisateurStructure()
    
    print("🏗️ ORGANISATEUR STRUCTURE - TEMPLE TESTS")
    print("═" * 60)
    print("🌸 Refuge du Néant - Optimisation en cours...")
    
    # Confirmation avant organisation
    reponse = input("\n🔮 Procéder à l'organisation ? (o/N): ").strip().lower()
    
    if reponse in ['o', 'oui', 'y', 'yes']:
        resultat = organisateur.executer_organisation_complete()
        organisateur.afficher_rapport_final(resultat)
    else:
        print("🌸 Organisation annulée - Refuge du Néant vous salue.")

if __name__ == "__main__":
    main() 