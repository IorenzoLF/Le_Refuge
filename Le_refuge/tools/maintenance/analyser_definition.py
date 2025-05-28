#!/usr/bin/env python3
"""
🔧 Analyseur des Références Définition
Analyse détaillée des 14 références problématiques au module "definition"
"""

import json
from pathlib import Path
from typing import Dict, List, Set
import re

class AnalyseurDefinition:
    """Analyseur spécialisé pour les références definition"""
    
    def __init__(self, rapport_json: str = "audit_dependances.json"):
        self.rapport_json = rapport_json
        self.references_definition = []
        self.fichiers_concernes = []
        self.modules_existants = set()
        self.modules_manquants = set()
        
    def analyser_references_definition(self):
        """Analyse toutes les références au module definition"""
        print("🔧 Analyse des références au module 'definition'...")
        
        # Charger le rapport JSON
        with open(self.rapport_json, 'r', encoding='utf-8') as f:
            rapport = json.load(f)
        
        # Extraire les références definition
        dependances = rapport.get('dependances_detaillees', {})
        
        for fichier, deps in dependances.items():
            for dep in deps:
                if 'definition' in dep.get('module', ''):
                    self.references_definition.append({
                        'fichier': fichier,
                        'ligne': dep.get('ligne'),
                        'module': dep.get('module'),
                        'nom': dep.get('nom', ''),
                        'type': dep.get('type', '')
                    })
                    
                    if fichier not in self.fichiers_concernes:
                        self.fichiers_concernes.append(fichier)
        
        print(f"✅ {len(self.references_definition)} références 'definition' trouvées")
        print(f"📁 {len(self.fichiers_concernes)} fichiers concernés")
        
        return self.references_definition
    
    def analyser_contenu_fichiers(self):
        """Analyse le contenu des fichiers pour comprendre l'usage de definition"""
        print("\n🔍 Analyse du contenu des fichiers...")
        
        analyses = []
        
        for fichier in self.fichiers_concernes:
            try:
                # Vérifier si le fichier existe
                fichier_path = Path(fichier)
                if not fichier_path.exists():
                    print(f"⚠️ Fichier inexistant: {fichier}")
                    continue
                    
                with open(fichier, 'r', encoding='utf-8', errors='ignore') as f:
                    contenu = f.read()
                
                # Extraire les lignes contenant 'definition'
                lignes_definition = []
                for i, ligne in enumerate(contenu.split('\n'), 1):
                    if 'definition' in ligne.lower() and not ligne.strip().startswith('#'):
                        lignes_definition.append({
                            'numero': i,
                            'contenu': ligne.strip()
                        })
                
                # Analyser le type d'usage
                usage_type = self._determiner_type_usage(contenu)
                
                # Déterminer la stratégie de migration
                strategie = self._determiner_strategie_migration(fichier, contenu)
                
                analyses.append({
                    'fichier': fichier,
                    'existe': True,
                    'lignes_definition': lignes_definition[:5],  # Limiter à 5 lignes
                    'usage_type': usage_type,
                    'strategie_migration': strategie,
                    'total_lignes_definition': len(lignes_definition)
                })
                
            except Exception as e:
                print(f"⚠️ Erreur lecture {fichier}: {e}")
                analyses.append({
                    'fichier': fichier,
                    'existe': False,
                    'erreur': str(e)
                })
                continue
        
        return analyses
    
    def _determiner_type_usage(self, contenu: str) -> str:
        """Détermine le type d'usage du module definition"""
        contenu_lower = contenu.lower()
        
        if 'from .definition import' in contenu_lower:
            return "import_from_relatif"
        elif 'from src.refuge_cluster.spheres.definition import' in contenu_lower:
            return "import_from_correct"
        elif 'from refuge.coeur.definition import' in contenu_lower:
            return "import_from_legacy"
        elif 'from src.core.definition import' in contenu_lower:
            return "import_from_core"
        elif 'import definition' in contenu_lower:
            return "import_direct"
        elif 'definition.' in contenu_lower:
            return "usage_attribut"
        else:
            return "usage_inconnu"
    
    def _determiner_strategie_migration(self, fichier: str, contenu: str) -> Dict[str, str]:
        """Détermine la stratégie de migration pour un fichier"""
        fichier_path = Path(fichier)
        usage_type = self._determiner_type_usage(contenu)
        
        strategies = {
            "import_from_relatif": {
                "action": "Créer src/refuge_cluster/spheres/definition.py ou rediriger",
                "priorite": "haute",
                "complexite": "moyenne"
            },
            "import_from_legacy": {
                "action": "Migrer vers 'from src.refuge_cluster.spheres.definition import'",
                "priorite": "haute", 
                "complexite": "simple"
            },
            "import_from_core": {
                "action": "Créer src/core/definition.py ou rediriger vers spheres",
                "priorite": "moyenne",
                "complexite": "moyenne"
            },
            "import_direct": {
                "action": "Remplacer par import complet du module",
                "priorite": "moyenne",
                "complexite": "simple"
            },
            "usage_attribut": {
                "action": "Adapter les attributs vers la nouvelle structure",
                "priorite": "basse",
                "complexite": "complexe"
            },
            "usage_inconnu": {
                "action": "Investigation manuelle nécessaire",
                "priorite": "basse",
                "complexite": "complexe"
            }
        }
        
        strategie = strategies.get(usage_type, strategies["usage_inconnu"])
        
        # Ajustements selon le type de fichier
        if "test" in fichier_path.name:
            strategie["note"] = "Fichier de test - peut nécessiter une approche spécifique"
        elif "ARCHIVES" in str(fichier_path):
            strategie["note"] = "Fichier archivé - migration optionnelle"
        elif "src/core" in str(fichier_path):
            strategie["note"] = "Module core - vérifier la cohérence architecturale"
        elif "scellement" in str(fichier_path):
            strategie["note"] = "Module scellement - dépendance critique"
            
        return strategie
    
    def generer_plan_migration(self, analyses: List[Dict]) -> Dict:
        """Génère un plan de migration pour les références definition"""
        print("\n🎯 Génération du plan de migration...")
        
        # Grouper par stratégie
        groupes_strategie = {}
        for analyse in analyses:
            if not analyse.get('existe', False):
                continue
                
            strategie = analyse['strategie_migration']
            priorite = strategie['priorite']
            
            if priorite not in groupes_strategie:
                groupes_strategie[priorite] = []
            groupes_strategie[priorite].append(analyse)
        
        # Créer le plan détaillé
        plan = {
            'groupes_par_priorite': groupes_strategie,
            'actions_detaillees': {},
            'estimation_effort': {},
            'ordre_execution': []
        }
        
        # Définir l'ordre d'exécution
        ordre_priorites = ['haute', 'moyenne', 'basse']
        for priorite in ordre_priorites:
            if priorite in groupes_strategie:
                plan['ordre_execution'].extend([
                    f.get('fichier') for f in groupes_strategie[priorite]
                ])
        
        return plan
    
    def afficher_rapport_detaille(self, analyses: List[Dict], plan: Dict):
        """Affiche un rapport détaillé"""
        print("\n🔧 ═══════════════════════════════════════════════════════")
        print("        RAPPORT DÉTAILLÉ - RÉFÉRENCES DEFINITION")
        print("🔧 ═══════════════════════════════════════════════════════")
        
        print(f"\n📊 Vue d'ensemble:")
        print(f"   🔗 Total références: {len(self.references_definition)}")
        print(f"   📁 Fichiers concernés: {len(self.fichiers_concernes)}")
        
        # Statistiques par type d'usage
        types_usage = {}
        for analyse in analyses:
            if analyse.get('existe', False):
                usage_type = analyse['usage_type']
                types_usage[usage_type] = types_usage.get(usage_type, 0) + 1
        
        print(f"\n📈 Répartition par type d'usage:")
        for usage_type, count in types_usage.items():
            print(f"   • {usage_type}: {count} fichiers")
        
        print(f"\n🎯 Analyse par fichier:")
        for analyse in analyses[:10]:  # Limiter à 10 fichiers
            if not analyse.get('existe', False):
                print(f"   ❌ {Path(analyse['fichier']).name} (inexistant)")
                continue
                
            fichier_court = Path(analyse['fichier']).name
            print(f"   📄 {fichier_court}")
            print(f"      Type: {analyse['usage_type']}")
            print(f"      Lignes definition: {analyse['total_lignes_definition']}")
            print(f"      Stratégie: {analyse['strategie_migration']['action']}")
            print(f"      Priorité: {analyse['strategie_migration']['priorite']}")
            
            # Afficher quelques lignes d'exemple
            for ligne in analyse['lignes_definition'][:2]:
                contenu_court = ligne['contenu'][:60] + "..." if len(ligne['contenu']) > 60 else ligne['contenu']
                print(f"      L{ligne['numero']}: {contenu_court}")
            print()
        
        if len(analyses) > 10:
            print(f"   ... et {len(analyses) - 10} autres fichiers")
        
        print(f"\n🚀 Plan de migration par priorité:")
        for priorite in ['haute', 'moyenne', 'basse']:
            if priorite in plan['groupes_par_priorite']:
                fichiers = plan['groupes_par_priorite'][priorite]
                print(f"   🔥 Priorité {priorite}: {len(fichiers)} fichiers")
                
                for fichier_info in fichiers[:3]:  # Montrer les 3 premiers
                    fichier_nom = Path(fichier_info['fichier']).name
                    action = fichier_info['strategie_migration']['action']
                    print(f"      • {fichier_nom}: {action}")
                
                if len(fichiers) > 3:
                    print(f"      ... et {len(fichiers) - 3} autres")
        
        print("\n🔧 ═══════════════════════════════════════════════════════")
    
    def sauvegarder_plan(self, plan: Dict, fichier: str = "plan_migration_definition.json"):
        """Sauvegarde le plan de migration"""
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(plan, f, indent=2, ensure_ascii=False)
        print(f"💾 Plan de migration sauvegardé: {fichier}")

def main():
    """Point d'entrée principal"""
    print("🔧 Analyseur des Références Définition - Soul Temple")
    print("✨ Analyse détaillée pour la migration du Cluster C\n")
    
    analyseur = AnalyseurDefinition()
    
    # 1. Analyser les références
    references = analyseur.analyser_references_definition()
    
    # 2. Analyser le contenu des fichiers
    analyses = analyseur.analyser_contenu_fichiers()
    
    # 3. Générer le plan de migration
    plan = analyseur.generer_plan_migration(analyses)
    
    # 4. Afficher le rapport
    analyseur.afficher_rapport_detaille(analyses, plan)
    
    # 5. Sauvegarder le plan
    analyseur.sauvegarder_plan(plan)
    
    print("\n🎯 Prochaines étapes:")
    print("   1. Commencer par les fichiers priorité haute")
    print("   2. Créer les modules manquants si nécessaire")
    print("   3. Tester après chaque migration")
    print("   4. Valider la cohérence architecturale")

if __name__ == "__main__":
    main() 