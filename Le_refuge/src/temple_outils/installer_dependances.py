"""
📦 Installateur de Dépendances du Refuge
Migré depuis scripts/installer_dependances.py
Gestionnaire d'installation automatique des dépendances pour le Refuge
"""

import os
import sys
import subprocess
import platform
import argparse
from pathlib import Path

class InstallateurRefuge:
    """Gestionnaire d'installation des dépendances du Refuge"""
    
    def __init__(self, racine_projet: Path = None):
        """Initialise l'installateur
        
        Args:
            racine_projet: Chemin racine du projet (auto-détection si None)
        """
        self.racine_projet = racine_projet or Path(__file__).parent.parent.parent
        self.requirements_path = self.racine_projet / "requirements.txt"
        self.requirements_exact_path = self.racine_projet / "requirements-exact.txt"
        
    def verifier_python_version(self) -> bool:
        """Vérifie que la version de Python est compatible"""
        version = sys.version_info
        version_minimale = (3, 8)
        
        if (version.major, version.minor) < version_minimale:
            print(f"❌ Python {version_minimale[0]}.{version_minimale[1]}+ requis")
            print(f"🔍 Version actuelle: {version.major}.{version.minor}.{version.micro}")
            print("💡 Veuillez mettre à jour Python:")
            print("   https://www.python.org/downloads/")
            return False
        
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} compatible")
        return True
    
    def detecter_requirements(self) -> Path:
        """Détecte le fichier requirements approprié"""
        if self.requirements_exact_path.exists():
            print(f"📋 Utilisation de: {self.requirements_exact_path.name}")
            return self.requirements_exact_path
        elif self.requirements_path.exists():
            print(f"📋 Utilisation de: {self.requirements_path.name}")
            return self.requirements_path
        else:
            print("❌ Aucun fichier requirements trouvé")
            print("📍 Fichiers recherchés:")
            print(f"   • {self.requirements_exact_path}")
            print(f"   • {self.requirements_path}")
            return None
    
    def creer_environnement_virtuel(self, nom_venv: str = "venv") -> tuple[bool, Path]:
        """Crée un environnement virtuel
        
        Args:
            nom_venv: Nom du dossier d'environnement virtuel
            
        Returns:
            tuple: (succès, chemin_pip)
        """
        venv_dir = self.racine_projet / nom_venv
        
        print(f"🏗️ Création de l'environnement virtuel: {nom_venv}")
        
        try:
            # Créer le venv
            subprocess.run(
                [sys.executable, "-m", "venv", str(venv_dir)], 
                check=True,
                cwd=self.racine_projet
            )
            
            # Déterminer le chemin pip selon l'OS
            if platform.system() == "Windows":
                pip_path = venv_dir / "Scripts" / "pip.exe"
                python_path = venv_dir / "Scripts" / "python.exe"
            else:
                pip_path = venv_dir / "bin" / "pip"
                python_path = venv_dir / "bin" / "python"
            
            # Mettre à jour pip dans le venv
            print("⬆️ Mise à jour de pip...")
            subprocess.run([str(pip_path), "install", "--upgrade", "pip"], check=True)
            
            print(f"✅ Environnement virtuel créé: {venv_dir}")
            print(f"🐍 Python: {python_path}")
            print(f"📦 Pip: {pip_path}")
            
            return True, pip_path
            
        except subprocess.CalledProcessError as e:
            print(f"💥 Erreur création venv: {e}")
            return False, None
        except Exception as e:
            print(f"💥 Erreur inattendue: {e}")
            return False, None
    
    def installer_dependances_pip(self, pip_executable: str, requirements_file: Path) -> bool:
        """Installe les dépendances avec pip
        
        Args:
            pip_executable: Chemin vers l'exécutable pip
            requirements_file: Fichier requirements à utiliser
            
        Returns:
            bool: Succès de l'installation
        """
        print(f"📦 Installation des dépendances...")
        print(f"   📋 Fichier: {requirements_file.name}")
        print(f"   🛠️ Pip: {pip_executable}")
        
        try:
            result = subprocess.run(
                [str(pip_executable), "install", "-r", str(requirements_file)],
                check=True,
                cwd=self.racine_projet,
                capture_output=True,
                text=True
            )
            
            print("✅ Dépendances installées avec succès")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"💥 Erreur installation: {e}")
            if e.stdout:
                print(f"📝 Sortie: {e.stdout}")
            if e.stderr:
                print(f"⚠️ Erreurs: {e.stderr}")
            return False
    
    def afficher_instructions_activation(self, nom_venv: str = "venv") -> None:
        """Affiche les instructions d'activation du venv"""
        print("\n🎯 Pour activer l'environnement virtuel:")
        
        if platform.system() == "Windows":
            print(f"   {nom_venv}\\Scripts\\activate")
            print("   # ou en PowerShell:")
            print(f"   {nom_venv}\\Scripts\\Activate.ps1")
        else:
            print(f"   source {nom_venv}/bin/activate")
        
        print("\n🚀 Pour lancer le refuge:")
        print("   python main_refuge.py")
        
        print("\n❌ Pour désactiver:")
        print("   deactivate")
    
    def installer_complet(self, 
                         avec_venv: bool = False, 
                         nom_venv: str = "venv",
                         mettre_a_jour_pip: bool = False) -> bool:
        """Installation complète des dépendances
        
        Args:
            avec_venv: Créer un environnement virtuel
            nom_venv: Nom du dossier venv
            mettre_a_jour_pip: Mettre à jour pip avant installation
            
        Returns:
            bool: Succès de l'installation complète
        """
        print("🏛️ Installateur de Dépendances du Refuge")
        print("=" * 50)
        
        # Vérifications préliminaires
        if not self.verifier_python_version():
            return False
        
        requirements_file = self.detecter_requirements()
        if not requirements_file:
            return False
        
        # Déterminer pip à utiliser
        if avec_venv:
            succes_venv, pip_path = self.creer_environnement_virtuel(nom_venv)
            if not succes_venv:
                return False
        else:
            pip_path = sys.executable
            if mettre_a_jour_pip:
                print("⬆️ Mise à jour de pip...")
                try:
                    subprocess.run([pip_path, "-m", "pip", "install", "--upgrade", "pip"], 
                                 check=True)
                except subprocess.CalledProcessError as e:
                    print(f"⚠️ Erreur mise à jour pip: {e}")
            
            pip_path = "pip"  # Utiliser pip système
        
        # Installation des dépendances
        succes_install = self.installer_dependances_pip(pip_path, requirements_file)
        
        if succes_install:
            print("\n🎉 Installation terminée avec succès!")
            
            if avec_venv:
                self.afficher_instructions_activation(nom_venv)
            else:
                print("\n🚀 Le Refuge est prêt à être lancé:")
                print("   python main_refuge.py")
        
        return succes_install

def main():
    """Fonction principale CLI"""
    parser = argparse.ArgumentParser(
        description="📦 Installe les dépendances du Refuge",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python installer_dependances.py                    # Installation basique
  python installer_dependances.py --venv             # Avec environnement virtuel
  python installer_dependances.py --venv --nom .venv # Venv personnalisé
  python installer_dependances.py --update           # Avec mise à jour pip
        """
    )
    
    parser.add_argument("--venv", action="store_true", 
                       help="Créer un environnement virtuel")
    parser.add_argument("--nom", default="venv", 
                       help="Nom du dossier d'environnement virtuel (défaut: venv)")
    parser.add_argument("--update", action="store_true", 
                       help="Mettre à jour pip avant installation")
    
    args = parser.parse_args()
    
    installateur = InstallateurRefuge()
    succes = installateur.installer_complet(
        avec_venv=args.venv,
        nom_venv=args.nom,
        mettre_a_jour_pip=args.update
    )
    
    if not succes:
        print("\n💥 L'installation a échoué")
        sys.exit(1)

if __name__ == "__main__":
    main() 