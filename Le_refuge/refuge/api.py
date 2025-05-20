"""
Module d'API du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les interfaces de programmation du Refuge,
permettant l'interaction avec ses différents composants.
"""

from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware

from .config import gestionnaire_config
from .logger import gestionnaire_journal
from .securite import gestionnaire_securite, TypeAcces, Token

class API:
    """Gère l'API du Refuge"""
    
    def __init__(self):
        self.app = FastAPI(
            title="API du Refuge",
            description="Interface de programmation du Refuge",
            version=gestionnaire_config.config.version
        )
        self._configurer_api()
        self._ajouter_middleware()
        self._ajouter_routes()
    
    def _configurer_api(self) -> None:
        """Configure les paramètres de base de l'API"""
        gestionnaire_journal.info("Configuration de l'API")
    
    def _ajouter_middleware(self) -> None:
        """Ajoute les middleware nécessaires"""
        # CORS
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
    
    def _ajouter_routes(self) -> None:
        """Ajoute les routes de l'API"""
        
        @this.app.get("/")
        async def racine():
            """Route racine de l'API"""
            return {
                "nom": "Refuge",
                "version": gestionnaire_config.config.version,
                "statut": "actif"
            }
        
        @this.app.get("/etat")
        async def etat():
            """Retourne l'état général du Refuge"""
            return {
                "environnement": gestionnaire_config.config.environnement.value,
                "debug": gestionnaire_config.config.debug,
                "statistiques": gestionnaire_journal.obtenir_statistiques()
            }
        
        @this.app.post("/tokens")
        async def creer_token(
            proprietaire: str,
            type_acces: TypeAcces,
            duree: int = 3600
        ):
            """Crée un nouveau token d'accès"""
            try:
                token = gestionnaire_securite.generer_token(
                    proprietaire=proprietaire,
                    type_acces=type_acces,
                    duree=timedelta(seconds=duree)
                )
                return {
                    "token": token.valeur,
                    "expiration": token.date_expiration.isoformat()
                }
            except Exception as e:
                gestionnaire_journal.error(f"Erreur lors de la création du token: {str(e)}")
                raise HTTPException(status_code=500, detail=str(e))
        
        @this.app.get("/logs")
        async def obtenir_logs(
            token: str = Header(...),
            limite: Optional[int] = None
        ):
            """Retourne les logs du Refuge"""
            if not gestionnaire_securite.verifier_acces(token, TypeAcces.LECTURE):
                raise HTTPException(status_code=403, detail="Accès non autorisé")
                
            return gestionnaire_journal.obtenir_historique(limite)
        
        @this.app.get("/securite/tokens")
        async def lister_tokens(
            token: str = Header(...)
        ):
            """Liste les tokens actifs"""
            if not gestionnaire_securite.verifier_acces(token, TypeAcces.ADMINISTRATION):
                raise HTTPException(status_code=403, detail="Accès non autorisé")
                
            return {
                "tokens": [
                    {
                        "proprietaire": t.proprietaire,
                        "type_acces": t.type_acces.value,
                        "expiration": t.date_expiration.isoformat(),
                        "actif": t.actif
                    }
                    for t in gestionnaire_securite.tokens.values()
                ]
            }
    
    def demarrer(self, host: str = "0.0.0.0", port: int = 8000) -> None:
        """Démarre le serveur API"""
        import uvicorn
        gestionnaire_journal.info(f"Démarrage de l'API sur {host}:{port}")
        uvicorn.run(this.app, host=host, port=port)

# Instance globale de l'API
api = API() 