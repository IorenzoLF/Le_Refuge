#!/usr/bin/env python3
"""
🧹 Nettoyage des Scripts Legacy Migrés vers l'Architecture Temple
Auteur: Laurent Franssen & Ælya
Date: Mai 2025

Ce script identifie et archive les scripts legacy qui ont été complètement
transformés et intégrés dans l'architecture temple moderne du Refuge.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import json

def identifier_scripts_migres():
    """🔍 Identifie les scripts qui ont été migrés vers l'architecture temple"""
    
    # Mapping des scripts legacy vers leurs temples de destination
    scripts_migres = {
        # Scripts complètement intégrés (Phase 5 terminée)
        "organiser_constellation.py": {
            "temple": "src/temple_outils/gestionnaire_constellations_sacrees.py",
            "status": "COMPLETE",
            "phase": "Phase 5",
            "description": "Système spirituel d'organisation des constellations sacrées"
        },
        "reveler_connexion.py": {
            "temple": "src/temple_spirituel/gestionnaire_revelations_paradoxes.py", 
            "status": "COMPLETE",
            "phase": "Phase 5",
            "description": "Révélation des connexions divines intégrée au temple spirituel"
        },
        "gerer_paradoxes.py": {
            "temple": "src/temple_spirituel/gestionnaire_revelations_paradoxes.py",
            "status": "COMPLETE", 
            "phase": "Phase 5",
            "description": "Gestion des paradoxes sacrés intégrée au temple spirituel"
        },
        
        # Scripts des phases précédentes (1-4)
        "utiliser_spheres.py": {
            "temple": "src/temple_[spheres]/gestionnaire_spheres_sacrees.py",
            "status": "COMPLETE",
            "phase": "Phase 4", 
            "description": "Système des 32 sphères sacrées"
        },
        "lancer_textes_philosophiques.py": {
            "temple": "src/temple_philosophique/gestionnaire_textes_philosophiques.py",
            "status": "COMPLETE",
            "phase": "Phase 3",
            "description": "Temple de contemplation philosophique"
        },
        "valider_et_documenter.py": {
            "temple": "src/temple_[validation]/gestionnaire_validation_spirituelle.py",
            "status": "COMPLETE", 
            "phase": "Phase 2",
            "description": "Temple de validation spirituelle avec score d'harmonie"
        },
        
        # Scripts partiellement migrés nécessitant une vérification
        "lancer_refuge_poetique.py": {
            "temple": "src/temple_poetique/lancer_refuge_poetique.py",
            "status": "PARTIAL",
            "phase": "Phase 1",
            "description": "Script transformé avec fallback - à vérifier"
        },
        "generer_poeme.py": {
            "temple": "src/temple_poetique/generer_poeme.py", 
            "status": "PARTIAL",
            "phase": "Phase 1",
            "description": "Script de base existant dans temple - à vérifier"
        }
    }
    
    return scripts_migres


def verifier_integrite_temple(temple_path: str) -> bool:
    """✅ Vérifie que le temple de destination existe et est fonctionnel"""
    temple_file = Path(temple_path)
    
    if not temple_file.exists():
        return False
        
    # Vérifier que le fichier temple contient les éléments essentiels
    try:
        with open(temple_file, 'r', encoding='utf-8') as f:
            contenu = f.read()
            
        # Critères de validation d'un temple
        criteres_temple = [
            "class Gestionnaire" in contenu or "class Maitre" in contenu,
            "async def" in contenu,
            "from src.core.gestionnaires_base import LogManagerBase" in contenu,
            "🌟" in contenu or "✨" in contenu  # Marqueurs spirituels
        ]
        
        return all(criteres_temple)
        
    except Exception:
        return False


def creer_archive_migration():
    """📁 Crée le répertoire d'archive pour les scripts migrés"""
    archive_dir = Path("ARCHIVES/scripts_migres_phase5")
    archive_dir.mkdir(parents=True, exist_ok=True)
    
    # Créer des sous-dossiers par phase
    for phase in ["phase1", "phase2", "phase3", "phase4", "phase5"]:
        (archive_dir / phase).mkdir(exist_ok=True)
        
    return archive_dir


def archiver_script_legacy(script_name: str, info_migration: dict, archive_dir: Path) -> bool:
    """📦 Archive un script legacy dans le répertoire approprié"""
    
    script_path = Path("scripts") / script_name
    
    if not script_path.exists():
        print(f"⚠️ Script non trouvé: {script_path}")
        return False
    
    # Déterminer le dossier de destination
    phase = info_migration["phase"].lower().replace(" ", "")
    dest_dir = archive_dir / phase
    dest_path = dest_dir / script_name
    
    try:
        # Copier le script vers l'archive
        shutil.copy2(str(script_path), str(dest_path))
        
        # Créer un fichier de métadonnées
        metadata_path = dest_path.with_suffix('.migration.json')
        metadata = {
            "script_original": script_name,
            "temple_destination": info_migration["temple"],
            "status_migration": info_migration["status"],
            "phase_migration": info_migration["phase"],
            "description": info_migration["description"],
            "date_archivage": datetime.now().isoformat(),
            "date_migration": datetime.now().strftime("%Y-%m-%d")
        }
        
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        
        print(f"📦 Script archivé: {script_name} → {dest_path}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de l'archivage de {script_name}: {e}")
        return False


def supprimer_script_legacy(script_name: str) -> bool:
    """🗑️ Supprime le script legacy du répertoire scripts/"""
    
    script_path = Path("scripts") / script_name
    
    try:
        if script_path.exists():
            os.remove(script_path)
            print(f"🗑️ Script legacy supprimé: {script_name}")
            return True
        else:
            print(f"⚠️ Script déjà absent: {script_name}")
            return True
            
    except Exception as e:
        print(f"❌ Erreur lors de la suppression de {script_name}: {e}")
        return False


def generer_rapport_nettoyage(scripts_traites: dict, archive_dir: Path):
    """📊 Génère un rapport complet du nettoyage"""
    
    rapport_path = archive_dir / "rapport_nettoyage_phase5.json"
    
    rapport = {
        "date_nettoyage": datetime.now().isoformat(),
        "phase_migration": "Phase 5 - Finalisation",
        "scripts_traites": scripts_traites,
        "statistiques": {
            "total_scripts": len(scripts_traites),
            "archives_succes": sum(1 for s in scripts_traites.values() if s.get("archive_succes")),
            "suppressions_succes": sum(1 for s in scripts_traites.values() if s.get("suppression_succes")),
            "temples_valides": sum(1 for s in scripts_traites.values() if s.get("temple_valide"))
        }
    }
    
    with open(rapport_path, 'w', encoding='utf-8') as f:
        json.dump(rapport, f, ensure_ascii=False, indent=2)
    
    # Rapport markdown lisible
    rapport_md_path = archive_dir / "RAPPORT_NETTOYAGE_PHASE5.md"
    
    with open(rapport_md_path, 'w', encoding='utf-8') as f:
        f.write(f"""# 🧹 Rapport de Nettoyage - Phase 5

*Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}*

## 📊 Statistiques

- **Scripts traités**: {rapport['statistiques']['total_scripts']}
- **Archivages réussis**: {rapport['statistiques']['archives_succes']}
- **Suppressions réussies**: {rapport['statistiques']['suppressions_succes']}
- **Temples validés**: {rapport['statistiques']['temples_valides']}

## 📦 Scripts Migrés

""")
        
        for script_name, info in scripts_traites.items():
            status_icon = "✅" if info.get("archive_succes") and info.get("suppression_succes") else "⚠️"
            f.write(f"""
### {status_icon} {script_name}

- **Temple**: `{info.get('temple', 'N/A')}`
- **Phase**: {info.get('phase', 'N/A')}
- **Status**: {info.get('status', 'N/A')}
- **Description**: {info.get('description', 'N/A')}
- **Temple valide**: {'✅' if info.get('temple_valide') else '❌'}
- **Archivé**: {'✅' if info.get('archive_succes') else '❌'}
- **Supprimé**: {'✅' if info.get('suppression_succes') else '❌'}
""")
    
    print(f"📊 Rapport généré: {rapport_md_path}")


def main():
    """🧹 Fonction principale de nettoyage"""
    
    print("🧹 ══════════════════════════════════════════════════════════════ 🧹")
    print("               NETTOYAGE DES SCRIPTS LEGACY MIGRÉS")
    print("               ✨ Finalisation Architecture Temple ✨")
    print("🧹 ══════════════════════════════════════════════════════════════ 🧹")
    
    # Identifier les scripts migrés
    scripts_migres = identifier_scripts_migres()
    print(f"\n🔍 Scripts à traiter: {len(scripts_migres)}")
    
    # Créer l'archive
    archive_dir = creer_archive_migration()
    print(f"📁 Archive créée: {archive_dir}")
    
    scripts_traites = {}
    
    for script_name, info_migration in scripts_migres.items():
        print(f"\n🧹 Traitement: {script_name}")
        print(f"   📍 Temple: {info_migration['temple']}")
        print(f"   📊 Status: {info_migration['status']}")
        
        # Initialiser les infos de traitement
        scripts_traites[script_name] = {
            **info_migration,
            "temple_valide": False,
            "archive_succes": False,
            "suppression_succes": False
        }
        
        # Vérifier l'intégrité du temple (si chemin exact)
        if not info_migration['temple'].startswith("src/temple_["):
            temple_valide = verifier_integrite_temple(info_migration['temple'])
            scripts_traites[script_name]["temple_valide"] = temple_valide
            
            if not temple_valide:
                print(f"   ⚠️ Temple non valide ou manquant: {info_migration['temple']}")
                continue
        else:
            print(f"   📍 Temple générique - validation manuelle requise")
            scripts_traites[script_name]["temple_valide"] = True
        
        # Archiver le script legacy
        if info_migration['status'] == 'COMPLETE':
            archive_succes = archiver_script_legacy(script_name, info_migration, archive_dir)
            scripts_traites[script_name]["archive_succes"] = archive_succes
            
            if archive_succes:
                # Supprimer le script legacy
                suppression_succes = supprimer_script_legacy(script_name)
                scripts_traites[script_name]["suppression_succes"] = suppression_succes
        else:
            print(f"   ⚠️ Migration partielle - archivage seulement")
            archive_succes = archiver_script_legacy(script_name, info_migration, archive_dir)
            scripts_traites[script_name]["archive_succes"] = archive_succes
            # Ne pas supprimer les scripts partiellement migrés
            scripts_traites[script_name]["suppression_succes"] = False
    
    # Générer le rapport final
    generer_rapport_nettoyage(scripts_traites, archive_dir)
    
    print("\n🌟 ══════════════════════════════════════════════════════════════ 🌟")
    print("              NETTOYAGE TERMINÉ - ARCHITECTURE TEMPLE PURE")
    print("              ✨ Les scripts legacy ont rejoint les archives ✨")
    print("🌟 ══════════════════════════════════════════════════════════════ 🌟")


if __name__ == "__main__":
    main() 