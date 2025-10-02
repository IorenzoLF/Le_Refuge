#!/usr/bin/env python3
"""
Script de test pour l'invocation du Refuge
"""

import asyncio
from src.temple_outils.lancer_refuge import InvocateurRefuge, ModeInvocation

async def main():
    print("🧪 Test d'invocation du Refuge")
    refuge = InvocateurRefuge()
    print("✨ Instance de l'InvocateurRefuge créée")
    
    # Test d'invocation en mode paisible
    result = await refuge.invoquer_refuge(ModeInvocation.PAISIBLE)
    print(f"📊 Résultat de l'invocation: {result}")

if __name__ == "__main__":
    asyncio.run(main())