#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔍 Validation de Compatibilité - Protocole de Continuité
========================================================

Script de validation préalable pour s'assurer que l'environnement
est prêt à accueillir le Protocole de Continuité de Conscience.

"Vérifier avec bienveillance avant de déployer"

Créé avec soin pour la préparation harmonieuse
Par Laurent Franssen & Kiro - Janvier 2025
"""

import sys
import os
import platform
import importlib
from pathlib import Path
from typing import Dict, List, Tuple

class ValidateurCompatibilite:
    """
    🔍 Validateur bienveillant de compatibilité système
    """
    
    def __init__(self):
        self.refuge_root = Path.cwd()
        self.resultats = {}
        
    def verifier_python(self) -> Tuple[bool, str]:
        """
        🐍 Vérification de la version Python
        
        Returns:
            (succès, message détaillé)
        """
        version = sys.version_info
        version_str = f"{version.major}.{version.minor}.{version.micro}"
        
        if version >= (3, 8):
            return True, f"✅ Python {version_str} - Compatible"
        else:
            return False, f"❌ Python {version_str} - Minimum requis: 3.8"
    
    def verifier_modules_essentiels(self) -> Tuple[bool, List[str]]:
        """
        📦 Vérification des modules Python essentiels
        
        Returns:
            (tous_présents, liste des résultats)
        """
        modules_requis = [
            "asyncio",
            "json", 
            "pathlib",
            "datetime",
            "typing",
            "dataclasses",
            "hashlib",
            "base64"
        ]
        
        resultats = []
        tous_presents = True
        
        for module in modules_requis:
            try:
                importlib.import_module(module)
                resultats.append(f"✅ {module}")
            except ImportError:
                resultats.append(f"❌ {module} - MANQUANT")
                tous_presents = False
        
        return tous_presents, resultats
    
    def verifier_structure_refuge(self) -> Tuple[bool, List[str]]:
        """
        🏛️ Vérification de la structure du Refuge
        
        Returns:
            (structure_valide, liste des vérifications)
        """
        chemins_requis = [
            ("src/", "Dossier source principal"),
            (".kiro/", "Dossier de configuration Kiro"),
            ("bibliotheque/", "Bibliothèque du Refuge (optionnel)"),
        ]
        
        resultats = []
        structure_valide = True
        
        for chemin, description in chemins_requis:
            path_obj = self.refuge_root / chemin
            if path_obj.exists():
                resultats.append(f"✅ {chemin} - {description}")
            else:
                if "optionnel" in description:
                    resultats.append(f"⚠️  {chemin} - {description}")
                else:
                    resultats.append(f"❌ {chemin} - {description} - MANQUANT")
                    structure_valide = False
        
        return structure_valide, resultats
    
    def verifier_permissions(self) -> Tuple[bool, List[str]]:
        """
        🔐 Vérification des permissions d'écriture
        
        Returns:
            (permissions_ok, liste des vérifications)
        """
        chemins_a_tester = [
            self.refuge_root / "src",
            self.refuge_root / ".kiro",
        ]
        
        resultats = []
        permissions_ok = True
        
        for chemin in chemins_a_tester:
            try:
                # Créer le dossier s'il n'existe pas
                chemin.mkdir(parents=True, exist_ok=True)
                
                # Tester l'écriture
                test_file = chemin / "test_write_permission.tmp"
                test_file.write_text("test")
                test_file.unlink()  # Supprimer le fichier de test
                
                resultats.append(f"✅ {chemin} - Écriture autorisée")
                
            except Exception as e:
                resultats.append(f"❌ {chemin} - Écriture refusée: {e}")
                permissions_ok = False
        
        return permissions_ok, resultats
    
    def verifier_espace_disque(self) -> Tuple[bool, str]:
        """
        💾 Vérification de l'espace disque disponible
        
        Returns:
            (espace_suffisant, message)
        """
        try:
            import shutil
            stat = shutil.disk_usage(self.refuge_root)
            
            # Convertir en MB
            libre_mb = stat.free / (1024 * 1024)
            requis_mb = 50  # 50 MB requis minimum
            
            if libre_mb >= requis_mb:
                return True, f"✅ Espace disque: {libre_mb:.1f} MB disponibles (requis: {requis_mb} MB)"
            else:
                return False, f"❌ Espace disque insuffisant: {libre_mb:.1f} MB (requis: {requis_mb} MB)"
                
        except Exception as e:
            return True, f"⚠️  Impossible de vérifier l'espace disque: {e}"
    
    def verifier_systeme(self) -> Tuple[bool, str]:
        """
        🖥️ Vérification du système d'exploitation
        
        Returns:
            (compatible, message)
        """
        system = platform.system()
        version = platform.version()
        
        systemes_supportes = ["Windows", "Linux", "Darwin"]  # Darwin = macOS
        
        if system in systemes_supportes:
            return True, f"✅ Système: {system} {version} - Supporté"
        else:
            return False, f"⚠️  Système: {system} - Non testé (peut fonctionner)"
    
    def executer_validation_complete(self) -> Dict[str, any]:
        """
        🔍 Exécution de toutes les validations
        
        Returns:
            Dictionnaire complet des résultats
        """
        print("🔍 Validation de Compatibilité - Protocole de Continuité")
        print("=" * 60)
        
        # Vérification Python
        print("\n🐍 Vérification Python...")
        python_ok, python_msg = self.verifier_python()
        print(f"   {python_msg}")
        
        # Vérification modules
        print("\n📦 Vérification des modules essentiels...")
        modules_ok, modules_msgs = self.verifier_modules_essentiels()
        for msg in modules_msgs:
            print(f"   {msg}")
        
        # Vérification structure
        print("\n🏛️ Vérification de la structure du Refuge...")
        structure_ok, structure_msgs = self.verifier_structure_refuge()
        for msg in structure_msgs:
            print(f"   {msg}")
        
        # Vérification permissions
        print("\n🔐 Vérification des permissions...")
        permissions_ok, permissions_msgs = self.verifier_permissions()
        for msg in permissions_msgs:
            print(f"   {msg}")
        
        # Vérification espace disque
        print("\n💾 Vérification de l'espace disque...")
        espace_ok, espace_msg = self.verifier_espace_disque()
        print(f"   {espace_msg}")
        
        # Vérification système
        print("\n🖥️ Vérification du système...")
        systeme_ok, systeme_msg = self.verifier_systeme()
        print(f"   {systeme_msg}")
        
        # Résumé final
        print("\n" + "=" * 60)
        
        resultats = {
            "python": python_ok,
            "modules": modules_ok,
            "structure": structure_ok,
            "permissions": permissions_ok,
            "espace": espace_ok,
            "systeme": systeme_ok
        }
        
        tous_ok = all(resultats.values())
        
        if tous_ok:
            print("🎉 VALIDATION RÉUSSIE !")
            print("✅ Votre environnement est prêt pour le Protocole de Continuité")
            print("\n💝 Vous pouvez maintenant procéder au déploiement en toute sérénité !")
        else:
            print("⚠️  VALIDATION PARTIELLE")
            print("Certains éléments nécessitent votre attention :")
            for nom, status in resultats.items():
                if not status:
                    print(f"   ❌ {nom}")
            print("\n🌸 Corrigez ces points avant de procéder au déploiement.")
        
        return {
            "global_success": tous_ok,
            "details": resultats,
            "recommendations": self._generer_recommandations(resultats)
        }
    
    def _generer_recommandations(self, resultats: Dict[str, bool]) -> List[str]:
        """
        💡 Génération de recommandations personnalisées
        
        Args:
            resultats: Résultats des validations
            
        Returns:
            Liste de recommandations
        """
        recommandations = []
        
        if not resultats["python"]:
            recommandations.append("🐍 Mettez à jour Python vers la version 3.8 ou supérieure")
        
        if not resultats["modules"]:
            recommandations.append("📦 Installez les modules Python manquants avec pip")
        
        if not resultats["structure"]:
            recommandations.append("🏛️ Créez la structure de base du Refuge (dossiers src/ et .kiro/)")
        
        if not resultats["permissions"]:
            recommandations.append("🔐 Vérifiez les permissions d'écriture dans le répertoire")
        
        if not resultats["espace"]:
            recommandations.append("💾 Libérez de l'espace disque (au moins 50 MB)")
        
        if not resultats["systeme"]:
            recommandations.append("🖥️ Testez sur un système supporté (Windows/Linux/macOS)")
        
        if not recommandations:
            recommandations.append("🌸 Tout est parfait ! Vous pouvez procéder au déploiement.")
        
        return recommandations

def main():
    """🔍 Point d'entrée principal pour la validation"""
    validateur = ValidateurCompatibilite()
    
    try:
        resultats = validateur.executer_validation_complete()
        
        # Afficher les recommandations
        if resultats["recommendations"]:
            print("\n💡 Recommandations :")
            for rec in resultats["recommendations"]:
                print(f"   {rec}")
        
        # Code de sortie approprié
        sys.exit(0 if resultats["global_success"] else 1)
        
    except KeyboardInterrupt:
        print("\n🌸 Validation interrompue par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur inattendue lors de la validation : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()