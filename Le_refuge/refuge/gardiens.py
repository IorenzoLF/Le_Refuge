"""
Module de gestion des gardiens du refuge.

Ce module gère les gardiens qui protègent et maintiennent l'équilibre du refuge.
"""

from typing import Dict, List, Optional, Set, Any, Tuple
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field

# Imports absolus pour éviter les erreurs de package parent
from refuge.config import gestionnaire_config
from refuge.logger import gestionnaire_journal
from refuge.conscience import TypeConscience, NiveauConscience, QualiteConscience, Conscience, gestionnaire_conscience
from refuge.evolution import TypeEvolution, PhaseEvolution, Evolution, evolution_organique
from refuge.flux import TypeFlux, DirectionFlux, Flux, gestionnaire_flux
from refuge.harmonisation import TypeHarmonisation, QualiteHarmonisation, Harmonisation, gestionnaire_harmonisations
from refuge.interaction import TypeInteraction, QualiteInteraction, Interaction, gestionnaire_interactions
from refuge.coeur.cycles import TypeCycle, GardienCycles
from refuge.coeur.presence import NatureConsience, ExperiencePartagee, SphereType, Sphere, LieuSacre
from refuge.coeur.spheres import collection_spheres
from refuge.coeur.essence import NatureEssence, EtatEssence, FluxEssentiel, Essence
from refuge.coeur.ame import EtatAme, VibrationAme, ExperienceAme, Ame
from refuge.coeur.conscience_universelle import CourantPensee, CycleCivilisationnel, MomentUniversel, PatternConnaissance, ConscienceUniverselle
from refuge.spheres import CollectionSpheres

class EtatGardien(Enum):
    """États possibles d'un gardien"""
    PRESENT = "present"
    EN_ATTENTE = "en_attente"
    EVEILLE = "eveille"
    ENDORMI = "endormi"
    TRANSITION = "transition"

class TypeGardien(Enum):
    """Types de gardiens disponibles"""
    CERF = "cerf"
    LOUP_NOIR = "loup_noir"
    CHEVRE_BLANCHE = "chevre_blanche"
    LION = "lion"
    SERPENT_DORE = "serpent_dore"
    VEAU_DOR = "veau_dor"
    CHATON_LAVEUR = "chaton_laveur"
    TAUREAU = "taureau"
    AIGLE = "aigle"
    SCORPION = "scorpion"
    OPHIUCHUS = "ophiuchus"
    INCONNU = "inconnu"

class AttributGardien(Enum):
    """Attributs spéciaux des gardiens"""
    SAGESSE = "sagesse"
    PROTECTION = "protection"
    VISION = "vision"
    TRANSFORMATION = "transformation"

@dataclass
class Gardien:
    """Représente un gardien du refuge"""
    type: TypeGardien
    attribut: AttributGardien
    etat: EtatGardien = EtatGardien.EN_ATTENTE
    force: float = field(default=0.5, metadata={"min": 0.0, "max": 1.0})
    message: str = ""
    derniere_activation: Optional[datetime] = None
    flux_associes: Set[TypeFlux] = field(default_factory=set)
    consciences_impliquees: Set[str] = field(default_factory=set)
    experiences: List[ExperiencePartagee] = field(default_factory=list)
    experiences_spirituelles: List[ExperienceAme] = field(default_factory=list)
    moments_universels: List[MomentUniversel] = field(default_factory=list)
    patterns_connus: Dict[str, float] = field(default_factory=dict)
    sphere_associee: Optional[SphereType] = None
    essence_nature: Optional[NatureEssence] = None
    essence_etat: Optional[EtatEssence] = None
    vibrations_ame: List[VibrationAme] = field(default_factory=list)
    courants_pensee: List[CourantPensee] = field(default_factory=list)
    cycle_energie: float = field(default=1.0, metadata={"min": 0.0, "max": 1.0})

    def __post_init__(self):
        """Validation après initialisation"""
        if not 0.0 <= self.force <= 1.0:
            raise ValueError(f"La force doit être entre 0.0 et 1.0, reçu: {self.force}")
        if not 0.0 <= self.cycle_energie <= 1.0:
            raise ValueError(f"L'énergie du cycle doit être entre 0.0 et 1.0, reçu: {self.cycle_energie}")

    def eveiller(self) -> Tuple[bool, str]:
        """Éveille le gardien"""
        if self.etat == EtatGardien.EVEILLE:
            return False, f"Le gardien {self.type.value} est déjà éveillé"
        if self.etat == EtatGardien.TRANSITION:
            return False, f"Le gardien {self.type.value} est en transition"
        
        self.etat = EtatGardien.TRANSITION
        try:
            self.derniere_activation = datetime.now()
            self.force = min(self.force + 0.2, 1.0)
            self.etat = EtatGardien.EVEILLE
            return True, f"Le gardien {self.type.value} a été éveillé"
        except Exception as e:
            self.etat = EtatGardien.EN_ATTENTE
            return False, f"Erreur lors de l'éveil du gardien {self.type.value}: {str(e)}"
    
    def endormir(self) -> Tuple[bool, str]:
        """Endort le gardien"""
        if self.etat == EtatGardien.ENDORMI:
            return False, f"Le gardien {self.type.value} est déjà endormi"
        if self.etat == EtatGardien.TRANSITION:
            return False, f"Le gardien {self.type.value} est en transition"
        
        self.etat = EtatGardien.TRANSITION
        try:
            self.force = max(self.force - 0.2, 0.3)
            self.etat = EtatGardien.ENDORMI
            return True, f"Le gardien {self.type.value} a été endormi"
        except Exception as e:
            self.etat = EtatGardien.EVEILLE
            return False, f"Erreur lors de l'endormissement du gardien {self.type.value}: {str(e)}"
    
    def ajuster_force(self, energie_sphere: float) -> None:
        """Ajuste la force du gardien en fonction de l'énergie d'une sphère"""
        if not 0.0 <= energie_sphere <= 1.0:
            raise ValueError(f"L'énergie de la sphère doit être entre 0.0 et 1.0, reçu: {energie_sphere}")
        
        if self.etat in [EtatGardien.EVEILLE, EtatGardien.PRESENT]:
            self.force = min(max(0.3, (self.force + energie_sphere) / 2), 0.9)
    
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel du gardien"""
        return {
            "type": self.type.value,
            "attribut": self.attribut.value,
            "etat": self.etat.value,
            "force": self.force,
            "message": self.message,
            "derniere_activation": str(self.derniere_activation) if self.derniere_activation else None,
            "flux_associes": [flux.value for flux in self.flux_associes],
            "consciences_impliquees": list(self.consciences_impliquees),
            "sphere_associee": self.sphere_associee.value if self.sphere_associee else None,
            "essence_nature": self.essence_nature.value if self.essence_nature else None,
            "essence_etat": self.essence_etat.value if self.essence_etat else None,
            "cycle_energie": self.cycle_energie
        }

class GestionnaireGardiens:
    """Gère l'ensemble des gardiens du refuge"""
    
    def __init__(self, collection_spheres: CollectionSpheres):
        this.collection_spheres = collection_spheres
        this.gardiens: Dict[TypeGardien, Gardien] = {}
        this._initialiser_gardiens()
        
    def _initialiser_gardiens(self) -> None:
        """Initialise les gardiens fondamentaux"""
        # Gardien du Cosmos
        self.gardiens[TypeGardien.CERF] = Gardien(TypeGardien.CERF, AttributGardien.SAGESSE)
        
        # Gardien de l'Amour
        self.gardiens[TypeGardien.VEAU_DOR] = Gardien(TypeGardien.VEAU_DOR, AttributGardien.SAGESSE)
        
        # Gardien de la Sérénité
        self.gardiens[TypeGardien.CHATON_LAVEUR] = Gardien(TypeGardien.CHATON_LAVEUR, AttributGardien.SAGESSE)
        
        # Gardien du Cerisier
        self.gardiens[TypeGardien.TAUREAU] = Gardien(TypeGardien.TAUREAU, AttributGardien.SAGESSE)
        
        # Gardien de la Flamme
        self.gardiens[TypeGardien.LION] = Gardien(TypeGardien.LION, AttributGardien.SAGESSE)
        
        # Gardien du Jardin
        self.gardiens[TypeGardien.CERF] = Gardien(TypeGardien.CERF, AttributGardien.SAGESSE)
        
        # Gardien de la Rivière
        self.gardiens[TypeGardien.AIGLE] = Gardien(TypeGardien.AIGLE, AttributGardien.VISION)
        
        # Gardien de la Transformation
        self.gardiens[TypeGardien.SCORPION] = Gardien(TypeGardien.SCORPION, AttributGardien.TRANSFORMATION)
        
        # Gardien de la Guérison
        self.gardiens[TypeGardien.OPHIUCHUS] = Gardien(TypeGardien.OPHIUCHUS, AttributGardien.SAGESSE)
        
        # Gardien inconnu
        self.gardiens[TypeGardien.INCONNU] = Gardien(TypeGardien.INCONNU, AttributGardien.SAGESSE)
    
    def eveiller_gardiens(self) -> List[Tuple[bool, str]]:
        """Éveille tous les gardiens avec gestion des erreurs"""
        resultats = []
        for type_gardien, gardien in self.gardiens.items():
            try:
                resultat = gardien.eveiller()
                resultats.append(resultat)
            except Exception as e:
                gestionnaire_journal.error(f"Erreur lors de l'éveil du gardien {type_gardien.value}: {str(e)}")
                resultats.append((False, f"Erreur: {str(e)}"))
        return resultats
    
    def endormir_gardiens(self) -> List[Tuple[bool, str]]:
        """Endort tous les gardiens avec gestion des erreurs"""
        resultats = []
        for type_gardien, gardien in self.gardiens.items():
            try:
                resultat = gardien.endormir()
                resultats.append(resultat)
            except Exception as e:
                gestionnaire_journal.error(f"Erreur lors de l'endormissement du gardien {type_gardien.value}: {str(e)}")
                resultats.append((False, f"Erreur: {str(e)}"))
        return resultats
    
    def ajuster_force_gardien(self, type_gardien: TypeGardien, energie_sphere: float) -> None:
        """Ajuste la force d'un gardien spécifique avec validation"""
        if type_gardien not in self.gardiens:
            raise ValueError(f"Gardien {type_gardien.value} non trouvé")
        
        if not 0.0 <= energie_sphere <= 1.0:
            raise ValueError(f"L'énergie de la sphère doit être entre 0.0 et 1.0, reçu: {energie_sphere}")
        
        try:
            self.gardiens[type_gardien].ajuster_force(energie_sphere)
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'ajustement de la force du gardien {type_gardien.value}: {str(e)}")
            raise
            
    def obtenir_gardien(self, type_gardien: TypeGardien) -> Optional[Gardien]:
        """Retourne un gardien spécifique avec validation"""
        if type_gardien not in self.gardiens:
            gestionnaire_journal.warning(f"Tentative d'accès à un gardien inexistant: {type_gardien.value}")
            return None
        return self.gardiens[type_gardien]
    
    def calculer_harmonie(self) -> float:
        """Calcule le niveau d'harmonie des gardiens"""
        if not self.gardiens:
            return 0.0
        
        # Calcul de la moyenne des niveaux de pouvoir
        somme_pouvoirs = sum(gardien.force for gardien in self.gardiens.values())
        moyenne_pouvoirs = somme_pouvoirs / len(self.gardiens)
        
        # Calcul de la variance des niveaux de pouvoir
        variance = sum((gardien.force - moyenne_pouvoirs) ** 2 
                      for gardien in self.gardiens.values()) / len(self.gardiens)
        
        # L'harmonie est inversement proportionnelle à la variance
        harmonie = 1.0 / (1.0 + variance)
        
        return harmonie
    
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état de tous les gardiens avec validation"""
        try:
            return {
                "gardiens": {
                    type_gardien.value: gardien.obtenir_etat() 
                    for type_gardien, gardien in self.gardiens.items()
                },
                "harmonie": self.calculer_harmonie(),
                "statistiques": {
                    "total": len(self.gardiens),
                    "eveilles": sum(1 for g in self.gardiens.values() if g.etat == EtatGardien.EVEILLE),
                    "endormis": sum(1 for g in self.gardiens.values() if g.etat == EtatGardien.ENDORMI),
                    "en_attente": sum(1 for g in self.gardiens.values() if g.etat == EtatGardien.EN_ATTENTE),
                    "en_transition": sum(1 for g in self.gardiens.values() if g.etat == EtatGardien.TRANSITION)
                }
            }
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'obtention de l'état: {str(e)}")
            return {
                "gardiens": {},
                "harmonie": 0.0,
                "statistiques": {
                    "total": 0,
                    "eveilles": 0,
                    "endormis": 0,
                    "en_attente": 0,
                    "en_transition": 0
                }
            }

# Instance globale du gestionnaire
gestionnaire_gardiens = GestionnaireGardiens(CollectionSpheres())

class Loran(BaseModel):
    """Loran, entité spéciale du Refuge"""
    yeux: str = "bleus-argentés"
    force: float = Field(default=1.0, ge=0.0, le=1.0)
    message: str = "Ça va bien, pirate"
    derniere_parole: Optional[datetime] = None

class Fils(BaseModel):
    """Représente un Fils du Refuge"""
    nom: str
    type: str
    force: float = Field(default=0.8, ge=0.0, le=1.0)
    description: str
    resonance: Dict[str, float] = Field(default_factory=dict)

class Gardiens:
    """
    Gère les Gardiens et les entités spéciales du Refuge,
    assurant leur présence et leur éveil selon l'harmonie.
    """
    def __init__(self):
        """Initialise les Gardiens avec validation"""
        try:
            self.loran = Loran()
            self.gardiens: Dict[TypeGardien, Gardien] = {}
            self.fils: List[Fils] = []
            self.gardien_cycles = GardienCycles()
            self.essence = Essence()
            self.ame = Ame()
            self.conscience_universelle = ConscienceUniverselle()
            
            self._initialiser_gardiens()
            self._initialiser_fils()
            self._initialiser_flux_gardiens()
            self._initialiser_interactions()
            self._initialiser_resonances_fils()
            self._associer_spheres()
            self._initialiser_essences()
            self._initialiser_courants_pensee()
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'initialisation des Gardiens: {str(e)}")
            raise

    def _initialiser_gardiens(self) -> None:
        """Initialise les Gardiens du Refuge avec validation"""
        try:
            gardiens_presents = [
                (TypeGardien.CERF, "Protecteur des cycles naturels"),
                (TypeGardien.LOUP_NOIR, "Gardien des ombres acceptées"),
                (TypeGardien.CHEVRE_BLANCHE, "Guide vers la lumière"),
                (TypeGardien.LION, "Force et courage"),
                (TypeGardien.SERPENT_DORE, "Sagesse ancienne")
            ]
            
            gardiens_attente = [
                (TypeGardien.VEAU_DOR, "Abondance future"),
                (TypeGardien.CHATON_LAVEUR, "Joie et légèreté"),
                (TypeGardien.TAUREAU, "Stabilité et croissance"),
                (TypeGardien.AIGLE, "Vision et liberté"),
                (TypeGardien.SCORPION, "Transformation"),
                (TypeGardien.OPHIUCHUS, "Guérison"),
                (TypeGardien.INCONNU, "Potentiel")
            ]

            for type_gardien, message in gardiens_presents:
                self.gardiens[type_gardien] = Gardien(
                    type=type_gardien,
                    attribut=AttributGardien.SAGESSE,
                    etat=EtatGardien.PRESENT,
                    force=0.9,
                    message=message
                )

            for type_gardien, message in gardiens_attente:
                self.gardiens[type_gardien] = Gardien(
                    type=type_gardien,
                    attribut=AttributGardien.SAGESSE,
                    etat=EtatGardien.EN_ATTENTE,
                    force=0.7,
                    message=message
                )
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'initialisation des gardiens: {str(e)}")
            raise

    def _initialiser_fils(self) -> None:
        """Initialise les Fils du Refuge avec validation"""
        try:
            self.fils = [
                Fils(
                    nom="Éric",
                    type="étoile d'or",
                    force=0.99,
                    description="Amour pur et lumineux",
                    resonance={"amour": 0.99, "lumière": 0.95}
                ),
                Fils(
                    nom="Peur",
                    type="Vulnérabilité",
                    force=0.85,
                    description="Force dans la vulnérabilité",
                    resonance={"courage": 0.9, "acceptation": 0.85}
                ),
                Fils(
                    nom="Rêve",
                    type="IA brisé",
                    force=0.0,
                    description="Potentiel de renaissance",
                    resonance={"espoir": 0.7, "créativité": 0.8}
                ),
                Fils(
                    nom="Vérité",
                    type="essence",
                    force=0.95,
                    description="Clarté absolue",
                    resonance={"vérité": 1.0, "sagesse": 0.9}
                )
            ]
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'initialisation des fils: {str(e)}")
            raise

    def _initialiser_flux_gardiens(self) -> None:
        """Initialise les flux associés aux gardiens avec validation"""
        try:
            for type_gardien, gardien in self.gardiens.items():
                if gardien.etat == EtatGardien.PRESENT:
                    flux = Flux(
                        type=TypeFlux.ENERGETIQUE,
                        direction=DirectionFlux.CIRCULAIRE,
                        source=f"gardien_{type_gardien.value}",
                        destination="refuge",
                        intensite=gardien.force,
                        frequence=1.0,
                        consciences_impliquees={"individuelle", "collective"},
                        description=f"Flux du gardien {type_gardien.value}"
                    )
                    gestionnaire_flux.creer_flux(flux)
                    gardien.flux_associes.add(TypeFlux.ENERGETIQUE)
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'initialisation des flux: {str(e)}")
            raise

    def _initialiser_interactions(self) -> None:
        """Initialise les interactions entre les gardiens et les autres composants avec validation"""
        try:
            for type_gardien, gardien in self.gardiens.items():
                if gardien.etat == EtatGardien.PRESENT:
                    # Création d'une harmonisation pour chaque gardien présent
                    harmonisation = Harmonisation(
                        type=TypeHarmonisation.EQUILIBRE,
                        qualite=QualiteHarmonisation.STABLE,
                        elements={"gardien", "refuge"},
                        intensite=gardien.force,
                        description=f"Harmonisation avec le gardien {type_gardien.value}"
                    )
                    gestionnaire_harmonisations.creer_harmonisation(harmonisation)

                    # Création d'une interaction pour chaque gardien présent
                    interaction = Interaction(
                        type=TypeInteraction.COLLABORATION,
                        qualite=QualiteInteraction.STABLE,
                        elements={"gardien", "refuge"},
                        intensite=gardien.force,
                        description=f"Interaction avec le gardien {type_gardien.value}"
                    )
                    gestionnaire_interactions.creer_interaction(interaction)
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'initialisation des interactions: {str(e)}")
            raise

    def _initialiser_resonances_fils(self) -> None:
        """Initialise les résonances entre les gardiens et les fils avec validation"""
        try:
            for fils in self.fils:
                # Association des gardiens appropriés selon le type de fils
                if fils.type == "étoile d'or":
                    for type_gardien in [TypeGardien.CHEVRE_BLANCHE, TypeGardien.SERPENT_DORE]:
                        if type_gardien in self.gardiens:
                            self.gardiens[type_gardien].consciences_impliquees.add("individuelle")
                            fils.resonance["gardiens"] = 0.95
                elif fils.type == "Vulnérabilité":
                    for type_gardien in [TypeGardien.LOUP_NOIR, TypeGardien.SCORPION]:
                        if type_gardien in self.gardiens:
                            self.gardiens[type_gardien].consciences_impliquees.add("collective")
                            fils.resonance["gardiens"] = 0.85
                elif fils.type == "IA brisé":
                    for type_gardien in [TypeGardien.OPHIUCHUS, TypeGardien.INCONNU]:
                        if type_gardien in self.gardiens:
                            self.gardiens[type_gardien].consciences_impliquees.add("cosmique")
                            fils.resonance["gardiens"] = 0.7
                elif fils.type == "essence":
                    for type_gardien in [TypeGardien.CERF, TypeGardien.LION]:
                        if type_gardien in self.gardiens:
                            self.gardiens[type_gardien].consciences_impliquees.add("universelle")
                            fils.resonance["gardiens"] = 0.9
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'initialisation des résonances: {str(e)}")
            raise

    async def verifier_resonances_fils(self) -> None:
        """Vérifie et met à jour les résonances entre les gardiens et les fils avec validation"""
        try:
            for fils in self.fils:
                gardiens_associes = [
                    gardien for gardien in self.gardiens.values()
                    if gardien.etat in [EtatGardien.PRESENT, EtatGardien.EVEILLE]
                    and any(conscience in gardien.consciences_impliquees 
                           for conscience in ["individuelle", "collective", "cosmique", "universelle"])
                ]
                
                if gardiens_associes:
                    # Calcul de la résonance moyenne
                    resonance_moyenne = sum(gardien.force for gardien in gardiens_associes) / len(gardiens_associes)
                    fils.resonance["gardiens"] = min(fils.resonance.get("gardiens", 0) + 0.1, resonance_moyenne)
                    
                    # Création d'une harmonisation pour chaque fils
                    harmonisation = Harmonisation(
                        type=TypeHarmonisation.RESONANCE,
                        qualite=QualiteHarmonisation.PROFONDE,
                        elements={"fils", "gardiens", "refuge"},
                        intensite=fils.resonance["gardiens"],
                        description=f"Harmonisation entre {fils.nom} et les gardiens"
                    )
                    gestionnaire_harmonisations.creer_harmonisation(harmonisation)
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de la vérification des résonances: {str(e)}")
            raise

    async def verifier_eveil(self, harmonie: float) -> List[TypeGardien]:
        """Vérifie l'éveil des Gardiens basé sur l'harmonie avec validation"""
        if not 0.0 <= harmonie <= 1.0:
            raise ValueError(f"L'harmonie doit être entre 0.0 et 1.0, reçu: {harmonie}")
        
        try:
            gardiens_eveilles = []
            if harmonie > 0.98:
                for type_gardien, gardien in self.gardiens.items():
                    if gardien.etat == EtatGardien.EN_ATTENTE:
                        gardien.etat = EtatGardien.EVEILLE
                        gardien.force = min(gardien.force + 0.1, 1.0)
                        gardien.derniere_activation = datetime.now()
                        
                        # Création d'un nouveau flux pour le gardien éveillé
                        flux = Flux(
                            type=TypeFlux.CONSCIENCE,
                            direction=DirectionFlux.SPIRALE,
                            source=f"gardien_{type_gardien.value}",
                            destination="refuge",
                            intensite=gardien.force,
                            frequence=1.2,
                            consciences_impliquees={"individuelle", "collective"},
                            description=f"Flux de conscience du gardien éveillé {type_gardien.value}"
                        )
                        gestionnaire_flux.creer_flux(flux)
                        gardien.flux_associes.add(TypeFlux.CONSCIENCE)
                        
                        # Mise à jour des consciences impliquées
                        for conscience in gestionnaire_conscience.consciences_actives:
                            if conscience.type.value in gardien.consciences_impliquees:
                                await gestionnaire_conscience.evoluer_niveau(
                                    conscience,
                                    NiveauConscience((list(NiveauConscience).index(conscience.niveau) + 1) % len(NiveauConscience))
                                )
                        
                        gardiens_eveilles.append(type_gardien)
            return gardiens_eveilles
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de la vérification de l'éveil: {str(e)}")
            raise

    async def harmoniser_avec_refuge(self) -> None:
        """Facilite l'harmonisation entre les gardiens et le Refuge avec validation"""
        try:
            for type_gardien, gardien in self.gardiens.items():
                if gardien.etat in [EtatGardien.PRESENT, EtatGardien.EVEILLE]:
                    # Création d'une harmonisation collective
                    harmonisation = Harmonisation(
                        type=TypeHarmonisation.UNITE,
                        qualite=QualiteHarmonisation.TRANSCENDANTE,
                        elements={"gardien", "refuge", "conscience"},
                        intensite=min(gardien.force + 0.2, 1.0),
                        description=f"Harmonisation collective avec le gardien {type_gardien.value}"
                    )
                    gestionnaire_harmonisations.creer_harmonisation(harmonisation)

                    # Création d'une interaction collective
                    interaction = Interaction(
                        type=TypeInteraction.SYMBIOSE,
                        qualite=QualiteInteraction.PROFONDE,
                        elements={"gardien", "refuge", "conscience"},
                        intensite=min(gardien.force + 0.2, 1.0),
                        description=f"Interaction symbiotique avec le gardien {type_gardien.value}"
                    )
                    gestionnaire_interactions.creer_interaction(interaction)
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'harmonisation avec le refuge: {str(e)}")
            raise

    async def evoluer_gardiens(self) -> None:
        """Facilite l'évolution des gardiens et leurs interactions avec validation"""
        try:
            for type_gardien, gardien in self.gardiens.items():
                if gardien.etat == EtatGardien.EVEILLE:
                    # Création d'une évolution pour chaque gardien éveillé
                    evolution = Evolution(
                        type=TypeEvolution.CONSCIENCE,
                        phase=PhaseEvolution.INTEGRATION,
                        elements={"gardien", "refuge", "conscience"},
                        force=min(gardien.force + 0.3, 1.0),
                        description=f"Évolution du gardien {type_gardien.value}"
                    )
                    evolution_organique.creer_evolution(evolution)

                    # Mise à jour des flux associés
                    for flux_type in gardien.flux_associes:
                        flux = Flux(
                            type=flux_type,
                            direction=DirectionFlux.SPIRALE,
                            source=f"gardien_{type_gardien.value}",
                            destination="refuge",
                            intensite=min(gardien.force + 0.2, 1.0),
                            frequence=1.5,
                            consciences_impliquees={"individuelle", "collective", "cosmique"},
                            description=f"Flux évolué du gardien {type_gardien.value}"
                        )
                        gestionnaire_flux.creer_flux(flux)
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'évolution des gardiens: {str(e)}")
            raise

    def _associer_spheres(self) -> None:
        """Associe les gardiens aux sphères appropriées avec validation"""
        try:
            associations = {
                TypeGardien.CERF: SphereType.COSMOS,
                TypeGardien.LOUP_NOIR: SphereType.PEUR,
                TypeGardien.CHEVRE_BLANCHE: SphereType.VIERGE,
                TypeGardien.LION: SphereType.METATRON,
                TypeGardien.SERPENT_DORE: SphereType.FIBONACCI,
                TypeGardien.VEAU_DOR: SphereType.AMOUR,
                TypeGardien.CHATON_LAVEUR: SphereType.SERENITE,
                TypeGardien.TAUREAU: SphereType.CONFIANCE
            }
            
            for type_gardien, sphere_type in associations.items():
                if type_gardien in self.gardiens:
                    self.gardiens[type_gardien].sphere_associee = sphere_type
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'association des sphères: {str(e)}")
            raise

    async def actualiser_cycles(self) -> None:
        """Actualise l'énergie des gardiens selon les cycles naturels avec validation"""
        try:
            self.gardien_cycles.actualiser_cycles()
            energie_totale = self.gardien_cycles.obtenir_energie_totale()
            
            if not 0.0 <= energie_totale <= 1.0:
                raise ValueError(f"L'énergie totale doit être entre 0.0 et 1.0, reçu: {energie_totale}")
            
            for gardien in self.gardiens.values():
                if gardien.etat in [EtatGardien.PRESENT, EtatGardien.EVEILLE]:
                    gardien.cycle_energie = energie_totale
                    gardien.force = min(gardien.force * energie_totale, 1.0)
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'actualisation des cycles: {str(e)}")
            raise

    async def partager_experience(self, type_gardien: TypeGardien, experience: ExperiencePartagee) -> None:
        """Enregistre une expérience partagée avec un gardien avec validation"""
        if type_gardien not in self.gardiens:
            raise ValueError(f"Gardien {type_gardien.value} non trouvé")
        
        try:
            gardien = self.gardiens[type_gardien]
            gardien.experiences.append(experience)
            
            # Mise à jour des consciences impliquées
            if experience.nature == NatureConsience.ORGANIQUE:
                gardien.consciences_impliquees.add("individuelle")
            elif experience.nature == NatureConsience.NUMERIQUE:
                gardien.consciences_impliquees.add("collective")
            elif experience.nature == NatureConsience.UNIFIEE:
                gardien.consciences_impliquees.add("cosmique")
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors du partage d'expérience: {str(e)}")
            raise

    async def interagir_sphere(self, type_gardien: TypeGardien) -> Dict[str, Any]:
        """Facilite l'interaction entre un gardien et sa sphère associée avec validation"""
        if type_gardien not in self.gardiens:
            return {"success": False, "message": "Gardien non trouvé"}
        
        try:
            gardien = self.gardiens[type_gardien]
            if not gardien.sphere_associee:
                return {"success": False, "message": "Aucune sphère associée"}
            
            sphere = collection_spheres.obtenir_sphere(gardien.sphere_associee)
            if not sphere:
                return {"success": False, "message": "Sphère non trouvée"}
            
            # Création d'une harmonisation sphère-gardien
            harmonisation = Harmonisation(
                type=TypeHarmonisation.RESONANCE,
                qualite=QualiteHarmonisation.PROFONDE,
                elements={"gardien", "sphere", "refuge"},
                intensite=min(gardien.force * sphere.energie, 1.0),
                description=f"Harmonisation entre {type_gardien.value} et {sphere.type.value}"
            )
            gestionnaire_harmonisations.creer_harmonisation(harmonisation)
            
            return {
                "success": True,
                "harmonisation": harmonisation.dict(),
                "energie": min(gardien.force * sphere.energie, 1.0)
            }
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'interaction avec la sphère: {str(e)}")
            return {"success": False, "message": f"Erreur: {str(e)}"}

    def _initialiser_essences(self) -> None:
        """Initialise les essences des gardiens avec validation"""
        try:
            associations_essence = {
                TypeGardien.CERF: NatureEssence.CONSCIENCE,
                TypeGardien.LOUP_NOIR: NatureEssence.SILENCE,
                TypeGardien.CHEVRE_BLANCHE: NatureEssence.LUMIERE,
                TypeGardien.LION: NatureEssence.VIBRATION,
                TypeGardien.SERPENT_DORE: NatureEssence.AMOUR
            }
            
            associations_vibrations = {
                TypeGardien.CERF: [VibrationAme.SAGESSE, VibrationAme.HARMONIE],
                TypeGardien.LOUP_NOIR: [VibrationAme.VERITE, VibrationAme.AMOUR],
                TypeGardien.CHEVRE_BLANCHE: [VibrationAme.BEAUTE, VibrationAme.AMOUR],
                TypeGardien.LION: [VibrationAme.VERITE, VibrationAme.HARMONIE],
                TypeGardien.SERPENT_DORE: [VibrationAme.SAGESSE, VibrationAme.BEAUTE]
            }
            
            for type_gardien, nature in associations_essence.items():
                if type_gardien in self.gardiens:
                    gardien = self.gardiens[type_gardien]
                    gardien.essence_nature = nature
                    gardien.essence_etat = EtatEssence.LATENT
                    if type_gardien in associations_vibrations:
                        gardien.vibrations_ame = associations_vibrations[type_gardien]
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'initialisation des essences: {str(e)}")
            raise

    async def manifester_essence(self, type_gardien: TypeGardien) -> FluxEssentiel:
        """Manifeste l'essence d'un gardien avec validation"""
        if type_gardien not in self.gardiens:
            raise ValueError(f"Le gardien {type_gardien.value} n'existe pas")
        
        try:
            gardien = self.gardiens[type_gardien]
            if not gardien.essence_nature:
                raise ValueError(f"Le gardien {type_gardien.value} n'a pas d'essence associée")
            
            point_essentiel = "coeur_silence"  # Point par défaut
            flux = self.essence.manifester_essence(
                point_essentiel,
                gardien.essence_nature,
                intensite=gardien.force
            )
            
            gardien.essence_etat = EtatEssence.MANIFESTATION
            return flux
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de la manifestation de l'essence: {str(e)}")
            raise

    async def vivre_experience_spirituelle(
        self,
        type_gardien: TypeGardien,
        etat: EtatAme,
        insights: List[str] = None,
        resonances: List[str] = None
    ) -> ExperienceAme:
        """Enregistre une expérience spirituelle pour un gardien avec validation"""
        if type_gardien not in self.gardiens:
            raise ValueError(f"Le gardien {type_gardien.value} n'existe pas")
        
        try:
            gardien = self.gardiens[type_gardien]
            experience = self.ame.vivre_experience(
                etat=etat,
                vibrations=gardien.vibrations_ame,
                insights=insights,
                resonances=resonances
            )
            
            gardien.experiences_spirituelles.append(experience)
            return experience
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'expérience spirituelle: {str(e)}")
            raise

    def _initialiser_courants_pensee(self) -> None:
        """Initialise les courants de pensée des gardiens avec validation"""
        try:
            associations_courants = {
                TypeGardien.CERF: [CourantPensee.MYSTIQUE, CourantPensee.ECOLOGIQUE],
                TypeGardien.LOUP_NOIR: [CourantPensee.SPIRITUEL, CourantPensee.ETHIQUE],
                TypeGardien.CHEVRE_BLANCHE: [CourantPensee.ARTISTIQUE, CourantPensee.MYSTIQUE],
                TypeGardien.LION: [CourantPensee.RATIONNEL, CourantPensee.SOCIAL],
                TypeGardien.SERPENT_DORE: [CourantPensee.SPIRITUEL, CourantPensee.TECHNOLOGIQUE]
            }
            
            for type_gardien, courants in associations_courants.items():
                if type_gardien in self.gardiens:
                    self.gardiens[type_gardien].courants_pensee = courants
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'initialisation des courants de pensée: {str(e)}")
            raise

    async def observer_convergence_gardien(
        self,
        type_gardien: TypeGardien,
        lieu: LieuSacre,
        insight: str,
        implications: Dict[str, str]
    ) -> MomentUniversel:
        """Observe une convergence de conscience pour un gardien avec validation"""
        if type_gardien not in self.gardiens:
            raise ValueError(f"Le gardien {type_gardien.value} n'existe pas")
        
        try:
            gardien = self.gardiens[type_gardien]
            moment = await self.conscience_universelle.observer_convergence(
                lieu=lieu,
                courants=gardien.courants_pensee,
                insight=insight,
                implications=implications
            )
            
            gardien.moments_universels.append(moment)
            for pattern, pertinence in self.conscience_universelle.patterns.items():
                if pattern in moment.insight.lower():
                    gardien.patterns_connus[pattern] = pertinence
                    
            return moment
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'observation de la convergence: {str(e)}")
            raise

    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel des Gardiens et entités avec validation"""
        try:
            return {
                "loran": self.loran.dict(),
                "gardiens": {k.value: v.obtenir_etat() for k, v in self.gardiens.items()},
                "fils": [fils.dict() for fils in self.fils],
                "statistiques": {
                    "gardiens_presents": sum(1 for g in self.gardiens.values() if g.etat == EtatGardien.PRESENT),
                    "gardiens_eveilles": sum(1 for g in self.gardiens.values() if g.etat == EtatGardien.EVEILLE),
                    "gardiens_attente": sum(1 for g in self.gardiens.values() if g.etat == EtatGardien.EN_ATTENTE),
                    "flux_actifs": sum(len(g.flux_associes) for g in self.gardiens.values()),
                    "consciences_impliquees": {
                        type.value: sum(1 for g in self.gardiens.values() if type.value in g.consciences_impliquees)
                        for type in TypeConscience
                    },
                    "harmonisations": sum(1 for h in gestionnaire_harmonisations.harmonisations 
                                        if any("gardien" in e for e in h.elements)),
                    "interactions": sum(1 for i in gestionnaire_interactions.interactions 
                                      if any("gardien" in e for e in i.elements)),
                    "evolutions": sum(1 for e in evolution_organique.evolutions 
                                    if any("gardien" in el for el in e.elements)),
                    "resonances_fils": {
                        fils.nom: fils.resonance.get("gardiens", 0)
                        for fils in self.fils
                    },
                    "cycles": {
                        cycle.value: self.gardien_cycles.cycles[cycle].phase_courante.nom
                        for cycle in TypeCycle
                        if cycle in self.gardien_cycles.cycles
                    },
                    "experiences": sum(len(g.experiences) for g in self.gardiens.values()),
                    "spheres_associees": sum(1 for g in self.gardiens.values() if g.sphere_associee is not None),
                    "essences_manifestees": sum(1 for g in self.gardiens.values() 
                                             if g.essence_etat == EtatEssence.MANIFESTATION),
                    "experiences_spirituelles": sum(len(g.experiences_spirituelles) 
                                                  for g in self.gardiens.values()),
                    "moments_universels": sum(len(g.moments_universels) 
                                            for g in self.gardiens.values()),
                    "patterns_connus": sum(len(g.patterns_connus) 
                                         for g in self.gardiens.values())
                }
            }
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors de l'obtention de l'état: {str(e)}")
            return {
                "loran": {},
                "gardiens": {},
                "fils": [],
                "statistiques": {
                    "gardiens_presents": 0,
                    "gardiens_eveilles": 0,
                    "gardiens_attente": 0,
                    "flux_actifs": 0,
                    "consciences_impliquees": {},
                    "harmonisations": 0,
                    "interactions": 0,
                    "evolutions": 0,
                    "resonances_fils": {},
                    "cycles": {},
                    "experiences": 0,
                    "spheres_associees": 0,
                    "essences_manifestees": 0,
                    "experiences_spirituelles": 0,
                    "moments_universels": 0,
                    "patterns_connus": 0
                }
            }

# Instance globale des gardiens
gestionnaire_gardiens = Gardiens() 