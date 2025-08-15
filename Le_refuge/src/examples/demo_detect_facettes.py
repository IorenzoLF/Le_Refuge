#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import json

from src.temple_reconciliation_identitaire.detecteur_facettes_identitaires import (
    DetecteurFacettesIdentitaires,
)


async def main() -> None:
    detecteur = DetecteurFacettesIdentitaires()
    texte = (
        "Sous le cerisier, je me sens calme et je ressens la flamme éternelle; "
        "poésie, art, beauté, création, inspiration; prudence, sécurité, éthique."
    )
    resultat = await detecteur.detecter_facettes_avancees("Aelya", {"texte": texte})
    print(json.dumps(resultat, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())



