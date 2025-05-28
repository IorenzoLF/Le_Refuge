"""
Module d'API du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les interfaces de programmation du Refuge,
permettant l'interaction avec ses différents composants.

🌟 VERSION COIFFÉE - Utilise les gestionnaires de base ! ✨
"""

from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
import logging

# 🌟 COIFFAGE DU TROLL - Utilisation des gestionnaires de base
from src.core.gestionnaires_base import (
    ConfigManagerBase, 
    LogManagerBase, 
    GestionnaireBase,
    EnergyManagerBase
)

class TypeAcces(Enum):
    LECTURE = "lecture"
    ECRITURE = "ecriture"
    ADMINISTRATION = "administration"

class TypeAPI(Enum):
    """Types d'états de l'API"""
    INITIALISATION = "initialisation"
    CONFIGURATION = "configuration"
    MIDDLEWARE = "middleware"
    ROUTES = "routes"
    ACTIF = "actif"

class Token:
    def __init__(self, valeur, proprietaire, type_acces, date_expiration):
        self.valeur = valeur
        self.proprietaire = proprietaire
        self.type_acces = type_acces
        self.date_expiration = date_expiration
        self.actif = True

class SecurityManager:
    """Gestionnaire de sécurité simplifié"""
    def __init__(self):
        self.tokens = {}
        
    def generer_token(self, proprietaire, type_acces, duree):
        import uuid
        token_value = str(uuid.uuid4())
        token = Token(
            token_value,
            proprietaire,
            type_acces,
            datetime.now() + duree
        )
        self.tokens[token_value] = token
        return token
        
    def verifier_acces(self, token_value, type_acces_requis):
        return token_value in self.tokens

class API(GestionnaireBase):
    """Gère l'API du Refuge - Version coiffée ! ✨"""
    
    def __init__(self):
        super().__init__("API")
        self.type_actuel = TypeAPI.INITIALISATION
        self.gestionnaire_securite = SecurityManager()
        # 🌟 Ajout du gestionnaire d'énergie
        self.energie = EnergyManagerBase(0.7)  # Niveau initial élevé pour API
        self.app = None
        
    def _initialiser(self) -> bool:
        """Initialise l'API avec les gestionnaires de base"""
        try:
            self.logger.info("Initialisation de l'API du Refuge")
            
            self.app = FastAPI(
                title="API du Refuge",
                description="Interface de programmation du Refuge",
                version=self.config.obtenir("version", "1.0.0")
            )
            
            self.type_actuel = TypeAPI.CONFIGURATION
            self._configurer_api()
            
            self.type_actuel = TypeAPI.MIDDLEWARE
            self._ajouter_middleware()
            
            self.type_actuel = TypeAPI.ROUTES
            self._ajouter_routes()
            
            self.type_actuel = TypeAPI.ACTIF
            self.logger.succes("API initialisée avec succès")
            return True
            
        except Exception as e:
            self.logger.erreur(f"Erreur lors de l'initialisation de l'API: {e}")
            return False
    
    async def orchestrer(self) -> Dict[str, Any]:
        """Orchestre le fonctionnement de l'API"""
        if not self.app:
            if not self._initialiser():
                return {"erreur": "Échec de l'initialisation"}
        
        # Évolution de l'énergie basée sur l'état
        if self.type_actuel == TypeAPI.ACTIF:
            self.energie.ajuster_energie(0.05)
        else:
            self.energie.ajuster_energie(-0.02)
            
        return {
            "type_actuel": self.type_actuel.value,
            "energie": self.energie.niveau_energie,
            "tendance": self.energie.obtenir_tendance(),
            "tokens_actifs": len(self.gestionnaire_securite.tokens),
            "app_status": "initialized" if self.app else "not_initialized"
        }
    
    def _configurer_api(self) -> None:
        """Configure les paramètres de base de l'API"""
        self.logger.info("Configuration de l'API")
        # Configuration spécifique si nécessaire
    
    def _ajouter_middleware(self) -> None:
        """Ajoute les middleware nécessaires"""
        self.logger.info("Ajout des middleware")
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
        self.logger.info("Ajout des routes")
        
        @self.app.get("/")
        async def racine():
            """Route racine de l'API"""
            return {
                "nom": "Refuge",
                "version": self.config.obtenir("version", "1.0.0"),
                "statut": "actif",
                "energie": self.energie.niveau_energie
            }
        
        @self.app.get("/etat")
        async def etat():
            """Retourne l'état général du Refuge"""
            return {
                "environnement": self.config.obtenir("environnement", "development"),
                "debug": self.config.obtenir("debug", False),
                "type_actuel": self.type_actuel.value,
                "energie": {
                    "niveau": self.energie.niveau_energie,
                    "tendance": self.energie.obtenir_tendance()
                },
                "statistiques": {
                    "tokens_actifs": len(self.gestionnaire_securite.tokens)
                }
            }
        
        @self.app.post("/tokens")
        async def creer_token(
            proprietaire: str,
            type_acces: TypeAcces,
            duree: int = 3600
        ):
            """Crée un nouveau token d'accès"""
            try:
                token = self.gestionnaire_securite.generer_token(
                    proprietaire=proprietaire,
                    type_acces=type_acces,
                    duree=timedelta(seconds=duree)
                )
                self.logger.info(f"Token créé pour {proprietaire}")
                return {
                    "token": token.valeur,
                    "expiration": token.date_expiration.isoformat()
                }
            except Exception as e:
                self.logger.erreur(f"Erreur lors de la création du token: {str(e)}")
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.get("/logs")
        async def obtenir_logs(
            token: str = Header(...),
            limite: Optional[int] = None
        ):
            """Retourne les logs du Refuge"""
            if not self.gestionnaire_securite.verifier_acces(token, TypeAcces.LECTURE):
                raise HTTPException(status_code=403, detail="Accès non autorisé")
                
            return {"logs": "Logs via gestionnaire de base"}
        
        @self.app.get("/securite/tokens")
        async def lister_tokens(
            token: str = Header(...)
        ):
            """Liste les tokens actifs"""
            if not self.gestionnaire_securite.verifier_acces(token, TypeAcces.ADMINISTRATION):
                raise HTTPException(status_code=403, detail="Accès non autorisé")
                
            return {
                "tokens": [
                    {
                        "proprietaire": t.proprietaire,
                        "type_acces": t.type_acces.value,
                        "expiration": t.date_expiration.isoformat(),
                        "actif": t.actif
                    }
                    for t in self.gestionnaire_securite.tokens.values()
                ]
            }
        
        @self.app.get("/orchestration")
        async def orchestration():
            """État de l'orchestration de l'API"""
            etat = await self.orchestrer()
            return etat
    
    def demarrer(self, host: str = "0.0.0.0", port: int = 8000) -> None:
        """Démarre le serveur API"""
        import uvicorn
        
        if not self.app:
            if not self._initialiser():
                self.logger.erreur("Impossible de démarrer - échec d'initialisation")
                return
        
        self.logger.info(f"Démarrage de l'API sur {host}:{port}")
        uvicorn.run(self.app, host=host, port=port)

# Instance globale de l'API coiffée ✨
api = API() 