#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔙 Rollback d'Urgence - Protocole de Continuité
===============================================

Script de rollback d'urgence pour restaurer l'état précédent
en cas de problème avec le déploiement du Protocole de Continuité.

"Retour en arrière bienveillant pour préserver l'harmonie"

Créé avec prudence pour la sécurité du Refuge
Par Laurent Franssen & Kiro - Janvier 2025
"""

import os
import sys
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Optional

class RollbackUrgence:
    """
    🔙 Gestionnaire de rollback d'urgence bienveillant
    """
    
    def __init__(self):
        self.refuge_root = Path.cwd()
        self.backup_root = self.refuge_root / ".kiro" / "backups" / "protocole_continuite"
        self.log_path = self.refuge_root / ".kiro" / "logs" / "rollback_urgence.log"
        
    def lister_sauvegardes_disponibles(self) -> List[Path]:
        """
        📋 Liste les sauvegardes disponibles pour rollback
        
        Returns:
            Liste des chemins de sauvegarde triés par date (plus récent en premier)
        """
        if not self.backup_root.exists():
            return []
        
        sauvegardes = []
        for item in self.backup_root.iterdir():
            if item.is_dir() and item.name.startswith("backup_"):
                sauvegardes.append(item)
        
        # Trier par date de modification (plus récent en premier)
        sauvegardes.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        
        return sauvegardes
    
    def afficher_sauvegardes(self) -> Optional[Path]:
        """
        📋 Affiche les sauvegardes disponibles et permet la sélection
        
        Returns:
            Chemin de la sauvegarde sélectionnée ou None si annulation
        """
        sauvegardes = self.lister_sauvegardes_disponibles()
        
        if not sauvegardes:
            print("❌ Aucune sauvegarde trouvée dans .kiro/backups/protocole_continuite/")
            return None
        
        print("📋 Sauvegardes disponibles :")
        print("=" * 50)
        
        for i, sauvegarde in enumerate(sauvegardes, 1):
            # Extraire la date du nom du dossier
            nom = sauvegarde.name
            if "_" in nom:
                try:
                    date_str = nom.split("_", 1)[1]
                    # Format: YYYYMMDD_HHMMSS
                    if len(date_str) >= 15:
                        date_part = date_str[:8]
                        time_part = date_str[9:15]
                        date_formatted = f"{date_part[:4]}-{date_part[4:6]}-{date_part[6:8]}"
                        time_formatted = f"{time_part[:2]}:{time_part[2:4]}:{time_part[4:6]}"
                        date_display = f"{date_formatted} {time_formatted}"
                    else:
                        date_display = date_str
                except:
                    date_display = nom
            else:
                date_display = nom
            
            # Taille de la sauvegarde
            try:
                taille = sum(f.stat().st_size for f in sauvegarde.rglob('*') if f.is_file())
                taille_mb = taille / (1024 * 1024)
                taille_str = f"{taille_mb:.1f} MB"
            except:
                taille_str = "? MB"
            
            print(f"  {i}. {date_display} ({taille_str})")
        
        print("\n0. Annuler le rollback")
        print("=" * 50)
        
        while True:
            try:
                choix = input("Choisissez une sauvegarde (0 pour annuler) : ").strip()
                
                if choix == "0":
                    return None
                
                index = int(choix) - 1
                if 0 <= index < len(sauvegardes):
                    return sauvegardes[index]
                else:
                    print("❌ Choix invalide. Veuillez entrer un numéro valide.")
                    
            except ValueError:
                print("❌ Veuillez entrer un numéro valide.")
            except KeyboardInterrupt:
                print("\n🌸 Rollback annulé par l'utilisateur.")
                return None
    
    def confirmer_rollback(self, sauvegarde_path: Path) -> bool:
        """
        ⚠️ Demande confirmation avant le rollback
        
        Args:
            sauvegarde_path: Chemin de la sauvegarde à restaurer
            
        Returns:
            True si confirmé, False sinon
        """
        print(f"\n⚠️  ATTENTION : ROLLBACK D'URGENCE")
        print("=" * 50)
        print(f"Sauvegarde sélectionnée : {sauvegarde_path.name}")
        print("\nCette opération va :")
        print("  • Supprimer la version actuelle du protocole")
        print("  • Restaurer l'état depuis la sauvegarde")
        print("  • Écraser les configurations actuelles")
        print("\n⚠️  Cette action est IRRÉVERSIBLE !")
        
        while True:
            try:
                confirmation = input("\nÊtes-vous sûr de vouloir continuer ? (oui/non) : ").strip().lower()
                
                if confirmation in ["oui", "o", "yes", "y"]:
                    return True
                elif confirmation in ["non", "n", "no"]:
                    return False
                else:
                    print("❌ Veuillez répondre par 'oui' ou 'non'.")
                    
            except KeyboardInterrupt:
                print("\n🌸 Rollback annulé par l'utilisateur.")
                return False
    
    def executer_rollback(self, sauvegarde_path: Path) -> bool:
        """
        🔙 Exécute le rollback depuis la sauvegarde spécifiée
        
        Args:
            sauvegarde_path: Chemin de la sauvegarde à restaurer
            
        Returns:
            True si rollback réussi
        """
        try:
            self._log(f"🔙 Début du rollback depuis : {sauvegarde_path}")
            
            # Étape 1 : Supprimer la version actuelle
            protocole_path = self.refuge_root / "src" / "protocole_continuite"
            if protocole_path.exists():
                self._log("🗑️ Suppression de la version actuelle...")
                shutil.rmtree(protocole_path)
            
            # Étape 2 : Restaurer les fichiers du protocole
            sauvegarde_protocole = sauvegarde_path / "protocole_continuite"
            if sauvegarde_protocole.exists():
                self._log("📁 Restauration des fichiers du protocole...")
                shutil.copytree(sauvegarde_protocole, protocole_path)
            else:
                self._log("⚠️ Aucun fichier de protocole dans la sauvegarde")
            
            # Étape 3 : Restaurer les configurations
            config_sauvegarde = sauvegarde_path / "continuite"
            if config_sauvegarde.exists():
                config_cible = self.refuge_root / ".kiro" / "continuite"
                if config_cible.exists():
                    shutil.rmtree(config_cible)
                self._log("⚙️ Restauration des configurations...")
                shutil.copytree(config_sauvegarde, config_cible)
            
            # Étape 4 : Restaurer les settings
            settings_sauvegarde = sauvegarde_path / "settings"
            if settings_sauvegarde.exists():
                settings_cible = self.refuge_root / ".kiro" / "settings"
                if settings_cible.exists():
                    # Ne pas écraser complètement, juste les fichiers du protocole
                    for item in settings_sauvegarde.iterdir():
                        if "protocole" in item.name.lower():
                            cible = settings_cible / item.name
                            if item.is_file():
                                shutil.copy2(item, cible)
                            elif item.is_dir():
                                if cible.exists():
                                    shutil.rmtree(cible)
                                shutil.copytree(item, cible)
            
            self._log("✅ Rollback terminé avec succès")
            return True
            
        except Exception as e:
            self._log(f"❌ Erreur lors du rollback : {e}")
            return False
    
    def valider_rollback(self) -> bool:
        """
        ✅ Valide que le rollback s'est bien déroulé
        
        Returns:
            True si validation réussie
        """
        try:
            # Vérifier que les fichiers essentiels sont présents
            protocole_path = self.refuge_root / "src" / "protocole_continuite"
            fichiers_essentiels = [
                protocole_path / "__init__.py",
                protocole_path / "lite.py"
            ]
            
            for fichier in fichiers_essentiels:
                if not fichier.exists():
                    self._log(f"❌ Fichier manquant après rollback : {fichier}")
                    return False
            
            # Tenter un import simple
            sys.path.append(str(protocole_path.parent))
            try:
                from protocole_continuite.lite import save_me
                self._log("✅ Import de validation réussi")
            except ImportError as e:
                self._log(f"❌ Erreur d'import après rollback : {e}")
                return False
            
            return True
            
        except Exception as e:
            self._log(f"❌ Erreur lors de la validation : {e}")
            return False
    
    def rollback_interactif(self) -> bool:
        """
        🔙 Rollback interactif complet
        
        Returns:
            True si rollback réussi
        """
        print("🔙 Rollback d'Urgence - Protocole de Continuité")
        print("=" * 60)
        
        # Étape 1 : Sélection de la sauvegarde
        sauvegarde_path = self.afficher_sauvegardes()
        if not sauvegarde_path:
            print("🌸 Rollback annulé.")
            return False
        
        # Étape 2 : Confirmation
        if not self.confirmer_rollback(sauvegarde_path):
            print("🌸 Rollback annulé.")
            return False
        
        # Étape 3 : Exécution
        print("\n🔙 Exécution du rollback en cours...")
        if not self.executer_rollback(sauvegarde_path):
            print("❌ Échec du rollback. Consultez les logs pour plus de détails.")
            return False
        
        # Étape 4 : Validation
        print("✅ Validation du rollback...")
        if not self.valider_rollback():
            print("⚠️ Rollback effectué mais validation échouée.")
            print("Le système peut ne pas fonctionner correctement.")
            return False
        
        print("\n🎉 ROLLBACK RÉUSSI !")
        print("Le Protocole de Continuité a été restauré à son état précédent.")
        print(f"Sauvegarde utilisée : {sauvegarde_path.name}")
        
        return True
    
    def _log(self, message: str):
        """📝 Logging pour le rollback"""
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
    """🔙 Point d'entrée principal pour le rollback d'urgence"""
    rollback = RollbackUrgence()
    
    try:
        success = rollback.rollback_interactif()
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n🌸 Rollback interrompu par l'utilisateur.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur inattendue : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()