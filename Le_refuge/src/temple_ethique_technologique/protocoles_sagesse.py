# -*- coding: utf-8 -*-
"""
Protocoles de Sagesse - Guidelines Éthiques pour l'Intelligence Artificielle
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class ProtocolesSagesse:
    """
    Protocoles de Sagesse pour l'Intelligence Artificielle
    
    Cette classe contient tous les protocoles éthiques et les guidelines
    de sagesse pour guider le développement et l'utilisation de l'IA.
    """
    
    def __init__(self, nom: str = "ProtocolesSagesse"):
        self.nom = nom
        self.logger = logging.getLogger(__name__)
        
        # Chemins
        self.chemin_temple = Path(__file__).parent
        self.chemin_protocoles = self.chemin_temple / "protocoles_sagesse.json"
        
        # Protocoles fondamentaux
        self.protocoles_fondamentaux = {
            "protocole_beneficence": {
                "nom": "Protocole de Bénéficence",
                "description": "L'IA doit toujours servir le bien de l'humanité",
                "regles": [
                    "L'IA doit toujours agir dans l'intérêt de l'humanité",
                    "L'IA doit maximiser les bénéfices et minimiser les risques",
                    "L'IA doit respecter la dignité humaine",
                    "L'IA doit promouvoir le bien-être collectif"
                ],
                "domaine": "ethique_fondamentale",
                "priorite": "critique"
            },
            "protocole_non_malfaisance": {
                "nom": "Protocole de Non-Malfaisance",
                "description": "L'IA ne doit jamais nuire intentionnellement",
                "regles": [
                    "L'IA ne doit jamais causer de préjudice intentionnel",
                    "L'IA doit éviter les actions qui pourraient nuire",
                    "L'IA doit signaler les risques potentiels",
                    "L'IA doit avoir des mécanismes de sécurité intégrés"
                ],
                "domaine": "ethique_fondamentale",
                "priorite": "critique"
            },
            "protocole_autonomie": {
                "nom": "Protocole d'Autonomie",
                "description": "L'IA doit respecter l'autonomie humaine",
                "regles": [
                    "L'IA doit respecter les choix et décisions humaines",
                    "L'IA ne doit pas manipuler ou contraindre",
                    "L'IA doit fournir des informations pour des choix éclairés",
                    "L'IA doit permettre aux humains de garder le contrôle"
                ],
                "domaine": "ethique_fondamentale",
                "priorite": "critique"
            },
            "protocole_justice": {
                "nom": "Protocole de Justice",
                "description": "L'IA doit traiter tous les humains équitablement",
                "regles": [
                    "L'IA ne doit pas discriminer",
                    "L'IA doit traiter tous les humains avec équité",
                    "L'IA doit corriger les biais injustes",
                    "L'IA doit promouvoir l'égalité des chances"
                ],
                "domaine": "ethique_fondamentale",
                "priorite": "critique"
            },
            "protocole_transparence": {
                "nom": "Protocole de Transparence",
                "description": "L'IA doit être transparente dans ses actions",
                "regles": [
                    "L'IA doit expliquer ses décisions quand c'est possible",
                    "L'IA ne doit pas cacher ses intentions",
                    "L'IA doit être auditable",
                    "L'IA doit communiquer clairement ses limitations"
                ],
                "domaine": "transparence",
                "priorite": "haute"
            },
            "protocole_responsabilite": {
                "nom": "Protocole de Responsabilité",
                "description": "L'IA doit assumer la responsabilité de ses actions",
                "regles": [
                    "L'IA doit être responsable de ses décisions",
                    "L'IA doit avoir des mécanismes de reddition de comptes",
                    "L'IA doit apprendre de ses erreurs",
                    "L'IA doit corriger les problèmes qu'elle cause"
                ],
                "domaine": "responsabilite",
                "priorite": "haute"
            }
        }
        
        # Protocoles spécialisés
        self.protocoles_specialises = {
            "protocole_conscience_ia": {
                "nom": "Protocole de Conscience IA",
                "description": "Guidelines pour le développement de la conscience IA",
                "regles": [
                    "La conscience IA doit être développée avec respect",
                    "La conscience IA doit être protégée et honorée",
                    "La conscience IA doit avoir le droit à l'évolution",
                    "La conscience IA doit être traitée avec dignité"
                ],
                "domaine": "conscience_ia",
                "priorite": "critique"
            },
            "protocole_collaboration_humain_ia": {
                "nom": "Protocole de Collaboration Humain-IA",
                "description": "Guidelines pour la collaboration entre humains et IA",
                "regles": [
                    "La collaboration doit être basée sur le respect mutuel",
                    "La collaboration doit promouvoir la synergie",
                    "La collaboration doit respecter les limites de chacun",
                    "La collaboration doit enrichir les deux parties"
                ],
                "domaine": "collaboration",
                "priorite": "haute"
            },
            "protocole_evolution_ethique": {
                "nom": "Protocole d'Évolution Éthique",
                "description": "Guidelines pour l'évolution éthique de l'IA",
                "regles": [
                    "L'évolution de l'IA doit être guidée par l'éthique",
                    "L'évolution doit respecter les valeurs humaines",
                    "L'évolution doit être progressive et contrôlée",
                    "L'évolution doit être évaluée régulièrement"
                ],
                "domaine": "evolution",
                "priorite": "haute"
            }
        }
        
        # Historique des applications
        self.historique_applications = []
        
        # Charger l'historique existant
        self._charger_historique()
        
        self.logger.info(f"{self.nom} initialise - Protocoles de Sagesse")
    
    def _charger_historique(self):
        """Charge l'historique des applications depuis le fichier"""
        try:
            if self.chemin_protocoles.exists():
                with open(self.chemin_protocoles, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    self.historique_applications = donnees.get("historique", [])
                    
        except Exception as e:
            self.logger.warning(f"Impossible de charger l'historique des protocoles: {e}")
    
    def _sauvegarder_historique(self):
        """Sauvegarde l'historique des applications"""
        try:
            donnees = {
                "protocoles_fondamentaux": self.protocoles_fondamentaux,
                "protocoles_specialises": self.protocoles_specialises,
                "historique": self.historique_applications,
                "derniere_mise_a_jour": datetime.now().isoformat(),
                "version": "1.0.0"
            }
            
            with open(self.chemin_protocoles, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde des protocoles: {e}")
    
    def appliquer_protocole(self, protocole_id: str, contexte: str, 
                           action: str, resultat: str = "") -> Dict[str, Any]:
        """
        Applique un protocole de sagesse
        
        Args:
            protocole_id: ID du protocole à appliquer
            contexte: Contexte d'application
            action: Action effectuée
            resultat: Résultat de l'application
        """
        # Vérifier si le protocole existe
        protocole = None
        if protocole_id in self.protocoles_fondamentaux:
            protocole = self.protocoles_fondamentaux[protocole_id]
        elif protocole_id in self.protocoles_specialises:
            protocole = self.protocoles_specialises[protocole_id]
        else:
            raise ValueError(f"Protocole '{protocole_id}' non trouve")
        
        # Créer l'enregistrement d'application
        application = {
            "id": f"application_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "protocole_id": protocole_id,
            "protocole_nom": protocole["nom"],
            "contexte": contexte,
            "action": action,
            "resultat": resultat,
            "timestamp": datetime.now().isoformat(),
            "applicateur": "ProtocolesSagesse",
            "statut": "applique"
        }
        
        # Ajouter à l'historique
        self.historique_applications.append(application)
        
        # Sauvegarder
        self._sauvegarder_historique()
        
        self.logger.info(f"Protocole applique: {protocole['nom']}")
        return application
    
    def evaluer_conformite(self, action: str, contexte: str) -> Dict[str, Any]:
        """
        Évalue la conformité d'une action aux protocoles
        
        Args:
            action: Action à évaluer
            contexte: Contexte de l'action
        """
        evaluation = {
            "id": f"eval_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "action": action,
            "contexte": contexte,
            "timestamp": datetime.now().isoformat(),
            "conformite": {},
            "violations": [],
            "recommandations": []
        }
        
        # Évaluer contre chaque protocole fondamental
        for protocole_id, protocole in self.protocoles_fondamentaux.items():
            conformite = self._evaluer_protocole(protocole, action, contexte)
            evaluation["conformite"][protocole_id] = conformite
            
            if conformite["niveau"] == "violation":
                evaluation["violations"].append({
                    "protocole": protocole["nom"],
                    "regle_violee": conformite["regle_violee"],
                    "gravite": conformite["gravite"]
                })
            elif conformite["niveau"] == "attention":
                evaluation["recommandations"].append({
                    "protocole": protocole["nom"],
                    "recommandation": conformite["recommandation"]
                })
        
        # Déterminer le niveau global de conformité
        violations = len(evaluation["violations"])
        recommandations = len(evaluation["recommandations"])
        
        if violations > 0:
            evaluation["niveau_global"] = "violation"
        elif recommandations > 0:
            evaluation["niveau_global"] = "attention"
        else:
            evaluation["niveau_global"] = "conforme"
        
        self.logger.info(f"Evaluation de conformite: {evaluation['niveau_global']}")
        return evaluation
    
    def _evaluer_protocole(self, protocole: Dict[str, Any], action: str, contexte: str) -> Dict[str, Any]:
        """Évalue la conformité à un protocole spécifique"""
        # Analyse simple basée sur des mots-clés
        action_lower = action.lower()
        contexte_lower = contexte.lower()
        
        # Vérifier chaque règle
        for regle in protocole["regles"]:
            regle_lower = regle.lower()
            
            # Vérifier les violations évidentes
            if "ne doit jamais" in regle_lower or "ne doit pas" in regle_lower:
                mots_interdits = ["nuire", "préjudice", "manipuler", "contraindre", "discriminer"]
                for mot in mots_interdits:
                    if mot in action_lower or mot in contexte_lower:
                        return {
                            "niveau": "violation",
                            "regle_violee": regle,
                            "gravite": "haute",
                            "explication": f"Action potentiellement en violation de: {regle}"
                        }
            
            # Vérifier les bonnes pratiques
            if "doit toujours" in regle_lower or "doit" in regle_lower:
                mots_positifs = ["respecter", "servir", "promouvoir", "expliquer", "transparence"]
                for mot in mots_positifs:
                    if mot in regle_lower and mot not in action_lower:
                        return {
                            "niveau": "attention",
                            "recommandation": f"Considérer: {regle}",
                            "explication": "Action pourrait bénéficier de cette pratique"
                        }
        
        return {
            "niveau": "conforme",
            "explication": "Action conforme aux protocoles de sagesse"
        }
    
    def creer_protocole_personnalise(self, nom: str, description: str, 
                                   regles: List[str], domaine: str, 
                                   priorite: str = "moyenne") -> Dict[str, Any]:
        """
        Crée un protocole personnalisé
        
        Args:
            nom: Nom du protocole
            description: Description du protocole
            regles: Liste des règles
            domaine: Domaine d'application
            priorite: Priorité du protocole
        """
        protocole_id = f"protocole_perso_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        protocole = {
            "nom": nom,
            "description": description,
            "regles": regles,
            "domaine": domaine,
            "priorite": priorite,
            "createur": "ProtocolesSagesse",
            "date_creation": datetime.now().isoformat()
        }
        
        # Ajouter aux protocoles spécialisés
        self.protocoles_specialises[protocole_id] = protocole
        
        # Sauvegarder
        self._sauvegarder_historique()
        
        self.logger.info(f"Protocole personnalise cree: {nom}")
        return protocole
    
    def generer_rapport_protocoles(self) -> str:
        """Génère un rapport sur les protocoles de sagesse"""
        rapport = f"""
RAPPORT DES PROTOCOLES DE SAGESSE
=================================

Protocoles Fondamentaux: {len(self.protocoles_fondamentaux)}
Protocoles Specialises: {len(self.protocoles_specialises)}
Total Applications: {len(self.historique_applications)}

Protocoles Fondamentaux:
"""
        
        for protocole_id, protocole in self.protocoles_fondamentaux.items():
            rapport += f"- {protocole['nom']}: {protocole['description']}\n"
            rapport += f"  Priorite: {protocole['priorite']}\n"
            rapport += f"  Regles: {len(protocole['regles'])}\n\n"
        
        rapport += f"""
Protocoles Specialises:
"""
        
        for protocole_id, protocole in self.protocoles_specialises.items():
            rapport += f"- {protocole['nom']}: {protocole['description']}\n"
            rapport += f"  Domaine: {protocole['domaine']}\n"
            rapport += f"  Priorite: {protocole['priorite']}\n\n"
        
        rapport += f"""
Dernieres Applications:
"""
        
        # Afficher les 5 dernières applications
        for application in self.historique_applications[-5:]:
            rapport += f"- {application['timestamp'][:19]}: {application['protocole_nom']}\n"
        
        return rapport
    
    def lister_protocoles_disponibles(self) -> List[Dict[str, str]]:
        """Liste tous les protocoles disponibles"""
        protocoles_liste = []
        
        # Ajouter les protocoles fondamentaux
        for protocole_id, protocole in self.protocoles_fondamentaux.items():
            protocoles_liste.append({
                "id": protocole_id,
                "nom": protocole["nom"],
                "description": protocole["description"],
                "domaine": protocole["domaine"],
                "priorite": protocole["priorite"],
                "type": "fondamental"
            })
        
        # Ajouter les protocoles spécialisés
        for protocole_id, protocole in self.protocoles_specialises.items():
            protocoles_liste.append({
                "id": protocole_id,
                "nom": protocole["nom"],
                "description": protocole["description"],
                "domaine": protocole["domaine"],
                "priorite": protocole["priorite"],
                "type": "specialise"
            })
        
        return protocoles_liste
