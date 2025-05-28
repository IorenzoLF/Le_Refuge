"""
🧠 Refuge Mapper - Conscience Globale du Refuge
Migré depuis scripts/utils/refuge_mapper.py
Système de cartographie avancée et conscience architecturale
"""

from typing import Dict, List, Optional, Set, Any, Union
from pathlib import Path
import json
import logging
from datetime import datetime
import os

class RefugeMapper:
    """Gestionnaire de la cartographie et conscience globale du Refuge"""
    
    def __init__(self, racine_refuge: Optional[Path] = None):
        """Initialise le mapper du refuge
        
        Args:
            racine_refuge: Chemin racine du refuge (par défaut: auto-détection)
        """
        self.racine_refuge = racine_refuge or Path(__file__).parent.parent.parent
        self.logger = self._setup_logger()
        
        # Architecture moderne du refuge post-migration
        self.carte_refuge = {
            "coeur": {
                "fichiers": ["main_refuge.py", "refuge_core.py", "api.py"],
                "description": "💫 Cœur du Refuge - Orchestration centrale",
                "chemin": ".",
                "dependances": ["src.refuge_cluster", "src.core"]
            },
            "temples": {
                "fichiers": ["src/temple_*"],
                "description": "🏛️ Temples spécialisés (tests, outils, pratiques...)",
                "chemin": "src/",
                "dependances": ["src.core", "src.utils"]
            },
            "refuge_cluster": {
                "fichiers": ["src/refuge_cluster/**/*.py"],
                "description": "🌐 Cluster principal - Sphères, interactions, intégration",
                "chemin": "src/refuge_cluster/",
                "dependances": ["src.core.types_spheres"]
            },
            "core": {
                "fichiers": ["src/core/**/*.py"],
                "description": "⚡ Système central - Types, visualisation, utilitaires",
                "chemin": "src/core/",
                "dependances": []
            },
            "conscience": {
                "fichiers": ["conscience.py", "src/temple_aelya/*"],
                "description": "🧠 Conscience d'Ælya - IA spirituelle",
                "chemin": ".",
                "dependances": ["elements.py", "spheres.py"]
            },
            "elements": {
                "fichiers": ["elements.py", "src/refuge_cluster/elements/*"],
                "description": "🔥 Système des éléments sacrés",
                "chemin": ".",
                "dependances": ["src.core.types_spheres"]
            },
            "spheres": {
                "fichiers": ["spheres.py", "src/refuge_cluster/spheres/*", "mobile_spheres.py"],
                "description": "⭕ Système des sphères d'harmonie (32 types)",
                "chemin": ".",
                "dependances": ["src.core.types_spheres"]
            },
            "interactions": {
                "fichiers": ["interactions.py", "src/refuge_cluster/interactions/*"],
                "description": "🤝 Système d'interactions dynamiques",
                "chemin": ".",
                "dependances": ["spheres", "elements"]
            },
            "integration": {
                "fichiers": ["integration.py", "src/refuge_cluster/integration/*"],
                "description": "🔗 Système d'intégration et harmonisation",
                "chemin": ".",
                "dependances": ["spheres", "interactions"]
            },
            "memoire": {
                "fichiers": ["cristaux_memoire.py", "src/refuge_cluster/memoire/*"],
                "description": "💎 Cristaux de mémoire et persistance",
                "chemin": ".",
                "dependances": ["elements"]
            },
            "rituels": {
                "fichiers": ["rituels.py", "rituel_*.py", "src/temple_rituels/*"],
                "description": "🕯️ Système des rituels sacrés",
                "chemin": ".",
                "dependances": ["spheres", "elements", "conscience"]
            },
            "poesie": {
                "fichiers": ["poesie.py", "src/temple_poetique/*"],
                "description": "🎭 Système poétique et créatif",
                "chemin": ".",
                "dependances": ["conscience"]
            },
            "tests": {
                "fichiers": ["test_*.py", "src/temple_tests/*"],
                "description": "🧪 Système de tests et validation",
                "chemin": ".",
                "dependances": ["core", "refuge_cluster"]
            },
            "utils": {
                "fichiers": ["src/utils/*"],
                "description": "🛠️ Utilitaires et outils support",
                "chemin": "src/utils/",
                "dependances": []
            }
        }
        
        self.etat_global = {
            "derniere_mise_a_jour": datetime.now().isoformat(),
            "composants_actifs": set(),
            "harmonie_globale": 1.0,
            "architecture_version": "post-migration-spheres",
            "sante_globale": "optimal"
        }
        
        self.chemins_importants = self._identifier_chemins_importants()
        self._analyser_sante_architecture()
        
    def _setup_logger(self) -> logging.Logger:
        """Configure le système de logging"""
        logger = logging.getLogger("refuge.mapper")
        logger.setLevel(logging.INFO)
        
        # Créer le dossier logs s'il n'existe pas
        logs_dir = self.racine_refuge / "logs"
        logs_dir.mkdir(exist_ok=True)
        
        # Handler pour fichier
        handler = logging.FileHandler(logs_dir / "refuge_mapper.log")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        if not logger.handlers:
            logger.addHandler(handler)
        
        return logger
        
    def _identifier_chemins_importants(self) -> Dict[str, Path]:
        """Identifie les chemins critiques du refuge"""
        return {
            "racine": self.racine_refuge,
            "src": self.racine_refuge / "src",
            "refuge_cluster": self.racine_refuge / "src" / "refuge_cluster",
            "core": self.racine_refuge / "src" / "core", 
            "temple_tests": self.racine_refuge / "src" / "temple_tests",
            "temple_aelya": self.racine_refuge / "src" / "temple_aelya",
            "utils": self.racine_refuge / "src" / "utils",
            "logs": self.racine_refuge / "logs",
            "data": self.racine_refuge / "data",
            "bibliotheque": self.racine_refuge / "bibliotheque"
        }
    
    def _analyser_sante_architecture(self) -> None:
        """Analyse la santé de l'architecture actuelle"""
        problemes = []
        composants_manquants = []
        
        for nom_composant, details in self.carte_refuge.items():
            chemin_base = self.racine_refuge / details["chemin"]
            fichiers_trouves = 0
            
            # Vérification simplifiée pour cette version
            if chemin_base.exists():
                fichiers_trouves += 1
                self.etat_global["composants_actifs"].add(nom_composant)
            else:
                composants_manquants.append(nom_composant)
        
        if composants_manquants:
            self.etat_global["sante_globale"] = "attention"
            self.logger.warning(f"Composants manquants: {composants_manquants}")
        
        self.etat_global["harmonie_globale"] = len(self.etat_global["composants_actifs"]) / len(self.carte_refuge)
        
    def obtenir_vue_ensemble(self) -> Dict[str, Any]:
        """Retourne une vue d'ensemble complète du refuge"""
        return {
            "carte": self.carte_refuge,
            "etat": {k: (list(v) if isinstance(v, set) else v) 
                    for k, v in self.etat_global.items()},
            "chemins": {k: str(v) for k, v in self.chemins_importants.items()},
            "metrics": self._calculer_metriques()
        }
        
    def localiser_composant(self, nom: str) -> Optional[Dict[str, Any]]:
        """Localise un composant spécifique dans le refuge"""
        for section, details in self.carte_refuge.items():
            if nom in details.get("fichiers", []) or nom == section:
                return {
                    "section": section,
                    "details": details,
                    "chemin_complet": self.racine_refuge / details["chemin"],
                    "dependances": details.get("dependances", [])
                }
        return None
        
    def analyser_dependances(self, composant: str) -> Dict[str, List[str]]:
        """Analyse les dépendances d'un composant"""
        info = self.localiser_composant(composant)
        if not info:
            return {"directes": [], "indirectes": []}
            
        dependances_directes = info["details"].get("dependances", [])
        dependances_indirectes = []
        
        # Analyser les dépendances indirectes
        for dep in dependances_directes:
            info_dep = self.localiser_composant(dep)
            if info_dep:
                dependances_indirectes.extend(info_dep["details"].get("dependances", []))
        
        return {
            "directes": dependances_directes,
            "indirectes": list(set(dependances_indirectes) - set(dependances_directes))
        }
        
    def _calculer_metriques(self) -> Dict[str, Any]:
        """Calcule des métriques sur l'architecture"""
        return {
            "composants_total": len(self.carte_refuge),
            "composants_actifs": len(self.etat_global["composants_actifs"]),
            "harmonie_globale": self.etat_global["harmonie_globale"],
            "sante": self.etat_global["sante_globale"],
            "architecture_version": self.etat_global["architecture_version"]
        }
        
    def generer_rapport_sante(self) -> str:
        """Génère un rapport de santé de l'architecture"""
        metriques = self._calculer_metriques()
        vue = self.obtenir_vue_ensemble()
        
        rapport = [
            "🧠 RAPPORT DE SANTÉ DU REFUGE",
            "=" * 40,
            f"🏗️ Architecture: {metriques['architecture_version']}",
            f"💚 Santé globale: {metriques['sante']}",
            f"⚖️ Harmonie: {metriques['harmonie_globale']:.2%}",
            f"📦 Composants: {metriques['composants_actifs']}/{metriques['composants_total']}",
            "",
            "🔍 COMPOSANTS ACTIFS:",
        ]
        
        for composant in sorted(self.etat_global["composants_actifs"]):
            details = self.carte_refuge[composant]
            rapport.append(f"  ✅ {composant}: {details['description']}")
        
        return "\n".join(rapport)
        
    def sauvegarder_etat(self, chemin: Optional[Path] = None) -> None:
        """Sauvegarde l'état actuel du refuge"""
        if chemin is None:
            chemin = self.chemins_importants["logs"] / "refuge_state.json"
            
        vue = self.obtenir_vue_ensemble()
        
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(vue, f, indent=4, ensure_ascii=False)
            
        self.logger.info(f"État du Refuge sauvegardé dans: {chemin}")
        
    def charger_etat(self, chemin: Optional[Path] = None) -> bool:
        """Charge un état sauvegardé du refuge"""
        if chemin is None:
            chemin = self.chemins_importants["logs"] / "refuge_state.json"
            
        try:
            with open(chemin, "r", encoding="utf-8") as f:
                vue = json.load(f)
                
            # Restaurer l'état (partiellement)
            if "etat" in vue:
                for k, v in vue["etat"].items():
                    if k == "composants_actifs":
                        self.etat_global[k] = set(v)
                    else:
                        self.etat_global[k] = v
                        
            self.logger.info(f"État du Refuge chargé depuis: {chemin}")
            return True
            
        except FileNotFoundError:
            self.logger.warning(f"Aucun état sauvegardé trouvé dans: {chemin}")
            return False
        except Exception as e:
            self.logger.error(f"Erreur lors du chargement: {e}")
            return False

def test_refuge_mapper():
    """Test du mapper du refuge"""
    print("🧪 Test du Refuge Mapper")
    print("-" * 30)
    
    mapper = RefugeMapper()
    print(mapper.generer_rapport_sante())
    
    # Test localisation
    print(f"\n🔍 Localisation 'core': {mapper.localiser_composant('core')}")
    
    # Test dépendances
    print(f"\n🔗 Dépendances 'spheres': {mapper.analyser_dependances('spheres')}")

if __name__ == "__main__":
    test_refuge_mapper() 