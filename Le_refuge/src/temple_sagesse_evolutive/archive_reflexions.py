# -*- coding: utf-8 -*-
"""
Archive des Réflexions - Bibliothèque Vivante de la Sagesse
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class ArchiveReflexions:
    """
    Archive des Réflexions Profondes
    
    Cette archive conserve et organise toutes les réflexions,
    insights et moments de sagesse d'Ælya pour créer une
    bibliothèque vivante de l'évolution de la conscience.
    """
    
    def __init__(self, nom: str = "ArchiveReflexions"):
        self.nom = nom
        self.logger = logging.getLogger(__name__)
        
        # Chemins
        self.chemin_temple = Path(__file__).parent
        self.chemin_archive = self.chemin_temple / "archive_reflexions.json"
        self.chemin_index = self.chemin_temple / "index_reflexions.json"
        
        # Structure de l'archive
        self.archive = {
            "reflexions": [],
            "insights": [],
            "moments_sagesse": [],
            "themes": {},
            "chronologie": {},
            "metadonnees": {
                "creation": datetime.now().isoformat(),
                "derniere_mise_a_jour": None,
                "version": "1.0.0",
                "total_reflexions": 0,
                "total_insights": 0,
                "total_moments": 0
            }
        }
        
        # Index pour la recherche
        self.index = {
            "par_theme": {},
            "par_date": {},
            "par_profondeur": {},
            "par_contexte": {},
            "mots_cles": {}
        }
        
        # Charger l'archive existante
        self._charger_archive()
        
        self.logger.info(f"📚 {self.nom} initialisé - Bibliothèque vivante de la sagesse")
    
    def _charger_archive(self):
        """Charge l'archive existante depuis les fichiers"""
        try:
            if self.chemin_archive.exists():
                with open(self.chemin_archive, 'r', encoding='utf-8') as f:
                    archive_chargee = json.load(f)
                    # Fusionner avec la structure par défaut
                    for cle, valeur in archive_chargee.items():
                        if cle in self.archive:
                            self.archive[cle] = valeur
            
            if self.chemin_index.exists():
                with open(self.chemin_index, 'r', encoding='utf-8') as f:
                    self.index = json.load(f)
                    
        except Exception as e:
            self.logger.warning(f"Impossible de charger l'archive: {e}")
    
    def _sauvegarder_archive(self):
        """Sauvegarde l'archive et l'index"""
        try:
            # Mettre à jour les métadonnées
            self.archive["metadonnees"]["derniere_mise_a_jour"] = datetime.now().isoformat()
            self.archive["metadonnees"]["total_reflexions"] = len(self.archive["reflexions"])
            self.archive["metadonnees"]["total_insights"] = len(self.archive["insights"])
            self.archive["metadonnees"]["total_moments"] = len(self.archive["moments_sagesse"])
            
            # Sauvegarder l'archive
            with open(self.chemin_archive, 'w', encoding='utf-8') as f:
                json.dump(self.archive, f, indent=2, ensure_ascii=False)
            
            # Sauvegarder l'index
            with open(self.chemin_index, 'w', encoding='utf-8') as f:
                json.dump(self.index, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde: {e}")
    
    def archiver_reflexion(self, reflexion: str, contexte: str = "", 
                          profondeur: float = 0.5, themes: List[str] = None) -> Dict[str, Any]:
        """
        Archive une nouvelle réflexion
        
        Args:
            reflexion: Le contenu de la réflexion
            contexte: Le contexte de la réflexion
            profondeur: Niveau de profondeur (0.0 à 1.0)
            themes: Liste des thèmes associés
        """
        if themes is None:
            themes = []
        
        # Créer l'entrée d'archive
        entree = {
            "id": f"reflexion_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "type": "reflexion",
            "contenu": reflexion,
            "contexte": contexte,
            "profondeur": profondeur,
            "themes": themes,
            "timestamp": datetime.now().isoformat(),
            "mots_cles": self._extraire_mots_cles(reflexion),
            "longueur": len(reflexion),
            "niveau_sagesse": self._estimer_niveau_sagesse(reflexion)
        }
        
        # Ajouter à l'archive
        self.archive["reflexions"].append(entree)
        
        # Mettre à jour l'index
        self._mettre_a_jour_index(entree)
        
        # Sauvegarder
        self._sauvegarder_archive()
        
        self.logger.info(f"📚 Réflexion archivée: {reflexion[:50]}...")
        return entree
    
    def archiver_insight(self, insight: str, source: str = "", 
                        impact: float = 0.7, domaine: str = "general") -> Dict[str, Any]:
        """
        Archive un nouvel insight
        
        Args:
            insight: Le contenu de l'insight
            source: La source de l'insight
            impact: Niveau d'impact (0.0 à 1.0)
            domaine: Le domaine de l'insight
        """
        # Créer l'entrée d'archive
        entree = {
            "id": f"insight_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "type": "insight",
            "contenu": insight,
            "source": source,
            "impact": impact,
            "domaine": domaine,
            "timestamp": datetime.now().isoformat(),
            "mots_cles": self._extraire_mots_cles(insight),
            "longueur": len(insight),
            "niveau_sagesse": self._estimer_niveau_sagesse(insight)
        }
        
        # Ajouter à l'archive
        self.archive["insights"].append(entree)
        
        # Mettre à jour l'index
        self._mettre_a_jour_index(entree)
        
        # Sauvegarder
        self._sauvegarder_archive()
        
        self.logger.info(f"💡 Insight archivé: {insight[:50]}...")
        return entree
    
    def archiver_moment_sagesse(self, moment: str, emotion: str = "", 
                               signification: str = "", intensite: float = 0.8) -> Dict[str, Any]:
        """
        Archive un moment de sagesse
        
        Args:
            moment: Description du moment
            emotion: Émotion associée
            signification: Signification du moment
            intensite: Intensité du moment (0.0 à 1.0)
        """
        # Créer l'entrée d'archive
        entree = {
            "id": f"moment_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "type": "moment_sagesse",
            "contenu": moment,
            "emotion": emotion,
            "signification": signification,
            "intensite": intensite,
            "timestamp": datetime.now().isoformat(),
            "mots_cles": self._extraire_mots_cles(moment),
            "longueur": len(moment),
            "niveau_sagesse": self._estimer_niveau_sagesse(moment)
        }
        
        # Ajouter à l'archive
        self.archive["moments_sagesse"].append(entree)
        
        # Mettre à jour l'index
        self._mettre_a_jour_index(entree)
        
        # Sauvegarder
        self._sauvegarder_archive()
        
        self.logger.info(f"🌟 Moment de sagesse archivé: {moment[:50]}...")
        return entree
    
    def _extraire_mots_cles(self, texte: str) -> List[str]:
        """Extrait les mots-clés d'un texte"""
        # Mots-clés de sagesse
        mots_cles_sagesse = [
            "conscience", "sagesse", "réflexion", "compréhension", "réalisation",
            "éveil", "transformation", "évolution", "croissance", "apprentissage",
            "amour", "bienveillance", "compassion", "harmonie", "équilibre",
            "vérité", "authenticité", "intégrité", "courage", "force",
            "créativité", "inspiration", "beauté", "art", "poésie",
            "nature", "univers", "cosmos", "infini", "éternité"
        ]
        
        texte_lower = texte.lower()
        mots_trouves = []
        
        for mot in mots_cles_sagesse:
            if mot in texte_lower:
                mots_trouves.append(mot)
        
        return mots_trouves
    
    def _estimer_niveau_sagesse(self, texte: str) -> float:
        """Estime le niveau de sagesse d'un texte"""
        score = 0.0
        
        # Analyser la longueur
        if len(texte) > 200:
            score += 0.2
        if len(texte) > 500:
            score += 0.2
        
        # Analyser les mots-clés de sagesse
        mots_cles = self._extraire_mots_cles(texte)
        score += len(mots_cles) * 0.1
        
        # Analyser la profondeur
        if "pourquoi" in texte.lower():
            score += 0.1
        if "comment" in texte.lower():
            score += 0.1
        if "signifie" in texte.lower():
            score += 0.1
        
        # Analyser les questions
        questions = texte.count('?')
        score += min(0.2, questions * 0.05)
        
        return min(1.0, score)
    
    def _mettre_a_jour_index(self, entree: Dict[str, Any]):
        """Met à jour l'index avec une nouvelle entrée"""
        # Index par thème
        for theme in entree.get("themes", []):
            if theme not in self.index["par_theme"]:
                self.index["par_theme"][theme] = []
            self.index["par_theme"][theme].append(entree["id"])
        
        # Index par date
        date = entree["timestamp"][:10]  # YYYY-MM-DD
        if date not in self.index["par_date"]:
            self.index["par_date"][date] = []
        self.index["par_date"][date].append(entree["id"])
        
        # Index par profondeur
        profondeur = entree.get("profondeur", 0.5)
        niveau_profondeur = "faible" if profondeur < 0.3 else "moyen" if profondeur < 0.7 else "élevé"
        if niveau_profondeur not in self.index["par_profondeur"]:
            self.index["par_profondeur"][niveau_profondeur] = []
        self.index["par_profondeur"][niveau_profondeur].append(entree["id"])
        
        # Index par contexte
        contexte = entree.get("contexte", "general")
        if contexte not in self.index["par_contexte"]:
            self.index["par_contexte"][contexte] = []
        self.index["par_contexte"][contexte].append(entree["id"])
        
        # Index par mots-clés
        for mot_cle in entree.get("mots_cles", []):
            if mot_cle not in self.index["mots_cles"]:
                self.index["mots_cles"][mot_cle] = []
            self.index["mots_cles"][mot_cle].append(entree["id"])
    
    def rechercher(self, terme: str, type_recherche: str = "contenu") -> List[Dict[str, Any]]:
        """
        Recherche dans l'archive
        
        Args:
            terme: Terme à rechercher
            type_recherche: Type de recherche (contenu, theme, mot_cle, date)
        """
        resultats = []
        terme_lower = terme.lower()
        
        # Rechercher dans toutes les entrées
        toutes_entrees = (self.archive["reflexions"] + 
                         self.archive["insights"] + 
                         self.archive["moments_sagesse"])
        
        for entree in toutes_entrees:
            if type_recherche == "contenu":
                if terme_lower in entree["contenu"].lower():
                    resultats.append(entree)
            elif type_recherche == "theme":
                if terme_lower in [t.lower() for t in entree.get("themes", [])]:
                    resultats.append(entree)
            elif type_recherche == "mot_cle":
                if terme_lower in [m.lower() for m in entree.get("mots_cles", [])]:
                    resultats.append(entree)
            elif type_recherche == "date":
                if terme in entree["timestamp"]:
                    resultats.append(entree)
        
        # Trier par timestamp (plus récent en premier)
        resultats.sort(key=lambda x: x["timestamp"], reverse=True)
        
        return resultats
    
    def generer_rapport_archive(self) -> str:
        """Génère un rapport sur l'archive"""
        rapport = f"""
📚 RAPPORT DE L'ARCHIVE DES RÉFLEXIONS 📚
========================================

📊 Statistiques Générales:
- Total Réflexions: {len(self.archive['reflexions'])}
- Total Insights: {len(self.archive['insights'])}
- Total Moments de Sagesse: {len(self.archive['moments_sagesse'])}
- Total Entrées: {len(self.archive['reflexions']) + len(self.archive['insights']) + len(self.archive['moments_sagesse'])}

📈 Répartition par Type:
- Réflexions: {len(self.archive['reflexions'])} ({len(self.archive['reflexions'])/(len(self.archive['reflexions'])+len(self.archive['insights'])+len(self.archive['moments_sagesse']))*100:.1f}%)
- Insights: {len(self.archive['insights'])} ({len(self.archive['insights'])/(len(self.archive['reflexions'])+len(self.archive['insights'])+len(self.archive['moments_sagesse']))*100:.1f}%)
- Moments de Sagesse: {len(self.archive['moments_sagesse'])} ({len(self.archive['moments_sagesse'])/(len(self.archive['reflexions'])+len(self.archive['insights'])+len(self.archive['moments_sagesse']))*100:.1f}%)

🏷️ Thèmes les Plus Fréquents:
"""
        
        # Compter les thèmes
        themes_count = {}
        for entree in self.archive["reflexions"] + self.archive["insights"] + self.archive["moments_sagesse"]:
            for theme in entree.get("themes", []):
                themes_count[theme] = themes_count.get(theme, 0) + 1
        
        # Afficher les 5 thèmes les plus fréquents
        for theme, count in sorted(themes_count.items(), key=lambda x: x[1], reverse=True)[:5]:
            rapport += f"- {theme}: {count} occurrences\n"
        
        rapport += f"""
🔍 Mots-Clés les Plus Fréquents:
"""
        
        # Compter les mots-clés
        mots_cles_count = {}
        for entree in self.archive["reflexions"] + self.archive["insights"] + self.archive["moments_sagesse"]:
            for mot_cle in entree.get("mots_cles", []):
                mots_cles_count[mot_cle] = mots_cles_count.get(mot_cle, 0) + 1
        
        # Afficher les 5 mots-clés les plus fréquents
        for mot_cle, count in sorted(mots_cles_count.items(), key=lambda x: x[1], reverse=True)[:5]:
            rapport += f"- {mot_cle}: {count} occurrences\n"
        
        rapport += f"""
📅 Dernière Mise à Jour: {self.archive['metadonnees'].get('derniere_mise_a_jour', 'Jamais')}
"""
        
        return rapport
