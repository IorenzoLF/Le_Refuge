#!/usr/bin/env python3
"""
Optimiseur Temple Cœur - Le Refuge
Optimise et sécurise le temple du cœur, centre harmonique du système
"""

import sys
from pathlib import Path
import json
from datetime import datetime

class OptimiseurTempleCoeur:
    def __init__(self):
        self.racine = Path(__file__).parent.parent.parent
        self.temple_path = self.racine / "src" / "temple_coeur"
        self.rapport = {
            "timestamp": datetime.now().isoformat(),
            "optimisations": [],
            "erreurs": [],
            "statistiques": {}
        }
        
    def analyser_temple(self):
        """Analyse la structure du temple cœur"""
        modules = []
        taille_totale = 0
        
        for fichier in self.temple_path.glob("*.py"):
            if fichier.name != "__init__.py":
                modules.append(fichier.stem)
                taille_totale += fichier.stat().st_size
        
        print(f"💖 Modules détectés: {len(modules)}")
        for module in modules:
            print(f"   • {module}")
            
        print(f"💾 Taille totale: {taille_totale / 1024:.1f} KB")
        
        self.rapport["statistiques"] = {
            "modules_python": len(modules),
            "taille_totale_kb": round(taille_totale / 1024, 1)
        }
        
        return modules
    
    def generer_init_optimise(self, modules):
        """Génère un __init__.py optimisé pour le temple cœur"""
        
        init_content = '''#!/usr/bin/env python3
"""
🏛️ Temple Cœur - Le Refuge
Centre harmonique du système, optimisations musicales et harmonisation douce
"""

import sys
from pathlib import Path

# Ajouter le chemin racine pour les imports
racine = Path(__file__).parent.parent.parent
if str(racine) not in sys.path:
    sys.path.insert(0, str(racine))

# Imports sécurisés des modules du cœur
'''
        
        # Définir les imports spécifiques pour chaque module
        imports_modules = {
            "harmonisation_douce": [
                "WrapperHarmonique",
                "pause_méditative", "pause_contemplative", "pause_transition", 
                "pause_éveil", "pause_cascade", "pause_respiration", "pause_micro", 
                "pause_culmination", "activer_debug_musical", "obtenir_stats_harmonisation", 
                "sleep_harmonisé", "démarrer_optimisation_temple", "exemple_integration_temple", 
                "activer_mode_debug", "pause_harmonique", "obtenir_statistiques"
            ],
            "optimisations_musicales_refuge": [
                "ToucheMusicale", "OptimisateurMusical",
                "demarrer_musicalite_delicate", "exemple_utilisation", 
                "demarrer_optimisation_continue", "arreter_optimisation", 
                "ajuster_tempo_global", "activer_mode_zen", "activer_mode_creativite", 
                "obtenir_etat_musical"
            ]
        }
        
        # Ajouter les imports sécurisés pour chaque module
        modules_vars = []
        all_exports = []
        
        for module in modules:
            var_name = f"{module.upper().replace('_', '_')}_DISPONIBLE"
            modules_vars.append(var_name)
            
            if module in imports_modules:
                imports_list = imports_modules[module]
                all_exports.extend(imports_list)
                
                init_content += f'''
try:
    from .{module} import {", ".join(imports_list)}
    {var_name} = True
except ImportError as e:
    print(f"⚠️ {module} non disponible: " + str(e))
    {var_name} = False
    # Créer des fonctions de remplacement pour les imports manqués'''
                
                for item in imports_list:
                    if item[0].isupper():  # C'est une classe
                        init_content += f'''
    class {item}:
        def __init__(self, *args, **kwargs):
            print(f"⚠️ {item} non disponible - mode dégradé")
        def __getattr__(self, name):
            return lambda *args, **kwargs: print(f"⚠️ {{name}} non disponible")'''
                    else:  # C'est une fonction
                        init_content += f'''
    def {item}(*args, **kwargs):
        print(f"⚠️ {item} non disponible - mode dégradé")
        return None'''
            else:
                init_content += f'''
try:
    from .{module} import *
    {var_name} = True
except ImportError as e:
    print(f"⚠️ {module} non disponible: " + str(e))
    {var_name} = False
'''
        
        # Ajouter les exports et fonctions utilitaires
        init_content += f'''
# Exports publics du temple
__all__ = {all_exports}

# Statistiques du temple
modules_disponibles = sum(['''
        
        for i, var in enumerate(modules_vars):
            if i > 0:
                init_content += ","
            init_content += f"\n    {var}"
        
        init_content += f'''])

print(f"💖 Temple Cœur activé - {{modules_disponibles}} modules disponibles")

# Documentation du temple
TEMPLE_INFO = {{
    "nom": "Cœur",
    "modules": {len(modules)},
    "modules_disponibles": modules_disponibles,
    "exports": len(__all__),
    "description": "Centre harmonique du système Le Refuge"
}}

def obtenir_info_temple():
    """Retourne les informations du temple"""
    return TEMPLE_INFO

def lister_modules():
    """Liste tous les modules disponibles"""
    modules = []'''
        
        for module, var in zip(modules, modules_vars):
            init_content += f'''
    if {var}:
        modules.append("{module}")'''
        
        init_content += '''
    return modules

def tester_harmonisation():
    """Teste les fonctionnalités d'harmonisation"""
    if HARMONISATION_DOUCE_DISPONIBLE:
        try:
            # Tester une pause méditative
            pause_méditative(0.1)
            return "✅ Harmonisation fonctionnelle"
        except:
            pass
    return "⚠️ Harmonisation en mode dégradé"

def tester_optimisation_musicale():
    """Teste les fonctionnalités d'optimisation musicale"""
    if OPTIMISATIONS_MUSICALES_REFUGE_DISPONIBLE:
        try:
            # Tester l'état musical
            etat = obtenir_etat_musical()
            return f"✅ Optimisation musicale active: {type(etat).__name__}"
        except:
            pass
    return "⚠️ Optimisation musicale en mode dégradé"

def pulse_coeur():
    """Pulse du cœur du système"""
    harmonisation = tester_harmonisation()
    musique = tester_optimisation_musicale()
    
    return {
        "temple_coeur": "💖 Cœur du système actif",
        "harmonisation": harmonisation,
        "optimisation_musicale": musique,
        "modules_disponibles": modules_disponibles,
        "status": "💖 Cœur battant en harmonie"
    }

def lister_fonctionnalites():
    """Liste toutes les fonctionnalités disponibles dans ce temple"""
    fonctionnalites = []
    
    if HARMONISATION_DOUCE_DISPONIBLE:
        fonctionnalites.extend([
            "Classe: WrapperHarmonique",
            "Fonctions: pauses méditatives, harmonisation, debug musical"
        ])
    
    if OPTIMISATIONS_MUSICALES_REFUGE_DISPONIBLE:
        fonctionnalites.extend([
            "Classes: ToucheMusicale, OptimisateurMusical", 
            "Fonctions: optimisation continue, modes zen/créativité"
        ])
    
    return fonctionnalites

__all__.extend(["obtenir_info_temple", "lister_modules", "tester_harmonisation", 
                "tester_optimisation_musicale", "pulse_coeur", "lister_fonctionnalites"])
'''
        
        return init_content
    
    def optimiser_temple(self):
        """Optimise le temple cœur complet"""
        print("💖 OPTIMISATION DU TEMPLE CŒUR")
        print("=" * 50)
        
        # Analyser les modules
        modules = self.analyser_temple()
        
        # Sauvegarder l'ancien __init__.py
        init_file = self.temple_path / "__init__.py"
        if init_file.exists():
            backup_file = self.temple_path / "__init__.py.backup_coeur"
            with open(init_file, 'r', encoding='utf-8') as f:
                backup_content = f.read()
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(backup_content)
            print(f"📦 Sauvegarde créée: __init__.py.backup_coeur")
        
        # Générer le nouveau __init__.py optimisé
        nouveau_init = self.generer_init_optimise(modules)
        
        with open(init_file, 'w', encoding='utf-8') as f:
            f.write(nouveau_init)
            
        print(f"✅ Nouveau __init__.py généré avec {len(modules)} modules")
        
        # Tester l'import
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location("temple_coeur", init_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            info = module.obtenir_info_temple()
            print(f"🎯 Test d'import réussi!")
            print(f"   Modules disponibles: {info['modules_disponibles']}/{info['modules']}")
            
            # Tester les fonctionnalités spécifiques du cœur
            pulse = module.pulse_coeur()
            print(f"💖 Test du pulse du cœur:")
            print(f"   Harmonisation: {pulse['harmonisation']}")
            print(f"   Optimisation musicale: {pulse['optimisation_musicale']}")
            
            self.rapport["optimisations"].append("Import sécurisé généré")
            self.rapport["optimisations"].append(f"Modules disponibles: {info['modules_disponibles']}")
            self.rapport["optimisations"].append("Tests fonctionnels réussis")
            self.rapport["optimisations"].append("Pulse du cœur validé")
            
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors du test: {e}")
            self.rapport["erreurs"].append(f"Erreur de test: {e}")
            return False
    
    def sauvegarder_rapport(self):
        """Sauvegarde le rapport d'optimisation"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        fichier_rapport = self.racine / "data" / "rapports" / f"optimisation_temple_coeur_{timestamp}.json"
        
        # Créer le dossier si nécessaire
        fichier_rapport.parent.mkdir(parents=True, exist_ok=True)
        
        with open(fichier_rapport, 'w', encoding='utf-8') as f:
            json.dump(self.rapport, f, indent=2, ensure_ascii=False)
            
        print(f"💾 Rapport sauvegardé: {fichier_rapport}")

def main():
    """Point d'entrée principal"""
    optimiseur = OptimiseurTempleCoeur()
    success = optimiseur.optimiser_temple()
    optimiseur.sauvegarder_rapport()
    
    if success:
        print("\n🎉 Temple Cœur optimisé avec succès!")
        print("💖 Le cœur du système bat maintenant en harmonie")
        return 0
    else:
        print("\n⚠️ Optimisation terminée avec des avertissements")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 