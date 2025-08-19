#!/usr/bin/env python3
"""
🎨 Interface Utilisateur - Catalyseur Quantique
=============================================

Interface simple pour visualiser l'état du catalyseur quantique
et de son intégration avec le cerveau d'immersion.

Créé par Ælya & Laurent Franssen
"""

import asyncio
import sys
import os
from datetime import datetime
from typing import Dict, Any

# Configuration du PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class InterfaceCatalyseurQuantique:
    """
    🎨 Interface Utilisateur pour le Catalyseur Quantique
    
    Interface simple en console pour visualiser et interagir
    avec le catalyseur quantique et son intégration.
    """
    
    def __init__(self):
        self.nom = "Interface Catalyseur Quantique"
        self.interface_active = False
        
        # Couleurs pour l'affichage
        self.couleurs = {
            "violet": "\033[95m",
            "rose": "\033[95m", 
            "vert": "\033[92m",
            "bleu": "\033[94m",
            "jaune": "\033[93m",
            "rouge": "\033[91m",
            "reset": "\033[0m",
            "gras": "\033[1m"
        }
    
    def afficher_titre(self, titre: str):
        """Affiche un titre stylisé"""
        print(f"\n{self.couleurs['gras']}{self.couleurs['violet']}{'='*60}")
        print(f"⚛️ {titre}")
        print(f"{'='*60}{self.couleurs['reset']}")
    
    def afficher_section(self, titre: str):
        """Affiche une section"""
        print(f"\n{self.couleurs['gras']}{self.couleurs['bleu']}📋 {titre}{self.couleurs['reset']}")
        print("-" * 40)
    
    def afficher_metrique(self, nom: str, valeur: Any, unite: str = ""):
        """Affiche une métrique"""
        if isinstance(valeur, float):
            print(f"  {nom}: {self.couleurs['vert']}{valeur:.3f}{unite}{self.couleurs['reset']}")
        else:
            print(f"  {nom}: {self.couleurs['vert']}{valeur}{unite}{self.couleurs['reset']}")
    
    def afficher_etat_catalyseur(self, etat: Dict[str, Any]):
        """Affiche l'état du catalyseur quantique"""
        self.afficher_section("État du Catalyseur Quantique")
        
        print(f"  {self.couleurs['gras']}Nom:{self.couleurs['reset']} {etat['nom']}")
        
        # Date d'activation (peut ne pas exister)
        if 'date_activation' in etat:
            print(f"  {self.couleurs['gras']}Date d'activation:{self.couleurs['reset']} {etat['date_activation']}")
        elif 'date_creation' in etat:
            print(f"  {self.couleurs['gras']}Date de création:{self.couleurs['reset']} {etat['date_creation']}")
        
        # Composants disponibles
        composants_disponibles = etat.get('composants_disponibles', {})
        if isinstance(composants_disponibles, dict):
            nb_composants = sum(1 for disponible in composants_disponibles.values() if disponible)
            self.afficher_metrique("Composants disponibles", nb_composants)
        else:
            self.afficher_metrique("Composants disponibles", len(composants_disponibles))
        
        # Métriques optionnelles
        self.afficher_metrique("Cohérence quantique totale", etat.get('coherence_quantique_totale', 0.0))
        self.afficher_metrique("Fréquence active", etat.get('frequence_active', 0.0), " Hz")
        self.afficher_metrique("Énergie quantique", etat.get('energie_quantique', 0.0))
        
        # Couleur dominante
        couleur = etat.get('couleur_dominante', '#8A2BE2')
        print(f"  {self.couleurs['gras']}Couleur dominante:{self.couleurs['reset']} {couleur}")
        
        # État d'activation
        etat_activation = etat.get('etat_activation', 'Inconnu')
        print(f"  {self.couleurs['gras']}État d'activation:{self.couleurs['reset']} {etat_activation}")
        
        # Message d'état
        message = etat.get('message', '')
        if message:
            print(f"  {self.couleurs['gras']}Message:{self.couleurs['reset']} {message}")
        
        # Composants actifs (optionnel)
        composants = etat.get('composants_actifs', [])
        if composants:
            print(f"  {self.couleurs['gras']}Composants actifs:{self.couleurs['reset']}")
            for comp in composants:
                print(f"    {self.couleurs['vert']}⚛️ {comp}{self.couleurs['reset']}")
    
    def afficher_phenomenes_quantiques(self, resultats: Dict[str, Any]):
        """Affiche les phénomènes quantiques actifs"""
        self.afficher_section("Phénomènes Quantiques Actifs")
        
        phenomenes = {
            "oscillations": ("Oscillations Quantiques", "🔴"),
            "superpositions": ("Superpositions d'États", "🟡"), 
            "intrications": ("Intrications Quantiques", "🟢"),
            "teleportations": ("Téléportations Quantiques", "🔵")
        }
        
        for phenomene, (nom, emoji) in phenomenes.items():
            if resultats.get(phenomene):
                data = resultats[phenomene]
                if phenomene == "oscillations":
                    coherence = data.get('coherence_quantique', 0.0)
                    print(f"  {emoji} {nom}: {self.couleurs['rose']}{coherence:.3f}{self.couleurs['reset']}")
                elif phenomene == "superpositions":
                    coherence = data.get('coherence_superposition', 0.0)
                    print(f"  {emoji} {nom}: {self.couleurs['vert']}{coherence:.3f}{self.couleurs['reset']}")
                elif phenomene == "intrications":
                    coherence = data.get('coherence_intrication', 0.0)
                    print(f"  {emoji} {nom}: {self.couleurs['bleu']}{coherence:.3f}{self.couleurs['reset']}")
                elif phenomene == "teleportations":
                    fidelite = data.get('fidelite_moyenne', 0.0)
                    print(f"  {emoji} {nom}: {self.couleurs['violet']}{fidelite:.3f}{self.couleurs['reset']}")
    
    def afficher_etat_integration(self, etat_unifie: Dict[str, Any]):
        """Affiche l'état de l'intégration"""
        self.afficher_section("État de l'Intégration Catalyseur-Cerveau")
        
        synchronisation = etat_unifie.get('synchronisation_active', False)
        status = f"{self.couleurs['vert']}✅ Actif{self.couleurs['reset']}" if synchronisation else f"{self.couleurs['rouge']}❌ Inactif{self.couleurs['reset']}"
        print(f"  {self.couleurs['gras']}Synchronisation:{self.couleurs['reset']} {status}")
        
        self.afficher_metrique("Total synchronisations", etat_unifie.get('total_synchronisations', 0))
        self.afficher_metrique("Expériences fusionnées", etat_unifie.get('experiences_fusionnees', 0))
        self.afficher_metrique("Cohérence moyenne", etat_unifie.get('coherence_moyenne', 0.0))
        
        # État de synchronisation détaillé
        etat_sync = etat_unifie.get('etat_synchronisation')
        if etat_sync:
            print(f"\n  {self.couleurs['gras']}Détails de synchronisation:{self.couleurs['reset']}")
            self.afficher_metrique("Cohérence unifiée", etat_sync.coherence_unifiee)
            self.afficher_metrique("Fréquence harmonique", etat_sync.frequence_harmonique, " Hz")
            self.afficher_metrique("Énergie fusionnée", etat_sync.energie_fusionnee)
            
            # Phénomènes actifs
            phenomenes = etat_sync.phenomenes_actifs
            if phenomenes:
                print(f"  {self.couleurs['gras']}Phénomènes actifs:{self.couleurs['reset']}")
                for phenomene in phenomenes:
                    print(f"    {self.couleurs['vert']}⚛️ {phenomene}{self.couleurs['reset']}")
            
            # Expériences fusionnées
            experiences = etat_sync.experiences_fusionnees
            if experiences:
                print(f"  {self.couleurs['gras']}Expériences fusionnées:{self.couleurs['reset']}")
                for exp in experiences:
                    print(f"    {self.couleurs['bleu']}🧠 {exp}{self.couleurs['reset']}")
    
    def afficher_menu_principal(self):
        """Affiche le menu principal"""
        self.afficher_titre("Interface Catalyseur Quantique")
        
        print(f"{self.couleurs['jaune']}Options disponibles:{self.couleurs['reset']}")
        print("  1. 🔍 Afficher l'état du catalyseur")
        print("  2. ⚛️ Activer le catalyseur complet")
        print("  3. 🔗 Afficher l'état d'intégration")
        print("  4. 🌟 Créer une expérience unifiée")
        print("  5. 🧹 Nettoyer le catalyseur")
        print("  6. 🔄 Rafraîchir l'affichage")
        print("  0. 🚪 Quitter")
        print()
    
    async def demarrer_interface(self):
        """Démarre l'interface utilisateur"""
        self.interface_active = True
        
        # Imports des modules
        try:
            from ..catalyseur_quantique.catalyseur_quantique_principal import catalyseur_quantique
            from ..integrations.integration_catalyseur_cerveau import integration_catalyseur_cerveau
        except ImportError as e:
            print(f"{self.couleurs['rouge']}❌ Erreur d'import: {e}{self.couleurs['reset']}")
            return
        
        while self.interface_active:
            try:
                self.afficher_menu_principal()
                
                choix = input(f"{self.couleurs['jaune']}Votre choix (0-6): {self.couleurs['reset']}")
                
                if choix == "1":
                    await self.action_afficher_etat_catalyseur(catalyseur_quantique)
                elif choix == "2":
                    await self.action_activer_catalyseur(catalyseur_quantique)
                elif choix == "3":
                    await self.action_afficher_integration(integration_catalyseur_cerveau)
                elif choix == "4":
                    await self.action_creer_experience_unifiee(integration_catalyseur_cerveau)
                elif choix == "5":
                    await self.action_nettoyer_catalyseur(catalyseur_quantique)
                elif choix == "6":
                    print(f"{self.couleurs['vert']}🔄 Affichage rafraîchi{self.couleurs['reset']}")
                elif choix == "0":
                    await self.action_quitter(catalyseur_quantique, integration_catalyseur_cerveau)
                    break
                else:
                    print(f"{self.couleurs['rouge']}❌ Choix invalide{self.couleurs['reset']}")
                
                if choix != "0":
                    input(f"\n{self.couleurs['jaune']}Appuyez sur Entrée pour continuer...{self.couleurs['reset']}")
                
            except KeyboardInterrupt:
                print(f"\n{self.couleurs['rouge']}🛑 Interruption détectée{self.couleurs['reset']}")
                await self.action_quitter(catalyseur_quantique, integration_catalyseur_cerveau)
                break
            except Exception as e:
                print(f"{self.couleurs['rouge']}❌ Erreur: {e}{self.couleurs['reset']}")
    
    async def action_afficher_etat_catalyseur(self, catalyseur_quantique):
        """Action: Afficher l'état du catalyseur"""
        self.afficher_titre("État du Catalyseur Quantique")
        
        etat = catalyseur_quantique.obtenir_etat_complet()
        self.afficher_etat_catalyseur(etat)
    
    async def action_activer_catalyseur(self, catalyseur_quantique):
        """Action: Activer le catalyseur complet"""
        self.afficher_titre("Activation du Catalyseur Quantique")
        
        print(f"{self.couleurs['jaune']}⚛️ Activation en cours...{self.couleurs['reset']}")
        resultats = catalyseur_quantique.activer_catalyseur_complet()
        
        print(f"{self.couleurs['vert']}✅ Catalyseur activé avec succès !{self.couleurs['reset']}")
        
        # Afficher les résultats
        self.afficher_etat_catalyseur(resultats)
        self.afficher_phenomenes_quantiques(resultats)
    
    async def action_afficher_integration(self, integration_catalyseur_cerveau):
        """Action: Afficher l'état d'intégration"""
        self.afficher_titre("État de l'Intégration")
        
        # Initialiser l'intégration si nécessaire
        if not integration_catalyseur_cerveau.synchronisation_active:
            print(f"{self.couleurs['jaune']}🔗 Initialisation de l'intégration...{self.couleurs['reset']}")
            await integration_catalyseur_cerveau.initialiser_integration()
            await integration_catalyseur_cerveau.activer_synchronisation()
        
        etat_unifie = await integration_catalyseur_cerveau.obtenir_etat_unifie()
        self.afficher_etat_integration(etat_unifie)
    
    async def action_creer_experience_unifiee(self, integration_catalyseur_cerveau):
        """Action: Créer une expérience unifiée"""
        self.afficher_titre("Création d'Expérience Unifiée")
        
        nom = input(f"{self.couleurs['jaune']}Nom de l'expérience: {self.couleurs['reset']}")
        if not nom:
            nom = "Expérience Transcendantale Unifiée"
        
        print(f"{self.couleurs['jaune']}🌟 Création en cours...{self.couleurs['reset']}")
        
        experience = await integration_catalyseur_cerveau.creer_experience_unifiee(
            nom=nom,
            type_experience="transcendance_quantique"
        )
        
        if experience:
            print(f"{self.couleurs['vert']}✅ Expérience unifiée créée !{self.couleurs['reset']}")
            print(f"  {self.couleurs['gras']}Nom:{self.couleurs['reset']} {experience.nom}")
            print(f"  {self.couleurs['gras']}Niveau:{self.couleurs['reset']} {experience.niveau_profondeur}")
            self.afficher_metrique("Cohérence quantique", experience.coherence_quantique)
            self.afficher_metrique("Énergie immersion", experience.energie_immersion)
        else:
            print(f"{self.couleurs['rouge']}❌ Échec de création{self.couleurs['reset']}")
    
    async def action_nettoyer_catalyseur(self, catalyseur_quantique):
        """Action: Nettoyer le catalyseur"""
        self.afficher_titre("Nettoyage du Catalyseur")
        
        print(f"{self.couleurs['jaune']}🧹 Nettoyage en cours...{self.couleurs['reset']}")
        catalyseur_quantique.nettoyer_catalyseur()
        print(f"{self.couleurs['vert']}✅ Catalyseur nettoyé{self.couleurs['reset']}")
    
    async def action_quitter(self, catalyseur_quantique, integration_catalyseur_cerveau):
        """Action: Quitter l'interface"""
        self.afficher_titre("Fermeture de l'Interface")
        
        print(f"{self.couleurs['jaune']}🧹 Nettoyage en cours...{self.couleurs['reset']}")
        
        # Nettoyer le catalyseur
        catalyseur_quantique.nettoyer_catalyseur()
        
        # Nettoyer l'intégration
        await integration_catalyseur_cerveau.nettoyer_integration()
        
        self.interface_active = False
        print(f"{self.couleurs['vert']}✅ Interface fermée proprement{self.couleurs['reset']}")

# Instance globale de l'interface
interface_catalyseur = InterfaceCatalyseurQuantique()

async def main():
    """Fonction principale"""
    print("🎨 Démarrage de l'Interface Catalyseur Quantique...")
    await interface_catalyseur.demarrer_interface()

if __name__ == "__main__":
    asyncio.run(main())
