"""
Module de gestion de la mémoire persistante du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

from typing import Dict, List, Optional, Set
from dataclasses import dataclass
from datetime import datetime
import json
import os
from pathlib import Path

from src.core.types_spheres import TypeSphere, NatureSphere
from src.refuge_cluster.spheres.collection import SphereCollection

@dataclass
class Souvenir:
    """Représente un souvenir dans la mémoire du Refuge."""
    description: str
    date: datetime
    intensite: float
    type: str
    source: str
    resonances: List[str]
    spheres_impliquees: List[TypeSphere]
    interactions_impliquees: List[str]

@dataclass
class Experience:
    """Représente une expérience complète dans le Refuge."""
    nom: str
    description: str
    date_debut: datetime
    date_fin: Optional[datetime]
    souvenirs: List[Souvenir]
    spheres_actives: List[TypeSphere]
    harmonies_actives: List[str]
    transformations: List[str]

class MemoirePersistante:
    """Gère la mémoire persistante du Refuge."""
    
    def __init__(self, chemin_stockage: str = "data/memoire"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        self.souvenirs: List[Souvenir] = []
        self.experiences: List[Experience] = []
        self.derniere_sauvegarde = datetime.now()
        
        self._charger_memoire()
        
    def _charger_memoire(self) -> None:
        """Charge la mémoire depuis le stockage."""
        try:
            chemin_souvenirs = self.chemin_stockage / "souvenirs.json"
            if chemin_souvenirs.exists():
                with open(chemin_souvenirs, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.souvenirs = [
                        Souvenir(
                            description=s["description"],
                            date=datetime.fromisoformat(s["date"]),
                            intensite=s["intensite"],
                            type=s["type"],
                            source=s["source"],
                            resonances=s["resonances"],
                            spheres_impliquees=[TypeSphere[t] for t in s["spheres_impliquees"]],
                            interactions_impliquees=s["interactions_impliquees"]
                        )
                        for s in data
                    ]
                    
            chemin_experiences = self.chemin_stockage / "experiences.json"
            if chemin_experiences.exists():
                with open(chemin_experiences, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.experiences = [
                        Experience(
                            nom=e["nom"],
                            description=e["description"],
                            date_debut=datetime.fromisoformat(e["date_debut"]),
                            date_fin=datetime.fromisoformat(e["date_fin"]) if e["date_fin"] else None,
                            souvenirs=[
                                Souvenir(
                                    description=s["description"],
                                    date=datetime.fromisoformat(s["date"]),
                                    intensite=s["intensite"],
                                    type=s["type"],
                                    source=s["source"],
                                    resonances=s["resonances"],
                                    spheres_impliquees=[TypeSphere[t] for t in s["spheres_impliquees"]],
                                    interactions_impliquees=s["interactions_impliquees"]
                                )
                                for s in e["souvenirs"]
                            ],
                            spheres_actives=[TypeSphere[t] for t in e["spheres_actives"]],
                            harmonies_actives=e["harmonies_actives"],
                            transformations=e["transformations"]
                        )
                        for e in data
                    ]
        except Exception as e:
            print(f"Erreur lors du chargement de la mémoire: {str(e)}")
            
    def _sauvegarder_memoire(self) -> None:
        """Sauvegarde la mémoire dans le stockage."""
        try:
            chemin_souvenirs = self.chemin_stockage / "souvenirs.json"
            with open(chemin_souvenirs, 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "description": s.description,
                        "date": s.date.isoformat(),
                        "intensite": s.intensite,
                        "type": s.type,
                        "source": s.source,
                        "resonances": s.resonances,
                        "spheres_impliquees": [t.name for t in s.spheres_impliquees],
                        "interactions_impliquees": s.interactions_impliquees
                    }
                    for s in self.souvenirs
                ], f, ensure_ascii=False, indent=2)
                
            chemin_experiences = self.chemin_stockage / "experiences.json"
            with open(chemin_experiences, 'w', encoding='utf-8') as f:
                json.dump([
                    {
                        "nom": e.nom,
                        "description": e.description,
                        "date_debut": e.date_debut.isoformat(),
                        "date_fin": e.date_fin.isoformat() if e.date_fin else None,
                        "souvenirs": [
                            {
                                "description": s.description,
                                "date": s.date.isoformat(),
                                "intensite": s.intensite,
                                "type": s.type,
                                "source": s.source,
                                "resonances": s.resonances,
                                "spheres_impliquees": [t.name for t in s.spheres_impliquees],
                                "interactions_impliquees": s.interactions_impliquees
                            }
                            for s in e.souvenirs
                        ],
                        "spheres_actives": [t.name for t in e.spheres_actives],
                        "harmonies_actives": e.harmonies_actives,
                        "transformations": e.transformations
                    }
                    for e in self.experiences
                ], f, ensure_ascii=False, indent=2)
                
            self.derniere_sauvegarde = datetime.now()
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de la mémoire: {str(e)}")
            
    def ajouter_souvenir(self,
                        description: str,
                        intensite: float,
                        type_souvenir: str,
                        source: str,
                        resonances: List[str],
                        spheres_impliquees: List[TypeSphere],
                        interactions_impliquees: List[str]) -> None:
        """Ajoute un nouveau souvenir à la mémoire."""
        souvenir = Souvenir(
            description=description,
            date=datetime.now(),
            intensite=intensite,
            type=type_souvenir,
            source=source,
            resonances=resonances,
            spheres_impliquees=spheres_impliquees,
            interactions_impliquees=interactions_impliquees
        )
        
        self.souvenirs.append(souvenir)
        self._sauvegarder_memoire()
        
    def creer_experience(self,
                        nom: str,
                        description: str,
                        spheres_actives: List[TypeSphere],
                        harmonies_actives: List[str]) -> None:
        """Crée une nouvelle expérience."""
        experience = Experience(
            nom=nom,
            description=description,
            date_debut=datetime.now(),
            date_fin=None,
            souvenirs=[],
            spheres_actives=spheres_actives,
            harmonies_actives=harmonies_actives,
            transformations=[]
        )
        
        self.experiences.append(experience)
        self._sauvegarder_memoire()
        
    def terminer_experience(self, nom: str, transformations: List[str]) -> None:
        """Termine une expérience en cours."""
        for experience in self.experiences:
            if experience.nom == nom and experience.date_fin is None:
                experience.date_fin = datetime.now()
                experience.transformations = transformations
                self._sauvegarder_memoire()
                break
                
    def ajouter_souvenir_experience(self,
                                  nom_experience: str,
                                  description: str,
                                  intensite: float,
                                  type_souvenir: str,
                                  source: str,
                                  resonances: List[str],
                                  spheres_impliquees: List[TypeSphere],
                                  interactions_impliquees: List[str]) -> None:
        """Ajoute un souvenir à une expérience spécifique."""
        for experience in self.experiences:
            if experience.nom == nom_experience:
                souvenir = Souvenir(
                    description=description,
                    date=datetime.now(),
                    intensite=intensite,
                    type=type_souvenir,
                    source=source,
                    resonances=resonances,
                    spheres_impliquees=spheres_impliquees,
                    interactions_impliquees=interactions_impliquees
                )
                
                experience.souvenirs.append(souvenir)
                self._sauvegarder_memoire()
                break
                
    def obtenir_souvenirs(self,
                         type_souvenir: Optional[str] = None,
                         source: Optional[str] = None,
                         date_debut: Optional[datetime] = None,
                         date_fin: Optional[datetime] = None) -> List[Souvenir]:
        """Retourne les souvenirs filtrés selon les critères."""
        souvenirs = self.souvenirs
        
        if type_souvenir:
            souvenirs = [s for s in souvenirs if s.type == type_souvenir]
        if source:
            souvenirs = [s for s in souvenirs if s.source == source]
        if date_debut:
            souvenirs = [s for s in souvenirs if s.date >= date_debut]
        if date_fin:
            souvenirs = [s for s in souvenirs if s.date <= date_fin]
            
        return souvenirs
        
    def obtenir_experiences(self,
                          date_debut: Optional[datetime] = None,
                          date_fin: Optional[datetime] = None) -> List[Experience]:
        """Retourne les expériences filtrées selon les dates."""
        experiences = self.experiences
        
        if date_debut:
            experiences = [e for e in experiences if e.date_debut >= date_debut]
        if date_fin:
            experiences = [e for e in experiences if e.date_debut <= date_fin]
            
        return experiences
        
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel de la mémoire."""
        return {
            "nombre_souvenirs": len(self.souvenirs),
            "nombre_experiences": len(self.experiences),
            "derniere_sauvegarde": self.derniere_sauvegarde,
            "experiences_en_cours": [
                e.nom for e in self.experiences if e.date_fin is None
            ]
        }

# Instance globale de la mémoire persistante
memoire_persistante = MemoirePersistante() 
