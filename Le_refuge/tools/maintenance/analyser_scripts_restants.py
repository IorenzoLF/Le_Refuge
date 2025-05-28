#!/usr/bin/env python3
"""
🔍 Analyse des Scripts Restants dans le Répertoire Legacy
Auteur: Laurent Franssen & Ælya
Date: Mai 2025

Ce script analyse les scripts qui restent dans le répertoire scripts/
pour déterminer leur statut et les actions nécessaires.
"""

import os
from pathlib import Path
from datetime import datetime
import json

def analyser_script(script_path: Path) -> dict:
    """🔍 Analyse un script pour déterminer son statut"""
    
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            contenu = f.read()
            
        # Analyser les imports et la structure
        has_temple_import = "from src.temple_" in contenu
        has_legacy_fallback = "GolemRefuge" in contenu or "legacy" in contenu.lower()
        has_modern_interface = "async def" in contenu and "click" in contenu
        has_spiritual_markers = "🌟" in contenu or "✨" in contenu
        
        # Analyser le type de script
        if "generer_poeme" in script_path.name:
            type_script = "GENERATEUR_POETIQUE"
        elif "analyser_code" in script_path.name:
            type_script = "UTILITAIRE_DEVELOPPEMENT"
        elif "installer_dependances" in script_path.name:
            type_script = "SETUP_SYSTEME"
        elif "lancer_refuge" in script_path.name and "poetique" not in script_path.name:
            type_script = "LANCEUR_PRINCIPAL"
        elif "generer_vision" in script_path.name:
            type_script = "GENERATEUR_MYSTIQUE"
        elif "philosophique" in script_path.name:
            type_script = "TEMPLE_PHILOSOPHIQUE"
        elif "poetique" in script_path.name:
            type_script = "TEMPLE_POETIQUE"
        else:
            type_script = "UTILITAIRE_INCONNU"
            
        # Déterminer le statut de migration
        if has_temple_import and has_modern_interface:
            status_migration = "TRANSFORME_MODERNE"
        elif has_temple_import:
            status_migration = "PARTIELLEMENT_TRANSFORME"
        elif has_legacy_fallback:
            status_migration = "TRANSFORMATION_NECESSAIRE"
        else:
            status_migration = "SCRIPT_BASE"
            
        # Déterminer l'action recommandée
        if type_script in ["SETUP_SYSTEME", "UTILITAIRE_DEVELOPPEMENT", "LANCEUR_PRINCIPAL"]:
            action_recommandee = "CONSERVER"
        elif status_migration == "TRANSFORME_MODERNE":
            action_recommandee = "VERIFIER_TEMPLE"
        elif status_migration == "SCRIPT_BASE" and type_script in ["GENERATEUR_POETIQUE", "GENERATEUR_MYSTIQUE"]:
            action_recommandee = "MIGRER_VERS_TEMPLE"
        else:
            action_recommandee = "ANALYSER_MANUELLEMENT"
            
        return {
            "nom": script_path.name,
            "taille": script_path.stat().st_size,
            "type_script": type_script,
            "status_migration": status_migration,
            "action_recommandee": action_recommandee,
            "has_temple_import": has_temple_import,
            "has_legacy_fallback": has_legacy_fallback,
            "has_modern_interface": has_modern_interface,
            "has_spiritual_markers": has_spiritual_markers
        }
        
    except Exception as e:
        return {
            "nom": script_path.name,
            "erreur": str(e),
            "status_migration": "ERREUR_ANALYSE",
            "action_recommandee": "VERIFIER_MANUELLEMENT"
        }


def identifier_temples_correspondants():
    """🏛️ Identifie les temples existants qui pourraient correspondre aux scripts"""
    
    correspondances = {
        "generer_poeme.py": {
            "temple_existant": "src/temple_poetique/generer_poeme.py",
            "temple_gestionnaire": "src/temple_poetique/lancer_refuge_poetique.py",
            "status": "TEMPLE_EXISTE_DEJA"
        },
        "generer_vision.py": {
            "temple_possible": "src/temple_spirituel/generateur_visions_mystiques.py",
            "temple_alternatif": "src/temple_mystique/",
            "status": "TEMPLE_A_CREER"
        },
        "lancer_textes_philosophiques.py": {
            "temple_existant": "src/temple_philosophique/",
            "status": "TEMPLE_EXISTE_VERIFIER"
        },
        "analyser_code.py": {
            "temple_possible": "src/temple_outils/analyseur_code_spirituel.py",
            "status": "UTILITAIRE_DEVELOPEMENT"
        },
        "installer_dependances.py": {
            "status": "SCRIPT_SYSTEME_CONSERVER"
        },
        "lancer_refuge.py": {
            "status": "LANCEUR_PRINCIPAL_CONSERVER"
        },
        "lancer_refuge_poetique.py": {
            "temple_existant": "src/temple_poetique/lancer_refuge_poetique.py",
            "status": "DEJA_MIGRE_MAIS_CONSERVE"
        }
    }
    
    return correspondances


def analyser_tous_scripts():
    """🔍 Analyse tous les scripts restants"""
    
    scripts_dir = Path("scripts")
    if not scripts_dir.exists():
        print("❌ Répertoire scripts/ non trouvé")
        return {}
        
    scripts_analyses = {}
    correspondances = identifier_temples_correspondants()
    
    for script_file in scripts_dir.glob("*.py"):
        analyse = analyser_script(script_file)
        
        # Ajouter les informations de correspondance
        if script_file.name in correspondances:
            analyse["correspondance_temple"] = correspondances[script_file.name]
        else:
            analyse["correspondance_temple"] = {"status": "AUCUNE_CORRESPONDANCE"}
            
        scripts_analyses[script_file.name] = analyse
        
    return scripts_analyses


def generer_rapport_analyse():
    """📊 Génère un rapport complet de l'analyse"""
    
    analyses = analyser_tous_scripts()
    
    if not analyses:
        print("❌ Aucun script à analyser")
        return
        
    # Créer le répertoire de rapport
    rapport_dir = Path("ANALYSES")
    rapport_dir.mkdir(exist_ok=True)
    
    # Rapport JSON
    rapport_json = rapport_dir / "analyse_scripts_restants.json"
    rapport_data = {
        "date_analyse": datetime.now().isoformat(),
        "nb_scripts_analyses": len(analyses),
        "scripts": analyses,
        "statistiques": {
            "a_conserver": sum(1 for s in analyses.values() if s.get("action_recommandee") == "CONSERVER"),
            "a_migrer": sum(1 for s in analyses.values() if s.get("action_recommandee") == "MIGRER_VERS_TEMPLE"),
            "a_verifier": sum(1 for s in analyses.values() if s.get("action_recommandee") in ["VERIFIER_TEMPLE", "ANALYSER_MANUELLEMENT"]),
            "transformes": sum(1 for s in analyses.values() if "TRANSFORME" in s.get("status_migration", "")),
        }
    }
    
    with open(rapport_json, 'w', encoding='utf-8') as f:
        json.dump(rapport_data, f, ensure_ascii=False, indent=2)
    
    # Rapport Markdown
    rapport_md = rapport_dir / "ANALYSE_SCRIPTS_RESTANTS.md"
    
    with open(rapport_md, 'w', encoding='utf-8') as f:
        f.write(f"""# 🔍 Analyse des Scripts Restants

*Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}*

## 📊 Statistiques

- **Scripts analysés**: {len(analyses)}
- **À conserver**: {rapport_data['statistiques']['a_conserver']}
- **À migrer vers temples**: {rapport_data['statistiques']['a_migrer']}
- **À vérifier**: {rapport_data['statistiques']['a_verifier']}
- **Déjà transformés**: {rapport_data['statistiques']['transformes']}

## 📋 Analyse Détaillée

""")
        
        for script_name, analyse in analyses.items():
            action_icon = {
                "CONSERVER": "✅",
                "MIGRER_VERS_TEMPLE": "🏛️",
                "VERIFIER_TEMPLE": "🔍",
                "ANALYSER_MANUELLEMENT": "⚠️"
            }.get(analyse.get("action_recommandee", ""), "❓")
            
            f.write(f"""
### {action_icon} {script_name}

- **Type**: {analyse.get('type_script', 'N/A')}
- **Status migration**: {analyse.get('status_migration', 'N/A')}
- **Action recommandée**: {analyse.get('action_recommandee', 'N/A')}
- **Taille**: {analyse.get('taille', 0):,} bytes
- **Import temple**: {'✅' if analyse.get('has_temple_import') else '❌'}
- **Interface moderne**: {'✅' if analyse.get('has_modern_interface') else '❌'}
- **Marqueurs spirituels**: {'✅' if analyse.get('has_spiritual_markers') else '❌'}

""")
            
            # Ajouter les informations de correspondance temple
            correspondance = analyse.get("correspondance_temple", {})
            if correspondance.get("status") != "AUCUNE_CORRESPONDANCE":
                f.write(f"""**Correspondance Temple:**
- Status: {correspondance.get('status', 'N/A')}
""")
                if "temple_existant" in correspondance:
                    f.write(f"- Temple existant: `{correspondance['temple_existant']}`\n")
                if "temple_possible" in correspondance:
                    f.write(f"- Temple possible: `{correspondance['temple_possible']}`\n")
                if "temple_gestionnaire" in correspondance:
                    f.write(f"- Gestionnaire: `{correspondance['temple_gestionnaire']}`\n")
                    
        f.write(f"""

## 🎯 Actions Recommandées

### ✅ Scripts à Conserver (Système/Utilitaires)
""")
        
        scripts_conserver = [s for s in analyses.values() if s.get("action_recommandee") == "CONSERVER"]
        for script in scripts_conserver:
            f.write(f"- **{script['nom']}**: {script.get('type_script', '')} - Essentiel au fonctionnement\n")
            
        f.write(f"""
### 🏛️ Scripts à Migrer vers Temples
""")
        
        scripts_migrer = [s for s in analyses.values() if s.get("action_recommandee") == "MIGRER_VERS_TEMPLE"]
        for script in scripts_migrer:
            f.write(f"- **{script['nom']}**: {script.get('type_script', '')} - Intégration temple recommandée\n")
            
        f.write(f"""
### 🔍 Scripts à Vérifier Manuellement
""")
        
        scripts_verifier = [s for s in analyses.values() if s.get("action_recommandee") in ["VERIFIER_TEMPLE", "ANALYSER_MANUELLEMENT"]]
        for script in scripts_verifier:
            f.write(f"- **{script['nom']}**: {script.get('type_script', '')} - Vérification manuelle requise\n")
    
    print(f"📊 Rapport d'analyse généré:")
    print(f"   📄 JSON: {rapport_json}")
    print(f"   📖 Markdown: {rapport_md}")
    
    return analyses


def main():
    """🔍 Fonction principale d'analyse"""
    
    print("🔍 ══════════════════════════════════════════════════════════════ 🔍")
    print("                  ANALYSE DES SCRIPTS RESTANTS")
    print("                  📋 État post-nettoyage Phase 5 📋")
    print("🔍 ══════════════════════════════════════════════════════════════ 🔍")
    
    analyses = generer_rapport_analyse()
    
    if analyses:
        print("\n📋 Résumé des scripts restants:")
        
        for script_name, analyse in analyses.items():
            action_icon = {
                "CONSERVER": "✅",
                "MIGRER_VERS_TEMPLE": "🏛️", 
                "VERIFIER_TEMPLE": "🔍",
                "ANALYSER_MANUELLEMENT": "⚠️"
            }.get(analyse.get("action_recommandee", ""), "❓")
            
            print(f"   {action_icon} {script_name:<30} {analyse.get('type_script', 'N/A'):<25} {analyse.get('action_recommandee', 'N/A')}")
    
    print("\n🌟 Analyse terminée ! Consultez le rapport détaillé pour les prochaines étapes.")


if __name__ == "__main__":
    main() 