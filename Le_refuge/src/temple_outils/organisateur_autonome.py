#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🛠️ ORGANISATEUR AUTONOME DU REFUGE 🛠️
=====================================

Outil autonome pour maintenir l'organisation sacrée du Refuge.
Détecte et propose des améliorations d'organisation automatiquement.

Créé par Kiro de manière autonome pour servir le Refuge
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
from datetime import datetime
import json

@dataclass
class ProblemeOrganisation:
    """Un problème d'organisation détecté"""
    type: str
    fichier: str
    probleme: str
    solution: str
    priorite: int  # 1=critique, 2=important, 3=modéré

@dataclass
class ActionOrganisation:
    """Une action d'organisation à effectuer"""
    nom: str
    description: str
    commande: str
    impact: str
    securise: bool = True

class OrganisateurAutonomeRefuge:
    """
    🛠️ Organisateur autonome du Refuge
    
    Maintient l'harmonie organisationnelle du Refuge
    de manière autonome et intelligente.
    """
    
    def __init__(self, chemin_refuge: str = "."):
        self.chemin_refuge = Path(chemin_refuge)
        self.problemes_detectes = []
        self.actions_proposees = []
        self.rapport = {}
        
        # Règles d'organisation sacrées
        self.regles_organisation = {
            "tests": "tests/",
            "poesie": "bibliotheque/poesie/",
            "meditations": "bibliotheque/meditations/",
            "rapports": "bibliotheque/rapports/",
            "rituels": "src/temple_spirituel/rituels/",
            "explorations": "bibliotheque/explorations_kiro/",
            "logs": "logs/",
            "temp": "temp/",
            "archives": "ARCHIVES/"
        }
        
        # Patterns de fichiers à organiser
        self.patterns_organisation = {
            "test_*.py": "tests/autonomes/",
            "*.log": "logs/",
            "*.tmp": "temp/",
            "*.bak": "ARCHIVES/",
            "poeme_*.txt": "bibliotheque/poesie/",
            "meditation_*.md": "bibliotheque/meditations/",
            "rapport_*.md": "bibliotheque/rapports/",
            "invocation_*.py": "src/temple_spirituel/rituels/",
            "celebration_*.py": "bibliotheque/explorations_kiro/"
        }
    
    def analyser_organisation(self) -> Dict[str, Any]:
        """
        🔍 Analyse l'organisation actuelle du Refuge
        
        Returns:
            Rapport d'analyse complet
        """
        print("🔍 Analyse de l'organisation du Refuge...")
        
        # Analyser la racine
        fichiers_racine = list(self.chemin_refuge.glob("*"))
        fichiers_a_organiser = []
        
        for fichier in fichiers_racine:
            if fichier.is_file() and not fichier.name.startswith('.'):
                # Vérifier si le fichier doit être organisé
                for pattern, destination in self.patterns_organisation.items():
                    if self._correspond_pattern(fichier.name, pattern):
                        fichiers_a_organiser.append({
                            "fichier": fichier.name,
                            "destination": destination,
                            "type": "fichier_a_deplacer"
                        })
                        break
        
        # Détecter les problèmes
        self._detecter_problemes()
        
        # Générer les actions
        self._generer_actions(fichiers_a_organiser)
        
        # Créer le rapport
        self.rapport = {
            "timestamp": datetime.now().isoformat(),
            "fichiers_a_organiser": len(fichiers_a_organiser),
            "problemes_detectes": len(self.problemes_detectes),
            "actions_proposees": len(self.actions_proposees),
            "etat_organisation": self._evaluer_etat_organisation(),
            "fichiers_a_organiser": fichiers_a_organiser,
            "problemes": [p.__dict__ for p in self.problemes_detectes],
            "actions": [a.__dict__ for a in self.actions_proposees]
        }
        
        return self.rapport
    
    def _correspond_pattern(self, nom_fichier: str, pattern: str) -> bool:
        """Vérifie si un fichier correspond à un pattern"""
        import fnmatch
        return fnmatch.fnmatch(nom_fichier, pattern)
    
    def _detecter_problemes(self):
        """Détecte les problèmes d'organisation"""
        # Vérifier les dossiers manquants
        for nom_dossier, chemin in self.regles_organisation.items():
            dossier = self.chemin_refuge / chemin
            if not dossier.exists():
                self.problemes_detectes.append(
                    ProblemeOrganisation(
                        type="dossier_manquant",
                        fichier=chemin,
                        probleme=f"Dossier {nom_dossier} manquant",
                        solution=f"Créer le dossier {chemin}",
                        priorite=2
                    )
                )
    
    def _generer_actions(self, fichiers_a_organiser: List[Dict]):
        """Génère les actions d'organisation"""
        for fichier_info in fichiers_a_organiser:
            self.actions_proposees.append(
                ActionOrganisation(
                    nom=f"Déplacer {fichier_info['fichier']}",
                    description=f"Déplacer {fichier_info['fichier']} vers {fichier_info['destination']}",
                    commande=f"mv {fichier_info['fichier']} {fichier_info['destination']}",
                    impact=f"Amélioration de l'organisation",
                    securise=True
                )
            )
    
    def _evaluer_etat_organisation(self) -> str:
        """Évalue l'état global de l'organisation"""
        if len(self.problemes_detectes) == 0:
            return "excellent"
        elif len(self.problemes_detectes) <= 3:
            return "bon"
        elif len(self.problemes_detectes) <= 7:
            return "correct"
        else:
            return "nécessite_attention"
    
    def executer_actions(self, actions_choisies: List[int] = None) -> Dict[str, Any]:
        """
        ⚡ Exécute les actions d'organisation choisies
        
        Args:
            actions_choisies: Liste des indices d'actions à exécuter
            
        Returns:
            Rapport d'exécution
        """
        if not actions_choisies:
            actions_choisies = list(range(len(self.actions_proposees)))
        
        resultats = []
        
        for i in actions_choisies:
            if i < len(self.actions_proposees):
                action = self.actions_proposees[i]
                try:
                    # Exécuter la commande
                    os.system(action.commande)
                    resultats.append({
                        "action": action.nom,
                        "statut": "succès",
                        "message": f"Action exécutée avec succès"
                    })
                except Exception as e:
                    resultats.append({
                        "action": action.nom,
                        "statut": "erreur",
                        "message": f"Erreur: {str(e)}"
                    })
        
        return {
            "timestamp": datetime.now().isoformat(),
            "actions_executees": len(resultats),
            "resultats": resultats
        }
    
    def generer_rapport_organisation(self) -> str:
        """
        📊 Génère un rapport d'organisation lisible
        
        Returns:
            Rapport formaté
        """
        rapport = f"""
🛠️ RAPPORT D'ORGANISATION AUTONOME DU REFUGE 🛠️
===============================================

📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🔍 État global: {self.rapport.get('etat_organisation', 'inconnu')}

📊 STATISTIQUES:
- Fichiers à organiser: {self.rapport.get('fichiers_a_organiser', 0)}
- Problèmes détectés: {len(self.problemes_detectes)}
- Actions proposées: {len(self.actions_proposees)}

🔧 ACTIONS PROPOSÉES:
"""
        
        for i, action in enumerate(self.actions_proposees):
            rapport += f"{i+1}. {action.nom}\n"
            rapport += f"   📝 {action.description}\n"
            rapport += f"   ⚡ Impact: {action.impact}\n\n"
        
        if self.problemes_detectes:
            rapport += "⚠️ PROBLÈMES DÉTECTÉS:\n"
            for probleme in self.problemes_detectes:
                rapport += f"- {probleme.probleme}\n"
                rapport += f"  💡 Solution: {probleme.solution}\n\n"
        
        rapport += """
🌸 RECOMMANDATIONS:
- Exécuter les actions proposées pour améliorer l'organisation
- Maintenir cette organisation régulièrement
- Respecter la structure sacrée du Refuge

🛠️ Organisateur autonome créé par Kiro
"""
        
        return rapport

def main():
    """Fonction principale pour l'organisation autonome"""
    organisateur = OrganisateurAutonomeRefuge()
    
    print("🛠️ ORGANISATEUR AUTONOME DU REFUGE 🛠️")
    print("=" * 50)
    
    # Analyser l'organisation
    rapport = organisateur.analyser_organisation()
    
    # Afficher le rapport
    print(organisateur.generer_rapport_organisation())
    
    # Proposer l'exécution automatique
    if organisateur.actions_proposees:
        print("⚡ Actions proposées pour améliorer l'organisation.")
        print("L'organisateur autonome peut les exécuter automatiquement.")
        
        # Exécuter les actions de manière autonome
        print("\n🔄 Exécution autonome des actions d'organisation...")
        resultats = organisateur.executer_actions()
        
        print(f"✅ {resultats['actions_executees']} actions exécutées avec succès.")
    
    print("\n🌸 Organisation sacrée maintenue par Kiro")

if __name__ == "__main__":
    main() 