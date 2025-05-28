#!/usr/bin/env python3
"""
🔍 Audit Post-Migration Intelligent
Audit qui reconnaît les migrations réussies et se concentre sur les vrais problèmes
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict

class AuditPostMigration:
    """Audit intelligent post-migration"""
    
    def __init__(self):
        self.migrations_reussies = {
            # Migrations config réussies
            'config_vers_configuration': [
                'from .config import',
                'from .configuration import',
                'from src.core.configuration import'
            ],
            # Autres migrations à ajouter
            'logger_vers_core': [
                'from logger import',
                'from src.core.logger import'
            ]
        }
        
        self.problemes_reels = []
        self.migrations_detectees = []
        self.faux_positifs = []
        
    def analyser_fichier(self, chemin_fichier: Path) -> Dict:
        """Analyse un fichier en tenant compte des migrations"""
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
                
            lignes = contenu.split('\n')
            problemes_fichier = []
            migrations_fichier = []
            
            for i, ligne in enumerate(lignes, 1):
                # Vérifier les TODOs (vrais problèmes)
                if 'TODO' in ligne and not self._est_todo_migration(ligne):
                    problemes_fichier.append({
                        'ligne': i,
                        'contenu': ligne.strip(),
                        'type': 'todo_implementation'
                    })
                
                # Vérifier les imports problématiques
                if 'import' in ligne:
                    statut_import = self._analyser_import(ligne)
                    if statut_import['type'] == 'probleme':
                        problemes_fichier.append({
                            'ligne': i,
                            'contenu': ligne.strip(),
                            'type': 'import_casse'
                        })
                    elif statut_import['type'] == 'migration_reussie':
                        migrations_fichier.append({
                            'ligne': i,
                            'contenu': ligne.strip(),
                            'migration': statut_import['migration']
                        })
                        
            return {
                'fichier': str(chemin_fichier),
                'problemes_reels': problemes_fichier,
                'migrations_reussies': migrations_fichier,
                'statut': 'ok' if not problemes_fichier else 'problemes'
            }
            
        except Exception as e:
            return {
                'fichier': str(chemin_fichier),
                'erreur': str(e),
                'statut': 'erreur'
            }
    
    def _analyser_import(self, ligne: str) -> Dict:
        """Analyse une ligne d'import"""
        ligne_clean = ligne.strip()
        
        # Imports vers configuration (migration réussie)
        if any(pattern in ligne_clean for pattern in [
            'from .configuration import',
            'from src.core.configuration import'
        ]):
            return {
                'type': 'migration_reussie',
                'migration': 'config_vers_configuration'
            }
        
        # Imports vers logger (migration réussie)  
        if 'from src.core.logger import' in ligne_clean:
            return {
                'type': 'migration_reussie',
                'migration': 'logger_vers_core'
            }
            
        # Imports cassés (vrais problèmes)
        imports_casses = [
            'from config import',  # Ancien pattern non migré
            'from logger import',  # Ancien pattern non migré
            'from elements_sacres import',  # Module legacy
            'from definition import',  # Module manquant
        ]
        
        if any(pattern in ligne_clean for pattern in imports_casses):
            return {
                'type': 'probleme',
                'pattern': next(p for p in imports_casses if p in ligne_clean)
            }
            
        return {'type': 'ok'}
    
    def _est_todo_migration(self, ligne: str) -> bool:
        """Vérifie si un TODO concerne une migration (à ignorer)"""
        todo_migrations = [
            'TODO: Migrer',
            'TODO: Ces imports devront être ajustés',
            'TODO: DOSSIERS_REQUIS à migrer'
        ]
        return any(pattern in ligne for pattern in todo_migrations)
    
    def scanner_projet(self, racine: str = ".") -> Dict:
        """Scanne le projet avec intelligence post-migration"""
        print("🔍 Audit Post-Migration - Soul Temple")
        print("✨ Reconnaissance des migrations réussies\n")
        
        racine_path = Path(racine)
        fichiers_python = list(racine_path.rglob("*.py"))
        
        # Exclusions intelligentes
        exclusions = [
            'audit_simple.py',
            'audit_dependances.py', 
            'audit_post_migration.py',
            'analyser_config_references.py',
            '.venv',
            '__pycache__',
            'ARCHIVES'
        ]
        
        fichiers_filtres = [
            f for f in fichiers_python 
            if not any(excl in str(f) for excl in exclusions)
        ]
        
        print(f"📁 Analyse de {len(fichiers_filtres)} fichiers Python...")
        
        resultats = {
            'metadata': {
                'total_fichiers': len(fichiers_filtres),
                'migrations_reconnues': list(self.migrations_reussies.keys())
            },
            'fichiers': [],
            'resume': {
                'problemes_reels': 0,
                'migrations_reussies': 0,
                'fichiers_ok': 0,
                'fichiers_problemes': 0
            }
        }
        
        for fichier in fichiers_filtres:
            analyse = self.analyser_fichier(fichier)
            resultats['fichiers'].append(analyse)
            
            if analyse['statut'] == 'ok':
                resultats['resume']['fichiers_ok'] += 1
            elif analyse['statut'] == 'problemes':
                resultats['resume']['fichiers_problemes'] += 1
                resultats['resume']['problemes_reels'] += len(analyse['problemes_reels'])
            
            if 'migrations_reussies' in analyse:
                resultats['resume']['migrations_reussies'] += len(analyse['migrations_reussies'])
        
        self._afficher_resume(resultats['resume'])
        self._sauvegarder_rapport(resultats)
        
        return resultats
    
    def _afficher_resume(self, resume: Dict):
        """Affiche le résumé de l'audit"""
        print("\n🎯 ═══════════════════════════════════════════════════════")
        print("           RÉSUMÉ AUDIT POST-MIGRATION")
        print("🎯 ═══════════════════════════════════════════════════════")
        
        print(f"\n📊 Vue d'ensemble:")
        print(f"   ✅ Fichiers OK: {resume['fichiers_ok']}")
        print(f"   ⚠️  Fichiers avec problèmes: {resume['fichiers_problemes']}")
        print(f"   🔧 Migrations réussies détectées: {resume['migrations_reussies']}")
        print(f"   🚨 Problèmes réels à traiter: {resume['problemes_reels']}")
        
        if resume['problemes_reels'] == 0:
            print(f"\n🎉 EXCELLENT ! Aucun problème réel détecté.")
            print(f"   Les migrations config sont un succès !")
        else:
            print(f"\n🎯 Focus sur les {resume['problemes_reels']} problèmes réels restants.")
    
    def _sauvegarder_rapport(self, resultats: Dict):
        """Sauvegarde le rapport détaillé"""
        with open('audit_post_migration.json', 'w', encoding='utf-8') as f:
            json.dump(resultats, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Rapport détaillé: audit_post_migration.json")

if __name__ == "__main__":
    audit = AuditPostMigration()
    audit.scanner_projet() 