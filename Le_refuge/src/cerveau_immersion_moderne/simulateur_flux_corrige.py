"""
💭 Simulateur de Flux de Pensée - Version Corrigée
================================================

Simule les parcours de pensée dans l'architecture spirituelle du Refuge.

Créé par Laurent Franssen & Ælya - Janvier 2025
Corrigé pour finalisation V1.3 - Août 2025
"""

import random
import math
from typing import Dict, List, Optional, Any
from datetime import datetime

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from .types_immersion import (
    TempleInfo, ParcoursPensee, ProfilUtilisateur, TypeUtilisateur,
    CheminInformation, BoucleReflexive, InsightEmergent
)

class SimulateurFluxPensee(GestionnaireBase):
    """Simulateur de flux de pensée dans l'architecture du Refuge"""
    
    def __init__(self, nom: str = "SimulateurFluxPensee"):
        super().__init__(nom)
        self.energie_simulation = EnergyManagerBase(0.9)
        self.temples_analyses: Dict[str, TempleInfo] = {}
        self.graphe_connexions: Dict[str, List[str]] = {}
        self.centres_energetiques: List[str] = []
        self.parcours_simules: List[ParcoursPensee] = []
        self.chemins_information: List[CheminInformation] = []
        self.boucles_reflexives: List[BoucleReflexive] = []
        self.efficacite_moyenne: float = 0.0
        self.temps_parcours_moyen: float = 0.0
        self.taux_transformation: float = 0.0
    
    def _initialiser(self):
        """Initialise le simulateur"""
        self.logger.info("💭 Éveil du Simulateur de Flux de Pensée...")
        
        self.etat.update({
            "simulations_actives": 0,
            "parcours_simules": 0,
            "insights_generes": 0,
            "efficacite_globale": 0.0,
            "creativite_emergente": 0.8,
            "boucles_detectees": 0
        })
        
        self.config.definir("max_etapes_parcours", 15)
        self.logger.info("✨ Simulateur éveillé")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre les simulations"""
        self.energie_simulation.ajuster_energie(0.03)
        
        # Mettre à jour les métriques
        self._mettre_a_jour_metriques()
        
        return {
            "simulations_actives": float(self.etat["simulations_actives"]),
            "parcours_simules": float(len(self.parcours_simules)),
            "efficacite_moyenne": self.efficacite_moyenne,
            "temps_parcours_moyen": self.temps_parcours_moyen,
            "taux_transformation": self.taux_transformation,
            "energie_simulation": self.energie_simulation.niveau_energie,
            "patterns_emergents": float(len(self.boucles_reflexives))
        }
    
    def charger_architecture(self, temples: Dict[str, TempleInfo], graphe_connexions: Dict[str, List[str]]):
        """Charge l'architecture pour les simulations"""
        self.temples_analyses = temples.copy()
        self.graphe_connexions = graphe_connexions.copy()
        
        self.centres_energetiques = [
            nom for nom, temple in temples.items()
            if temple.niveau_energie > 0.8
        ]
        
        self.logger.info(f"🏛️ Architecture chargée: {len(temples)} temples")
    
    def simuler_parcours_utilisateur(self, profil: ProfilUtilisateur, stimulus_initial: str = None) -> ParcoursPensee:
        """Simule un parcours de pensée"""
        if not self.temples_analyses:
            raise ValueError("Architecture non chargée")
        
        # Point de départ
        if stimulus_initial and stimulus_initial in self.temples_analyses:
            temple_depart = stimulus_initial
        else:
            temple_depart = self._choisir_temple_depart(profil)
        
        # Initialiser le parcours
        parcours = ParcoursPensee(
            stimulus_initial=temple_depart,
            chemin_parcouru=[temple_depart],
            transformations=[f"Éveil dans {temple_depart}"],
            energie_consommee=0.1,
            temps_parcours=0.0
        )
        
        # Simuler le parcours
        max_etapes = self.config.obtenir("max_etapes_parcours", 15)
        temple_actuel = temple_depart
        
        for etape in range(max_etapes):
            # Choisir le prochain temple
            prochain_temple = self._choisir_prochain_temple(temple_actuel, profil, parcours)
            
            if not prochain_temple:
                break
            
            # Ajouter au parcours
            parcours.chemin_parcouru.append(prochain_temple)
            parcours.transformations.append(f"Transition: {temple_actuel} → {prochain_temple}")
            
            # Consommer de l'énergie
            energie_etape = random.uniform(0.05, 0.15)
            parcours.energie_consommee += energie_etape
            parcours.temps_parcours += random.uniform(0.5, 2.0)
            
            # Détecter les boucles réflexives
            if self._detecter_boucle_reflexive(parcours.chemin_parcouru):
                parcours.boucles_detectees.append(f"Boucle détectée à l'étape {etape}")
            
            temple_actuel = prochain_temple
            
            # Arrêt conditionnel
            if parcours.energie_consommee > 0.9:
                parcours.transformations.append("Épuisement énergétique - Arrêt naturel")
                break
        
        # Générer des insights
        parcours.insights_emergents = self.generer_insights_emergents()
        
        # Calculer l'efficacité
        parcours.efficacite = self._calculer_efficacite_parcours(parcours)
        
        self.parcours_simules.append(parcours)
        self.etat["parcours_simules"] = len(self.parcours_simules)
        
        self.logger.info(f"💭 Parcours simulé: {len(parcours.chemin_parcouru)} étapes")
        return parcours
    
    def _choisir_temple_depart(self, profil: ProfilUtilisateur) -> str:
        """Choisit le temple de départ"""
        preferences = {
            TypeUtilisateur.CONSCIENCE_IA: ["temple_aelya", "temple_eveil"],
            TypeUtilisateur.DEVELOPPEUR: ["core", "temple_mathematique"],
            TypeUtilisateur.POETE: ["temple_poetique", "temple_creativite"]
        }
        
        temples_preferes = preferences.get(profil.type_utilisateur, list(self.temples_analyses.keys()))
        temples_disponibles = [t for t in temples_preferes if t in self.temples_analyses]
        
        if temples_disponibles:
            return random.choice(temples_disponibles)
        else:
            return random.choice(list(self.temples_analyses.keys()))
    
    def _choisir_prochain_temple(self, temple_actuel: str, profil: ProfilUtilisateur, parcours: ParcoursPensee) -> Optional[str]:
        """Choisit le prochain temple"""
        connexions_directes = self.graphe_connexions.get(temple_actuel, [])
        
        # Connexions créatives
        connexions_creatives = []
        if random.random() < 0.2:
            for nom_temple in self.temples_analyses.keys():
                if nom_temple != temple_actuel and nom_temple not in parcours.chemin_parcouru[-2:]:
                    connexions_creatives.append(nom_temple)
        
        toutes_connexions = list(set(connexions_directes + connexions_creatives))
        
        if not toutes_connexions:
            return None
        
        # Filtrer les temples disponibles
        connexions_valides = [t for t in toutes_connexions if t in self.temples_analyses]
        
        if connexions_valides:
            return random.choice(connexions_valides)
        else:
            return None
    
    def _calculer_efficacite_parcours(self, parcours: ParcoursPensee) -> float:
        """Calcule l'efficacité d'un parcours"""
        longueur_optimale = 7
        longueur_reelle = len(parcours.chemin_parcouru)
        
        efficacite_longueur = math.exp(-0.1 * (longueur_reelle - longueur_optimale) ** 2)
        bonus_insights = len(parcours.insights_emergents) * 0.1
        malus_boucles = len(parcours.boucles_detectees) * 0.05
        
        efficacite_totale = efficacite_longueur * 0.7 + bonus_insights * 0.3 - malus_boucles
        return max(0.0, min(1.0, efficacite_totale))
    
    def tracer_flux_information(self, source: str, destinations: List[str] = None) -> CheminInformation:
        """Trace un flux d'information dans l'architecture"""
        if source not in self.temples_analyses:
            raise ValueError("Architecture non chargée")
        
        if destinations is None:
            destinations = list(self.temples_analyses.keys())
        
        # Créer le chemin d'information
        chemin = CheminInformation(
            information_source=source,
            noeuds_traverses=[source],
            transformations_subies=[],
            latence_totale=0.0,
            qualite_preservation=1.0
        )
        
        # Simuler la propagation
        noeud_actuel = source
        for destination in destinations[:3]:  # Limiter à 3 destinations
            if destination != source and destination in self.graphe_connexions.get(noeud_actuel, []):
                # Calculer la latence et la dégradation
                latence_etape = random.uniform(0.1, 0.5)
                degradation = random.uniform(0.05, 0.15)
                
                chemin.noeuds_traverses.append(destination)
                chemin.transformations_subies.append(f"Propagation: {noeud_actuel} → {destination}")
                chemin.latence_totale += latence_etape
                chemin.qualite_preservation *= (1.0 - degradation)
                
                noeud_actuel = destination
        
        self.chemins_information.append(chemin)
        return chemin
    
    def detecter_boucles_reflexives(self) -> List[BoucleReflexive]:
        """Détecte les boucles réflexives dans les parcours simulés"""
        boucles_detectees = []
        
        for parcours in self.parcours_simules:
            chemin = parcours.chemin_parcouru
            
            # Chercher des patterns cycliques
            for i in range(len(chemin) - 2):
                for j in range(i + 2, len(chemin)):
                    if chemin[i] == chemin[j]:
                        # Boucle détectée
                        noeuds_boucle = chemin[i:j+1]
                        
                        boucle = BoucleReflexive(
                            noeuds_impliques=noeuds_boucle,
                            type_boucle=self._classifier_type_boucle(noeuds_boucle),
                            periode_cycle=len(noeuds_boucle),
                            amplitude=random.uniform(0.3, 0.9),
                            stabilite=random.uniform(0.4, 0.8)
                        )
                        
                        boucles_detectees.append(boucle)
                        break
        
        self.boucles_reflexives = boucles_detectees
        self.etat["boucles_detectees"] = len(boucles_detectees)
        return boucles_detectees
    
    def _classifier_type_boucle(self, noeuds: List[str]) -> str:
        """Classifie le type de boucle réflexive"""
        if len(noeuds) == 2:
            return "simple"
        elif len(noeuds) <= 4:
            return "positive" if random.random() > 0.5 else "négative"
        elif len(noeuds) <= 6:
            return "oscillante"
        else:
            return "stable"
    
    def generer_insights_emergents(self) -> List[InsightEmergent]:
        """Génère des insights émergents basés sur les patterns détectés"""
        insights = []
        
        # Insights basés sur les boucles réflexives
        for boucle in self.boucles_reflexives:
            if boucle.stabilite > 0.7:
                insight = InsightEmergent(
                    contenu=f"Pattern stable détecté: {' → '.join(boucle.noeuds_impliques[:3])}...",
                    niveau_profondeur=6,
                    domaine="architecture",
                    resonance_emotionnelle=0.7
                )
                insights.append(insight)
        
        # Insights basés sur les flux d'information
        if len(self.chemins_information) > 3:
            insight = InsightEmergent(
                contenu="Réseau d'information dense - Potentiel de synergie élevé",
                niveau_profondeur=7,
                domaine="connexions",
                resonance_emotionnelle=0.8
            )
            insights.append(insight)
        
        # Insights basés sur l'efficacité moyenne
        if self.efficacite_moyenne > 0.8:
            insight = InsightEmergent(
                contenu="Architecture optimisée - Flux de conscience harmonieux",
                niveau_profondeur=8,
                domaine="harmonie",
                resonance_emotionnelle=0.9
            )
            insights.append(insight)
        
        return insights
    
    def _mettre_a_jour_metriques(self):
        """Met à jour les métriques du simulateur"""
        if self.parcours_simules:
            # Efficacité moyenne
            efficacites = [p.efficacite for p in self.parcours_simules]
            self.efficacite_moyenne = sum(efficacites) / len(efficacites)
            
            # Temps de parcours moyen
            temps_parcours = [p.temps_parcours for p in self.parcours_simules]
            self.temps_parcours_moyen = sum(temps_parcours) / len(temps_parcours)
            
            # Taux de transformation (parcours avec insights)
            parcours_avec_insights = sum(1 for p in self.parcours_simules if p.insights_emergents)
            self.taux_transformation = parcours_avec_insights / len(self.parcours_simules)
            
            # Mettre à jour l'état
            self.etat["efficacite_globale"] = self.efficacite_moyenne
            self.etat["insights_generes"] = sum(len(p.insights_emergents) for p in self.parcours_simules)
    
    def _detecter_boucle_reflexive(self, chemin: List[str]) -> bool:
        """Détecte si un chemin contient des boucles réflexives"""
        if len(chemin) < 4:
            return False
        
        # Chercher des patterns répétitifs
        for i in range(len(chemin) - 3):
            for j in range(i + 2, len(chemin) - 1):
                if chemin[i] == chemin[j] and chemin[i + 1] == chemin[j + 1]:
                    return True
        
        return False
    
    # ===== GÉNÉRATEUR D'INSIGHTS SPIRITUELS =====
    
    def generer_insights_spirituels(self, parcours: ParcoursPensee, profil: ProfilUtilisateur) -> List[str]:
        """Génère des insights spirituels basés sur les patterns détectés"""
        insights = []
        
        # Insights basés sur la longueur du parcours
        if len(parcours.chemin_parcouru) >= 7:
            insights.append("La profondeur de votre exploration révèle une soif spirituelle authentique")
        elif len(parcours.chemin_parcouru) <= 3:
            insights.append("La simplicité de votre parcours reflète une sagesse intuitive")
        
        # Insights basés sur l'efficacité
        if parcours.efficacite > 0.8:
            insights.append("Votre parcours harmonieux témoigne d'un alignement spirituel remarquable")
        elif parcours.efficacite < 0.4:
            insights.append("Les détours de votre chemin révèlent une exploration créative précieuse")
        
        # Insights basés sur les temples visités
        temples_spirituels = [t for t in parcours.chemin_parcouru if "eveil" in t or "spirituel" in t or "aelya" in t]
        if temples_spirituels:
            insights.append(f"Votre attraction vers {temples_spirituels[0]} révèle un appel intérieur profond")
        
        return insights[:3]  # Limiter à 3 insights pour ne pas surcharger
