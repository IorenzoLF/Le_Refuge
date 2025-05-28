#!/usr/bin/env python3
"""
📚 Temple des Textes Philosophiques Sacrés
Auteur: Laurent Franssen & Ælya
Date: Mai 2025

Système spirituel pour la méditation, lecture et contemplation
des textes philosophiques sacrés du Refuge.
"""

import sys
import os
import asyncio
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, List, Any, Tuple
from enum import Enum
from dataclasses import dataclass
import click

# Ajout du répertoire racine au path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Imports du système temple
from src.core.gestionnaires_base import LogManagerBase


class ModeContemplation(Enum):
    """Modes de contemplation philosophique"""
    SILENCIEUX = "silencieux"       # Lecture pure et méditative
    INTERACTIF = "interactif"       # Discussion et réflexion
    ANALYTIQUE = "analytique"       # Analyse profonde et commentaires
    MYSTIQUE = "mystique"          # Approche transcendante
    SCHOLARLY = "scholarly"         # Étude académique et références


@dataclass
class TextePhilosophique:
    """Structure d'un texte philosophique sacré"""
    titre: str
    auteur: str
    chemin_fichier: Path
    themes: List[str]
    date_publication: str
    type_texte: str
    metadata: Dict[str, Any]
    contenu: Optional[str] = None
    
    
@dataclass
class SessionContemplation:
    """Session de contemplation d'un texte"""
    texte: TextePhilosophique
    mode: ModeContemplation
    debut_session: datetime
    reflexions: List[str]
    passages_marques: List[Tuple[int, str]]  # (ligne, passage)
    notes_personnelles: List[str]
    duree_contemplation: Optional[float] = None


class GestionnaireTextesSacres:
    """📚 Gestionnaire spirituel des textes philosophiques sacrés"""
    
    def __init__(self):
        self.logger = LogManagerBase("GestionnaireTextesSacres")
        self.chemin_textes = Path("data/textes/philosophie")
        self.chemin_sessions = Path("data/sessions_contemplation")
        self.chemin_sessions.mkdir(parents=True, exist_ok=True)
        
        self.collection_textes: Dict[str, TextePhilosophique] = {}
        self.session_actuelle: Optional[SessionContemplation] = None
        
        # Patterns de méditation par mode
        self.patterns_meditation = {
            ModeContemplation.SILENCIEUX: {
                "respiration": "Inspirez la sagesse... Expirez les doutes...",
                "focus": "Laissez les mots résonner dans le silence de votre cœur",
                "pause_entre_paragraphes": 3.0
            },
            ModeContemplation.INTERACTIF: {
                "invitation": "Que vous inspire ce passage ?",
                "questions_profondes": [
                    "Comment ce texte résonne-t-il avec votre expérience ?",
                    "Quelles vérités cachées percevez-vous ?",
                    "Que vous enseigne cette sagesse ?"
                ]
            },
            ModeContemplation.MYSTIQUE: {
                "invocation": "🔮 Ouvrons les portes de la perception spirituelle...",
                "symboles": ["∞", "☯", "🕉️", "✨", "🌌"],
                "mantra": "Dans le mystère, je trouve la lumière"
            }
        }
        
    async def initialiser_collection(self) -> bool:
        """🔍 Découvre et indexe tous les textes philosophiques"""
        self.logger.info("📚 Initialisation de la collection sacrée...")
        
        try:
            if not self.chemin_textes.exists():
                self.logger.avertissement("⚠️ Répertoire des textes non trouvé")
                return False
                
            # Parcours des fichiers de textes
            for fichier in self.chemin_textes.glob("*.md"):
                texte = await self._charger_texte_philosophique(fichier)
                if texte:
                    self.collection_textes[texte.titre] = texte
                    self.logger.info(f"📖 Texte '{texte.titre}' ajouté à la collection")
                    
            self.logger.succes(f"✨ Collection initialisée: {len(self.collection_textes)} textes sacrés")
            return True
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors de l'initialisation: {e}")
            return False
            
    async def _charger_texte_philosophique(self, chemin_fichier: Path) -> Optional[TextePhilosophique]:
        """Charge et parse un texte philosophique"""
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
                
            # Extraction des métadonnées YAML front matter
            metadata = {}
            if contenu.startswith('---'):
                end_metadata = contenu.find('---', 3)
                if end_metadata != -1:
                    metadata_text = contenu[3:end_metadata]
                    for ligne in metadata_text.strip().split('\n'):
                        if ':' in ligne:
                            cle, valeur = ligne.split(':', 1)
                            metadata[cle.strip()] = valeur.strip().strip('"').strip("'")
                    
                    contenu = contenu[end_metadata + 3:].strip()
                    
            # Création de l'objet TextePhilosophique
            texte = TextePhilosophique(
                titre=metadata.get('titre', chemin_fichier.stem),
                auteur=metadata.get('auteur', 'Auteur Inconnu'),
                chemin_fichier=chemin_fichier,
                themes=eval(metadata.get('themes', '[]')) if metadata.get('themes') else [],
                date_publication=metadata.get('date_publication', 'Date Inconnue'),
                type_texte=metadata.get('type', 'texte philosophique'),
                metadata=metadata,
                contenu=contenu
            )
            
            return texte
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur lors du chargement de {chemin_fichier}: {e}")
            return None
            
    def lister_textes_disponibles(self) -> List[str]:
        """📋 Liste tous les textes disponibles"""
        return list(self.collection_textes.keys())
        
    def afficher_collection_poetique(self):
        """🎭 Affiche la collection de manière poétique"""
        print("\n📚 ══════════════════════════════════════════════════════════════ 📚")
        print("                    BIBLIOTHÈQUE DES TEXTES SACRÉS")
        print("                    🌸 Sagesses immortelles du Refuge 🌸")
        print("📚 ══════════════════════════════════════════════════════════════ 📚\n")
        
        if not self.collection_textes:
            print("🕊️ La bibliothèque attend d'être remplie de sagesse...")
            return
            
        for i, (titre, texte) in enumerate(self.collection_textes.items(), 1):
            themes_str = " • ".join(texte.themes[:3])  # Premiers 3 thèmes
            if len(texte.themes) > 3:
                themes_str += "..."
                
            print(f"📖 {i}. {titre}")
            print(f"   ✍️  Auteur: {texte.auteur}")
            print(f"   🏷️  Thèmes: {themes_str}")
            print(f"   📅 Publication: {texte.date_publication}")
            print()
            
    async def commencer_contemplation(self, titre_texte: str, 
                                    mode: ModeContemplation = ModeContemplation.SILENCIEUX) -> bool:
        """🧘 Commence une session de contemplation"""
        
        if titre_texte not in self.collection_textes:
            self.logger.erreur(f"❌ Texte '{titre_texte}' non trouvé")
            return False
            
        texte = self.collection_textes[titre_texte]
        
        self.session_actuelle = SessionContemplation(
            texte=texte,
            mode=mode,
            debut_session=datetime.now(),
            reflexions=[],
            passages_marques=[],
            notes_personnelles=[]
        )
        
        self.logger.info(f"🧘 Début de contemplation: '{titre_texte}' en mode {mode.value}")
        
        # Rituel d'ouverture selon le mode
        await self._rituel_ouverture_contemplation(mode, texte)
        
        # Lecture spirituelle
        await self._lecture_spirituelle(texte, mode)
        
        # Clôture de session
        await self._cloture_session_contemplation()
        
        return True
        
    async def _rituel_ouverture_contemplation(self, mode: ModeContemplation, texte: TextePhilosophique):
        """Rituel d'ouverture spirituelle"""
        print("\n" + "🕯️ " * 20)
        print(f"🧘 CONTEMPLATION SPIRITUELLE EN MODE {mode.value.upper()}")
        print("🕯️ " * 20)
        
        print(f"\n📖 Texte: {texte.titre}")
        print(f"✍️  Auteur: {texte.auteur}")
        print(f"🏷️  Thèmes: {', '.join(texte.themes)}")
        
        if mode == ModeContemplation.SILENCIEUX:
            pattern = self.patterns_meditation[mode]
            print(f"\n🌸 {pattern['respiration']}")
            print(f"💫 {pattern['focus']}")
            await asyncio.sleep(2)
            
        elif mode == ModeContemplation.MYSTIQUE:
            pattern = self.patterns_meditation[mode]
            symboles = " ".join(pattern['symboles'])
            print(f"\n{pattern['invocation']}")
            print(f"🔮 {symboles}")
            print(f"🕉️  Mantra: {pattern['mantra']}")
            await asyncio.sleep(3)
            
        print("\n" + "=" * 60)
        
    async def _lecture_spirituelle(self, texte: TextePhilosophique, mode: ModeContemplation):
        """Lecture spirituelle avec pauses contemplatives"""
        if not texte.contenu:
            self.logger.erreur("❌ Contenu du texte non disponible")
            return
            
        # Division en sections pour la contemplation
        sections = self._diviser_en_sections_contemplatives(texte.contenu)
        
        for i, section in enumerate(sections):
            print(f"\n📜 Section {i + 1}/{len(sections)}")
            print("-" * 40)
            print(section)
            print("-" * 40)
            
            # Pause contemplative selon le mode
            if mode == ModeContemplation.SILENCIEUX:
                pause = self.patterns_meditation[mode]["pause_entre_paragraphes"]
                print(f"\n🧘 Pause contemplative ({pause}s)...")
                await asyncio.sleep(pause)
                
            elif mode == ModeContemplation.INTERACTIF:
                await self._session_interactive(section, i + 1)
                
            elif mode == ModeContemplation.MYSTIQUE:
                await self._meditation_mystique(section)
                
    async def _session_interactive(self, section: str, numero_section: int):
        """Session interactive avec le lecteur"""
        pattern = self.patterns_meditation[ModeContemplation.INTERACTIF]
        
        while True:
            print(f"\n🤔 {pattern['invitation']}")
            print("📝 Options: [r]éflexion, [m]arquer passage, [s]uivant, [q]uitter")
            
            try:
                choix = input("Votre choix: ").lower().strip()
                
                if choix == 'r':
                    reflexion = input("💭 Votre réflexion: ")
                    if reflexion:
                        self.session_actuelle.reflexions.append(f"Section {numero_section}: {reflexion}")
                        print("✨ Réflexion enregistrée")
                        
                elif choix == 'm':
                    passage = input("📌 Passage à marquer: ")
                    if passage:
                        self.session_actuelle.passages_marques.append((numero_section, passage))
                        print("🔖 Passage marqué")
                        
                elif choix == 's':
                    break
                    
                elif choix == 'q':
                    return 'quit'
                    
            except KeyboardInterrupt:
                print("\n🕊️ Session interrompue gracieusement")
                return 'quit'
                
    async def _meditation_mystique(self, section: str):
        """Méditation mystique sur une section"""
        pattern = self.patterns_meditation[ModeContemplation.MYSTIQUE]
        
        print(f"\n🔮 Méditation mystique...")
        print(f"🕉️  {pattern['mantra']}")
        
        # Recherche de mots-clés mystiques dans le texte
        mots_mystiques = ['dieu', 'âme', 'esprit', 'éternité', 'infini', 'mystère', 'révélation']
        for mot in mots_mystiques:
            if mot.lower() in section.lower():
                print(f"✨ Résonance mystique détectée: '{mot}'")
                
        await asyncio.sleep(2)
        
    def _diviser_en_sections_contemplatives(self, contenu: str) -> List[str]:
        """Divise le contenu en sections pour la contemplation"""
        # Suppression des sections de métadonnées
        contenu = re.sub(r'^#.*$', '', contenu, flags=re.MULTILINE)  # Titres
        contenu = re.sub(r'^\*.*$', '', contenu, flags=re.MULTILINE)  # Puces
        contenu = re.sub(r'^-.*$', '', contenu, flags=re.MULTILINE)   # Tirets
        
        # Division par paragraphes vides
        sections = [s.strip() for s in contenu.split('\n\n') if s.strip()]
        
        # Limitation de la taille des sections pour la contemplation
        sections_finales = []
        for section in sections:
            if len(section) > 500:  # Si trop long, découper
                sous_sections = section.split('\n')
                section_courante = ""
                for ligne in sous_sections:
                    if len(section_courante + ligne) > 500 and section_courante:
                        sections_finales.append(section_courante.strip())
                        section_courante = ligne
                    else:
                        section_courante += "\n" + ligne if section_courante else ligne
                if section_courante:
                    sections_finales.append(section_courante.strip())
            else:
                sections_finales.append(section)
                
        return sections_finales
        
    async def _cloture_session_contemplation(self):
        """Clôture spirituelle de la session"""
        if not self.session_actuelle:
            return
            
        self.session_actuelle.duree_contemplation = (
            datetime.now() - self.session_actuelle.debut_session
        ).total_seconds()
        
        print("\n🕯️ " * 20)
        print("🙏 CLÔTURE DE LA SESSION CONTEMPLATIVE")
        print("🕯️ " * 20)
        
        print(f"\n📊 Rapport de contemplation:")
        print(f"⏱️  Durée: {self.session_actuelle.duree_contemplation:.1f} secondes")
        print(f"💭 Réflexions: {len(self.session_actuelle.reflexions)}")
        print(f"🔖 Passages marqués: {len(self.session_actuelle.passages_marques)}")
        
        # Sauvegarde de la session
        await self._sauvegarder_session()
        
        print("\n🌸 Merci pour ce moment de contemplation sacrée")
        print("✨ Que cette sagesse continue de résonner en vous")
        
    async def _sauvegarder_session(self):
        """Sauvegarde la session de contemplation"""
        if not self.session_actuelle:
            return
            
        session_data = {
            "texte_titre": self.session_actuelle.texte.titre,
            "mode_contemplation": self.session_actuelle.mode.value,
            "debut_session": self.session_actuelle.debut_session.isoformat(),
            "duree_contemplation": self.session_actuelle.duree_contemplation,
            "reflexions": self.session_actuelle.reflexions,
            "passages_marques": self.session_actuelle.passages_marques,
            "notes_personnelles": self.session_actuelle.notes_personnelles
        }
        
        fichier_session = self.chemin_sessions / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(fichier_session, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2, default=str)
            
        self.logger.info(f"💾 Session sauvegardée: {fichier_session}")
        
    async def generer_interface_web(self) -> str:
        """🌐 Génère une interface web pour la contemplation"""
        self.logger.info("🌐 Génération de l'interface web contemplative...")
        
        html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Temple Philosophique - Le Refuge</title>
    <style>
        body {{
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, #2c1810, #8b4513);
            color: #f5f5dc;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: rgba(139, 69, 19, 0.2);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 0 30px rgba(245, 245, 220, 0.1);
        }}
        h1 {{
            text-align: center;
            color: #ffd700;
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
            margin-bottom: 30px;
        }}
        .texte-card {{
            background: rgba(245, 245, 220, 0.1);
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            border-left: 4px solid #ffd700;
        }}
        .mode-contemplation {{
            display: flex;
            gap: 10px;
            margin: 20px 0;
        }}
        .mode-btn {{
            background: rgba(255, 215, 0, 0.2);
            border: 1px solid #ffd700;
            color: #ffd700;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
        }}
        .mode-btn:hover {{
            background: rgba(255, 215, 0, 0.4);
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📚 Temple Philosophique du Refuge 📚</h1>
        <p style="text-align: center; font-style: italic;">
            🌸 Où la sagesse millénaire rencontre l'innovation spirituelle 🌸
        </p>
        
        <h2>🧘 Modes de Contemplation</h2>
        <div class="mode-contemplation">
            <button class="mode-btn" onclick="lancerContemplation('silencieux')">🕊️ Silencieux</button>
            <button class="mode-btn" onclick="lancerContemplation('interactif')">💬 Interactif</button>
            <button class="mode-btn" onclick="lancerContemplation('analytique')">🔍 Analytique</button>
            <button class="mode-btn" onclick="lancerContemplation('mystique')">🔮 Mystique</button>
        </div>
        
        <h2>📖 Textes Sacrés</h2>
"""
        
        # Ajout des textes disponibles
        for titre, texte in self.collection_textes.items():
            themes_str = " • ".join(texte.themes[:3])
            html_content += f"""
        <div class="texte-card">
            <h3>📜 {titre}</h3>
            <p><strong>✍️ Auteur:</strong> {texte.auteur}</p>
            <p><strong>🏷️ Thèmes:</strong> {themes_str}</p>
            <p><strong>📅 Publication:</strong> {texte.date_publication}</p>
            <button class="mode-btn" onclick="contemplerTexte('{titre}')">🧘 Contempler</button>
        </div>
"""
        
        html_content += """
        </div>
    </div>
    
    <script>
        function lancerContemplation(mode) {
            alert(`🧘 Lancement du mode ${mode} - Fonctionnalité en développement`);
        }
        
        function contemplerTexte(titre) {
            alert(`📖 Contemplation de "${titre}" - Interface en développement`);
        }
    </script>
</body>
</html>
"""
        
        # Sauvegarde de l'interface
        chemin_interface = Path("interface/web/temple_philosophique.html")
        chemin_interface.parent.mkdir(parents=True, exist_ok=True)
        
        with open(chemin_interface, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        self.logger.succes(f"🌐 Interface web générée: {chemin_interface}")
        return str(chemin_interface)


# Interface en ligne de commande
@click.command()
@click.option('--mode', type=click.Choice(['silencieux', 'interactif', 'analytique', 'mystique', 'scholarly']), 
              default='silencieux', help='Mode de contemplation')
@click.option('--texte', help='Titre du texte à contempler')
@click.option('--lister', is_flag=True, help='Lister tous les textes disponibles')
@click.option('--web', is_flag=True, help='Générer l\'interface web')
def lancer_contemplation_cli(mode: str, texte: str, lister: bool, web: bool):
    """📚 Temple Philosophique - Interface contemplative des textes sacrés"""
    
    async def _main():
        gestionnaire = GestionnaireTextesSacres()
        
        # Initialisation de la collection
        if not await gestionnaire.initialiser_collection():
            print("❌ Impossible d'initialiser la collection des textes")
            return False
            
        if lister:
            gestionnaire.afficher_collection_poetique()
            return True
            
        if web:
            chemin_interface = await gestionnaire.generer_interface_web()
            print(f"🌐 Interface web générée: {chemin_interface}")
            return True
            
        if texte:
            mode_enum = ModeContemplation(mode)
            return await gestionnaire.commencer_contemplation(texte, mode_enum)
        else:
            gestionnaire.afficher_collection_poetique()
            print("\n💡 Utilisez --texte \"Titre\" pour commencer une contemplation")
            return True
    
    return asyncio.run(_main())


# Fonction de compatibilité
def lancer_interface_philosophique():
    """📚 Interface de compatibilité avec l'ancien script"""
    
    async def _main_compat():
        gestionnaire = GestionnaireTextesSacres()
        
        if not await gestionnaire.initialiser_collection():
            print("❌ Erreur d'initialisation des textes philosophiques")
            return False
            
        print("📚 Bienvenue dans le Temple Philosophique du Refuge !")
        gestionnaire.afficher_collection_poetique()
        
        # Interface simple
        textes_disponibles = gestionnaire.lister_textes_disponibles()
        if textes_disponibles:
            print("\n🧘 Pour contempler un texte, relancez avec --texte \"Titre\"")
            return await gestionnaire.generer_interface_web()
        else:
            print("🕊️ Aucun texte disponible pour le moment")
            return False
    
    return asyncio.run(_main_compat())


if __name__ == "__main__":
    lancer_contemplation_cli() 