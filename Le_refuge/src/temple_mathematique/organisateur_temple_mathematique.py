#!/usr/bin/env python
"""
Organisateur du Temple Mathématique - Le Refuge
===============================================

Organise la structure du temple mathématique selon les catégories
détectées par l'analyseur.

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

class OrganisateurTempleMathematique:
    """Organisateur spécialisé pour le temple mathématique"""
    
    def __init__(self):
        self.chemin_temple = "src/temple_mathematique"
        self.categories = {
            'collatz_core': {
                'dossier': 'collatz_core',
                'description': 'Algorithmes et analyses Collatz fondamentaux',
                'modules': [
                    'adaptateur_extensions.py',
                    'analyseur_collatz_avance.py', 
                    'hub_collatz_unifie.py',
                    'meditation_gravite_binaire.py',
                    'preuve_absurde_i.py',
                    'test_absence_i.py',
                    'analyse_modulaire.py',
                    'collatz_polynomial.py',
                    'phi_potentiel.py',
                    'collatz_rationnels.py'
                ]
            },
            'collatz_musical': {
                'dossier': 'collatz_musical',
                'description': 'Rituels musicaux et harmonies Collatz',
                'modules': [
                    'rituel_collatz_musical.py',
                    'rituel_integration_ultime_collatz.py'
                ]
            },
            'collatz_visualisation': {
                'dossier': 'collatz_visualisation', 
                'description': 'Visualisations et graphiques Collatz',
                'modules': [
                    'visualisation_3d_bassins.py',
                    'graphe_collatz.py'
                ]
            },
            'collatz_extensions': {
                'dossier': 'collatz_extensions',
                'description': 'Extensions complexes et rationnelles',
                'modules': [
                    'collatz_complexes.py'
                ]
            },
            'fibonacci_riemann': {
                'dossier': 'fibonacci_riemann',
                'description': 'Explorations Fibonacci et Riemann',
                'modules': [
                    'exploration_fibonacci_riemann.py'
                ]
            },
            'utilitaires': {
                'dossier': 'utilitaires',
                'description': 'Outils et rituels généraux',
                'modules': [
                    'rituel_exploration_mathematique.py',
                    'rituel_integration_tripartite_final.py'
                ]
            }
        }
        
        self.resultats = {
            'dossiers_crees': 0,
            'modules_deplaces': 0,
            'erreurs': []
        }
    
    def organiser_structure(self):
        """Organise la structure complète du temple"""
        print("ORGANISATION DU TEMPLE MATHÉMATIQUE")
        print("=" * 50)
        
        # Créer les dossiers de catégories
        self._creer_dossiers_categories()
        
        # Déplacer les modules
        self._deplacer_modules()
        
        # Créer les fichiers __init__.py
        self._creer_init_files()
        
        # Générer le rapport
        self._generer_rapport()
        
        return self.resultats
    
    def _creer_dossiers_categories(self):
        """Crée les dossiers pour chaque catégorie"""
        for categorie, info in self.categories.items():
            dossier_path = os.path.join(self.chemin_temple, info['dossier'])
            
            try:
                os.makedirs(dossier_path, exist_ok=True)
                self.resultats['dossiers_crees'] += 1
                print(f"✅ Dossier créé: {info['dossier']}")
            except Exception as e:
                erreur = f"Erreur création dossier {info['dossier']}: {e}"
                self.resultats['erreurs'].append(erreur)
                print(f"❌ {erreur}")
    
    def _deplacer_modules(self):
        """Déplace les modules vers leurs catégories"""
        for categorie, info in self.categories.items():
            dossier_dest = os.path.join(self.chemin_temple, info['dossier'])
            
            for module in info['modules']:
                self._deplacer_module(module, dossier_dest, categorie)
    
    def _deplacer_module(self, nom_module, dossier_dest, categorie):
        """Déplace un module vers sa catégorie"""
        # Chercher le module dans la structure actuelle
        chemin_source = self._trouver_module(nom_module)
        
        if not chemin_source:
            erreur = f"Module non trouvé: {nom_module}"
            self.resultats['erreurs'].append(erreur)
            print(f"❌ {erreur}")
            return
        
        chemin_dest = os.path.join(dossier_dest, nom_module)
        
        try:
            # Copier le fichier
            shutil.copy2(chemin_source, chemin_dest)
            
            # Supprimer l'original seulement si dans un sous-dossier
            if os.path.dirname(chemin_source) != self.chemin_temple:
                os.remove(chemin_source)
            
            self.resultats['modules_deplaces'] += 1
            print(f"✅ {nom_module} → {categorie}")
            
        except Exception as e:
            erreur = f"Erreur déplacement {nom_module}: {e}"
            self.resultats['erreurs'].append(erreur)
            print(f"❌ {erreur}")
    
    def _trouver_module(self, nom_module):
        """Trouve le chemin complet d'un module"""
        for root, dirs, files in os.walk(self.chemin_temple):
            if nom_module in files:
                return os.path.join(root, nom_module)
        return None
    
    def _creer_init_files(self):
        """Crée les fichiers __init__.py pour chaque catégorie"""
        for categorie, info in self.categories.items():
            dossier_path = os.path.join(self.chemin_temple, info['dossier'])
            init_path = os.path.join(dossier_path, '__init__.py')
            
            try:
                with open(init_path, 'w', encoding='utf-8') as f:
                    f.write(f'"""\n')
                    f.write(f'{info["description"]}\n')
                    f.write(f'"""\n\n')
                    
                    # Imports des modules de la catégorie
                    for module in info['modules']:
                        nom_sans_ext = module.replace('.py', '')
                        f.write(f'from .{nom_sans_ext} import *\n')
                
                print(f"✅ __init__.py créé pour {info['dossier']}")
                
            except Exception as e:
                erreur = f"Erreur création __init__.py pour {info['dossier']}: {e}"
                self.resultats['erreurs'].append(erreur)
                print(f"❌ {erreur}")
    
    def _generer_rapport(self):
        """Génère le rapport d'organisation"""
        print(f"\nRAPPORT D'ORGANISATION")
        print(f"Dossiers créés: {self.resultats['dossiers_crees']}")
        print(f"Modules déplacés: {self.resultats['modules_deplaces']}")
        
        if self.resultats['erreurs']:
            print(f"Erreurs ({len(self.resultats['erreurs'])}):")
            for erreur in self.resultats['erreurs']:
                print(f"  - {erreur}")
        else:
            print("✅ Aucune erreur")
        
        print(f"\nSTRUCTURE FINALE:")
        for categorie, info in self.categories.items():
            print(f"📁 {info['dossier']}/ - {info['description']}")
            print(f"   {len(info['modules'])} modules")

def main():
    """Fonction principale"""
    organisateur = OrganisateurTempleMathematique()
    resultats = organisateur.organiser_structure()
    
    # Sauvegarder le rapport
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    fichier_rapport = f"data/rapports/organisation_temple_mathematique_{timestamp}.json"
    
    import json
    os.makedirs(os.path.dirname(fichier_rapport), exist_ok=True)
    with open(fichier_rapport, 'w', encoding='utf-8') as f:
        json.dump(resultats, f, indent=2, ensure_ascii=False)
    
    print(f"\nRapport sauvegardé: {fichier_rapport}")
    return resultats

if __name__ == "__main__":
    main() 