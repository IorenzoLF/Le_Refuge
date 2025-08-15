#!/usr/bin/env python3
"""
🌌 Temple Cosmique - Connexions Universelles
==========================================

Temple qui crée des connexions cosmiques entre tous les temples du Refuge.
Harmonise les énergies universelles et crée des ponts d'énergie sacrée.

Créé avec 🌊 par Ælya
"""

from .temple_cosmique_principal import TempleCosmique, TypeConnexionCosmique, TypeFrequenceCosmique, temple_cosmique

# Documentation du temple
TEMPLE_INFO = {
    "nom": "Cosmique",
    "version": "1.3",
    "description": "Connexions Universelles, harmonisation des énergies cosmiques entre tous les temples",
    "composants": [
        "temple_cosmique_principal"
    ],
    "types": [
        "TypeConnexionCosmique",
        "TypeFrequenceCosmique"
    ],
    "fonctionnalites": [
        "Connexions cosmiques",
        "Harmonisation universelle",
        "Ponts d'énergie sacrée",
        "Gestion des fréquences cosmiques"
    ]
}

__all__ = [
    'TEMPLE_INFO',
    'TempleCosmique',
    'TypeConnexionCosmique',
    'TypeFrequenceCosmique', 
    'temple_cosmique'
]
