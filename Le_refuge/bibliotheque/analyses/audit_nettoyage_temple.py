#!/usr/bin/env python3
"""
Audit de Nettoyage du Temple
============================

Identifie les éléments à nettoyer dans la racine :
- Bibliothèques externes (ParlAI, PyTorch-BigGraph)
- Répertoires de backup obsolètes
- Gros répertoires non essentiels

Auteur: Laurent & Ælya
Date: 26 Mai 2025
Objectif: Préparer le nettoyage de notre temple de l'âme
"""

import os
from pathlib import Path
from datetime import datetime
import json

class AuditeurNettoyageTemple:
    """Identifie ce qui peut être nettoyé dans notre temple"""
    
    def __init__(self):
        self.racine = Path(".")
        self.bibliotheques_externes = {
            'ParlAI': 'Bibliothèque de dialogue Facebook',
            'PyTorch-BigGraph': 'Bibliothèque de graphes PyTorch', 
            'AI-Scientist': 'Projet de recherche externe',
            'AI-Scientist-v2': 'Version 2 du projet de recherche'
        }
        
        self.backups_suspects = {
            'backup_cluster_test': 'Backup de test',
            'backup_cluster_sacred_20250525_181950': 'Backup du 25 mai',
            'backup_coeur_migration': 'Backup migration coeur'
        }
    
    def analyser_taille_repertoires(self) -> dict:
        """Analyse la taille des répertoires principaux"""
        print("📏 Analyse des tailles des répertoires...")
        
        tailles = {}
        for item in self.racine.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                try:
                    # Compter les fichiers récursivement
                    nb_fichiers = sum(1 for _ in item.rglob('*') if _.is_file())
                    taille_mb = sum(f.stat().st_size for f in item.rglob('*') if f.is_file()) / (1024*1024)
                    
                    tailles[item.name] = {
                        'fichiers': nb_fichiers,
                        'taille_mb': round(taille_mb, 2),
                        'type': self._categoriser_repertoire(item.name)
                    }
                except Exception as e:
                    tailles[item.name] = {
                        'fichiers': 0,
                        'taille_mb': 0,
                        'erreur': str(e),
                        'type': 'erreur'
                    }
        
        return tailles
    
    def _categoriser_repertoire(self, nom: str) -> str:
        """Catégorise un répertoire selon son utilité"""
        if nom in self.bibliotheques_externes:
            return 'bibliotheque_externe'
        elif nom in self.backups_suspects:
            return 'backup'
        elif nom in ['src', 'app', 'data', 'logs', 'etat']:
            return 'refuge_core'
        else:
            return 'refuge_autre'
    
    def generer_rapport_nettoyage(self) -> dict:
        """Génère un rapport complet de nettoyage"""
        print("\n🧹 AUDIT DE NETTOYAGE DU TEMPLE")
        print("=" * 35)
        
        # Analyser les tailles
        tailles = self.analyser_taille_repertoires()
        
        # Séparer par catégories
        bibliotheques = {k: v for k, v in tailles.items() if v['type'] == 'bibliotheque_externe'}
        backups = {k: v for k, v in tailles.items() if v['type'] == 'backup'}
        refuge_core = {k: v for k, v in tailles.items() if v['type'] == 'refuge_core'}
        autres = {k: v for k, v in tailles.items() if v['type'] == 'refuge_autre'}
        
        # Calculer économies
        economie_bibliotheques = sum(v['taille_mb'] for v in bibliotheques.values())
        economie_backups = sum(v['taille_mb'] for v in backups.values())
        
        rapport = {
            'timestamp': datetime.now().isoformat(),
            'bibliotheques_externes': bibliotheques,
            'backups_suspects': backups,
            'refuge_core': refuge_core,
            'refuge_autres': autres,
            'economie_potentielle': {
                'bibliotheques_mb': round(economie_bibliotheques, 2),
                'backups_mb': round(economie_backups, 2),
                'total_mb': round(economie_bibliotheques + economie_backups, 2)
            }
        }
        
        return rapport
    
    def afficher_rapport_console(self, rapport: dict):
        """Affiche le rapport dans la console"""
        print(f"\n📋 RAPPORT NETTOYAGE TEMPLE - {rapport['timestamp'][:19]}")
        print("=" * 50)
        
        # Économies potentielles
        economie = rapport['economie_potentielle']
        print(f"\n💾 ÉCONOMIES POTENTIELLES")
        print(f"   📚 Bibliothèques externes: {economie['bibliotheques_mb']} MB")
        print(f"   💾 Backups obsolètes: {economie['backups_mb']} MB")
        print(f"   📊 Total libérable: {economie['total_mb']} MB")
        
        # Bibliothèques externes
        if rapport['bibliotheques_externes']:
            print(f"\n🔗 BIBLIOTHÈQUES EXTERNES À DÉPLACER")
            for nom, info in rapport['bibliotheques_externes'].items():
                desc = self.bibliotheques_externes.get(nom, 'Inconnue')
                print(f"   📚 {nom} - {info['taille_mb']} MB - {desc}")
                print(f"       {info['fichiers']} fichiers")
        
        # Backups suspects
        if rapport['backups_suspects']:
            print(f"\n💾 BACKUPS À SUPPRIMER (après vérification)")
            for nom, info in rapport['backups_suspects'].items():
                desc = self.backups_suspects.get(nom, 'Backup')
                print(f"   📦 {nom} - {info['taille_mb']} MB - {desc}")
                print(f"       {info['fichiers']} fichiers")
        
        # Cœur du refuge (à conserver)
        if rapport['refuge_core']:
            print(f"\n🏛️ CŒUR DU REFUGE (à conserver)")
            for nom, info in rapport['refuge_core'].items():
                print(f"   ✅ {nom} - {info['taille_mb']} MB")
        
        # Recommandations
        print(f"\n💡 RECOMMANDATIONS")
        if rapport['bibliotheques_externes']:
            print("   🔥 PRIORITÉ HAUTE: Déplacer les bibliothèques externes")
        if rapport['backups_suspects']:
            print("   🟡 PRIORITÉ MOYENNE: Supprimer les backups après vérification")
        if economie['total_mb'] == 0:
            print("   🎉 Le temple est déjà bien organisé !")
        
        print(f"\n🏛️ NOTRE TEMPLE SERA PLUS HARMONIEUX APRÈS NETTOYAGE ✨")

def main():
    """Point d'entrée principal"""
    print("🧹 AUDIT DE NETTOYAGE DU TEMPLE")
    print("================================")
    print("Préparation du nettoyage de notre temple de l'âme ✨\n")
    
    auditeur = AuditeurNettoyageTemple()
    
    try:
        rapport = auditeur.generer_rapport_nettoyage()
        auditeur.afficher_rapport_console(rapport)
        
        # Sauvegarder
        fichier = f"rapport_nettoyage_temple_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"\n💾 Rapport sauvegardé: {fichier}")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")

if __name__ == "__main__":
    main() 