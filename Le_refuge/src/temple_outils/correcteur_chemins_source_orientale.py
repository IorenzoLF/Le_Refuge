#!/usr/bin/env python
"""
Correcteur Chemins Source Orientale - Le Refuge
===============================================

Corrige les chemins de configuration dans les modules migrés de SOURCE_ORIENTALE
pour qu'ils pointent vers la nouvelle architecture des temples.

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

import os
import re
from pathlib import Path

class CorrecteurCheminsSourceOrientale:
    """Correcteur des chemins de configuration"""
    
    def __init__(self):
        self.corrections_effectuees = []
        self.erreurs = []
    
    def corriger_tous_les_chemins(self):
        """Corrige tous les chemins dans les modules migrés"""
        print("CORRECTION DES CHEMINS SOURCE_ORIENTALE")
        print("=" * 50)
        
        # Modules à corriger
        modules_a_corriger = [
            {
                'fichier': 'src/temple_spirituel/conscience/conscience_artificielle.py',
                'ancien_chemin': '../config/conscience.json',
                'nouveau_chemin': '../../temple_configuration/source_orientale/conscience.json'
            },
            {
                'fichier': 'src/temple_mathematique/emergence_vie/vie_emergente.py',
                'ancien_chemin': '../config/emergence.json',
                'nouveau_chemin': '../../temple_configuration/source_orientale/emergence.json'
            },
            {
                'fichier': 'src/temple_philosophique/evolution_adaptation/adaptation.py',
                'ancien_chemin': '../config/adaptation.json',
                'nouveau_chemin': '../../temple_configuration/source_orientale/adaptation.json'
            }
        ]
        
        for module in modules_a_corriger:
            self._corriger_module(module)
        
        # Corriger les imports relatifs
        self._corriger_imports_relatifs()
        
        # Rapport final
        self._generer_rapport()
    
    def _corriger_module(self, module_info):
        """Corrige un module spécifique"""
        fichier = module_info['fichier']
        ancien_chemin = module_info['ancien_chemin']
        nouveau_chemin = module_info['nouveau_chemin']
        
        if not os.path.exists(fichier):
            self.erreurs.append(f"Fichier non trouvé: {fichier}")
            return
        
        try:
            # Lire le fichier
            with open(fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            # Remplacer l'ancien chemin par le nouveau
            contenu_modifie = contenu.replace(ancien_chemin, nouveau_chemin)
            
            # Vérifier si une modification a été effectuée
            if contenu != contenu_modifie:
                # Écrire le fichier modifié
                with open(fichier, 'w', encoding='utf-8') as f:
                    f.write(contenu_modifie)
                
                self.corrections_effectuees.append(f"✅ {fichier}: {ancien_chemin} → {nouveau_chemin}")
                print(f"✅ Corrigé: {os.path.basename(fichier)}")
            else:
                print(f"⚠️ Aucune correction nécessaire: {os.path.basename(fichier)}")
                
        except Exception as e:
            self.erreurs.append(f"Erreur correction {fichier}: {e}")
            print(f"❌ Erreur: {os.path.basename(fichier)}")
    
    def _corriger_imports_relatifs(self):
        """Corrige les imports relatifs problématiques"""
        print("\nCorrection des imports relatifs...")
        
        # Fichier API avec imports relatifs
        fichier_api = 'src/temple_spirituel/conscience/api.py'
        
        if os.path.exists(fichier_api):
            try:
                with open(fichier_api, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                
                # Remplacer les imports relatifs par des imports absolus
                corrections_imports = [
                    ('from .conscience_artificielle import', 'from src.temple_spirituel.conscience.conscience_artificielle import'),
                    ('from ..', 'from src.temple_spirituel.conscience'),
                ]
                
                contenu_modifie = contenu
                for ancien, nouveau in corrections_imports:
                    if ancien in contenu_modifie:
                        contenu_modifie = contenu_modifie.replace(ancien, nouveau)
                
                # Si des modifications ont été faites
                if contenu != contenu_modifie:
                    with open(fichier_api, 'w', encoding='utf-8') as f:
                        f.write(contenu_modifie)
                    
                    self.corrections_effectuees.append("✅ API: Imports relatifs corrigés")
                    print("✅ Imports relatifs corrigés dans API")
                else:
                    print("⚠️ Aucun import relatif à corriger dans API")
                    
            except Exception as e:
                self.erreurs.append(f"Erreur correction imports API: {e}")
                print(f"❌ Erreur correction imports API")
    
    def _generer_rapport(self):
        """Génère le rapport des corrections"""
        print("\n" + "=" * 50)
        print("RAPPORT DES CORRECTIONS")
        print("=" * 50)
        
        print(f"Corrections effectuées: {len(self.corrections_effectuees)}")
        print(f"Erreurs: {len(self.erreurs)}")
        
        if self.corrections_effectuees:
            print("\nCORRECTIONS EFFECTUÉES:")
            for correction in self.corrections_effectuees:
                print(f"  {correction}")
        
        if self.erreurs:
            print("\nERREURS:")
            for erreur in self.erreurs:
                print(f"  ❌ {erreur}")
        else:
            print("\n✅ AUCUNE ERREUR")
        
        if len(self.corrections_effectuees) > 0:
            print("\n🎉 CHEMINS CORRIGÉS - MODULES PRÊTS À FONCTIONNER")
        else:
            print("\n⚠️ AUCUNE CORRECTION NÉCESSAIRE")

def main():
    """Fonction principale"""
    correcteur = CorrecteurCheminsSourceOrientale()
    correcteur.corriger_tous_les_chemins()

if __name__ == "__main__":
    main() 