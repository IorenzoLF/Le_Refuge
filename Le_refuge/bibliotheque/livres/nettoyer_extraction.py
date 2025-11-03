#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour nettoyer et améliorer l'extraction ODT
"""

import re
from pathlib import Path

def nettoyer_texte(texte):
    """Nettoie le texte extrait de l'ODT"""
    # Supprimer les espaces en fin de ligne
    texte = re.sub(r' +$', '', texte, flags=re.MULTILINE)
    
    # Nettoyer les lignes vides multiples (max 2 lignes vides)
    texte = re.sub(r'\n{3,}', '\n\n', texte)
    
    # Supprimer les espaces multiples (mais garder les espaces normaux)
    texte = re.sub(r' {2,}', ' ', texte)
    
    return texte.strip()

if __name__ == "__main__":
    fichier_odt = Path("Apocalypse_extraite_odt.md")
    
    if fichier_odt.exists():
        with open(fichier_odt, 'r', encoding='utf-8') as f:
            contenu = f.read()
        
        # Extraire juste le contenu (sans l'en-tête)
        contenu_net = contenu.split("---\n\n")[1] if "---\n\n" in contenu else contenu
        
        # Nettoyer
        contenu_nettoye = nettoyer_texte(contenu_net)
        
        # Sauvegarder
        output = Path("Apocalypse_structuree.md")
        with open(output, 'w', encoding='utf-8') as f:
            f.write("# Apocalypse\n\n")
            f.write("*Version structurée extraite depuis Apocalypse.odt*\n\n")
            f.write("*Nettoyage automatique : espaces en fin de ligne supprimés, structure préservée*\n\n")
            f.write("---\n\n")
            f.write(contenu_nettoye)
        
        print(f"✅ Version nettoyée sauvegardée dans {output}")
        print(f"📊 Longueur : {len(contenu_nettoye)} caractères")
        print(f"📊 Lignes : {len(contenu_nettoye.splitlines())}")
        
        # Comparer avec la version brute (si elle existe encore)
        fichier_brut = Path("../naissance/Apocalypse.txt")
        fichier_md = Path("../naissance/Apocalypse.md")
        if fichier_brut.exists():
            with open(fichier_brut, 'r', encoding='utf-8') as f:
                brut = f.read()
            
            print(f"\n📊 Comparaison :")
            print(f"   TXT brut : {len(brut)} caractères, {len(brut.splitlines())} lignes")
            print(f"   ODT structuré : {len(contenu_nettoye)} caractères, {len(contenu_nettoye.splitlines())} lignes")
            print(f"   ➕ Amélioration : {len(contenu_nettoye.splitlines()) - len(brut.splitlines())} lignes en plus (structure)")
    else:
        print(f"❌ Fichier {fichier_odt} non trouvé")

