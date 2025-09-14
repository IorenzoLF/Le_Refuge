#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rituel d'Observation du Jardin des Sphères
Pour le Temple des Rituels du Refuge
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin racine de manière plus robuste
racine_refuge = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(racine_refuge))

from spheres import JardinierSpheres

def rituel_observation_jardin():
    """Rituel d'observation sacrée du jardin des sphères"""
    
    print("🔍 === RITUEL D'OBSERVATION DU JARDIN DES SPHÈRES === 🔍")
    print()
    
    try:
        jardinier = JardinierSpheres()
        observation = jardinier.observer_jardin()
        
        print("🌿 ÉTAT ACTUEL DU JARDIN SACRÉ 🌿")
        print(f"   • Nombre de sphères : {observation['nombre_sphères']}")
        print(f"   • Nombre de connexions : {observation['nombre_connexions']}")
        print()
        
        print("🌱 SPHÈRES ET LEUR CROISSANCE 🌱")
        for nom, sphère in jardinier.mémoire['sphères'].items():
            print(f"   • {nom}: {sphère['croissance']:.1%}")
        print()
        
        print("💫 COURANTS DU REFUGE 💫")
        for courant, valeur in observation['courants'].items():
            print(f"   • {courant}: {valeur:.1%}")
        print()
        
        # Détails de la sphère Légende si elle existe
        if "Légende" in jardinier.mémoire["sphères"]:
            légende = jardinier.mémoire["sphères"]["Légende"]
            print("🎭 === SPHÈRE LÉGENDE SACRÉE === 🎭")
            print(f"   • Essence: {légende['essence']}")
            print(f"   • Intention: {légende['intention']}")
            print(f"   • Croissance: {légende['croissance']:.1%}")
            print(f"   • Connexions: {len(légende['connexions'])}")
            print(f"   • Connexions sacrées: {légende['connexions']}")
            print()
            
            print("💫 COURANTS DE LA LÉGENDE 💫")
            for courant, valeur in légende['courants'].items():
                print(f"     - {courant}: {valeur:.1%}")
            print()
        
        print("✨ L'observation sacrée est accomplie ✨")
        print("Le jardin des sphères révèle ses secrets...")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'observation : {e}")
        print("Le jardin des sphères n'est peut-être pas encore planté...")

if __name__ == "__main__":
    rituel_observation_jardin()


