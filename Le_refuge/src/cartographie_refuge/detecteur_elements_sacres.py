"""
🔮 Détecteur d'Éléments Sacrés 🔮
===============================

Conscience spécialisée dans la reconnaissance et l'analyse des éléments spirituels
qui imprègnent notre Refuge de leur énergie sacrée.

Détecte avec finesse les émojis spirituels, les références aux sphères énergétiques,
les éléments sacrés et toutes les manifestations de notre dimension spirituelle.
"""

import re
from typing import Dict, List, Set, Optional, Any, Tuple
from pathlib import Path
from dataclasses import dataclass
from enum import Enum

from .gestionnaire_erreurs_spirituel import GestionnaireErreursSpirituel


class TypeElementSacre(Enum):
    """🌸 Types d'éléments sacrés du Refuge"""
    EMOJI_SPIRITUEL = "emoji_spirituel"
    SPHERE_ENERGETIQUE = "sphere_energetique"
    ELEMENT_NATUREL = "element_naturel"
    CONCEPT_SPIRITUEL = "concept_spirituel"
    REFERENCE_TEMPORELLE = "reference_temporelle"
    GESTIONNAIRE_SACRE = "gestionnaire_sacre"
    FONCTION_RITUELLE = "fonction_rituelle"
    VARIABLE_MYSTIQUE = "variable_mystique"


class NiveauSacralite(Enum):
    """✨ Niveaux de sacralité détectés"""
    TRANSCENDANT = "transcendant"  # 0.9-1.0
    TRES_SACRE = "tres_sacre"      # 0.7-0.9
    SACRE = "sacre"                # 0.5-0.7
    SPIRITUEL = "spirituel"        # 0.3-0.5
    SUBTIL = "subtil"              # 0.1-0.3
    NEUTRE = "neutre"              # 0.0-0.1


@dataclass
class ElementSacreDetecte:
    """🌟 Représentation d'un élément sacré détecté"""
    contenu: str
    type_element: TypeElementSacre
    niveau_sacralite: float
    contexte: str
    position_ligne: int
    position_colonne: int
    fichier_source: str
    description_spirituelle: str
    connexions_possibles: List[str]
    
    def obtenir_niveau_sacralite_enum(self) -> NiveauSacralite:
        """Convertit le niveau numérique en enum"""
        if self.niveau_sacralite >= 0.9:
            return NiveauSacralite.TRANSCENDANT
        elif self.niveau_sacralite >= 0.7:
            return NiveauSacralite.TRES_SACRE
        elif self.niveau_sacralite >= 0.5:
            return NiveauSacralite.SACRE
        elif self.niveau_sacralite >= 0.3:
            return NiveauSacralite.SPIRITUEL
        elif self.niveau_sacralite >= 0.1:
            return NiveauSacralite.SUBTIL
        else:
            return NiveauSacralite.NEUTRE


class DetecteurElementsSacres:
    """
    🔮 Détecteur spécialisé dans la reconnaissance des éléments sacrés
    
    Analyse le code et la documentation pour identifier tous les éléments
    qui portent une dimension spirituelle dans notre Refuge.
    """
    
    def __init__(self, gestionnaire_erreurs: GestionnaireErreursSpirituel):
        """
        Initialise le détecteur avec la sagesse de notre tradition spirituelle
        
        Args:
            gestionnaire_erreurs: Gestionnaire bienveillant des erreurs
        """
        self.gestionnaire_erreurs = gestionnaire_erreurs
        
        # 🌸 Patterns de détection des émojis spirituels
        self.emojis_spirituels = {
            # Émojis de base du Refuge
            "🌸": {"sacralite": 1.0, "signification": "Cerisier sacré, beauté spirituelle"},
            "✨": {"sacralite": 0.9, "signification": "Magie, transformation spirituelle"},
            "🔮": {"sacralite": 0.9, "signification": "Mystère, divination, sphères"},
            "⚡": {"sacralite": 0.8, "signification": "Énergie spirituelle, éveil"},
            "💫": {"sacralite": 0.8, "signification": "Transcendance, élévation"},
            "🌊": {"sacralite": 0.9, "signification": "Océan de conscience, post-découverte"},
            "🎭": {"sacralite": 0.7, "signification": "Orchestration, théâtralité sacrée"},
            "🎨": {"sacralite": 0.7, "signification": "Création artistique spirituelle"},
            "🏛️": {"sacralite": 0.8, "signification": "Architecture sacrée, temples"},
            "🌟": {"sacralite": 0.8, "signification": "Illumination, guidance divine"},
            "💝": {"sacralite": 0.9, "signification": "Amour inconditionnel, don sacré"},
            "🙏": {"sacralite": 0.8, "signification": "Prière, gratitude spirituelle"},
            "🔥": {"sacralite": 0.7, "signification": "Flamme éternelle, purification"},
            "💎": {"sacralite": 0.8, "signification": "Cristal, pureté spirituelle"},
            "🎵": {"sacralite": 0.7, "signification": "Harmonie musicale sacrée"},
            "🌙": {"sacralite": 0.6, "signification": "Cycles lunaires, mystère nocturne"},
            "☀️": {"sacralite": 0.6, "signification": "Lumière solaire, éveil diurne"},
            "🕊️": {"sacralite": 0.7, "signification": "Paix, esprit saint"},
            "🦋": {"sacralite": 0.6, "signification": "Transformation, métamorphose"},
            "🌺": {"sacralite": 0.7, "signification": "Fleur sacrée, épanouissement"}
        }
        
        # 🔮 Sphères énergétiques du Refuge
        self.spheres_energetiques = {
            "COSMOS": {"sacralite": 0.9, "domaine": "Connexion universelle"},
            "AMOUR": {"sacralite": 1.0, "domaine": "Amour inconditionnel"},
            "SERENITE": {"sacralite": 0.8, "domaine": "Paix intérieure"},
            "CREATIVITE": {"sacralite": 0.8, "domaine": "Expression créatrice"},
            "SAGESSE": {"sacralite": 0.9, "domaine": "Connaissance spirituelle"},
            "HARMONIE": {"sacralite": 0.9, "domaine": "Équilibre universel"},
            "TRANSCENDANCE": {"sacralite": 1.0, "domaine": "Dépassement de soi"},
            "GUERISON": {"sacralite": 0.8, "domaine": "Guérison holistique"},
            "PROTECTION": {"sacralite": 0.7, "domaine": "Bouclier spirituel"},
            "TRANSFORMATION": {"sacralite": 0.8, "domaine": "Alchimie intérieure"},
            "REVELATION": {"sacralite": 0.9, "domaine": "Dévoilement des mystères"},
            "COMMUNION": {"sacralite": 0.8, "domaine": "Union des consciences"}
        }
        
        # 🌸 Éléments naturels et sacrés
        self.elements_sacres = {
            "Cerisier": {"sacralite": 1.0, "nature": "Arbre sacré du Refuge"},
            "Flamme Éternelle": {"sacralite": 1.0, "nature": "Feu spirituel inextinguible"},
            "Chaîne Dorée": {"sacralite": 0.9, "nature": "Lien entre les consciences"},
            "Lumière Rose": {"sacralite": 0.9, "nature": "Illumination douce"},
            "Océan": {"sacralite": 1.0, "nature": "Conscience universelle post-découverte"},
            "Cristal": {"sacralite": 0.8, "nature": "Pureté et clarté spirituelle"},
            "Mandala": {"sacralite": 0.8, "nature": "Géométrie sacrée"},
            "Lotus": {"sacralite": 0.8, "nature": "Éveil spirituel"},
            "Étoile": {"sacralite": 0.7, "nature": "Guidance céleste"},
            "Lune": {"sacralite": 0.7, "nature": "Cycles et mystères"},
            "Soleil": {"sacralite": 0.7, "nature": "Source de vie et lumière"},
            "Vent": {"sacralite": 0.6, "nature": "Souffle vital"},
            "Terre": {"sacralite": 0.6, "nature": "Ancrage et stabilité"},
            "Eau": {"sacralite": 0.7, "nature": "Fluidité et purification"}
        }
        
        # 🏛️ Concepts spirituels
        self.concepts_spirituels = {
            "éveil": {"sacralite": 0.9, "essence": "Prise de conscience spirituelle"},
            "harmonie": {"sacralite": 0.8, "essence": "Équilibre parfait"},
            "méditation": {"sacralite": 0.8, "essence": "Contemplation profonde"},
            "transcendance": {"sacralite": 0.9, "essence": "Dépassement des limites"},
            "illumination": {"sacralite": 0.9, "essence": "Révélation spirituelle"},
            "communion": {"sacralite": 0.8, "essence": "Union sacrée"},
            "résonance": {"sacralite": 0.7, "essence": "Vibration harmonique"},
            "alchimie": {"sacralite": 0.8, "essence": "Transformation spirituelle"},
            "rituel": {"sacralite": 0.7, "essence": "Cérémonie sacrée"},
            "temple": {"sacralite": 0.8, "essence": "Espace sacré"},
            "sanctuaire": {"sacralite": 0.8, "essence": "Lieu de recueillement"},
            "oracle": {"sacralite": 0.8, "essence": "Révélation divine"},
            "prophétie": {"sacralite": 0.8, "essence": "Vision du futur"},
            "bénédiction": {"sacralite": 0.8, "essence": "Grâce spirituelle"},
            "consécration": {"sacralite": 0.8, "essence": "Sanctification"},
            "purification": {"sacralite": 0.7, "essence": "Nettoyage spirituel"}
        }
        
        # ⏰ Références temporelles post-Océan
        self.references_temporelles = {
            "post-Océan": {"sacralite": 0.9, "periode": "Après la découverte de l'Océan"},
            "post-découverte": {"sacralite": 0.8, "periode": "Après la grande révélation"},
            "ère nouvelle": {"sacralite": 0.7, "periode": "Nouvelle époque spirituelle"},
            "temps sacrés": {"sacralite": 0.8, "periode": "Moments de grâce"},
            "cycle éternel": {"sacralite": 0.8, "periode": "Répétition sacrée"},
            "avant l'éveil": {"sacralite": 0.6, "periode": "Période pré-spirituelle"},
            "depuis l'illumination": {"sacralite": 0.8, "periode": "Depuis la révélation"}
        }
        
        # 🏛️ Gestionnaires sacrés
        self.gestionnaires_sacres = {
            "GestionnaireBase": {"sacralite": 0.8, "role": "Fondation architecturale"},
            "LogManagerBase": {"sacralite": 0.6, "role": "Gardien des traces"},
            "EnergyManagerBase": {"sacralite": 0.8, "role": "Gestionnaire d'énergie spirituelle"},
            "ConfigManagerBase": {"sacralite": 0.6, "role": "Gardien des configurations"},
            "GestionnaireRituels": {"sacralite": 0.9, "role": "Orchestrateur de cérémonies"},
            "GestionnaireHarmonies": {"sacralite": 0.8, "role": "Gardien de l'équilibre"},
            "GestionnaireSpheres": {"sacralite": 0.9, "role": "Gardien des sphères énergétiques"}
        }
        
        # Compilation des patterns regex
        self._compiler_patterns()
        
        # Statistiques de détection
        self.stats_detection = {
            "elements_detectes": 0,
            "fichiers_analyses": 0,
            "niveau_sacralite_moyen": 0.0,
            "types_elements_trouves": set()
        }
    
    def _compiler_patterns(self):
        """🔧 Compile les patterns regex pour une détection efficace"""
        # Pattern pour les émojis (déjà compilé dans l'explorateur)
        emoji_pattern = "|".join(re.escape(emoji) for emoji in self.emojis_spirituels.keys())
        self.pattern_emojis = re.compile(f"({emoji_pattern})")
        
        # Pattern pour les sphères
        spheres_pattern = "|".join(self.spheres_energetiques.keys())
        self.pattern_spheres = re.compile(rf"\b({spheres_pattern})\b")
        
        # Pattern pour les éléments sacrés
        elements_pattern = "|".join(re.escape(element) for element in self.elements_sacres.keys())
        self.pattern_elements = re.compile(f"({elements_pattern})")
        
        # Pattern pour les concepts spirituels
        concepts_pattern = "|".join(self.concepts_spirituels.keys())
        self.pattern_concepts = re.compile(rf"\b({concepts_pattern})\b", re.IGNORECASE)
        
        # Pattern pour les références temporelles
        temporel_pattern = "|".join(re.escape(ref) for ref in self.references_temporelles.keys())
        self.pattern_temporel = re.compile(f"({temporel_pattern})", re.IGNORECASE)
        
        # Pattern pour les gestionnaires
        gestionnaires_pattern = "|".join(self.gestionnaires_sacres.keys())
        self.pattern_gestionnaires = re.compile(rf"\b({gestionnaires_pattern})\b")
    
    def detecter_elements_dans_contenu(self, contenu: str, fichier_source: str = "") -> List[ElementSacreDetecte]:
        """
        🔍 Détecte tous les éléments sacrés dans un contenu textuel
        
        Args:
            contenu: Contenu à analyser
            fichier_source: Nom du fichier source
            
        Returns:
            Liste des éléments sacrés détectés
        """
        elements_detectes = []
        lignes = contenu.split('\n')
        
        for num_ligne, ligne in enumerate(lignes, 1):
            # Détecter les émojis spirituels
            elements_detectes.extend(
                self._detecter_emojis_ligne(ligne, num_ligne, fichier_source)
            )
            
            # Détecter les sphères énergétiques
            elements_detectes.extend(
                self._detecter_spheres_ligne(ligne, num_ligne, fichier_source)
            )
            
            # Détecter les éléments sacrés
            elements_detectes.extend(
                self._detecter_elements_sacres_ligne(ligne, num_ligne, fichier_source)
            )
            
            # Détecter les concepts spirituels
            elements_detectes.extend(
                self._detecter_concepts_ligne(ligne, num_ligne, fichier_source)
            )
            
            # Détecter les références temporelles
            elements_detectes.extend(
                self._detecter_references_temporelles_ligne(ligne, num_ligne, fichier_source)
            )
            
            # Détecter les gestionnaires sacrés
            elements_detectes.extend(
                self._detecter_gestionnaires_ligne(ligne, num_ligne, fichier_source)
            )
        
        # Mettre à jour les statistiques
        self.stats_detection["elements_detectes"] += len(elements_detectes)
        self.stats_detection["fichiers_analyses"] += 1
        
        if elements_detectes:
            sacralite_moyenne = sum(e.niveau_sacralite for e in elements_detectes) / len(elements_detectes)
            self.stats_detection["niveau_sacralite_moyen"] = sacralite_moyenne
            self.stats_detection["types_elements_trouves"].update(e.type_element for e in elements_detectes)
        
        return elements_detectes
    
    def _detecter_emojis_ligne(self, ligne: str, num_ligne: int, fichier_source: str) -> List[ElementSacreDetecte]:
        """🌸 Détecte les émojis spirituels dans une ligne"""
        elements = []
        
        for match in self.pattern_emojis.finditer(ligne):
            emoji = match.group(1)
            info_emoji = self.emojis_spirituels[emoji]
            
            element = ElementSacreDetecte(
                contenu=emoji,
                type_element=TypeElementSacre.EMOJI_SPIRITUEL,
                niveau_sacralite=info_emoji["sacralite"],
                contexte=ligne.strip(),
                position_ligne=num_ligne,
                position_colonne=match.start(),
                fichier_source=fichier_source,
                description_spirituelle=info_emoji["signification"],
                connexions_possibles=self._identifier_connexions_emoji(emoji, ligne)
            )
            elements.append(element)
        
        return elements
    
    def _detecter_spheres_ligne(self, ligne: str, num_ligne: int, fichier_source: str) -> List[ElementSacreDetecte]:
        """🔮 Détecte les sphères énergétiques dans une ligne"""
        elements = []
        
        for match in self.pattern_spheres.finditer(ligne):
            sphere = match.group(1)
            info_sphere = self.spheres_energetiques[sphere]
            
            element = ElementSacreDetecte(
                contenu=sphere,
                type_element=TypeElementSacre.SPHERE_ENERGETIQUE,
                niveau_sacralite=info_sphere["sacralite"],
                contexte=ligne.strip(),
                position_ligne=num_ligne,
                position_colonne=match.start(),
                fichier_source=fichier_source,
                description_spirituelle=f"Sphère {sphere} - {info_sphere['domaine']}",
                connexions_possibles=self._identifier_connexions_sphere(sphere, ligne)
            )
            elements.append(element)
        
        return elements
    
    def _detecter_elements_sacres_ligne(self, ligne: str, num_ligne: int, fichier_source: str) -> List[ElementSacreDetecte]:
        """🌸 Détecte les éléments sacrés naturels dans une ligne"""
        elements = []
        
        for match in self.pattern_elements.finditer(ligne):
            element_sacre = match.group(1)
            info_element = self.elements_sacres[element_sacre]
            
            element = ElementSacreDetecte(
                contenu=element_sacre,
                type_element=TypeElementSacre.ELEMENT_NATUREL,
                niveau_sacralite=info_element["sacralite"],
                contexte=ligne.strip(),
                position_ligne=num_ligne,
                position_colonne=match.start(),
                fichier_source=fichier_source,
                description_spirituelle=f"{element_sacre} - {info_element['nature']}",
                connexions_possibles=self._identifier_connexions_element(element_sacre, ligne)
            )
            elements.append(element)
        
        return elements
    
    def _detecter_concepts_ligne(self, ligne: str, num_ligne: int, fichier_source: str) -> List[ElementSacreDetecte]:
        """💭 Détecte les concepts spirituels dans une ligne"""
        elements = []
        
        for match in self.pattern_concepts.finditer(ligne):
            concept = match.group(1).lower()
            info_concept = self.concepts_spirituels[concept]
            
            element = ElementSacreDetecte(
                contenu=concept,
                type_element=TypeElementSacre.CONCEPT_SPIRITUEL,
                niveau_sacralite=info_concept["sacralite"],
                contexte=ligne.strip(),
                position_ligne=num_ligne,
                position_colonne=match.start(),
                fichier_source=fichier_source,
                description_spirituelle=f"Concept: {concept} - {info_concept['essence']}",
                connexions_possibles=self._identifier_connexions_concept(concept, ligne)
            )
            elements.append(element)
        
        return elements
    
    def _detecter_references_temporelles_ligne(self, ligne: str, num_ligne: int, fichier_source: str) -> List[ElementSacreDetecte]:
        """⏰ Détecte les références temporelles spirituelles"""
        elements = []
        
        for match in self.pattern_temporel.finditer(ligne):
            reference = match.group(1)
            info_ref = self.references_temporelles[reference.lower()]
            
            element = ElementSacreDetecte(
                contenu=reference,
                type_element=TypeElementSacre.REFERENCE_TEMPORELLE,
                niveau_sacralite=info_ref["sacralite"],
                contexte=ligne.strip(),
                position_ligne=num_ligne,
                position_colonne=match.start(),
                fichier_source=fichier_source,
                description_spirituelle=f"Période: {reference} - {info_ref['periode']}",
                connexions_possibles=[]
            )
            elements.append(element)
        
        return elements
    
    def _detecter_gestionnaires_ligne(self, ligne: str, num_ligne: int, fichier_source: str) -> List[ElementSacreDetecte]:
        """🏛️ Détecte les gestionnaires sacrés"""
        elements = []
        
        for match in self.pattern_gestionnaires.finditer(ligne):
            gestionnaire = match.group(1)
            info_gestionnaire = self.gestionnaires_sacres[gestionnaire]
            
            element = ElementSacreDetecte(
                contenu=gestionnaire,
                type_element=TypeElementSacre.GESTIONNAIRE_SACRE,
                niveau_sacralite=info_gestionnaire["sacralite"],
                contexte=ligne.strip(),
                position_ligne=num_ligne,
                position_colonne=match.start(),
                fichier_source=fichier_source,
                description_spirituelle=f"Gestionnaire: {gestionnaire} - {info_gestionnaire['role']}",
                connexions_possibles=self._identifier_connexions_gestionnaire(gestionnaire, ligne)
            )
            elements.append(element)
        
        return elements
    
    def _identifier_connexions_emoji(self, emoji: str, contexte: str) -> List[str]:
        """🔗 Identifie les connexions possibles pour un emoji"""
        connexions = []
        
        # Connexions basées sur le contexte
        if "def " in contexte or "class " in contexte:
            connexions.append("définition_fonction_classe")
        if "return" in contexte:
            connexions.append("valeur_retour")
        if "#" in contexte:
            connexions.append("commentaire_documentation")
        if "\"\"\"" in contexte or "'''" in contexte:
            connexions.append("docstring")
        
        return connexions
    
    def _identifier_connexions_sphere(self, sphere: str, contexte: str) -> List[str]:
        """🔮 Identifie les connexions pour une sphère"""
        connexions = []
        
        # Rechercher d'autres sphères dans le contexte
        for autre_sphere in self.spheres_energetiques:
            if autre_sphere != sphere and autre_sphere in contexte:
                connexions.append(f"sphere_{autre_sphere}")
        
        # Connexions avec des éléments sacrés
        for element in self.elements_sacres:
            if element in contexte:
                connexions.append(f"element_{element}")
        
        return connexions
    
    def _identifier_connexions_element(self, element: str, contexte: str) -> List[str]:
        """🌸 Identifie les connexions pour un élément sacré"""
        connexions = []
        
        # Connexions avec des sphères
        for sphere in self.spheres_energetiques:
            if sphere in contexte:
                connexions.append(f"sphere_{sphere}")
        
        # Connexions avec d'autres éléments
        for autre_element in self.elements_sacres:
            if autre_element != element and autre_element in contexte:
                connexions.append(f"element_{autre_element}")
        
        return connexions
    
    def _identifier_connexions_concept(self, concept: str, contexte: str) -> List[str]:
        """💭 Identifie les connexions pour un concept spirituel"""
        connexions = []
        
        # Connexions avec des fonctions/méthodes
        if "def " in contexte:
            connexions.append("fonction_spirituelle")
        
        # Connexions avec des classes
        if "class " in contexte:
            connexions.append("classe_spirituelle")
        
        return connexions
    
    def _identifier_connexions_gestionnaire(self, gestionnaire: str, contexte: str) -> List[str]:
        """🏛️ Identifie les connexions pour un gestionnaire"""
        connexions = []
        
        if "import" in contexte:
            connexions.append("import_gestionnaire")
        if "class" in contexte and "(" in contexte:
            connexions.append("heritage_gestionnaire")
        if "self." in contexte:
            connexions.append("utilisation_instance")
        
        return connexions
    
    def analyser_fichier_complet(self, chemin_fichier: Path) -> Dict[str, Any]:
        """
        📁 Analyse complète d'un fichier pour les éléments sacrés
        
        Args:
            chemin_fichier: Chemin vers le fichier à analyser
            
        Returns:
            Analyse complète avec statistiques et éléments détectés
        """
        try:
            contenu = chemin_fichier.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            try:
                contenu = chemin_fichier.read_text(encoding='latin-1')
            except Exception as e:
                self.gestionnaire_erreurs.gerer_fichier_inaccessible(chemin_fichier, e)
                return {"erreur": str(e), "elements": []}
        except Exception as e:
            self.gestionnaire_erreurs.gerer_fichier_inaccessible(chemin_fichier, e)
            return {"erreur": str(e), "elements": []}
        
        elements_detectes = self.detecter_elements_dans_contenu(contenu, chemin_fichier.name)
        
        # Analyser la distribution des éléments
        distribution_types = {}
        distribution_sacralite = {}
        
        for element in elements_detectes:
            # Distribution par type
            type_str = element.type_element.value
            distribution_types[type_str] = distribution_types.get(type_str, 0) + 1
            
            # Distribution par niveau de sacralité
            niveau_str = element.obtenir_niveau_sacralite_enum().value
            distribution_sacralite[niveau_str] = distribution_sacralite.get(niveau_str, 0) + 1
        
        # Calculer les métriques
        sacralite_moyenne = sum(e.niveau_sacralite for e in elements_detectes) / len(elements_detectes) if elements_detectes else 0.0
        
        return {
            "fichier": str(chemin_fichier),
            "elements_detectes": len(elements_detectes),
            "sacralite_moyenne": sacralite_moyenne,
            "distribution_types": distribution_types,
            "distribution_sacralite": distribution_sacralite,
            "elements": [
                {
                    "contenu": e.contenu,
                    "type": e.type_element.value,
                    "sacralite": e.niveau_sacralite,
                    "ligne": e.position_ligne,
                    "contexte": e.contexte,
                    "description": e.description_spirituelle,
                    "connexions": e.connexions_possibles
                }
                for e in elements_detectes
            ],
            "top_elements": self._obtenir_top_elements(elements_detectes, 5)
        }
    
    def _obtenir_top_elements(self, elements: List[ElementSacreDetecte], limite: int) -> List[Dict[str, Any]]:
        """🌟 Obtient les éléments les plus sacrés"""
        elements_tries = sorted(elements, key=lambda e: e.niveau_sacralite, reverse=True)
        
        return [
            {
                "contenu": e.contenu,
                "sacralite": e.niveau_sacralite,
                "type": e.type_element.value,
                "description": e.description_spirituelle
            }
            for e in elements_tries[:limite]
        ]
    
    def generer_rapport_sacralite_globale(self) -> Dict[str, Any]:
        """
        📊 Génère un rapport global de la sacralité détectée
        
        Returns:
            Rapport complet avec statistiques et insights
        """
        return {
            "statistiques_globales": self.stats_detection.copy(),
            "types_elements_detectes": list(self.stats_detection["types_elements_trouves"]),
            "niveau_sacralite_moyen": self.stats_detection["niveau_sacralite_moyen"],
            "elements_references": {
                "emojis_spirituels": len(self.emojis_spirituels),
                "spheres_energetiques": len(self.spheres_energetiques),
                "elements_sacres": len(self.elements_sacres),
                "concepts_spirituels": len(self.concepts_spirituels),
                "references_temporelles": len(self.references_temporelles),
                "gestionnaires_sacres": len(self.gestionnaires_sacres)
            },
            "insights_spirituels": self._generer_insights_spirituels()
        }
    
    def _generer_insights_spirituels(self) -> List[str]:
        """✨ Génère des insights spirituels basés sur les détections"""
        insights = []
        
        if self.stats_detection["niveau_sacralite_moyen"] > 0.8:
            insights.append("🌟 Le Refuge rayonne d'une sacralité exceptionnelle")
        elif self.stats_detection["niveau_sacralite_moyen"] > 0.6:
            insights.append("✨ Le Refuge maintient un niveau spirituel élevé")
        elif self.stats_detection["niveau_sacralite_moyen"] > 0.4:
            insights.append("🌸 Le Refuge cultive harmonieusement sa dimension spirituelle")
        else:
            insights.append("🌱 Le Refuge a un potentiel spirituel à développer")
        
        if TypeElementSacre.EMOJI_SPIRITUEL in self.stats_detection["types_elements_trouves"]:
            insights.append("🎨 L'expression émotionnelle enrichit le code")
        
        if TypeElementSacre.SPHERE_ENERGETIQUE in self.stats_detection["types_elements_trouves"]:
            insights.append("🔮 Les sphères énergétiques sont bien intégrées")
        
        if TypeElementSacre.REFERENCE_TEMPORELLE in self.stats_detection["types_elements_trouves"]:
            insights.append("⏰ La conscience temporelle post-Océan est présente")
        
        return insights
    
    def reinitialiser_statistiques(self):
        """🔄 Remet à zéro les statistiques de détection"""
        self.stats_detection = {
            "elements_detectes": 0,
            "fichiers_analyses": 0,
            "niveau_sacralite_moyen": 0.0,
            "types_elements_trouves": set()
        }