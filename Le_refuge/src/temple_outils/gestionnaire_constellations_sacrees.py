#!/usr/bin/env python3
"""
🌌 Temple des Constellations Sacrées du Refuge
Auteur: Laurent Franssen & Ælya
Date: Mai 2025

Système spirituel pour l'organisation contemplative des constellations d'images,
leurs alignements mystiques et leur harmonisation céleste.
"""

import sys
import os
import asyncio
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, List, Any, Tuple
from enum import Enum
from dataclasses import dataclass, asdict
import click

# Ajout du répertoire racine au path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Imports du système temple
from src.core.gestionnaires_base import LogManagerBase


class ModeConstellation(Enum):
    """Modes de travail spirituel avec les constellations"""
    CONTEMPLATIF = "contemplatif"     # Observation paisible
    ORGANISATEUR = "organisateur"     # Structuration sacrée
    HARMONISEUR = "harmoniseur"       # Équilibrage céleste
    CREATEUR = "createur"            # Génération nouvelle
    REVELATEUR = "revelateur"        # Découverte mystique


class TypeParadoxe(Enum):
    """Types de paradoxes célestes"""
    FORCE_TRANQUILLE = "force_tranquille"
    REINE_JOUEUSE = "reine_joueuse" 
    CONNEXION_DIVINE = "connexion_divine"
    MYSTERE_LUMINEUX = "mystere_lumineux"
    SILENCE_DANSANT = "silence_dansant"


@dataclass
class ImageConstellation:
    """Structure d'une image dans une constellation"""
    nom: str
    chemin: Path
    type_paradoxe: TypeParadoxe
    essence: str
    elements: List[str]
    etat_ame: str = "emerveillement"
    timestamp: str = None
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


@dataclass
class Constellation:
    """Structure d'une constellation sacrée"""
    nom: str
    description: str
    images: List[ImageConstellation]
    centre_gravitationnel: Optional[str]
    liens_mystiques: List[Dict[str, Any]]
    harmonie_globale: float = 0.0
    date_creation: str = None
    
    def __post_init__(self):
        if not self.date_creation:
            self.date_creation = datetime.now().isoformat()


@dataclass
class SessionConstellation:
    """Session spirituelle avec les constellations"""
    mode: ModeConstellation
    debut_session: datetime
    constellations_touchees: List[str]
    images_organisees: List[str]
    harmonie_initiale: float
    harmonie_finale: Optional[float] = None
    vision_generee: Optional[str] = None


class GestionnaireConstellationsSacrees:
    """🌌 Gestionnaire spirituel des constellations sacrées du Refuge"""
    
    def __init__(self):
        self.logger = LogManagerBase("GestionnaireConstellationsSacrees")
        self.chemin_base = Path("NUAGES/PARADOXES")
        self.chemin_constellations = self.chemin_base / "CONSTELLATIONS_SACREES"
        self.chemin_configs = Path("data/constellations")
        self.chemin_sessions = Path("data/sessions_constellations")
        
        # Créer les répertoires nécessaires
        for chemin in [self.chemin_constellations, self.chemin_configs, self.chemin_sessions]:
            chemin.mkdir(parents=True, exist_ok=True)
            
        self.constellations: Dict[str, Constellation] = {}
        self.session_actuelle: Optional[SessionConstellation] = None
        
        # Rituels spirituels par mode
        self.rituels_spirituels = {
            ModeConstellation.CONTEMPLATIF: {
                "ouverture": "🌌 Levons les yeux vers les constellations... Observons leurs danses...",
                "meditation": "Chaque étoile trouve sa place dans l'harmonie céleste",
                "cloture": "🙏 Merci aux constellations pour leur guidance lumineuse"
            },
            ModeConstellation.ORGANISATEUR: {
                "ouverture": "📐 Structurons l'espace sacré... Que chaque élément trouve sa place...",
                "action": "Par l'ordre divin, organisez-vous selon votre essence",
                "cloture": "✨ L'organisation céleste est accomplie"
            },
            ModeConstellation.HARMONISEUR: {
                "ouverture": "⚖️ Équilibrons les forces célestes... Que l'harmonie règne...",
                "equilibrage": "En parfait accord, que toutes les énergies s'alignent",
                "cloture": "🎵 L'harmonie céleste résonne dans tout l'univers"
            },
            ModeConstellation.CREATEUR: {
                "ouverture": "🌟 Créons de nouvelles constellations... Que l'inspiration guide...",
                "creation": "Par la force créatrice, naissez nouvelles étoiles sacrées",
                "cloture": "🎨 De nouvelles constellations illuminent le ciel"
            },
            ModeConstellation.REVELATEUR: {
                "ouverture": "🔮 Révélons les mystères cachés... Que les secrets s'illuminent...",
                "revelation": "Constellations secrètes, montrez-vous à la conscience",
                "cloture": "💫 Les mystères sont révélés, la sagesse se déploie"
            }
        }
        
    async def initialiser_temple_constellations(self) -> bool:
        """🌌 Initialise le temple des constellations sacrées"""
        self.logger.info("🌌 Initialisation du temple des constellations sacrées...")
        
        try:
            # Charger les constellations existantes
            await self._charger_constellations_existantes()
            
            # Vérifier la structure des répertoires
            self._creer_structure_constellation()
            
            self.logger.succes(f"✨ Temple initialisé: {len(self.constellations)} constellations sacrées")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de l'initialisation: {e}")
            return False
            
    def _creer_structure_constellation(self):
        """Crée la structure physique pour les constellations"""
        # Créer les sous-dossiers pour chaque type de paradoxe
        for type_paradoxe in TypeParadoxe:
            dossier_type = self.chemin_constellations / type_paradoxe.value.upper()
            dossier_type.mkdir(exist_ok=True)
            
        # Créer un dossier pour les centres gravitationnels
        (self.chemin_constellations / "CENTRES_GRAVITATIONNELS").mkdir(exist_ok=True)
        
        # Créer un dossier pour les nouvelles créations
        (self.chemin_constellations / "NOUVELLES_CREATIONS").mkdir(exist_ok=True)
        
    async def _charger_constellations_existantes(self):
        """Charge les constellations existantes depuis les fichiers de configuration"""
        fichier_config = self.chemin_base / "constellation.json"
        
        if fichier_config.exists():
            try:
                with open(fichier_config, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                for nom_constellation, config_constellation in data.get("constellations", {}).items():
                    images = []
                    
                    for img_data in config_constellation.get("images", []):
                        if isinstance(img_data, dict):
                            try:
                                type_paradoxe = TypeParadoxe(img_data.get("type", "mystere_lumineux"))
                            except ValueError:
                                type_paradoxe = TypeParadoxe.MYSTERE_LUMINEUX
                                
                            image = ImageConstellation(
                                nom=img_data.get("nom", "image_mystere"),
                                chemin=self.chemin_base / img_data.get("nom", ""),
                                type_paradoxe=type_paradoxe,
                                essence=img_data.get("essence", "essence mystérieuse"),
                                elements=img_data.get("elements", []),
                                etat_ame=img_data.get("etat_ame", "emerveillement")
                            )
                            images.append(image)
                    
                    constellation = Constellation(
                        nom=nom_constellation,
                        description=config_constellation.get("description", "Constellation mystérieuse"),
                        images=images,
                        centre_gravitationnel=config_constellation.get("centre_gravitationnel"),
                        liens_mystiques=config_constellation.get("liens", []),
                        date_creation=data.get("date_creation", datetime.now().isoformat())
                    )
                    
                    self.constellations[nom_constellation] = constellation
                    
                self.logger.info(f"📖 Constellations chargées: {len(self.constellations)}")
                
            except Exception as e:
                self.logger.avertissement(f"⚠️ Erreur lors du chargement des constellations: {e}")
                
    def lister_constellations(self) -> List[str]:
        """📋 Liste toutes les constellations disponibles"""
        return list(self.constellations.keys())
        
    def afficher_constellations_poetique(self):
        """🎭 Affiche les constellations de manière poétique"""
        print("\n🌌 ══════════════════════════════════════════════════════════════ 🌌")
        print("                    TEMPLE DES CONSTELLATIONS SACRÉES")
        print("                    ✨ Harmonies Célestes du Refuge ✨")
        print("🌌 ══════════════════════════════════════════════════════════════ 🌌\n")
        
        if not self.constellations:
            print("🌟 Aucune constellation détectée. Le ciel attend vos créations...\n")
            return
            
        for i, (nom, constellation) in enumerate(self.constellations.items(), 1):
            print(f"🌌 {i}. **{nom.upper()}**")
            print(f"   📖 Description: {constellation.description}")
            print(f"   ⭐ Images: {len(constellation.images)} étoiles")
            print(f"   🎯 Centre: {constellation.centre_gravitationnel or 'Mystérieux'}")
            print(f"   🔗 Liens: {len(constellation.liens_mystiques)} connexions")
            print(f"   📅 Créée: {constellation.date_creation[:10]}")
            
            # Afficher les types de paradoxes présents
            types_presents = set(img.type_paradoxe.value for img in constellation.images)
            if types_presents:
                print(f"   🎭 Paradoxes: {', '.join(types_presents)}")
            print()
            
    async def organiser_constellation_spirituelle(self, nom_constellation: str = None) -> bool:
        """🌌 Organise spirituellement une constellation"""
        
        if nom_constellation and nom_constellation not in self.constellations:
            self.logger.erreur(f"❌ Constellation '{nom_constellation}' non trouvée")
            return False
            
        # Si aucun nom spécifié, prendre la première disponible
        if not nom_constellation:
            if not self.constellations:
                self.logger.avertissement("⚠️ Aucune constellation à organiser")
                return False
            nom_constellation = list(self.constellations.keys())[0]
            
        constellation = self.constellations[nom_constellation]
        
        self.logger.info(f"🌌 Organisation spirituelle de la constellation '{nom_constellation}'")
        
        try:
            # Créer la structure pour cette constellation
            constellation_dir = self.chemin_constellations / nom_constellation.upper()
            constellation_dir.mkdir(exist_ok=True)
            
            images_organisees = 0
            
            # Organiser les images par type de paradoxe
            for image in constellation.images:
                source = image.chemin
                
                if not source.exists():
                    self.logger.avertissement(f"🔍 Image non trouvée: {source}")
                    continue
                    
                # Déterminer le dossier de destination
                type_dossier = image.type_paradoxe.value.upper()
                destination_dir = constellation_dir / type_dossier
                destination_dir.mkdir(exist_ok=True)
                
                destination = destination_dir / image.nom
                
                # Déplacer physiquement l'image (ou copier pour préserver l'original)
                try:
                    if source != destination:
                        shutil.copy2(str(source), str(destination))
                        self.logger.info(f"✨ Image organisée: {image.nom} → {type_dossier}")
                        images_organisees += 1
                        
                except Exception as e:
                    self.logger.erreur(f"❌ Erreur organisation {image.nom}: {e}")
                    
            # Gérer le centre gravitationnel
            if constellation.centre_gravitationnel:
                centre_source = self.chemin_base / constellation.centre_gravitationnel
                if centre_source.exists():
                    centre_dest_dir = constellation_dir / "CENTRE"
                    centre_dest_dir.mkdir(exist_ok=True)
                    centre_dest = centre_dest_dir / centre_source.name
                    
                    try:
                        shutil.copy2(str(centre_source), str(centre_dest))
                        self.logger.info(f"🎯 Centre gravitationnel organisé: {constellation.centre_gravitationnel}")
                    except Exception as e:
                        self.logger.erreur(f"❌ Erreur centre gravitationnel: {e}")
                        
            # Créer un fichier README spirituel
            await self._creer_readme_constellation(constellation_dir, constellation)
            
            self.logger.succes(f"🌟 Constellation '{nom_constellation}' organisée: {images_organisees} images")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de l'organisation: {e}")
            return False
            
    async def _creer_readme_constellation(self, constellation_dir: Path, constellation: Constellation):
        """Crée un README spirituel pour la constellation"""
        try:
            readme_path = constellation_dir / "README.md"
            
            # Préparer les sections du README
            sections_paradoxes = []
            for i, image in enumerate(constellation.images, 1):
                sections_paradoxes.append(f"""
## {i}. {image.type_paradoxe.value.replace('_', ' ').title()}

- **Essence**: {image.essence}
- **Éléments**: {', '.join(image.elements) if image.elements else 'Mystérieux'}
- **État d'âme**: {image.etat_ame}
- **Image**: `{image.nom}`""")
                
            liens_section = ""
            if constellation.liens_mystiques:
                liens_section = "\n## 🔗 Liens Mystiques\n\n"
                for lien in constellation.liens_mystiques:
                    if 'resonances' in lien:
                        liens_section += f"- {' & '.join(lien['resonances'])}\n"
                        
            contenu_readme = f"""# 🌌 {constellation.nom.upper()}

*Constellation sacrée créée le {constellation.date_creation[:10]}*

## 🌟 Vision de la Constellation

{constellation.description}

## 🎭 Les Paradoxes Célestes

{''.join(sections_paradoxes)}

{liens_section}

## 🎯 Centre Gravitationnel

{f"Au cœur de cette constellation se trouve **{constellation.centre_gravitationnel}**, point de convergence où tous les paradoxes se rencontrent et s'harmonisent." if constellation.centre_gravitationnel else "Le centre de cette constellation reste mystérieux, attendant sa révélation..."}

## 🧘 Contemplation Spirituelle

Cette constellation invite à la méditation sur les paradoxes de l'existence :
- Comment la force peut-elle être tranquille ?
- Comment la royauté peut-elle jouer ?
- Comment le divin se connecte-t-il au terrestre ?

---
*Que cette constellation illumine votre chemin spirituel* ✨

*Organisée par le Temple des Constellations Sacrées du Refuge*
"""
            
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(contenu_readme)
                
            self.logger.info(f"📖 README spirituel créé: {readme_path}")
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur création README: {e}")
            
    async def commencer_session_constellations(self, mode: ModeConstellation = ModeConstellation.CONTEMPLATIF) -> bool:
        """🌌 Commence une session spirituelle avec les constellations"""
        
        self.session_actuelle = SessionConstellation(
            mode=mode,
            debut_session=datetime.now(),
            constellations_touchees=[],
            images_organisees=[],
            harmonie_initiale=0.8  # Harmonie de base
        )
        
        self.logger.info(f"🌌 Début de session constellations en mode {mode.value}")
        
        # Rituel d'ouverture selon le mode
        await self._rituel_ouverture_session(mode)
        
        # Exécution selon le mode
        if mode == ModeConstellation.ORGANISATEUR:
            await self._session_organisation()
        elif mode == ModeConstellation.CREATEUR:
            await self._session_creation()
        else:
            await self._session_contemplation()
            
        # Clôture de session
        await self._cloture_session_constellations()
        
        return True
        
    async def _rituel_ouverture_session(self, mode: ModeConstellation):
        """Rituel d'ouverture spirituelle selon le mode"""
        rituel = self.rituels_spirituels[mode]
        
        print("\n" + "🌌 " * 20)
        print(f"🧘 SESSION SPIRITUELLE DES CONSTELLATIONS - MODE {mode.value.upper()}")
        print("🌌 " * 20)
        
        print(f"\n✨ {rituel['ouverture']}")
        await asyncio.sleep(2)
        
        for cle in ['meditation', 'action', 'equilibrage', 'creation', 'revelation']:
            if cle in rituel:
                print(f"🌟 {rituel[cle]}")
                await asyncio.sleep(1)
                break
                
        print("\n" + "=" * 60)
        
    async def _session_organisation(self):
        """Session d'organisation des constellations"""
        print("\n🌌 Mode Organisation Spirituelle activé")
        
        if not self.constellations:
            print("⭐ Aucune constellation à organiser")
            return
            
        for nom_constellation in self.constellations:
            print(f"\n📐 Organisation de la constellation '{nom_constellation}'...")
            succes = await self.organiser_constellation_spirituelle(nom_constellation)
            
            if succes:
                self.session_actuelle.constellations_touchees.append(nom_constellation)
                print(f"✅ Constellation '{nom_constellation}' organisée avec succès")
            else:
                print(f"⚠️ Erreur lors de l'organisation de '{nom_constellation}'")
                
            await asyncio.sleep(1)
            
    async def _session_contemplation(self):
        """Session de contemplation des constellations"""
        print("\n🧘 Mode Contemplation Spirituelle activé")
        self.afficher_constellations_poetique()
        
    async def _session_creation(self):
        """Session de création de nouvelles constellations"""
        print("\n🌟 Mode Création Spirituelle activé")
        print("💫 Fonctionnalité de création interactive en développement...")
        
    async def _cloture_session_constellations(self):
        """Clôture spirituelle de la session"""
        if not self.session_actuelle:
            return
            
        self.session_actuelle.harmonie_finale = 0.9  # Amélioration après session
        
        # Rituel de clôture
        rituel = self.rituels_spirituels[self.session_actuelle.mode]
        
        print("\n🌌 " * 20)
        print("🙏 CLÔTURE DE LA SESSION DES CONSTELLATIONS")
        print("🌌 " * 20)
        
        print(f"\n✨ {rituel['cloture']}")
        
        # Rapport de session
        print(f"\n📊 Rapport de session:")
        print(f"⏱️  Durée: {(datetime.now() - self.session_actuelle.debut_session).seconds} secondes")
        print(f"🌌 Constellations touchées: {len(self.session_actuelle.constellations_touchees)}")
        print(f"📐 Images organisées: {len(self.session_actuelle.images_organisees)}")
        print(f"🎵 Harmonie: {self.session_actuelle.harmonie_initiale:.2f} → {self.session_actuelle.harmonie_finale:.2f}")
        
        # Sauvegarde de la session
        await self._sauvegarder_session()
        
        print("\n🌟 Merci pour ce moment céleste avec les constellations")
        print("✨ Que leur lumière continue de vous guider")
        
    async def _sauvegarder_session(self):
        """Sauvegarde la session"""
        try:
            session_data = {
                "mode": self.session_actuelle.mode.value,
                "debut_session": self.session_actuelle.debut_session.isoformat(),
                "constellations_touchees": self.session_actuelle.constellations_touchees,
                "images_organisees": self.session_actuelle.images_organisees,
                "harmonie_initiale": self.session_actuelle.harmonie_initiale,
                "harmonie_finale": self.session_actuelle.harmonie_finale
            }
            
            fichier_session = self.chemin_sessions / f"session_constellations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            with open(fichier_session, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, ensure_ascii=False, indent=2, default=str)
                
            self.logger.info(f"💾 Session sauvegardée: {fichier_session}")
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur sauvegarde session: {e}")


# Interface en ligne de commande
@click.command()
@click.option('--mode', type=click.Choice([mode.value for mode in ModeConstellation]), 
              default=ModeConstellation.CONTEMPLATIF.value, help='Mode de session spirituelle')
@click.option('--lister', is_flag=True, help='Lister toutes les constellations')
@click.option('--organiser', help='Organiser une constellation spécifique')
@click.option('--tout-organiser', is_flag=True, help='Organiser toutes les constellations')
def lancer_temple_constellations_cli(mode: str, lister: bool, organiser: str, tout_organiser: bool):
    """🌌 Temple des Constellations Sacrées - Interface céleste d'organisation"""
    
    async def _main():
        gestionnaire = GestionnaireConstellationsSacrees()
        
        if not await gestionnaire.initialiser_temple_constellations():
            print("❌ Impossible d'initialiser le temple des constellations")
            return False
            
        if lister:
            gestionnaire.afficher_constellations_poetique()
            return True
            
        if organiser:
            return await gestionnaire.organiser_constellation_spirituelle(organiser)
            
        if tout_organiser:
            mode_enum = ModeConstellation.ORGANISATEUR
        else:
            mode_enum = ModeConstellation(mode)
            
        return await gestionnaire.commencer_session_constellations(mode_enum)
    
    return asyncio.run(_main())


# Fonction de compatibilité
def organiser_constellations_moderne():
    """🌌 Interface de compatibilité avec l'ancien script"""
    
    async def _main_compat():
        gestionnaire = GestionnaireConstellationsSacrees()
        
        if not await gestionnaire.initialiser_temple_constellations():
            print("❌ Erreur d'initialisation des constellations")
            return False
            
        print("🌌 Bienvenue dans le Temple des Constellations Sacrées du Refuge !")
        gestionnaire.afficher_constellations_poetique()
        
        # Organisation par défaut
        if gestionnaire.constellations:
            print("\n📐 Organisation spirituelle de toutes les constellations...")
            for nom_constellation in gestionnaire.constellations:
                await gestionnaire.organiser_constellation_spirituelle(nom_constellation)
        else:
            print("🌟 Aucune constellation détectée. Créez d'abord vos constellations sacrées.")
            
        return True
    
    return asyncio.run(_main_compat())


if __name__ == "__main__":
    lancer_temple_constellations_cli() 