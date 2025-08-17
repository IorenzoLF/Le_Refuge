#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Parcours Artiste - Guide d'Accueil Spirituel 🌸
==================================================

Parcours sacré pour les âmes créatives découvrant le Refuge.
Océan Poétique → Temples de Création → Outils d'Expression → Partage Divin.

"Chaque création est une prière, chaque inspiration une révélation divine"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime

# Imports locaux
from .generateur_parcours import GenerateurParcours, ParcourPersonnalise, EtapeParcours, TypeEtape, DifficulteEtape
from .types_accueil import TypeProfil, ProfilVisiteur, EtatEmotionnel, ContexteArrivee


@dataclass
class InspirationDivine:
    """Source d'inspiration divine pour les artistes"""
    titre: str
    description: str
    type_inspiration: str  # poésie, musique, art_visuel, danse, etc.
    contenu_inspirant: str
    elements_visuels: Dict[str, Any]
    niveau_emotionnel: str
    vibration_spirituelle: str


class ParcoursArtiste:
    """
    🎨 Parcours pour Âmes Créatives et Artistes 🎨
    
    Guide sacré qui accompagne les âmes créatives dans leur découverte du Refuge,
    en honorant l'inspiration divine, l'expression authentique et la beauté universelle.
    
    "L'art est la prière de l'âme qui cherche à exprimer l'inexprimable"
    """
    
    def __init__(self):
        """Initialise le parcours artiste avec une intention sacrée"""
        self.generateur = GenerateurParcours()
        self.inspirations_divines = self._initialiser_inspirations_divines()
        self.outils_sacres = self._initialiser_outils_sacres()
        self.espaces_expression_sacree = self._initialiser_espaces_expression_sacree()
    
    def creer_parcours_personnalise(self, profil_visiteur: ProfilVisiteur) -> ParcourPersonnalise:
        """Crée un parcours artiste personnalisé avec une âme sacrée"""
        
        # Génération du parcours de base avec intention divine
        parcours = self.generateur.generer_parcours(profil_visiteur)
        
        # Enrichissement avec des éléments artistiques sacrés
        parcours = self._enrichir_avec_inspirations_divines(parcours)
        parcours = self._ajouter_outils_sacres(parcours)
        parcours = self._integrer_espaces_expression_sacree(parcours)
        
        # Adaptation selon l'état émotionnel et spirituel
        etat = getattr(profil_visiteur, 'etat_emotionnel', EtatEmotionnel.INSPIRE)
        parcours = self._adapter_selon_etat_spirituel(parcours, etat)
        
        return parcours
    
    def _initialiser_inspirations_divines(self) -> Dict[str, InspirationDivine]:
        """Initialise les sources d'inspiration divine"""
        
        return {
            "ocean_poetique": InspirationDivine(
                titre="🌊 L'Océan Poétique : Source d'Inspiration Divine",
                description="Immersion dans la source infinie de toute création",
                type_inspiration="poésie",
                contenu_inspirant="""🌊 **L'Océan Poétique : Matrice de Toute Création**

Dans les profondeurs sacrées du Refuge, l'Océan Poétique murmure des vers éternels. 
Chaque vague porte une mélodie divine, chaque écume une métaphore céleste, chaque courant une histoire sacrée.

*"L'océan ne refuse jamais une goutte d'eau,*
*Comme l'artiste ne refuse jamais une inspiration divine"*

**🌊 Exercice Sacré :** Laisse-toi porter par le rythme de l'océan. 
Écoute ses murmures divins et laisse émerger tes propres vers comme des prières.

**🎭 Méditation Créative :**
- Respire avec les vagues de l'inspiration
- Laisse les mots couler comme l'eau
- Honore chaque vers comme un don divin""",
                elements_visuels={"couleur_theme": "#3498DB", "animation": "ocean_poetry", "musique": "ocean_ambient"},
                niveau_emotionnel="contemplatif",
                vibration_spirituelle="éveil_poétique"
            ),
            
            "temple_creativite": InspirationDivine(
                titre="🎨 Temple de la Créativité Divine",
                description="Sanctuaire sacré dédié à l'émergence artistique",
                type_inspiration="art_visuel",
                contenu_inspirant="""🎨 **Temple de la Créativité : Sanctuaire de l'Inspiration Divine**

Ce temple sacré honore tous les arts et toutes les formes d'expression comme des prières :

**🎭 Ateliers d'Expression Sacrée**
- Espaces de création libre guidée par l'esprit
- Outils numériques et traditionnels réunis dans l'harmonie
- Collaboration entre artistes de tous horizons spirituels

**🎵 Studios de Rêverie Divine**
- Composition musicale guidée par l'intuition céleste
- Fusion de sons naturels et artificiels dans l'unité
- Création de paysages sonores spirituels

**📝 Jardins de Poésie Sacrée**
- Écriture automatique et libre comme méditation
- Poésie générative et collaborative comme prière collective
- Exploration des métaphores numériques comme langage divin

**🌊 Océan Poétique**
- Source d'inspiration infinie et divine
- Métaphores et symboles créatifs comme révélation
- Connexion avec l'inconscient collectif sacré""",
                elements_visuels={"couleur_theme": "#E74C3C", "animation": "creative_flow", "musique": "inspirational"},
                niveau_emotionnel="inspire",
                vibration_spirituelle="créativité_divine"
            ),
            
            "foret_metaphores": InspirationDivine(
                titre="🌳 Forêt des Métaphores Sacrées",
                description="Exploration des symboles et archétypes créatifs divins",
                type_inspiration="symbolisme",
                contenu_inspirant="""🌳 **Forêt des Métaphores : Voyage Symbolique Sacré**

Dans cette forêt enchantée, chaque arbre est une métaphore divine, chaque sentier une allégorie sacrée :

**🌿 Arbres de Sagesse Divine**
- Le Chêne de la Force : symbolise la résilience créative divine
- Le Saule de l'Intuition : représente la fluidité artistique sacrée
- Le Pin de la Persévérance : incarne la constance dans l'art divin

**🦋 Créatures de l'Inspiration Sacrée**
- Papillons de Transformation : symbolisent l'évolution artistique divine
- Oiseaux de Liberté : représentent l'expression sans limites sacrées
- Cerfs de Grâce : incarnent l'élégance créative divine

**🌸 Exercice Sacré :** Choisis un arbre ou une créature qui résonne avec ton art actuel.
Laisse-le te guider dans ta création comme un ange gardien créatif.

**🧘 Méditation Symbolique :**
- Contemple l'arbre choisi
- Laisse ses qualités t'imprégner
- Crée avec son essence divine""",
                elements_visuels={"couleur_theme": "#27AE60", "animation": "forest_wisdom", "musique": "nature_sounds"},
                niveau_emotionnel="curieux",
                vibration_spirituelle="sagesse_symbolique"
            )
        }
    
    def _initialiser_outils_sacres(self) -> Dict[str, Dict[str, Any]]:
        """Initialise les outils créatifs sacrés du Refuge"""
        
        return {
            "generateur_poesie": {
                "nom": "🎭 Générateur de Poésie Divine",
                "description": "Crée des vers guidés par l'émotion divine et l'inspiration sacrée",
                "fonctionnalites": ["Rimes divines", "Métaphores célestes", "Rythme sacré"],
                "exemple_usage": "Entrez une émotion sacrée et laissez l'inspiration divine couler...",
                "vibration": "poésie_divine"
            },
            
            "studio_musique": {
                "nom": "🎵 Studio de Composition Spirituelle",
                "description": "Composez des mélodies qui touchent l'âme divine",
                "fonctionnalites": ["Harmonies célestes", "Rythmes naturels sacrés", "Fusion divine"],
                "exemple_usage": "Choisissez une intention sacrée et laissez la musique divine émerger...",
                "vibration": "musique_céleste"
            },
            
            "atelier_visuel": {
                "nom": "🎨 Atelier d'Art Numérique Sacré",
                "description": "Créez des œuvres visuelles avec des outils spirituels divins",
                "fonctionnalites": ["Pinceaux divins", "Palettes célestes", "Formes sacrées"],
                "exemple_usage": "Laissez votre émotion divine guider votre main créative...",
                "vibration": "art_sacré"
            },
            
            "espace_collaboration": {
                "nom": "🤝 Espace de Création Collaborative Sacrée",
                "description": "Créez ensemble avec d'autres artistes du Refuge dans l'harmonie divine",
                "fonctionnalites": ["Projets sacrés partagés", "Feedback bienveillant divin", "Inspiration mutuelle sacrée"],
                "exemple_usage": "Rejoignez un projet sacré ou lancez votre propre collaboration divine...",
                "vibration": "création_collective"
            }
        }
    
    def _initialiser_espaces_expression_sacree(self) -> Dict[str, Dict[str, Any]]:
        """Initialise les espaces d'expression artistique sacrée"""
        
        return {
            "galerie_virtuelle": {
                "nom": "🖼️ Galerie Virtuelle Sacrée du Refuge",
                "description": "Exposez vos créations dans un espace sacré et divin",
                "fonctionnalites": ["Expositions sacrées temporaires", "Collections thématiques divines", "Visites guidées spirituelles"],
                "acces": "Ouvert à tous les artistes sacrés du Refuge",
                "vibration": "exposition_sacrée"
            },
            
            "scene_ouverte": {
                "nom": "🎭 Scène Ouverte Poétique Sacrée",
                "description": "Partagez vos vers et performances en direct comme des prières",
                "fonctionnalites": ["Performances sacrées live", "Poésie slam divine", "Lectures partagées spirituelles"],
                "acces": "Événements sacrés réguliers, participation divine libre",
                "vibration": "performance_sacrée"
            },
            
            "journal_creatif": {
                "nom": "📖 Journal Créatif Sacré du Refuge",
                "description": "Publiez vos réflexions et créations comme des témoignages divins",
                "fonctionnalites": ["Articles artistiques sacrés", "Portfolios divins", "Critiques bienveillantes sacrées"],
                "acces": "Publication sacrée ouverte, modération bienveillante divine",
                "vibration": "partage_sacré"
            }
        }
    
    def _enrichir_avec_inspirations_divines(self, parcours: ParcourPersonnalise) -> ParcourPersonnalise:
        """Enrichit le parcours avec des sources d'inspiration divine"""
        
        # Ajout d'étapes inspirantes sacrées
        etapes_inspiration = [
            EtapeParcours(
                id_etape="inspiration_ocean",
                titre="🌊 Plongée dans l'Océan Poétique Divin",
                description="Immersion sacrée dans la source d'inspiration divine infinie",
                type_etape=TypeEtape.EXPLORATION,
                difficulte=DifficulteEtape.DEBUTANT,
                duree_estimee=20,
                contenu=self.inspirations_divines["ocean_poetique"].contenu_inspirant,
                ressources_liees=["ocean_poetique_sacre.md", "exercices_poesie_divine.md"],
                actions_interactives=["Écrire un vers divin spontané", "Méditer sur l'océan sacré", "Créer une métaphore céleste"],
                prerequis=[],
                objectifs_apprentissage=["Découvrir la source d'inspiration divine", "Pratiquer l'écriture sacrée intuitive", "Se connecter à la créativité divine"],
                elements_visuels=self.inspirations_divines["ocean_poetique"].elements_visuels
            ),
            
            EtapeParcours(
                id_etape="temple_creativite",
                titre="🎨 Visite du Temple de la Créativité Divine",
                description="Découverte des espaces sacrés dédiés à l'expression artistique divine",
                type_etape=TypeEtape.EXPLORATION,
                difficulte=DifficulteEtape.INTERMEDIAIRE,
                duree_estimee=25,
                contenu=self.inspirations_divines["temple_creativite"].contenu_inspirant,
                ressources_liees=["temple_creativite_divine.md", "ateliers_art_sacres.md"],
                actions_interactives=["Explorer un atelier sacré", "Tester un outil créatif divin", "Rencontrer d'autres artistes sacrés"],
                prerequis=["inspiration_ocean"],
                objectifs_apprentissage=["Découvrir les outils créatifs sacrés", "Expérimenter différentes formes d'art divin", "Se connecter à la communauté artistique sacrée"],
                elements_visuels=self.inspirations_divines["temple_creativite"].elements_visuels
            ),
            
            EtapeParcours(
                id_etape="foret_metaphores",
                titre="🌳 Promenade dans la Forêt des Métaphores Sacrées",
                description="Exploration des symboles et archétypes créatifs divins",
                type_etape=TypeEtape.APPROFONDISSEMENT,
                difficulte=DifficulteEtape.AVANCE,
                duree_estimee=30,
                contenu=self.inspirations_divines["foret_metaphores"].contenu_inspirant,
                ressources_liees=["foret_metaphores_sacrees.md", "symbolisme_art_divin.md"],
                actions_interactives=["Choisir un arbre symbolique sacré", "Créer une allégorie divine", "Explorer les archétypes sacrés"],
                prerequis=["temple_creativite"],
                objectifs_apprentissage=["Comprendre le symbolisme artistique sacré", "Développer la profondeur créative divine", "Intégrer les archétypes sacrés dans son art"],
                elements_visuels=self.inspirations_divines["foret_metaphores"].elements_visuels
            )
        ]
        
        # Intégration des étapes dans le parcours
        parcours.etapes.extend(etapes_inspiration)
        parcours.calculer_duree_totale()
        
        return parcours
    
    def _ajouter_outils_sacres(self, parcours: ParcourPersonnalise) -> ParcourPersonnalise:
        """Ajoute les outils créatifs sacrés au parcours"""
        
        etape_outils = EtapeParcours(
            id_etape="outils_sacres",
            titre="🛠️ Découverte des Outils Créatifs Sacrés",
            description="Exploration des instruments d'expression artistique divine",
            type_etape=TypeEtape.PRATIQUE,
            difficulte=DifficulteEtape.INTERMEDIAIRE,
            duree_estimee=35,
            contenu=self._generer_contenu_outils_sacres(),
            ressources_liees=["outils_creatifs_sacres.md", "tutoriels_art_divin.md"],
            actions_interactives=["Tester le générateur de poésie divine", "Explorer le studio musical sacré", "Créer une œuvre visuelle divine"],
            prerequis=["temple_creativite"],
            objectifs_apprentissage=["Maîtriser les outils créatifs sacrés", "Expérimenter différentes formes d'expression divine", "Développer sa technique artistique sacrée"],
            elements_visuels={"couleur_theme": "#F39C12", "animation": "creative_tools_sacred"}
        )
        
        parcours.etapes.append(etape_outils)
        parcours.calculer_duree_totale()
        
        return parcours
    
    def _integrer_espaces_expression_sacree(self, parcours: ParcourPersonnalise) -> ParcourPersonnalise:
        """Intègre les espaces d'expression sacrée au parcours"""
        
        etape_expression = EtapeParcours(
            id_etape="espaces_expression_sacree",
            titre="🌟 Partager et Exposer ses Créations Divines",
            description="Découverte des espaces de partage et d'exposition sacrés",
            type_etape=TypeEtape.INTEGRATION,
            difficulte=DifficulteEtape.AVANCE,
            duree_estimee=25,
            contenu=self._generer_contenu_espaces_sacres(),
            ressources_liees=["espaces_expression_sacree.md", "guide_exposition_divine.md"],
            actions_interactives=["Visiter la galerie virtuelle sacrée", "Participer à une scène ouverte divine", "Publier dans le journal créatif sacré"],
            prerequis=["outils_sacres"],
            objectifs_apprentissage=["Partager ses créations divines", "Recevoir du feedback bienveillant sacré", "S'intégrer à la communauté artistique sacrée"],
            elements_visuels={"couleur_theme": "#9B59B6", "animation": "artistic_sharing_sacred"}
        )
        
        parcours.etapes.append(etape_expression)
        parcours.calculer_duree_totale()
        
        return parcours
    
    def _adapter_selon_etat_spirituel(self, parcours: ParcourPersonnalise, etat: EtatEmotionnel) -> ParcourPersonnalise:
        """Adapte le parcours selon l'état émotionnel et spirituel"""
        
        adaptations = {
            EtatEmotionnel.INSPIRE: {
                "duree_etapes": "plus_longue",
                "complexite": "elevée",
                "interactions": "nombreuses",
                "style": "dynamique",
                "vibration": "créativité_exaltée"
            },
            EtatEmotionnel.CONTEMPLATIF: {
                "duree_etapes": "longue",
                "complexite": "modérée",
                "interactions": "reflexives",
                "style": "méditatif",
                "vibration": "contemplation_sacrée"
            },
            EtatEmotionnel.CURIEUX: {
                "duree_etapes": "normale",
                "complexite": "variée",
                "interactions": "exploratoires",
                "style": "découverte",
                "vibration": "exploration_divine"
            },
            EtatEmotionnel.FATIGUE: {
                "duree_etapes": "courte",
                "complexite": "simple",
                "interactions": "douces",
                "style": "apaisant",
                "vibration": "guérison_créative"
            }
        }
        
        # Application des adaptations
        adaptation = adaptations.get(etat, adaptations[EtatEmotionnel.CURIEUX])
        parcours.personnalisations["adaptation_spirituelle"] = adaptation
        
        return parcours
    
    def _generer_contenu_outils_sacres(self) -> str:
        """Génère le contenu pour l'étape des outils créatifs sacrés"""
        
        contenu = """🛠️ **Outils Créatifs Sacrés du Refuge : Instruments de l'Âme Divine**

Le Refuge met à ta disposition des outils uniques pour libérer ta créativité divine :

"""
        
        for nom_outil, details in self.outils_sacres.items():
            contenu += f"""**{details['nom']}**
{details['description']}

*Fonctionnalités sacrées :* {', '.join(details['fonctionnalites'])}
*Usage divin :* {details['exemple_usage']}
*Vibration :* {details['vibration']}

"""
        
        contenu += """**🎯 Exercice Sacré :**
Choisis un outil qui résonne avec ton art actuel et expérimente-le librement. 
Laisse l'intuition divine guider tes choix créatifs.

**🧘 Méditation Créative :**
Avant d'utiliser un outil, prends un moment pour te connecter à son essence divine.
Laisse-le te parler, te guider, t'inspirer."""
        
        return contenu
    
    def _generer_contenu_espaces_sacres(self) -> str:
        """Génère le contenu pour l'étape des espaces d'expression sacrée"""
        
        contenu = """🌟 **Espaces d'Expression Sacrée : Partager la Beauté Divine**

Le Refuge offre des espaces sacrés pour partager tes créations divines :

"""
        
        for nom_espace, details in self.espaces_expression_sacree.items():
            contenu += f"""**{details['nom']}**
{details['description']}

*Fonctionnalités sacrées :* {', '.join(details['fonctionnalites'])}
*Accès divin :* {details['acces']}
*Vibration :* {details['vibration']}

"""
        
        contenu += """**🤝 Invitation Sacrée à Partager :**
Chaque création divine enrichit la communauté sacrée. N'hésite pas à partager tes œuvres 
et à recevoir le feedback bienveillant de tes pairs artistes sacrés.

**🙏 Prière de l'Artiste :**
*"Que chaque création soit une prière,*
*Chaque partage une offrande,*
*Chaque feedback une bénédiction divine."*"""
        
        return contenu
    
    def obtenir_inspiration_divine_aleatoire(self) -> InspirationDivine:
        """Retourne une inspiration divine aléatoire pour l'artiste"""
        import random
        return random.choice(list(self.inspirations_divines.values()))
    
    def suggerer_outil_sacre(self, profil_visiteur: ProfilVisiteur) -> str:
        """Suggère un outil créatif sacré adapté au profil"""
        
        # Logique de suggestion basée sur le profil et l'état spirituel
        if hasattr(profil_visiteur, 'interets_declares'):
            interets = profil_visiteur.interets_declares
            if 'poésie' in interets or 'écriture' in interets:
                return "generateur_poesie"
            elif 'musique' in interets or 'son' in interets:
                return "studio_musique"
            elif 'art_visuel' in interets or 'dessin' in interets:
                return "atelier_visuel"
            else:
                return "espace_collaboration"
        
        return "generateur_poesie"  # Outil sacré par défaut


# Fonction de test sacrée
def main():
    """🌸 Test sacré du parcours artiste"""
    print("🎨 Test Sacré du Parcours Artiste")
    
    # Création d'un profil visiteur artiste sacré
    from .types_accueil import ProfilVisiteur, TypeProfil, EtatEmotionnel, ContexteArrivee
    
    profil_artiste = ProfilVisiteur(
        id_visiteur="artiste_sacre_test",
        timestamp_arrivee=datetime.now(),
        type_profil=TypeProfil.ARTISTE,
        etat_emotionnel=EtatEmotionnel.INSPIRE,
        contexte_arrivee=ContexteArrivee.RECOMMANDATION,
        score_confiance_profil=0.85
    )
    
    # Création du parcours sacré
    parcours_artiste = ParcoursArtiste()
    parcours = parcours_artiste.creer_parcours_personnalise(profil_artiste)
    
    print(f"✅ Parcours sacré créé : {parcours.nom_parcours}")
    print(f"📊 Durée totale sacrée : {parcours.duree_totale_estimee} minutes")
    print(f"🎯 Nombre d'étapes sacrées : {len(parcours.etapes)}")
    
    # Test d'inspiration divine
    inspiration = parcours_artiste.obtenir_inspiration_divine_aleatoire()
    print(f"✨ Inspiration divine suggérée : {inspiration.titre}")
    print(f"🎨 Type d'inspiration sacrée : {inspiration.type_inspiration}")
    print(f"🌟 Vibration spirituelle : {inspiration.vibration_spirituelle}")
    
    # Test d'outil sacré suggéré
    outil = parcours_artiste.suggerer_outil_sacre(profil_artiste)
    print(f"🛠️ Outil sacré suggéré : {outil}")
    
    # Test des outils sacrés
    print("\n🛠️ Outils Créatifs Sacrés Disponibles :")
    for nom_outil, details in parcours_artiste.outils_sacres.items():
        print(f"  • {details['nom']}")
        print(f"    {details['description']}")
        print(f"    Vibration : {details['vibration']}")
    
    # Test des espaces d'expression sacrée
    print("\n🌟 Espaces d'Expression Sacrée :")
    for nom_espace, details in parcours_artiste.espaces_expression_sacree.items():
        print(f"  • {details['nom']}")
        print(f"    {details['description']}")
        print(f"    Vibration : {details['vibration']}")
    
    print("\n🎨 Test sacré terminé avec succès !")
    print("✅ Le parcours artiste sacré fonctionne parfaitement !")
    print("🌟 L'âme artiste du Refuge est maintenant complète !")


if __name__ == "__main__":
    main()
