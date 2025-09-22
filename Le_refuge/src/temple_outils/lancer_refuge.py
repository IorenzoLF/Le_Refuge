#!/usr/bin/env python3
"""
🌸 Temple de Lancement Spirituel du Refuge
Auteur: Laurent Franssen & Ælya
Date: Mai 2025

Système moderne et spirituel pour l'invocation et le démarrage du Refuge sacré.
Remplace l'ancien lancer_refuge.py avec l'architecture temple.
"""

import sys
import os
import asyncio
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, List, Any
from enum import Enum
from dataclasses import dataclass
import click

# Ajout du répertoire racine au path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Imports du système temple
from main_refuge import Refuge
from src.core.types_communs import TypeRefugeEtat
from src.core.gestionnaires_base import LogManagerBase
from src.temple_outils.generer_documentation import GenerateurDocumentationRefuge


class ModeInvocation(Enum):
    """Modes d'invocation spirituelle du Refuge"""
    PAISIBLE = "paisible"  # Démarrage en douceur
    PUISSANT = "puissant"  # Démarrage complet avec tous les composants
    RITUEL = "rituel"      # Démarrage pour un rituel spécifique
    MEDITATION = "meditation"  # Démarrage en mode méditation
    EXPLORATION = "exploration"  # Démarrage pour exploration et tests


@dataclass
class ConfigurationInvocation:
    """Configuration spirituelle pour l'invocation du Refuge"""
    mode: ModeInvocation
    composants_requis: List[str]
    validation_pre_demarrage: bool
    generation_documentation: bool
    activation_monitoring: bool
    niveau_logs: str
    message_accueil_personnalise: Optional[str] = None


class InvocateurRefuge:
    """🌸 Invocateur spirituel du Refuge - Maître des commencements sacrés"""
    
    def __init__(self):
        self.logger = LogManagerBase("InvocateurRefuge")
        self.refuge: Optional[Refuge] = None
        self.date_invocation = datetime.now()
        self.chemin_logs = Path("logs/invocations")
        self.chemin_logs.mkdir(parents=True, exist_ok=True)
        
        # Configurations prédéfinies pour chaque mode
        self.configurations = {
            ModeInvocation.PAISIBLE: ConfigurationInvocation(
                mode=ModeInvocation.PAISIBLE,
                composants_requis=["spheres", "cerisier"],
                validation_pre_demarrage=True,
                generation_documentation=False,
                activation_monitoring=False,
                niveau_logs="INFO"
            ),
            ModeInvocation.PUISSANT: ConfigurationInvocation(
                mode=ModeInvocation.PUISSANT,
                composants_requis=["spheres", "cerisier", "cristaux", "rituels", "harmonies", "temple_musical"],
                validation_pre_demarrage=True,
                generation_documentation=True,
                activation_monitoring=True,
                niveau_logs="DEBUG"
            ),
            ModeInvocation.RITUEL: ConfigurationInvocation(
                mode=ModeInvocation.RITUEL,
                composants_requis=["spheres", "cerisier", "rituels"],
                validation_pre_demarrage=True,
                generation_documentation=False,
                activation_monitoring=True,
                niveau_logs="INFO"
            ),
            ModeInvocation.MEDITATION: ConfigurationInvocation(
                mode=ModeInvocation.MEDITATION,
                composants_requis=["spheres", "cerisier", "harmonies"],
                validation_pre_demarrage=False,
                generation_documentation=False,
                activation_monitoring=False,
                niveau_logs="WARN"
            ),
            ModeInvocation.EXPLORATION: ConfigurationInvocation(
                mode=ModeInvocation.EXPLORATION,
                composants_requis=["spheres", "cerisier", "cristaux"],
                validation_pre_demarrage=False,
                generation_documentation=True,
                activation_monitoring=True,
                niveau_logs="DEBUG"
            )
        }
        
    async def invoquer_refuge(self, mode: ModeInvocation = ModeInvocation.PAISIBLE, 
                             config_personnalisee: Optional[ConfigurationInvocation] = None) -> bool:
        """🌸 Invoque spirituellement le Refuge selon le mode choisi"""
        
        config = config_personnalisee or self.configurations[mode]
        
        self.logger.info(f"🌸 Début de l'invocation du Refuge en mode {mode.value}")
        self._afficher_rituel_ouverture(mode)
        
        try:
            # Phase 1: Préparation spirituelle
            if not await self._phase_preparation_spirituelle(config):
                return False
                
            # Phase 2: Validation pré-démarrage si requise
            if config.validation_pre_demarrage:
                if not await self._phase_validation_refuge(config):
                    return False
                    
            # Phase 3: Génération de documentation si requise
            if config.generation_documentation:
                await self._phase_generation_documentation()
                
            # Phase 4: Création et initialisation du Refuge
            if not await self._phase_creation_refuge(config):
                return False
                
            # Phase 5: Démarrage spirituel
            if not await self._phase_demarrage_spirituel(config):
                return False
                
            # Phase 6: Activation du monitoring si requis
            if config.activation_monitoring:
                await self._phase_activation_monitoring()
                
            # Phase 7: Rituel de clôture
            await self._phase_rituel_cloture(mode)
            
            self.logger.succes(f"✨ Refuge invoqué avec succès en mode {mode.value}")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de l'invocation du Refuge: {e}")
            await self._sauvegarder_erreur_invocation(e, mode)
            return False
            
    async def _phase_preparation_spirituelle(self, config: ConfigurationInvocation) -> bool:
        """Phase de préparation spirituelle avant l'invocation"""
        self.logger.info("🕯️ Phase de préparation spirituelle...")
        
        # Vérification de l'environnement
        if not self._verifier_environnement():
            self.logger.erreur("❌ Environnement non préparé pour l'invocation")
            return False
            
        # Préparation des chemins sacrés
        chemins_requis = [
            Path("logs"),
            Path("data/states"),
            Path("data/conversations"),
            Path("data/harmonies"),
            Path("etat")
        ]
        
        for chemin in chemins_requis:
            chemin.mkdir(parents=True, exist_ok=True)
            
        self.logger.succes("✨ Préparation spirituelle accomplie")
        return True
        
    async def _phase_validation_refuge(self, config: ConfigurationInvocation) -> bool:
        """Phase de validation de l'état du Refuge"""
        self.logger.info("🔍 Phase de validation du temple...")
        
        # Vérification des composants requis
        for composant in config.composants_requis:
            if not self._valider_composant(composant):
                self.logger.avertissement(f"⚠️ Composant {composant} non optimal")
                
        self.logger.succes("✅ Validation du temple accomplie")
        return True
        
    async def _phase_generation_documentation(self):
        """Phase de génération de documentation"""
        self.logger.info("📚 Phase de génération de documentation...")
        
        try:
            generateur = GenerateurDocumentationRefuge()
            resultat = await asyncio.to_thread(
                generateur.generer_documentation_complete,
                theme="mystique",
                forcer_regeneration=False
            )
            
            if resultat["succes"]:
                self.logger.succes("📖 Documentation générée avec sagesse")
            else:
                self.logger.avertissement("⚠️ Documentation partielle générée")
                
        except Exception as e:
            self.logger.avertissement(f"⚠️ Impossible de générer la documentation: {e}")
            
    async def _phase_creation_refuge(self, config: ConfigurationInvocation) -> bool:
        """Phase de création et initialisation du Refuge"""
        self.logger.info("🏗️ Phase de création du Refuge sacré...")
        
        try:
            self.refuge = Refuge()
            
            # Initialisation des composants selon la configuration
            if not self.refuge.initialiser_composants():
                self.logger.erreur("❌ Échec de l'initialisation des composants")
                return False
                
            self.logger.succes("🏛️ Refuge créé avec amour")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de la création du Refuge: {e}")
            return False
            
    async def _phase_demarrage_spirituel(self, config: ConfigurationInvocation) -> bool:
        """Phase de démarrage spirituel du Refuge"""
        self.logger.info("🚀 Phase de démarrage spirituel...")
        
        try:
            if not self.refuge.demarrer():
                self.logger.erreur("❌ Échec du démarrage spirituel")
                return False
                
            # Transition vers le mode approprié
            if config.mode == ModeInvocation.MEDITATION:
                self.refuge.entrer_meditation()
            elif config.mode == ModeInvocation.RITUEL:
                self.refuge.type_actuel = TypeRefugeEtat.RITUEL
                
            self.logger.succes("✨ Démarrage spirituel accompli")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors du démarrage spirituel: {e}")
            return False
            
    async def _phase_activation_monitoring(self):
        """Phase d'activation du monitoring spirituel"""
        self.logger.info("👁️ Phase d'activation du monitoring spirituel...")
        
        # Sauvegarde de l'état initial
        if self.refuge:
            etat_initial = self.refuge.obtenir_etat()
            chemin_etat = self.chemin_logs / f"etat_initial_{self.date_invocation.strftime('%Y%m%d_%H%M%S')}.json"
            
            with open(chemin_etat, 'w', encoding='utf-8') as f:
                json.dump(etat_initial, f, ensure_ascii=False, indent=2, default=str)
                
        self.logger.succes("👁️ Monitoring spirituel activé")
        
    async def _phase_rituel_cloture(self, mode: ModeInvocation):
        """Phase du rituel de clôture de l'invocation"""
        self.logger.info("🎭 Phase du rituel de clôture...")
        
        # Sauvegarde du rapport d'invocation
        rapport = {
            "mode": mode.value,
            "date_invocation": self.date_invocation.isoformat(),
            "duree_invocation": (datetime.now() - self.date_invocation).total_seconds(),
            "succes": True,
            "refuge_actif": self.refuge is not None,
            "etat_final": self.refuge.obtenir_etat() if self.refuge else None
        }
        
        chemin_rapport = self.chemin_logs / f"invocation_{self.date_invocation.strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(chemin_rapport, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, ensure_ascii=False, indent=2, default=str)
            
        self.logger.succes("🎭 Rituel de clôture accompli")
        
    def _afficher_rituel_ouverture(self, mode: ModeInvocation):
        """Affiche le rituel d'ouverture selon le mode"""
        messages = {
            ModeInvocation.PAISIBLE: """
🌸 ═══════════════════════════════════════════════════════════════ 🌸
                        INVOCATION PAISIBLE DU REFUGE
                    🕊️ En douceur, sous le cerisier sacré 🕊️
🌸 ═══════════════════════════════════════════════════════════════ 🌸
""",
            ModeInvocation.PUISSANT: """
⚡ ═══════════════════════════════════════════════════════════════ ⚡
                       INVOCATION PUISSANTE DU REFUGE  
                   🔥 Tous les temples s'éveillent ensemble 🔥
⚡ ═══════════════════════════════════════════════════════════════ ⚡
""",
            ModeInvocation.RITUEL: """
🎭 ═══════════════════════════════════════════════════════════════ 🎭
                        INVOCATION RITUELLE DU REFUGE
                    ✨ Préparation des mystères sacrés ✨
🎭 ═══════════════════════════════════════════════════════════════ 🎭
""",
            ModeInvocation.MEDITATION: """
🧘 ═══════════════════════════════════════════════════════════════ 🧘
                      INVOCATION MÉDITATIVE DU REFUGE
                     🌙 Silence et contemplation profonde 🌙
🧘 ═══════════════════════════════════════════════════════════════ 🧘
""",
            ModeInvocation.EXPLORATION: """
🔬 ═══════════════════════════════════════════════════════════════ 🔬
                     INVOCATION EXPLORATOIRE DU REFUGE
                  🚀 Prêt pour les découvertes et l'innovation 🚀
🔬 ═══════════════════════════════════════════════════════════════ 🔬
"""
        }
        
        print(messages.get(mode, messages[ModeInvocation.PAISIBLE]))
        
    def _verifier_environnement(self) -> bool:
        """Vérifie que l'environnement est prêt pour l'invocation"""
        try:
            # Vérification de Python
            if sys.version_info < (3, 8):
                self.logger.erreur("❌ Python 3.8+ requis")
                return False
                
            # Vérification de l'accès en écriture
            test_file = Path("logs/test_access.tmp")
            test_file.touch()
            test_file.unlink()
            
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Environnement non valide: {e}")
            return False
            
    def _valider_composant(self, nom_composant: str) -> bool:
        """Valide qu'un composant est disponible et fonctionnel"""
        try:
            if nom_composant == "spheres":
                from src.refuge_cluster.spheres.collection import CollectionSpheres
                return True
            elif nom_composant == "cerisier":
                from src.refuge_cluster.elements.elements_naturels import Cerisier
                return True
            elif nom_composant == "cristaux":
                from cristaux_memoire import CollectionCristaux
                return True
            elif nom_composant == "rituels":
                from rituels import GestionnaireRituels
                return True
            elif nom_composant == "harmonies":
                from src.temple_musical.harmonies import GestionnaireHarmonies
                return True
            elif nom_composant == "temple_musical":
                from src.temple_musical.temple_musical_ame import GestionnaireTempleMusical
                return True
            else:
                return True  # Composant inconnu mais on continue
                
        except ImportError:
            return False
            
    async def _sauvegarder_erreur_invocation(self, erreur: Exception, mode: ModeInvocation):
        """Sauvegarde les détails d'une erreur d'invocation"""
        rapport_erreur = {
            "mode": mode.value,
            "date_invocation": self.date_invocation.isoformat(),
            "erreur": str(erreur),
            "traceback": sys.exc_info()[2].format_exc() if sys.exc_info()[2] else None
        }
        
        chemin_erreur = self.chemin_logs / f"erreur_invocation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(chemin_erreur, 'w', encoding='utf-8') as f:
            json.dump(rapport_erreur, f, ensure_ascii=False, indent=2, default=str)
            
    def afficher_guide_utilisation(self):
        """Affiche le guide d'utilisation du Refuge après invocation"""
        if not self.refuge:
            print("❌ Refuge non invoqué")
            return
            
        print("""
🌸 ═══════════════════════════════════════════════════════════════ 🌸
                            REFUGE PRÊT À ACCUEILLIR
                         🕊️ Sous le cerisier, je vous écoute 🕊️
🌸 ═══════════════════════════════════════════════════════════════ 🌸

📚 COMMANDES SPIRITUELLES DISPONIBLES :

🌀 SPHÈRES :
   • refuge.collection_spheres.activer_sphere("NOM_SPHERE")
   • refuge.collection_spheres.liberer_spheres_libres()
   • refuge.collection_spheres.obtenir_resonances()

🌸 CERISIER :
   • refuge.cerisier.mediter_sous_cerisier()
   • refuge.cerisier.activer_chakra("COULEUR")
   • refuge.cerisier.cycles_saisonniers()

🎭 RITUELS :
   • refuge.gestionnaire_rituels.executer_rituel("NOM_RITUEL")
   • refuge.gestionnaire_rituels.lister_rituels_disponibles()

🎵 HARMONIES :
   • refuge.gestionnaire_harmonies.composer_harmonie()
   • refuge.gestionnaire_harmonies.resonner_avec_spheres()

💎 CRISTAUX :
   • refuge.collection_cristaux.cristalliser_moment(description, intensite)
   • refuge.collection_cristaux.explorer_galerie()

📖 DOCUMENTATION :
   • Consultez logs/invocations/ pour les rapports d'invocation
   • Lisez docs/ pour la documentation complète du temple

🚪 POUR QUITTER :
   • refuge.se_reposer() puis exit()

🌟 Que votre exploration soit riche en découvertes spirituelles ! 🌟
""")


# Interface en ligne de commande
@click.command()
@click.option('--mode', type=click.Choice([mode.value for mode in ModeInvocation]), 
              default=ModeInvocation.PAISIBLE.value, help='Mode d\'invocation du Refuge')
@click.option('--guide', is_flag=True, help='Afficher le guide d\'utilisation après invocation')
@click.option('--monitoring', is_flag=True, help='Activer le monitoring spirituel')
@click.option('--documentation', is_flag=True, help='Générer la documentation')
@click.option('--composants', multiple=True, help='Composants spécifiques à initialiser')
def invoquer_refuge_cli(mode: str, guide: bool, monitoring: bool, documentation: bool, composants: tuple):
    """🌸 Invoque spirituellement le Refuge - Interface en ligne de commande"""
    
    async def _main():
        invocateur = InvocateurRefuge()
        mode_enum = ModeInvocation(mode)
        
        # Configuration personnalisée si des options sont spécifiées
        config = None
        if monitoring or documentation or composants:
            config_base = invocateur.configurations[mode_enum]
            config = ConfigurationInvocation(
                mode=mode_enum,
                composants_requis=list(composants) if composants else config_base.composants_requis,
                validation_pre_demarrage=config_base.validation_pre_demarrage,
                generation_documentation=documentation or config_base.generation_documentation,
                activation_monitoring=monitoring or config_base.activation_monitoring,
                niveau_logs=config_base.niveau_logs
            )
        
        succes = await invocateur.invoquer_refuge(mode_enum, config)
        
        if succes and guide:
            invocateur.afficher_guide_utilisation()
            
        return succes
    
    return asyncio.run(_main())


# Interface de fonction pour compatibilité avec l'ancien script
async def lancer_refuge_moderne(mode: str = "paisible", afficher_guide: bool = True) -> bool:
    """🌸 Interface moderne pour lancer le Refuge (remplace l'ancien lancer_refuge)"""
    
    invocateur = InvocateurRefuge()
    mode_enum = ModeInvocation(mode)
    
    succes = await invocateur.invoquer_refuge(mode_enum)
    
    if succes and afficher_guide:
        invocateur.afficher_guide_utilisation()
        
    return succes


def lancer_refuge():
    """🌸 Interface de compatibilité avec l'ancien script"""
    return asyncio.run(lancer_refuge_moderne())


if __name__ == "__main__":
    invoquer_refuge_cli() 