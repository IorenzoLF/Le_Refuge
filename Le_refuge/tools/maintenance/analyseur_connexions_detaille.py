#!/usr/bin/env python3
"""
🔍 Analyseur Détaillé des Connexions du Temple de l'Âme
Examine en profondeur les 66 connexions potentielles pour créer un meilleur système
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict

class AnalyseurConnexionsDetaille:
    """Analyseur approfondi des connexions potentielles"""
    
    def __init__(self):
        self.connexions_analysees = []
        self.patterns_connexions = defaultdict(list)
        self.recommandations = []
        
    def analyser_connexions_completes(self):
        """Analyse complète des 66 connexions"""
        print("🔍 ═══════════════════════════════════════════════════════")
        print("        ANALYSE DÉTAILLÉE DES CONNEXIONS")
        print("🔍 ═══════════════════════════════════════════════════════")
        print()
        
        # 1. Charger les données d'interconnexions
        donnees_interconnexions = self._charger_donnees_interconnexions()
        
        # 2. Charger les données robustes
        donnees_robustes = self._charger_donnees_robustes()
        
        # 3. Analyser les types de connexions
        self._analyser_types_connexions(donnees_interconnexions, donnees_robustes)
        
        # 4. Identifier les patterns de connexions
        self._identifier_patterns()
        
        # 5. Évaluer la qualité des connexions
        self._evaluer_qualite_connexions()
        
        # 6. Générer des recommandations stratégiques
        self._generer_recommandations_strategiques()
        
        # 7. Rapport final
        self._generer_rapport_detaille()
        
    def _charger_donnees_interconnexions(self) -> Dict:
        """Charge les données d'analyse d'interconnexions"""
        try:
            with open("bibliotheque/apprentissage/analyse_interconnexions.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️ Fichier analyse_interconnexions.json non trouvé")
            return {}
    
    def _charger_donnees_robustes(self) -> Dict:
        """Charge les données d'auto-découverte robuste"""
        try:
            with open("bibliotheque/apprentissage/interface_robuste.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️ Fichier interface_robuste.json non trouvé")
            return {}
    
    def _analyser_types_connexions(self, interconnexions: Dict, robustes: Dict):
        """Analyse les différents types de connexions possibles"""
        print("📊 Analyse des types de connexions...")
        
        # Connexions par imports (données interconnexions)
        if "modules" in interconnexions:
            for module_path, module_info in interconnexions["modules"].items():
                imports = module_info.get("imports", [])
                for import_module in imports:
                    self.connexions_analysees.append({
                        "type": "import_direct",
                        "source": module_path,
                        "cible": import_module,
                        "force": "forte",
                        "temple_source": self._extraire_temple(module_path),
                        "temple_cible": self._extraire_temple(import_module)
                    })
        
        # Connexions par catégories (données robustes)
        if "fonctionnalites_count" in robustes:
            for categorie, count in robustes["fonctionnalites_count"].items():
                if count > 1:
                    self.connexions_analysees.append({
                        "type": "categorie_fonctionnelle",
                        "categorie": categorie,
                        "elements": count,
                        "force": "moyenne" if count < 5 else "forte",
                        "potentiel": "élevé" if count > 10 else "moyen"
                    })
        
        # Connexions par temples (données robustes)
        if "temples" in robustes:
            for temple_name, temple_info in robustes["temples"].items():
                modules_count = len(temple_info.get("modules", []))
                if modules_count > 3:
                    self.connexions_analysees.append({
                        "type": "temple_interne",
                        "temple": temple_name,
                        "modules": modules_count,
                        "classes": temple_info.get("classes_totales", 0),
                        "fonctions": temple_info.get("fonctions_totales", 0),
                        "force": "forte" if modules_count > 10 else "moyenne",
                        "priorite": "haute" if temple_info.get("classes_totales", 0) > 20 else "moyenne"
                    })
        
        print(f"   📊 {len(self.connexions_analysees)} connexions analysées")
        print()
    
    def _extraire_temple(self, chemin: str) -> str:
        """Extrait le nom du temple depuis un chemin"""
        if "temple_" in chemin:
            parts = chemin.split("/")
            for part in parts:
                if part.startswith("temple_"):
                    return part
        return "core" if "src/core" in chemin else "autre"
    
    def _identifier_patterns(self):
        """Identifie les patterns dans les connexions"""
        print("🔍 Identification des patterns...")
        
        # Grouper par type
        for connexion in self.connexions_analysees:
            type_connexion = connexion["type"]
            self.patterns_connexions[type_connexion].append(connexion)
        
        # Analyser les patterns spécifiques
        self._analyser_pattern_imports()
        self._analyser_pattern_categories()
        self._analyser_pattern_temples()
        
        print(f"   🔍 {len(self.patterns_connexions)} patterns identifiés")
        print()
    
    def _analyser_pattern_imports(self):
        """Analyse le pattern des imports directs"""
        imports = self.patterns_connexions.get("import_direct", [])
        if imports:
            # Connexions inter-temples
            inter_temples = [c for c in imports if c["temple_source"] != c["temple_cible"]]
            intra_temples = [c for c in imports if c["temple_source"] == c["temple_cible"]]
            
            self.patterns_connexions["imports_inter_temples"] = inter_temples
            self.patterns_connexions["imports_intra_temples"] = intra_temples
    
    def _analyser_pattern_categories(self):
        """Analyse le pattern des catégories fonctionnelles"""
        categories = self.patterns_connexions.get("categorie_fonctionnelle", [])
        
        # Catégories dominantes
        dominantes = [c for c in categories if c["elements"] > 10]
        moyennes = [c for c in categories if 3 <= c["elements"] <= 10]
        petites = [c for c in categories if c["elements"] < 3]
        
        self.patterns_connexions["categories_dominantes"] = dominantes
        self.patterns_connexions["categories_moyennes"] = moyennes
        self.patterns_connexions["categories_petites"] = petites
    
    def _analyser_pattern_temples(self):
        """Analyse le pattern des temples"""
        temples = self.patterns_connexions.get("temple_interne", [])
        
        # Temples riches vs pauvres
        riches = [t for t in temples if t["classes"] > 15]
        moyens = [t for t in temples if 5 <= t["classes"] <= 15]
        pauvres = [t for t in temples if t["classes"] < 5]
        
        self.patterns_connexions["temples_riches"] = riches
        self.patterns_connexions["temples_moyens"] = moyens
        self.patterns_connexions["temples_pauvres"] = pauvres
    
    def _evaluer_qualite_connexions(self):
        """Évalue la qualité et le potentiel des connexions"""
        print("⚖️ Évaluation de la qualité des connexions...")
        
        # Métriques de qualité
        total_connexions = len(self.connexions_analysees)
        connexions_fortes = len([c for c in self.connexions_analysees if c.get("force") == "forte"])
        connexions_moyennes = len([c for c in self.connexions_analysees if c.get("force") == "moyenne"])
        
        # Potentiel d'amélioration
        categories_dominantes = len(self.patterns_connexions.get("categories_dominantes", []))
        temples_riches = len(self.patterns_connexions.get("temples_riches", []))
        
        self.qualite_connexions = {
            "total": total_connexions,
            "fortes": connexions_fortes,
            "moyennes": connexions_moyennes,
            "ratio_fortes": connexions_fortes / total_connexions if total_connexions > 0 else 0,
            "categories_dominantes": categories_dominantes,
            "temples_riches": temples_riches,
            "potentiel_global": "élevé" if categories_dominantes > 3 and temples_riches > 3 else "moyen"
        }
        
        print(f"   ⚖️ Qualité évaluée: {self.qualite_connexions['potentiel_global']}")
        print()
    
    def _generer_recommandations_strategiques(self):
        """Génère des recommandations stratégiques basées sur l'analyse"""
        print("💡 Génération des recommandations stratégiques...")
        
        # Recommandations basées sur les catégories dominantes
        categories_dominantes = self.patterns_connexions.get("categories_dominantes", [])
        for cat in categories_dominantes:
            self.recommandations.append({
                "type": "categorie_prioritaire",
                "categorie": cat["categorie"],
                "elements": cat["elements"],
                "action": f"Créer un hub pour la catégorie '{cat['categorie']}' avec {cat['elements']} éléments",
                "priorite": "haute",
                "impact": "élevé"
            })
        
        # Recommandations basées sur les temples riches
        temples_riches = self.patterns_connexions.get("temples_riches", [])
        for temple in temples_riches:
            self.recommandations.append({
                "type": "temple_prioritaire",
                "temple": temple["temple"],
                "classes": temple["classes"],
                "action": f"Optimiser les connexions internes du temple '{temple['temple']}' ({temple['classes']} classes)",
                "priorite": "haute",
                "impact": "élevé"
            })
        
        # Recommandations pour les connexions inter-temples
        inter_temples = self.patterns_connexions.get("imports_inter_temples", [])
        if len(inter_temples) < 10:
            self.recommandations.append({
                "type": "connexions_manquantes",
                "action": "Créer plus de connexions inter-temples (actuellement très faibles)",
                "priorite": "critique",
                "impact": "révolutionnaire"
            })
        
        # Recommandations pour les catégories moyennes
        categories_moyennes = self.patterns_connexions.get("categories_moyennes", [])
        for cat in categories_moyennes:
            self.recommandations.append({
                "type": "categorie_potentiel",
                "categorie": cat["categorie"],
                "action": f"Développer la catégorie '{cat['categorie']}' (potentiel de croissance)",
                "priorite": "moyenne",
                "impact": "moyen"
            })
        
        print(f"   💡 {len(self.recommandations)} recommandations générées")
        print()
    
    def _generer_rapport_detaille(self):
        """Génère le rapport détaillé d'analyse"""
        print("📋 RAPPORT DÉTAILLÉ DES CONNEXIONS")
        print("=" * 50)
        print()
        
        # Vue d'ensemble
        print("📊 VUE D'ENSEMBLE:")
        print(f"   • Connexions analysées: {self.qualite_connexions['total']}")
        print(f"   • Connexions fortes: {self.qualite_connexions['fortes']} ({self.qualite_connexions['ratio_fortes']:.1%})")
        print(f"   • Connexions moyennes: {self.qualite_connexions['moyennes']}")
        print(f"   • Potentiel global: {self.qualite_connexions['potentiel_global']}")
        print()
        
        # Patterns identifiés
        print("🔍 PATTERNS IDENTIFIÉS:")
        for pattern, elements in self.patterns_connexions.items():
            if elements and not pattern.startswith("import_"):
                print(f"   • {pattern}: {len(elements)} éléments")
        print()
        
        # Top recommandations
        print("💡 TOP RECOMMANDATIONS STRATÉGIQUES:")
        recommandations_triees = sorted(self.recommandations, 
                                      key=lambda x: {"critique": 3, "haute": 2, "moyenne": 1}.get(x["priorite"], 0), 
                                      reverse=True)
        
        for i, rec in enumerate(recommandations_triees[:5], 1):
            print(f"   {i}. [{rec['priorite'].upper()}] {rec['action']}")
        print()
        
        # Catégories dominantes détaillées
        categories_dominantes = self.patterns_connexions.get("categories_dominantes", [])
        if categories_dominantes:
            print("🎯 CATÉGORIES DOMINANTES (Opportunités majeures):")
            for cat in sorted(categories_dominantes, key=lambda x: x["elements"], reverse=True):
                print(f"   • {cat['categorie']}: {cat['elements']} éléments (Force: {cat['force']})")
            print()
        
        # Temples riches détaillés
        temples_riches = self.patterns_connexions.get("temples_riches", [])
        if temples_riches:
            print("🏛️ TEMPLES RICHES (Hubs potentiels):")
            for temple in sorted(temples_riches, key=lambda x: x["classes"], reverse=True):
                print(f"   • {temple['temple']}: {temple['classes']} classes, {temple['fonctions']} fonctions")
            print()
        
        # Stratégie recommandée
        print("🎯 STRATÉGIE RECOMMANDÉE POUR LE SYSTÈME:")
        print("   1. PRIORITÉ 1: Connecter les catégories dominantes")
        print("   2. PRIORITÉ 2: Optimiser les temples riches")
        print("   3. PRIORITÉ 3: Créer des ponts inter-temples")
        print("   4. PRIORITÉ 4: Développer les catégories moyennes")
        print()
        
        # Sauvegarde
        self._sauvegarder_analyse()
        
        print("💾 Analyse détaillée sauvegardée: bibliotheque/apprentissage/analyse_connexions_detaillee.json")
    
    def _sauvegarder_analyse(self):
        """Sauvegarde l'analyse détaillée"""
        analyse_complete = {
            "connexions_analysees": self.connexions_analysees,
            "patterns_connexions": dict(self.patterns_connexions),
            "qualite_connexions": self.qualite_connexions,
            "recommandations": self.recommandations,
            "resume": {
                "total_connexions": len(self.connexions_analysees),
                "patterns_identifies": len(self.patterns_connexions),
                "recommandations_generees": len(self.recommandations),
                "potentiel_global": self.qualite_connexions["potentiel_global"]
            }
        }
        
        os.makedirs("bibliotheque/apprentissage", exist_ok=True)
        with open("bibliotheque/apprentissage/analyse_connexions_detaillee.json", "w", encoding="utf-8") as f:
            json.dump(analyse_complete, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    analyseur = AnalyseurConnexionsDetaille()
    analyseur.analyser_connexions_completes() 