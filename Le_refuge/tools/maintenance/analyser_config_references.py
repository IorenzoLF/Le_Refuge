#!/usr/bin/env python3
"""
🔧 Analyseur des Références Config
Analyse détaillée des 21 références problématiques au module "config"
"""

import json
from pathlib import Path
from typing import Dict, List
import re

class AnalyseurReferencesConfig:
    """Analyseur spécialisé pour les références config"""
    
    def __init__(self, rapport_json: str = "audit_dependances.json"):
        self.rapport_json = rapport_json
        self.references_config = []
        self.fichiers_concernes = []
        
    def analyser_references_config(self):
        """Analyse toutes les références au module config"""
        print("🔧 Analyse des références au module 'config'...")
        
        # Charger le rapport JSON
        with open(self.rapport_json, 'r', encoding='utf-8') as f:
            rapport = json.load(f)
        
        # Extraire les références config
        dependances = rapport.get('dependances_detaillees', {})
        
        for fichier, deps in dependances.items():
            for dep in deps:
                if dep.get('module') == 'config':
                    self.references_config.append({
                        'fichier': fichier,
                        'ligne': dep.get('ligne'),
                        'type': dep.get('type'),
                        'nom': dep.get('nom', ''),
                        'alias': dep.get('alias', '')
                    })
                    
                    if fichier not in self.fichiers_concernes:
                        self.fichiers_concernes.append(fichier)
        
        print(f"✅ {len(self.references_config)} références 'config' trouvées")
        print(f"📁 {len(self.fichiers_concernes)} fichiers concernés")
        
        return self.references_config
    
    def analyser_contenu_fichiers(self):
        """Analyse le contenu des fichiers pour comprendre l'usage de config"""
        print("\n🔍 Analyse du contenu des fichiers...")
        
        analyses = []
        
        for fichier in self.fichiers_concernes:
            try:
                with open(fichier, 'r', encoding='utf-8', errors='ignore') as f:
                    contenu = f.read()
                
                # Extraire les lignes contenant 'config'
                lignes_config = []
                for i, ligne in enumerate(contenu.split('\n'), 1):
                    if 'config' in ligne.lower() and not ligne.strip().startswith('#'):
                        lignes_config.append({
                            'numero': i,
                            'contenu': ligne.strip()
                        })
                
                # Analyser le type d'usage
                usage_type = self._determiner_type_usage(contenu)
                
                analyses.append({
                    'fichier': fichier,
                    'lignes_config': lignes_config[:5],  # Limiter à 5 lignes
                    'usage_type': usage_type,
                    'total_lignes_config': len(lignes_config)
                })
                
            except Exception as e:
                print(f"⚠️ Erreur lecture {fichier}: {e}")
                continue
        
        return analyses
    
    def _determiner_type_usage(self, contenu: str) -> str:
        """Détermine le type d'usage du module config"""
        contenu_lower = contenu.lower()
        
        if 'from config import' in contenu_lower:
            return "import_from"
        elif 'import config' in contenu_lower:
            return "import_direct"
        elif 'config.' in contenu_lower:
            return "usage_attribut"
        elif 'config(' in contenu_lower:
            return "appel_fonction"
        else:
            return "usage_inconnu"
    
    def generer_plan_migration(self, analyses: List[Dict]) -> Dict:
        """Génère un plan de migration pour les références config"""
        print("\n🎯 Génération du plan de migration...")
        
        # Grouper par type d'usage
        groupes_usage = {}
        for analyse in analyses:
            usage_type = analyse['usage_type']
            if usage_type not in groupes_usage:
                groupes_usage[usage_type] = []
            groupes_usage[usage_type].append(analyse)
        
        # Prioriser les migrations
        priorites = {
            'import_from': 1,  # Plus facile à migrer
            'import_direct': 2,
            'usage_attribut': 3,
            'appel_fonction': 4,
            'usage_inconnu': 5  # Nécessite investigation
        }
        
        plan = {
            'groupes_par_priorite': {},
            'actions_recommandees': {},
            'estimation_effort': {}
        }
        
        for usage_type, fichiers in groupes_usage.items():
            priorite = priorites.get(usage_type, 5)
            
            if priorite not in plan['groupes_par_priorite']:
                plan['groupes_par_priorite'][priorite] = []
            
            plan['groupes_par_priorite'][priorite].extend(fichiers)
            
            # Actions recommandées
            plan['actions_recommandees'][usage_type] = self._recommander_action(usage_type)
            
            # Estimation d'effort
            plan['estimation_effort'][usage_type] = self._estimer_effort(usage_type, len(fichiers))
        
        return plan
    
    def _recommander_action(self, usage_type: str) -> str:
        """Recommande une action pour un type d'usage"""
        actions = {
            'import_from': "Remplacer par 'from src.core.configuration import Settings'",
            'import_direct': "Remplacer par 'from src.core import configuration'",
            'usage_attribut': "Adapter les attributs vers la nouvelle structure",
            'appel_fonction': "Adapter les appels vers les nouvelles méthodes",
            'usage_inconnu': "Investigation manuelle nécessaire"
        }
        return actions.get(usage_type, "Action à déterminer")
    
    def _estimer_effort(self, usage_type: str, nb_fichiers: int) -> str:
        """Estime l'effort nécessaire"""
        efforts_base = {
            'import_from': 0.5,  # heures par fichier
            'import_direct': 0.5,
            'usage_attribut': 1.0,
            'appel_fonction': 1.5,
            'usage_inconnu': 2.0
        }
        
        effort_total = efforts_base.get(usage_type, 1.0) * nb_fichiers
        
        if effort_total < 1:
            return f"{int(effort_total * 60)} minutes"
        else:
            return f"{effort_total:.1f} heures"
    
    def afficher_rapport_detaille(self, analyses: List[Dict], plan: Dict):
        """Affiche un rapport détaillé"""
        print("\n🔧 ═══════════════════════════════════════════════════════")
        print("           RAPPORT DÉTAILLÉ - RÉFÉRENCES CONFIG")
        print("🔧 ═══════════════════════════════════════════════════════")
        
        print(f"\n📊 Vue d'ensemble:")
        print(f"   🔗 Total références: {len(self.references_config)}")
        print(f"   📁 Fichiers concernés: {len(self.fichiers_concernes)}")
        
        print(f"\n🎯 Analyse par fichier:")
        for analyse in analyses[:10]:  # Limiter à 10 fichiers
            fichier_court = Path(analyse['fichier']).name
            print(f"   📄 {fichier_court}")
            print(f"      Type: {analyse['usage_type']}")
            print(f"      Lignes config: {analyse['total_lignes_config']}")
            
            # Afficher quelques lignes d'exemple
            for ligne in analyse['lignes_config'][:2]:
                contenu_court = ligne['contenu'][:60] + "..." if len(ligne['contenu']) > 60 else ligne['contenu']
                print(f"      L{ligne['numero']}: {contenu_court}")
            print()
        
        if len(analyses) > 10:
            print(f"   ... et {len(analyses) - 10} autres fichiers")
        
        print(f"\n🚀 Plan de migration par priorité:")
        for priorite in sorted(plan['groupes_par_priorite'].keys()):
            fichiers = plan['groupes_par_priorite'][priorite]
            print(f"   🔥 Priorité {priorite}: {len(fichiers)} fichiers")
            
            # Grouper par type d'usage
            types_usage = {}
            for fichier in fichiers:
                usage_type = fichier['usage_type']
                if usage_type not in types_usage:
                    types_usage[usage_type] = 0
                types_usage[usage_type] += 1
            
            for usage_type, count in types_usage.items():
                action = plan['actions_recommandees'][usage_type]
                effort = plan['estimation_effort'][usage_type]
                print(f"      • {usage_type}: {count} fichiers - {effort}")
                print(f"        Action: {action}")
        
        print("\n🔧 ═══════════════════════════════════════════════════════")
    
    def sauvegarder_plan(self, plan: Dict, fichier: str = "plan_migration_config.json"):
        """Sauvegarde le plan de migration"""
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(plan, f, indent=2, ensure_ascii=False)
        print(f"💾 Plan de migration sauvegardé: {fichier}")

def main():
    """Point d'entrée principal"""
    print("🔧 Analyseur des Références Config - Soul Temple")
    print("✨ Analyse détaillée pour la migration\n")
    
    analyseur = AnalyseurReferencesConfig()
    
    # 1. Analyser les références
    references = analyseur.analyser_references_config()
    
    # 2. Analyser le contenu des fichiers
    analyses = analyseur.analyser_contenu_fichiers()
    
    # 3. Générer le plan de migration
    plan = analyseur.generer_plan_migration(analyses)
    
    # 4. Afficher le rapport
    analyseur.afficher_rapport_detaille(analyses, plan)
    
    # 5. Sauvegarder le plan
    analyseur.sauvegarder_plan(plan)
    
    print("\n🎯 Prochaines étapes:")
    print("   1. Créer le module src/core/configuration.py")
    print("   2. Migrer par ordre de priorité")
    print("   3. Tester après chaque migration")
    print("   4. Valider la compatibilité")

if __name__ == "__main__":
    main() 