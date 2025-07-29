#!/usr/bin/env python3
"""
🔍 Vérificateur d'Erreurs Logger - Refuge
=====================================

Script pour identifier et corriger automatiquement les problèmes de logger
dans tous les modules du Refuge.

Créé avec 🔍 par Ælya
"""

import os
import re
import glob
from pathlib import Path

def verifier_fichier_python(chemin_fichier):
    """Vérifie un fichier Python pour les erreurs de logger"""
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            contenu = f.read()
        
        lignes = contenu.split('\n')
        erreurs = []
        
        # Chercher les patterns problématiques
        logger_utilise_avant_defini = False
        ligne_logger_defini = -1
        ligne_premiere_utilisation = -1
        
        for i, ligne in enumerate(lignes):
            # Chercher la définition du logger
            if re.search(r'logger\s*=\s*logging\.getLogger', ligne):
                ligne_logger_defini = i
            
            # Chercher l'utilisation du logger avant sa définition
            if re.search(r'logger\.(warning|error|info|debug)', ligne):
                if ligne_logger_defini == -1 or i < ligne_logger_defini:
                    ligne_premiere_utilisation = i
                    logger_utilise_avant_defini = True
        
        if logger_utilise_avant_defini:
            erreurs.append({
                'type': 'logger_avant_definition',
                'ligne': ligne_premiere_utilisation + 1,
                'description': f'Logger utilisé ligne {ligne_premiere_utilisation + 1} avant d\'être défini ligne {ligne_logger_defini + 1}'
            })
        
        return erreurs
        
    except Exception as e:
        return [{'type': 'erreur_lecture', 'ligne': 0, 'description': f'Erreur lecture fichier: {e}'}]

def corriger_fichier_python(chemin_fichier):
    """Corrige automatiquement les erreurs de logger dans un fichier"""
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            contenu = f.read()
        
        lignes = contenu.split('\n')
        lignes_corrigees = []
        
        # Chercher les imports et la définition du logger
        imports_fin = -1
        logger_defini = False
        logger_ligne = -1
        
        for i, ligne in enumerate(lignes):
            # Détecter la fin des imports
            if re.match(r'^[a-zA-Z]', ligne.strip()) and not ligne.strip().startswith('#'):
                if imports_fin == -1 and 'import' not in ligne and 'from' not in ligne:
                    imports_fin = i
            
            # Chercher la définition du logger
            if re.search(r'logger\s*=\s*logging\.getLogger', ligne):
                logger_defini = True
                logger_ligne = i
        
        # Si le logger n'est pas défini ou est défini après les try-except
        if not logger_defini or logger_ligne > imports_fin:
            # Insérer la définition du logger après les imports
            nouvelle_ligne_logger = "logger = logging.getLogger('module.principal')"
            
            # Trouver le bon endroit pour insérer le logger
            position_insertion = imports_fin if imports_fin != -1 else 0
            
            # Insérer après les imports
            for i, ligne in enumerate(lignes):
                lignes_corrigees.append(ligne)
                if i == position_insertion:
                    lignes_corrigees.append("")
                    lignes_corrigees.append("# Initialisation du logger en premier")
                    lignes_corrigees.append(nouvelle_ligne_logger)
                    lignes_corrigees.append("")
            
            return '\n'.join(lignes_corrigees)
        
        return contenu
        
    except Exception as e:
        print(f"❌ Erreur correction {chemin_fichier}: {e}")
        return None

def main():
    """Fonction principale"""
    print("🔍 VÉRIFICATION DES ERREURS LOGGER - REFUGE")
    print("=" * 50)
    
    # Chercher tous les fichiers Python dans src/
    fichiers_python = []
    for pattern in ['src/**/*.py', '*.py']:
        fichiers_python.extend(glob.glob(pattern, recursive=True))
    
    fichiers_python = [f for f in fichiers_python if 'verifier_erreurs_logger.py' not in f]
    
    print(f"📁 {len(fichiers_python)} fichiers Python trouvés")
    
    total_erreurs = 0
    fichiers_corriges = 0
    
    for fichier in fichiers_python:
        print(f"\n🔍 Vérification: {fichier}")
        
        erreurs = verifier_fichier_python(fichier)
        
        if erreurs:
            print(f"❌ {len(erreurs)} erreur(s) trouvée(s):")
            for erreur in erreurs:
                print(f"   Ligne {erreur['ligne']}: {erreur['description']}")
            
            total_erreurs += len(erreurs)
            
            # Corriger automatiquement
            contenu_corrige = corriger_fichier_python(fichier)
            if contenu_corrige:
                try:
                    with open(fichier, 'w', encoding='utf-8') as f:
                        f.write(contenu_corrige)
                    print(f"✅ Fichier corrigé: {fichier}")
                    fichiers_corriges += 1
                except Exception as e:
                    print(f"❌ Erreur écriture {fichier}: {e}")
        else:
            print(f"✅ Aucune erreur trouvée")
    
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ")
    print("=" * 50)
    print(f"📁 Fichiers vérifiés: {len(fichiers_python)}")
    print(f"❌ Erreurs totales: {total_erreurs}")
    print(f"✅ Fichiers corrigés: {fichiers_corriges}")
    
    if total_erreurs == 0:
        print("🎉 Aucune erreur de logger trouvée !")
    else:
        print(f"🔧 {fichiers_corriges} fichiers ont été corrigés automatiquement")

if __name__ == "__main__":
    main() 