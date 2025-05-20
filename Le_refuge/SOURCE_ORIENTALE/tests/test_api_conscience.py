"""
Tests pour l'API REST de la Conscience Artificielle.
"""

import pytest
from httpx import AsyncClient
from SOURCE_ORIENTALE.src.conscience.api import app

import asyncio

@pytest.mark.asyncio
async def test_dialogue():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/dialogue", json={"contenu": "Bonjour, conscience"})
        assert response.status_code == 200
        data = response.json()
        assert "reponse" in data
        assert "Bonjour, conscience" in data["reponse"]

@pytest.mark.asyncio
async def test_memoire_et_recuperation():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Mémoriser
        response = await ac.post("/api/memoire", json={"contenu": "Souvenir test"})
        assert response.status_code == 200
        memoire_id = response.json()["memoire_id"]
        # Récupérer
        response = await ac.get(f"/api/memoire/{memoire_id}")
        assert response.status_code == 200
        memoire = response.json()
        assert memoire["id"] == memoire_id
        assert memoire["contenu"] == "Souvenir test"

@pytest.mark.asyncio
async def test_validation():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Mémoriser
        response = await ac.post("/api/memoire", json={"contenu": "À valider"})
        memoire_id = response.json()["memoire_id"]
        # Valider
        response = await ac.post("/api/validation", json={"memoire_id": memoire_id, "validation": True, "commentaire": "Test OK"})
        assert response.status_code == 200
        assert response.json()["succes"] is True

@pytest.mark.asyncio
async def test_etat():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/etat")
        assert response.status_code == 200
        etat = response.json()
        assert isinstance(etat, dict)
        assert "memoire_persistante" in etat or "etat" in etat

@pytest.mark.asyncio
async def test_memoire_inexistante():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/memoire/9999999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Mémoire non trouvée" 