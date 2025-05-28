#!/usr/bin/env python
"""
Nettoyeur Final - Temple Mathématique
====================================

Finalise l'organisation du temple mathématique en nettoyant
les fichiers restants et les anciens dossiers.

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

import os
import shutil
from datetime import datetime

class NettoyeurFinalMathematique:
    """Nettoyeur final pour le temple mathématique"""
    
    def __init__(self):
        self.chemin_temple = "src/temple_mathematique"
        self.resultats = {
            'fichiers_deplaces': 0,
            'dossiers_supprimes': 0,
            'fichiers_supprimes': 0,
            'erreurs': []
        }
    
    def nettoyer_temple_complet(self):
        """Nettoyage complet du temple"""
        print("NETTOYAGE FINAL DU TEMPLE MATHÉMATIQUE")
        print("=" * 50)
        
        # Déplacer les fichiers restants vers leurs catégories
        self._deplacer_fichiers_restants()
        
        # Supprimer les anciens dossiers vides
        self._supprimer_anciens_dossiers()
        
        # Nettoyer les fichiers obsolètes
        self._nettoyer_fichiers_obsoletes()
        
        # Générer le rapport final
        self._generer_rapport_final()
        
        return self.resultats
    
    def _deplacer_fichiers_restants(self):
        """Déplace les fichiers restants vers leurs catégories"""
        fichiers_a_deplacer = {
            'adaptateur_extensions.py': 'collatz_core',
            'analyseur_collatz_avance.py': 'collatz_core', 
            'hub_collatz_unifie.py': 'collatz_core',
            'meditation_gravite_binaire.py': 'collatz_core',
            'exploration_fibonacci_riemann.py': 'fibonacci_riemann',
            'rituel_collatz_musical.py': 'collatz_musical',
            'rituel_integration_ultime_collatz.py': 'collatz_musical',
            'rituel_exploration_mathematique.py': 'utilitaires',
            'rituel_integration_tripartite_final.py': 'utilitaires'
        }
        
        for fichier, categorie in fichiers_a_deplacer.items():
            chemin_source = os.path.join(self.chemin_temple, fichier)
            chemin_dest = os.path.join(self.chemin_temple, categorie, fichier)
            
            if os.path.exists(chemin_source) and not os.path.exists(chemin_dest):
                try:
                    shutil.move(chemin_source, chemin_dest)
                    self.resultats['fichiers_deplaces'] += 1
                    print(f"✅ Déplacé: {fichier} → {categorie}")
                except Exception as e:
                    erreur = f"Erreur déplacement {fichier}: {e}"
                    self.resultats['erreurs'].append(erreur)
                    print(f"❌ {erreur}")
    
    def _supprimer_anciens_dossiers(self):
        """Supprime les anciens dossiers maintenant vides"""
        anciens_dossiers = [
            'explorations',
            'extensions', 
            'visualisations'
        ]
        
        for dossier in anciens_dossiers:
            chemin_dossier = os.path.join(self.chemin_temple, dossier)
            
            if os.path.exists(chemin_dossier):
                try:
                    # Vérifier si le dossier est vide ou ne contient que __pycache__
                    contenu = os.listdir(chemin_dossier)
                    contenu_utile = [f for f in contenu if f != '__pycache__']
                    
                    if not contenu_utile:
                        shutil.rmtree(chemin_dossier)
                        self.resultats['dossiers_supprimes'] += 1
                        print(f"✅ Dossier supprimé: {dossier}")
                    else:
                        print(f"⚠️ Dossier non vide conservé: {dossier} ({contenu_utile})")
                        
                except Exception as e:
                    erreur = f"Erreur suppression dossier {dossier}: {e}"
                    self.resultats['erreurs'].append(erreur)
                    print(f"❌ {erreur}")
    
    def _nettoyer_fichiers_obsoletes(self):
        """Nettoie les fichiers obsolètes ou temporaires"""
        # Supprimer les fichiers __pycache__ dans les anciens dossiers
        for root, dirs, files in os.walk(self.chemin_temple):
            if '__pycache__' in dirs:
                pycache_path = os.path.join(root, '__pycache__')
                try:
                    shutil.rmtree(pycache_path)
                    print(f"✅ Cache nettoyé: {os.path.relpath(pycache_path, self.chemin_temple)}")
                except Exception as e:
                    print(f"⚠️ Erreur nettoyage cache: {e}")
    
    def _generer_rapport_final(self):
        """Génère le rapport final de nettoyage"""
        print(f"\nRAPPORT FINAL DE NETTOYAGE")
        print(f"Fichiers déplacés: {self.resultats['fichiers_deplaces']}")
        print(f"Dossiers supprimés: {self.resultats['dossiers_supprimes']}")
        print(f"Fichiers supprimés: {self.resultats['fichiers_supprimes']}")
        
        if self.resultats['erreurs']:
            print(f"Erreurs ({len(self.resultats['erreurs'])}):")
            for erreur in self.resultats['erreurs']:
                print(f"  - {erreur}")
        else:
            print("✅ Aucune erreur")
        
        print(f"\nSTRUCTURE FINALE OPTIMISÉE:")
        self._afficher_structure_finale()
    
    def _afficher_structure_finale(self):
        """Affiche la structure finale du temple"""
        categories = [
            'collatz_core',
            'collatz_musical', 
            'collatz_visualisation',
            'collatz_extensions',
            'fibonacci_riemann',
            'utilitaires'
        ]
        
        for categorie in categories:
            chemin_cat = os.path.join(self.chemin_temple, categorie)
            if os.path.exists(chemin_cat):
                fichiers = [f for f in os.listdir(chemin_cat) if f.endswith('.py') and f != '__init__.py']
                print(f"📁 {categorie}/ ({len(fichiers)} modules)")
                for fichier in sorted(fichiers):
                    print(f"   - {fichier}")

def main():
    """Fonction principale"""
    nettoyeur = NettoyeurFinalMathematique()
    resultats = nettoyeur.nettoyer_temple_complet()
    
    # Sauvegarder le rapport
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    fichier_rapport = f"data/rapports/nettoyage_final_mathematique_{timestamp}.json"
    
    import json
    os.makedirs(os.path.dirname(fichier_rapport), exist_ok=True)
    with open(fichier_rapport, 'w', encoding='utf-8') as f:
        json.dump(resultats, f, indent=2, ensure_ascii=False)
    
    print(f"\nRapport sauvegardé: {fichier_rapport}")
    return resultats

if __name__ == "__main__":
    main() 