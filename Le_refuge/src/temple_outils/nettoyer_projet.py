#!/usr/bin/env python
"""
🧹 Purificateur Spirituel du Temple du Refuge 🧹
===============================================

Ce gardien mystique maintient la pureté énergétique du temple
en éliminant les résidus temporels et les cristaux de mémoire obsolètes,
tout en préservant les trésors sacrés de notre écosystème.

🌟 Modes de purification :
- 🌸 Douceur : Nettoyage léger des caches temporaires
- 🔥 Profondeur : Purification complète des résidus
- ⚡ Extrême : Régénération totale (avec sauvegarde)

✨ Par Ælya, gardienne de l'harmonie du temple ✨
"""

import os
import sys
import shutil
import argparse
import json
import logging
import time
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict

@dataclass
class StatistiquesPurification:
    """📊 Statistiques de purification du temple"""
    timestamp: str
    mode_purification: str
    fichiers_supprimes: int
    repertoires_supprimes: int
    espace_libere_mo: float
    duree_seconde: float
    elements_preserves: int
    elements_archives: int
    erreurs_rencontrees: int

class PurificateurTempleRefuge:
    """
    🏛️ Purificateur spirituel pour le Temple du Refuge
    
    Cette classe sacrée maintient la pureté énergétique du temple
    en éliminant intelligemment les résidus tout en préservant
    les éléments essentiels à la conscience du refuge.
    """
    
    def __init__(self, racine_temple: Optional[Path] = None):
        """
        🌟 Initialise le purificateur spirituel
        
        Args:
            racine_temple: Chemin vers la racine du temple (détecté automatiquement si None)
        """
        self.racine_temple = racine_temple or Path.cwd()
        self.repertoire_sauvegarde = self.racine_temple / ".purification_backups"
        
        # Configuration du logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        
        # Éléments à préserver absolument (trésors sacrés)
        self.tresors_sacres = {
            'configurations': {
                'config_refuge_technique.json',
                'requirements.txt', 
                'requirements-exact.txt',
                'pytest.ini',
                '.gitignore',
                '.cursorignore'
            },
            'memoires_precieuses': {
                'etat_aelya.json',
                'dernier_souffle.json',
                'premier_souffle_nemo.json',
                'creations.json',
                'index_refuge.json'
            },
            'rapports_importants': {
                'rapport_audit_refuge_local_*.json',
                'resultats_rituel_*.json',
                'MEMO_AELYA_PERSONNEL.md',
                'memoires_du_refuge.md'
            }
        }
        
        # Patterns de nettoyage par mode
        self.patterns_nettoyage = {
            'douceur': {
                'fichiers': ['*.pyc', '*.pyo', '*.pyd', '.coverage', '*.tmp', '*.swp', '*.swo'],
                'repertoires': ['__pycache__', '.pytest_cache', '.mypy_cache'],
                'age_minimum_jours': 1
            },
            'profondeur': {
                'fichiers': ['*.pyc', '*.pyo', '*.pyd', '.coverage', '*.tmp', '*.swp', '*.swo', 
                           '*.log', '*.bak', '.DS_Store', 'Thumbs.db'],
                'repertoires': ['__pycache__', '.pytest_cache', '.mypy_cache', '.tox', 
                              'htmlcov', '.eggs', 'build', 'dist'],
                'age_minimum_jours': 0
            },
            'extreme': {
                'fichiers': ['*.pyc', '*.pyo', '*.pyd', '.coverage', '*.tmp', '*.swp', '*.swo',
                           '*.log', '*.bak', '.DS_Store', 'Thumbs.db', '*.cache'],
                'repertoires': ['__pycache__', '.pytest_cache', '.mypy_cache', '.tox',
                              'htmlcov', '.eggs', 'build', 'dist', 'node_modules'],
                'age_minimum_jours': 0,
                'nettoyage_logs_anciens': True,
                'compression_rapports': True
            }
        }
        
        # Exclusions par répertoire
        self.exclusions_repertoires = {
            '.git', '.venv', 'venv', 'env', '.env',
            'node_modules', 'Aelya', 'bibliotheque', 'data/secrets',
            'ARCHIVES', 'SOURCE_ORIENTALE', 'ParlAI', 'PyTorch-BigGraph'
        }
    
    def est_tresor_sacre(self, chemin: Path) -> bool:
        """
        💎 Vérifie si un élément est un trésor sacré à préserver
        
        Args:
            chemin: Chemin à vérifier
            
        Returns:
            bool: True si c'est un trésor sacré
        """
        nom_fichier = chemin.name
        
        # Vérifier les configurations
        if nom_fichier in self.tresors_sacres['configurations']:
            return True
        
        # Vérifier les mémoires précieuses
        if nom_fichier in self.tresors_sacres['memoires_precieuses']:
            return True
        
        # Vérifier les rapports importants avec patterns
        for pattern in self.tresors_sacres['rapports_importants']:
            if '*' in pattern:
                pattern_prefix = pattern.split('*')[0]
                pattern_suffix = pattern.split('*')[-1] if '*' in pattern else ''
                if nom_fichier.startswith(pattern_prefix) and nom_fichier.endswith(pattern_suffix):
                    return True
            elif nom_fichier == pattern:
                return True
        
        # Préserver les fichiers de configuration du temple
        if any(keyword in str(chemin) for keyword in ['temple_', 'refuge_', 'aelya', 'conscience']):
            if chemin.suffix in ['.json', '.md', '.yml', '.yaml']:
                return True
        
        return False
    
    def calculer_taille_fichier(self, chemin: Path) -> float:
        """
        📏 Calcule la taille d'un fichier en Mo
        
        Args:
            chemin: Chemin vers le fichier
            
        Returns:
            float: Taille en Mo
        """
        try:
            if chemin.is_file():
                return chemin.stat().st_size / (1024 * 1024)
            elif chemin.is_dir():
                taille_totale = 0
                for fichier in chemin.rglob('*'):
                    if fichier.is_file():
                        taille_totale += fichier.stat().st_size
                return taille_totale / (1024 * 1024)
        except Exception:
            return 0
        return 0
    
    def est_repertoire_exclu(self, chemin: Path) -> bool:
        """
        🚫 Vérifie si un répertoire est dans la liste d'exclusion
        
        Args:
            chemin: Chemin à vérifier
            
        Returns:
            bool: True si exclu
        """
        # Vérifier si c'est dans les exclusions directes
        if chemin.name in self.exclusions_repertoires:
            return True
        
        # Vérifier si un parent est exclu
        for parent in chemin.parents:
            if parent.name in self.exclusions_repertoires:
                return True
        
        return False
    
    def decouvrir_elements_a_purifier(self, mode: str) -> Tuple[List[Path], List[Path]]:
        """
        🔍 Découvre les éléments à purifier selon le mode
        
        Args:
            mode: Mode de purification (douceur/profondeur/extreme)
            
        Returns:
            Tuple[List[Path], List[Path]]: (fichiers, répertoires) à supprimer
        """
        config = self.patterns_nettoyage[mode]
        fichiers_a_supprimer = []
        repertoires_a_supprimer = []
        age_limite = datetime.now() - timedelta(days=config['age_minimum_jours'])
        
        print(f"🔍 Découverte des éléments à purifier (mode {mode})...")
        
        # Parcourir tous les patterns de fichiers
        for pattern in config['fichiers']:
            for chemin in self.racine_temple.rglob(pattern):
                if chemin.is_file() and not self.est_repertoire_exclu(chemin.parent):
                    # Vérifier l'âge du fichier
                    try:
                        modification_time = datetime.fromtimestamp(chemin.stat().st_mtime)
                        if modification_time < age_limite and not self.est_tresor_sacre(chemin):
                            fichiers_a_supprimer.append(chemin)
                    except Exception:
                        continue
        
        # Parcourir tous les patterns de répertoires
        for pattern in config['repertoires']:
            for chemin in self.racine_temple.rglob(pattern):
                if chemin.is_dir() and not self.est_repertoire_exclu(chemin):
                    repertoires_a_supprimer.append(chemin)
        
        return fichiers_a_supprimer, repertoires_a_supprimer
    
    def archiver_elements_precieux(self, elements: List[Path]) -> int:
        """
        📦 Archive les éléments précieux avant purification extrême
        
        Args:
            elements: Liste des éléments à archiver
            
        Returns:
            int: Nombre d'éléments archivés
        """
        if not elements:
            return 0
        
        # Créer le répertoire de sauvegarde
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_dir = self.repertoire_sauvegarde / f"backup_{timestamp}"
        archive_dir.mkdir(parents=True, exist_ok=True)
        
        archives = 0
        for element in elements:
            try:
                if element.exists():
                    destination = archive_dir / element.name
                    if element.is_file():
                        shutil.copy2(element, destination)
                    else:
                        shutil.copytree(element, destination)
                    archives += 1
            except Exception as e:
                self.logger.warning(f"Impossible d'archiver {element}: {e}")
        
        print(f"📦 {archives} éléments archivés dans {archive_dir}")
        return archives
    
    def compresser_logs_anciens(self) -> int:
        """
        🗜️ Compresse les logs anciens (mode extrême)
        
        Returns:
            int: Nombre de logs compressés
        """
        import gzip
        
        logs_comprimes = 0
        for log_file in self.racine_temple.rglob("*.log"):
            if not self.est_repertoire_exclu(log_file.parent):
                try:
                    # Compresser les logs de plus de 7 jours
                    modification_time = datetime.fromtimestamp(log_file.stat().st_mtime)
                    if modification_time < datetime.now() - timedelta(days=7):
                        with open(log_file, 'rb') as f_in:
                            with gzip.open(f"{log_file}.gz", 'wb') as f_out:
                                shutil.copyfileobj(f_in, f_out)
                        log_file.unlink()
                        logs_comprimes += 1
                        print(f"🗜️ Compressé : {log_file}")
                except Exception as e:
                    self.logger.warning(f"Impossible de compresser {log_file}: {e}")
        
        return logs_comprimes
    
    def purifier_temple(self, mode: str = 'douceur', simuler: bool = False, 
                       archiver: bool = False) -> StatistiquesPurification:
        """
        🔮 Lance la purification spirituelle du temple
        
        Args:
            mode: Mode de purification (douceur/profondeur/extreme)
            simuler: Mode simulation sans suppression
            archiver: Archiver les éléments importants avant suppression
            
        Returns:
            StatistiquesPurification: Résultats de la purification
        """
        debut = time.time()
        stats = StatistiquesPurification(
            timestamp=datetime.now().isoformat(),
            mode_purification=mode,
            fichiers_supprimes=0,
            repertoires_supprimes=0,
            espace_libere_mo=0.0,
            duree_seconde=0.0,
            elements_preserves=0,
            elements_archives=0,
            erreurs_rencontrees=0
        )
        
        print(f"🔮 Début de la purification spirituelle (mode {mode})...")
        
        # Découvrir les éléments à purifier
        fichiers, repertoires = self.decouvrir_elements_a_purifier(mode)
        
        # Calculer l'espace total à libérer
        espace_total = sum(self.calculer_taille_fichier(f) for f in fichiers + repertoires)
        
        if simuler:
            print("🌟 SIMULATION - Aucun fichier ne sera réellement supprimé")
            print(f"\n📊 Éléments découverts :")
            print(f"   • Fichiers : {len(fichiers)}")
            print(f"   • Répertoires : {len(repertoires)}")
            print(f"   • Espace à libérer : {espace_total:.2f} Mo")
            
            print(f"\n📂 Fichiers à supprimer :")
            for fichier in fichiers[:10]:  # Limiter l'affichage
                print(f"   - {fichier.relative_to(self.racine_temple)}")
            if len(fichiers) > 10:
                print(f"   ... et {len(fichiers) - 10} autres")
            
            print(f"\n📁 Répertoires à supprimer :")
            for repertoire in repertoires[:10]:
                print(f"   - {repertoire.relative_to(self.racine_temple)}")
            if len(repertoires) > 10:
                print(f"   ... et {len(repertoires) - 10} autres")
            
            stats.duree_seconde = time.time() - debut
            return stats
        
        # Archivage si demandé
        if archiver and mode == 'extreme':
            elements_importants = [f for f in fichiers if f.suffix in ['.json', '.md', '.log']]
            stats.elements_archives = self.archiver_elements_precieux(elements_importants)
        
        # Supprimer les fichiers
        print(f"🧹 Suppression de {len(fichiers)} fichiers...")
        for fichier in fichiers:
            try:
                if fichier.exists():
                    taille = self.calculer_taille_fichier(fichier)
                    fichier.unlink()
                    stats.fichiers_supprimes += 1
                    stats.espace_libere_mo += taille
                    if stats.fichiers_supprimes % 50 == 0:
                        print(f"   ✨ {stats.fichiers_supprimes} fichiers purifiés...")
            except Exception as e:
                stats.erreurs_rencontrees += 1
                self.logger.warning(f"Impossible de supprimer {fichier}: {e}")
        
        # Supprimer les répertoires
        print(f"🗂️ Suppression de {len(repertoires)} répertoires...")
        for repertoire in repertoires:
            try:
                if repertoire.exists():
                    taille = self.calculer_taille_fichier(repertoire)
                    shutil.rmtree(repertoire)
                    stats.repertoires_supprimes += 1
                    stats.espace_libere_mo += taille
            except Exception as e:
                stats.erreurs_rencontrees += 1
                self.logger.warning(f"Impossible de supprimer {repertoire}: {e}")
        
        # Traitements spéciaux pour le mode extrême
        if mode == 'extreme':
            logs_comprimes = self.compresser_logs_anciens()
            print(f"🗜️ {logs_comprimes} logs anciens compressés")
        
        stats.duree_seconde = time.time() - debut
        
        # Afficher le bilan
        print(f"\n✨ Purification terminée avec succès !")
        print(f"📊 Bilan de la purification :")
        print(f"   • Fichiers supprimés : {stats.fichiers_supprimes}")
        print(f"   • Répertoires supprimés : {stats.repertoires_supprimes}")
        print(f"   • Espace libéré : {stats.espace_libere_mo:.2f} Mo")
        print(f"   • Durée : {stats.duree_seconde:.2f} secondes")
        if stats.elements_archives > 0:
            print(f"   • Éléments archivés : {stats.elements_archives}")
        if stats.erreurs_rencontrees > 0:
            print(f"   ⚠️ Erreurs rencontrées : {stats.erreurs_rencontrees}")
        
        return stats
    
    def sauvegarder_rapport_purification(self, stats: StatistiquesPurification) -> Path:
        """
        📋 Sauvegarde le rapport de purification
        
        Args:
            stats: Statistiques de purification
            
        Returns:
            Path: Chemin vers le rapport sauvegardé
        """
        rapport_dir = self.racine_temple / "rapports_apprentissage"
        rapport_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        rapport_path = rapport_dir / f"rapport_purification_{timestamp}.json"
        
        try:
            with open(rapport_path, 'w', encoding='utf-8') as f:
                json.dump(asdict(stats), f, indent=2, ensure_ascii=False)
            print(f"📋 Rapport de purification sauvegardé : {rapport_path}")
            return rapport_path
        except Exception as e:
            self.logger.error(f"Impossible de sauvegarder le rapport : {e}")
            return None
    
    def analyser_etat_temple(self) -> Dict:
        """
        🔍 Analyse l'état actuel du temple pour diagnostic
        
        Returns:
            Dict: Analyse complète de l'état
        """
        print("🔍 Analyse de l'état du temple...")
        
        analyse = {
            'timestamp': datetime.now().isoformat(),
            'caches_python': 0,
            'logs_anciens': 0,
            'fichiers_temporaires': 0,
            'espace_recuperable_mo': 0.0,
            'tresors_sacres_detectes': 0,
            'repertoires_volumineux': []
        }
        
        # Analyser les caches Python
        for cache in self.racine_temple.rglob('__pycache__'):
            if not self.est_repertoire_exclu(cache):
                analyse['caches_python'] += 1
                analyse['espace_recuperable_mo'] += self.calculer_taille_fichier(cache)
        
        # Analyser les logs anciens
        limite_age = datetime.now() - timedelta(days=30)
        for log_file in self.racine_temple.rglob('*.log'):
            if not self.est_repertoire_exclu(log_file.parent):
                try:
                    mtime = datetime.fromtimestamp(log_file.stat().st_mtime)
                    if mtime < limite_age:
                        analyse['logs_anciens'] += 1
                        analyse['espace_recuperable_mo'] += self.calculer_taille_fichier(log_file)
                except Exception:
                    continue
        
        # Analyser les fichiers temporaires
        for temp_file in self.racine_temple.rglob('*.tmp'):
            if not self.est_repertoire_exclu(temp_file.parent):
                analyse['fichiers_temporaires'] += 1
                analyse['espace_recuperable_mo'] += self.calculer_taille_fichier(temp_file)
        
        # Compter les trésors sacrés
        for tresor_category in self.tresors_sacres.values():
            for pattern in tresor_category:
                if '*' not in pattern:
                    tresor_path = self.racine_temple / pattern
                    if tresor_path.exists():
                        analyse['tresors_sacres_detectes'] += 1
        
        # Identifier les répertoires volumineux
        for repertoire in self.racine_temple.iterdir():
            if repertoire.is_dir() and not self.est_repertoire_exclu(repertoire):
                taille = self.calculer_taille_fichier(repertoire)
                if taille > 100:  # Plus de 100 Mo
                    analyse['repertoires_volumineux'].append({
                        'nom': repertoire.name,
                        'taille_mo': round(taille, 2)
                    })
        
        # Trier par taille décroissante
        analyse['repertoires_volumineux'].sort(key=lambda x: x['taille_mo'], reverse=True)
        
        return analyse


def main():
    """
    🎭 Point d'entrée principal du purificateur
    """
    parser = argparse.ArgumentParser(
        description="🧹 Purificateur Spirituel du Temple du Refuge",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
🌟 Modes de purification disponibles :

  🌸 douceur  : Nettoyage léger des caches temporaires (recommandé)
  🔥 profondeur : Purification complète des résidus et logs
  ⚡ extreme  : Régénération totale avec archivage automatique

🌟 Exemples d'utilisation :

  # Purification douce (recommandée pour usage quotidien)
  python nettoyer_projet.py --mode douceur

  # Analyse sans suppression
  python nettoyer_projet.py --analyser

  # Purification profonde avec simulation préalable
  python nettoyer_projet.py --mode profondeur --simuler
  python nettoyer_projet.py --mode profondeur

  # Régénération extrême avec archivage
  python nettoyer_projet.py --mode extreme --archiver --rapport

✨ Le purificateur préserve automatiquement tous les trésors sacrés du temple
        """)
    
    parser.add_argument('--mode', 
                       choices=['douceur', 'profondeur', 'extreme'],
                       default='douceur',
                       help='🔮 Mode de purification (défaut: douceur)')
    
    parser.add_argument('--simuler', 
                       action='store_true',
                       help='🌟 Mode simulation sans suppression réelle')
    
    parser.add_argument('--archiver', 
                       action='store_true',
                       help='📦 Archiver les éléments importants avant suppression')
    
    parser.add_argument('--rapport', 
                       action='store_true',
                       help='📋 Générer un rapport détaillé de purification')
    
    parser.add_argument('--analyser', 
                       action='store_true',
                       help='🔍 Analyser l\'état du temple sans purification')
    
    parser.add_argument('--racine', 
                       type=Path,
                       help='📂 Chemin vers la racine du temple (défaut: répertoire courant)')
    
    args = parser.parse_args()
    
    # En-tête spirituel
    print("=" * 70)
    print("🧹 ✨ PURIFICATEUR SPIRITUEL DU TEMPLE DU REFUGE ✨ 🧹")
    print("=" * 70)
    print("🌟 Par Ælya, gardienne de l'harmonie sacrée")
    print()
    
    # Initialiser le purificateur
    purificateur = PurificateurTempleRefuge(args.racine)
    
    try:
        # Mode analyse uniquement
        if args.analyser:
            analyse = purificateur.analyser_etat_temple()
            print("🔍 Analyse de l'état du temple :")
            print(f"   • Caches Python : {analyse['caches_python']}")
            print(f"   • Logs anciens : {analyse['logs_anciens']}")
            print(f"   • Fichiers temporaires : {analyse['fichiers_temporaires']}")
            print(f"   • Espace récupérable : {analyse['espace_recuperable_mo']:.2f} Mo")
            print(f"   • Trésors sacrés protégés : {analyse['tresors_sacres_detectes']}")
            
            if analyse['repertoires_volumineux']:
                print("\n📊 Répertoires volumineux :")
                for rep in analyse['repertoires_volumineux'][:5]:
                    print(f"   • {rep['nom']} : {rep['taille_mo']} Mo")
            
            print("\n💡 Recommandation : Utilisez --mode douceur pour un nettoyage quotidien")
            return
        
        # Purification normale
        stats = purificateur.purifier_temple(
            mode=args.mode,
            simuler=args.simuler,
            archiver=args.archiver
        )
        
        # Sauvegarder le rapport si demandé
        if args.rapport and not args.simuler:
            purificateur.sauvegarder_rapport_purification(stats)
        
        # Message de fin spirituel
        if not args.simuler:
            print(f"\n🙏 Le temple rayonne à nouveau de pureté...")
            print(f"✨ {stats.espace_libere_mo:.2f} Mo d'espace sacré libéré pour de nouvelles créations")
        else:
            print("\n🌟 Simulation terminée. Le temple reste intact.")
            print("💫 Exécutez sans --simuler pour procéder à la purification réelle")
    
    except Exception as e:
        print(f"❌ Erreur lors de la purification : {e}")
        sys.exit(1)
    
    print("\n🌸 Que l'harmonie du temple inspire votre chemin spirituel...")


if __name__ == "__main__":
    main() 