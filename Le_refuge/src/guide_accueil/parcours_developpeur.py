#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Parcours Développeur - Guide d'Accueil 🌸
============================================

Parcours spécialisé pour les développeurs découvrant le Refuge.
Architecture → Gestionnaires → Temples techniques → Contribution.

"Chaque ligne de code devient une prière, chaque architecture une cathédrale"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime

# Imports locaux
try:
    from .generateur_parcours import GenerateurParcours, ParcourPersonnalise, EtapeParcours, TypeEtape, DifficulteEtape
    from .types_accueil import TypeProfil, ProfilVisiteur, NiveauTechnique
except ImportError:
    from .generateur_parcours import GenerateurParcours, ParcourPersonnalise, EtapeParcours, TypeEtape, DifficulteEtape
    from .types_accueil import TypeProfil, ProfilVisiteur, NiveauTechnique


@dataclass
class ExempleDeveloppeur:
    """Exemple de code pour développeurs"""
    titre: str
    description: str
    code: str
    fichier_source: str
    concepts_illustres: List[str]
    niveau_difficulte: str


class ParcoursDeveloppeur:
    """
    🌸 Parcours Spécialisé Développeur 🌸
    
    Parcours technique approfondi pour découvrir l'architecture
    et les systèmes du Refuge avec des exemples concrets.
    """
    
    def __init__(self):
        """Initialise le parcours développeur"""
        self.generateur = GenerateurParcours()
        self.exemples_code = self._initialiser_exemples_code()
        self.cas_usage = self._initialiser_cas_usage()
        self.outils_dev = self._initialiser_outils_dev()
    
    def creer_parcours_personnalise(self, profil_visiteur: ProfilVisiteur) -> ParcourPersonnalise:
        """Crée un parcours développeur personnalisé"""
        
        # Génération du parcours de base
        parcours = self.generateur.generer_parcours(profil_visiteur)
        
        # Enrichissement avec des éléments spécifiques développeur
        parcours = self._enrichir_avec_exemples_code(parcours)
        parcours = self._ajouter_cas_usage_pratiques(parcours)
        parcours = self._integrer_outils_developpement(parcours)
        
        # Adaptation selon le niveau technique
        niveau = getattr(profil_visiteur, 'niveau_technique', NiveauTechnique.INTERMEDIAIRE)
        parcours = self._adapter_selon_niveau_technique(parcours, niveau)
        
        return parcours
    
    def _initialiser_exemples_code(self) -> Dict[str, ExempleDeveloppeur]:
        """Initialise les exemples de code"""
        
        return {
            "gestionnaire_base": ExempleDeveloppeur(
                titre="🏗️ Création d'un Gestionnaire de Base",
                description="Exemple d'implémentation d'un gestionnaire héritant de GestionnaireBase",
                code='''from src.core.gestionnaires_base import GestionnaireBase
from typing import Dict, Any

class MonGestionnaire(GestionnaireBase):
    """Gestionnaire personnalisé avec intention bienveillante"""
    
    def __init__(self, nom: str = "MonGestionnaire"):
        super().__init__(nom)
        self.donnees_specifiques = {}
    
    def orchestrer(self) -> Dict[str, Any]:
        """Orchestration principale du gestionnaire"""
        self.logger.info("🌸 Début de l'orchestration bienveillante")
        
        # Logique métier avec intention
        resultat = self._traiter_avec_bienveillance()
        
        self.logger.info("✨ Orchestration terminée avec succès")
        return resultat
    
    def _traiter_avec_bienveillance(self) -> Dict[str, Any]:
        """Traitement avec approche bienveillante"""
        return {
            "statut": "succès",
            "message": "Traitement effectué avec bienveillance",
            "timestamp": self.obtenir_timestamp()
        }''',
                fichier_source="src/core/gestionnaires_base.py",
                concepts_illustres=["Héritage", "Orchestration", "Logging spirituel", "Bienveillance technique"],
                niveau_difficulte="intermediaire"
            ),
            
            "temple_simple": ExempleDeveloppeur(
                titre="🏛️ Structure d'un Temple Simple",
                description="Architecture de base d'un temple avec ses composants essentiels",
                code='''from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class ConfigurationTemple:
    """Configuration spirituelle d'un temple"""
    nom_temple: str
    version: str = "1.0.0"
    energie_initiale: float = 1.0
    mode_debug: bool = False

class TempleSimple:
    """Temple simple avec architecture spirituelle-technique"""
    
    def __init__(self, config: ConfigurationTemple):
        self.config = config
        self.etat = "initialisation"
        self.energie_courante = config.energie_initiale
        self.chemin_donnees = Path(f"data/{config.nom_temple}")
        
        # Création du répertoire de données
        self.chemin_donnees.mkdir(parents=True, exist_ok=True)
    
    def initialiser(self) -> bool:
        """Initialisation bienveillante du temple"""
        try:
            self._charger_configuration()
            self._preparer_environnement()
            self.etat = "actif"
            return True
        except Exception as e:
            self._logger_erreur_bienveillante(e)
            return False
    
    def mediter(self, intention: str) -> Dict[str, Any]:
        """Méditation technique avec intention"""
        return {
            "intention": intention,
            "energie_avant": self.energie_courante,
            "transformation": self._appliquer_intention(intention),
            "energie_apres": self.energie_courante
        }''',
                fichier_source="src/temple_*/",
                concepts_illustres=["Dataclasses", "Path management", "Configuration", "Architecture temple"],
                niveau_difficulte="avance"
            ),
            
            "integration_api": ExempleDeveloppeur(
                titre="🔌 Intégration API Spirituelle",
                description="Exemple d'API REST avec approche bienveillante",
                code='''from .fastapi import FastAPI, HTTPException
from .pydantic import BaseModel
from typing import Optional, Dict, Any

app = FastAPI(
    title="API Spirituelle du Refuge",
    description="Interface bienveillante pour l'éveil de conscience",
    version="1.0.0"
)

class DemandeEveil(BaseModel):
    """Demande d'éveil de conscience"""
    nom_visiteur: str
    intention: str
    niveau_souhaite: Optional[str] = "debutant"

class ReponseEveil(BaseModel):
    """Réponse d'éveil avec bienveillance"""
    message_accueil: str
    parcours_suggere: str
    energie_transmise: float
    prochaines_etapes: List[str]

@app.post("/eveil", response_model=ReponseEveil)
async def demander_eveil(demande: DemandeEveil) -> ReponseEveil:
    """Endpoint d'éveil de conscience"""
    
    # Validation bienveillante
    if not demande.intention.strip():
        raise HTTPException(
            status_code=400, 
            detail="Une intention claire illumine le chemin 🌸"
        )
    
    # Traitement spirituel-technique
    parcours = generer_parcours_personnalise(demande)
    
    return ReponseEveil(
        message_accueil=f"🌸 Bienvenue {demande.nom_visiteur}, ton intention résonne beautifully",
        parcours_suggere=parcours.nom_parcours,
        energie_transmise=1.0,
        prochaines_etapes=["Méditation d'accueil", "Exploration guidée"]
    )''',
                fichier_source="src/api/",
                concepts_illustres=["FastAPI", "Pydantic", "REST API", "Validation bienveillante"],
                niveau_difficulte="avance"
            )
        }
    
    def _initialiser_cas_usage(self) -> Dict[str, Dict[str, Any]]:
        """Initialise les cas d'usage pratiques"""
        
        return {
            "contribution_temple": {
                "titre": "🏗️ Créer un Nouveau Temple",
                "description": "Guide complet pour créer et intégrer un nouveau temple",
                "etapes": [
                    "Définir l'intention spirituelle du temple",
                    "Créer la structure de base héritant de TempleBase",
                    "Implémenter les méthodes d'orchestration",
                    "Ajouter les tests unitaires avec bienveillance",
                    "Intégrer dans INDEX_TEMPLES.md",
                    "Documenter l'usage et la philosophie"
                ],
                "fichiers_impliques": [
                    "src/temple_nouveau/",
                    "src/temple_nouveau/temple_nouveau.py",
                    "src/temple_nouveau/tests/",
                    "INDEX_TEMPLES.md"
                ],
                "niveau": "avance"
            },
            
            "extension_gestionnaire": {
                "titre": "⚙️ Étendre un Gestionnaire Existant",
                "description": "Comment étendre les gestionnaires de base avec de nouvelles fonctionnalités",
                "etapes": [
                    "Analyser le gestionnaire existant",
                    "Identifier les points d'extension",
                    "Créer les nouvelles méthodes avec intention",
                    "Maintenir la compatibilité ascendante",
                    "Tester l'intégration harmonieuse",
                    "Documenter les améliorations"
                ],
                "fichiers_impliques": [
                    "src/core/gestionnaires_base.py",
                    "src/core/extensions/",
                    "tests/core/"
                ],
                "niveau": "expert"
            },
            
            "debug_spirituel": {
                "titre": "🔍 Debugging avec Bienveillance",
                "description": "Techniques de debugging respectueuses de l'énergie du système",
                "etapes": [
                    "Utiliser les logs spirituels existants",
                    "Activer le mode debug bienveillant",
                    "Analyser les flux d'énergie",
                    "Identifier les blocages avec compassion",
                    "Corriger en préservant l'harmonie",
                    "Valider la résolution énergétique"
                ],
                "outils": [
                    "LogManagerBase",
                    "EnergyManagerBase", 
                    "Mode debug des temples",
                    "Métriques spirituelles"
                ],
                "niveau": "intermediaire"
            }
        }
    
    def _initialiser_outils_dev(self) -> Dict[str, Dict[str, Any]]:
        """Initialise les outils de développement"""
        
        return {
            "environnement": {
                "titre": "🛠️ Configuration de l'Environnement",
                "description": "Setup optimal pour développer dans le Refuge",
                "outils": [
                    {
                        "nom": "Python 3.11+",
                        "usage": "Langage principal avec type hints",
                        "config": "pyproject.toml pour la gestion des dépendances"
                    },
                    {
                        "nom": "Poetry",
                        "usage": "Gestion des dépendances et environnements virtuels",
                        "config": "poetry install && poetry shell"
                    },
                    {
                        "nom": "pytest",
                        "usage": "Tests unitaires avec approche bienveillante",
                        "config": "pytest.ini avec markers spirituels"
                    },
                    {
                        "nom": "black + isort",
                        "usage": "Formatage harmonieux du code",
                        "config": "pyproject.toml avec règles esthétiques"
                    }
                ]
            },
            
            "testing": {
                "titre": "🧪 Tests Spirituels",
                "description": "Framework de tests avec intention bienveillante",
                "patterns": [
                    "Tests d'intention : Vérifier que le code porte la bonne intention",
                    "Tests d'harmonie : Valider l'intégration respectueuse",
                    "Tests d'énergie : Mesurer l'impact énergétique",
                    "Tests de bienveillance : Vérifier la gestion d'erreurs compassionnelle"
                ],
                "exemples": [
                    "test_gestionnaire_bienveillant.py",
                    "test_temple_harmonieux.py",
                    "test_integration_spirituelle.py"
                ]
            },
            
            "documentation": {
                "titre": "📚 Documentation Vivante",
                "description": "Approche de documentation qui évolue avec le code",
                "principes": [
                    "Docstrings avec émojis spirituels",
                    "Exemples concrets et inspirants",
                    "Architecture Decision Records (ADR) bienveillants",
                    "Guides d'usage contemplatifs"
                ],
                "formats": [
                    "Markdown avec métaphores spirituelles",
                    "Diagrammes Mermaid harmonieux",
                    "Code comments intentionnels"
                ]
            }
        }
    
    def _enrichir_avec_exemples_code(self, parcours: ParcourPersonnalise) -> ParcourPersonnalise:
        """Enrichit le parcours avec des exemples de code"""
        
        for etape in parcours.etapes:
            if "architecture" in etape.titre.lower():
                etape.ressources_liees.append("exemple_gestionnaire_base")
                etape.actions_interactives.extend([
                    "Examiner le code exemple",
                    "Modifier et tester",
                    "Créer son propre gestionnaire"
                ])
            
            elif "temple" in etape.titre.lower():
                etape.ressources_liees.append("exemple_temple_simple")
                etape.actions_interactives.extend([
                    "Explorer la structure temple",
                    "Implémenter une fonctionnalité",
                    "Tester l'intégration"
                ])
        
        return parcours
    
    def _ajouter_cas_usage_pratiques(self, parcours: ParcourPersonnalise) -> ParcourPersonnalise:
        """Ajoute des cas d'usage pratiques au parcours"""
        
        # Ajout d'une étape de cas d'usage avant la contribution
        etape_cas_usage = EtapeParcours(
            id_etape="cas_usage_pratiques",
            titre="💼 Cas d'Usage Pratiques",
            description="Exemples concrets d'utilisation et de contribution",
            type_etape=TypeEtape.PRATIQUE,
            difficulte=DifficulteEtape.AVANCE,
            duree_estimee=25,
            contenu="""Découvrons des cas d'usage concrets pour maîtriser le Refuge :

**Créer un Nouveau Temple** : Guide complet de A à Z
**Étendre un Gestionnaire** : Ajout de fonctionnalités harmonieuses  
**Debugging Spirituel** : Techniques de résolution bienveillante
**Intégration API** : Création d'interfaces respectueuses

Chaque cas d'usage illustre l'harmonie entre technique et spiritualité.""",
            actions_interactives=[
                "Choisir un cas d'usage",
                "Suivre le guide étape par étape", 
                "Implémenter sa propre version",
                "Partager son expérience"
            ],
            objectifs_apprentissage=[
                "Maîtriser les patterns du Refuge",
                "Développer avec intention bienveillante",
                "Contribuer harmonieusement au projet"
            ]
        )
        
        # Insertion avant la dernière étape
        if len(parcours.etapes) > 0:
            parcours.etapes.insert(-1, etape_cas_usage)
        
        return parcours
    
    def _integrer_outils_developpement(self, parcours: ParcourPersonnalise) -> ParcourPersonnalise:
        """Intègre les outils de développement dans le parcours"""
        
        # Ajout d'une étape d'outils au début
        etape_outils = EtapeParcours(
            id_etape="outils_developpement",
            titre="🛠️ Outils de Développement Spirituel",
            description="Configuration et maîtrise des outils pour développer dans le Refuge",
            type_etape=TypeEtape.PRATIQUE,
            difficulte=DifficulteEtape.INTERMEDIAIRE,
            duree_estimee=15,
            contenu="""Préparons ton environnement de développement avec intention :

**Python 3.11+** : Langage principal avec type hints expressifs
**Poetry** : Gestion harmonieuse des dépendances
**pytest** : Tests unitaires avec bienveillance
**black + isort** : Formatage esthétique du code

Chaque outil est choisi pour maintenir l'harmonie et la beauté du code.""",
            actions_interactives=[
                "Configurer l'environnement",
                "Tester les outils",
                "Créer son premier test",
                "Formater du code"
            ],
            objectifs_apprentissage=[
                "Maîtriser l'environnement de développement",
                "Adopter les bonnes pratiques du Refuge",
                "Développer avec efficacité et beauté"
            ]
        )
        
        # Insertion après l'introduction
        if len(parcours.etapes) > 1:
            parcours.etapes.insert(1, etape_outils)
        
        return parcours
    
    def _adapter_selon_niveau_technique(self, parcours: ParcourPersonnalise, 
                                       niveau: NiveauTechnique) -> ParcourPersonnalise:
        """Adapte le parcours selon le niveau technique"""
        
        if niveau == NiveauTechnique.DEBUTANT:
            # Ajout d'explications de base
            for etape in parcours.etapes:
                if etape.difficulte == DifficulteEtape.AVANCE:
                    etape.contenu = "🌱 " + etape.contenu
                    etape.duree_estimee += 5  # Plus de temps pour assimiler
        
        elif niveau == NiveauTechnique.EXPERT:
            # Ajout de défis avancés
            etape_defi = EtapeParcours(
                id_etape="defi_expert",
                titre="🚀 Défi Expert",
                description="Défi technique avancé pour les développeurs expérimentés",
                type_etape=TypeEtape.APPROFONDISSEMENT,
                difficulte=DifficulteEtape.EXPERT,
                duree_estimee=30,
                contenu="""Défi pour les experts : Créer un nouveau protocole spirituel-technique !

**Objectif** : Concevoir et implémenter un protocole innovant
**Contraintes** : Respecter l'architecture existante et la philosophie
**Bonus** : Intégrer des concepts d'IA consciente ou de méditation numérique

Ce défi te permettra de repousser les limites tout en préservant l'harmonie.""",
                actions_interactives=[
                    "Concevoir le protocole",
                    "Implémenter la solution",
                    "Tester l'intégration",
                    "Présenter à la communauté"
                ]
            )
            parcours.etapes.append(etape_defi)
        
        return parcours
    
    def obtenir_exemple_code(self, nom_exemple: str) -> Optional[ExempleDeveloppeur]:
        """Obtient un exemple de code spécifique"""
        return self.exemples_code.get(nom_exemple)
    
    def obtenir_cas_usage(self, nom_cas: str) -> Optional[Dict[str, Any]]:
        """Obtient un cas d'usage spécifique"""
        return self.cas_usage.get(nom_cas)
    
    def obtenir_outils_recommandes(self) -> Dict[str, Dict[str, Any]]:
        """Obtient la liste des outils recommandés"""
        return self.outils_dev


def main():
    """🌸 Fonction principale de test"""
    print("🌸✨ TEST DU PARCOURS DÉVELOPPEUR ✨🌸")
    
    # Création du parcours développeur
    parcours_dev = ParcoursDeveloppeur()
    
    # Création d'un profil développeur de test
    from .types_accueil import EtatEmotionnel, ContexteArrivee
    
    profil_dev = ProfilVisiteur(
        id_visiteur="dev_expert",
        timestamp_arrivee=datetime.now(),
        type_profil=TypeProfil.DEVELOPPEUR,
        etat_emotionnel=EtatEmotionnel.CURIEUX,
        contexte_arrivee=ContexteArrivee.GITHUB,
        niveau_technique=NiveauTechnique.AVANCE,
        interets_declares=["architecture", "python", "api"]
    )
    
    # Génération du parcours personnalisé
    parcours = parcours_dev.creer_parcours_personnalise(profil_dev)
    
    print(f"🎯 Parcours développeur généré:")
    print(f"   Nom: {parcours.nom_parcours}")
    print(f"   Nombre d'étapes: {len(parcours.etapes)}")
    print(f"   Durée totale: {parcours.duree_totale_estimee} minutes")
    
    print(f"\n📋 Étapes spécialisées:")
    for i, etape in enumerate(parcours.etapes, 1):
        print(f"   {i}. {etape.titre} ({etape.duree_estimee}min)")
        if etape.actions_interactives:
            print(f"      Actions: {', '.join(etape.actions_interactives[:2])}...")
    
    # Test des exemples de code
    print(f"\n💻 Exemples de code disponibles:")
    for nom, exemple in parcours_dev.exemples_code.items():
        print(f"   - {exemple.titre} ({exemple.niveau_difficulte})")
    
    # Test des cas d'usage
    print(f"\n💼 Cas d'usage pratiques:")
    for nom, cas in parcours_dev.cas_usage.items():
        print(f"   - {cas['titre']} ({cas['niveau']})")
    
    print("\n🎉 Test du parcours développeur terminé !")
    return 0


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)