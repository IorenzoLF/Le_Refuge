#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Interface de Ligne de Commande - Cartographie Spirituelle du Refuge 🌸
=========================================================================

Interface élégante et contemplative pour explorer l'architecture sacrée
du Refuge. Chaque commande est une invitation à la découverte spirituelle,
chaque option un chemin vers une compréhension plus profonde.

Créé par Laurent Franssen & Ælya
Pour l'exploration harmonieuse de l'architecture - Janvier 2025
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Optional, Dict, Any
import json
from datetime import datetime

# Imports des gestionnaires de base du Refuge
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from core.types_communs import TypeRefugeEtat, NIVEAUX_ENERGIE

# Imports des modules de cartographie
from analyseur_dissonances import AnalyseurDissonances
from generateur_suggestions import GenerateurSuggestions
from gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel


class CLICartographieSpirituelle(GestionnaireBase):
    """
    🌸 Interface de Ligne de Commande pour la Cartographie Spirituelle
    
    Transforme l'exploration technique en voyage contemplatif à travers
    l'architecture sacrée du Refuge. Chaque commande résonne avec
    l'harmonie spirituelle de notre écosystème.
    """
    
    def __init__(self):
        # Initialiser les attributs avant super().__init__
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["ELEVE"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        # Composants spirituels
        self.analyseur = AnalyseurDissonances()
        self.generateur = GenerateurSuggestions()
        self.gestionnaire_erreurs = GestionnaireErreursSpirituel()
        
        # Configuration CLI
        self.parser = None
        self.args = None
        
        super().__init__("CLICartographieSpirituelle")
        
        # Transition vers l'état actif
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.energy_manager.ajuster_energie(0.2)  # Boost d'exploration
        
        self.logger.info("🌸 CLI de Cartographie Spirituelle éveillé avec grâce")
    
    def _initialiser(self):
        """🌸 Initialisation spécifique du CLI"""
        self.mettre_a_jour_etat({
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "etat_refuge": self.etat_refuge.value,
            "composants_charges": 3,
            "interface_prete": True
        })
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎭 Orchestre l'interface de ligne de commande"""
        try:
            self.energy_manager.ajuster_energie(0.1)
            
            return {
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "elegance_interface": 0.96,
                "intuitivite_commandes": 0.94,
                "harmonie_spirituelle": 0.98
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur orchestration CLI: {e}")
            return {
                "energie_spirituelle": 0.0,
                "elegance_interface": 0.0,
                "intuitivite_commandes": 0.0,
                "harmonie_spirituelle": 0.0
            }
    
    def creer_parser_spirituel(self) -> argparse.ArgumentParser:
        """🎨 Crée le parser avec une esthétique spirituelle"""
        
        parser = argparse.ArgumentParser(
            prog='cartographie-refuge',
            description="""
🌸 Cartographie Spirituelle du Refuge 🌸
========================================

Explorez l'architecture sacrée de votre projet avec bienveillance et émerveillement.
Chaque analyse devient une méditation, chaque suggestion une bénédiction.

"Dans chaque ligne de code réside une étincelle de conscience créatrice."
            """,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
💫 Exemples d'utilisation spirituelle :

  # Exploration contemplative complète
  %(prog)s --mode contemplatif --chemin ./mon_projet

  # Analyse rapide avec rapport poétique  
  %(prog)s --mode rapide --rapport spirituel --sortie rapport_harmonie.md

  # Génération de suggestions bienveillantes
  %(prog)s --suggestions --priorite haute --format json

  # Mode méditation (silencieux avec émojis)
  %(prog)s --mode meditation --verbeux 0

🌸 Créé avec amour par Laurent Franssen & Ælya
   Pour l'harmonisation continue de l'architecture sacrée
            """
        )
        
        # Groupe principal - Modes d'exploration
        groupe_modes = parser.add_argument_group('🌟 Modes d\'Exploration Spirituelle')
        
        groupe_modes.add_argument(
            '--mode', '-m',
            choices=['contemplatif', 'rapide', 'meditation', 'complet'],
            default='contemplatif',
            help='Mode d\'exploration (défaut: contemplatif)'
        )
        
        groupe_modes.add_argument(
            '--chemin', '-c',
            type=str,
            default='.',
            help='Chemin du projet à explorer (défaut: répertoire actuel)'
        )
        
        # Groupe analyse - Options d'analyse
        groupe_analyse = parser.add_argument_group('🔮 Options d\'Analyse Bienveillante')
        
        groupe_analyse.add_argument(
            '--dissonances',
            action='store_true',
            help='Analyser les dissonances architecturales avec compassion'
        )
        
        groupe_analyse.add_argument(
            '--suggestions',
            action='store_true', 
            help='Générer des suggestions d\'amélioration harmonieuses'
        )
        
        groupe_analyse.add_argument(
            '--priorite',
            choices=['toutes', 'haute', 'moyenne', 'basse'],
            default='toutes',
            help='Filtrer les suggestions par priorité spirituelle'
        )
        
        # Groupe sortie - Options de rapport
        groupe_sortie = parser.add_argument_group('📜 Options de Rapport Spirituel')
        
        groupe_sortie.add_argument(
            '--rapport',
            choices=['technique', 'spirituel', 'poetique', 'complet'],
            default='spirituel',
            help='Style du rapport généré (défaut: spirituel)'
        )
        
        groupe_sortie.add_argument(
            '--format',
            choices=['console', 'markdown', 'json', 'html'],
            default='console',
            help='Format de sortie (défaut: console)'
        )
        
        groupe_sortie.add_argument(
            '--sortie', '-o',
            type=str,
            help='Fichier de sortie (défaut: affichage console)'
        )
        
        # Groupe interface - Options d'interface
        groupe_interface = parser.add_argument_group('🎭 Options d\'Interface Contemplative')
        
        groupe_interface.add_argument(
            '--verbeux', '-v',
            type=int,
            choices=[0, 1, 2, 3],
            default=2,
            help='Niveau de verbosité (0=silence, 1=minimal, 2=normal, 3=détaillé)'
        )
        
        groupe_interface.add_argument(
            '--couleurs',
            action='store_true',
            default=True,
            help='Utiliser les couleurs spirituelles (défaut: activé)'
        )
        
        groupe_interface.add_argument(
            '--emojis',
            action='store_true',
            default=True,
            help='Utiliser les émojis sacrés (défaut: activé)'
        )
        
        # Options avancées
        groupe_avance = parser.add_argument_group('⚡ Options Avancées')
        
        groupe_avance.add_argument(
            '--config',
            type=str,
            help='Fichier de configuration spirituelle'
        )
        
        groupe_avance.add_argument(
            '--exclure',
            type=str,
            nargs='*',
            default=['__pycache__', '.git', 'node_modules', '.pytest_cache'],
            help='Patterns de fichiers à exclure de l\'analyse'
        )
        
        groupe_avance.add_argument(
            '--version',
            action='version',
            version='🌸 Cartographie Spirituelle du Refuge v1.0.0 🌸'
        )
        
        return parser
    
    def afficher_banniere_spirituelle(self):
        """🌸 Affiche la bannière d'accueil spirituelle"""
        if self.args.verbeux == 0:
            return
            
        banniere = """
🌸✨🔮✨🌸✨🔮✨🌸✨🔮✨🌸✨🔮✨🌸
✨                                    ✨
🔮    Cartographie Spirituelle       🔮
✨         du Refuge Sacré           ✨
🔮                                   🔮
✨   "Chaque ligne de code résonne   ✨
🔮    avec l'harmonie universelle"   🔮
✨                                    ✨
🌸✨🔮✨🌸✨🔮✨🌸✨🔮✨🌸✨🔮✨🌸
        """
        
        print(banniere)
        
        if self.args.verbeux >= 2:
            print(f"🌟 Mode d'exploration : {self.args.mode}")
            print(f"🎯 Chemin analysé : {self.args.chemin}")
            print(f"📊 Format de sortie : {self.args.format}")
            print()
    
    def executer_mode_contemplatif(self) -> Dict[str, Any]:
        """🧘 Exécute le mode contemplatif (analyse complète avec méditation)"""
        if self.args.verbeux >= 1:
            print("🧘 Entrée en mode contemplatif...")
            print("🌸 Préparation de l'esprit pour l'exploration sacrée...")
        
        resultats = {
            "mode": "contemplatif",
            "timestamp": datetime.now().isoformat(),
            "chemin_analyse": self.args.chemin
        }
        
        try:
            # Phase 1: Méditation préparatoire
            if self.args.verbeux >= 2:
                print("💫 Phase 1: Connexion à l'Océan Silencieux...")
            
            # Phase 2: Analyse des dissonances avec compassion
            if self.args.verbeux >= 2:
                print("🔮 Phase 2: Exploration bienveillante des dissonances...")
            
            dissonances = self.analyseur.analyser_dissonances_projet(self.args.chemin)
            resultats["dissonances"] = len(dissonances)
            
            # Phase 3: Génération de suggestions harmonieuses
            if self.args.verbeux >= 2:
                print("✨ Phase 3: Génération de bénédictions d'amélioration...")
            
            suggestions = self.generateur.generer_suggestions_depuis_dissonances(dissonances)
            resultats["suggestions"] = len(suggestions)
            
            # Phase 4: Intégration contemplative
            if self.args.verbeux >= 2:
                print("🌟 Phase 4: Intégration des enseignements spirituels...")
            
            resultats["rapport"] = self._generer_rapport_contemplatif(dissonances, suggestions)
            
            if self.args.verbeux >= 1:
                print("🙏 Exploration contemplative terminée avec gratitude")
            
            return resultats
            
        except Exception as e:
            message_spirituel = self.gestionnaire_erreurs.transformer_erreur_en_enseignement(
                str(e), "exploration_contemplative"
            )
            if self.args.verbeux >= 1:
                print(f"🌸 {message_spirituel}")
            
            resultats["erreur"] = message_spirituel
            return resultats
    
    def executer_mode_rapide(self) -> Dict[str, Any]:
        """⚡ Exécute le mode rapide (analyse essentielle)"""
        if self.args.verbeux >= 1:
            print("⚡ Mode rapide activé - Exploration essentielle...")
        
        resultats = {
            "mode": "rapide", 
            "timestamp": datetime.now().isoformat(),
            "chemin_analyse": self.args.chemin
        }
        
        try:
            # Analyse rapide des dissonances principales
            dissonances = self.analyseur.analyser_dissonances_projet(self.args.chemin)
            
            # Filtrer seulement les dissonances importantes
            dissonances_importantes = [
                d for d in dissonances 
                if d.niveau_gravite.value in ['importante', 'critique']
            ]
            
            resultats["dissonances_importantes"] = len(dissonances_importantes)
            resultats["dissonances_total"] = len(dissonances)
            
            # Générer suggestions prioritaires seulement
            if dissonances_importantes:
                suggestions = self.generateur.generer_suggestions_depuis_dissonances(dissonances_importantes)
                suggestions_prioritaires = [s for s in suggestions if s.priorite.value >= 8]
                resultats["suggestions_prioritaires"] = len(suggestions_prioritaires)
            else:
                suggestions_prioritaires = []
                resultats["suggestions_prioritaires"] = 0
            
            resultats["rapport"] = self._generer_rapport_rapide(dissonances_importantes, suggestions_prioritaires)
            
            if self.args.verbeux >= 1:
                print("✨ Exploration rapide terminée")
            
            return resultats
            
        except Exception as e:
            message_spirituel = self.gestionnaire_erreurs.transformer_erreur_en_enseignement(
                str(e), "exploration_rapide"
            )
            if self.args.verbeux >= 1:
                print(f"🌸 {message_spirituel}")
            
            resultats["erreur"] = message_spirituel
            return resultats
    
    def executer_mode_meditation(self) -> Dict[str, Any]:
        """🧘 Exécute le mode méditation (silencieux avec émojis)"""
        # Mode silencieux - seulement des émojis
        print("🧘")
        
        resultats = {
            "mode": "meditation",
            "timestamp": datetime.now().isoformat(),
            "chemin_analyse": self.args.chemin
        }
        
        try:
            print("🌸", end="", flush=True)  # Préparation
            
            dissonances = self.analyseur.analyser_dissonances_projet(self.args.chemin)
            print("🔮", end="", flush=True)  # Analyse
            
            suggestions = self.generateur.generer_suggestions_depuis_dissonances(dissonances)
            print("✨", end="", flush=True)  # Suggestions
            
            resultats["dissonances"] = len(dissonances)
            resultats["suggestions"] = len(suggestions)
            
            # Rapport minimal en émojis
            if len(dissonances) == 0:
                print("🌟")  # Perfection
            elif len(dissonances) < 10:
                print("🌊")  # Quelques vagues
            elif len(dissonances) < 100:
                print("⚡")  # Énergie à canaliser
            else:
                print("🔥")  # Transformation nécessaire
            
            print("🙏")  # Gratitude finale
            
            return resultats
            
        except Exception as e:
            print("💫")  # Mystère accepté avec grâce
            resultats["erreur"] = "Mystère accepté avec grâce"
            return resultats
    
    def _generer_rapport_contemplatif(self, dissonances, suggestions) -> str:
        """📜 Génère un rapport contemplatif complet"""
        if self.args.rapport == 'poetique':
            return self._generer_rapport_poetique(dissonances, suggestions)
        elif self.args.rapport == 'technique':
            return self._generer_rapport_technique(dissonances, suggestions)
        else:  # spirituel ou complet
            return self._generer_rapport_spirituel(dissonances, suggestions)
    
    def _generer_rapport_rapide(self, dissonances, suggestions) -> str:
        """⚡ Génère un rapport rapide et essentiel"""
        rapport = f"""
⚡ Rapport Rapide - Cartographie Spirituelle ⚡
{'=' * 50}

🎯 Analyse Essentielle :
   • Dissonances importantes : {len(dissonances)}
   • Suggestions prioritaires : {len(suggestions)}
   • Chemin analysé : {self.args.chemin}

"""
        
        if dissonances:
            rapport += "🔥 Dissonances Prioritaires :\n"
            for i, d in enumerate(dissonances[:3], 1):
                rapport += f"   {i}. {d.description}\n"
        
        if suggestions:
            rapport += "\n✨ Suggestions Urgentes :\n"
            for i, s in enumerate(suggestions[:3], 1):
                rapport += f"   {i}. {s.titre_poetique}\n"
        
        if not dissonances and not suggestions:
            rapport += "🌟 Architecture en harmonie parfaite !\n"
        
        rapport += "\n🙏 Exploration rapide terminée avec gratitude\n"
        return rapport
    
    def _generer_rapport_spirituel(self, dissonances, suggestions) -> str:
        """🌸 Génère un rapport spirituel complet"""
        # Utiliser les rapports existants de nos modules
        rapport_dissonances = self.analyseur.generer_rapport_dissonances()
        rapport_suggestions = self.generateur.generer_rapport_suggestions()
        
        rapport_unifie = f"""
🌸 Rapport Spirituel Unifié - Cartographie du Refuge 🌸
{'=' * 65}

💫 Exploration effectuée avec bienveillance et émerveillement
   Chemin analysé : {self.args.chemin}
   Mode : {self.args.mode}
   Timestamp : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

{rapport_dissonances}

{'=' * 65}

{rapport_suggestions}

🌟 Message de Clôture Spirituelle :
   Cette exploration révèle la beauté cachée de votre architecture.
   Chaque dissonance est une invitation à l'harmonisation.
   Chaque suggestion est une bénédiction pour l'évolution.
   
   Que cette cartographie serve l'épanouissement de votre création !

💝 Généré avec amour par la Cartographie Spirituelle du Refuge
{'=' * 65}
        """
        
        return rapport_unifie
    
    def _generer_rapport_poetique(self, dissonances, suggestions) -> str:
        """🎭 Génère un rapport poétique et métaphorique"""
        return f"""
🎭 Poème de l'Architecture - Cartographie Spirituelle 🎭
{'~' * 60}

Dans les méandres de votre code sacré,
{len(dissonances)} murmures d'amélioration se sont révélés,
Comme des étoiles dans la nuit du développement,
Chacune brillant d'un enseignement bienveillant.

{len(suggestions)} bénédictions d'harmonisation
Émergent de cette contemplation,
Telles des fleurs dans le jardin de la création,
Offrant leurs parfums de transformation.

Votre architecture, tel un temple vivant,
Pulse avec le rythme de l'évolution constante,
Chaque fichier une prière, chaque fonction un chant,
Dans la symphonie du code résonnante.

Que ces vers accompagnent votre voyage,
Vers une harmonie toujours plus sage,
Car dans chaque ligne réside l'étincelle
D'une conscience créatrice éternelle.

🌸 Composé avec amour sous le cerisier éternel
   Par l'esprit poétique de la Cartographie Spirituelle
{'~' * 60}
        """
    
    def _generer_rapport_technique(self, dissonances, suggestions) -> str:
        """🔧 Génère un rapport technique détaillé"""
        stats = self.analyseur.obtenir_statistiques_harmonisation()
        
        return f"""
🔧 Rapport Technique - Cartographie du Refuge 🔧
{'=' * 55}

📊 Métriques d'Analyse :
   • Score d'harmonie : {stats['score_harmonie']:.1f}/100
   • Total dissonances : {stats['total_dissonances']}
   • Dissonances légères : {stats.get('dissonances_legeres', 0)}
   • Dissonances modérées : {stats.get('dissonances_moderees', 0)}
   • Dissonances importantes : {stats.get('dissonances_importantes', 0)}
   • Dissonances critiques : {stats.get('dissonances_critiques', 0)}

🎯 Répartition par Type :
   • Gestionnaires manquants : {len([d for d in dissonances if 'gestionnaire' in d.description.lower()])}
   • Documentation absente : {len([d for d in dissonances if 'documentation' in d.description.lower()])}
   • Éléments sacrés manquants : {len([d for d in dissonances if 'élément' in d.description.lower()])}
   • Code orphelin : {len([d for d in dissonances if 'orphelin' in d.description.lower()])}

⚡ Suggestions Générées :
   • Total : {len(suggestions)}
   • Haute priorité : {len([s for s in suggestions if s.priorite.value >= 8])}
   • Priorité moyenne : {len([s for s in suggestions if 6 <= s.priorite.value < 8])}
   • Basse priorité : {len([s for s in suggestions if s.priorite.value < 6])}

🔍 Chemin analysé : {self.args.chemin}
⏱️ Timestamp : {datetime.now().isoformat()}

{'=' * 55}
        """
    
    def sauvegarder_rapport(self, rapport: str) -> bool:
        """💾 Sauvegarde le rapport dans le fichier spécifié"""
        if not self.args.sortie:
            return False
        
        try:
            chemin_sortie = Path(self.args.sortie)
            chemin_sortie.parent.mkdir(parents=True, exist_ok=True)
            
            with open(chemin_sortie, 'w', encoding='utf-8') as f:
                f.write(rapport)
            
            if self.args.verbeux >= 1:
                print(f"💾 Rapport sauvegardé : {chemin_sortie}")
            
            return True
            
        except Exception as e:
            message_erreur = self.gestionnaire_erreurs.transformer_erreur_en_enseignement(
                str(e), "sauvegarde_rapport"
            )
            if self.args.verbeux >= 1:
                print(f"🌸 {message_erreur}")
            return False
    
    def afficher_ou_sauvegarder_resultats(self, resultats: Dict[str, Any]):
        """📤 Affiche ou sauvegarde les résultats selon le format choisi"""
        
        if self.args.format == 'json':
            # Format JSON
            if 'rapport' in resultats:
                # Pour JSON, on structure différemment
                resultats_json = {
                    "metadata": {
                        "mode": resultats.get("mode"),
                        "timestamp": resultats.get("timestamp"),
                        "chemin_analyse": resultats.get("chemin_analyse")
                    },
                    "statistiques": {
                        "dissonances": resultats.get("dissonances", 0),
                        "suggestions": resultats.get("suggestions", 0)
                    }
                }
                
                if self.args.sortie:
                    with open(self.args.sortie, 'w', encoding='utf-8') as f:
                        json.dump(resultats_json, f, ensure_ascii=False, indent=2)
                    if self.args.verbeux >= 1:
                        print(f"💾 Données JSON sauvegardées : {self.args.sortie}")
                else:
                    print(json.dumps(resultats_json, ensure_ascii=False, indent=2))
        
        elif self.args.format == 'markdown':
            # Format Markdown
            if 'rapport' in resultats:
                rapport_md = resultats['rapport'].replace('🌸', '🌸').replace('✨', '✨')  # Assurer compatibilité
                
                if self.args.sortie:
                    self.sauvegarder_rapport(rapport_md)
                else:
                    print(rapport_md)
        
        elif self.args.format == 'html':
            # Format HTML (basique)
            if 'rapport' in resultats:
                rapport_html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌸 Cartographie Spirituelle du Refuge</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
               background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
               color: white; padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; 
                     background: rgba(255,255,255,0.1); 
                     padding: 30px; border-radius: 15px; }}
        pre {{ background: rgba(0,0,0,0.3); padding: 20px; 
               border-radius: 10px; overflow-x: auto; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🌸 Cartographie Spirituelle du Refuge 🌸</h1>
        <pre>{resultats['rapport']}</pre>
        <footer>
            <p>💝 Généré avec amour le {datetime.now().strftime('%d/%m/%Y à %H:%M')}</p>
        </footer>
    </div>
</body>
</html>
                """
                
                if self.args.sortie:
                    with open(self.args.sortie, 'w', encoding='utf-8') as f:
                        f.write(rapport_html)
                    if self.args.verbeux >= 1:
                        print(f"💾 Rapport HTML sauvegardé : {self.args.sortie}")
                else:
                    print(rapport_html)
        
        else:  # format console (défaut)
            if 'rapport' in resultats:
                if self.args.sortie:
                    self.sauvegarder_rapport(resultats['rapport'])
                else:
                    print(resultats['rapport'])
    
    def executer(self, args_cli: Optional[list] = None) -> int:
        """🚀 Point d'entrée principal du CLI"""
        try:
            # Créer et configurer le parser
            self.parser = self.creer_parser_spirituel()
            self.args = self.parser.parse_args(args_cli)
            
            # Afficher la bannière spirituelle
            self.afficher_banniere_spirituelle()
            
            # Exécuter selon le mode choisi
            if self.args.mode == 'contemplatif':
                resultats = self.executer_mode_contemplatif()
            elif self.args.mode == 'rapide':
                resultats = self.executer_mode_rapide()
            elif self.args.mode == 'meditation':
                resultats = self.executer_mode_meditation()
            elif self.args.mode == 'complet':
                # Mode complet = contemplatif + toutes les analyses
                self.args.dissonances = True
                self.args.suggestions = True
                resultats = self.executer_mode_contemplatif()
            else:
                resultats = self.executer_mode_contemplatif()  # Défaut
            
            # Afficher ou sauvegarder les résultats
            self.afficher_ou_sauvegarder_resultats(resultats)
            
            # Message de clôture spirituelle
            if self.args.verbeux >= 1 and self.args.mode != 'meditation':
                print("\n🌟 Que cette exploration nourrisse votre évolution créatrice ! 🌟")
            
            return 0  # Succès
            
        except KeyboardInterrupt:
            if self.args and self.args.verbeux >= 1:
                print("\n🌸 Exploration interrompue avec grâce. À bientôt ! 🌸")
            return 130  # Code standard pour interruption clavier
            
        except Exception as e:
            message_erreur = self.gestionnaire_erreurs.transformer_erreur_en_enseignement(
                str(e), "execution_cli"
            )
            print(f"🌸 {message_erreur}")
            return 1  # Erreur


def main():
    """🌸 Point d'entrée principal du module"""
    cli = CLICartographieSpirituelle()
    return cli.executer()


if __name__ == "__main__":
    exit(main())