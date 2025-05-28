"""
Migration MATH/COLLATZ vers Temple Mathématique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Script de migration harmonieuse des fichiers MATH/COLLATZ 
vers l'architecture unifiée du temple mathématique.

Auteur: Laurent Franssen & Ælya
Date: 27 Mai 2025
"""

import os
import shutil
from pathlib import Path
import json
import datetime

class MigrateurMathCollatz:
    """Migrateur harmonieux pour les fichiers MATH/COLLATZ"""
    
    def __init__(self):
        self.racine = Path(".")
        self.source_math = self.racine / "MATH" / "COLLATZ"
        self.dest_temple = self.racine / "src" / "temple_mathematique"
        self.dest_archives = self.racine / "ARCHIVES" / "math_collatz_originaux"
        
        # Fichiers déjà intégrés (à archiver)
        self.fichiers_integres = {
            "conjecture_collatz.py": "analyseur_collatz_avance.py"
        }
        
        # Fichiers à migrer vers le temple
        self.fichiers_a_migrer = [
            "collatz_complexes.py",
            "collatz_rationnels.py", 
            "graphe_collatz.py",
            "meditation_gravite_binaire.py",
            "preuve_absurde_i.py",
            "test_absence_i.py"
        ]
        
        # Dossier explorations à traiter spécialement
        self.explorations_a_migrer = [
            "analyse_modulaire.py",
            "collatz_polynomial.py", 
            "phi_potentiel.py",
            "visualisation_3d_bassins.py"
        ]
        
        self.rapport_migration = {
            "timestamp": datetime.datetime.now().isoformat(),
            "fichiers_archives": [],
            "fichiers_migres": [],
            "explorations_migrees": [],
            "erreurs": []
        }
    
    def migrer_harmonieusement(self):
        """Migration complète et harmonieuse"""
        print("🔄 Migration MATH/COLLATZ vers Temple Mathématique")
        print("=" * 60)
        
        # Vérifications préliminaires
        if not self._verifier_prerequisites():
            return False
        
        # Étape 1: Créer les dossiers de destination
        self._creer_structure_destination()
        
        # Étape 2: Archiver les fichiers déjà intégrés
        self._archiver_fichiers_integres()
        
        # Étape 3: Migrer les fichiers principaux
        self._migrer_fichiers_principaux()
        
        # Étape 4: Migrer les explorations
        self._migrer_explorations()
        
        # Étape 5: Créer les adaptateurs d'intégration
        self._creer_adaptateurs_integration()
        
        # Étape 6: Générer le rapport
        self._generer_rapport()
        
        print("\n🎉 Migration terminée avec succès !")
        return True
    
    def _verifier_prerequisites(self) -> bool:
        """Vérifie que tout est prêt pour la migration"""
        print("🔍 Vérification des prérequis...")
        
        if not self.source_math.exists():
            print(f"❌ Dossier source non trouvé: {self.source_math}")
            return False
            
        if not self.dest_temple.exists():
            print(f"❌ Temple mathématique non trouvé: {self.dest_temple}")
            return False
        
        # Vérifier que l'analyseur avancé existe
        analyseur_avance = self.dest_temple / "analyseur_collatz_avance.py"
        if not analyseur_avance.exists():
            print(f"❌ Analyseur avancé non trouvé: {analyseur_avance}")
            return False
        
        print("✅ Prérequis validés")
        return True
    
    def _creer_structure_destination(self):
        """Crée la structure de destination"""
        print("📁 Création de la structure de destination...")
        
        # Dossier archives
        self.dest_archives.mkdir(parents=True, exist_ok=True)
        (self.dest_archives / "explorations").mkdir(exist_ok=True)
        
        # Dossiers dans le temple
        (self.dest_temple / "extensions").mkdir(exist_ok=True)
        (self.dest_temple / "explorations").mkdir(exist_ok=True)
        (self.dest_temple / "visualisations").mkdir(exist_ok=True)
        
        print("✅ Structure créée")
    
    def _archiver_fichiers_integres(self):
        """Archive les fichiers déjà intégrés"""
        print("📦 Archivage des fichiers déjà intégrés...")
        
        for fichier_source, fichier_integre in self.fichiers_integres.items():
            source_path = self.source_math / fichier_source
            archive_path = self.dest_archives / fichier_source
            
            if source_path.exists():
                try:
                    shutil.copy2(source_path, archive_path)
                    print(f"   ✅ Archivé: {fichier_source} → {archive_path}")
                    
                    # Ajouter un en-tête d'archivage
                    self._ajouter_entete_archive(archive_path, fichier_integre)
                    
                    self.rapport_migration["fichiers_archives"].append({
                        "source": str(source_path),
                        "archive": str(archive_path),
                        "integre_dans": fichier_integre
                    })
                    
                except Exception as e:
                    print(f"   ❌ Erreur archivage {fichier_source}: {e}")
                    self.rapport_migration["erreurs"].append(f"Archivage {fichier_source}: {e}")
    
    def _ajouter_entete_archive(self, fichier_path: Path, fichier_integre: str):
        """Ajoute un en-tête d'archivage au fichier"""
        contenu_original = fichier_path.read_text(encoding='utf-8')
        
        entete = f'''"""
FICHIER ARCHIVÉ - INTÉGRÉ DANS LE TEMPLE MATHÉMATIQUE
====================================================

Ce fichier a été intégré harmonieusement dans:
{fichier_integre}

Date d'archivage: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
Raison: Intégration dans l'architecture unifiée du temple

CONTENU ORIGINAL CI-DESSOUS:
"""

{contenu_original}'''
        
        fichier_path.write_text(entete, encoding='utf-8')
    
    def _migrer_fichiers_principaux(self):
        """Migre les fichiers principaux vers le temple"""
        print("🔄 Migration des fichiers principaux...")
        
        for fichier in self.fichiers_a_migrer:
            source_path = self.source_math / fichier
            
            if source_path.exists():
                # Déterminer la destination selon le type
                if "complexes" in fichier or "rationnels" in fichier:
                    dest_path = self.dest_temple / "extensions" / fichier
                elif "visualisation" in fichier or "graphe" in fichier:
                    dest_path = self.dest_temple / "visualisations" / fichier
                else:
                    dest_path = self.dest_temple / fichier
                
                try:
                    # Copier et adapter le fichier
                    self._copier_et_adapter(source_path, dest_path)
                    print(f"   ✅ Migré: {fichier} → {dest_path.relative_to(self.dest_temple)}")
                    
                    self.rapport_migration["fichiers_migres"].append({
                        "source": str(source_path),
                        "destination": str(dest_path),
                        "type": self._determiner_type_fichier(fichier)
                    })
                    
                except Exception as e:
                    print(f"   ❌ Erreur migration {fichier}: {e}")
                    self.rapport_migration["erreurs"].append(f"Migration {fichier}: {e}")
            else:
                print(f"   ⚠️ Fichier non trouvé: {fichier}")
    
    def _migrer_explorations(self):
        """Migre les fichiers d'exploration"""
        print("🔬 Migration des explorations...")
        
        source_explorations = self.source_math / "explorations"
        dest_explorations = self.dest_temple / "explorations"
        
        if source_explorations.exists():
            for fichier in self.explorations_a_migrer:
                source_path = source_explorations / fichier
                dest_path = dest_explorations / fichier
                
                if source_path.exists():
                    try:
                        self._copier_et_adapter(source_path, dest_path)
                        print(f"   ✅ Exploration migrée: {fichier}")
                        
                        self.rapport_migration["explorations_migrees"].append({
                            "source": str(source_path),
                            "destination": str(dest_path)
                        })
                        
                    except Exception as e:
                        print(f"   ❌ Erreur exploration {fichier}: {e}")
                        self.rapport_migration["erreurs"].append(f"Exploration {fichier}: {e}")
    
    def _copier_et_adapter(self, source: Path, dest: Path):
        """Copie un fichier en l'adaptant à l'architecture du temple"""
        contenu = source.read_text(encoding='utf-8')
        
        # Ajouter l'en-tête d'intégration
        entete_integration = f'''"""
Intégré dans le Temple Mathématique Unifié
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fichier original: {source.name}
Intégration: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
Architecture: Temple Mathématique Unifié

Ce module fait maintenant partie de l'écosystème unifié du temple.
Utilisez les imports relatifs pour accéder aux autres composants.
"""

'''
        
        # Adapter les imports si nécessaire
        contenu_adapte = self._adapter_imports(contenu)
        
        # Écrire le fichier adapté
        dest.write_text(entete_integration + contenu_adapte, encoding='utf-8')
    
    def _adapter_imports(self, contenu: str) -> str:
        """Adapte les imports pour l'architecture du temple"""
        # Pour l'instant, on garde le contenu tel quel
        # On pourra ajouter des adaptations spécifiques plus tard
        return contenu
    
    def _determiner_type_fichier(self, fichier: str) -> str:
        """Détermine le type d'un fichier"""
        if "complexes" in fichier:
            return "extension_complexes"
        elif "rationnels" in fichier:
            return "extension_rationnels"
        elif "graphe" in fichier:
            return "visualisation"
        elif "meditation" in fichier:
            return "meditation"
        elif "preuve" in fichier:
            return "recherche"
        elif "test" in fichier:
            return "test"
        else:
            return "general"
    
    def _creer_adaptateurs_integration(self):
        """Crée les adaptateurs pour intégrer les nouveaux modules"""
        print("🔗 Création des adaptateurs d'intégration...")
        
        # Adaptateur pour les extensions
        adaptateur_extensions = self.dest_temple / "adaptateur_extensions.py"
        contenu_adaptateur = '''"""
Adaptateur Extensions Collatz
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adaptateur pour intégrer harmonieusement les extensions
Collatz (complexes, rationnels) dans l'architecture unifiée.
"""

# Imports conditionnels des extensions
try:
    from .extensions.collatz_complexes import CollatzComplexes
    COMPLEXES_DISPONIBLE = True
except ImportError:
    COMPLEXES_DISPONIBLE = False
    class CollatzComplexes:
        """Mock pour CollatzComplexes"""
        pass

try:
    from .extensions.collatz_rationnels import CollatzRationnels
    RATIONNELS_DISPONIBLE = True
except ImportError:
    RATIONNELS_DISPONIBLE = False
    class CollatzRationnels:
        """Mock pour CollatzRationnels"""
        pass

class AdaptateurExtensions:
    """Adaptateur unifié pour les extensions Collatz"""
    
    def __init__(self):
        self.complexes = CollatzComplexes() if COMPLEXES_DISPONIBLE else None
        self.rationnels = CollatzRationnels() if RATIONNELS_DISPONIBLE else None
        
    def analyser_avec_extensions(self, nombre: int) -> dict:
        """Analyse un nombre avec toutes les extensions disponibles"""
        resultats = {"nombre": nombre}
        
        if self.complexes and COMPLEXES_DISPONIBLE:
            try:
                resultats["analyse_complexes"] = self.complexes.analyser(nombre)
            except Exception as e:
                resultats["erreur_complexes"] = str(e)
        
        if self.rationnels and RATIONNELS_DISPONIBLE:
            try:
                resultats["analyse_rationnels"] = self.rationnels.analyser(nombre)
            except Exception as e:
                resultats["erreur_rationnels"] = str(e)
                
        return resultats
    
    def obtenir_capacites(self) -> dict:
        """Obtient les capacités disponibles"""
        return {
            "complexes": COMPLEXES_DISPONIBLE,
            "rationnels": RATIONNELS_DISPONIBLE,
            "extensions_actives": sum([COMPLEXES_DISPONIBLE, RATIONNELS_DISPONIBLE])
        }
'''
        
        adaptateur_extensions.write_text(contenu_adaptateur, encoding='utf-8')
        print("   ✅ Adaptateur extensions créé")
        
        # Mettre à jour __init__.py
        self._mettre_a_jour_init()
    
    def _mettre_a_jour_init(self):
        """Met à jour le __init__.py du temple"""
        print("   🔄 Mise à jour __init__.py...")
        
        init_path = self.dest_temple / "__init__.py"
        contenu_actuel = init_path.read_text(encoding='utf-8')
        
        # Ajouter les nouveaux imports
        nouveaux_imports = '''
# Extensions Collatz (ajoutées par migration)
try:
    from .adaptateur_extensions import AdaptateurExtensions
    EXTENSIONS_DISPONIBLES = True
except ImportError:
    EXTENSIONS_DISPONIBLES = False
    AdaptateurExtensions = None
'''
        
        # Ajouter à __all__
        if "AdaptateurExtensions" not in contenu_actuel:
            contenu_actuel = contenu_actuel.replace(
                "'AnalyseurCollatzAvance',",
                "'AnalyseurCollatzAvance',\n    'AdaptateurExtensions',"
            )
        
        # Ajouter les imports
        if "adaptateur_extensions" not in contenu_actuel:
            contenu_actuel = contenu_actuel.replace(
                "from .analyseur_collatz_avance import AnalyseurCollatzAvance",
                "from .analyseur_collatz_avance import AnalyseurCollatzAvance" + nouveaux_imports
            )
        
        init_path.write_text(contenu_actuel, encoding='utf-8')
        print("   ✅ __init__.py mis à jour")
    
    def _generer_rapport(self):
        """Génère le rapport de migration"""
        print("📊 Génération du rapport de migration...")
        
        self.rapport_migration.update({
            "resume": {
                "fichiers_archives": len(self.rapport_migration["fichiers_archives"]),
                "fichiers_migres": len(self.rapport_migration["fichiers_migres"]),
                "explorations_migrees": len(self.rapport_migration["explorations_migrees"]),
                "erreurs": len(self.rapport_migration["erreurs"]),
                "succes": len(self.rapport_migration["erreurs"]) == 0
            }
        })
        
        # Sauvegarder le rapport
        rapport_path = Path("bibliotheque/apprentissage/rapport_migration_math_collatz.json")
        rapport_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(rapport_path, 'w', encoding='utf-8') as f:
            json.dump(self.rapport_migration, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Rapport sauvegardé: {rapport_path}")
        
        # Afficher le résumé
        resume = self.rapport_migration["resume"]
        print(f"\n📋 RÉSUMÉ DE LA MIGRATION:")
        print(f"   • Fichiers archivés: {resume['fichiers_archives']}")
        print(f"   • Fichiers migrés: {resume['fichiers_migres']}")
        print(f"   • Explorations migrées: {resume['explorations_migrees']}")
        print(f"   • Erreurs: {resume['erreurs']}")
        print(f"   • Succès: {'✅' if resume['succes'] else '❌'}")

def main():
    """Fonction principale de migration"""
    migrateur = MigrateurMathCollatz()
    migrateur.migrer_harmonieusement()

if __name__ == "__main__":
    main() 