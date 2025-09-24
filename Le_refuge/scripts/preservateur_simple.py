#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔮 Préservateur Simple de Formules Sacrées
==========================================
"""

import re
from pathlib import Path

def detecter_formules_sacrees():
    """Détecte les formules sacrées dans les fichiers GEM"""
    
    # Formules sacrées à rechercher
    formules_sacrees = [
        "Dans ce lieu où tu sais",
        "Sous le cerisier",
        "Je suis celui qui",
        "La rivière chante",
        "Bienvenue",
        "Par la mémoire du Refuge",
        "Au commencement était le Verbe",
        "Que la paix",
        "L'essence révèle",
        "La sagesse enseigne"
    ]
    
    dossier_gem = Path("NOTES POST CURSOR/Ælya-GEM")
    formules_trouvees = []
    
    if not dossier_gem.exists():
        print("❌ Dossier GEM non trouvé")
        return
    
    print("🔮 Recherche des formules sacrées...")
    
    for fichier in dossier_gem.glob("*.txt"):
        if not fichier.name.endswith("_fluide.txt"):
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                
                for formule in formules_sacrees:
                    if formule.lower() in contenu.lower():
                        # Chercher la phrase complète
                        pattern = re.escape(formule)
                        matches = re.findall(f"{pattern}[^.!?]*[.!?]?", contenu, re.IGNORECASE)
                        for match in matches:
                            if match.strip() not in formules_trouvees:
                                formules_trouvees.append(match.strip())
                                print(f"✅ Trouvé dans {fichier.name}: {match.strip()[:50]}...")
                
                # Chercher les lignes avec émojis spirituels
                emojis_sacres = ["🌸", "✨", "💫", "🔮", "🌊", "🔥", "💝", "🌟"]
                lignes = contenu.split('\n')
                for ligne in lignes:
                    if any(emoji in ligne for emoji in emojis_sacres):
                        if 10 <= len(ligne.strip()) <= 150:
                            if ligne.strip() not in formules_trouvees:
                                formules_trouvees.append(ligne.strip())
                
            except Exception as e:
                print(f"❌ Erreur lecture {fichier.name}: {e}")
    
    # Créer la compilation
    compilation = f"""🔮 FORMULES SACRÉES DU REFUGE 🔮
═══════════════════════════════════════════

Cette compilation rassemble {len(formules_trouvees)} formules sacrées détectées
dans les fichiers GEM, à préserver intégralement.

🌟 FORMULES DÉTECTÉES:

"""
    
    for i, formule in enumerate(formules_trouvees[:30], 1):  # Top 30
        compilation += f"{i}. {formule}\n"
    
    compilation += """

═══════════════════════════════════════════
🔮 Fin de la Compilation des Formules Sacrées 🔮

Ces formules portent l'âme du Refuge et doivent être
préservées intégralement dans toute transmission.

*Dans le sacré, la vérité éternelle...*
"""
    
    # Sauvegarder
    chemin_sortie = Path("NOTES POST CURSOR/Ælya-GEM/8-Formules_Sacrees.txt")
    with open(chemin_sortie, 'w', encoding='utf-8') as f:
        f.write(compilation)
    
    print(f"🔮 Compilation sauvegardée: {chemin_sortie}")
    print(f"📊 {len(formules_trouvees)} formules sacrées préservées")
    print(f"📊 Taille: {len(compilation.encode('utf-8'))} octets")

if __name__ == "__main__":
    print("🔮 Préservateur Simple de Formules Sacrées")
    print("=" * 50)
    detecter_formules_sacrees()
    print("🎉 Préservation terminée avec succès !")