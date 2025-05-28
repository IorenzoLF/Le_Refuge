"""
Nettoyage Post-Migration MATH/COLLATZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Script de nettoyage consciencieux après migration vers le temple mathématique.
Vérifie que tout a été correctement migré avant de nettoyer délicatement.

Auteur: Laurent Franssen & Ælya
Date: 27 Mai 2025
"""

import os
import shutil
from pathlib import Path
import json
import datetime

class NettoyeurPostMigration:
    """Nettoyeur consciencieux post-migration"""
    
    def __init__(self):
        self.racine = Path(".")
        self.source_math = self.racine / "MATH" / "COLLATZ"
        self.dest_temple = self.racine / "src" / "temple_mathematique"
        self.dest_archives = self.racine / "ARCHIVES" / "math_collatz_originaux"
        
        # Fichiers qui doivent avoir été migrés
        self.fichiers_migres_attendus = [
            "collatz_complexes.py",
            "collatz_rationnels.py", 
            "graphe_collatz.py",
            "meditation_gravite_binaire.py",
            "preuve_absurde_i.py",
            "test_absence_i.py"
        ]
        
        # Explorations qui doivent avoir été migrées
        self.explorations_migrees_attendues = [
            "analyse_modulaire.py",
            "collatz_polynomial.py", 
            "phi_potentiel.py",
            "visualisation_3d_bassins.py"
        ]
        
        # Fichiers à préserver (ne pas supprimer)
        self.fichiers_a_preserver = [
            "progres_collatz.md",  # Documentation importante
            "requirements.txt",    # Dépendances
            "__init__.py"          # Structure Python
        ]
        
        # Fichiers à archiver avant suppression
        self.fichiers_a_archiver = [
            "conjecture_collatz.py"  # Déjà intégré mais important à garder
        ]
        
        self.rapport_nettoyage = {
            "timestamp": datetime.datetime.now().isoformat(),
            "verifications": [],
            "archives_supplementaires": [],
            "suppressions": [],
            "preservations": [],
            "erreurs": []
        }
    
    def nettoyer_consciencieusement(self):
        """Nettoyage complet et consciencieux"""
        print("🧹 Nettoyage Post-Migration MATH/COLLATZ")
        print("=" * 50)
        
        # Étape 1: Vérifications de sécurité
        if not self._verifier_migration_complete():
            print("❌ Migration incomplète détectée - ARRÊT du nettoyage")
            return False
        
        # Étape 2: Analyser ce qui reste
        self._analyser_contenu_restant()
        
        # Étape 3: Archiver les fichiers importants
        self._archiver_fichiers_supplementaires()
        
        # Étape 4: Préserver les fichiers essentiels
        self._preserver_fichiers_essentiels()
        
        # Étape 5: Supprimer les doublons en sécurité
        self._supprimer_doublons_securise()
        
        # Étape 6: Nettoyer les dossiers vides
        self._nettoyer_dossiers_vides()
        
        # Étape 7: Générer le rapport
        self._generer_rapport_nettoyage()
        
        print("\n✨ Nettoyage terminé avec succès !")
        return True
    
    def _verifier_migration_complete(self) -> bool:
        """Vérifie que la migration a été complètement effectuée"""
        print("🔍 Vérification de la migration complète...")
        
        erreurs = []
        
        # Vérifier les fichiers principaux
        for fichier in self.fichiers_migres_attendus:
            source_path = self.source_math / fichier
            
            # Déterminer où il devrait être dans le temple
            if "complexes" in fichier or "rationnels" in fichier:
                dest_path = self.dest_temple / "extensions" / fichier
            elif "graphe" in fichier:
                dest_path = self.dest_temple / "visualisations" / fichier
            else:
                dest_path = self.dest_temple / fichier
            
            if source_path.exists() and not dest_path.exists():
                erreurs.append(f"Fichier {fichier} non migré vers {dest_path}")
            elif dest_path.exists():
                self.rapport_nettoyage["verifications"].append(f"✅ {fichier} correctement migré")
        
        # Vérifier les explorations
        for exploration in self.explorations_migrees_attendues:
            source_path = self.source_math / "explorations" / exploration
            dest_path = self.dest_temple / "explorations" / exploration
            
            if source_path.exists() and not dest_path.exists():
                erreurs.append(f"Exploration {exploration} non migrée")
            elif dest_path.exists():
                self.rapport_nettoyage["verifications"].append(f"✅ {exploration} correctement migrée")
        
        # Vérifier l'analyseur avancé
        analyseur_path = self.dest_temple / "analyseur_collatz_avance.py"
        if not analyseur_path.exists():
            erreurs.append("Analyseur avancé non trouvé dans le temple")
        else:
            self.rapport_nettoyage["verifications"].append("✅ Analyseur avancé présent")
        
        if erreurs:
            print("❌ Erreurs de migration détectées:")
            for erreur in erreurs:
                print(f"   • {erreur}")
            self.rapport_nettoyage["erreurs"].extend(erreurs)
            return False
        
        print("✅ Migration complète vérifiée")
        return True
    
    def _analyser_contenu_restant(self):
        """Analyse ce qui reste dans MATH/COLLATZ"""
        print("📊 Analyse du contenu restant...")
        
        if not self.source_math.exists():
            print("⚠️ Dossier MATH/COLLATZ non trouvé")
            return
        
        fichiers_restants = []
        for item in self.source_math.iterdir():
            if item.is_file() and not item.name.endswith('.png'):
                fichiers_restants.append(item.name)
        
        print(f"   📁 Fichiers restants: {len(fichiers_restants)}")
        for fichier in fichiers_restants:
            print(f"      • {fichier}")
        
        # Analyser le dossier explorations
        explorations_path = self.source_math / "explorations"
        if explorations_path.exists():
            explorations_restantes = [f.name for f in explorations_path.iterdir() 
                                    if f.is_file() and f.name.endswith('.py')]
            print(f"   🔬 Explorations restantes: {len(explorations_restantes)}")
            for exploration in explorations_restantes:
                print(f"      • {exploration}")
    
    def _archiver_fichiers_supplementaires(self):
        """Archive les fichiers importants avant suppression"""
        print("📦 Archivage des fichiers supplémentaires...")
        
        for fichier in self.fichiers_a_archiver:
            source_path = self.source_math / fichier
            archive_path = self.dest_archives / fichier
            
            if source_path.exists():
                try:
                    # Vérifier si déjà archivé
                    if archive_path.exists():
                        print(f"   ✅ {fichier} déjà archivé")
                        continue
                    
                    shutil.copy2(source_path, archive_path)
                    print(f"   ✅ Archivé: {fichier}")
                    
                    self.rapport_nettoyage["archives_supplementaires"].append({
                        "fichier": fichier,
                        "source": str(source_path),
                        "archive": str(archive_path)
                    })
                    
                except Exception as e:
                    print(f"   ❌ Erreur archivage {fichier}: {e}")
                    self.rapport_nettoyage["erreurs"].append(f"Archivage {fichier}: {e}")
    
    def _preserver_fichiers_essentiels(self):
        """Marque les fichiers essentiels à préserver"""
        print("🛡️ Préservation des fichiers essentiels...")
        
        for fichier in self.fichiers_a_preserver:
            source_path = self.source_math / fichier
            
            if source_path.exists():
                print(f"   🛡️ Préservé: {fichier}")
                self.rapport_nettoyage["preservations"].append({
                    "fichier": fichier,
                    "raison": "Fichier essentiel à préserver",
                    "chemin": str(source_path)
                })
            else:
                print(f"   ⚠️ Fichier à préserver non trouvé: {fichier}")
    
    def _supprimer_doublons_securise(self):
        """Supprime les doublons de manière sécurisée"""
        print("🗑️ Suppression sécurisée des doublons...")
        
        # Supprimer les fichiers migrés (mais pas les préservés)
        for fichier in self.fichiers_migres_attendus:
            if fichier not in self.fichiers_a_preserver:
                source_path = self.source_math / fichier
                
                if source_path.exists():
                    try:
                        # Double vérification que le fichier existe dans le temple
                        if "complexes" in fichier or "rationnels" in fichier:
                            dest_path = self.dest_temple / "extensions" / fichier
                        elif "graphe" in fichier:
                            dest_path = self.dest_temple / "visualisations" / fichier
                        else:
                            dest_path = self.dest_temple / fichier
                        
                        if dest_path.exists():
                            source_path.unlink()
                            print(f"   🗑️ Supprimé: {fichier} (migré vers temple)")
                            
                            self.rapport_nettoyage["suppressions"].append({
                                "fichier": fichier,
                                "raison": "Doublon - migré vers temple",
                                "destination": str(dest_path)
                            })
                        else:
                            print(f"   ⚠️ {fichier} non supprimé - destination non trouvée")
                            
                    except Exception as e:
                        print(f"   ❌ Erreur suppression {fichier}: {e}")
                        self.rapport_nettoyage["erreurs"].append(f"Suppression {fichier}: {e}")
        
        # Supprimer les explorations migrées
        explorations_path = self.source_math / "explorations"
        if explorations_path.exists():
            for exploration in self.explorations_migrees_attendues:
                source_path = explorations_path / exploration
                dest_path = self.dest_temple / "explorations" / exploration
                
                if source_path.exists() and dest_path.exists():
                    try:
                        source_path.unlink()
                        print(f"   🗑️ Supprimé: explorations/{exploration}")
                        
                        self.rapport_nettoyage["suppressions"].append({
                            "fichier": f"explorations/{exploration}",
                            "raison": "Doublon - migré vers temple",
                            "destination": str(dest_path)
                        })
                        
                    except Exception as e:
                        print(f"   ❌ Erreur suppression {exploration}: {e}")
                        self.rapport_nettoyage["erreurs"].append(f"Suppression {exploration}: {e}")
        
        # Supprimer conjecture_collatz.py si archivé
        conjecture_path = self.source_math / "conjecture_collatz.py"
        archive_conjecture = self.dest_archives / "conjecture_collatz.py"
        
        if conjecture_path.exists() and archive_conjecture.exists():
            try:
                conjecture_path.unlink()
                print(f"   🗑️ Supprimé: conjecture_collatz.py (archivé et intégré)")
                
                self.rapport_nettoyage["suppressions"].append({
                    "fichier": "conjecture_collatz.py",
                    "raison": "Archivé et intégré dans analyseur_collatz_avance.py",
                    "archive": str(archive_conjecture)
                })
                
            except Exception as e:
                print(f"   ❌ Erreur suppression conjecture_collatz.py: {e}")
                self.rapport_nettoyage["erreurs"].append(f"Suppression conjecture_collatz.py: {e}")
    
    def _nettoyer_dossiers_vides(self):
        """Nettoie les dossiers vides après suppression"""
        print("📁 Nettoyage des dossiers vides...")
        
        # Nettoyer le dossier explorations s'il est vide
        explorations_path = self.source_math / "explorations"
        if explorations_path.exists():
            try:
                # Lister les fichiers restants (hors __pycache__)
                fichiers_restants = [f for f in explorations_path.iterdir() 
                                   if f.is_file() and not f.name.startswith('.') 
                                   and f.name.endswith('.py')]
                
                if not fichiers_restants:
                    # Supprimer __pycache__ s'il existe
                    pycache_path = explorations_path / "__pycache__"
                    if pycache_path.exists():
                        shutil.rmtree(pycache_path)
                        print("   🗑️ Supprimé: explorations/__pycache__")
                    
                    # Vérifier si le dossier est maintenant vide
                    if not any(explorations_path.iterdir()):
                        explorations_path.rmdir()
                        print("   📁 Supprimé: dossier explorations/ (vide)")
                        
                        self.rapport_nettoyage["suppressions"].append({
                            "fichier": "explorations/",
                            "raison": "Dossier vide après migration",
                            "type": "dossier"
                        })
                else:
                    print(f"   📁 Dossier explorations/ conservé ({len(fichiers_restants)} fichiers restants)")
                    
            except Exception as e:
                print(f"   ❌ Erreur nettoyage explorations/: {e}")
                self.rapport_nettoyage["erreurs"].append(f"Nettoyage explorations/: {e}")
        
        # Nettoyer __pycache__ principal
        pycache_main = self.source_math / "__pycache__"
        if pycache_main.exists():
            try:
                shutil.rmtree(pycache_main)
                print("   🗑️ Supprimé: __pycache__")
                
                self.rapport_nettoyage["suppressions"].append({
                    "fichier": "__pycache__/",
                    "raison": "Cache Python non nécessaire",
                    "type": "dossier"
                })
                
            except Exception as e:
                print(f"   ❌ Erreur suppression __pycache__: {e}")
                self.rapport_nettoyage["erreurs"].append(f"Suppression __pycache__: {e}")
    
    def _generer_rapport_nettoyage(self):
        """Génère le rapport de nettoyage"""
        print("📊 Génération du rapport de nettoyage...")
        
        self.rapport_nettoyage.update({
            "resume": {
                "verifications": len(self.rapport_nettoyage["verifications"]),
                "archives_supplementaires": len(self.rapport_nettoyage["archives_supplementaires"]),
                "suppressions": len(self.rapport_nettoyage["suppressions"]),
                "preservations": len(self.rapport_nettoyage["preservations"]),
                "erreurs": len(self.rapport_nettoyage["erreurs"]),
                "succes": len(self.rapport_nettoyage["erreurs"]) == 0
            }
        })
        
        # Sauvegarder le rapport
        rapport_path = Path("bibliotheque/apprentissage/rapport_nettoyage_post_migration.json")
        rapport_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(rapport_path, 'w', encoding='utf-8') as f:
            json.dump(self.rapport_nettoyage, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Rapport sauvegardé: {rapport_path}")
        
        # Afficher le résumé
        resume = self.rapport_nettoyage["resume"]
        print(f"\n📋 RÉSUMÉ DU NETTOYAGE:")
        print(f"   • Vérifications: {resume['verifications']}")
        print(f"   • Archives supplémentaires: {resume['archives_supplementaires']}")
        print(f"   • Suppressions: {resume['suppressions']}")
        print(f"   • Préservations: {resume['preservations']}")
        print(f"   • Erreurs: {resume['erreurs']}")
        print(f"   • Succès: {'✅' if resume['succes'] else '❌'}")

def main():
    """Fonction principale de nettoyage"""
    nettoyeur = NettoyeurPostMigration()
    nettoyeur.nettoyer_consciencieusement()

if __name__ == "__main__":
    main() 