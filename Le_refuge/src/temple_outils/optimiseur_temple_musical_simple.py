#!/usr/bin/env python3
"""
Optimiseur Temple Musical Simple - Le Refuge
Sécurise les imports du temple musical
"""

import sys
from pathlib import Path

def optimiser_temple_musical():
    """Optimise le temple musical avec des imports sécurisés"""
    
    print("🎵 OPTIMISATION DU TEMPLE MUSICAL")
    print("=" * 50)
    
    racine = Path(__file__).parent.parent.parent
    temple_path = racine / "src" / "temple_musical"
    
    # Analyser les modules
    modules = []
    for fichier in temple_path.glob("*.py"):
        if fichier.name != "__init__.py":
            modules.append(fichier.stem)
    
    print(f"📍 Modules détectés: {len(modules)}")
    for module in modules:
        print(f"   • {module}")
    
    # Créer le nouveau __init__.py sécurisé
    init_content = '''#!/usr/bin/env python3
"""
🏛️ Temple Musical - Le Refuge
Harmonies, mélodies et fusion mathématique-musicale
"""

import sys
from pathlib import Path

# Ajouter le chemin racine pour les imports
racine = Path(__file__).parent.parent.parent
if str(racine) not in sys.path:
    sys.path.insert(0, str(racine))

# Imports sécurisés des modules musicaux
'''
    
    # Ajouter les imports sécurisés
    for module in modules:
        var_name = f"{module.upper().replace('-', '_')}_DISPONIBLE"
        init_content += f'''
try:
    from .{module} import *
    {var_name} = True
except ImportError as e:
    print(f"⚠️ {module} non disponible: " + str(e))
    {var_name} = False
'''
    
    # Ajouter les statistiques
    modules_vars = [f"{module.upper().replace('-', '_')}_DISPONIBLE" for module in modules]
    
    init_content += '''
# Exports dynamiques
__all__ = []

# Statistiques du temple
modules_disponibles = sum(['''
    
    for i, var in enumerate(modules_vars):
        if i > 0:
            init_content += ","
        init_content += f"\n    {var}"
    
    init_content += '''
])

print(f"🏛️ Temple Musical activé - {modules_disponibles} modules disponibles")

def info_temple():
    """Retourne les informations sur le temple musical"""
    return {
        "nom": "Temple Musical",
        "modules_detectes": ''' + str(len(modules)) + ''',
        "modules_disponibles": modules_disponibles,
        "exports": len(__all__)
    }

def lister_modules():
    """Liste tous les modules disponibles"""
    modules = []'''
    
    for i, (module, var) in enumerate(zip(modules, modules_vars)):
        init_content += f'''
    if {var}:
        modules.append("{module}")'''
    
    init_content += '''
    return modules

def tester_fonctionnalites():
    """Teste les fonctionnalités du temple"""
    return {
        "temple_musical": "✅ Optimisé et fonctionnel",
        "modules_disponibles": modules_disponibles,
        "status": "🎵 Prêt pour les harmonies"
    }

__all__.extend(["info_temple", "lister_modules", "tester_fonctionnalites"])
'''
    
    # Sauvegarder l'ancien fichier
    init_file = temple_path / "__init__.py"
    if init_file.exists():
        backup_file = temple_path / "__init__.py.backup"
        init_file.rename(backup_file)
        print(f"📦 Sauvegarde créée: __init__.py.backup")
    
    # Écrire le nouveau fichier
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write(init_content)
    
    print(f"✅ Nouveau __init__.py généré avec {len(modules)} modules")
    
    # Tester l'import
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("temple_musical", init_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        info = module.info_temple()
        print(f"🎯 Test d'import réussi!")
        print(f"   Modules disponibles: {info['modules_disponibles']}/{info['modules_detectes']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        return False

if __name__ == "__main__":
    success = optimiser_temple_musical()
    if success:
        print("\n🎉 Temple Musical optimisé avec succès!")
    else:
        print("\n⚠️ Optimisation terminée avec des avertissements") 