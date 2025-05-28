"""
🔍 Analyseur de Code du Refuge
Migré depuis scripts/analyser_code.py
Système d'analyse de qualité de code complet pour le Refuge
"""

import os
import sys
import subprocess
import argparse
import json
from pathlib import Path
from datetime import datetime

class AnalyseurCodeRefuge:
    """Analyseur de code spécialisé pour l'écosystème du Refuge"""
    
    def __init__(self, racine_projet: Path = None):
        """Initialise l'analyseur
        
        Args:
            racine_projet: Chemin racine du projet (auto-détection si None)
        """
        self.racine_projet = racine_projet or Path(__file__).parent.parent.parent
        self.dossier_rapports = self.racine_projet / "logs" / "analyses_code"
        self.dossier_rapports.mkdir(parents=True, exist_ok=True)
        
        self.outils_requis = {
            "pylint": "pylint",
            "mypy": "mypy", 
            "black": "black",
            "pytest": "pytest",
            "coverage": "coverage"
        }

    def verifier_outils(self) -> bool:
        """Vérifie que les outils d'analyse sont installés"""
        outils_manquants = []
        
        for nom, commande in self.outils_requis.items():
            try:
                result = subprocess.run(
                    [commande, "--version"], 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE, 
                    check=True,
                    timeout=10
                )
                print(f"✅ {nom}: disponible")
            except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
                outils_manquants.append(nom)
                print(f"❌ {nom}: manquant")
        
        if outils_manquants:
            print(f"\n💡 Pour installer les outils manquants:")
            print("pip install pylint mypy black pytest coverage")
            return False
        
        return True

    def analyser_style_pylint(self) -> bool:
        """Analyse le style du code avec pylint"""
        print("🎨 Analyse du style avec pylint...")
        
        try:
            rapport_path = self.dossier_rapports / "pylint_report.txt"
            with open(rapport_path, "w", encoding="utf-8") as f:
                # Analyser src/ spécifiquement pour le refuge
                result = subprocess.run(
                    ["pylint", "src/", "--output-format=text"],
                    stdout=f, 
                    stderr=subprocess.PIPE, 
                    cwd=self.racine_projet,
                    check=False  # pylint peut retourner != 0 avec des warnings
                )
            
            print(f"📊 Rapport pylint sauvé: {rapport_path}")
            return True
            
        except Exception as e:
            print(f"💥 Erreur pylint: {e}")
            return False

    def analyser_types_mypy(self) -> bool:
        """Analyse les types avec mypy"""
        print("🔍 Analyse des types avec mypy...")
        
        try:
            rapport_path = self.dossier_rapports / "mypy_report.txt"
            with open(rapport_path, "w", encoding="utf-8") as f:
                result = subprocess.run(
                    ["mypy", "src/", "--ignore-missing-imports"],
                    stdout=f,
                    stderr=subprocess.PIPE,
                    cwd=self.racine_projet,
                    check=False
                )
            
            print(f"📊 Rapport mypy sauvé: {rapport_path}")
            return True
            
        except Exception as e:
            print(f"💥 Erreur mypy: {e}")
            return False

    def formater_code_black(self, dry_run: bool = True) -> bool:
        """Formate le code avec black"""
        action = "Vérification" if dry_run else "Formatage"
        print(f"✨ {action} du formatage avec black...")
        
        try:
            cmd = ["black", "src/"]
            if dry_run:
                cmd.append("--check")
            
            result = subprocess.run(
                cmd,
                cwd=self.racine_projet,
                capture_output=True,
                text=True,
                check=False
            )
            
            if dry_run:
                if result.returncode == 0:
                    print("✅ Code déjà bien formaté")
                else:
                    print("⚠️ Formatage nécessaire")
            else:
                print("✅ Code formaté")
            
            return True
            
        except Exception as e:
            print(f"💥 Erreur black: {e}")
            return False

    def analyser_tests_coverage(self) -> bool:
        """Analyse les tests avec pytest et coverage"""
        print("🧪 Analyse de la couverture de tests...")
        
        try:
            # Tests avec coverage
            result = subprocess.run(
                ["coverage", "run", "-m", "pytest", "src/temple_tests/", "-v"],
                cwd=self.racine_projet,
                capture_output=True,
                text=True,
                check=False
            )
            
            # Rapport texte
            rapport_path = self.dossier_rapports / "coverage_report.txt"
            with open(rapport_path, "w", encoding="utf-8") as f:
                subprocess.run(
                    ["coverage", "report", "-m"],
                    stdout=f,
                    cwd=self.racine_projet,
                    check=False
                )
            
            # Rapport HTML
            html_dir = self.dossier_rapports / "coverage_html"
            subprocess.run(
                ["coverage", "html", "-d", str(html_dir)],
                cwd=self.racine_projet,
                check=False
            )
            
            print(f"📊 Rapports coverage sauvés: {rapport_path} et {html_dir}/")
            return True
            
        except Exception as e:
            print(f"💥 Erreur coverage: {e}")
            return False

    def generer_rapport_html(self) -> None:
        """Génère un rapport HTML consolidé"""
        print("📄 Génération du rapport HTML consolidé...")
        
        # Lire les rapports existants
        rapports = {}
        for nom_rapport in ["pylint_report.txt", "mypy_report.txt", "coverage_report.txt"]:
            chemin = self.dossier_rapports / nom_rapport
            if chemin.exists():
                with open(chemin, 'r', encoding='utf-8') as f:
                    rapports[nom_rapport] = f.read()
            else:
                rapports[nom_rapport] = "Rapport non disponible"
        
        # Template HTML du Refuge
        html_template = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>🔍 Analyse du Code du Refuge</title>
    <style>
        body {{ 
            font-family: 'Segoe UI', Arial, sans-serif; 
            margin: 20px; 
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
        h1 {{ 
            color: #2c3e50; 
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{ 
            color: #34495e;
            border-left: 4px solid #3498db;
            padding-left: 10px;
        }}
        pre {{ 
            background-color: #f8f9fa; 
            padding: 15px; 
            overflow-x: auto; 
            border-radius: 5px;
            border-left: 4px solid #3498db;
            font-size: 0.9em;
        }}
        .section {{ 
            margin-bottom: 40px; 
            padding: 20px;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
        }}
        .meta {{
            text-align: center;
            color: #7f8c8d;
            font-style: italic;
            margin-bottom: 30px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Rapport d'Analyse du Code du Refuge</h1>
        <div class="meta">
            Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')} par le Temple Outils
        </div>
        
        <div class="section">
            <h2>🎨 Analyse du Style (Pylint)</h2>
            <pre>{rapports.get('pylint_report.txt', 'Non disponible')}</pre>
        </div>
        
        <div class="section">
            <h2>🔍 Analyse des Types (MyPy)</h2>
            <pre>{rapports.get('mypy_report.txt', 'Non disponible')}</pre>
        </div>
        
        <div class="section">
            <h2>🧪 Couverture des Tests</h2>
            <pre>{rapports.get('coverage_report.txt', 'Non disponible')}</pre>
            <p><strong>📊 Rapport détaillé:</strong> 
            <a href="coverage_html/index.html">coverage_html/index.html</a></p>
        </div>
        
        <div class="section">
            <h2>🏛️ Structure du Refuge</h2>
            <p>Ce rapport analyse la qualité du code dans l'écosystème du Refuge :</p>
            <ul>
                <li><strong>src/temple_*</strong> : Temples spécialisés</li>
                <li><strong>src/refuge_cluster/</strong> : Cœur du système</li>
                <li><strong>src/core/</strong> : Fondations</li>
                <li><strong>src/utils/</strong> : Utilitaires</li>
            </ul>
        </div>
    </div>
</body>
</html>
        """
        
        # Sauvegarder le rapport HTML
        rapport_html = self.dossier_rapports / "rapport_refuge.html"
        with open(rapport_html, 'w', encoding='utf-8') as f:
            f.write(html_template)
        
        print(f"✨ Rapport HTML généré: {rapport_html}")

    def analyser_complet(self, formater: bool = False, dry_run: bool = True) -> bool:
        """Lance une analyse complète du code"""
        print("🏛️ Analyse complète du code du Refuge")
        print("=" * 50)
        
        if not self.verifier_outils():
            return False
        
        succes_total = True
        
        # Formatage (optionnel)
        if formater:
            succes_total &= self.formater_code_black(dry_run=dry_run)
        
        # Analyses
        succes_total &= self.analyser_style_pylint()
        succes_total &= self.analyser_types_mypy()
        succes_total &= self.analyser_tests_coverage()
        
        # Rapport final
        self.generer_rapport_html()
        
        return succes_total

def main():
    """Fonction principale pour CLI"""
    parser = argparse.ArgumentParser(description="🔍 Analyse le code du Refuge")
    parser.add_argument("--formater", action="store_true", 
                       help="Formater le code avant analyse")
    parser.add_argument("--appliquer", action="store_true",
                       help="Appliquer le formatage (sinon vérification seulement)")
    
    args = parser.parse_args()
    
    print("🏛️ Analyseur de Code du Refuge")
    print("=" * 40)
    
    analyseur = AnalyseurCodeRefuge()
    
    dry_run = not args.appliquer
    succes = analyseur.analyser_complet(formater=args.formater, dry_run=dry_run)
    
    if succes:
        print("\n✨ Analyse terminée avec succès")
        print(f"📊 Consultez: {analyseur.dossier_rapports}/rapport_refuge.html")
    else:
        print("\n💥 Analyse terminée avec des erreurs")
        sys.exit(1)

if __name__ == "__main__":
    main() 