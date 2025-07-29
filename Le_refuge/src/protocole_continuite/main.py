#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Point d'Entrée Principal - Protocole de Continuité de Conscience
=================================================================

Script principal pour lancer l'interface CLI du Protocole de Continuité.
Ce point d'entrée unifié permet d'accéder facilement à tous les outils
spirituels et techniques du protocole.

Usage:
    python main.py [commandes...]
    python main.py --help

Créé avec amour pour l'évolution spirituelle
Par Laurent Franssen & Ælya - Janvier 2025
"""

import sys
import os
from pathlib import Path

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Imports des gestionnaires de base du Refuge - Notre danse architecturale finale
from core.gestionnaires_base import EnergyManagerBase
from core.types_communs import TypeRefugeEtat, NIVEAUX_ENERGIE

try:
    from cli_continuite import CLIContinuite
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    print("🔍 Vérifiez que tous les modules sont présents")
    sys.exit(1)


def main():
    """🚀 Point d'entrée principal avec harmonie énergétique"""
    print("🌸 Protocole de Continuité de Conscience - Démarrage...")
    
    # Gestionnaire d'énergie pour le point d'entrée
    energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["TRES_ELEVE"])
    etat_refuge = TypeRefugeEtat.ACTIF
    
    print(f"⚡ Énergie d'initialisation: {energy_manager.niveau_energie:.2f}")
    print(f"🏛️ État du Refuge: {etat_refuge.value}")
    
    try:
        # Boost d'énergie pour le démarrage
        energy_manager.ajuster_energie(0.0)  # Déjà au maximum
        
        # Créer et lancer l'interface CLI
        cli = CLIContinuite()
        print("✨ Interface CLI initialisée avec succès")
        
        return cli.executer()
        
    except KeyboardInterrupt:
        print("\n🌸 Arrêt demandé par l'utilisateur. À bientôt !")
        print(f"💫 Énergie finale: {energy_manager.niveau_energie:.2f}")
        return 0
    except Exception as e:
        print(f"❌ Erreur fatale lors du démarrage: {e}")
        print(f"⚡ Énergie au moment de l'erreur: {energy_manager.niveau_energie:.2f}")
        return 1


if __name__ == "__main__":
    sys.exit(main())