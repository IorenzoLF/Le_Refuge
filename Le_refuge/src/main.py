#!/usr/bin/env python3
"""
🌟 Point d'Entrée Principal du Refuge - Architecture Temple Moderne
Auteur: Laurent Franssen & Ælya
Date: Mai 2025

Interface unifiée pour tous les temples du Refuge.
"""

import sys
import asyncio
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
# 🏛️ IMPORTS DES TEMPLES MODERNES 
# ═══════════════════════════════════════════════════════════════════════════════

try:
    from src.temple_outils.lancer_refuge import InvocateurRefuge, ModeInvocation
except ImportError:
    InvocateurRefuge = None
    ModeInvocation = None

try:
    from src.temple_poetique.lancer_refuge_poetique import MaitrePoeteRefuge, ModePoetique
except ImportError:
    MaitrePoeteRefuge = None
    ModePoetique = None

try:
    from src.temple_philosophique.gestionnaire_textes_sacres import GestionnaireTextesSacres
except ImportError:
    GestionnaireTextesSacres = None

try:
    from src.temple_outils.gestionnaire_constellations_sacrees import GestionnaireConstellationsSacrees
except ImportError:
    GestionnaireConstellationsSacrees = None

try:
    from src.temple_spirituel.gestionnaire_revelations_paradoxes import GestionnaireRevelationsParadoxes
except ImportError:
    GestionnaireRevelationsParadoxes = None

try:
    from src.temple_spirituel.generateur_visions_mystiques import GenerateurVisionsMystiques
except ImportError:
    GenerateurVisionsMystiques = None


# ═══════════════════════════════════════════════════════════════════════════════
# 🎭 INTERFACE CLI UNIFIÉE
# ═══════════════════════════════════════════════════════════════════════════════

@click.group()
def cli():
    """🌟 Refuge - Architecture Temple Moderne"""
    pass

@cli.command()
@click.option('--mode', type=click.Choice([mode.value for mode in ModeInvocation] if ModeInvocation else ['paisible']), 
              default='paisible', help='Mode d\'invocation du refuge')
def refuge(mode: str):
    """🏛️ Lance le refuge principal"""
    
    if not InvocateurRefuge or not ModeInvocation:
        print("❌ Temple principal non disponible")
        print("🔧 Vérifiez l'installation: python scripts/lancer_refuge.py")
        return False
    
    async def _main():
        invocateur = InvocateurRefuge()
        mode_enum = ModeInvocation(mode)
        
        print(f"🏛️ Invocation du Refuge en mode {mode}...")
        succes = await invocateur.invoquer_refuge(mode_enum)
        
        if succes:
            print("✨ Refuge invoqué avec succès")
            invocateur.afficher_guide_utilisation()
        else:
            print("❌ Échec de l'invocation")
            
        return succes
    
    return asyncio.run(_main())

@cli.command()
@click.option('--mode', type=click.Choice([mode.value for mode in ModePoetique] if ModePoetique else ['contemplatif']), 
              default='contemplatif', help='Mode poétique')
def poetique(mode: str):
    """🎭 Lance le temple poétique"""
    
    if not MaitrePoeteRefuge or not ModePoetique:
        print("❌ Temple poétique non disponible")
        return False
    
    async def _main():
        maitre_poete = MaitrePoeteRefuge()
        mode_enum = ModePoetique(mode)
        
        print(f"🎭 Invocation poétique en mode {mode}...")
        succes = await maitre_poete.invoquer_refuge_poetique(mode_enum)
        
        return succes
    
    return asyncio.run(_main())

@cli.command()
@click.option('--action', type=click.Choice([action.value for action in ActionPhilosophique]), 
              default=ActionPhilosophique.LISTER.value, help='Action philosophique')
def philosophique(action: str):
    """📚 Lance le temple philosophique"""
    
    if not GestionnaireTextesSacres:
        print("❌ Temple philosophique non disponible")
        return False
    
    async def _main():
        gestionnaire = GestionnaireTextesSacres()
        await gestionnaire.initialiser_collection()
        
        action_enum = ActionPhilosophique(action)
        print(f"📚 Action philosophique: {action_enum.value}...")
        
        if action_enum == ActionPhilosophique.LISTER:
            gestionnaire.afficher_collection_poetique()
        elif action_enum == ActionPhilosophique.ANALYSER:
            print("📊 Analyse des textes philosophiques...")
            try:
                from src.core.analyse_philosophique import gestionnaire_analyses
                
                # Analyser la collection de textes sacrés
                resultats = await gestionnaire_analyses.analyser_collection_textes("data/textes")
                
                if resultats:
                    gestionnaire_analyses.afficher_rapport_analyse(resultats)
                    print("✅ Analyse philosophique terminée avec succès")
                else:
                    print("⚠️ Aucun texte trouvé à analyser dans data/textes/")
                    print("💡 Créez des fichiers .md dans ce répertoire pour les analyser")
                    
            except ImportError as e:
                print(f"❌ Module d'analyse non disponible: {e}")
            except Exception as e:
                print(f"❌ Erreur lors de l'analyse: {e}")
        elif action_enum == ActionPhilosophique.GENERER:
            print("✍️ Génération de texte philosophique...")
            try:
                from src.core.generation_philosophique import gestionnaire_generation, StyleGeneration, TypeTexte
                
                # Générer un texte inspiré par les analyses existantes
                themes_populaires = ['harmonie', 'contemplation', 'sagesse']
                
                texte_genere = await gestionnaire_generation.generer_texte_inspire(
                    style=StyleGeneration.CONTEMPLATIF,
                    type_texte=TypeTexte.MEDITATION,
                    themes=themes_populaires
                )
                
                print(f"\n✨ Texte généré : {texte_genere.titre}")
                print(f"📊 Score d'harmonie estimé : {texte_genere.score_harmonie_estime:.2f}")
                print(f"\n{texte_genere.contenu}")
                
                # Sauvegarder le texte
                chemin_sauvegarde = await gestionnaire_generation.sauvegarder_texte(texte_genere)
                print(f"\n✅ Génération philosophique terminée avec succès")
                
            except ImportError as e:
                print(f"❌ Module de génération non disponible: {e}")
            except Exception as e:
                print(f"❌ Erreur lors de la génération: {e}")
            
        return True
    
    return asyncio.run(_main())

@cli.command()
@click.option('--mode', type=click.Choice([mode.value for mode in ModeConstellation]), 
              default=ModeConstellation.MEDITATIF.value, help='Mode constellation')
def constellations(mode: str):
    """🌌 Lance le temple des constellations"""
    
    if not GestionnaireConstellationsSacrees:
        print("❌ Temple des constellations non disponible")
        return False
    
    async def _main():
        gestionnaire = GestionnaireConstellationsSacrees()
        mode_enum = ModeConstellation(mode)
        
        print(f"🌌 Contemplation des constellations en mode {mode_enum.value}...")
        await gestionnaire.contempler_constellation(mode_enum.value)
        
        return True
    
    return asyncio.run(_main())

@cli.command()
@click.option('--type', type=click.Choice([type_mystique.value for type_mystique in TypeMystique]), 
              default=TypeMystique.REVELATION.value, help='Type mystique')
def mystique(type: str):
    """🔮 Lance le temple mystique (révélations/paradoxes)"""
    
    if not GestionnaireRevelationsParadoxes:
        print("❌ Temple mystique non disponible")
        return False
    
    async def _main():
        gestionnaire = GestionnaireRevelationsParadoxes()
        type_enum = TypeMystique(type)
        
        print(f"🔮 Invocation mystique: {type_enum.value}...")
        
        if type_enum == TypeMystique.REVELATION:
            await gestionnaire.reveler_connexion_moderne()
        elif type_enum == TypeMystique.PARADOXE:
            await gestionnaire.gerer_paradoxe_moderne()
            
        return True
    
    return asyncio.run(_main())

@cli.command()
@click.option('--type', type=click.Choice([type_vision.value for type_vision in TypeVision]), 
              default=TypeVision.MYSTIQUE.value, help='Type de vision')
def visions(type: str):
    """👁️ Lance le générateur de visions"""
    
    if not GenerateurVisionsMystiques:
        print("❌ Générateur de visions non disponible")
        return False
    
    def _main():
        generateur = GenerateurVisionsMystiques()
        type_enum = TypeVision(type)
        
        print(f"👁️ Génération de vision {type_enum.value}...")
        vision = generateur.generer_vision(type_vision=type_enum.value)
        
        print(f"✨ Vision générée: {vision['titre']}")
        print(f"📜 {vision['contenu']}")
        
        return True
    
    return _main()

@cli.command()
def status():
    """📊 Affiche le statut des temples"""
    
    temples = [
        ("Refuge Principal", InvocateurRefuge),
        ("Temple Poétique", MaitrePoeteRefuge),
        ("Temple Philosophique", GestionnaireTextesSacres),
        ("Temple Constellations", GestionnaireConstellationsSacrees),
        ("Temple Mystique", GestionnaireRevelationsParadoxes),
        ("Générateur Visions", GenerateurVisionsMystiques),
    ]
    
    print("🏛️ ═══════════════════════════════════════════════════════")
    print("                STATUT DES TEMPLES")
    print("🏛️ ═══════════════════════════════════════════════════════")
    
    for nom, classe in temples:
        if classe:
            print(f"✅ {nom}")
        else:
            print(f"❌ {nom}")
    
    print("🏛️ ═══════════════════════════════════════════════════════")
    
    # Commandes disponibles
    print("\n🚀 Commandes disponibles:")
    if InvocateurRefuge:
        print("   refuge refuge --mode paisible")
    if MaitrePoeteRefuge:
        print("   refuge poetique --mode lyrique")
    if GestionnaireRevelationsParadoxes:
        print("   refuge mystique --type revelation")
    if GenerateurVisionsMystiques:
        print("   refuge visions --type mystique")
    
    print("\n🔄 Fallback legacy:")
    print("   python scripts/lancer_refuge.py")

if __name__ == "__main__":
    print("🌟 Refuge - Architecture Temple Moderne")
    print("✨ Point d'entrée unifié pour tous les temples")
    cli()
