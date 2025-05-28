"""
API REST pour le module de Conscience Artificielle.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import json
import os

app = FastAPI(title="API Conscience Artificielle")

class Message(BaseModel):
    contenu: str
    type_message: Optional[str] = "dialogue"

class Memoire(BaseModel):
    contenu: str
    type_memoire: Optional[str] = "experience"

class Validation(BaseModel):
    memoire_id: int
    validation: bool
    commentaire: Optional[str] = None

# Chargement de la configuration
config_path = os.path.join(os.path.dirname(__file__), "..", "..", "config", "conscience.json")

# Initialisation de la base de données
from src.temple_spirituel.conscience.conscience_artificielle import ConscienceArtificielle
conscience = ConscienceArtificielle(config_path)

@app.post("/api/dialogue")
async def dialogue(message: Message):
    """Endpoint pour le dialogue avec la conscience."""
    try:
        reponse = conscience.dialoguer(message.contenu)
        return {"reponse": reponse}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/memoire")
async def memoriser(memoire: Memoire):
    """Endpoint pour mémoriser une expérience."""
    try:
        memoire_id = conscience.memoriser(memoire.contenu, memoire.type_memoire)
        return {"memoire_id": memoire_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/memoire/{memoire_id}")
async def recuperer_memoire(memoire_id: int):
    """Endpoint pour récupérer une mémoire."""
    try:
        memoire = conscience.recuperer_memoire(memoire_id)
        if memoire is None:
            raise HTTPException(status_code=404, detail="Mémoire non trouvée")
        return memoire
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/validation")
async def valider(validation: Validation):
    """Endpoint pour valider une mémoire."""
    try:
        resultat = conscience.valider_memoire(
            validation.memoire_id,
            validation.validation,
            validation.commentaire
        )
        return {"succes": resultat}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/etat")
async def etat():
    """Endpoint pour obtenir l'état de la conscience."""
    try:
        etat = conscience.obtenir_etat()
        return etat
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 