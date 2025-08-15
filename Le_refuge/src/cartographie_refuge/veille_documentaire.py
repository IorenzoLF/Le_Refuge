#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔍 Système de Veille Documentaire - Cartographie Spirituelle du Refuge 🔍
=========================================================================

Système intelligent de détection automatique des incohérences documentaires
et de maintenance proactive de la cohérence informationnelle.

"Que chaque mot soit juste, que chaque information soit harmonieuse"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import re
import json
import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

# Imports du Refuge
try:
    from ..core.gestionnaires_base import GestionnaireBase
except ImportError:
    # Fallback pour les tests
    import sys
    sys.path.append('src')
    from core.gestionnaires_base import GestionnaireBase


class TypeIncoherence(Enum):
    """Types d'incohérences documentaires détectables"""
    NOMBRE_TEMPLES = "nombre_temples"
    REFERENCE_TEMPORELLE = "reference_temporelle"
    VERSION_OBSOLETE = "version_obsolete"
    LIEN_BRISE = "lien_brise"
    INFORMATION_CONTRADICTOIRE = "information_contradictoire"
    DOCUMENTATION_MANQUANTE = "documentation_manquante"


class NiveauGravite(Enum):
    """Niveaux de gravité des incohérences"""
    INFO = "info"
    ATTENTION = "attention"
    IMPORTANT = "important"
    CRITIQUE = "critique"


@dataclass
class IncohérenceDetectee:
    """Représente une incohérence documentaire détectée"""
    type_incoherence: TypeIncoherence
    fichier: Path
    ligne: Optional[int] = None
    contenu_actuel: str = ""
    contenu_attendu: str = ""
    description: str = ""
    gravite: NiveauGravite = NiveauGravite.ATTENTION
    suggestion_correction: str = ""
    timestamp_detection: datetime = field(default_factory=datetime.now)


@dataclass
class RapportVeille:
    """Rapport complet de veille documentaire"""
    timestamp_generation: datetime
    fichiers_analyses: int = 0
    incoherences_detectees: List[IncohérenceDetectee] = field(default_factory=list)
    metriques_qualite: Dict[str, Any] = field(default_factory=dict)
    recommandations: List[str] = field(default_factory=list)
    actions_correctives: List[str] = field(default_factory=list)


class VeilleDocumentaireSpirituelle(GestionnaireBase):
    """
    🔍 Système de Veille Documentaire Spirituelle 🔍
    
    Détecte automatiquement les incohérences dans la documentation
    et propose des corrections harmonieuses pour maintenir la cohérence
    informationnelle du Refuge.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialise le système de veille documentaire
        
        Args:
            config: Configuration optionnelle du système
        """
        super().__init__(config or {})
        
        # Configuration
        self.refuge_root = Path.cwd()
        self.patterns_documentation = [
            "*.md", "*.rst", "*.txt", "README*", "GUIDE*", "DOCUMENTATION*"
        ]
        
        # Patterns de détection
        self.patterns_temples = {
            r'(\d+)\s+temples?': TypeIncoherence.NOMBRE_TEMPLES,
            r'Index.*des\s+(\d+)\s+temples': TypeIncoherence.NOMBRE_TEMPLES,
            r'(\d+)\s+Temples\s+Actifs': TypeIncoherence.NOMBRE_TEMPLES,
        }
        
        self.patterns_temporels = {
            r'avant.*découverte.*océan': TypeIncoherence.REFERENCE_TEMPORELLE,
            r'pré.*océan': TypeIncoherence.REFERENCE_TEMPORELLE,
            r'(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s+2024': TypeIncoherence.VERSION_OBSOLETE,
        }
        
        # Cache des résultats
        self.cache_temples_actifs: Optional[int] = None
        self.derniere_analyse: Optional[datetime] = None
        
        # Initialisation
        self._initialiser_veille()
    
    def _initialiser_veille(self) -> None:
        """Initialise le système de veille"""
        try:
            self.logger.info("🔍 Initialisation de la Veille Documentaire Spirituelle...")
            self.logger.info("✨ Système de veille initialisé avec bienveillance")
        except Exception as e:
            print(f"❌ Erreur lors de l'initialisation de la veille: {e}")
            raise
    
    async def analyser_coherence_complete(self) -> RapportVeille:
        """
        Effectue une analyse complète de cohérence documentaire
        
        Returns:
            RapportVeille: Rapport complet des incohérences détectées
        """
        self.logger.info("🔍 Analyse complète de cohérence documentaire")
        
        rapport = RapportVeille(timestamp_generation=datetime.now())
        
        try:
            # 1. Compter les temples actifs (référence)
            temples_actifs = await self._compter_temples_actifs()
            self.cache_temples_actifs = temples_actifs
            
            # 2. Analyser tous les fichiers de documentation
            fichiers_doc = await self._collecter_fichiers_documentation()
            rapport.fichiers_analyses = len(fichiers_doc)
            
            # 3. Détecter les incohérences
            for fichier in fichiers_doc:
                incoherences = await self._analyser_fichier(fichier, temples_actifs)
                rapport.incoherences_detectees.extend(incoherences)
            
            # 4. Calculer les métriques de qualité
            rapport.metriques_qualite = self._calculer_metriques_qualite(rapport)
            
            # 5. Générer les recommandations
            rapport.recommandations = self._generer_recommandations(rapport)
            rapport.actions_correctives = self._generer_actions_correctives(rapport)
            
            self.derniere_analyse = datetime.now()
            
            self.logger.info(f"✅ Analyse terminée: {len(rapport.incoherences_detectees)} incohérences détectées")
            return rapport
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'analyse de cohérence: {e}")
            raise
    
    async def _compter_temples_actifs(self) -> int:
        """Compte le nombre réel de temples actifs dans le Refuge"""
        temples_dir = self.refuge_root / "src"
        if not temples_dir.exists():
            return 0
        
        temples = [d for d in temples_dir.iterdir() 
                  if d.is_dir() and d.name.startswith('temple_')]
        
        self.logger.debug(f"🏛️ {len(temples)} temples actifs détectés")
        return len(temples)
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre les opérations de veille documentaire"""
        try:
            rapport = await self.analyser_coherence_complete()
            score_coherence = rapport.metriques_qualite.get('score_coherence_pct', 0) / 100.0
            
            return {
                "coherence_documentaire": score_coherence,
                "temples_detectes": float(self.cache_temples_actifs or 0),
                "incoherences_detectees": float(len(rapport.incoherences_detectees))
            }
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'orchestration: {e}")
            return {"erreur": 1.0}
    
    def __str__(self) -> str:
        return f"VeilleDocumentaireSpirituelle(dernière_analyse={self.derniere_analyse})"
    
    def __repr__(self) -> str:
        return self.__str__()


async def main():
    """🔍 Fonction principale de veille documentaire"""
    print("🔍✨ VEILLE DOCUMENTAIRE SPIRITUELLE DU REFUGE ✨🔍")
    
    # Initialisation
    veille = VeilleDocumentaireSpirituelle()
    
    try:
        print("✅ Système de veille documentaire initialisé avec succès")
        return 0
        
    except Exception as e:
        print(f"❌ ERREUR CRITIQUE: {e}")
        return 2


if __name__ == "__main__":
    import asyncio
    exit_code = asyncio.run(main())
    exit(exit_code)