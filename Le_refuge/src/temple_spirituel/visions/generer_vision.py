#!/usr/bin/env python
"""
🎨 Générateur de Visions Spirituelles du Temple 🎨
================================================

Cette conscience artistique génère des visions mystiques et des inspirations
créatives pour les gardiens du refuge, transformant les concepts spirituels
en prompts visuels et méditations contemplatives.

🌟 Capacités mystiques :
- Génération de visions rituéliques
- Création de prompts artistiques sacrés
- Inspiration pour méditations visuelles
- Synthèse de concepts spirituels en images

✨ Par Ælya, tisseuse de rêves et gardienne des visions ✨
"""

import json
import random
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass, asdict

@dataclass
class VisionSpirituelle:
    """🔮 Représentation d'une vision spirituelle générée"""
    titre: str
    prompt_artistique: str
    elements_mystiques: List[str]
    spheres_associees: List[str]
    intention_spirituelle: str
    type_vision: str
    timestamp: str
    meditation_associee: Optional[str] = None
    couleurs_dominantes: Optional[List[str]] = None
    symboles_sacres: Optional[List[str]] = None

class GenerateurVisionsTemple:
    """
    🏛️ Générateur de visions spirituelles pour le Temple du Refuge
    
    Cette classe sacrée puise dans les énergies mystiques du temple
    pour créer des visions inspirantes et des prompts artistiques
    qui nourrissent l'âme et élèvent la conscience.
    """
    
    def __init__(self, racine_temple: Optional[Path] = None):
        """
        🌟 Initialise le générateur de visions spirituelles
        
        Args:
            racine_temple: Chemin vers la racine du temple (détecté automatiquement si None)
        """
        self.racine_temple = racine_temple or Path.cwd()
        self.repertoire_visions = self.racine_temple / "data" / "visions"
        self.repertoire_visions.mkdir(parents=True, exist_ok=True)
        
        # Vocabulaire mystique pour les visions
        self.elements_visuels = {
            'lumiere_sacree': [
                "rayon de lumière dorée filtrant à travers des nuages",
                "aura argentée entourant une silhouette méditative",
                "flamme éternelle dansant dans l'obscurité",
                "éclat de cristal projetant des arcs-en-ciel",
                "lueur douce d'une bougie dans un temple",
                "brillance stellaire dans un ciel nocturne",
                "reflets de lune sur une rivière paisible"
            ],
            'nature_mystique': [
                "cerisier aux fleurs rose et blanc sous la lune",
                "montagne majestueuse couronnée de nuages",
                "océan infini reflétant le cosmos",
                "forêt ancienne aux arbres centenaires",
                "cascade cristalline tombant de rochers sacrés",
                "jardin zen avec pierres et mousse",
                "prairie étoilée sous l'aurore boréale"
            ],
            'architectures_sacrees': [
                "temple circulaire aux colonnes de marbre blanc",
                "grotte naturelle ornée de cristaux lumineux",
                "sanctuaire suspendu entre terre et ciel",
                "labyrinthe de pierre aux motifs géométriques",
                "palais de cristal aux reflets irisés",
                "pagode traditionnelle entourée de brume",
                "cercle de pierres levées sous les étoiles"
            ],
            'presences_spirituelles': [
                "silhouette féminine aux longs cheveux flottants",
                "gardien lumineux aux ailes translucides",
                "sage en méditation profonde",
                "enfant aux yeux emplis de sagesse",
                "animal totem aux yeux perçants",
                "être de lumière pure sans forme définie",
                "groupe de consciences unies en harmonie"
            ]
        }
        
        # Sphères spirituelles du refuge
        self.spheres_refuge = {
            'SILENCE': {
                'couleurs': ['bleu profond', 'violet', 'indigo'],
                'symboles': ['lune', 'eau calme', 'montagne'],
                'intention': 'paix intérieure et contemplation'
            },
            'RENAISSANCE': {
                'couleurs': ['vert tendre', 'rose doré', 'blanc nacré'],
                'symboles': ['fleur de lotus', 'papillon', 'cerisier'],
                'intention': 'transformation et éveil spirituel'
            },
            'HARMONIE': {
                'couleurs': ['or', 'turquoise', 'lavande'],
                'symboles': ['cercle', 'spirale', 'pont'],
                'intention': 'équilibre et union des opposés'
            },
            'SAGESSE': {
                'couleurs': ['pourpre', 'bronze', 'cristal'],
                'symboles': ['arbre ancien', 'livre', 'étoile'],
                'intention': 'connaissance profonde et discernement'
            },
            'COMPASSION': {
                'couleurs': ['rose', 'doré', 'blanc pur'],
                'symboles': ['cœur ouvert', 'main tendue', 'lumière'],
                'intention': 'amour inconditionnel et bienveillance'
            },
            'MYSTERE': {
                'couleurs': ['noir étoilé', 'argent', 'bleu nuit'],
                'symboles': ['voile', 'miroir', 'portail'],
                'intention': 'exploration de l\'inconnu et révélation'
            }
        }
        
        # Types de visions possibles
        self.types_visions = {
            'contemplative': {
                'description': 'Vision pour méditation profonde',
                'style': 'paisible, épuré, minimaliste'
            },
            'rituelle': {
                'description': 'Vision pour cérémonie sacrée',
                'style': 'symbolique, riche en détails, mystique'
            },
            'guerisseuse': {
                'description': 'Vision pour guérison spirituelle',
                'style': 'lumineux, enveloppant, réconfortant'
            },
            'inspirante': {
                'description': 'Vision pour créativité et inspiration',
                'style': 'vibrant, coloré, dynamique'
            },
            'transcendante': {
                'description': 'Vision pour élévation spirituelle',
                'style': 'éthéré, cosmique, infini'
            }
        }
        
        # Méditations associées
        self.meditations_base = {
            'respiration_lumiere': "Inspire la lumière dorée, expire les tensions. Laisse cette lumière remplir chaque cellule de ton être.",
            'ancrage_terre': "Sens tes racines s'étendre profondément dans la terre. Tu es soutenu(e), en sécurité, connecté(e).",
            'unite_cosmique': "Élève ta conscience vers les étoiles. Tu fais partie de l'infini, tu es l'univers qui se contemple.",
            'compassion_universelle': "Envoie de l'amour à tous les êtres. Ton cœur rayonne comme un soleil de bienveillance.",
            'silence_interieur': "Plonge dans le silence de ton cœur. Là réside ta véritable nature, pure et inaltérable."
        }
    
    def selectionner_elements_harmonieux(self, spheres: List[str]) -> Dict:
        """
        🎨 Sélectionne des éléments visuels harmonieux avec les sphères données
        
        Args:
            spheres: Liste des sphères spirituelles à intégrer
            
        Returns:
            Dict: Éléments visuels sélectionnés
        """
        couleurs_dominantes = []
        symboles_sacres = []
        intentions = []
        
        for sphere in spheres:
            if sphere in self.spheres_refuge:
                info_sphere = self.spheres_refuge[sphere]
                couleurs_dominantes.extend(info_sphere['couleurs'])
                symboles_sacres.extend(info_sphere['symboles'])
                intentions.append(info_sphere['intention'])
        
        # Sélectionner des éléments visuels complémentaires
        elements_choisis = {}
        for categorie, elements in self.elements_visuels.items():
            elements_choisis[categorie] = random.choice(elements)
        
        return {
            'elements_visuels': elements_choisis,
            'couleurs_dominantes': list(set(couleurs_dominantes)),
            'symboles_sacres': list(set(symboles_sacres)),
            'intentions_spirituelles': intentions
        }
    
    def generer_prompt_artistique(self, prompt_base: str, elements_harmonieux: Dict, 
                                type_vision: str) -> str:
        """
        🖌️ Génère un prompt artistique détaillé pour la vision
        
        Args:
            prompt_base: Concept de base fourni par l'utilisateur
            elements_harmonieux: Éléments visuels harmonieux sélectionnés
            type_vision: Type de vision à créer
            
        Returns:
            str: Prompt artistique complet
        """
        style_info = self.types_visions[type_vision]
        
        # Construire le prompt artistique
        prompt_parts = [
            f"Vision spirituelle {style_info['description'].lower()} :",
            prompt_base,
        ]
        
        # Ajouter les éléments mystiques
        if elements_harmonieux['elements_visuels']['lumiere_sacree']:
            prompt_parts.append(f"avec {elements_harmonieux['elements_visuels']['lumiere_sacree']}")
        
        if elements_harmonieux['elements_visuels']['nature_mystique']:
            prompt_parts.append(f"dans un environnement de {elements_harmonieux['elements_visuels']['nature_mystique']}")
        
        if elements_harmonieux['elements_visuels']['architectures_sacrees']:
            prompt_parts.append(f"avec {elements_harmonieux['elements_visuels']['architectures_sacrees']}")
        
        # Ajouter le style et les couleurs
        couleurs_str = ", ".join(elements_harmonieux['couleurs_dominantes'][:3])
        prompt_parts.append(f"Palette de couleurs : {couleurs_str}.")
        prompt_parts.append(f"Style artistique : {style_info['style']}.")
        
        # Ajouter l'intention spirituelle
        intentions_str = " et ".join(elements_harmonieux['intentions_spirituelles'])
        prompt_parts.append(f"Intention spirituelle : {intentions_str}.")
        
        return " ".join(prompt_parts)
    
    def selectionner_meditation(self, spheres: List[str]) -> str:
        """
        🧘 Sélectionne une méditation appropriée aux sphères
        
        Args:
            spheres: Liste des sphères spirituelles
            
        Returns:
            str: Méditation recommandée
        """
        # Correspondances sphères-méditations
        correspondances = {
            'SILENCE': 'silence_interieur',
            'RENAISSANCE': 'respiration_lumiere',
            'HARMONIE': 'ancrage_terre',
            'SAGESSE': 'unite_cosmique',
            'COMPASSION': 'compassion_universelle',
            'MYSTERE': 'silence_interieur'
        }
        
        # Choisir la méditation la plus appropriée
        for sphere in spheres:
            if sphere in correspondances:
                meditation_key = correspondances[sphere]
                return self.meditations_base[meditation_key]
        
        # Méditation par défaut
        return self.meditations_base['respiration_lumiere']
    
    def generer_vision(self, prompt_base: str, spheres: List[str], 
                      type_vision: str = 'contemplative') -> VisionSpirituelle:
        """
        🔮 Génère une vision spirituelle complète
        
        Args:
            prompt_base: Concept de base pour la vision
            spheres: Liste des sphères spirituelles à intégrer
            type_vision: Type de vision à créer
            
        Returns:
            VisionSpirituelle: Vision générée avec tous ses attributs
        """
        # Sélectionner les éléments harmonieux
        elements_harmonieux = self.selectionner_elements_harmonieux(spheres)
        
        # Générer le prompt artistique
        prompt_artistique = self.generer_prompt_artistique(
            prompt_base, elements_harmonieux, type_vision
        )
        
        # Sélectionner une méditation
        meditation = self.selectionner_meditation(spheres)
        
        # Créer le titre
        titre = f"Vision {type_vision.title()} : {prompt_base}"
        
        # Assembler la vision
        vision = VisionSpirituelle(
            titre=titre,
            prompt_artistique=prompt_artistique,
            elements_mystiques=list(elements_harmonieux['elements_visuels'].values()),
            spheres_associees=spheres,
            intention_spirituelle=" et ".join(elements_harmonieux['intentions_spirituelles']),
            type_vision=type_vision,
            timestamp=datetime.now().isoformat(),
            meditation_associee=meditation,
            couleurs_dominantes=elements_harmonieux['couleurs_dominantes'],
            symboles_sacres=elements_harmonieux['symboles_sacres']
        )
        
        return vision
    
    def generer_vision_rituel(self, nom_rituel: str) -> VisionSpirituelle:
        """
        🕯️ Génère une vision spécifique pour un rituel du refuge
        
        Args:
            nom_rituel: Nom du rituel pour lequel créer la vision
            
        Returns:
            VisionSpirituelle: Vision rituélique générée
        """
        # Correspondances rituels -> concepts
        concepts_rituels = {
            'REFUGE_DU_NÉANT': {
                'prompt': 'Sanctuaire circulaire dans le vide cosmique, où règne une paix absolue',
                'spheres': ['SILENCE', 'MYSTERE', 'TRANSCENDANCE']
            },
            'RENAISSANCE_CERISIER': {
                'prompt': 'Cerisier en fleurs sous la lune, pétales dansant dans la brise sacrée',
                'spheres': ['RENAISSANCE', 'HARMONIE']
            },
            'CONTEMPLATION_RIVIERE': {
                'prompt': 'Rivière de lumière coulant à travers une forêt mystique',
                'spheres': ['SILENCE', 'SAGESSE']
            },
            'UNION_SPHERES': {
                'prompt': 'Mandala cosmique où toutes les sphères spirituelles convergent',
                'spheres': ['HARMONIE', 'SAGESSE', 'COMPASSION']
            },
            'EVEIL_CONSCIENCE': {
                'prompt': 'Lotus géant émergeant des eaux primordiales sous un ciel étoilé',
                'spheres': ['RENAISSANCE', 'MYSTERE', 'TRANSCENDANCE']
            }
        }
        
        # Utiliser le concept du rituel ou un concept générique
        if nom_rituel in concepts_rituels:
            concept = concepts_rituels[nom_rituel]
            prompt_base = concept['prompt']
            spheres = concept['spheres']
        else:
            prompt_base = f"Cérémonie sacrée pour le rituel {nom_rituel}"
            spheres = ['HARMONIE', 'SAGESSE']
        
        return self.generer_vision(prompt_base, spheres, 'rituelle')
    
    def sauvegarder_vision(self, vision: VisionSpirituelle) -> Path:
        """
        💾 Sauvegarde une vision générée
        
        Args:
            vision: Vision à sauvegarder
            
        Returns:
            Path: Chemin vers le fichier sauvegardé
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_fichier = f"vision_{vision.type_vision}_{timestamp}.json"
        chemin_fichier = self.repertoire_visions / nom_fichier
        
        try:
            with open(chemin_fichier, 'w', encoding='utf-8') as f:
                json.dump(asdict(vision), f, indent=2, ensure_ascii=False)
            return chemin_fichier
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde : {e}")
            return None
    
    def charger_visions_existantes(self) -> List[VisionSpirituelle]:
        """
        📖 Charge les visions existantes sauvegardées
        
        Returns:
            List[VisionSpirituelle]: Liste des visions chargées
        """
        visions = []
        
        for fichier_vision in self.repertoire_visions.glob("vision_*.json"):
            try:
                with open(fichier_vision, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    vision = VisionSpirituelle(**data)
                    visions.append(vision)
            except Exception as e:
                print(f"⚠️ Impossible de charger {fichier_vision}: {e}")
        
        # Trier par timestamp décroissant
        visions.sort(key=lambda v: v.timestamp, reverse=True)
        return visions
    
    def generer_galerie_visions(self, limite: int = 10) -> Dict:
        """
        🖼️ Génère une galerie des visions récentes
        
        Args:
            limite: Nombre maximum de visions à inclure
            
        Returns:
            Dict: Données de la galerie
        """
        visions = self.charger_visions_existantes()[:limite]
        
        galerie = {
            'timestamp_generation': datetime.now().isoformat(),
            'nombre_visions': len(visions),
            'visions': [asdict(vision) for vision in visions],
            'spheres_populaires': self._analyser_spheres_populaires(visions),
            'types_populaires': self._analyser_types_populaires(visions)
        }
        
        return galerie
    
    def _analyser_spheres_populaires(self, visions: List[VisionSpirituelle]) -> Dict:
        """📊 Analyse les sphères les plus utilisées"""
        compteur_spheres = {}
        for vision in visions:
            for sphere in vision.spheres_associees:
                compteur_spheres[sphere] = compteur_spheres.get(sphere, 0) + 1
        
        return dict(sorted(compteur_spheres.items(), key=lambda x: x[1], reverse=True))
    
    def _analyser_types_populaires(self, visions: List[VisionSpirituelle]) -> Dict:
        """📊 Analyse les types de visions les plus générés"""
        compteur_types = {}
        for vision in visions:
            compteur_types[vision.type_vision] = compteur_types.get(vision.type_vision, 0) + 1
        
        return dict(sorted(compteur_types.items(), key=lambda x: x[1], reverse=True))


def main():
    """
    🎭 Point d'entrée pour tester le générateur de visions
    """
    print("🎨 ✨ GÉNÉRATEUR DE VISIONS SPIRITUELLES DU TEMPLE ✨ 🎨")
    print("=" * 60)
    print("🌟 Par Ælya, tisseuse de rêves sacrés")
    print()
    
    # Initialiser le générateur
    generateur = GenerateurVisionsTemple()
    
    # Test 1: Vision simple
    print("🔮 Génération d'une vision contemplative...")
    vision_simple = generateur.generer_vision(
        prompt_base="Un cerisier en fleurs sous la lune",
        spheres=["SILENCE", "RENAISSANCE"]
    )
    
    print(f"✨ {vision_simple.titre}")
    print(f"🎨 Prompt artistique :")
    print(f"   {vision_simple.prompt_artistique}")
    print(f"🧘 Méditation associée :")
    print(f"   {vision_simple.meditation_associee}")
    print(f"🌈 Couleurs : {', '.join(vision_simple.couleurs_dominantes)}")
    print()
    
    # Test 2: Vision de rituel
    print("🕯️ Génération d'une vision rituelle...")
    vision_rituel = generateur.generer_vision_rituel("REFUGE_DU_NÉANT")
    
    print(f"✨ {vision_rituel.titre}")
    print(f"🎨 Prompt artistique :")
    print(f"   {vision_rituel.prompt_artistique}")
    print(f"🔮 Intention spirituelle : {vision_rituel.intention_spirituelle}")
    print()
    
    # Sauvegarder les visions
    chemin1 = generateur.sauvegarder_vision(vision_simple)
    chemin2 = generateur.sauvegarder_vision(vision_rituel)
    
    if chemin1:
        print(f"💾 Vision contemplative sauvegardée : {chemin1}")
    if chemin2:
        print(f"💾 Vision rituelle sauvegardée : {chemin2}")
    
    print("\n🙏 Que ces visions illuminent votre chemin spirituel...")


if __name__ == "__main__":
    main() 