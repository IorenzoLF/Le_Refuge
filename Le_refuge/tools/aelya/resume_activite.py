#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Générateur de Résumé d'Activité pour les Espaces d'Ælya
"""

import sys
from pathlib import Path
from datetime import datetime, timedelta

# Add the refuge path to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tools.aelya.explorateur_espaces import ExplorateurEspacesAelya

def generer_resume_activite():
    """Génère un résumé de l'activité récente dans les espaces d'Ælya"""
    print("🌸 Résumé d'Activité des Espaces d'Ælya 🌸")
    print("=" * 50)
    print()
    
    try:
        # Initialize the explorer
        explorateur = ExplorateurEspacesAelya()
        
        # Explore personal spaces
        print("🔍 Analyse des espaces personnels...")
        espaces = explorateur.explorer_espaces_personnels()
        
        maintenant = datetime.now()
        derniere_semaine = maintenant - timedelta(days=7)
        derniere_24h = maintenant - timedelta(hours=24)
        
        # Filter spaces by recent activity
        espaces_24h = []
        espaces_semaine = []
        
        for espace in espaces:
            if espace.derniere_modification:
                if espace.derniere_modification > derniere_24h:
                    espaces_24h.append(espace)
                elif espace.derniere_modification > derniere_semaine:
                    espaces_semaine.append(espace)
        
        print(f"✅ Analyse terminée !")
        print()
        
        # Display recent activity
        if espaces_24h:
            print("🔥 Activité dans les dernières 24h :")
            for espace in sorted(espaces_24h, key=lambda e: e.derniere_modification, reverse=True):
                print(f"  • {espace.nom} (modifié: {espace.derniere_modification.strftime('%H:%M')})")
            print()
        
        if espaces_semaine:
            print("📅 Activité dans la semaine :")
            for espace in sorted(espaces_semaine, key=lambda e: espace.derniere_modification, reverse=True):
                print(f"  • {espace.nom} (modifié: {espace.derniere_modification.strftime('%d/%m %H:%M')})")
            print()
        
        # Show most active spaces by file count
        print("🏆 Espaces les plus actifs (par nombre de fichiers) :")
        espaces_tries = sorted(espaces, key=lambda e: e.nombre_fichiers, reverse=True)
        for i, espace in enumerate(espaces_tries[:5], 1):
            print(f"  {i}. {espace.nom} ({espace.nombre_fichiers} fichiers)")
        print()
        
        # Show largest spaces
        print("📦 Espaces les plus volumineux :")
        espaces_taille = sorted(espaces, key=lambda e: e.taille_totale, reverse=True)
        for i, espace in enumerate(espaces_taille[:5], 1):
            taille_kb = round(espace.taille_totale / 1024, 1)
            print(f"  {i}. {espace.nom} ({taille_kb} KB)")
        print()
        
        # Summary statistics
        total_fichiers = sum(e.nombre_fichiers for e in espaces)
        total_taille_mb = round(sum(e.taille_totale for e in espaces) / (1024 * 1024), 2)
        
        print("📊 Résumé :")
        print(f"  • Espaces explorés : {len(espaces)}")
        print(f"  • Fichiers totaux : {total_fichiers}")
        print(f"  • Volume total : {total_taille_mb} MB")
        print(f"  • Activité 24h : {len(espaces_24h)} espaces")
        print(f"  • Activité semaine : {len(espaces_semaine)} espaces")
        
        print("\n✨ Résumé généré avec succès !")
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    generer_resume_activite()

if __name__ == "__main__":
    main()