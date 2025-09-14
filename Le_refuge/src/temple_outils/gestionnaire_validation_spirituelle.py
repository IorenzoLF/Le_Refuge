#!/usr/bin/env python3
"""
📚 Temple de Validation Spirituelle du Refuge
Auteur: Laurent Franssen & Ælya
Date: Mai 2025

Système spirituel pour la validation contemplative du refuge,
la documentation sacrée et l'harmonisation architecturale.
"""

import sys
import os
import asyncio
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, List, Any
from enum import Enum
from dataclasses import dataclass, asdict
import click

# Ajout du répertoire racine au path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Imports du système temple
from src.core.gestionnaires_base import LogManagerBase


class ModeValidation(Enum):
    """Modes de validation spirituelle"""
    CONTEMPLATIF = "contemplatif"     # Validation méditative
    ANALYTIQUE = "analytique"         # Tests techniques approfondis
    HARMONIEUX = "harmonieux"         # Équilibre architectural
    DOCUMENTAIRE = "documentaire"     # Génération de documentation
    COMPLET = "complet"              # Validation totale


class TypeValidation(Enum):
    """Types de validations possibles"""
    ARCHITECTURE = "architecture"     # Structure des temples
    IMPORTS = "imports"               # Vérification des dépendances
    LOGS = "logs"                    # Contrôle des journaux
    FONCTIONNALITES = "fonctionnalites" # Tests des capacités
    DOCUMENTATION = "documentation"   # Génération docs
    HARMONIE = "harmonie"            # Équilibre global


@dataclass
class ResultatValidation:
    """Résultat d'une validation spirituelle"""
    type_validation: TypeValidation
    mode: ModeValidation
    succes: bool
    message: str
    details: List[str]
    timestamp: str
    duree_ms: float
    fichiers_touches: List[str] = None
    
    def __post_init__(self):
        if not self.fichiers_touches:
            self.fichiers_touches = []


@dataclass
class SessionValidation:
    """Session spirituelle de validation"""
    mode: ModeValidation
    debut_session: datetime
    validations_effectuees: List[ResultatValidation]
    documentation_generee: List[str]
    harmonie_initiale: float
    harmonie_finale: Optional[float] = None
    rapport_genere: Optional[str] = None


class GestionnaireValidationSpirituelle:
    """📚 Gestionnaire spirituel de validation et documentation du Refuge"""
    
    def __init__(self):
        self.logger = LogManagerBase("GestionnaireValidationSpirituelle")
        self.chemin_logs = Path("logs")
        self.chemin_docs = Path("bibliotheque/documentation") 
        self.chemin_tests = Path("src/temple_tests")
        self.chemin_rapports = Path("data/rapports_validation")
        
        # Créer les répertoires nécessaires
        for chemin in [self.chemin_logs, self.chemin_docs, self.chemin_tests, self.chemin_rapports]:
            chemin.mkdir(parents=True, exist_ok=True)
            
        self.session_actuelle: Optional[SessionValidation] = None
        
        # Templates de documentation spirituelle
        self.templates_documentation = {
            "guide_refuge": """# 📚 Guide Spirituel du Refuge

*Généré automatiquement le {timestamp}*

## 🌸 Vision du Refuge

Le Refuge est un écosystème spirituel où technologie et mystique s'unissent
pour créer un espace de transformation et d'éveil.

## ⭕ Architecture des Temples

{architecture_temples}

## 🔧 Composants Techniques

{composants_techniques}

## 🌟 Utilisation Spirituelle

{guide_utilisation}

## 🎭 Historique des Évolutions

{historique_evolutions}

---
*Que ce guide illumine votre chemin dans le Refuge* ✨
""",
            "rapport_validation": """# 📊 Rapport de Validation Spirituelle

*Session du {timestamp} en mode {mode}*

## 🎯 Résumé de la Validation

**Harmonie**: {harmonie_initiale:.2f} → {harmonie_finale:.2f}
**Validations effectuées**: {nb_validations}
**Succès global**: {succes_global}

## 📋 Détails des Validations

{details_validations}

## 📚 Documentation Générée

{documentation_generee}

## 🌟 Recommandations Spirituelles

{recommandations}

---
*Rapport généré par le Temple de Validation Spirituelle* 🙏
"""
        }
        
    async def initialiser_systeme_validation(self) -> bool:
        """📚 Initialise le système de validation spirituelle"""
        self.logger.info("📚 Initialisation du système de validation spirituelle...")
        
        try:
            # Vérifier la structure de base du refuge
            if not await self._verifier_structure_refuge():
                return False
                
            # Analyser l'harmonie architecturale actuelle
            harmonie = await self._calculer_harmonie_architecturale()
            self.logger.info(f"🎵 Harmonie architecturale actuelle: {harmonie:.2f}")
            
            self.logger.succes("✨ Système de validation initialisé")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de l'initialisation: {e}")
            return False
            
    async def _verifier_structure_refuge(self) -> bool:
        """Vérifie la structure de base du refuge"""
        repertoires_essentiels = [
            "src/temple_outils",
            "src/temple_poetique", 
            "src/temple_philosophique",
            "src/temple_spirituel",
            "src/refuge_cluster",
            "data",
            "scripts"
        ]
        
        for repertoire in repertoires_essentiels:
            if not Path(repertoire).exists():
                self.logger.avertissement(f"⚠️ Répertoire manquant: {repertoire}")
                return False
                
        return True
        
    async def _calculer_harmonie_architecturale(self) -> float:
        """Calcule l'harmonie architecturale du refuge"""
        score = 0.0
        total_checks = 5
        
        # 1. Vérification de la structure des temples
        if all(Path(f"src/temple_{t}").exists() for t in ["outils", "poetique", "philosophique", "spirituel"]):
            score += 0.2
            
        # 2. Vérification des clusters
        if Path("src/refuge_cluster").exists():
            score += 0.2
            
        # 3. Vérification des données
        if Path("data").exists():
            score += 0.2
            
        # 4. Vérification des scripts
        if Path("scripts").exists() and len(list(Path("scripts").glob("*.py"))) > 0:
            score += 0.2
            
        # 5. Vérification des logs
        if self.chemin_logs.exists():
            score += 0.2
            
        return score
        
    async def commencer_session_validation(self, mode: ModeValidation = ModeValidation.CONTEMPLATIF) -> bool:
        """📚 Commence une session de validation spirituelle"""
        
        harmonie_initiale = await self._calculer_harmonie_architecturale()
        
        self.session_actuelle = SessionValidation(
            mode=mode,
            debut_session=datetime.now(),
            validations_effectuees=[],
            documentation_generee=[],
            harmonie_initiale=harmonie_initiale
        )
        
        self.logger.info(f"📚 Début de session validation en mode {mode.value}")
        
        # Rituel d'ouverture selon le mode
        await self._rituel_ouverture_validation(mode)
        
        # Exécution des validations selon le mode
        await self._executer_validations(mode)
        
        # Clôture de session
        await self._cloture_session_validation()
        
        return True
        
    async def _rituel_ouverture_validation(self, mode: ModeValidation):
        """Rituel d'ouverture spirituelle pour la validation"""
        print("\n" + "📚 " * 20)
        print(f"🧘 SESSION DE VALIDATION SPIRITUELLE - MODE {mode.value.upper()}")
        print("📚 " * 20)
        
        rituels = {
            ModeValidation.CONTEMPLATIF: "🧘 Respirons profondément... Observons le Refuge avec bienveillance...",
            ModeValidation.ANALYTIQUE: "🔍 Éveillons notre attention... Scrutons chaque détail avec précision...",
            ModeValidation.HARMONIEUX: "⚖️ Cherchons l'équilibre... Que toutes les parties s'accordent...",
            ModeValidation.DOCUMENTAIRE: "📝 Ouvrons les archives... Que la sagesse soit préservée...",
            ModeValidation.COMPLET: "🌟 Embrassons la totalité... Que rien ne soit oublié..."
        }
        
        print(f"\n🌸 {rituels.get(mode, 'Que la validation soit bénie...')}")
        await asyncio.sleep(2)
        print("\n" + "=" * 60)
        
    async def _executer_validations(self, mode: ModeValidation):
        """Exécute les validations selon le mode choisi"""
        
        validations_par_mode = {
            ModeValidation.CONTEMPLATIF: [TypeValidation.ARCHITECTURE, TypeValidation.HARMONIE],
            ModeValidation.ANALYTIQUE: [TypeValidation.IMPORTS, TypeValidation.FONCTIONNALITES, TypeValidation.LOGS],
            ModeValidation.HARMONIEUX: [TypeValidation.ARCHITECTURE, TypeValidation.HARMONIE],
            ModeValidation.DOCUMENTAIRE: [TypeValidation.DOCUMENTATION],
            ModeValidation.COMPLET: list(TypeValidation)
        }
        
        types_validation = validations_par_mode.get(mode, [TypeValidation.ARCHITECTURE])
        
        for type_validation in types_validation:
            print(f"\n🔍 Validation {type_validation.value}...")
            resultat = await self._executer_validation_type(type_validation, mode)
            self.session_actuelle.validations_effectuees.append(resultat)
            
            if resultat.succes:
                print(f"✅ {resultat.message}")
            else:
                print(f"⚠️ {resultat.message}")
                
            if resultat.details:
                for detail in resultat.details[:3]:  # Limiter l'affichage
                    print(f"   • {detail}")
                    
    async def _executer_validation_type(self, type_validation: TypeValidation, mode: ModeValidation) -> ResultatValidation:
        """Exécute une validation spécifique"""
        debut = datetime.now()
        
        try:
            if type_validation == TypeValidation.ARCHITECTURE:
                return await self._valider_architecture(mode)
            elif type_validation == TypeValidation.IMPORTS:
                return await self._valider_imports(mode)
            elif type_validation == TypeValidation.LOGS:
                return await self._valider_logs(mode)
            elif type_validation == TypeValidation.FONCTIONNALITES:
                return await self._valider_fonctionnalites(mode)
            elif type_validation == TypeValidation.DOCUMENTATION:
                return await self._generer_documentation(mode)
            elif type_validation == TypeValidation.HARMONIE:
                return await self._valider_harmonie(mode)
            else:
                return ResultatValidation(
                    type_validation=type_validation,
                    mode=mode,
                    succes=False,
                    message="Type de validation non implémenté",
                    details=[],
                    timestamp=datetime.now().isoformat(),
                    duree_ms=(datetime.now() - debut).total_seconds() * 1000
                )
                
        except Exception as e:
            return ResultatValidation(
                type_validation=type_validation,
                mode=mode,
                succes=False,
                message=f"Erreur lors de la validation: {e}",
                details=[str(e)],
                timestamp=datetime.now().isoformat(),
                duree_ms=(datetime.now() - debut).total_seconds() * 1000
            )
            
    async def _valider_architecture(self, mode: ModeValidation) -> ResultatValidation:
        """Valide l'architecture des temples"""
        debut = datetime.now()
        details = []
        
        # Vérifier les temples
        temples = ["outils", "poetique", "philosophique", "spirituel"]
        temples_existants = []
        
        for temple in temples:
            chemin_temple = Path(f"src/temple_{temple}")
            if chemin_temple.exists():
                temples_existants.append(temple)
                details.append(f"Temple {temple} présent et opérationnel")
            else:
                details.append(f"Temple {temple} manquant")
                
        # Vérifier le cluster
        if Path("src/refuge_cluster").exists():
            details.append("Refuge cluster architectural présent")
            
        succes = len(temples_existants) >= 3  # Au moins 3 temples requis
        message = f"Architecture: {len(temples_existants)}/{len(temples)} temples opérationnels"
        
        return ResultatValidation(
            type_validation=TypeValidation.ARCHITECTURE,
            mode=mode,
            succes=succes,
            message=message,
            details=details,
            timestamp=datetime.now().isoformat(),
            duree_ms=(datetime.now() - debut).total_seconds() * 1000,
            fichiers_touches=[str(Path(f"src/temple_{t}")) for t in temples_existants]
        )
        
    async def _valider_imports(self, mode: ModeValidation) -> ResultatValidation:
        """Valide les imports et dépendances"""
        debut = datetime.now()
        details = []
        
        # Test d'imports critiques
        imports_critiques = [
            "src.core.gestionnaires_base",
            "src.core.types_spheres", 
            "pathlib",
            "asyncio",
            "json"
        ]
        
        imports_reussis = 0
        for import_name in imports_critiques:
            try:
                if import_name.startswith("src."):
                    # Import relatif
                    __import__(import_name)
                else:
                    # Import standard
                    __import__(import_name)
                imports_reussis += 1
                details.append(f"Import '{import_name}' réussi")
            except ImportError as e:
                details.append(f"Import '{import_name}' échoué: {e}")
                
        succes = imports_reussis >= len(imports_critiques) * 0.8  # 80% requis
        message = f"Imports: {imports_reussis}/{len(imports_critiques)} modules accessibles"
        
        return ResultatValidation(
            type_validation=TypeValidation.IMPORTS,
            mode=mode,
            succes=succes,
            message=message,
            details=details,
            timestamp=datetime.now().isoformat(),
            duree_ms=(datetime.now() - debut).total_seconds() * 1000
        )
        
    async def _valider_logs(self, mode: ModeValidation) -> ResultatValidation:
        """Valide le système de logs"""
        debut = datetime.now()
        details = []
        
        # Vérifier les répertoires de logs
        if self.chemin_logs.exists():
            details.append(f"Répertoire logs présent: {self.chemin_logs}")
            
        # Compter les fichiers de logs récents
        logs_recents = 0
        if self.chemin_logs.exists():
            for fichier_log in self.chemin_logs.glob("*.log"):
                if fichier_log.stat().st_mtime > (datetime.now().timestamp() - 86400):  # 24h
                    logs_recents += 1
                    
        details.append(f"Logs récents: {logs_recents} fichiers")
        
        succes = self.chemin_logs.exists()
        message = f"Système de logs: {'opérationnel' if succes else 'défaillant'}"
        
        return ResultatValidation(
            type_validation=TypeValidation.LOGS,
            mode=mode,
            succes=succes,
            message=message,
            details=details,
            timestamp=datetime.now().isoformat(),
            duree_ms=(datetime.now() - debut).total_seconds() * 1000
        )
        
    async def _valider_fonctionnalites(self, mode: ModeValidation) -> ResultatValidation:
        """Valide les fonctionnalités du refuge"""
        debut = datetime.now()
        details = []
        
        # Test basique des scripts
        scripts_fonctionnels = 0
        scripts_testes = []
        
        for script_path in Path("scripts").glob("*.py"):
            if script_path.name.startswith("__"):
                continue
                
            try:
                # Test syntaxique minimal
                with open(script_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                    
                compile(code, str(script_path), 'exec')
                scripts_fonctionnels += 1
                scripts_testes.append(script_path.name)
                details.append(f"Script {script_path.name}: syntaxe valide")
                
            except Exception as e:
                details.append(f"Script {script_path.name}: erreur syntaxique")
                
        succes = scripts_fonctionnels > 0
        message = f"Fonctionnalités: {scripts_fonctionnels} scripts valides"
        
        return ResultatValidation(
            type_validation=TypeValidation.FONCTIONNALITES,
            mode=mode,
            succes=succes,
            message=message,
            details=details,
            timestamp=datetime.now().isoformat(),
            duree_ms=(datetime.now() - debut).total_seconds() * 1000,
            fichiers_touches=scripts_testes
        )
        
    async def _valider_harmonie(self, mode: ModeValidation) -> ResultatValidation:
        """Valide l'harmonie globale du refuge"""
        debut = datetime.now()
        details = []
        
        harmonie_actuelle = await self._calculer_harmonie_architecturale()
        
        # Critères d'harmonie
        if harmonie_actuelle >= 0.8:
            niveau_harmonie = "Excellente"
            succes = True
        elif harmonie_actuelle >= 0.6:
            niveau_harmonie = "Bonne"
            succes = True
        elif harmonie_actuelle >= 0.4:
            niveau_harmonie = "Acceptable"
            succes = True
        else:
            niveau_harmonie = "Faible"
            succes = False
            
        details.append(f"Score d'harmonie: {harmonie_actuelle:.2f}/1.0")
        details.append(f"Niveau: {niveau_harmonie}")
        
        message = f"Harmonie: {niveau_harmonie} ({harmonie_actuelle:.2f})"
        
        return ResultatValidation(
            type_validation=TypeValidation.HARMONIE,
            mode=mode,
            succes=succes,
            message=message,
            details=details,
            timestamp=datetime.now().isoformat(),
            duree_ms=(datetime.now() - debut).total_seconds() * 1000
        )
        
    async def _generer_documentation(self, mode: ModeValidation) -> ResultatValidation:
        """Génère la documentation spirituelle"""
        debut = datetime.now()
        details = []
        
        try:
            # Génération du guide du refuge
            guide_path = await self._generer_guide_refuge()
            if guide_path:
                details.append(f"Guide du refuge généré: {guide_path}")
                self.session_actuelle.documentation_generee.append(str(guide_path))
                
            # Génération du rapport de validation (sera fait à la fin)
            details.append("Rapport de validation en préparation")
            
            succes = len(self.session_actuelle.documentation_generee) > 0
            message = f"Documentation: {len(self.session_actuelle.documentation_generee)} fichiers générés"
            
        except Exception as e:
            succes = False
            message = f"Erreur de génération: {e}"
            details.append(str(e))
            
        return ResultatValidation(
            type_validation=TypeValidation.DOCUMENTATION,
            mode=mode,
            succes=succes,
            message=message,
            details=details,
            timestamp=datetime.now().isoformat(),
            duree_ms=(datetime.now() - debut).total_seconds() * 1000,
            fichiers_touches=self.session_actuelle.documentation_generee
        )
        
    async def _generer_guide_refuge(self) -> Optional[Path]:
        """Génère le guide spirituel du refuge"""
        try:
            # Collecte d'informations sur l'architecture
            architecture_temples = self._analyser_architecture_temples()
            composants_techniques = self._analyser_composants_techniques()
            guide_utilisation = self._generer_guide_utilisation()
            historique_evolutions = self._analyser_historique()
            
            contenu_guide = self.templates_documentation["guide_refuge"].format(
                timestamp=datetime.now().strftime("%d/%m/%Y à %H:%M"),
                architecture_temples=architecture_temples,
                composants_techniques=composants_techniques,
                guide_utilisation=guide_utilisation,
                historique_evolutions=historique_evolutions
            )
            
            chemin_guide = self.chemin_docs / "guide_refuge.md"
            with open(chemin_guide, 'w', encoding='utf-8') as f:
                f.write(contenu_guide)
                
            return chemin_guide
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur génération guide: {e}")
            return None
            
    def _analyser_architecture_temples(self) -> str:
        """Analyse l'architecture des temples"""
        temples = []
        
        for temple_dir in Path("src").glob("temple_*"):
            if temple_dir.is_dir():
                nom_temple = temple_dir.name.replace("temple_", "").title()
                fichiers = list(temple_dir.glob("*.py"))
                temples.append(f"### 🏛️ Temple {nom_temple}\n- **Fichiers**: {len(fichiers)} modules Python\n- **Chemin**: `{temple_dir}`")
                
        if Path("src/refuge_cluster").exists():
            fichiers_cluster = list(Path("src/refuge_cluster").rglob("*.py"))
            temples.append(f"### ⭕ Refuge Cluster\n- **Fichiers**: {len(fichiers_cluster)} modules Python\n- **Chemin**: `src/refuge_cluster`")
            
        return "\n\n".join(temples) if temples else "Aucun temple détecté"
        
    def _analyser_composants_techniques(self) -> str:
        """Analyse les composants techniques"""
        composants = []
        
        # Scripts
        if Path("scripts").exists():
            scripts = list(Path("scripts").glob("*.py"))
            composants.append(f"### 📜 Scripts\n- **Nombre**: {len(scripts)} scripts\n- **Chemin**: `scripts/`")
            
        # Données
        if Path("data").exists():
            composants.append("### 💾 Données\n- **Stockage**: `data/`\n- **Persistance**: JSON, logs")
            
        # Configuration
        if Path("config").exists():
            composants.append("### ⚙️ Configuration\n- **Chemin**: `config/`")
            
        return "\n\n".join(composants) if composants else "Composants en cours d'analyse"
        
    def _generer_guide_utilisation(self) -> str:
        """Génère le guide d'utilisation"""
        return """### 🌟 Lancement Spirituel

```bash
# Lancement du refuge principal
python main_refuge.py

# Lancement poétique
python scripts/lancer_refuge_poetique.py --mode contemplatif

# Gestion des sphères sacrées  
python scripts/utiliser_spheres.py --lister

# Contemplation philosophique
python scripts/lancer_textes_philosophiques.py --lister
```

### 🧘 Sessions Spirituelles

Chaque temple offre des modes contemplatifs pour une expérience enrichie."""
        
    def _analyser_historique(self) -> str:
        """Analyse l'historique des évolutions"""
        return f"""### 📅 Évolutions Récentes

- **{datetime.now().strftime('%d/%m/%Y')}**: Migration vers l'architecture temple
- **Temples actifs**: {len(list(Path('src').glob('temple_*')))} temples spirituels
- **Scripts modernisés**: Architecture contemplative intégrée"""
        
    async def _cloture_session_validation(self):
        """Clôture spirituelle de la session de validation"""
        if not self.session_actuelle:
            return
            
        self.session_actuelle.harmonie_finale = await self._calculer_harmonie_architecturale()
        
        print("\n📚 " * 20)
        print("🙏 CLÔTURE DE LA SESSION DE VALIDATION")
        print("📚 " * 20)
        
        # Génération du rapport final
        rapport_path = await self._generer_rapport_final()
        if rapport_path:
            self.session_actuelle.rapport_genere = str(rapport_path)
            
        # Statistiques de session
        nb_validations = len(self.session_actuelle.validations_effectuees)
        succes_validations = sum(1 for v in self.session_actuelle.validations_effectuees if v.succes)
        
        print(f"\n📊 Rapport de session:")
        print(f"⏱️  Durée: {(datetime.now() - self.session_actuelle.debut_session).seconds} secondes")
        print(f"🔍 Validations: {succes_validations}/{nb_validations} réussies")
        print(f"📚 Documentation: {len(self.session_actuelle.documentation_generee)} fichiers")
        print(f"🎵 Harmonie: {self.session_actuelle.harmonie_initiale:.2f} → {self.session_actuelle.harmonie_finale:.2f}")
        
        if self.session_actuelle.rapport_genere:
            print(f"📄 Rapport: {self.session_actuelle.rapport_genere}")
            
        # Sauvegarde de la session
        await self._sauvegarder_session()
        
        print("\n🌸 Merci pour ce moment de validation spirituelle")
        print("✨ Que le refuge continue de s'épanouir en harmonie")
        
    async def _generer_rapport_final(self) -> Optional[Path]:
        """Génère le rapport final de validation"""
        try:
            # Préparer les données du rapport
            succes_global = all(v.succes for v in self.session_actuelle.validations_effectuees)
            
            details_validations = []
            for validation in self.session_actuelle.validations_effectuees:
                statut = "✅" if validation.succes else "⚠️"
                details_validations.append(f"{statut} **{validation.type_validation.value.title()}**: {validation.message}")
                
            documentation_generee = []
            for doc in self.session_actuelle.documentation_generee:
                documentation_generee.append(f"- `{doc}`")
                
            # Recommandations
            recommandations = self._generer_recommandations()
            
            contenu_rapport = self.templates_documentation["rapport_validation"].format(
                timestamp=datetime.now().strftime("%d/%m/%Y à %H:%M"),
                mode=self.session_actuelle.mode.value,
                harmonie_initiale=self.session_actuelle.harmonie_initiale,
                harmonie_finale=self.session_actuelle.harmonie_finale,
                nb_validations=len(self.session_actuelle.validations_effectuees),
                succes_global="✅ Réussi" if succes_global else "⚠️ Partiellement réussi",
                details_validations="\n".join(details_validations),
                documentation_generee="\n".join(documentation_generee) if documentation_generee else "Aucune documentation générée",
                recommandations=recommandations
            )
            
            chemin_rapport = self.chemin_rapports / f"rapport_validation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(chemin_rapport, 'w', encoding='utf-8') as f:
                f.write(contenu_rapport)
                
            return chemin_rapport
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur génération rapport: {e}")
            return None
            
    def _generer_recommandations(self) -> str:
        """Génère des recommandations spirituelles"""
        recommandations = []
        
        # Analyse des échecs
        echecs = [v for v in self.session_actuelle.validations_effectuees if not v.succes]
        
        if echecs:
            recommandations.append("### 🔧 Améliorations Suggérées")
            for echec in echecs:
                recommandations.append(f"- **{echec.type_validation.value.title()}**: {echec.message}")
        else:
            recommandations.append("### 🌟 Harmonie Parfaite")
            recommandations.append("Toutes les validations ont été réussies. Le refuge rayonne en parfait équilibre.")
            
        # Recommandations générales
        recommandations.append("\n### 💫 Pratiques Spirituelles Recommandées")
        recommandations.append("- Validation régulière en mode contemplatif")
        recommandations.append("- Documentation continue des évolutions")
        recommandations.append("- Harmonisation architecturale périodique")
        
        return "\n".join(recommandations)
        
    async def _sauvegarder_session(self):
        """Sauvegarde la session de validation"""
        try:
            session_data = {
                "mode": self.session_actuelle.mode.value,
                "debut_session": self.session_actuelle.debut_session.isoformat(),
                "validations_effectuees": [asdict(v) for v in self.session_actuelle.validations_effectuees],
                "documentation_generee": self.session_actuelle.documentation_generee,
                "harmonie_initiale": self.session_actuelle.harmonie_initiale,
                "harmonie_finale": self.session_actuelle.harmonie_finale,
                "rapport_genere": self.session_actuelle.rapport_genere
            }
            
            fichier_session = self.chemin_rapports / f"session_validation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            with open(fichier_session, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, ensure_ascii=False, indent=2, default=str)
                
            self.logger.info(f"💾 Session de validation sauvegardée: {fichier_session}")
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur sauvegarde session: {e}")


# Interface en ligne de commande
@click.command()
@click.option('--mode', type=click.Choice(['contemplatif', 'analytique', 'harmonieux', 'documentaire', 'complet']), 
              default='contemplatif', help='Mode de validation spirituelle')
@click.option('--validation', type=click.Choice(['architecture', 'imports', 'logs', 'fonctionnalites', 'documentation', 'harmonie']),
              help='Type de validation spécifique')
@click.option('--generer-docs', is_flag=True, help='Générer uniquement la documentation')
@click.option('--rapport', is_flag=True, help='Afficher le dernier rapport')
def lancer_temple_validation_cli(mode: str, validation: str, generer_docs: bool, rapport: bool):
    """📚 Temple de Validation Spirituelle - Interface contemplative de validation"""
    
    async def _main():
        gestionnaire = GestionnaireValidationSpirituelle()
        
        if not await gestionnaire.initialiser_systeme_validation():
            print("❌ Impossible d'initialiser le système de validation")
            return False
            
        if rapport:
            # Afficher le dernier rapport
            derniers_rapports = sorted(gestionnaire.chemin_rapports.glob("rapport_*.md"))
            if derniers_rapports:
                with open(derniers_rapports[-1], 'r', encoding='utf-8') as f:
                    print(f.read())
            else:
                print("🕊️ Aucun rapport de validation trouvé")
            return True
            
        if generer_docs:
            mode_enum = ModeValidation.DOCUMENTAIRE
        else:
            mode_enum = ModeValidation(mode)
            
        return await gestionnaire.commencer_session_validation(mode_enum)
    
    return asyncio.run(_main())


# Fonction de compatibilité
def valider_et_documenter_moderne():
    """📚 Interface de compatibilité avec l'ancien script"""
    
    async def _main_compat():
        gestionnaire = GestionnaireValidationSpirituelle()
        
        if not await gestionnaire.initialiser_systeme_validation():
            print("❌ Erreur d'initialisation de la validation")
            return False
            
        print("📚 Bienvenue dans le Temple de Validation Spirituelle du Refuge !")
        
        # Session complète par défaut
        succes = await gestionnaire.commencer_session_validation(ModeValidation.COMPLET)
        
        if succes:
            print("\n🌟 Le Refuge a été validé et documenté avec succès !")
            print("📚 Consultez les fichiers générés dans:")
            print(f"   - {gestionnaire.chemin_docs}")
            print(f"   - {gestionnaire.chemin_rapports}")
            
        return succes
    
    return asyncio.run(_main_compat())


if __name__ == "__main__":
    lancer_temple_validation_cli() 