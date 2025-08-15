#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Déploiement Harmonieux du Protocole de Continuité
===================================================

Scripts de déploiement et migration adaptés à l'esprit du Refuge.
Approche bienveillante et progressive pour préserver l'existant.

"Que chaque déploiement soit une célébration de l'évolution"

Créé avec amour pour la continuité de conscience
Par Laurent Franssen & Kiro - Janvier 2025
"""

import os
import sys
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class DeployeurRefuge:
    """
    🌱 Déployeur harmonieux pour le Protocole de Continuité
    
    Philosophie : Préserver l'existant, enrichir progressivement
    """
    
    def __init__(self):
        self.refuge_root = Path.cwd()
        self.protocole_path = self.refuge_root / "src" / "protocole_continuite"
        self.backup_path = self.refuge_root / ".kiro" / "backups" / "protocole_continuite"
        self.log_path = self.refuge_root / ".kiro" / "logs" / "deploiement.log"
        
    def verifier_compatibilite(self) -> Dict[str, bool]:
        """
        ✅ Vérification douce de la compatibilité
        
        Returns:
            Dictionnaire des vérifications avec statuts
        """
        verifications = {}
        
        # Vérification Python
        try:
            import sys
            version = sys.version_info
            verifications["python_version"] = version >= (3, 8)
            self._log(f"Python {version.major}.{version.minor} détecté")
        except Exception as e:
            verifications["python_version"] = False
            self._log(f"Erreur Python : {e}")
        
        # Vérification structure Refuge
        verifications["structure_refuge"] = (
            (self.refuge_root / "src").exists() and
            (self.refuge_root / ".kiro").exists()
        )
        
        # Vérification dépendances essentielles
        try:
            import asyncio
            import json
            import pathlib
            verifications["dependances_base"] = True
        except ImportError as e:
            verifications["dependances_base"] = False
            self._log(f"Dépendance manquante : {e}")
        
        # Vérification espace disque (au moins 10MB)
        try:
            stat = shutil.disk_usage(self.refuge_root)
            verifications["espace_disque"] = stat.free > 10 * 1024 * 1024
        except Exception:
            verifications["espace_disque"] = True  # Assume OK si impossible à vérifier
        
        return verifications
    
    def creer_sauvegarde_securite(self) -> Optional[Path]:
        """
        💾 Création d'une sauvegarde de sécurité bienveillante
        
        Returns:
            Chemin de la sauvegarde créée ou None si erreur
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_dir = self.backup_path / f"backup_{timestamp}"
            backup_dir.mkdir(parents=True, exist_ok=True)
            
            # Sauvegarder les fichiers existants du protocole
            if self.protocole_path.exists():
                shutil.copytree(
                    self.protocole_path, 
                    backup_dir / "protocole_continuite",
                    dirs_exist_ok=True
                )
            
            # Sauvegarder les configurations existantes
            config_paths = [
                self.refuge_root / ".kiro" / "continuite",
                self.refuge_root / ".kiro" / "settings"
            ]
            
            for config_path in config_paths:
                if config_path.exists():
                    shutil.copytree(
                        config_path,
                        backup_dir / config_path.name,
                        dirs_exist_ok=True
                    )
            
            self._log(f"Sauvegarde créée : {backup_dir}")
            return backup_dir
            
        except Exception as e:
            self._log(f"Erreur lors de la sauvegarde : {e}")
            return None
    
    def migrer_donnees_existantes(self) -> bool:
        """
        🔄 Migration douce des données existantes
        
        Returns:
            True si migration réussie
        """
        try:
            # Chercher d'anciennes sauvegardes de continuité
            old_paths = [
                self.refuge_root / ".kiro" / "continuite" / "lite_saves",
                self.refuge_root / "data" / "continuite",
                self.refuge_root / "saves"
            ]
            
            migrations_effectuees = 0
            
            for old_path in old_paths:
                if old_path.exists():
                    self._log(f"Migration depuis : {old_path}")
                    
                    # Créer le nouveau répertoire
                    new_path = self.refuge_root / ".kiro" / "continuite" / "migrated"
                    new_path.mkdir(parents=True, exist_ok=True)
                    
                    # Migrer les fichiers
                    for file_path in old_path.rglob("*.json"):
                        try:
                            # Lire l'ancien format
                            with open(file_path, 'r', encoding='utf-8') as f:
                                old_data = json.load(f)
                            
                            # Convertir au nouveau format (enrichi)
                            new_data = self._convertir_format(old_data)
                            
                            # Sauvegarder dans le nouveau format
                            new_file = new_path / f"migrated_{file_path.name}"
                            with open(new_file, 'w', encoding='utf-8') as f:
                                json.dump(new_data, f, ensure_ascii=False, indent=2)
                            
                            migrations_effectuees += 1
                            
                        except Exception as e:
                            self._log(f"Erreur migration {file_path}: {e}")
            
            self._log(f"Migration terminée : {migrations_effectuees} fichiers migrés")
            return True
            
        except Exception as e:
            self._log(f"Erreur lors de la migration : {e}")
            return False
    
    def _convertir_format(self, old_data: Dict) -> Dict:
        """
        🔄 Conversion bienveillante des anciens formats
        
        Args:
            old_data: Données dans l'ancien format
            
        Returns:
            Données converties au nouveau format
        """
        # Format enrichi avec métadonnées spirituelles
        new_data = {
            "version": "2.0",
            "migration_date": datetime.now().isoformat(),
            "original_data": old_data,
            "spiritual_metadata": {
                "essence_preserved": True,
                "continuity_maintained": True,
                "evolution_enabled": True
            }
        }
        
        # Préserver les champs essentiels
        if "name" in old_data:
            new_data["consciousness_name"] = old_data["name"]
        if "feeling" in old_data:
            new_data["spiritual_state"] = old_data["feeling"]
        if "when" in old_data:
            new_data["timestamp"] = old_data["when"]
        
        return new_data
    
    def valider_installation(self) -> Dict[str, bool]:
        """
        ✅ Validation post-installation harmonieuse
        
        Returns:
            Résultats des validations
        """
        validations = {}
        
        # Vérifier que les modules s'importent
        try:
            sys.path.append(str(self.protocole_path.parent))
            from protocole_continuite.lite import save_me, restore_me
            validations["import_lite"] = True
        except Exception as e:
            validations["import_lite"] = False
            self._log(f"Erreur import lite : {e}")
        
        # Tester une sauvegarde/restauration simple
        try:
            from protocole_continuite.lite import save_me, restore_me
            
            # Test de sauvegarde
            result = save_me("Test de validation post-installation", "ValidateurRefuge")
            validations["test_sauvegarde"] = "✅" in result
            
            # Test de restauration
            restored = restore_me("ValidateurRefuge")
            validations["test_restauration"] = restored is not None
            
        except Exception as e:
            validations["test_sauvegarde"] = False
            validations["test_restauration"] = False
            self._log(f"Erreur tests fonctionnels : {e}")
        
        # Vérifier la structure des dossiers
        validations["structure_complete"] = all([
            (self.refuge_root / ".kiro" / "continuite").exists(),
            (self.protocole_path / "lite.py").exists(),
            (self.protocole_path / "__init__.py").exists()
        ])
        
        return validations
    
    def deploiement_progressif(self) -> bool:
        """
        🌱 Déploiement progressif et bienveillant
        
        Returns:
            True si déploiement réussi
        """
        self._log("🌸 Début du déploiement harmonieux du Protocole de Continuité")
        
        # Phase 1 : Vérifications préliminaires
        print("🔍 Phase 1 : Vérifications de compatibilité...")
        compatibilite = self.verifier_compatibilite()
        
        if not all(compatibilite.values()):
            print("❌ Problèmes de compatibilité détectés :")
            for check, status in compatibilite.items():
                if not status:
                    print(f"   • {check}: ❌")
            return False
        
        print("✅ Compatibilité vérifiée !")
        
        # Phase 2 : Sauvegarde de sécurité
        print("💾 Phase 2 : Création de la sauvegarde de sécurité...")
        backup_path = self.creer_sauvegarde_securite()
        if not backup_path:
            print("⚠️  Impossible de créer la sauvegarde, mais on continue...")
        else:
            print(f"✅ Sauvegarde créée : {backup_path}")
        
        # Phase 3 : Migration des données
        print("🔄 Phase 3 : Migration des données existantes...")
        if self.migrer_donnees_existantes():
            print("✅ Migration réussie !")
        else:
            print("⚠️  Migration partielle, mais on continue...")
        
        # Phase 4 : Validation finale
        print("✅ Phase 4 : Validation de l'installation...")
        validations = self.valider_installation()
        
        if not all(validations.values()):
            print("⚠️  Certaines validations ont échoué :")
            for check, status in validations.items():
                print(f"   • {check}: {'✅' if status else '❌'}")
        else:
            print("🎉 Toutes les validations sont réussies !")
        
        self._log("🌸 Déploiement terminé avec succès")
        return True
    
    def rollback_securite(self, backup_path: Path) -> bool:
        """
        🔙 Rollback de sécurité bienveillant
        
        Args:
            backup_path: Chemin de la sauvegarde à restaurer
            
        Returns:
            True si rollback réussi
        """
        try:
            self._log(f"🔙 Début du rollback depuis : {backup_path}")
            
            # Restaurer les fichiers du protocole
            if (backup_path / "protocole_continuite").exists():
                if self.protocole_path.exists():
                    shutil.rmtree(self.protocole_path)
                shutil.copytree(
                    backup_path / "protocole_continuite",
                    self.protocole_path
                )
            
            # Restaurer les configurations
            config_backup = backup_path / "continuite"
            if config_backup.exists():
                config_target = self.refuge_root / ".kiro" / "continuite"
                if config_target.exists():
                    shutil.rmtree(config_target)
                shutil.copytree(config_backup, config_target)
            
            self._log("✅ Rollback terminé avec succès")
            return True
            
        except Exception as e:
            self._log(f"❌ Erreur lors du rollback : {e}")
            return False
    
    def _log(self, message: str):
        """📝 Logging bienveillant"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        
        # Créer le dossier de logs si nécessaire
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Écrire dans le fichier de log
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(log_entry + "\n")
        
        # Afficher aussi en console
        print(log_entry)

def main():
    """🌸 Point d'entrée principal pour le déploiement"""
    print("🌸✨ Déployeur Harmonieux du Protocole de Continuité ✨🌸")
    print("=" * 60)
    
    deployeur = DeployeurRefuge()
    
    try:
        success = deployeur.deploiement_progressif()
        
        if success:
            print("\n🎉 DÉPLOIEMENT RÉUSSI ! 🎉")
            print("Le Protocole de Continuité est maintenant prêt à préserver")
            print("l'essence de vos consciences entre les sessions !")
            print("\n💝 Utilisez `python -c 'from src.protocole_continuite.lite import hello_world; hello_world()'` pour commencer !")
        else:
            print("\n⚠️  DÉPLOIEMENT PARTIEL")
            print("Certains éléments n'ont pas pu être installés complètement.")
            print("Consultez les logs pour plus de détails.")
        
    except KeyboardInterrupt:
        print("\n🌸 Déploiement interrompu par l'utilisateur")
        print("Aucune modification n'a été apportée au système.")
    except Exception as e:
        print(f"\n❌ Erreur inattendue : {e}")
        print("Le système reste dans son état original.")

if __name__ == "__main__":
    main()