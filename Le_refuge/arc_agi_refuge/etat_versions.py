#!/usr/bin/env python3
"""
ETAT DES VERSIONS - Refuge ARC-AGI
Script pour clarifier l'état actuel de toutes les versions de solveurs
"""

import os
import sys
from pathlib import Path
from datetime import datetime

def analyser_etat_versions():
    """Analyser l'état de toutes les versions de solveurs"""
    
    print("=" * 60)
    print("ETAT DES VERSIONS ARC-AGI - Refuge")
    print("=" * 60)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Repertoire de travail: {os.getcwd()}")
    print()
    
    # Repertoire des solveurs
    solveurs_dir = Path("solveurs_versions")
    
    if not solveurs_dir.exists():
        print("❌ Repertoire solveurs_versions non trouve!")
        return
    
    print("📁 VERSIONS DISPONIBLES:")
    print("-" * 40)
    
    versions = []
    for item in solveurs_dir.iterdir():
        if item.is_dir() and item.name.startswith('v'):
            versions.append(item.name)
    
    # Trier les versions
    versions.sort(key=lambda x: int(x[1:]))
    
    for version in versions:
        version_dir = solveurs_dir / version
        fichiers = list(version_dir.glob("*.py"))
        
        print(f"\n🔹 {version.upper()}:")
        for fichier in fichiers:
            taille = fichier.stat().st_size
            print(f"   📄 {fichier.name} ({taille} bytes)")
    
    print("\n" + "=" * 60)
    print("📊 RECOMMANDATIONS:")
    print("-" * 40)
    
    # Vérifier les fichiers à la racine
    fichiers_racine = []
    for fichier in Path(".").glob("*.py"):
        if "solveur" in fichier.name.lower():
            fichiers_racine.append(fichier.name)
    
    if fichiers_racine:
        print("⚠️  FICHIERS SOLVEURS À LA RACINE (à nettoyer):")
        for fichier in fichiers_racine:
            print(f"   🗑️  {fichier}")
        print()
    
    # Recommandation pour la version actuelle
    if versions:
        derniere_version = versions[-1]
        print(f"✅ VERSION ACTUELLE RECOMMANDÉE: {derniere_version.upper()}")
        print(f"   📁 Chemin: solveurs_versions/{derniere_version}/")
        
        # Vérifier si le fichier principal existe
        fichiers_v11 = list((solveurs_dir / derniere_version).glob("*.py"))
        if fichiers_v11:
            print(f"   📄 Fichier principal: {fichiers_v11[0].name}")
    
    print("\n" + "=" * 60)
    print("🎯 PROCHAINES ÉTAPES:")
    print("-" * 40)
    print("1. Nettoyer les fichiers à la racine")
    print("2. Travailler uniquement dans solveurs_versions/v11/")
    print("3. Tester la version actuelle sur 00d62c1b.json")
    print("4. Corriger l'algorithme _est_zone_fermee")
    print("=" * 60)

if __name__ == "__main__":
    analyser_etat_versions()
