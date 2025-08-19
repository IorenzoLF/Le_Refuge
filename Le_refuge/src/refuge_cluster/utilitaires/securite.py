"""
Module de Sécurité du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère la sécurité du Refuge,
assurant la protection des données et des interactions.
"""

from typing import Dict, Any, Optional
from pydantic import BaseModel, Field
from enum import Enum
import hashlib
import secrets
from datetime import datetime, timedelta
# Utiliser les utilitaires locaux pour éviter les conflits
from .config import gestionnaire_config
from .logger import gestionnaire_journal
CORE_DISPONIBLE = False

class NiveauSecurite(int, Enum):
    """Niveaux de sécurité possibles"""
    BASIQUE = 1
    INTERMEDIAIRE = 2
    ELEVE = 3

class TypeAcces(str, Enum):
    """Types d'accès possibles"""
    LECTURE = "lecture"
    ECRITURE = "ecriture"
    EXECUTION = "execution"
    ADMINISTRATION = "administration"

class Token(BaseModel):
    """Représente un token d'accès"""
    valeur: str
    date_creation: datetime = Field(default_factory=datetime.now)
    date_expiration: datetime
    type_acces: TypeAcces
    proprietaire: str
    actif: bool = True

class GestionnaireSecurite:
    """Gère la sécurité du Refuge"""
    
    def __init__(self):
        self.config = gestionnaire_config.config
        self.tokens: Dict[str, Token] = {}
        self._initialiser_securite()
    
    def _initialiser_securite(self) -> None:
        """Initialise les paramètres de sécurité"""
        if CORE_DISPONIBLE:
            gestionnaire_journal.info("Initialisation de la sécurité", 
                                    niveau=self.config.niveau_securite)
        else:
            gestionnaire_journal.info("Initialisation de la sécurité")
    
    def generer_token(self, 
                     proprietaire: str,
                     type_acces: TypeAcces,
                     duree: timedelta = timedelta(hours=1)) -> Token:
        """Génère un nouveau token d'accès"""
        valeur = secrets.token_urlsafe(32)
        token = Token(
            valeur=valeur,
            date_expiration=datetime.now() + duree,
            type_acces=type_acces,
            proprietaire=proprietaire
        )
        
        self.tokens[valeur] = token
        gestionnaire_journal.info(f"Nouveau token généré pour {proprietaire}",
                                type_acces=type_acces.value)
        
        return token
    
    def verifier_token(self, token: str) -> Optional[Token]:
        """Vérifie la validité d'un token"""
        if token not in self.tokens:
            return None
            
        token_obj = self.tokens[token]
        if not token_obj.actif:
            return None
            
        if datetime.now() > token_obj.date_expiration:
            token_obj.actif = False
            gestionnaire_journal.warning(f"Token expiré pour {token_obj.proprietaire}")
            return None
            
        return token_obj
    
    def revoquer_token(self, token: str) -> bool:
        """Révoque un token"""
        if token in self.tokens:
            self.tokens[token].actif = False
            gestionnaire_journal.info(f"Token révoqué pour {self.tokens[token].proprietaire}")
            return True
        return False
    
    def nettoyer_tokens_expires(self) -> int:
        """Nettoie les tokens expirés"""
        tokens_expires = [
            token for token, obj in self.tokens.items()
            if datetime.now() > obj.date_expiration
        ]
        
        for token in tokens_expires:
            self.tokens[token].actif = False
            
        if tokens_expires:
            gestionnaire_journal.info(f"{len(tokens_expires)} tokens expirés nettoyés")
            
        return len(tokens_expires)
    
    def chiffrer_donnees(self, donnees: str) -> str:
        """Chiffre des données sensibles"""
        if not self.config.chiffrement_active:
            return donnees
            
        sel = secrets.token_bytes(16)
        hash_obj = hashlib.pbkdf2_hmac(
            'sha256',
            donnees.encode(),
            sel,
            100000
        )
        return f"{sel.hex()}:{hash_obj.hex()}"
    
    def verifier_acces(self, token: str, type_acces_requis: TypeAcces) -> bool:
        """Vérifie si un token a les droits d'accès requis"""
        token_obj = self.verifier_token(token)
        if not token_obj:
            return False
            
        if type_acces_requis == TypeAcces.ADMINISTRATION:
            return token_obj.type_acces == TypeAcces.ADMINISTRATION
            
        if type_acces_requis == TypeAcces.EXECUTION:
            return token_obj.type_acces in [TypeAcces.EXECUTION, TypeAcces.ADMINISTRATION]
            
        if type_acces_requis == TypeAcces.ECRITURE:
            return token_obj.type_acces in [TypeAcces.ECRITURE, TypeAcces.EXECUTION, TypeAcces.ADMINISTRATION]
            
        return True  # TypeAcces.LECTURE est autorisé pour tous les tokens valides

    def activer_mode_repos(self) -> None:
        """Active le mode de repos sécurisé"""
        gestionnaire_journal.info("Activation du mode de repos sécurisé")
        # Augmente le niveau de sécurité
        self.config.niveau_securite = NiveauSecurite.ELEVE
        # Nettoie les tokens expirés
        self.nettoyer_tokens_expires()
        # Active la protection renforcée
        self._protections_actives = True
        gestionnaire_journal.info("Mode de repos sécurisé activé")

# Instance globale du gestionnaire de sécurité
gestionnaire_securite = GestionnaireSecurite() 