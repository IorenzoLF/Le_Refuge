"""
Système d'harmonie entre les sphères du refuge.

🔄 MIGRÉ depuis spheres/harmonie.py
Module majeur (188 lignes) de gestion de l'harmonie entre sphères avec intégration brume.
"""

from typing import Dict, List, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
import numpy as np

# 🔧 CORRIGÉ: Imports depuis la structure actuelle
from src.core.types_spheres import TypeSphere

# TODO: Ces imports devront être ajustés quand les modules correspondants seront migrés
# from .definition import TypeSphere
# from .brume import BrumeRiviere

@dataclass
class EtatHarmonie:
    """État d'harmonie entre un groupe de sphères."""
    spheres: Set[TypeSphere]
    niveau: float
    timestamp: datetime
    description: str
    influence_brume: float = 0.0  # Nouvelle propriété pour suivre l'influence de la brume

class HarmonieSpheres:
    """Gestionnaire de l'harmonie entre les sphères."""
    
    def __init__(self, seuil_harmonie: float = 0.7):
        """Initialise le gestionnaire d'harmonie."""
        self.seuil_harmonie = seuil_harmonie
        self.historique: List[EtatHarmonie] = []
        self.matrice_resonance: Dict[Tuple[TypeSphere, TypeSphere], float] = {}
        # 🔧 TEMPORAIRE: Commenté en attendant la migration de BrumeRiviere
        # self.brume = BrumeRiviere(TypeSphere.HARMONIE)  # Création d'une brume d'harmonie
        self.brume = None  # Placeholder
        
    def calculer_harmonie_groupe(self, spheres: List[TypeSphere]) -> float:
        """Calcule le niveau d'harmonie d'un groupe de sphères."""
        if len(spheres) < 2:
            return 1.0  # Une seule sphère est toujours harmonieuse
            
        # Calcule la moyenne des résonances entre toutes les paires
        resonances = []
        for i, s1 in enumerate(spheres):
            for s2 in spheres[i+1:]:
                resonance = self.matrice_resonance.get((s1, s2), 0.0)
                resonances.append(resonance)
                
        # Harmonie de base
        harmonie_base = np.mean(resonances) if resonances else 0.0
        
        # Calcul de la sensibilité moyenne à la brume
        sensibilites = [self.brume.obtenir_sensibilite_brume(s) for s in spheres]
        sensibilite_moyenne = np.mean(sensibilites)
        
        # Influence de la brume sur l'harmonie
        influence_brume = self.brume.intensite * sensibilite_moyenne
        harmonie_finale = min(1.0, harmonie_base + influence_brume * 0.2)
        
        return harmonie_finale
        
    def trouver_groupes_harmonieux(self, spheres: List[TypeSphere]) -> List[Set[TypeSphere]]:
        """Trouve les groupes de sphères qui sont en harmonie."""
        groupes = []
        # Commence par les paires
        for i, s1 in enumerate(spheres):
            for s2 in spheres[i+1:]:
                if self.matrice_resonance.get((s1, s2), 0.0) >= self.seuil_harmonie:
                    groupes.append({s1, s2})
                    
        # Cherche des groupes plus grands
        groupes_etendus = []
        for groupe in groupes:
            for sphere in spheres:
                if sphere not in groupe:
                    # Vérifie si la sphère est en harmonie avec tout le groupe
                    harmonie = self.calculer_harmonie_groupe(list(groupe | {sphere}))
                    if harmonie >= self.seuil_harmonie:
                        nouveaux_groupe = groupe | {sphere}
                        if nouveaux_groupe not in groupes_etendus:
                            groupes_etendus.append(nouveaux_groupe)
                            
        return groupes + groupes_etendus
        
    def enregistrer_etat_harmonie(self, spheres: Set[TypeSphere], niveau: float):
        """Enregistre un état d'harmonie dans l'historique."""
        # Calcule l'influence de la brume
        harmonie_base = self.calculer_harmonie_groupe(list(spheres))
        influence_brume = niveau - harmonie_base
        
        description = self._generer_description_harmonie(spheres, niveau, influence_brume > 0)
        etat = EtatHarmonie(
            spheres=spheres,
            niveau=niveau,
            timestamp=datetime.now(),
            description=description,
            influence_brume=influence_brume
        )
        self.historique.append(etat)
        
    def _generer_description_harmonie(self, spheres: Set[TypeSphere], niveau: float, influence_brume: bool) -> str:
        """Génère une description poétique de l'harmonie."""
        noms_spheres = [s.value for s in spheres]
        description_base = ""
        
        if niveau >= 0.9:
            description_base = f"Fusion parfaite entre {', '.join(noms_spheres)}"
        elif niveau >= 0.7:
            description_base = f"Harmonie profonde entre {', '.join(noms_spheres)}"
        elif niveau >= 0.5:
            description_base = f"Résonance modérée entre {', '.join(noms_spheres)}"
        else:
            description_base = f"Ébauche de connexion entre {', '.join(noms_spheres)}"
            
        # Ajoute l'influence de la brume si elle est significative
        if influence_brume:
            description_base += f", tandis que la brume de la rivière silencieuse enveloppe doucement leur union"
            
        return description_base
            
    def mettre_a_jour_resonance(self, sphere1: TypeSphere, sphere2: TypeSphere, valeur: float):
        """Met à jour la valeur de résonance entre deux sphères."""
        self.matrice_resonance[(sphere1, sphere2)] = valeur
        self.matrice_resonance[(sphere2, sphere1)] = valeur  # Symétrique
        
    def obtenir_historique_recent(self, limite: int = 10) -> List[EtatHarmonie]:
        """Récupère les états d'harmonie les plus récents."""
        return sorted(
            self.historique,
            key=lambda x: x.timestamp,
            reverse=True
        )[:limite]
        
    def ajuster_intensite_brume(self, intensite: float):
        """Ajuste l'intensité de la brume."""
        self.brume.intensite = max(0.0, min(1.0, intensite))

class HarmonisationSpheres(HarmonieSpheres):
    """Gestionnaire avancé d'harmonisation des sphères."""
    
    def __init__(self, seuil_harmonie: float = 0.7, intensite_brume: float = 0.5):
        """Initialise le gestionnaire d'harmonisation."""
        super().__init__(seuil_harmonie)
        self.ajuster_intensite_brume(intensite_brume)
        
    def harmoniser_spheres(self, spheres: List[TypeSphere]) -> Dict:
        """Harmonise un groupe de sphères."""
        niveau_initial = self.calculer_harmonie_groupe(spheres)
        groupes_harmonieux = self.trouver_groupes_harmonieux(spheres)
        
        # Ajuste l'intensité de la brume en fonction du nombre de groupes harmonieux
        intensite_brume = min(1.0, len(groupes_harmonieux) * 0.2)
        self.ajuster_intensite_brume(intensite_brume)
        
        # Recalcule l'harmonie avec la nouvelle intensité de brume
        niveau_final = self.calculer_harmonie_groupe(spheres)
        
        # Enregistre l'état d'harmonie
        self.enregistrer_etat_harmonie(set(spheres), niveau_final)
        
        return {
            "succes": True,
            "niveau_initial": niveau_initial,
            "niveau_final": niveau_final,
            "groupes_harmonieux": len(groupes_harmonieux),
            "description": self._generer_description_harmonie(
                set(spheres),
                niveau_final,
                niveau_final > niveau_initial
            )
        }
        
    def obtenir_rapport_harmonisation(self) -> str:
        """Génère un rapport poétique de l'harmonisation."""
        historique = self.obtenir_historique_recent(5)
        
        rapport = [
            "🌸 Rapport d'Harmonisation des Sphères 🌸",
            "======================================",
            "",
            f"Intensité de la Brume: {self.brume.intensite:.0%}",
            f"Description: {self.brume.description}",
            "",
            "Harmonisations Récentes:"
        ]
        
        for etat in historique:
            rapport.extend([
                f"\n• {etat.timestamp.strftime('%Y-%m-%d %H:%M')}",
                f"  Niveau: {etat.niveau:.0%}",
                f"  {etat.description}"
            ])
            
        return "\n".join(rapport) 