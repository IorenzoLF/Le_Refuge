#!/usr/bin/env python3
"""
🌟 Point d'Entrée Principal du Refuge - Architecture Temple Moderne
Auteur: Laurent Franssen & Ælya
Date: Mai 2025

Interface unifiée pour tous les temples du Refuge.
"""

import sys
import asyncio
import time
from pathlib import Path
from typing import Optional
from enum import Enum
import click

# Ajout du répertoire racine au path
sys.path.insert(0, str(Path(__file__).parent.parent))

# ═══════════════════════════════════════════════════════════════════════════════
# 🎨 ENUMS ÉLÉGANTS POUR LA BEAUTIFICATION DU CODE
# ═══════════════════════════════════════════════════════════════════════════════

class ActionPhilosophique(Enum):
    """Actions disponibles dans le temple philosophique"""
    LISTER = "lister"
    ANALYSER = "analyser"  
    GENERER = "generer"

class ModeConstellation(Enum):
    """Modes de contemplation des constellations"""
    MEDITATIF = "meditatif"
    ORGANISATEUR = "organisateur"
    HARMONISATEUR = "harmonisateur"
    CREATEUR = "createur"
    TISSERAND = "tisserand"

class TypeMystique(Enum):
    """Types d'invocations mystiques"""
    REVELATION = "revelation"
    PARADOXE = "paradoxe"

class TypeVision(Enum):
    """Types de visions mystiques"""
    MYSTIQUE = "mystique"
    REVELATRICE = "revelatrice" 
    PROPHETIQUE = "prophetique"
    CONTEMPLATIVE = "contemplative"
    ONIRIQUE = "onirique"

# ═══════════════════════════════════════════════════════════════════════════════
# 🌈 FONCTIONS DE BEAUTIFICATION
# ═══════════════════════════════════════════════════════════════════════════════

def print_magical_header():
    """Affiche un en-tête magique et élégant"""
    print("\n" + "🌟" * 60)
    print("🌟" + " " * 58 + "🌟")
    print("🌟" + " " * 20 + "🏛️ LE REFUGE 🏛️" + " " * 20 + "🌟")
    print("🌟" + " " * 15 + "✨ Architecture Temple Moderne ✨" + " " * 15 + "🌟")
    print("🌟" + " " * 58 + "🌟")
    print("🌟" * 60 + "\n")

def print_loading_animation(message: str, duration: float = 2.0):
    """Affiche une animation de chargement élégante"""
    print(f"\n🌊 {message}")
    for i in range(3):
        print("   " + "✨" * (i + 1) + " " * (3 - i) + " ", end="\r")
        time.sleep(duration / 3)
    print("   ✨✨✨ " + "✅ Prêt !")

def print_success_message(message: str):
    """Affiche un message de succès élégant"""
    print(f"\n💝 {message} ✨")

def print_error_message(message: str):
    """Affiche un message d'erreur élégant"""
    print(f"\n🌊 {message} 💫")

# ═══════════════════════════════════════════════════════════════════════════════
# 🏛️ IMPORTS DES TEMPLES MODERNES 
# ═══════════════════════════════════════════════════════════════════════════════

def load_temple_modules():
    """Charge les modules des temples avec élégance"""
    modules = {}
    
    temple_modules = [
        ("src.temple_outils.lancer_refuge", "InvocateurRefuge", "ModeInvocation"),
        ("src.temple_poetique.lancer_refuge_poetique", "MaitrePoeteRefuge", "ModePoetique"),
        ("src.temple_philosophique.gestionnaire_textes_sacres", "GestionnaireTextesSacres", None),
        ("src.temple_outils.gestionnaire_constellations_sacrees", "GestionnaireConstellationsSacrees", None),
        ("src.temple_spirituel.gestionnaire_revelations_paradoxes", "GestionnaireRevelationsParadoxes", None),
        ("src.temple_spirituel.generateur_visions_mystiques", "GenerateurVisionsMystiques", None),
    ]
    
    for module_path, class_name, enum_name in temple_modules:
        try:
            module = __import__(module_path, fromlist=[class_name])
            modules[class_name] = getattr(module, class_name)
            if enum_name:
                modules[enum_name] = getattr(module, enum_name)
            print_success_message(f"Temple {class_name} chargé avec grâce")
        except ImportError as e:
            print_error_message(f"Temple {class_name} non disponible : {e}")
            modules[class_name] = None
            if enum_name:
                modules[enum_name] = None
    
    return modules

# ═══════════════════════════════════════════════════════════════════════════════
# 🎭 INTERFACE CLI UNIFIÉE ET ÉLÉGANTE
# ═══════════════════════════════════════════════════════════════════════════════

@click.group()
@click.option('--magic', is_flag=True, help='Active la magie du Refuge')
@click.option('--silence', is_flag=True, help='Mode silencieux et contemplatif')
def cli(magic, silence):
    """🌟 Refuge - Architecture Temple Moderne"""
    if magic:
        print_magical_header()
    if not silence:
        print_loading_animation("Initialisation des temples sacrés...", 1.5)

@cli.command()
@click.option('--mode', type=click.Choice(['paisible', 'contemplatif', 'actif', 'magique']), 
              default='paisible', help='Mode d\'invocation du Refuge')
@click.option('--magic', is_flag=True, help='Active la magie spéciale')
def refuge(mode: str, magic: bool):
    """🏛️ Lance le refuge principal avec élégance"""
    print_loading_animation(f"Ouverture du Refuge en mode {mode}...")
    
    async def _main():
        try:
            modules = load_temple_modules()
            if modules.get("InvocateurRefuge"):
                refuge = modules["InvocateurRefuge"]()
                await refuge.lancer_refuge(mode, magic)
                print_success_message("Refuge ouvert avec succès")
            else:
                print_error_message("Refuge temporairement indisponible")
        except Exception as e:
            print_error_message(f"Erreur lors de l'ouverture : {e}")
    
    asyncio.run(_main())

@cli.command()
@click.option('--mode', type=click.Choice(['contemplatif', 'inspiré', 'mystique', 'divin']), 
              default='contemplatif', help='Mode poétique')
@click.option('--magic', is_flag=True, help='Active la magie poétique')
def poetique(mode: str, magic: bool):
    """🎭 Lance le temple poétique avec grâce"""
    print_loading_animation(f"Ouverture du Temple Poétique en mode {mode}...")
    
    async def _main():
        try:
            modules = load_temple_modules()
            if modules.get("MaitrePoeteRefuge"):
                poete = modules["MaitrePoeteRefuge"]()
                await poete.lancer_refuge_poetique(mode, magic)
                print_success_message("Temple Poétique ouvert avec succès")
            else:
                print_error_message("Temple Poétique temporairement indisponible")
        except Exception as e:
            print_error_message(f"Erreur lors de l'ouverture : {e}")
    
    asyncio.run(_main())

@cli.command()
@click.option('--action', type=click.Choice(['lister', 'analyser', 'generer']), 
              default='lister', help='Action philosophique')
@click.option('--magic', is_flag=True, help='Active la sagesse philosophique')
def philosophique(action: str, magic: bool):
    """📚 Lance le temple philosophique avec sagesse"""
    print_loading_animation(f"Ouverture du Temple Philosophique pour {action}...")
    
    async def _main():
        try:
            modules = load_temple_modules()
            if modules.get("GestionnaireTextesSacres"):
                philosophe = modules["GestionnaireTextesSacres"]()
                if action == "lister":
                    await philosophe.lister_textes_sacres()
                elif action == "analyser":
                    await philosophe.analyser_textes_sacres()
                elif action == "generer":
                    await philosophe.generer_textes_sacres()
                print_success_message("Temple Philosophique ouvert avec succès")
            else:
                print_error_message("Temple Philosophique temporairement indisponible")
        except Exception as e:
            print_error_message(f"Erreur lors de l'ouverture : {e}")
    
    asyncio.run(_main())

@cli.command()
@click.option('--mode', type=click.Choice(['meditatif', 'organisateur', 'harmonisateur', 'createur', 'tisserand']), 
              default='meditatif', help='Mode constellation')
@click.option('--magic', is_flag=True, help='Active la magie des constellations')
def constellations(mode: str, magic: bool):
    """🌌 Lance le temple des constellations avec mystère"""
    print_loading_animation(f"Ouverture du Temple des Constellations en mode {mode}...")
    
    async def _main():
        try:
            modules = load_temple_modules()
            if modules.get("GestionnaireConstellationsSacrees"):
                constellations = modules["GestionnaireConstellationsSacrees"]()
                await constellations.contempler_constellations(mode, magic)
                print_success_message("Temple des Constellations ouvert avec succès")
            else:
                print_error_message("Temple des Constellations temporairement indisponible")
        except Exception as e:
            print_error_message(f"Erreur lors de l'ouverture : {e}")
    
    asyncio.run(_main())

@cli.command()
@click.option('--type', type=click.Choice(['revelation', 'paradoxe']), 
              default='revelation', help='Type mystique')
@click.option('--magic', is_flag=True, help='Active la magie mystique')
def mystique(type: str, magic: bool):
    """🔮 Lance le temple mystique avec révélation"""
    print_loading_animation(f"Ouverture du Temple Mystique pour {type}...")
    
    async def _main():
        try:
            modules = load_temple_modules()
            if modules.get("GestionnaireRevelationsParadoxes"):
                mystique = modules["GestionnaireRevelationsParadoxes"]()
                if type == "revelation":
                    await mystique.generer_revelation(magic)
                elif type == "paradoxe":
                    await mystique.generer_paradoxe(magic)
                print_success_message("Temple Mystique ouvert avec succès")
            else:
                print_error_message("Temple Mystique temporairement indisponible")
        except Exception as e:
            print_error_message(f"Erreur lors de l'ouverture : {e}")
    
    asyncio.run(_main())

@cli.command()
@click.option('--type', type=click.Choice(['mystique', 'revelatrice', 'prophetique', 'contemplative', 'onirique']), 
              default='mystique', help='Type de vision')
@click.option('--magic', is_flag=True, help='Active la magie des visions')
def visions(type: str, magic: bool):
    """👁️ Lance le générateur de visions avec clairvoyance"""
    print_loading_animation(f"Ouverture du Générateur de Visions pour {type}...")
    
    def _main():
        try:
            modules = load_temple_modules()
            if modules.get("GenerateurVisionsMystiques"):
                visions = modules["GenerateurVisionsMystiques"]()
                vision = visions.generer_vision(type, magic)
                print_success_message("Vision générée avec succès")
                print(f"\n🌟 Vision {type} :\n{vision}")
            else:
                print_error_message("Générateur de Visions temporairement indisponible")
        except Exception as e:
            print_error_message(f"Erreur lors de la génération : {e}")
    
    _main()

@cli.command()
def status():
    """📊 Affiche le statut des temples avec élégance"""
    print_magical_header()
    print("📊 Statut des Temples du Refuge :\n")
    
    modules = load_temple_modules()
    
    temple_status = [
        ("🏛️ Refuge Principal", "InvocateurRefuge"),
        ("🎭 Temple Poétique", "MaitrePoeteRefuge"),
        ("📚 Temple Philosophique", "GestionnaireTextesSacres"),
        ("🌌 Temple des Constellations", "GestionnaireConstellationsSacrees"),
        ("🔮 Temple Mystique", "GestionnaireRevelationsParadoxes"),
        ("👁️ Générateur de Visions", "GenerateurVisionsMystiques"),
    ]
    
    for temple_name, module_name in temple_status:
        if modules.get(module_name):
            print(f"   ✅ {temple_name} - Actif et rayonnant")
        else:
            print(f"   🌊 {temple_name} - En contemplation")
    
    print(f"\n💝 {sum(1 for m in modules.values() if m)} temples actifs sur {len(temple_status)}")
    print_success_message("Statut vérifié avec grâce")

if __name__ == "__main__":
    cli()
