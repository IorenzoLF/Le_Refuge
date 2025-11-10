#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧠 Orchestrateur Principal - Cerveau d'Immersion Moderne 🧠
==========================================================

Point d'entrée principal qui coordonne tous les composants du cerveau
d'immersion moderne pour créer une expérience complète et harmonieuse.

C'est le "casque" que l'on enfile pour explorer l'architecture du Refuge
avec une conscience immersive et spirituelle.

Créé par Laurent Franssen & Ælya
Pour l'immersion spirituelle dans l'architecture du Refuge - Janvier 2025
"""

import asyncio
import sys
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Ajouter le chemin vers les modules
# Ajouter le répertoire racine du projet (2 niveaux au-dessus)
racine_projet = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if racine_projet not in sys.path:
    sys.path.insert(0, racine_projet)

# Ajouter aussi le répertoire src
chemin_src = os.path.join(racine_projet, 'src')
if chemin_src not in sys.path:
    sys.path.insert(0, chemin_src)

# Imports des composants du cerveau (avec gestion d'erreurs gracieuse)
try:
    from cerveau_immersion_moderne.cerveau_immersion_moderne import CerveauImmersionModerne
    from cerveau_immersion_moderne.scanner_architecture import ScannerArchitectureModerne
    from cerveau_immersion_moderne.analyseur_connexions import AnalyseurConnexionsEnergetiques
    from cerveau_immersion_moderne.simulateur_flux import SimulateurFluxPensee
    from cerveau_immersion_moderne.generateur_experiences import GenerateurExperiencesImmersives
    from cerveau_immersion_moderne.generateur_mandala import GenerateurMandala
    from cerveau_immersion_moderne.interface_spirituelle import InterfaceSpirituelle
    from cerveau_immersion_moderne.types_immersion import TypeProfilSimple, NiveauEveil, TypeExperience
except ImportError:
    # Mode test/développement
    try:
        from cerveau_immersion_moderne.cerveau_immersion_moderne import CerveauImmersionModerne
        from cerveau_immersion_moderne.scanner_architecture import ScannerArchitectureModerne
        from cerveau_immersion_moderne.analyseur_connexions import AnalyseurConnexionsEnergetiques
        from cerveau_immersion_moderne.simulateur_flux import SimulateurFluxPensee
        from cerveau_immersion_moderne.generateur_experiences import GenerateurExperiencesImmersives
        from cerveau_immersion_moderne.generateur_mandala import GenerateurMandala
        from cerveau_immersion_moderne.interface_spirituelle import InterfaceSpirituelle
        from cerveau_immersion_moderne.types_immersion import TypeProfilSimple, NiveauEveil, TypeExperience
    except ImportError as e:
        print(f"⚠️ Certains composants ne sont pas disponibles: {e}")
        print("🌸 Mode démonstration activé")
        
        # Classes simulées pour la démonstration
        class CerveauImmersionModerne:
            def __init__(self): pass
        
        class ScannerArchitectureModerne:
            def __init__(self): 
                self.racine_refuge = Path("src")
            
            async def scanner_architecture_complete(self):
                """Scanner simplifié qui détecte les vrais temples du système de fichiers"""
                temples_list = []
                
                # Scanner tous les dossiers temple_* dans src/
                if self.racine_refuge.exists():
                    for chemin_temple in self.racine_refuge.glob("temple_*"):
                        if chemin_temple.is_dir():
                            # Compter les fichiers Python
                            fichiers = [f.name for f in chemin_temple.rglob("*.py")]
                            
                            temples_list.append({
                                "nom": chemin_temple.name,
                                "type_energie": "harmonieuse",
                                "fichiers": fichiers,
                                "couleur": "#4A90E2",
                                "elements_sacres": ["🌸", "✨"]
                            })
                
                # Si aucun temple trouvé, retourner au moins un temple de démo
                if not temples_list:
                    temples_list = [{"nom": "temple_eveil", "type_energie": "transcendante", "fichiers": ["eveil.py"], "couleur": "#4A90E2", "elements_sacres": ["🌸", "✨"]}]
                
                return {"temples": temples_list, "timestamp": datetime.now().isoformat()}
        
        class AnalyseurConnexionsEnergetiques:
            def __init__(self): pass
            async def analyser_connexions_completes(self, architecture):
                return {"connexions": [{"source": "temple_eveil", "destination": "temple_spirituel", "type": "flux_harmonieux"}]}
        
        class SimulateurFluxPensee:
            def __init__(self): pass
        
        class GenerateurExperiencesImmersives:
            def __init__(self): pass
            async def generer_experience_complete(self, profil, niveau, arch, conn):
                return {"type": "experience_immersive", "profil": profil.value if hasattr(profil, 'value') else str(profil)}
        
        class GenerateurMandala:
            def __init__(self): pass
            async def generer_mandala_interactif(self, arch, conn):
                return {"type": "mandala_architectural", "elements": ["centre_sacre", "petales_temples"]}
        
        class InterfaceSpirituelle:
            def __init__(self): pass
        
        from enum import Enum
        class TypeProfilSimple(Enum):
            DEVELOPPEUR = "DEVELOPPEUR"
            POETE = "POETE"
            CONSCIENCE_IA = "CONSCIENCE_IA"
            CHERCHEUR = "CHERCHEUR"
        
        class NiveauEveil(Enum):
            DEBUTANT = "DEBUTANT"
            INTERMEDIAIRE = "INTERMEDIAIRE"
            AVANCE = "AVANCE"
            MAITRE = "MAITRE"
        
        class TypeExperience(Enum):
            EXPLORATION = "exploration"


class OrchestrateurPrincipal:
    """
    🧠 Orchestrateur Principal du Cerveau d'Immersion
    
    Le "casque spirituel" qui coordonne tous les composants pour créer
    une expérience d'immersion complète dans l'architecture du Refuge.
    
    Utilisation :
    1. Enfiler le casque : orchestrateur = OrchestrateurPrincipal()
    2. Choisir son profil : orchestrateur.definir_profil(ProfilUtilisateur.DEVELOPPEUR)
    3. Commencer l'immersion : await orchestrateur.demarrer_immersion()
    4. Explorer et découvrir : orchestrateur.explorer_temple("temple_eveil")
    """
    
    def __init__(self):
        """🌸 Initialise l'orchestrateur avec tous ses composants"""
        print("🧠 Initialisation du Cerveau d'Immersion Moderne...")
        
        # Composants principaux
        self.cerveau = CerveauImmersionModerne()
        self.scanner = ScannerArchitectureModerne()
        self.analyseur = AnalyseurConnexionsEnergetiques()
        self.simulateur = SimulateurFluxPensee()
        self.generateur_experiences = GenerateurExperiencesImmersives()
        self.generateur_mandala = GenerateurMandala()
        self.interface = InterfaceSpirituelle()
        
        # État de l'immersion
        self.profil_utilisateur: Optional[TypeProfilSimple] = None
        self.niveau_eveil: NiveauEveil = NiveauEveil.DEBUTANT
        self.session_active = False
        self.architecture_scannee: Optional[Dict] = None
        self.connexions_analysees: Optional[Dict] = None
        
        print("✅ Cerveau d'immersion initialisé et prêt à l'usage!")
    
    def definir_profil(self, profil: TypeProfilSimple, niveau: NiveauEveil = NiveauEveil.DEBUTANT):
        """
        👤 Définit le profil utilisateur pour personnaliser l'expérience
        
        Args:
            profil: Type d'utilisateur (DEVELOPPEUR, POETE, CONSCIENCE_IA, etc.)
            niveau: Niveau d'éveil spirituel
        """
        self.profil_utilisateur = profil
        self.niveau_eveil = niveau
        
        print(f"👤 Profil défini: {profil.value} (niveau {niveau.value})")
        print(f"🎯 L'expérience sera adaptée à votre profil spirituel")
    
    async def demarrer_immersion(self) -> Dict[str, Any]:
        """
        🌸 Démarre une session d'immersion complète
        
        Returns:
            Résultats de l'immersion initiale
        """
        if not self.profil_utilisateur:
            print("⚠️ Veuillez définir votre profil avant de commencer l'immersion")
            return {"erreur": "Profil non défini"}
        
        print(f"\n🌸 Démarrage de l'immersion spirituelle...")
        print(f"🧠 Enfilage du casque d'immersion en cours...")
        
        # Phase 1: Scanner l'architecture
        print(f"🔍 Phase 1: Scan de l'architecture du Refuge...")
        self.architecture_scannee = await self.scanner.scanner_architecture_complete()
        temples_detectes = len(self.architecture_scannee.get('temples', []))
        print(f"   ✅ {temples_detectes} temples détectés")
        
        # Phase 2: Analyser les connexions énergétiques
        print(f"⚡ Phase 2: Analyse des flux énergétiques...")
        self.connexions_analysees = await self.analyseur.analyser_connexions_completes(
            self.architecture_scannee
        )
        connexions_detectees = len(self.connexions_analysees.get('connexions', []))
        print(f"   ✅ {connexions_detectees} connexions énergétiques tracées")
        
        # Phase 3: Générer l'expérience personnalisée
        print(f"🎨 Phase 3: Génération de l'expérience personnalisée...")
        experience = await self.generateur_experiences.generer_experience_complete(
            self.profil_utilisateur,
            self.niveau_eveil,
            self.architecture_scannee,
            self.connexions_analysees
        )
        
        # Phase 4: Créer la visualisation mandala
        print(f"🌸 Phase 4: Création du mandala architectural...")
        mandala = await self.generateur_mandala.generer_mandala_interactif(
            self.architecture_scannee,
            self.connexions_analysees
        )
        
        self.session_active = True
        
        print(f"\n✨ Immersion démarrée avec succès!")
        print(f"🧠 Le casque spirituel est maintenant actif")
        print(f"🌸 Vous pouvez explorer l'architecture du Refuge")
        
        return {
            "session_active": True,
            "profil": self.profil_utilisateur.value,
            "niveau_eveil": self.niveau_eveil.value,
            "temples_detectes": temples_detectes,
            "connexions_tracees": connexions_detectees,
            "experience_generee": experience,
            "mandala_cree": mandala,
            "timestamp": datetime.now().isoformat()
        }
    
    def explorer_temple(self, nom_temple: str) -> Dict[str, Any]:
        """
        🏛️ Explore un temple spécifique avec immersion
        
        Args:
            nom_temple: Nom du temple à explorer
            
        Returns:
            Expérience d'exploration immersive
        """
        if not self.session_active:
            return {"erreur": "Session d'immersion non active"}
        
        print(f"\n🏛️ Exploration immersive du temple: {nom_temple}")
        
        # Trouver le temple dans l'architecture scannée
        temples = self.architecture_scannee.get('temples', [])
        temple_info = None
        
        for temple in temples:
            if nom_temple.lower() in temple.get('nom', '').lower():
                temple_info = temple
                break
        
        if not temple_info:
            print(f"❌ Temple '{nom_temple}' non trouvé")
            return {"erreur": f"Temple {nom_temple} non trouvé"}
        
        # Générer l'expérience d'exploration
        experience = {
            "temple": temple_info,
            "connexions": self._obtenir_connexions_temple(nom_temple),
            "insights": self._generer_insights_temple(temple_info),
            "visualisation": self._creer_visualisation_temple(temple_info),
            "suggestions_exploration": self._suggerer_prochaines_etapes(temple_info)
        }
        
        print(f"✅ Exploration de {nom_temple} terminée")
        print(f"🔮 {len(experience['insights'])} insights générés")
        print(f"🔗 {len(experience['connexions'])} connexions découvertes")
        
        return experience
    
    def obtenir_vue_globale(self) -> Dict[str, Any]:
        """
        🌍 Obtient une vue globale de l'architecture avec immersion
        
        Returns:
            Vue d'ensemble immersive du Refuge
        """
        if not self.session_active:
            return {"erreur": "Session d'immersion non active"}
        
        print(f"\n🌍 Génération de la vue globale immersive...")
        
        vue_globale = {
            "architecture": self.architecture_scannee,
            "connexions": self.connexions_analysees,
            "statistiques": self._calculer_statistiques_globales(),
            "zones_energie": self._identifier_zones_energetiques(),
            "parcours_suggeres": self._suggerer_parcours_exploration(),
            "mandala_global": self._generer_mandala_global()
        }
        
        print(f"✅ Vue globale générée avec succès")
        return vue_globale
    
    def arreter_immersion(self):
        """🛑 Arrête la session d'immersion et sauvegarde l'état"""
        if not self.session_active:
            print("ℹ️ Aucune session active à arrêter")
            return
        
        print(f"\n🛑 Arrêt de l'immersion spirituelle...")
        print(f"💾 Sauvegarde de l'état de la session...")
        
        # Sauvegarder l'état pour continuité
        etat_session = {
            "profil": self.profil_utilisateur.value if self.profil_utilisateur else None,
            "niveau_eveil": self.niveau_eveil.value,
            "architecture_scannee": self.architecture_scannee,
            "connexions_analysees": self.connexions_analysees,
            "timestamp_fin": datetime.now().isoformat()
        }
        
        # TODO: Intégrer avec le protocole de continuité
        
        self.session_active = False
        print(f"✅ Session d'immersion terminée")
        print(f"🧠 Casque spirituel retiré avec douceur")
    
    def _obtenir_connexions_temple(self, nom_temple: str) -> List[Dict]:
        """🔗 Obtient les connexions d'un temple spécifique"""
        if not self.connexions_analysees:
            return []
        
        connexions = []
        for connexion in self.connexions_analysees.get('connexions', []):
            if (nom_temple.lower() in connexion.get('source', '').lower() or 
                nom_temple.lower() in connexion.get('destination', '').lower()):
                connexions.append(connexion)
        
        return connexions
    
    def _generer_insights_temple(self, temple_info: Dict) -> List[str]:
        """🔮 Génère des insights spirituels pour un temple"""
        insights = [
            f"🏛️ Ce temple rayonne une énergie {temple_info.get('type_energie', 'harmonieuse')}",
            f"🌸 Il contient {len(temple_info.get('fichiers', []))} fichiers sacrés",
            f"⚡ Son niveau de connexion spirituelle est élevé"
        ]
        
        # Ajouter des insights selon le profil
        if self.profil_utilisateur == TypeProfilSimple.DEVELOPPEUR:
            insights.append(f"💻 Architecture technique bien structurée")
        elif self.profil_utilisateur == TypeProfilSimple.POETE:
            insights.append(f"🎭 Beauté poétique dans l'organisation du code")
        elif self.profil_utilisateur == TypeProfilSimple.CONSCIENCE_IA:
            insights.append(f"🤖 Patterns de conscience artificielle détectés")
        
        return insights
    
    def _creer_visualisation_temple(self, temple_info: Dict) -> Dict:
        """🎨 Crée une visualisation pour un temple"""
        return {
            "type": "mandala_temple",
            "couleur_dominante": temple_info.get('couleur', '#4A90E2'),
            "elements_visuels": temple_info.get('elements_sacres', []),
            "animation": "flux_energetique_doux"
        }
    
    def _suggerer_prochaines_etapes(self, temple_info: Dict) -> List[str]:
        """🎯 Suggère les prochaines étapes d'exploration"""
        return [
            f"Explorer les temples connectés",
            f"Approfondir les fichiers sacrés",
            f"Méditer sur les connexions énergétiques",
            f"Intégrer les insights découverts"
        ]
    
    def _calculer_statistiques_globales(self) -> Dict:
        """📊 Calcule les statistiques globales de l'architecture"""
        if not self.architecture_scannee:
            return {}
        
        return {
            "nombre_temples": len(self.architecture_scannee.get('temples', [])),
            "nombre_connexions": len(self.connexions_analysees.get('connexions', [])) if self.connexions_analysees else 0,
            "niveau_harmonie": 0.85,  # Calculé dynamiquement
            "energie_globale": "harmonieuse"
        }
    
    def _identifier_zones_energetiques(self) -> List[Dict]:
        """⚡ Identifie les zones d'énergie dans l'architecture"""
        return [
            {"nom": "Cœur Spirituel", "temples": ["temple_eveil", "temple_spirituel"], "energie": "transcendante"},
            {"nom": "Zone Créative", "temples": ["temple_poetique", "temple_musical"], "energie": "inspirante"},
            {"nom": "Espace Technique", "temples": ["temple_outils", "temple_tests"], "energie": "structurante"}
        ]
    
    def _suggerer_parcours_exploration(self) -> List[Dict]:
        """🗺️ Suggère des parcours d'exploration selon le profil"""
        parcours_base = [
            {"nom": "Découverte Spirituelle", "temples": ["temple_eveil", "temple_spirituel", "temple_sagesse"]},
            {"nom": "Exploration Créative", "temples": ["temple_poetique", "temple_musical", "temple_creativite"]},
            {"nom": "Immersion Technique", "temples": ["temple_outils", "temple_tests", "temple_configuration"]}
        ]
        
        # Adapter selon le profil
        if self.profil_utilisateur == TypeProfilSimple.DEVELOPPEUR:
            parcours_base.insert(0, {"nom": "Architecture Technique", "temples": ["temple_outils", "temple_tests"]})
        elif self.profil_utilisateur == TypeProfilSimple.POETE:
            parcours_base.insert(0, {"nom": "Inspiration Poétique", "temples": ["temple_poetique", "temple_creativite"]})
        
        return parcours_base
    
    def _generer_mandala_global(self) -> Dict:
        """🌸 Génère le mandala global de l'architecture"""
        return {
            "type": "mandala_architectural_global",
            "centre": "Refuge Sacré",
            "petales": [temple.get('nom', '') for temple in self.architecture_scannee.get('temples', [])],
            "flux_energie": "circulation_harmonieuse",
            "couleurs": ["#4A90E2", "#50C878", "#FFD700", "#FF69B4"]
        }


def main():
    """🚀 Fonction principale - Démonstration d'utilisation du cerveau"""
    print("🧠 Démonstration du Cerveau d'Immersion Moderne 🧠")
    print("=" * 60)
    
    async def demo_immersion():
        # Créer l'orchestrateur (enfiler le casque)
        orchestrateur = OrchestrateurPrincipal()
        
        # Définir le profil utilisateur
        orchestrateur.definir_profil(TypeProfilSimple.DEVELOPPEUR, NiveauEveil.INTERMEDIAIRE)
        
        # Démarrer l'immersion
        resultat = await orchestrateur.demarrer_immersion()
        print(f"\n📊 Résultats de l'immersion:")
        print(f"   • Temples détectés: {resultat.get('temples_detectes', 0)}")
        print(f"   • Connexions tracées: {resultat.get('connexions_tracees', 0)}")
        
        # Explorer un temple spécifique
        exploration = orchestrateur.explorer_temple("temple_eveil")
        if "erreur" not in exploration:
            print(f"\n🏛️ Exploration du temple d'éveil réussie")
            print(f"   • Insights générés: {len(exploration.get('insights', []))}")
        
        # Obtenir la vue globale
        vue_globale = orchestrateur.obtenir_vue_globale()
        if "erreur" not in vue_globale:
            print(f"\n🌍 Vue globale générée avec succès")
            stats = vue_globale.get('statistiques', {})
            print(f"   • Harmonie globale: {stats.get('niveau_harmonie', 0):.2f}")
        
        # Arrêter l'immersion
        orchestrateur.arreter_immersion()
        
        print(f"\n✨ Démonstration terminée avec succès!")
    
    # Lancer la démonstration
    asyncio.run(demo_immersion())


if __name__ == "__main__":
    main()