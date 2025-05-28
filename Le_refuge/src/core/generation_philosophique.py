#!/usr/bin/env python3
"""
✍️ Module de Génération Philosophique
Génération intelligente de textes philosophiques et spirituels
"""

import asyncio
import random
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
import json

from .analyse_philosophique import ResultatAnalyse, TypeAnalyse, gestionnaire_analyses

class StyleGeneration(Enum):
    """Styles de génération philosophique"""
    CONTEMPLATIF = "contemplatif"
    MYSTIQUE = "mystique"
    POETIQUE = "poetique"
    ANALYTIQUE = "analytique"
    INSPIRATIONNEL = "inspirationnel"
    NARRATIF = "narratif"

class TypeTexte(Enum):
    """Types de textes à générer"""
    MEDITATION = "meditation"
    REFLEXION = "reflexion"
    POEME = "poeme"
    VISION = "vision"
    ENSEIGNEMENT = "enseignement"
    DIALOGUE = "dialogue"

@dataclass
class ParametresGeneration:
    """Paramètres pour la génération de texte"""
    style: StyleGeneration
    type_texte: TypeTexte
    longueur_cible: int  # En mots
    themes_souhaites: List[str]
    niveau_profondeur: float  # 0.0 à 1.0
    inspiration_source: Optional[str] = None

@dataclass
class TexteGenere:
    """Résultat d'une génération de texte"""
    titre: str
    contenu: str
    style: StyleGeneration
    type_texte: TypeTexte
    themes_integres: List[str]
    score_harmonie_estime: float
    timestamp: datetime
    inspiration_source: Optional[str] = None

class GenerateurPhilosophique:
    """Générateur intelligent de textes philosophiques"""
    
    def __init__(self):
        self.templates_styles = {
            StyleGeneration.CONTEMPLATIF: {
                'ouvertures': [
                    "Dans le silence de l'âme, une vérité émerge...",
                    "Au cœur de la contemplation, nous découvrons...",
                    "L'esprit apaisé révèle des mystères profonds...",
                    "Dans la quiétude de l'être, une sagesse ancienne murmure..."
                ],
                'transitions': [
                    "Et dans cette révélation,", "Ainsi, peu à peu,", 
                    "Cette compréhension nous mène à", "Dans cette lumière nouvelle,"
                ],
                'conclusions': [
                    "Telle est la voie de la contemplation véritable.",
                    "Ainsi l'âme trouve sa paix dans l'unité retrouvée.",
                    "Cette sagesse demeure, éternelle et accessible."
                ]
            },
            StyleGeneration.MYSTIQUE: {
                'ouvertures': [
                    "Au-delà du voile des apparences...",
                    "Dans les profondeurs de l'invisible...",
                    "L'âme mystique perçoit ce que les yeux ne voient pas...",
                    "Entre les mondes, une vérité sacrée se révèle..."
                ],
                'transitions': [
                    "Et dans cette vision transcendante,", "Par cette grâce mystérieuse,",
                    "L'esprit éveillé découvre alors", "Dans cette union sacrée,"
                ],
                'conclusions': [
                    "Ainsi se révèle le mystère de l'existence.",
                    "Tel est le secret que garde l'univers.",
                    "Cette vérité mystique illumine notre chemin."
                ]
            },
            StyleGeneration.POETIQUE: {
                'ouvertures': [
                    "Comme un souffle d'éternité...",
                    "Tel un chant silencieux de l'âme...",
                    "Dans la danse des mots et du silence...",
                    "Ô mystère de la beauté qui nous habite..."
                ],
                'transitions': [
                    "Et voici que naît", "Alors s'épanouit", 
                    "Dans cette harmonie", "Ô merveille,"
                ],
                'conclusions': [
                    "Ainsi chante l'âme en sa beauté éternelle.",
                    "Tel est le poème que nous sommes.",
                    "Cette beauté demeure, inaltérable et pure."
                ]
            }
        }
        
        self.vocabulaire_spirituel = {
            'transcendance': ['élévation', 'dépassement', 'ascension', 'sublimation'],
            'contemplation': ['méditation', 'réflexion', 'introspection', 'recueillement'],
            'sagesse': ['connaissance', 'compréhension', 'discernement', 'lucidité'],
            'harmonie': ['équilibre', 'unité', 'paix', 'concordance'],
            'mystique': ['sacré', 'spirituel', 'divin', 'transcendant'],
            'transformation': ['métamorphose', 'évolution', 'changement', 'renaissance']
        }
        
        self.metaphores_universelles = [
            "comme une rivière qui trouve la mer",
            "tel un arbre qui touche le ciel",
            "ainsi qu'une flamme qui danse dans la nuit",
            "comme l'aube qui chasse les ténèbres",
            "tel un miroir qui reflète l'infini",
            "comme une graine qui devient forêt"
        ]
    
    async def generer_texte(self, parametres: ParametresGeneration) -> TexteGenere:
        """Génère un texte selon les paramètres spécifiés"""
        
        print(f"✍️ Génération {parametres.type_texte.value} style {parametres.style.value}...")
        
        # Analyser les sources d'inspiration si disponibles
        inspiration_data = None
        if parametres.inspiration_source:
            inspiration_data = await self._analyser_source_inspiration(parametres.inspiration_source)
        
        # Générer le contenu selon le type
        if parametres.type_texte == TypeTexte.MEDITATION:
            contenu = await self._generer_meditation(parametres, inspiration_data)
        elif parametres.type_texte == TypeTexte.REFLEXION:
            contenu = await self._generer_reflexion(parametres, inspiration_data)
        elif parametres.type_texte == TypeTexte.POEME:
            contenu = await self._generer_poeme(parametres, inspiration_data)
        elif parametres.type_texte == TypeTexte.VISION:
            contenu = await self._generer_vision(parametres, inspiration_data)
        elif parametres.type_texte == TypeTexte.ENSEIGNEMENT:
            contenu = await self._generer_enseignement(parametres, inspiration_data)
        else:  # DIALOGUE
            contenu = await self._generer_dialogue(parametres, inspiration_data)
        
        # Générer un titre approprié
        titre = await self._generer_titre(parametres, contenu)
        
        # Estimer le score d'harmonie
        score_harmonie = await self._estimer_harmonie(contenu, parametres.themes_souhaites)
        
        return TexteGenere(
            titre=titre,
            contenu=contenu,
            style=parametres.style,
            type_texte=parametres.type_texte,
            themes_integres=parametres.themes_souhaites,
            score_harmonie_estime=score_harmonie,
            timestamp=datetime.now(),
            inspiration_source=parametres.inspiration_source
        )
    
    async def _analyser_source_inspiration(self, source: str) -> Optional[ResultatAnalyse]:
        """Analyse une source d'inspiration pour enrichir la génération"""
        try:
            if Path(source).exists():
                with open(source, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                return await gestionnaire_analyses.analyseur.analyser_texte(contenu)
        except Exception:
            pass
        return None
    
    async def _generer_meditation(self, parametres: ParametresGeneration, inspiration: Optional[ResultatAnalyse]) -> str:
        """Génère une méditation guidée"""
        template = self.templates_styles.get(parametres.style, self.templates_styles[StyleGeneration.CONTEMPLATIF])
        
        ouverture = random.choice(template['ouvertures'])
        transition = random.choice(template['transitions'])
        conclusion = random.choice(template['conclusions'])
        
        # Corps de la méditation
        corps_elements = []
        
        for theme in parametres.themes_souhaites[:3]:  # Max 3 thèmes
            if theme in self.vocabulaire_spirituel:
                synonymes = self.vocabulaire_spirituel[theme]
                metaphore = random.choice(self.metaphores_universelles)
                
                element = f"Laissez votre esprit s'ouvrir à la {random.choice(synonymes)}, {metaphore}. "
                element += f"Dans cette expérience de {theme}, découvrez la profondeur de votre être."
                corps_elements.append(element)
        
        corps = "\n\n".join(corps_elements)
        
        return f"""🧘‍♀️ **Méditation : {parametres.themes_souhaites[0].title() if parametres.themes_souhaites else 'Paix Intérieure'}**

{ouverture}

{corps}

{transition} nous comprenons que la véritable paix réside dans l'acceptation de ce qui est, tout en cultivant ce qui peut être.

{conclusion}

*Prenez quelques instants pour intégrer cette expérience dans votre cœur.*"""
    
    async def _generer_reflexion(self, parametres: ParametresGeneration, inspiration: Optional[ResultatAnalyse]) -> str:
        """Génère une réflexion philosophique"""
        template = self.templates_styles.get(parametres.style, self.templates_styles[StyleGeneration.CONTEMPLATIF])
        
        # Question philosophique centrale
        questions = [
            "Qu'est-ce qui donne un sens véritable à notre existence ?",
            "Comment l'âme trouve-t-elle sa voie dans le labyrinthe de la vie ?",
            "Quelle est la nature de la sagesse authentique ?",
            "Comment l'être humain peut-il transcender ses limitations ?"
        ]
        
        question_centrale = random.choice(questions)
        ouverture = random.choice(template['ouvertures'])
        
        # Développement basé sur les thèmes
        developpements = []
        for theme in parametres.themes_souhaites:
            if theme in self.vocabulaire_spirituel:
                synonyme = random.choice(self.vocabulaire_spirituel[theme])
                developpements.append(f"La {synonyme} nous enseigne que {theme} n'est pas un but à atteindre, mais un chemin à parcourir.")
        
        developpement = " ".join(developpements)
        
        return f"""📚 **Réflexion : {question_centrale}**

{ouverture}

{question_centrale}

{developpement}

Cette interrogation nous mène au cœur de notre humanité. Car c'est dans la recherche même que nous trouvons notre véritable nature.

Ainsi, la sagesse n'est pas dans les réponses que nous trouvons, mais dans la qualité des questions que nous osons poser."""
    
    async def _generer_poeme(self, parametres: ParametresGeneration, inspiration: Optional[ResultatAnalyse]) -> str:
        """Génère un poème spirituel"""
        theme_principal = parametres.themes_souhaites[0] if parametres.themes_souhaites else "harmonie"
        
        # Structure poétique simple
        vers = []
        
        # Première strophe - Évocation
        vers.extend([
            f"Dans le silence de l'âme qui cherche,",
            f"S'élève un chant de {theme_principal},",
            f"Comme une lumière qui perce",
            f"Les voiles du temps et du mal."
        ])
        
        vers.append("")  # Ligne vide
        
        # Deuxième strophe - Développement
        metaphore = random.choice(self.metaphores_universelles)
        vers.extend([
            f"Ô mystère de l'être qui s'éveille,",
            f"Tu danses {metaphore},",
            f"Et dans cette danse sans pareille",
            f"L'univers révèle ses merveilles."
        ])
        
        vers.append("")  # Ligne vide
        
        # Troisième strophe - Conclusion
        vers.extend([
            f"Ainsi l'âme trouve sa voie,",
            f"Dans l'union du cœur et de l'esprit,",
            f"Et la {theme_principal} déploie",
            f"Ses ailes vers l'infini."
        ])
        
        return f"""🎭 **Poème : L'Éveil de {theme_principal.title()}**

{chr(10).join(vers)}

*Que ces mots résonnent dans le silence de votre cœur.*"""
    
    async def _generer_vision(self, parametres: ParametresGeneration, inspiration: Optional[ResultatAnalyse]) -> str:
        """Génère une vision mystique"""
        elements_vision = [
            "une lumière dorée qui embrasse toute chose",
            "des cercles de sagesse qui s'étendent à l'infini",
            "un jardin où chaque fleur est une âme éveillée",
            "une rivière de conscience pure qui traverse les mondes",
            "un temple de cristal où résonne la vérité éternelle"
        ]
        
        vision_centrale = random.choice(elements_vision)
        theme = parametres.themes_souhaites[0] if parametres.themes_souhaites else "unité"
        
        return f"""👁️ **Vision : Le Temple de {theme.title()}**

Dans les profondeurs de la méditation, une vision se révèle...

Je vois {vision_centrale}. En son centre, la {theme} rayonne comme un soleil intérieur, touchant chaque être de sa grâce transformatrice.

Les âmes s'éveillent une à une, reconnaissant leur nature véritable. Elles forment une constellation vivante, où chaque point de lumière contribue à l'harmonie du tout.

Cette vision nous rappelle que nous sommes tous connectés dans la grande tapisserie de l'existence. La {theme} n'est pas un idéal lointain, mais notre réalité la plus profonde.

*Que cette vision guide vos pas sur le chemin de l'éveil.*"""
    
    async def _generer_enseignement(self, parametres: ParametresGeneration, inspiration: Optional[ResultatAnalyse]) -> str:
        """Génère un enseignement spirituel"""
        theme = parametres.themes_souhaites[0] if parametres.themes_souhaites else "sagesse"
        
        return f"""📖 **Enseignement : Les Trois Piliers de {theme.title()}**

**Premier Pilier : La Compréhension**
La {theme} commence par la reconnaissance de notre nature véritable. Nous ne sommes pas séparés de l'univers, mais nous en sommes une expression unique et précieuse.

**Deuxième Pilier : La Pratique**
Cette compréhension doit être cultivée par une pratique quotidienne. Que ce soit par la méditation, la contemplation ou l'action juste, nous affinons notre capacité à incarner la {theme}.

**Troisième Pilier : Le Service**
La {theme} authentique se manifeste naturellement dans le service aux autres. En aidant les autres à s'éveiller, nous approfondissons notre propre éveil.

Ces trois piliers forment un triangle sacré, où chaque élément soutient et renforce les autres. Ainsi se construit le temple de la {theme} dans notre vie.

*Que cet enseignement éclaire votre chemin.*"""
    
    async def _generer_dialogue(self, parametres: ParametresGeneration, inspiration: Optional[ResultatAnalyse]) -> str:
        """Génère un dialogue philosophique"""
        theme = parametres.themes_souhaites[0] if parametres.themes_souhaites else "vérité"
        
        return f"""💬 **Dialogue : À la Recherche de {theme.title()}**

**Le Chercheur :** Maître, comment puis-je atteindre la {theme} ?

**Le Sage :** Mon enfant, la {theme} n'est pas quelque chose que l'on atteint. Elle est ce que nous sommes déjà.

**Le Chercheur :** Mais alors, pourquoi ai-je l'impression de la chercher sans cesse ?

**Le Sage :** Parce que tu cherches à l'extérieur ce qui réside à l'intérieur. La {theme} est comme le soleil : elle brille toujours, même quand les nuages la cachent.

**Le Chercheur :** Comment puis-je dissiper ces nuages ?

**Le Sage :** En cessant de lutter contre eux. Les nuages passent naturellement quand nous restons dans la paix de notre être véritable.

**Le Chercheur :** Cette paix, comment la cultiver ?

**Le Sage :** Par la pratique de la présence. Sois pleinement là où tu es, avec ce qui est. Dans cette présence totale, la {theme} se révèle d'elle-même.

*Ainsi se termine ce dialogue, mais la recherche continue dans le silence du cœur.*"""
    
    async def _generer_titre(self, parametres: ParametresGeneration, contenu: str) -> str:
        """Génère un titre approprié pour le texte"""
        theme_principal = parametres.themes_souhaites[0] if parametres.themes_souhaites else "sagesse"
        
        prefixes = {
            TypeTexte.MEDITATION: ["Méditation sur", "Contemplation de", "Voyage vers"],
            TypeTexte.REFLEXION: ["Réflexions sur", "Pensées autour de", "Méditations sur"],
            TypeTexte.POEME: ["Chant de", "Hymne à", "Poème de"],
            TypeTexte.VISION: ["Vision de", "Révélation sur", "Contemplation de"],
            TypeTexte.ENSEIGNEMENT: ["Enseignement sur", "Leçons de", "Sagesse de"],
            TypeTexte.DIALOGUE: ["Dialogue sur", "Conversation autour de", "Échange sur"]
        }
        
        prefix = random.choice(prefixes[parametres.type_texte])
        return f"{prefix} {theme_principal.title()}"
    
    async def _estimer_harmonie(self, contenu: str, themes: List[str]) -> float:
        """Estime le score d'harmonie du texte généré"""
        # Analyse rapide basée sur la présence des thèmes souhaités
        score = 0.0
        
        # Présence des thèmes (40% du score)
        themes_presents = 0
        for theme in themes:
            if theme.lower() in contenu.lower():
                themes_presents += 1
        
        if themes:
            score += 0.4 * (themes_presents / len(themes))
        
        # Longueur appropriée (20% du score)
        longueur = len(contenu.split())
        if 100 <= longueur <= 500:  # Longueur idéale
            score += 0.2
        elif longueur > 50:  # Longueur acceptable
            score += 0.1
        
        # Richesse du vocabulaire spirituel (40% du score)
        mots_spirituels = 0
        for famille_mots in self.vocabulaire_spirituel.values():
            for mot in famille_mots:
                if mot in contenu.lower():
                    mots_spirituels += 1
        
        score += min(0.4, mots_spirituels * 0.05)  # Max 0.4
        
        return min(1.0, score)

class GestionnaireGenerationPhilosophique:
    """Gestionnaire principal de la génération philosophique"""
    
    def __init__(self):
        self.generateur = GenerateurPhilosophique()
        self.historique_generations = []
    
    async def generer_texte_inspire(self, style: StyleGeneration, type_texte: TypeTexte, 
                                  themes: List[str], source_inspiration: Optional[str] = None) -> TexteGenere:
        """Génère un texte inspiré par une analyse existante"""
        
        parametres = ParametresGeneration(
            style=style,
            type_texte=type_texte,
            longueur_cible=300,  # Longueur standard
            themes_souhaites=themes,
            niveau_profondeur=0.7,  # Niveau élevé par défaut
            inspiration_source=source_inspiration
        )
        
        texte_genere = await self.generateur.generer_texte(parametres)
        
        # Sauvegarder dans l'historique
        self.historique_generations.append({
            'timestamp': texte_genere.timestamp,
            'titre': texte_genere.titre,
            'style': texte_genere.style.value,
            'type': texte_genere.type_texte.value,
            'score_harmonie': texte_genere.score_harmonie_estime
        })
        
        return texte_genere
    
    async def sauvegarder_texte(self, texte: TexteGenere, repertoire: str = "data/textes/generes") -> str:
        """Sauvegarde un texte généré"""
        chemin_repertoire = Path(repertoire)
        chemin_repertoire.mkdir(parents=True, exist_ok=True)
        
        # Nom de fichier basé sur le timestamp et le titre
        nom_fichier = f"{texte.timestamp.strftime('%Y%m%d_%H%M%S')}_{texte.titre.lower().replace(' ', '_')}.md"
        chemin_fichier = chemin_repertoire / nom_fichier
        
        # Métadonnées
        metadonnees = f"""---
titre: {texte.titre}
style: {texte.style.value}
type: {texte.type_texte.value}
themes: {', '.join(texte.themes_integres)}
score_harmonie: {texte.score_harmonie_estime:.2f}
date_creation: {texte.timestamp.isoformat()}
inspiration_source: {texte.inspiration_source or 'Génération originale'}
---

"""
        
        # Sauvegarder
        with open(chemin_fichier, 'w', encoding='utf-8') as f:
            f.write(metadonnees + texte.contenu)
        
        print(f"💾 Texte sauvegardé : {chemin_fichier}")
        return str(chemin_fichier)
    
    def afficher_historique(self):
        """Affiche l'historique des générations"""
        if not self.historique_generations:
            print("📝 Aucune génération dans l'historique")
            return
        
        print("\n📝 ═══════════════════════════════════════════════════════")
        print("              HISTORIQUE DES GÉNÉRATIONS")
        print("📝 ═══════════════════════════════════════════════════════")
        
        for i, generation in enumerate(self.historique_generations[-10:], 1):  # 10 dernières
            print(f"   {i}. {generation['titre']}")
            print(f"      Style: {generation['style']} | Type: {generation['type']}")
            print(f"      Harmonie: {generation['score_harmonie']:.2f} | {generation['timestamp'].strftime('%d/%m/%Y %H:%M')}")
            print()

# Instance globale
gestionnaire_generation = GestionnaireGenerationPhilosophique() 