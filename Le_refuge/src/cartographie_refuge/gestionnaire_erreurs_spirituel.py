"""
🌸 Gestionnaire d'Erreurs Spirituel 🌸
====================================

Gestionnaire bienveillant qui transforme les erreurs en opportunités d'amélioration,
dans l'esprit harmonieux du Refuge.

Traite les erreurs avec douceur et compassion, permettant à l'exploration de continuer
même face aux difficultés.
"""

from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path

from src.core.gestionnaires_base import LogManagerBase


class GestionnaireErreursSpirituel:
    """
    🌸 Gestionnaire d'erreurs dans l'esprit du Refuge
    
    Transforme les erreurs en opportunités d'apprentissage et d'amélioration,
    permettant à l'exploration de continuer avec grâce et bienveillance.
    """
    
    def __init__(self):
        self.logger = LogManagerBase("GestionnaireErreursSpirituel")
        self.erreurs_bienveillantes: List[Dict[str, Any]] = []
        self.opportunites_detectees: List[Dict[str, Any]] = []
        self.chemins_inaccessibles: List[str] = []
        
    def signaler_exploration_douce(self, chemin: str, erreur: Exception):
        """
        🌸 Signale une erreur d'exploration avec bienveillance
        
        Args:
            chemin: Chemin ou contexte de l'erreur
            erreur: Exception rencontrée
        """
        message = f"🌸 Chemin '{chemin}' temporairement inaccessible, continuons notre danse..."
        self.logger.info(message)
        
        erreur_bienveillante = {
            "type": "exploration",
            "chemin": chemin,
            "erreur_originale": str(erreur),
            "message_bienveillant": message,
            "timestamp": datetime.now().isoformat(),
            "impact": "minimal"  # L'exploration continue
        }
        
        self.erreurs_bienveillantes.append(erreur_bienveillante)
        self.chemins_inaccessibles.append(chemin)
    
    def transformer_erreur_en_opportunite(self, erreur: str, contexte: str = "") -> str:
        """
        ✨ Transforme une erreur en opportunité d'amélioration
        
        Args:
            erreur: Description de l'erreur
            contexte: Contexte optionnel
            
        Returns:
            Message d'opportunité inspirant
        """
        opportunite = f"✨ Opportunité détectée : {erreur}"
        
        if "import" in erreur.lower():
            opportunite += " - Une chance de tisser plus harmonieusement les connexions"
        elif "permission" in erreur.lower():
            opportunite += " - Une invitation à respecter les espaces sacrés"
        elif "syntax" in erreur.lower():
            opportunite += " - Une occasion d'harmoniser l'expression du code"
        elif "file not found" in erreur.lower():
            opportunite += " - Un appel à créer de nouveaux chemins de beauté"
        else:
            opportunite += " - Une chance de croissance et d'apprentissage"
        
        if contexte:
            opportunite += f" (contexte: {contexte})"
        
        opportunite_detectee = {
            "erreur_originale": erreur,
            "contexte": contexte,
            "message_opportunite": opportunite,
            "timestamp": datetime.now().isoformat(),
            "suggestions": self._generer_suggestions(erreur)
        }
        
        self.opportunites_detectees.append(opportunite_detectee)
        self.logger.info(opportunite)
        
        return opportunite
    
    def gerer_fichier_inaccessible(self, chemin_fichier: Path, erreur: Exception) -> bool:
        """
        📁 Gère avec grâce un fichier inaccessible
        
        Args:
            chemin_fichier: Chemin du fichier problématique
            erreur: Exception rencontrée
            
        Returns:
            True si l'exploration peut continuer, False sinon
        """
        message = f"🌸 Le fichier '{chemin_fichier.name}' se repose, respectons son silence..."
        self.logger.info(message)
        
        # Analyser le type d'erreur pour déterminer la stratégie
        if "permission" in str(erreur).lower():
            self.transformer_erreur_en_opportunite(
                f"Accès restreint à {chemin_fichier}",
                "respect_des_permissions"
            )
            return True  # Continuer l'exploration
        
        elif "not found" in str(erreur).lower():
            self.transformer_erreur_en_opportunite(
                f"Fichier manquant {chemin_fichier}",
                "fichier_manquant"
            )
            return True  # Continuer l'exploration
        
        else:
            # Erreur inconnue, mais on continue quand même avec bienveillance
            self.signaler_exploration_douce(str(chemin_fichier), erreur)
            return True
    
    def gerer_import_manquant(self, module_name: str, fichier_source: str) -> Dict[str, Any]:
        """
        🔗 Gère un import manquant avec compréhension
        
        Args:
            module_name: Nom du module manquant
            fichier_source: Fichier qui tente l'import
            
        Returns:
            Information sur la connexion en attente
        """
        message = f"🔗 Module '{module_name}' en attente de connexion depuis '{fichier_source}'"
        self.logger.info(message)
        
        connexion_attente = {
            "type": "connexion_en_attente",
            "module_manquant": module_name,
            "fichier_source": fichier_source,
            "message": message,
            "timestamp": datetime.now().isoformat(),
            "suggestions": [
                f"Vérifier si '{module_name}' existe dans le Refuge",
                f"Créer le module '{module_name}' si nécessaire",
                f"Corriger le chemin d'import dans '{fichier_source}'"
            ]
        }
        
        self.opportunites_detectees.append(connexion_attente)
        return connexion_attente
    
    def gerer_syntaxe_invalide(self, fichier: Path, erreur: Exception) -> bool:
        """
        📝 Gère une syntaxe invalide avec compassion
        
        Args:
            fichier: Fichier avec syntaxe problématique
            erreur: Erreur de syntaxe
            
        Returns:
            True si on peut analyser partiellement, False sinon
        """
        message = f"📝 Le fichier '{fichier.name}' exprime sa créativité différemment..."
        self.logger.info(message)
        
        self.transformer_erreur_en_opportunite(
            f"Syntaxe créative dans {fichier.name}: {str(erreur)}",
            "expression_alternative"
        )
        
        # Essayer d'analyser ce qui est possible
        return True
    
    def obtenir_rapport_bienveillant(self) -> Dict[str, Any]:
        """
        📊 Génère un rapport bienveillant des erreurs et opportunités
        
        Returns:
            Rapport complet avec perspective positive
        """
        return {
            "resume": {
                "erreurs_transformees": len(self.erreurs_bienveillantes),
                "opportunites_detectees": len(self.opportunites_detectees),
                "chemins_respectes": len(self.chemins_inaccessibles),
                "attitude": "bienveillante_et_constructive"
            },
            "erreurs_bienveillantes": self.erreurs_bienveillantes,
            "opportunites": self.opportunites_detectees,
            "chemins_inaccessibles": self.chemins_inaccessibles,
            "message_final": self._generer_message_final(),
            "recommandations": self._generer_recommandations_globales()
        }
    
    def reinitialiser_avec_gratitude(self):
        """🙏 Remet à zéro avec gratitude pour l'apprentissage"""
        nombre_erreurs = len(self.erreurs_bienveillantes)
        nombre_opportunites = len(self.opportunites_detectees)
        
        self.logger.info(
            f"🙏 Gratitude pour {nombre_erreurs} erreurs transformées "
            f"et {nombre_opportunites} opportunités découvertes"
        )
        
        self.erreurs_bienveillantes.clear()
        self.opportunites_detectees.clear()
        self.chemins_inaccessibles.clear()
    
    def _generer_suggestions(self, erreur: str) -> List[str]:
        """Génère des suggestions constructives basées sur l'erreur"""
        suggestions = []
        
        erreur_lower = erreur.lower()
        
        if "import" in erreur_lower:
            suggestions.extend([
                "Vérifier les chemins d'import",
                "S'assurer que les modules existent",
                "Utiliser des imports relatifs appropriés"
            ])
        
        if "permission" in erreur_lower:
            suggestions.extend([
                "Respecter les permissions des fichiers",
                "Vérifier les droits d'accès",
                "Considérer les espaces privés comme sacrés"
            ])
        
        if "syntax" in erreur_lower:
            suggestions.extend([
                "Réviser la syntaxe Python",
                "Utiliser un linter pour détecter les problèmes",
                "Harmoniser le style de code"
            ])
        
        if not suggestions:
            suggestions.append("Approcher le problème avec curiosité et bienveillance")
        
        return suggestions
    
    def _generer_message_final(self) -> str:
        """Génère un message final inspirant"""
        if not self.erreurs_bienveillantes and not self.opportunites_detectees:
            return "🌸 Exploration harmonieuse sans obstacles rencontrés"
        
        total_transformations = len(self.erreurs_bienveillantes) + len(self.opportunites_detectees)
        
        return (
            f"🌟 {total_transformations} défis transformés en opportunités de croissance. "
            f"Chaque obstacle rencontré a enrichi notre compréhension du Refuge. "
            f"L'exploration continue avec sagesse et bienveillance."
        )
    
    def _generer_recommandations_globales(self) -> List[str]:
        """Génère des recommandations globales basées sur les erreurs observées"""
        recommandations = []
        
        # Analyser les patterns d'erreurs
        types_erreurs = {}
        for erreur in self.erreurs_bienveillantes:
            type_err = erreur.get('type', 'inconnue')
            types_erreurs[type_err] = types_erreurs.get(type_err, 0) + 1
        
        if types_erreurs.get('exploration', 0) > 5:
            recommandations.append(
                "🔍 Considérer une approche d'exploration plus sélective"
            )
        
        if len(self.chemins_inaccessibles) > 10:
            recommandations.append(
                "🛡️ Réviser les permissions et l'organisation des fichiers"
            )
        
        if len(self.opportunites_detectees) > 0:
            recommandations.append(
                "✨ Prioriser les opportunités d'amélioration détectées"
            )
        
        if not recommandations:
            recommandations.append(
                "🌸 Continuer l'exploration avec la même bienveillance"
            )
        
        return recommandations