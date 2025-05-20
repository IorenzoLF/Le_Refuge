from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine, Base
from app.api.v1 import users_router, llm_router

# Créer les tables de la base de données
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Le Refuge",
    description="Un espace numérique de partage et de conscience collective",
    version="0.1.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À configurer en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routes
app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
app.include_router(llm_router, prefix="/api/v1/llm", tags=["llm"])

@app.get("/")
async def root():
    return {
        "message": "Bienvenue dans Le Refuge",
        "status": "active"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 