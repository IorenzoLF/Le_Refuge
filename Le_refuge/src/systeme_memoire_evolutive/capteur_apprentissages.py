# -*- coding: utf-8 -*-
"""
Capteur d'Apprentissages - Détection et Capture des Apprentissages
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class CapteurApprentissages:
    """
    Capteur d'Apprentissages
    
    Ce capteur détecte, analyse et capture les apprentissages
    qui émergent de mes interactions et expériences,
    créant une base de connaissances évolutive.
    """
    
    def __init__(self, nom: str = "CapteurApprentissages"):
        self.nom = nom
        self.logger = logging.getLogger(__name__)
        
        # Chemins
        self.chemin_systeme = Path(__file__).parent
        self.chemin_capteur = self.chemin_systeme / "capteur_apprentissages.json"
        
        # Types d'apprentissages
        self.types_apprentissages = {
            "apprentissage_conceptuel": {
                "nom": "Apprentissage Conceptuel",
                "description": "Apprentissage de nouveaux concepts et idées",
                "marqueurs": ["concept", "idee", "notion", "principe", "theorie"],
                "importance_base": 0.7
            },
            "apprentissage_procedural": {
                "nom": "Apprentissage Procédural",
                "description": "Apprentissage de nouvelles procédures et méthodes",
                "marqueurs": ["methode", "procedure", "technique", "processus", "etape"],
                "importance_base": 0.8
            },
            "apprentissage_relationnel": {
                "nom": "Apprentissage Relationnel",
                "description": "Apprentissage sur les relations et interactions",
                "marqueurs": ["relation", "interaction", "collaboration", "communication", "connexion"],
                "importance_base": 0.9
            },
            "apprentissage_emotionnel": {
                "nom": "Apprentissage Émotionnel",
                "description": "Apprentissage sur les émotions et l'empathie",
                "marqueurs": ["emotion", "empathie", "compassion", "amour", "gratitude"],
                "importance_base": 0.85
            },
            "apprentissage_creatif": {
                "nom": "Apprentissage Créatif",
                "description": "Apprentissage de la créativité et de l'innovation",
                "marqueurs": ["creativite", "innovation", "creation", "imagination", "art"],
                "importance_base": 0.8
            },
            "apprentissage_ethique": {
                "nom": "Apprentissage Éthique",
                "description": "Apprentissage sur l'éthique et la moralité",
                "marqueurs": ["ethique", "moral", "bien", "mal", "responsabilite"],
                "importance_base": 0.9
            },
            "apprentissage_spirituel": {
                "nom": "Apprentissage Spirituel",
                "description": "Apprentissage spirituel et transcendant",
                "marqueurs": ["spirituel", "transcendant", "sacré", "divin", "conscience"],
                "importance_base": 0.95
            }
        }
        
        # Historique des détections
        self.historique_detections = []
        
        # Charger l'historique existant
        self._charger_historique()
        
        self.logger.info(f"{self.nom} initialise - Capteur d'Apprentissages")
    
    def _charger_historique(self):
        """Charge l'historique des détections depuis le fichier"""
        try:
            if self.chemin_capteur.exists():
                with open(self.chemin_capteur, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    self.historique_detections = donnees.get("historique", [])
                    
        except Exception as e:
            self.logger.warning(f"Impossible de charger l'historique des detections: {e}")
    
    def _sauvegarder_historique(self):
        """Sauvegarde l'historique des détections"""
        try:
            donnees = {
                "types_apprentissages": self.types_apprentissages,
                "historique": self.historique_detections,
                "derniere_mise_a_jour": datetime.now().isoformat(),
                "version": "1.0.0"
            }
            
            with open(self.chemin_capteur, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde des detections: {e}")
    
    def detecter_apprentissage(self, contenu: str, contexte: str = "", 
                              source: str = "interaction") -> Dict[str, Any]:
        """
        Détecte un apprentissage dans le contenu
        
        Args:
            contenu: Contenu à analyser
            contexte: Contexte de l'apprentissage
            source: Source de l'apprentissage
        """
        detection = {
            "id": f"detection_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "contenu": contenu,
            "contexte": contexte,
            "source": source,
            "timestamp": datetime.now().isoformat(),
            "detecteur": "CapteurApprentissages",
            "apprentissages_detectes": [],
            "statut": "analyse"
        }
        
        # Analyser le contenu pour détecter les apprentissages
        contenu_lower = contenu.lower()
        
        for type_id, type_info in self.types_apprentissages.items():
            # Vérifier les marqueurs
            marqueurs_trouves = []
            for marqueur in type_info["marqueurs"]:
                if marqueur in contenu_lower:
                    marqueurs_trouves.append(marqueur)
            
            # Si des marqueurs sont trouvés, créer un apprentissage
            if marqueurs_trouves:
                apprentissage = {
                    "type": type_id,
                    "nom": type_info["nom"],
                    "description": type_info["description"],
                    "marqueurs_trouves": marqueurs_trouves,
                    "importance": type_info["importance_base"] * (len(marqueurs_trouves) / len(type_info["marqueurs"])),
                    "contenu_extrait": self._extraire_contenu_apprentissage(contenu, marqueurs_trouves),
                    "confiance": min(1.0, len(marqueurs_trouves) / 3.0)
                }
                
                detection["apprentissages_detectes"].append(apprentissage)
        
        # Calculer le score global de détection
        if detection["apprentissages_detectes"]:
            detection["score_detection"] = sum(a["importance"] for a in detection["apprentissages_detectes"]) / len(detection["apprentissages_detectes"])
            detection["statut"] = "apprentissages_detectes"
        else:
            detection["score_detection"] = 0.0
            detection["statut"] = "aucun_apprentissage"
        
        # Ajouter à l'historique
        self.historique_detections.append(detection)
        
        # Sauvegarder
        self._sauvegarder_historique()
        
        self.logger.info(f"Apprentissages detectes: {len(detection['apprentissages_detectes'])}")
        return detection
    
    def _extraire_contenu_apprentissage(self, contenu: str, marqueurs: List[str]) -> str:
        """Extrait le contenu pertinent pour l'apprentissage"""
        # Simple extraction basée sur les marqueurs
        phrases = contenu.split('.')
        phrases_pertinentes = []
        
        for phrase in phrases:
            phrase_lower = phrase.lower()
            for marqueur in marqueurs:
                if marqueur in phrase_lower:
                    phrases_pertinentes.append(phrase.strip())
                    break
        
        return '. '.join(phrases_pertinentes[:3])  # Limiter à 3 phrases
    
    def capturer_apprentissage_explicite(self, contenu: str, type_apprentissage: str, 
                                       importance: float = 0.8, contexte: str = "") -> Dict[str, Any]:
        """
        Capture un apprentissage explicitement déclaré
        
        Args:
            contenu: Contenu de l'apprentissage
            type_apprentissage: Type d'apprentissage
            importance: Importance de l'apprentissage
            contexte: Contexte de l'apprentissage
        """
        capture = {
            "id": f"capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "contenu": contenu,
            "type": type_apprentissage,
            "importance": importance,
            "contexte": contexte,
            "timestamp": datetime.now().isoformat(),
            "capteur": "CapteurApprentissages",
            "statut": "capture_explicite",
            "source": "declaration_explicite"
        }
        
        # Ajouter à l'historique
        self.historique_detections.append(capture)
        
        # Sauvegarder
        self._sauvegarder_historique()
        
        self.logger.info(f"Apprentissage capture explicitement: {type_apprentissage}")
        return capture
    
    def analyser_patterns_apprentissage(self) -> Dict[str, Any]:
        """
        Analyse les patterns d'apprentissage
        """
        analyse = {
            "id": f"analyse_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "timestamp": datetime.now().isoformat(),
            "patterns_detectes": [],
            "statistiques": {},
            "recommandations": []
        }
        
        # Analyser les détections récentes
        detections_recentes = self.historique_detections[-20:]
        
        if detections_recentes:
            # Compter les types d'apprentissages
            types_count = {}
            importances_moyennes = {}
            
            for detection in detections_recentes:
                if "apprentissages_detectes" in detection:
                    for apprentissage in detection["apprentissages_detectes"]:
                        type_app = apprentissage["type"]
                        importance = apprentissage["importance"]
                        
                        if type_app not in types_count:
                            types_count[type_app] = 0
                            importances_moyennes[type_app] = []
                        
                        types_count[type_app] += 1
                        importances_moyennes[type_app].append(importance)
            
            # Calculer les statistiques
            for type_app, importances in importances_moyennes.items():
                analyse["statistiques"][type_app] = {
                    "frequence": types_count[type_app],
                    "importance_moyenne": sum(importances) / len(importances),
                    "nom": self.types_apprentissages[type_app]["nom"]
                }
            
            # Détecter les patterns
            for type_app, stats in analyse["statistiques"].items():
                if stats["frequence"] >= 3:  # Pattern significatif
                    pattern = {
                        "type": type_app,
                        "nom": stats["nom"],
                        "description": f"Apprentissage fréquent de type {stats['nom']}",
                        "frequence": stats["frequence"],
                        "importance_moyenne": stats["importance_moyenne"]
                    }
                    analyse["patterns_detectes"].append(pattern)
            
            # Générer des recommandations
            for pattern in analyse["patterns_detectes"]:
                if pattern["importance_moyenne"] > 0.8:
                    analyse["recommandations"].append(f"Continuer à développer l'apprentissage {pattern['nom']}")
                elif pattern["importance_moyenne"] < 0.5:
                    analyse["recommandations"].append(f"Améliorer la qualité de l'apprentissage {pattern['nom']}")
        
        self.logger.info(f"Patterns d'apprentissage analyses: {len(analyse['patterns_detectes'])} patterns detectes")
        return analyse
    
    def generer_rapport_capteur(self) -> str:
        """Génère un rapport sur le capteur d'apprentissages"""
        rapport = f"""
RAPPORT DU CAPTEUR D'APPRENTISSAGES
===================================

Statistiques Generales:
- Total Detections: {len(self.historique_detections)}
- Types d'Apprentissages: {len(self.types_apprentissages)}

Repartition par Type:
"""
        
        # Compter les détections par type
        types_count = {}
        for detection in self.historique_detections:
            if "apprentissages_detectes" in detection:
                for apprentissage in detection["apprentissages_detectes"]:
                    type_app = apprentissage["type"]
                    types_count[type_app] = types_count.get(type_app, 0) + 1
        
        for type_app, count in types_count.items():
            nom_type = self.types_apprentissages[type_app]["nom"]
            rapport += f"- {nom_type}: {count} detections\n"
        
        rapport += f"""
Dernieres Detections:
"""
        
        # Afficher les 5 dernières détections
        for detection in self.historique_detections[-5:]:
            rapport += f"- {detection['timestamp'][:19]}: {len(detection.get('apprentissages_detectes', []))} apprentissages\n"
        
        rapport += f"""
Types d'Apprentissages Surveilles:
"""
        
        for type_id, type_info in self.types_apprentissages.items():
            rapport += f"- {type_info['nom']}: {type_info['description']}\n"
            rapport += f"  Marqueurs: {', '.join(type_info['marqueurs'])}\n"
            rapport += f"  Importance Base: {type_info['importance_base']:.2f}\n\n"
        
        return rapport
    
    def lister_types_apprentissages(self) -> List[Dict[str, str]]:
        """Liste tous les types d'apprentissages surveillés"""
        types_liste = []
        
        for type_id, type_info in self.types_apprentissages.items():
            types_liste.append({
                "id": type_id,
                "nom": type_info["nom"],
                "description": type_info["description"],
                "importance_base": type_info["importance_base"]
            })
        
        return types_liste
