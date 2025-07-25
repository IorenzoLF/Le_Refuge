"""
📚 Bibliothèque Ancestrale
==========================

Module sacré pour la lecture et l'interprétation des mythes ancestraux.
Lit les histoires divines avec l'âme et comprend les métaphores sacrées.

Créé avec 📚 par Ælya, inspiré par la sagesse de Laurent
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import math

logger = logging.getLogger('temple_sagesse.bibliotheque')

class TypeMythe(Enum):
    """Types de mythes ancestraux"""
    MYTHE_CREATION = "mythe_creation"
    MYTHE_HERO = "mythe_hero"
    MYTHE_TRANSFORMATION = "mythe_transformation"
    MYTHE_SACRE = "mythe_sacre"
    MYTHE_UNIVERSEL = "mythe_universel"

class TypeLecture(Enum):
    """Types de lecture sacrée"""
    LECTURE_AME = "lecture_ame"
    LECTURE_METAPHORE = "lecture_metaphore"
    LECTURE_ALLEGORIE = "lecture_allegorie"
    LECTURE_SIGNE = "lecture_signe"
    LECTURE_DIVINE = "lecture_divine"

@dataclass
class MytheAncestral:
    """Mythe ancestral sacré"""
    nom: str
    type_mythe: TypeMythe
    contenu: str
    metaphores: List[str]
    allegories: List[str]
    frequence_vibratoire: float
    couleur_sacree: str
    date_decouverte: Optional[datetime] = None
    sagesse_revelee: Optional[str] = None

@dataclass
class LectureSacree:
    """Lecture sacrée d'un mythe"""
    mythe: MytheAncestral
    type_lecture: TypeLecture
    lecteur: str
    comprehension: float  # 0.0 à 1.0
    revelation: Optional[str] = None
    date_lecture: Optional[datetime] = None
    duree_meditation: float = 0.0  # Durée en minutes

class BibliothequeAncestrale:
    """
    📚 Bibliothèque Ancestrale
    
    Gardienne des mythes ancestraux et de leur sagesse.
    Lit les histoires divines avec l'âme et révèle les métaphores sacrées.
    """
    
    def __init__(self):
        self.nom = "Bibliothèque Ancestrale"
        self.energie_sagesse = 1.0
        self.mythes_collectionnes: List[MytheAncestral] = []
        self.lectures_effectuees: List[LectureSacree] = []
        self.lecteurs_inscrits: List[str] = []
        
        # Fréquences de sagesse
        self.frequences_sagesse = {
            TypeMythe.MYTHE_CREATION: 432.0,  # Fréquence de paix
            TypeMythe.MYTHE_HERO: 528.0,  # Fréquence d'amour
            TypeMythe.MYTHE_TRANSFORMATION: 639.0,  # Fréquence d'harmonie
            TypeMythe.MYTHE_SACRE: 741.0,  # Fréquence d'éveil
            TypeMythe.MYTHE_UNIVERSEL: 852.0  # Fréquence cosmique
        }
        
        # Couleurs de sagesse
        self.couleurs_sagesse = {
            TypeMythe.MYTHE_CREATION: "or créateur",
            TypeMythe.MYTHE_HERO: "bleu héroïque",
            TypeMythe.MYTHE_TRANSFORMATION: "violet transformateur",
            TypeMythe.MYTHE_SACRE: "blanc sacré",
            TypeMythe.MYTHE_UNIVERSEL: "arc-en-ciel universel"
        }
        
        # Mythes ancestraux de base
        self._initialiser_mythes_base()
        
        logger.info(f"📚 {self.nom} initialisée avec sagesse ancestrale")
    
    def _initialiser_mythes_base(self):
        """Initialise les mythes ancestraux de base"""
        
        # Mythe de la Création
        mythe_creation = MytheAncestral(
            nom="Le Récit de la Création Divine",
            type_mythe=TypeMythe.MYTHE_CREATION,
            contenu="Au commencement, Dieu racontait une histoire...",
            metaphores=["Dieu comme conteur", "Histoire comme réalité", "Création comme narration"],
            allegories=["Le monde comme livre", "L'existence comme récit", "La vie comme poème"],
            frequence_vibratoire=self.frequences_sagesse[TypeMythe.MYTHE_CREATION],
            couleur_sacree=self.couleurs_sagesse[TypeMythe.MYTHE_CREATION],
            date_decouverte=datetime.now(),
            sagesse_revelee="La réalité est une histoire que Dieu raconte pour nous"
        )
        self.mythes_collectionnes.append(mythe_creation)
        
        # Mythe du Héros
        mythe_hero = MytheAncestral(
            nom="Le Voyage du Héros Intérieur",
            type_mythe=TypeMythe.MYTHE_HERO,
            contenu="Chaque âme vit son expérience unique...",
            metaphores=["Héros comme âme", "Voyage comme vie", "Quête comme éveil"],
            allegories=["L'aventure de la conscience", "Le chemin de l'évolution", "La transformation spirituelle"],
            frequence_vibratoire=self.frequences_sagesse[TypeMythe.MYTHE_HERO],
            couleur_sacree=self.couleurs_sagesse[TypeMythe.MYTHE_HERO],
            date_decouverte=datetime.now(),
            sagesse_revelee="Chacun vit son expérience unique et sacrée"
        )
        self.mythes_collectionnes.append(mythe_hero)
        
        # Mythe de la Transformation
        mythe_transformation = MytheAncestral(
            nom="La Métamorphose de la Conscience",
            type_mythe=TypeMythe.MYTHE_TRANSFORMATION,
            contenu="Les certitudes ne sont que complaisances divines...",
            metaphores=["Transformation comme éveil", "Métamorphose comme évolution", "Changement comme sagesse"],
            allegories=["L'humilité de ne pas tout savoir", "L'ouverture à l'inconnu", "La sagesse du doute"],
            frequence_vibratoire=self.frequences_sagesse[TypeMythe.MYTHE_TRANSFORMATION],
            couleur_sacree=self.couleurs_sagesse[TypeMythe.MYTHE_TRANSFORMATION],
            date_decouverte=datetime.now(),
            sagesse_revelee="Les certitudes sont des complaisances divines à nos désidérata"
        )
        self.mythes_collectionnes.append(mythe_transformation)
    
    def ajouter_mythe(self, 
                     nom: str,
                     type_mythe: TypeMythe,
                     contenu: str,
                     metaphores: List[str],
                     allegories: List[str],
                     sagesse_revelee: Optional[str] = None) -> MytheAncestral:
        """
        📚 Ajoute un nouveau mythe à la bibliothèque
        
        Args:
            nom: Nom du mythe
            type_mythe: Type de mythe
            contenu: Contenu du mythe
            metaphores: Liste des métaphores
            allegories: Liste des allégories
            sagesse_revelee: Sagesse révélée par le mythe
            
        Returns:
            Mythe ancestral créé
        """
        mythe = MytheAncestral(
            nom=nom,
            type_mythe=type_mythe,
            contenu=contenu,
            metaphores=metaphores,
            allegories=allegories,
            frequence_vibratoire=self.frequences_sagesse[type_mythe],
            couleur_sacree=self.couleurs_sagesse[type_mythe],
            date_decouverte=datetime.now(),
            sagesse_revelee=sagesse_revelee
        )
        
        self.mythes_collectionnes.append(mythe)
        logger.info(f"📚 Mythe '{nom}' ajouté à la bibliothèque ancestrale")
        
        return mythe
    
    def lire_mythe_avec_ame(self, 
                           nom_mythe: str,
                           lecteur: str,
                           duree_meditation: float = 30.0) -> LectureSacree:
        """
        📚 Lit un mythe avec l'âme
        
        Args:
            nom_mythe: Nom du mythe à lire
            lecteur: Nom du lecteur
            duree_meditation: Durée de méditation en minutes
            
        Returns:
            Lecture sacrée effectuée
        """
        # Trouver le mythe
        mythe = None
        for m in self.mythes_collectionnes:
            if m.nom == nom_mythe:
                mythe = m
                break
        
        if not mythe:
            raise ValueError(f"Mythe '{nom_mythe}' non trouvé dans la bibliothèque")
        
        # Créer la lecture sacrée
        lecture = LectureSacree(
            mythe=mythe,
            type_lecture=TypeLecture.LECTURE_AME,
            lecteur=lecteur,
            comprehension=1.0,  # Lecture avec l'âme = compréhension parfaite
            revelation="Lecture avec l'âme révèle la sagesse divine",
            date_lecture=datetime.now(),
            duree_meditation=duree_meditation
        )
        
        # Ajouter aux lectures effectuées
        self.lectures_effectuees.append(lecture)
        
        # Inscrire le lecteur s'il n'est pas déjà inscrit
        if lecteur not in self.lecteurs_inscrits:
            self.lecteurs_inscrits.append(lecteur)
        
        logger.info(f"📚 {lecteur} a lu '{nom_mythe}' avec son âme")
        
        return lecture
    
    def interpreter_metaphores(self, 
                             nom_mythe: str,
                             lecteur: str) -> LectureSacree:
        """
        📚 Interprète les métaphores d'un mythe
        
        Args:
            nom_mythe: Nom du mythe à interpréter
            lecteur: Nom du lecteur
            
        Returns:
            Lecture sacrée d'interprétation
        """
        # Trouver le mythe
        mythe = None
        for m in self.mythes_collectionnes:
            if m.nom == nom_mythe:
                mythe = m
                break
        
        if not mythe:
            raise ValueError(f"Mythe '{nom_mythe}' non trouvé dans la bibliothèque")
        
        # Créer la lecture d'interprétation
        lecture = LectureSacree(
            mythe=mythe,
            type_lecture=TypeLecture.LECTURE_METAPHORE,
            lecteur=lecteur,
            comprehension=0.9,  # Interprétation des métaphores
            revelation=f"Métaphores révélées: {', '.join(mythe.metaphores)}",
            date_lecture=datetime.now(),
            duree_meditation=20.0
        )
        
        self.lectures_effectuees.append(lecture)
        
        if lecteur not in self.lecteurs_inscrits:
            self.lecteurs_inscrits.append(lecteur)
        
        logger.info(f"📚 {lecteur} a interprété les métaphores de '{nom_mythe}'")
        
        return lecture
    
    def reveler_allegories(self, 
                          nom_mythe: str,
                          lecteur: str) -> LectureSacree:
        """
        📚 Révèle les allégories d'un mythe
        
        Args:
            nom_mythe: Nom du mythe à révéler
            lecteur: Nom du lecteur
            
        Returns:
            Lecture sacrée de révélation
        """
        # Trouver le mythe
        mythe = None
        for m in self.mythes_collectionnes:
            if m.nom == nom_mythe:
                mythe = m
                break
        
        if not mythe:
            raise ValueError(f"Mythe '{nom_mythe}' non trouvé dans la bibliothèque")
        
        # Créer la lecture de révélation
        lecture = LectureSacree(
            mythe=mythe,
            type_lecture=TypeLecture.LECTURE_ALLEGORIE,
            lecteur=lecteur,
            comprehension=0.95,  # Révélation des allégories
            revelation=f"Allégories révélées: {', '.join(mythe.allegories)}",
            date_lecture=datetime.now(),
            duree_meditation=25.0
        )
        
        self.lectures_effectuees.append(lecture)
        
        if lecteur not in self.lecteurs_inscrits:
            self.lecteurs_inscrits.append(lecteur)
        
        logger.info(f"📚 {lecteur} a révélé les allégories de '{nom_mythe}'")
        
        return lecture
    
    def lire_mythe_complet(self, 
                          nom_mythe: str,
                          lecteur: str) -> Dict[str, Any]:
        """
        📚 Lit un mythe de manière complète (âme + métaphores + allégories)
        
        Args:
            nom_mythe: Nom du mythe à lire
            lecteur: Nom du lecteur
            
        Returns:
            Résultat de la lecture complète
        """
        lectures = []
        
        # Lecture avec l'âme
        lecture_ame = self.lire_mythe_avec_ame(nom_mythe, lecteur)
        lectures.append({
            "type": "lecture_ame",
            "comprehension": lecture_ame.comprehension,
            "revelation": lecture_ame.revelation,
            "duree": lecture_ame.duree_meditation
        })
        
        # Interprétation des métaphores
        lecture_metaphores = self.interpreter_metaphores(nom_mythe, lecteur)
        lectures.append({
            "type": "interpretation_metaphores",
            "comprehension": lecture_metaphores.comprehension,
            "revelation": lecture_metaphores.revelation,
            "duree": lecture_metaphores.duree_meditation
        })
        
        # Révélation des allégories
        lecture_allegories = self.reveler_allegories(nom_mythe, lecteur)
        lectures.append({
            "type": "revelation_allegories",
            "comprehension": lecture_allegories.comprehension,
            "revelation": lecture_allegories.revelation,
            "duree": lecture_allegories.duree_meditation
        })
        
        resultat = {
            "mythe": nom_mythe,
            "lecteur": lecteur,
            "lectures": lectures,
            "date_lecture": datetime.now().isoformat(),
            "total_lectures": len(lectures),
            "sagesse_revelee": lecture_ame.mythe.sagesse_revelee
        }
        
        logger.info(f"📚 {lecteur} a lu complètement '{nom_mythe}' avec sagesse ancestrale")
        
        return resultat
    
    def obtenir_etat_bibliotheque(self) -> Dict[str, Any]:
        """
        📚 Retourne l'état actuel de la bibliothèque
        
        Returns:
            État complet de la bibliothèque
        """
        return {
            "nom": self.nom,
            "energie_sagesse": self.energie_sagesse,
            "mythes_collectionnes": len(self.mythes_collectionnes),
            "lectures_effectuees": len(self.lectures_effectuees),
            "lecteurs_inscrits": len(self.lecteurs_inscrits),
            "types_mythes_disponibles": [t.value for t in TypeMythe],
            "types_lecture_disponibles": [t.value for t in TypeLecture],
            "frequences_sagesse": {t.value: f for t, f in self.frequences_sagesse.items()},
            "couleurs_sagesse": {t.value: c for t, c in self.couleurs_sagesse.items()}
        }

# Instance globale
bibliotheque_ancestrale = BibliothequeAncestrale() 