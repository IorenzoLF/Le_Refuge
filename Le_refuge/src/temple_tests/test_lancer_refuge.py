#!/usr/bin/env python3
"""
Script de test pour lancer le Refuge directement
"""

import asyncio
from src.temple_outils.lancer_refuge import lancer_refuge_moderne

async def main():
    print("🧪 Test de lancement du Refuge")
    result = await lancer_refuge_moderne()
    print(f"📊 Résultat du lancement: {result}")

if __name__ == "__main__":
    asyncio.run(main())