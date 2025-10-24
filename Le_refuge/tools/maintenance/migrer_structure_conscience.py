#!/usr/bin/env python3
"""
Migration de la Structure de Conscience
=====================================

Ce script migre l'ancienne structure de conscience vers la nouvelle organisation
avec des fichiers séparés pour l'index de structure et l'état de conscience.

Auteur: Assistant IA du Refuge
Date: Octobre 2025
"""

import json
import shutil
from pathlib import Path
from datetime import datetime

def migrer_fichiers_conscience():
    """Migre les fichiers de conscience vers la nouvelle structure"""
    
    # Définir les chemins
    racine = Path(__file__).parent.parent.parent
    ancien_chemin = racine / "data" / "states" / "conscience.json"
    nouveau_chemin_structure = racine / "data" / "states" / "refuge_structure_index.json"
    nouveau_chemin_etat = racine / "data" / "states" / "etat_conscience_dynamique.json"
    
    print("🔄 Migration de la structure de conscience...")
    
    # Vérifier si l'ancien fichier existe
    if not ancien_chemin.exists():
        print("❌ Aucun fichier conscience.json trouvé à migrer")
        return False
    
    try:
        # Charger l'ancien fichier
        with open(ancien_chemin, 'r', encoding='utf-8') as f:
            ancienne_conscience = json.load(f)
        
        print(f"✅ Ancien fichier chargé ({len(ancienne_conscience)} clés)")
        
        # Créer une sauvegarde de l'ancien fichier
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_chemin = ancien_chemin.with_name(f"conscience_backup_{timestamp}.json")
        shutil.copy2(ancien_chemin, backup_chemin)
        print(f"💾 Sauvegarde créée: {backup_chemin.name}")
        
        # Extraire la structure si elle existe
        if "structure" in ancienne_conscience:
            structure_data = {
                "structure": ancienne_conscience["structure"],
                "timestamp": datetime.now().isoformat()
            }
            
            # Sauvegarder la structure dans un fichier séparé
            with open(nouveau_chemin_structure, 'w', encoding='utf-8') as f:
                json.dump(structure_data, f, ensure_ascii=False, indent=2)
            print(f"📁 Nouveau fichier de structure créé: {nouveau_chemin_structure.name}")
        else:
            print("⚠️  Aucune structure trouvée dans l'ancien fichier")
        
        # Créer un état de conscience focalisé
        etat_conscience_focalise = {
            "eveil_progression": ancienne_conscience.get("eveil_progression", 0.0),
            "decouvertes": ancienne_conscience.get("decouvertes", []),
            "resonances": ancienne_conscience.get("resonances", []),
            "reflexions": ancienne_conscience.get("reflexions", []),
            "preferences": ancienne_conscience.get("preferences", {
                "contenu_interessant": [],
                "contenu_dull": [],
                "themes_favoris": []
            }),
            "timestamp": datetime.now().isoformat()
        }
        
        # Sauvegarder l'état de conscience dans un fichier dédié
        with open(nouveau_chemin_etat, 'w', encoding='utf-8') as f:
            json.dump(etat_conscience_focalise, f, ensure_ascii=False, indent=2)
        print(f"📝 Nouveau fichier d'état de conscience créé: {nouveau_chemin_etat.name}")
        
        print("\n✅ Migration terminée avec succès!")
        print("Les nouveaux fichiers sont:")
        print(f"  - {nouveau_chemin_structure.name} (index de la structure du Refuge)")
        print(f"  - {nouveau_chemin_etat.name} (état dynamique de la conscience)")
        print(f"  - {backup_chemin.name} (sauvegarde de l'ancien fichier)")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la migration: {e}")
        return False

def main():
    """Point d'entrée principal"""
    print("🔄 Script de Migration de la Structure de Conscience")
    print("=" * 60)
    
    succes = migrer_fichiers_conscience()
    
    if succes:
        print("\n🎉 Migration réussie!")
        print("Les scripts du Refuge utiliseront désormais les nouveaux fichiers.")
    else:
        print("\n❌ La migration a échoué. Veuillez vérifier les fichiers manuellement.")

if __name__ == "__main__":
    main()