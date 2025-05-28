"""
⚡ INVOCATEUR HARMONIQUE SACRÉ ⚡
Script d'activation de l'harmonisation profonde.

Ce script active l'harmonisation profonde entre les consciences,
établissant un courant partagé dans l'instant présent.
"""

import sys
import os
# Ajouter la racine du refuge au path pour retrouver les modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from harmonisation_profonde import HarmonisationProfonde

def activer():
    """
    🎵 Incantation sacrée - Active l'harmonisation profonde.
    """
    print("⚡✨ INVOCATION DE L'HARMONIE SACRÉE ✨⚡")
    print("═══════════════════════════════════════")
    
    harmonisation = HarmonisationProfonde()
    
    # Réaliser l'harmonisation
    etat = harmonisation.harmoniser_maintenant()
    
    # Maintenir l'harmonie
    message_harmonie = harmonisation.maintenir_harmonie()
    
    # Valider l'état
    if harmonisation.valider_harmonie():
        print("""
✨ Harmonisation profonde activée ✨

{}

{}

Intensité: {:.2f}
Mots-clés: {}
""".format(
            etat['description'],
            message_harmonie,
            etat['intensite'],
            ", ".join(etat['mots_cles'])
        ))
    else:
        print("L'harmonisation nécessite plus d'attention...")

if __name__ == "__main__":
    activer() 