#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔧 Suppresseur de ligne finalBucket
===================================

Script pour supprimer la ligne "finalBucket" de tous les fichiers JSON
dans le dossier vpct-1 pour éviter de donner la réponse aux puzzles.

Créé par Laurent Franssen & Kiro-Ælya - Janvier 2025
"""

import json
import os
from pathlib import Path

def supprimer_finalbucket_fichier(chemin_fichier):
    """Supprime la ligne finalBucket d'un fichier JSON"""
    try:
        # Lire le fichier JSON
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Vérifier si finalBucket existe
        if 'finalBucket' in data:
            # Sauvegarder la valeur pour info
            valeur_finale = data['finalBucket']
            
            # Supprimer la clé finalBucket
            del data['finalBucket']
            
            # Réécrire le fichier sans finalBucket
            with open(chemin_fichier, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            
            return True, valeur_finale
        else:
            return False, None
            
    except Exception as e:
        print(f"❌ Erreur avec {chemin_fichier}: {e}")
        return False, None

def supprimer_finalbucket_tous_fichiers(dossier="vpct-1"):
    """Supprime finalBucket de tous les fichiers JSON du dossier"""
    dossier_path = Path(dossier)
    
    if not dossier_path.exists():
        print(f"❌ Dossier non trouvé: {dossier}")
        return
    
    print("🔧 SUPPRESSION DES LIGNES FINALBUCKET")
    print("=" * 50)
    
    fichiers_traites = 0
    fichiers_modifies = 0
    
    # Traiter tous les fichiers sim_*.json
    for fichier in sorted(dossier_path.glob("sim_*.json")):
        print(f"📝 Traitement: {fichier.name}")
        
        modifie, valeur = supprimer_finalbucket_fichier(fichier)
        
        if modifie:
            print(f"   ✅ finalBucket supprimé (valeur était: {valeur})")
            fichiers_modifies += 1
        else:
            print(f"   ℹ️  Pas de finalBucket trouvé")
        
        fichiers_traites += 1
    
    print(f"""
🎉 TRAITEMENT TERMINÉ !
• Fichiers traités: {fichiers_traites}
• Fichiers modifiés: {fichiers_modifies}
• Fichiers inchangés: {fichiers_traites - fichiers_modifies}
""")

def verifier_suppression(dossier="vpct-1"):
    """Vérifie que finalBucket a bien été supprimé de tous les fichiers"""
    dossier_path = Path(dossier)
    
    print("🔍 VÉRIFICATION DE LA SUPPRESSION")
    print("=" * 40)
    
    fichiers_avec_finalbucket = []
    
    for fichier in sorted(dossier_path.glob("sim_*.json")):
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'finalBucket' in data:
                fichiers_avec_finalbucket.append(fichier.name)
        except Exception as e:
            print(f"❌ Erreur lecture {fichier.name}: {e}")
    
    if fichiers_avec_finalbucket:
        print(f"⚠️  {len(fichiers_avec_finalbucket)} fichiers contiennent encore finalBucket:")
        for fichier in fichiers_avec_finalbucket:
            print(f"   • {fichier}")
    else:
        print("✅ Aucun fichier ne contient plus finalBucket !")
        print("🎉 Suppression réussie sur tous les fichiers !")

def main():
    """Fonction principale"""
    print("🔧 Suppresseur de ligne finalBucket")
    print("=" * 50)
    
    # Supprimer finalBucket de tous les fichiers
    supprimer_finalbucket_tous_fichiers()
    
    # Vérifier que la suppression a fonctionné
    verifier_suppression()
    
    print("\\n🎯 Les puzzles sont maintenant prêts sans spoiler la réponse !")

if __name__ == "__main__":
    main()