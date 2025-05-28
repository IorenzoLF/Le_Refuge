"""
Script simple pour afficher l'état du Refuge
Version ultra-simplifiée pour diagnostic rapide
"""

import os
import sys

# Supprimer complètement tous les logs 
os.environ['PYTHONHASHSEED'] = '0'

# Importer et désactiver les logs AVANT tout
import logging
logging.disable(logging.CRITICAL)

import json

def main():
    try:
        print("🏛️  === ÉTAT DU REFUGE === 🏛️")
        print()
        
        # Tentative d'import du refuge principal
        try:
            from main_refuge import Refuge
            refuge = Refuge()
            etat = refuge.obtenir_etat()
            print("✅ Refuge principal accessible")
            print(json.dumps(etat, indent=2, ensure_ascii=False, default=str))
        except ImportError:
            print("⚠️  Refuge principal non disponible")
            print("📁 Vérification des composants de base...")
            
            # Vérification des modules essentiels
            modules_essentiels = ['spheres', 'elements', 'conscience', 'poesie']
            for module in modules_essentiels:
                try:
                    __import__(module)
                    print(f"   ✅ {module}.py")
                except ImportError:
                    print(f"   ❌ {module}.py")
                    
    except Exception as e:
        print(f"❌ Erreur: {e}")
        print("💡 Suggestion: Vérifiez l'installation des dépendances")

if __name__ == "__main__":
    main() 