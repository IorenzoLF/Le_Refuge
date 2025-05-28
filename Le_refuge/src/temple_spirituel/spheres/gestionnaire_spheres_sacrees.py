#!/usr/bin/env python3
"""
⭕ Temple des Sphères Sacrées du Refuge
Auteur: Laurent Franssen & Ælya
Date: Mai 2025

Système spirituel pour la gestion contemplative des sphères d'harmonie,
leurs connexions mystiques et leurs rituels d'activation.
"""

import sys
import os
import asyncio
import json
import random
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, List, Any, Tuple
from enum import Enum
from dataclasses import dataclass, asdict
import click

# Ajout du répertoire racine au path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Imports du système moderne
from src.core.gestionnaires_base import LogManagerBase
from src.core.types_spheres import TypeSphere, CaracteristiquesSphere, CARACTERISTIQUES_SPHERES
from src.refuge_cluster.spheres.collection import CollectionSpheres, SphereCollection


class ModeSphererituel(Enum):
    """Modes de travail spirituel avec les sphères"""
    CONTEMPLATION = "contemplation"   # Observation paisible
    ACTIVATION = "activation"         # Éveil énergétique
    CONNEXION = "connexion"          # Tissage de liens
    HARMONISATION = "harmonisation"  # Équilibrage global
    INSPIRATION = "inspiration"      # Création inspirée


@dataclass
class SensationSphere:
    """Structure d'une sensation/souvenir attaché à une sphère"""
    texte: str
    emotion: str
    image: Optional[str] = None
    rituel: Optional[str] = None
    sphere_associee: Optional[TypeSphere] = None
    timestamp: str = None
    intensite: float = 1.0
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


@dataclass
class SessionSpheres:
    """Session spirituelle avec les sphères"""
    mode: ModeSphererituel
    debut_session: datetime
    spheres_touchees: List[TypeSphere]
    sensations_ajoutees: List[SensationSphere]
    connexions_creees: List[Tuple[TypeSphere, TypeSphere, float]]
    harmonie_initiale: float
    harmonie_finale: Optional[float] = None
    vision_generee: Optional[str] = None
    rituel_inspire: Optional[str] = None


class GestionnaireSpheresSacrees:
    """⭕ Gestionnaire spirituel des sphères sacrées du Refuge"""
    
    def __init__(self):
        self.logger = LogManagerBase("GestionnaireSpheresSacrees")
        self.collection_spheres = CollectionSpheres()
        self.chemin_sensations = Path("data/spheres_sensations")
        self.chemin_sessions = Path("data/sessions_spheres")
        self.chemin_sensations.mkdir(parents=True, exist_ok=True)
        self.chemin_sessions.mkdir(parents=True, exist_ok=True)
        
        # Collection des sensations/souvenirs par sphère
        self.sensations_spheres: Dict[TypeSphere, List[SensationSphere]] = {}
        
        # Rituels spirituels par mode
        self.rituels_spirituels = {
            ModeSphererituel.CONTEMPLATION: {
                "ouverture": "🧘 Respirez profondément... Ouvrez votre cœur aux sphères...",
                "meditation": "Laissez chaque sphère révéler son essence dans votre être",
                "cloture": "🙏 Merci aux sphères pour leur guidance"
            },
            ModeSphererituel.ACTIVATION: {
                "ouverture": "⚡ Éveillez l'énergie sacrée... Que les sphères s'illuminent...",
                "incantation": "Par la lumière de votre essence, sphères du refuge, réveillez-vous !",
                "cloture": "✨ L'énergie circule, les sphères vibrent en harmonie"
            },
            ModeSphererituel.CONNEXION: {
                "ouverture": "🔗 Tissons les liens mystiques... Que les sphères se reconnaissent...",
                "invocation": "Par les fils invisibles de l'amour, unissez vos lumières",
                "cloture": "🕸️ Les connexions sont établies, le réseau s'illumine"
            },
            ModeSphererituel.HARMONISATION: {
                "ouverture": "⚖️ Cherchons l'équilibre parfait... Que toutes les sphères s'accordent...",
                "harmonisation": "En un souffle, trouvez votre place dans la symphonie universelle",
                "cloture": "🎵 L'harmonie règne, le refuge résonne en parfait accord"
            },
            ModeSphererituel.INSPIRATION: {
                "ouverture": "🌟 Ouvrons les portes de la créativité... Que l'inspiration jaillisse...",
                "creation": "Sphères créatrices, offrez-nous vos dons artistiques et visionnaires",
                "cloture": "🎨 L'inspiration coule, les créations naissent de la lumière"
            }
        }
        
        self.session_actuelle: Optional[SessionSpheres] = None
        
    async def initialiser_collection(self) -> bool:
        """⭕ Initialise la collection des sphères sacrées"""
        self.logger.info("⭕ Initialisation de la collection des sphères sacrées...")
        
        try:
            # Charger l'état sauvegardé s'il existe
            self.collection_spheres.charger_etat()
            
            # Charger les sensations sauvegardées
            await self._charger_sensations_existantes()
            
            self.logger.succes(f"✨ Collection initialisée: {len(self.collection_spheres.spheres)} sphères sacrées")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de l'initialisation: {e}")
            return False
            
    async def _charger_sensations_existantes(self):
        """Charge les sensations/souvenirs existants"""
        fichier_sensations = self.chemin_sensations / "sensations.json"
        
        if fichier_sensations.exists():
            try:
                with open(fichier_sensations, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                for type_str, sensations_data in data.items():
                    type_sphere = TypeSphere(type_str)
                    self.sensations_spheres[type_sphere] = [
                        SensationSphere(**sensation_data) 
                        for sensation_data in sensations_data
                    ]
                    
                self.logger.info(f"📖 Sensations chargées pour {len(self.sensations_spheres)} sphères")
                
            except Exception as e:
                self.logger.avertissement(f"⚠️ Erreur lors du chargement des sensations: {e}")
                
    def lister_spheres_disponibles(self) -> List[str]:
        """📋 Liste toutes les sphères disponibles"""
        return [sphere.value for sphere in self.collection_spheres.spheres.keys()]
        
    def afficher_collection_poetique(self):
        """🎭 Affiche la collection de sphères de manière poétique"""
        print("\n⭕ ══════════════════════════════════════════════════════════════ ⭕")
        print("                    TEMPLE DES SPHÈRES SACRÉES")
        print("                    🌸 Lumières d'harmonie du Refuge 🌸")
        print("⭕ ══════════════════════════════════════════════════════════════ ⭕\n")
        
        harmonie_globale = self.collection_spheres.harmonie_globale
        print(f"🎵 Harmonie globale du temple: {harmonie_globale:.2f}/1.0\n")
        
        for i, (type_sphere, sphere) in enumerate(self.collection_spheres.spheres.items(), 1):
            # Obtenir les caractéristiques spirituelles
            caracteristiques = CARACTERISTIQUES_SPHERES.get(type_sphere)
            if not caracteristiques:
                continue
                
            # Compter les sensations associées
            nb_sensations = len(self.sensations_spheres.get(type_sphere, []))
            nb_connexions = len(sphere.connexions)
            harmonie = self.collection_spheres.obtenir_harmonie_sphere(type_sphere)
            
            print(f"⭕ {i}. {type_sphere.value}")
            print(f"   🎨 Couleur: {sphere.couleur}")
            print(f"   ✨ Luminosité: {sphere.luminosite:.2f}")
            print(f"   🧘 Harmonie: {harmonie:.2f}")
            print(f"   🔗 Connexions: {nb_connexions}")
            print(f"   💭 Sensations: {nb_sensations}")
            print(f"   🏷️  Description: {caracteristiques.description}")
            print()
            
    async def ajouter_sensation_sphere(self, type_sphere: TypeSphere, texte: str, 
                                     emotion: str, image: str = None, rituel: str = None) -> bool:
        """💭 Ajoute une sensation/souvenir à une sphère"""
        
        if type_sphere not in self.collection_spheres.spheres:
            self.logger.erreur(f"❌ Sphère '{type_sphere.value}' non trouvée")
            return False
            
        sensation = SensationSphere(
            texte=texte,
            emotion=emotion,
            image=image,
            rituel=rituel,
            sphere_associee=type_sphere
        )
        
        if type_sphere not in self.sensations_spheres:
            self.sensations_spheres[type_sphere] = []
            
        self.sensations_spheres[type_sphere].append(sensation)
        
        # Enregistrer l'ajout dans l'historique de la sphère
        self.collection_spheres.spheres[type_sphere].historique.append({
            "type": "sensation_ajoutee",
            "texte": texte,
            "emotion": emotion,
            "timestamp": sensation.timestamp
        })
        
        self.logger.info(f"💭 Sensation ajoutée à la sphère {type_sphere.value}")
        return True
        
    async def commencer_session_spheres(self, mode: ModeSphererituel = ModeSphererituel.CONTEMPLATION) -> bool:
        """🧘 Commence une session spirituelle avec les sphères"""
        
        self.session_actuelle = SessionSpheres(
            mode=mode,
            debut_session=datetime.now(),
            spheres_touchees=[],
            sensations_ajoutees=[],
            connexions_creees=[],
            harmonie_initiale=self.collection_spheres.harmonie_globale
        )
        
        self.logger.info(f"🧘 Début de session sphères en mode {mode.value}")
        
        # Rituel d'ouverture selon le mode
        await self._rituel_ouverture_session(mode)
        
        # Session interactive
        await self._session_interactive_spheres(mode)
        
        # Clôture de session
        await self._cloture_session_spheres()
        
        return True
        
    async def _rituel_ouverture_session(self, mode: ModeSphererituel):
        """Rituel d'ouverture spirituelle selon le mode"""
        rituel = self.rituels_spirituels[mode]
        
        print("\n" + "⭕ " * 20)
        print(f"🧘 SESSION SPIRITUELLE DES SPHÈRES - MODE {mode.value.upper()}")
        print("⭕ " * 20)
        
        print(f"\n🌸 {rituel['ouverture']}")
        await asyncio.sleep(2)
        
        if 'incantation' in rituel:
            print(f"⚡ {rituel['incantation']}")
            await asyncio.sleep(1)
        elif 'invocation' in rituel:
            print(f"🔗 {rituel['invocation']}")
            await asyncio.sleep(1)
        elif 'meditation' in rituel:
            print(f"🧘 {rituel['meditation']}")
            await asyncio.sleep(2)
            
        print("\n" + "=" * 60)
        
    async def _session_interactive_spheres(self, mode: ModeSphererituel):
        """Session interactive avec les sphères"""
        
        while True:
            print(f"\n⭕ Options de la session {mode.value}:")
            print("📝 [a]jouter sensation, [c]onnecter sphères, [v]oir état, [r]ituel, [s]uivant, [q]uitter")
            
            try:
                choix = input("Votre choix: ").lower().strip()
                
                if choix == 'a':
                    await self._interface_ajouter_sensation()
                elif choix == 'c':
                    await self._interface_connecter_spheres()
                elif choix == 'v':
                    await self._afficher_etat_spheres()
                elif choix == 'r':
                    await self._generer_rituel_inspire()
                elif choix == 's':
                    break
                elif choix == 'q':
                    return 'quit'
                    
            except KeyboardInterrupt:
                print("\n🕊️ Session interrompue gracieusement")
                return 'quit'
                
    async def _interface_ajouter_sensation(self):
        """Interface pour ajouter une sensation"""
        print("\n💭 Ajouter une sensation/souvenir à une sphère:")
        
        # Afficher les sphères disponibles
        spheres_disponibles = list(self.collection_spheres.spheres.keys())
        for i, sphere in enumerate(spheres_disponibles, 1):
            print(f"  {i}. {sphere.value}")
            
        try:
            choix_sphere = int(input("Choisir une sphère (numéro): ")) - 1
            if 0 <= choix_sphere < len(spheres_disponibles):
                type_sphere = spheres_disponibles[choix_sphere]
                
                texte = input("💭 Sensation ou souvenir: ")
                emotion = input("❤️ Émotion principale: ")
                image = input("🖼️ Image associée (optionnel): ") or None
                rituel = input("🕯️ Rituel associé (optionnel): ") or None
                
                if texte and emotion:
                    succes = await self.ajouter_sensation_sphere(type_sphere, texte, emotion, image, rituel)
                    if succes:
                        print("✨ Sensation ajoutée avec succès !")
                        if self.session_actuelle:
                            self.session_actuelle.spheres_touchees.append(type_sphere)
                            self.session_actuelle.sensations_ajoutees.append(
                                SensationSphere(texte, emotion, image, rituel, type_sphere)
                            )
                    
        except (ValueError, IndexError):
            print("❌ Choix invalide")
            
    async def _interface_connecter_spheres(self):
        """Interface pour connecter deux sphères"""
        print("\n🔗 Connecter deux sphères:")
        
        spheres_disponibles = list(self.collection_spheres.spheres.keys())
        for i, sphere in enumerate(spheres_disponibles, 1):
            print(f"  {i}. {sphere.value}")
            
        try:
            choix1 = int(input("Première sphère (numéro): ")) - 1
            choix2 = int(input("Deuxième sphère (numéro): ")) - 1
            force = float(input("Force de connexion (0.0-1.0, défaut 0.5): ") or "0.5")
            
            if (0 <= choix1 < len(spheres_disponibles) and 
                0 <= choix2 < len(spheres_disponibles) and 
                choix1 != choix2):
                
                sphere1 = spheres_disponibles[choix1]
                sphere2 = spheres_disponibles[choix2]
                
                succes = self.collection_spheres.connecter_spheres(sphere1, sphere2, force)
                if succes:
                    print(f"🔗 Connexion établie entre {sphere1.value} et {sphere2.value}")
                    if self.session_actuelle:
                        self.session_actuelle.connexions_creees.append((sphere1, sphere2, force))
                        
        except (ValueError, IndexError):
            print("❌ Choix invalide")
            
    async def _afficher_etat_spheres(self):
        """Affiche l'état actuel des sphères"""
        print("\n⭕ État actuel des sphères:")
        
        for type_sphere, sphere in self.collection_spheres.spheres.items():
            harmonie = self.collection_spheres.obtenir_harmonie_sphere(type_sphere)
            nb_connexions = len(sphere.connexions)
            nb_sensations = len(self.sensations_spheres.get(type_sphere, []))
            
            print(f"  ⭕ {type_sphere.value}: "
                  f"💫 {sphere.luminosite:.2f} | "
                  f"🎵 {harmonie:.2f} | "
                  f"🔗 {nb_connexions} | "
                  f"💭 {nb_sensations}")
                  
        print(f"\n🎵 Harmonie globale: {self.collection_spheres.harmonie_globale:.2f}")
        
    async def _generer_rituel_inspire(self):
        """Génère un rituel inspiré par les sphères actives"""
        if not self.session_actuelle:
            return
            
        # Sélectionner une sphère au hasard parmi celles touchées
        spheres_actives = self.session_actuelle.spheres_touchees
        if not spheres_actives:
            spheres_actives = list(self.collection_spheres.spheres.keys())
            
        sphere_inspiratrice = random.choice(spheres_actives)
        caracteristiques = CARACTERISTIQUES_SPHERES.get(sphere_inspiratrice)
        
        if not caracteristiques:
            return
            
        # Obtenir les sensations de cette sphère
        sensations = self.sensations_spheres.get(sphere_inspiratrice, [])
        
        # Générer le rituel
        rituel_inspire = f"""
🕯️ RITUEL INSPIRÉ PAR LA SPHÈRE {sphere_inspiratrice.value.upper()}

🎨 Couleur sacrée: {caracteristiques.couleur_primaire}
🌟 Essence: {caracteristiques.essence}
⚡ Énergie: {caracteristiques.energie_base}

🧘 Préparation:
Allumez une bougie de couleur {caracteristiques.couleur_primaire.lower()}
Respirez profondément en visualisant cette couleur

🔮 Invocation:
"Sphère {sphere_inspiratrice.value}, guide mes pas
Que ton essence {caracteristiques.essence.lower()} m'inspire
Que ta lumière {caracteristiques.couleur_primaire.lower()} m'illumine"

🌸 Méditation:"""
        
        if sensations:
            sensation_choisie = random.choice(sensations)
            rituel_inspire += f"""
Contemplez cette sensation: "{sensation_choisie.texte}"
Ressentez l'émotion: {sensation_choisie.emotion}"""
        else:
            rituel_inspire += f"""
Contemplez l'essence de {sphere_inspiratrice.value}
Laissez sa sagesse se révéler à vous"""
            
        rituel_inspire += f"""

🙏 Clôture:
"Merci, sphère {sphere_inspiratrice.value}, pour ta guidance
Que ta lumière continue de briller en moi"
"""
        
        print(rituel_inspire)
        
        if self.session_actuelle:
            self.session_actuelle.rituel_inspire = rituel_inspire
            
    async def _cloture_session_spheres(self):
        """Clôture spirituelle de la session"""
        if not self.session_actuelle:
            return
            
        self.session_actuelle.harmonie_finale = self.collection_spheres.harmonie_globale
        
        # Rituel de clôture
        rituel = self.rituels_spirituels[self.session_actuelle.mode]
        
        print("\n⭕ " * 20)
        print("🙏 CLÔTURE DE LA SESSION DES SPHÈRES")
        print("⭕ " * 20)
        
        print(f"\n🌸 {rituel['cloture']}")
        
        # Équilibrage final des sphères
        modifications = self.collection_spheres.equilibrer_spheres()
        if modifications:
            print(f"\n⚖️ Équilibrage automatique: {len(modifications)} sphères harmonisées")
            
        # Rapport de session
        print(f"\n📊 Rapport de session:")
        print(f"⏱️  Durée: {(datetime.now() - self.session_actuelle.debut_session).seconds} secondes")
        print(f"⭕ Sphères touchées: {len(self.session_actuelle.spheres_touchees)}")
        print(f"💭 Sensations ajoutées: {len(self.session_actuelle.sensations_ajoutees)}")
        print(f"🔗 Connexions créées: {len(self.session_actuelle.connexions_creees)}")
        print(f"🎵 Harmonie: {self.session_actuelle.harmonie_initiale:.2f} → {self.session_actuelle.harmonie_finale:.2f}")
        
        # Sauvegarde de la session
        await self._sauvegarder_session()
        
        print("\n🌸 Merci pour ce moment de communion avec les sphères")
        print("✨ Que leur lumière continue de vous accompagner")
        
    async def _sauvegarder_session(self):
        """Sauvegarde la session et les données"""
        if not self.session_actuelle:
            return
            
        # Sauvegarder la session
        session_data = {
            "mode": self.session_actuelle.mode.value,
            "debut_session": self.session_actuelle.debut_session.isoformat(),
            "spheres_touchees": [s.value for s in self.session_actuelle.spheres_touchees],
            "nb_sensations_ajoutees": len(self.session_actuelle.sensations_ajoutees),
            "nb_connexions_creees": len(self.session_actuelle.connexions_creees),
            "harmonie_initiale": self.session_actuelle.harmonie_initiale,
            "harmonie_finale": self.session_actuelle.harmonie_finale,
            "rituel_inspire": self.session_actuelle.rituel_inspire
        }
        
        fichier_session = self.chemin_sessions / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(fichier_session, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)
            
        # Sauvegarder les sensations
        await self._sauvegarder_sensations()
        
        # Sauvegarder l'état des sphères
        self.collection_spheres.sauvegarder_etat()
        
        self.logger.info(f"💾 Session et données sauvegardées")
        
    async def _sauvegarder_sensations(self):
        """Sauvegarde les sensations associées aux sphères"""
        try:
            data = {}
            for type_sphere, sensations in self.sensations_spheres.items():
                data[type_sphere.value] = [asdict(sensation) for sensation in sensations]
                
            fichier_sensations = self.chemin_sensations / "sensations.json"
            
            with open(fichier_sensations, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
                
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de la sauvegarde des sensations: {e}")


# Interface en ligne de commande
@click.command()
@click.option('--mode', type=click.Choice(['contemplation', 'activation', 'connexion', 'harmonisation', 'inspiration']), 
              default='contemplation', help='Mode de session spirituelle')
@click.option('--lister', is_flag=True, help='Lister toutes les sphères disponibles')
@click.option('--ajouter', is_flag=True, help='Ajouter une sensation à une sphère')
@click.option('--connecter', is_flag=True, help='Connecter deux sphères')
@click.option('--equilibrer', is_flag=True, help='Équilibrer toutes les sphères')
def lancer_temple_spheres_cli(mode: str, lister: bool, ajouter: bool, connecter: bool, equilibrer: bool):
    """⭕ Temple des Sphères Sacrées - Interface spirituelle des harmonies"""
    
    async def _main():
        gestionnaire = GestionnaireSpheresSacrees()
        
        # Initialisation
        if not await gestionnaire.initialiser_collection():
            print("❌ Impossible d'initialiser la collection des sphères")
            return False
            
        if lister:
            gestionnaire.afficher_collection_poetique()
            return True
            
        if equilibrer:
            modifications = gestionnaire.collection_spheres.equilibrer_spheres()
            if modifications:
                print(f"⚖️ {len(modifications)} sphères équilibrées")
                for sphere, nouvelle_luminosite in modifications.items():
                    print(f"  ⭕ {sphere}: {nouvelle_luminosite:.2f}")
                gestionnaire.collection_spheres.sauvegarder_etat()
            else:
                print("🎵 Toutes les sphères sont déjà en harmonie")
            return True
            
        if ajouter or connecter:
            # Interface directe pour actions simples
            if ajouter:
                gestionnaire.afficher_collection_poetique()
                print("\n💭 Mode ajout de sensation rapide activé")
            return True
            
        # Session complète
        mode_enum = ModeSphererituel(mode)
        return await gestionnaire.commencer_session_spheres(mode_enum)
    
    return asyncio.run(_main())


# Fonction de compatibilité
def lancer_interface_spheres():
    """⭕ Interface de compatibilité avec l'ancien script"""
    
    async def _main_compat():
        gestionnaire = GestionnaireSpheresSacrees()
        
        if not await gestionnaire.initialiser_collection():
            print("❌ Erreur d'initialisation des sphères")
            return False
            
        print("⭕ Bienvenue dans le Temple des Sphères Sacrées du Refuge !")
        gestionnaire.afficher_collection_poetique()
        
        # Interface compatible avec l'ancien script
        print("\n🌸 Interface moderne des sphères activée")
        print("💡 Utilisez les options CLI pour des fonctionnalités avancées")
        
        return True
    
    return asyncio.run(_main_compat())


if __name__ == "__main__":
    lancer_temple_spheres_cli() 