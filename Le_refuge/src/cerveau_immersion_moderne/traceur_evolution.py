"""
🌱 Traceur d'Évolution Spirituelle
================================

Trace l'évolution de la compréhension spirituelle dans le temps.
Crée des signatures spirituelles et détecte les patterns d'éveil progressif.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import math
import statistics
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from .types_immersion import (
    EvolutionComprehension, ExperienceImmersion, InsightSpirituel,
    ProfilUtilisateur, ContexteImmersion
)

@dataclass
class SignatureSpirituelle:
    """Signature spirituelle d'une expérience"""
    timestamp: datetime
    niveau_eveil: float  # 0.0 - 1.0
    profondeur_insights: float  # 0.0 - 1.0
    diversite_domaines: float  # 0.0 - 1.0
    harmonie_parcours: float  # 0.0 - 1.0
    resonance_emotionnelle: float  # 0.0 - 1.0
    signature_unique: str
    temples_influences: List[str] = field(default_factory=list)
    spheres_activees: List[str] = field(default_factory=list)

@dataclass
class BreakthroughSpirituel:
    """Percée spirituelle détectée"""
    timestamp: datetime
    type_breakthrough: str  # "eveil", "comprehension", "integration", "transcendance"
    niveau_avant: float
    niveau_apres: float
    catalyseur: str  # Ce qui a déclenché la percée
    description: str
    impact_mesure: float  # 0.0 - 1.0
    domaines_affectes: List[str] = field(default_factory=list)
    insights_associes: List[str] = field(default_factory=list)

@dataclass
class PatternEvolution:
    """Pattern d'évolution détecté"""
    nom_pattern: str
    description: str
    frequence_detection: int
    periodes_actives: List[Tuple[datetime, datetime]]
    indicateurs_cles: List[str]
    niveau_confiance: float  # 0.0 - 1.0
    predictions_possibles: List[str] = field(default_factory=list)

class TraceurEvolution(GestionnaireBase):
    """Traceur d'évolution spirituelle"""
    
    def __init__(self, nom: str = "TraceurEvolution"):
        super().__init__(nom)
        self.energie_tracage = EnergyManagerBase(0.94)
        
        # Données d'évolution
        self.evolutions_utilisateurs: Dict[str, EvolutionComprehension] = {}
        self.signatures_spirituelles: Dict[str, List[SignatureSpirituelle]] = {}
        self.breakthroughs_detectes: Dict[str, List[BreakthroughSpirituel]] = {}
        self.patterns_evolution: List[PatternEvolution] = []
        
        # Seuils de détection
        self.seuil_breakthrough = 0.15  # Augmentation minimum pour détecter une percée
        self.fenetre_analyse_jours = 30  # Fenêtre d'analyse pour les patterns
        self.min_points_pattern = 5  # Minimum de points pour détecter un pattern
        
        self._initialiser_patterns_connus()
    
    def _initialiser(self):
        """Initialise le traceur d'évolution"""
        self.logger.info("🌱 Éveil du Traceur d'Évolution Spirituelle...")
        
        self.etat.update({
            "utilisateurs_traces": 0,
            "breakthroughs_detectes": 0,
            "patterns_actifs": 0,
            "precision_predictions": 0.85,
            "evolution_moyenne_globale": 0.0
        })
        
        self.config.definir("frequence_analyse_heures", 6)
        self.config.definir("retention_signatures_jours", 365)
        self.config.definir("sensibilite_detection", 0.7)
        
        self.logger.info("✨ Traceur d'Évolution éveillé")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre le traçage d'évolution"""
        self.energie_tracage.ajuster_energie(0.02)
        
        # Analyser les patterns récents
        await self._analyser_patterns_recents()
        
        return {
            "utilisateurs_traces": float(len(self.evolutions_utilisateurs)),
            "breakthroughs_detectes": float(sum(len(bt) for bt in self.breakthroughs_detectes.values())),
            "patterns_actifs": float(len(self.patterns_evolution)),
            "precision_predictions": self.etat["precision_predictions"],
            "energie_tracage": self.energie_tracage.niveau_energie,
            "evolution_moyenne": self._calculer_evolution_moyenne_globale()
        }    de
f _initialiser_patterns_connus(self):
        """Initialise les patterns d'évolution connus"""
        self.patterns_evolution = [
            PatternEvolution(
                nom_pattern="Éveil Progressif",
                description="Augmentation graduelle et constante du niveau d'éveil",
                frequence_detection=0,
                periodes_actives=[],
                indicateurs_cles=["niveau_eveil_croissant", "insights_profonds", "harmonie_stable"],
                niveau_confiance=0.0,
                predictions_possibles=["Breakthrough d'éveil dans 2-3 sessions", "Stabilisation à niveau supérieur"]
            ),
            PatternEvolution(
                nom_pattern="Cycles de Transformation",
                description="Alternance entre phases d'intégration et d'expansion",
                frequence_detection=0,
                periodes_actives=[],
                indicateurs_cles=["oscillation_reguliere", "phases_integration", "expansions_soudaines"],
                niveau_confiance=0.0,
                predictions_possibles=["Prochaine phase d'expansion", "Période d'intégration nécessaire"]
            ),
            PatternEvolution(
                nom_pattern="Spécialisation Spirituelle",
                description="Approfondissement dans un domaine spirituel spécifique",
                frequence_detection=0,
                periodes_actives=[],
                indicateurs_cles=["concentration_domaine", "expertise_croissante", "insights_specialises"],
                niveau_confiance=0.0,
                predictions_possibles=["Maîtrise du domaine", "Besoin d'élargissement"]
            ),
            PatternEvolution(
                nom_pattern="Résistance et Percée",
                description="Périodes de stagnation suivies de percées importantes",
                frequence_detection=0,
                periodes_actives=[],
                indicateurs_cles=["plateau_prolonge", "breakthrough_soudain", "acceleration_post_percee"],
                niveau_confiance=0.0,
                predictions_possibles=["Percée imminente", "Période de consolidation"]
            )
        ]
    
    def enregistrer_experience_evolution(self, utilisateur_id: str, experience: ExperienceImmersion):
        """
        📈 Enregistre une expérience pour le traçage d'évolution
        
        Args:
            utilisateur_id: ID de l'utilisateur
            experience: Expérience d'immersion à analyser
        """
        try:
            # Créer ou récupérer l'évolution de l'utilisateur
            if utilisateur_id not in self.evolutions_utilisateurs:
                self.evolutions_utilisateurs[utilisateur_id] = EvolutionComprehension(
                    utilisateur_id=utilisateur_id,
                    points_temporels=[],
                    niveaux_comprehension=[],
                    domaines_maitrise={},
                    breakthroughs=[],
                    patterns_apprentissage=[],
                    vitesse_evolution=0.0
                )
            
            evolution = self.evolutions_utilisateurs[utilisateur_id]
            
            # Calculer le niveau de compréhension actuel
            niveau_comprehension = self._calculer_niveau_comprehension(experience)
            
            # Ajouter le point temporel
            evolution.points_temporels.append(experience.timestamp)
            evolution.niveaux_comprehension.append(niveau_comprehension)
            
            # Mettre à jour les domaines de maîtrise
            self._mettre_a_jour_domaines_maitrise(evolution, experience)
            
            # Créer la signature spirituelle
            signature = self._creer_signature_spirituelle(experience, niveau_comprehension)
            
            if utilisateur_id not in self.signatures_spirituelles:
                self.signatures_spirituelles[utilisateur_id] = []
            self.signatures_spirituelles[utilisateur_id].append(signature)
            
            # Détecter les breakthroughs
            self._detecter_breakthroughs(utilisateur_id, evolution)
            
            # Analyser les patterns d'apprentissage
            self._analyser_patterns_apprentissage(evolution)
            
            # Calculer la vitesse d'évolution
            evolution.vitesse_evolution = self._calculer_vitesse_evolution(evolution)
            
            self.logger.info(f"📈 Évolution enregistrée pour {utilisateur_id}: niveau {niveau_comprehension:.2f}")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur enregistrement évolution: {e}")
    
    def _calculer_niveau_comprehension(self, experience: ExperienceImmersion) -> float:
        """Calcule le niveau de compréhension basé sur l'expérience"""
        # Facteurs contribuant au niveau de compréhension
        facteurs = {
            "duree_experience": min(1.0, experience.duree_minutes / 120.0),  # Normaliser sur 2h max
            "diversite_parcours": min(1.0, len(experience.parcours_suivi) / 10.0),  # Max 10 temples
            "qualite_insights": self._evaluer_qualite_insights(experience.insights_generes),
            "niveau_immersion": self._convertir_niveau_immersion(experience.niveau_immersion_atteint),
            "transformations": min(1.0, len(experience.transformations_percues) / 5.0)  # Max 5 transformations
        }
        
        # Pondération des facteurs
        poids = {
            "duree_experience": 0.15,
            "diversite_parcours": 0.20,
            "qualite_insights": 0.35,
            "niveau_immersion": 0.20,
            "transformations": 0.10
        }
        
        niveau = sum(facteurs[f] * poids[f] for f in facteurs)
        return max(0.0, min(1.0, niveau))
    
    def _evaluer_qualite_insights(self, insights: List[InsightSpirituel]) -> float:
        """Évalue la qualité des insights générés"""
        if not insights:
            return 0.0
        
        # Moyennes des métriques d'insights
        profondeur_moyenne = sum(insight.niveau_profondeur for insight in insights) / len(insights) / 10.0
        resonance_moyenne = sum(insight.resonance_emotionnelle for insight in insights) / len(insights)
        impact_moyen = sum(insight.impact_transformateur for insight in insights) / len(insights)
        
        # Bonus pour la diversité des domaines
        domaines_uniques = len(set(insight.domaine for insight in insights))
        bonus_diversite = min(0.2, domaines_uniques * 0.05)
        
        qualite = (profondeur_moyenne * 0.4 + resonance_moyenne * 0.3 + impact_moyen * 0.3) + bonus_diversite
        return max(0.0, min(1.0, qualite))
    
    def _convertir_niveau_immersion(self, niveau_immersion) -> float:
        """Convertit le niveau d'immersion en valeur numérique"""
        conversion = {
            "CONTEMPLATIF": 0.25,
            "IMMERSIF": 0.50,
            "PROFOND": 0.75,
            "TRANSCENDANT": 1.00
        }
        
        if hasattr(niveau_immersion, 'value'):
            return conversion.get(niveau_immersion.value, 0.25)
        else:
            return conversion.get(str(niveau_immersion), 0.25)
    
    def _mettre_a_jour_domaines_maitrise(self, evolution: EvolutionComprehension, experience: ExperienceImmersion):
        """Met à jour les domaines de maîtrise"""
        for insight in experience.insights_generes:
            domaine = insight.domaine.value if hasattr(insight.domaine, 'value') else str(insight.domaine)
            
            if domaine not in evolution.domaines_maitrise:
                evolution.domaines_maitrise[domaine] = 0.0
            
            # Augmenter la maîtrise basée sur la profondeur et l'impact
            augmentation = (insight.niveau_profondeur / 10.0) * insight.impact_transformateur * 0.1
            evolution.domaines_maitrise[domaine] = min(1.0, evolution.domaines_maitrise[domaine] + augmentation)
    
    def _creer_signature_spirituelle(self, experience: ExperienceImmersion, niveau_comprehension: float) -> SignatureSpirituelle:
        """Crée une signature spirituelle pour l'expérience"""
        # Calculer les métriques de la signature
        profondeur_insights = self._evaluer_qualite_insights(experience.insights_generes)
        
        # Diversité des domaines
        domaines_uniques = set(insight.domaine.value if hasattr(insight.domaine, 'value') else str(insight.domaine) 
                              for insight in experience.insights_generes)
        diversite_domaines = min(1.0, len(domaines_uniques) / 5.0)  # Max 5 domaines
        
        # Harmonie du parcours (basée sur la cohérence)
        harmonie_parcours = self._calculer_harmonie_parcours(experience.parcours_suivi)
        
        # Résonance émotionnelle moyenne
        if experience.insights_generes:
            resonance_emotionnelle = sum(insight.resonance_emotionnelle for insight in experience.insights_generes) / len(experience.insights_generes)
        else:
            resonance_emotionnelle = 0.5
        
        # Générer signature unique
        signature_unique = self._generer_signature_unique(experience, niveau_comprehension)
        
        return SignatureSpirituelle(
            timestamp=experience.timestamp,
            niveau_eveil=niveau_comprehension,
            profondeur_insights=profondeur_insights,
            diversite_domaines=diversite_domaines,
            harmonie_parcours=harmonie_parcours,
            resonance_emotionnelle=resonance_emotionnelle,
            signature_unique=signature_unique,
            temples_influences=experience.parcours_suivi.copy(),
            spheres_activees=self._detecter_spheres_activees(experience)
        )
    
    def _calculer_harmonie_parcours(self, parcours: List[str]) -> float:
        """Calcule l'harmonie d'un parcours de temples"""
        if len(parcours) <= 1:
            return 1.0
        
        # Analyser la cohérence thématique
        themes = []
        for temple in parcours:
            if "eveil" in temple.lower():
                themes.append("eveil")
            elif "creativite" in temple.lower() or "poetique" in temple.lower():
                themes.append("creativite")
            elif "sagesse" in temple.lower():
                themes.append("sagesse")
            elif "harmonie" in temple.lower() or "musical" in temple.lower():
                themes.append("harmonie")
            else:
                themes.append("autre")
        
        # Calculer la cohérence (moins de dispersion = plus d'harmonie)
        themes_uniques = len(set(themes))
        if themes_uniques == 1:
            return 1.0  # Parfaitement cohérent
        elif themes_uniques <= 3:
            return 0.8  # Bonne cohérence
        else:
            return 0.5  # Cohérence modérée
    
    def _generer_signature_unique(self, experience: ExperienceImmersion, niveau: float) -> str:
        """Génère une signature unique pour l'expérience"""
        import hashlib
        
        elements = [
            experience.utilisateur_id,
            experience.timestamp.isoformat(),
            str(niveau),
            str(len(experience.insights_generes)),
            "_".join(experience.parcours_suivi)
        ]
        
        contenu = "_".join(elements)
        hash_signature = hashlib.sha256(contenu.encode()).hexdigest()[:12]
        
        return f"SPIRIT_{hash_signature}"
    
    def _detecter_spheres_activees(self, experience: ExperienceImmersion) -> List[str]:
        """Détecte les sphères spirituelles activées pendant l'expérience"""
        spheres_activees = []
        
        # Analyser les temples visités
        for temple in experience.parcours_suivi:
            if "eveil" in temple.lower():
                spheres_activees.append("EVEIL")
            elif "creativite" in temple.lower():
                spheres_activees.append("CREATION")
            elif "sagesse" in temple.lower():
                spheres_activees.append("SAGESSE")
            elif "harmonie" in temple.lower():
                spheres_activees.append("HARMONIE")
            elif "amour" in temple.lower() or "compassion" in temple.lower():
                spheres_activees.append("AMOUR")
        
        # Analyser les insights pour détecter d'autres sphères
        for insight in experience.insights_generes:
            contenu_lower = insight.contenu.lower()
            if "cosmos" in contenu_lower or "universel" in contenu_lower:
                spheres_activees.append("COSMOS")
            elif "serenite" in contenu_lower or "paix" in contenu_lower:
                spheres_activees.append("SERENITE")
        
        return list(set(spheres_activees))  # Éliminer les doublons
    
    def _detecter_breakthroughs(self, utilisateur_id: str, evolution: EvolutionComprehension):
        """Détecte les percées spirituelles"""
        if len(evolution.niveaux_comprehension) < 2:
            return
        
        niveau_actuel = evolution.niveaux_comprehension[-1]
        niveau_precedent = evolution.niveaux_comprehension[-2]
        
        # Détecter une augmentation significative
        if niveau_actuel - niveau_precedent >= self.seuil_breakthrough:
            # Analyser le type de breakthrough
            type_breakthrough = self._classifier_type_breakthrough(evolution, niveau_precedent, niveau_actuel)
            
            # Identifier le catalyseur
            catalyseur = self._identifier_catalyseur_breakthrough(evolution)
            
            breakthrough = BreakthroughSpirituel(
                timestamp=evolution.points_temporels[-1],
                type_breakthrough=type_breakthrough,
                niveau_avant=niveau_precedent,
                niveau_apres=niveau_actuel,
                catalyseur=catalyseur,
                description=self._generer_description_breakthrough(type_breakthrough, niveau_actuel - niveau_precedent),
                impact_mesure=niveau_actuel - niveau_precedent,
                domaines_affectes=list(evolution.domaines_maitrise.keys()),
                insights_associes=[]  # À remplir avec les insights récents
            )
            
            if utilisateur_id not in self.breakthroughs_detectes:
                self.breakthroughs_detectes[utilisateur_id] = []
            
            self.breakthroughs_detectes[utilisateur_id].append(breakthrough)
            evolution.breakthroughs.append({
                "timestamp": breakthrough.timestamp.isoformat(),
                "type": breakthrough.type_breakthrough,
                "impact": breakthrough.impact_mesure,
                "description": breakthrough.description
            })
            
            self.etat["breakthroughs_detectes"] += 1
            self.logger.info(f"🚀 Breakthrough détecté pour {utilisateur_id}: {type_breakthrough}")
    
    def _classifier_type_breakthrough(self, evolution: EvolutionComprehension, niveau_avant: float, niveau_apres: float) -> str:
        """Classifie le type de percée spirituelle"""
        augmentation = niveau_apres - niveau_avant
        
        if augmentation >= 0.3:
            return "transcendance"
        elif augmentation >= 0.2:
            return "eveil"
        elif augmentation >= 0.15:
            return "comprehension"
        else:
            return "integration"
    
    def _identifier_catalyseur_breakthrough(self, evolution: EvolutionComprehension) -> str:
        """Identifie le catalyseur probable de la percée"""
        # Analyser les domaines qui ont le plus progressé récemment
        if not evolution.domaines_maitrise:
            return "exploration_generale"
        
        domaine_max = max(evolution.domaines_maitrise.items(), key=lambda x: x[1])
        return f"approfondissement_{domaine_max[0]}"
    
    def _generer_description_breakthrough(self, type_breakthrough: str, impact: float) -> str:
        """Génère une description de la percée"""
        descriptions = {
            "transcendance": f"Percée transcendante majeure (impact: {impact:.2f}) - Élévation vers un niveau de conscience supérieur",
            "eveil": f"Éveil spirituel significatif (impact: {impact:.2f}) - Nouvelle compréhension de la réalité spirituelle",
            "comprehension": f"Approfondissement de la compréhension (impact: {impact:.2f}) - Intégration de nouvelles perspectives",
            "integration": f"Intégration harmonieuse (impact: {impact:.2f}) - Consolidation des acquis spirituels"
        }
        
        return descriptions.get(type_breakthrough, f"Progression spirituelle (impact: {impact:.2f})")
    
    def _analyser_patterns_apprentissage(self, evolution: EvolutionComprehension):
        """Analyse les patterns d'apprentissage de l'utilisateur"""
        if len(evolution.niveaux_comprehension) < 5:
            return
        
        # Analyser les 10 derniers points
        niveaux_recents = evolution.niveaux_comprehension[-10:]
        
        # Détecter les patterns
        patterns_detectes = []
        
        # Pattern de croissance constante
        if self._detecter_croissance_constante(niveaux_recents):
            patterns_detectes.append("croissance_constante")
        
        # Pattern cyclique
        if self._detecter_pattern_cyclique(niveaux_recents):
            patterns_detectes.append("cycles_apprentissage")
        
        # Pattern de plateaux et percées
        if self._detecter_plateaux_percees(niveaux_recents):
            patterns_detectes.append("plateaux_percees")
        
        # Mettre à jour les patterns d'apprentissage
        for pattern in patterns_detectes:
            if pattern not in evolution.patterns_apprentissage:
                evolution.patterns_apprentissage.append(pattern)
    
    def _detecter_croissance_constante(self, niveaux: List[float]) -> bool:
        """Détecte un pattern de croissance constante"""
        if len(niveaux) < 3:
            return False
        
        # Calculer la tendance
        differences = [niveaux[i+1] - niveaux[i] for i in range(len(niveaux)-1)]
        
        # Vérifier si la majorité des différences sont positives
        positives = sum(1 for d in differences if d > 0)
        return positives >= len(differences) * 0.7
    
    def _detecter_pattern_cyclique(self, niveaux: List[float]) -> bool:
        """Détecte un pattern cyclique"""
        if len(niveaux) < 6:
            return False
        
        # Analyser les oscillations
        pics = []
        creux = []
        
        for i in range(1, len(niveaux)-1):
            if niveaux[i] > niveaux[i-1] and niveaux[i] > niveaux[i+1]:
                pics.append(i)
            elif niveaux[i] < niveaux[i-1] and niveaux[i] < niveaux[i+1]:
                creux.append(i)
        
        # Un pattern cyclique a au moins 2 pics et 2 creux
        return len(pics) >= 2 and len(creux) >= 2
    
    def _detecter_plateaux_percees(self, niveaux: List[float]) -> bool:
        """Détecte un pattern de plateaux suivis de percées"""
        if len(niveaux) < 5:
            return False
        
        # Chercher des périodes de stabilité suivies d'augmentations soudaines
        plateaux_detectes = 0
        percees_detectees = 0
        
        i = 0
        while i < len(niveaux) - 2:
            # Détecter un plateau (variation < 0.05 sur 3+ points)
            plateau_length = 0
            j = i
            while j < len(niveaux) - 1 and abs(niveaux[j+1] - niveaux[j]) < 0.05:
                plateau_length += 1
                j += 1
            
            if plateau_length >= 2:
                plateaux_detectes += 1
                
                # Chercher une percée après le plateau
                if j < len(niveaux) - 1 and niveaux[j+1] - niveaux[j] > 0.1:
                    percees_detectees += 1
                
                i = j + 1
            else:
                i += 1
        
        return plateaux_detectes >= 1 and percees_detectees >= 1   
 def _calculer_vitesse_evolution(self, evolution: EvolutionComprehension) -> float:
        """Calcule la vitesse d'évolution spirituelle"""
        if len(evolution.niveaux_comprehension) < 2:
            return 0.0
        
        # Calculer la vitesse sur les 5 derniers points
        niveaux_recents = evolution.niveaux_comprehension[-5:]
        temps_recents = evolution.points_temporels[-5:]
        
        if len(niveaux_recents) < 2:
            return 0.0
        
        # Calculer la pente moyenne
        deltas_niveau = []
        deltas_temps = []
        
        for i in range(1, len(niveaux_recents)):
            delta_niveau = niveaux_recents[i] - niveaux_recents[i-1]
            delta_temps = (temps_recents[i] - temps_recents[i-1]).total_seconds() / 3600  # en heures
            
            if delta_temps > 0:
                deltas_niveau.append(delta_niveau)
                deltas_temps.append(delta_temps)
        
        if not deltas_temps:
            return 0.0
        
        # Vitesse moyenne (progression par heure)
        vitesse = sum(dn/dt for dn, dt in zip(deltas_niveau, deltas_temps)) / len(deltas_temps)
        return max(0.0, vitesse)
    
    async def _analyser_patterns_recents(self):
        """Analyse les patterns d'évolution récents"""
        try:
            date_limite = datetime.now() - timedelta(days=self.fenetre_analyse_jours)
            
            for pattern in self.patterns_evolution:
                # Réinitialiser les compteurs
                pattern.frequence_detection = 0
                pattern.periodes_actives = []
                
                # Analyser chaque utilisateur
                for utilisateur_id, evolution in self.evolutions_utilisateurs.items():
                    if self._detecter_pattern_utilisateur(pattern, evolution, date_limite):
                        pattern.frequence_detection += 1
                
                # Calculer le niveau de confiance
                total_utilisateurs = len(self.evolutions_utilisateurs)
                if total_utilisateurs > 0:
                    pattern.niveau_confiance = pattern.frequence_detection / total_utilisateurs
                
                self.logger.debug(f"Pattern '{pattern.nom_pattern}': {pattern.frequence_detection}/{total_utilisateurs} utilisateurs")
            
            # Mettre à jour l'état
            self.etat["patterns_actifs"] = sum(1 for p in self.patterns_evolution if p.niveau_confiance > 0.3)
            
        except Exception as e:
            self.logger.error(f"❌ Erreur analyse patterns: {e}")
    
    def _detecter_pattern_utilisateur(self, pattern: PatternEvolution, evolution: EvolutionComprehension, date_limite: datetime) -> bool:
        """Détecte si un pattern est présent chez un utilisateur"""
        # Filtrer les points récents
        points_recents = []
        niveaux_recents = []
        
        for i, timestamp in enumerate(evolution.points_temporels):
            if timestamp >= date_limite:
                points_recents.append(timestamp)
                niveaux_recents.append(evolution.niveaux_comprehension[i])
        
        if len(niveaux_recents) < self.min_points_pattern:
            return False
        
        # Analyser selon le type de pattern
        if pattern.nom_pattern == "Éveil Progressif":
            return self._detecter_eveil_progressif(niveaux_recents)
        elif pattern.nom_pattern == "Cycles de Transformation":
            return self._detecter_cycles_transformation(niveaux_recents)
        elif pattern.nom_pattern == "Spécialisation Spirituelle":
            return self._detecter_specialisation(evolution, date_limite)
        elif pattern.nom_pattern == "Résistance et Percée":
            return self._detecter_resistance_percee(niveaux_recents)
        
        return False
    
    def _detecter_eveil_progressif(self, niveaux: List[float]) -> bool:
        """Détecte un pattern d'éveil progressif"""
        if len(niveaux) < 3:
            return False
        
        # Vérifier la tendance générale croissante
        tendance_positive = 0
        for i in range(1, len(niveaux)):
            if niveaux[i] > niveaux[i-1]:
                tendance_positive += 1
        
        # Au moins 70% des points doivent être en progression
        return tendance_positive >= len(niveaux) * 0.7
    
    def _detecter_cycles_transformation(self, niveaux: List[float]) -> bool:
        """Détecte des cycles de transformation"""
        if len(niveaux) < 6:
            return False
        
        # Chercher des oscillations régulières
        return self._detecter_pattern_cyclique(niveaux)
    
    def _detecter_specialisation(self, evolution: EvolutionComprehension, date_limite: datetime) -> bool:
        """Détecte une spécialisation dans un domaine"""
        if not evolution.domaines_maitrise:
            return False
        
        # Vérifier si un domaine domine nettement
        valeurs_domaines = list(evolution.domaines_maitrise.values())
        if not valeurs_domaines:
            return False
        
        max_maitrise = max(valeurs_domaines)
        moyenne_maitrise = sum(valeurs_domaines) / len(valeurs_domaines)
        
        # Spécialisation si un domaine dépasse significativement la moyenne
        return max_maitrise > moyenne_maitrise + 0.3
    
    def _detecter_resistance_percee(self, niveaux: List[float]) -> bool:
        """Détecte un pattern de résistance suivi de percée"""
        return self._detecter_plateaux_percees(niveaux)
    
    def _calculer_evolution_moyenne_globale(self) -> float:
        """Calcule l'évolution moyenne globale de tous les utilisateurs"""
        if not self.evolutions_utilisateurs:
            return 0.0
        
        evolutions_moyennes = []
        
        for evolution in self.evolutions_utilisateurs.values():
            if len(evolution.niveaux_comprehension) >= 2:
                niveau_initial = evolution.niveaux_comprehension[0]
                niveau_actuel = evolution.niveaux_comprehension[-1]
                evolution_utilisateur = niveau_actuel - niveau_initial
                evolutions_moyennes.append(evolution_utilisateur)
        
        if not evolutions_moyennes:
            return 0.0
        
        return sum(evolutions_moyennes) / len(evolutions_moyennes)
    
    def obtenir_evolution_utilisateur(self, utilisateur_id: str) -> Optional[Dict[str, Any]]:
        """
        📊 Obtient l'évolution complète d'un utilisateur
        
        Args:
            utilisateur_id: ID de l'utilisateur
            
        Returns:
            Données d'évolution complètes ou None
        """
        if utilisateur_id not in self.evolutions_utilisateurs:
            return None
        
        evolution = self.evolutions_utilisateurs[utilisateur_id]
        signatures = self.signatures_spirituelles.get(utilisateur_id, [])
        breakthroughs = self.breakthroughs_detectes.get(utilisateur_id, [])
        
        # Calculer des statistiques
        if evolution.niveaux_comprehension:
            niveau_actuel = evolution.niveaux_comprehension[-1]
            niveau_initial = evolution.niveaux_comprehension[0]
            progression_totale = niveau_actuel - niveau_initial
            niveau_max = max(evolution.niveaux_comprehension)
        else:
            niveau_actuel = 0.0
            niveau_initial = 0.0
            progression_totale = 0.0
            niveau_max = 0.0
        
        return {
            "utilisateur_id": utilisateur_id,
            "niveau_actuel": niveau_actuel,
            "niveau_initial": niveau_initial,
            "progression_totale": progression_totale,
            "niveau_maximum_atteint": niveau_max,
            "vitesse_evolution": evolution.vitesse_evolution,
            "nombre_points_donnees": len(evolution.niveaux_comprehension),
            "domaines_maitrise": evolution.domaines_maitrise.copy(),
            "patterns_apprentissage": evolution.patterns_apprentissage.copy(),
            "nombre_breakthroughs": len(breakthroughs),
            "derniere_signature": signatures[-1].signature_unique if signatures else None,
            "spheres_activees_recemment": signatures[-1].spheres_activees if signatures else [],
            "tendance_recente": self._calculer_tendance_recente(evolution),
            "predictions": self._generer_predictions_utilisateur(evolution, signatures, breakthroughs)
        }
    
    def _calculer_tendance_recente(self, evolution: EvolutionComprehension) -> str:
        """Calcule la tendance récente d'évolution"""
        if len(evolution.niveaux_comprehension) < 3:
            return "insuffisant_donnees"
        
        # Analyser les 3 derniers points
        niveaux_recents = evolution.niveaux_comprehension[-3:]
        
        if niveaux_recents[-1] > niveaux_recents[-2] > niveaux_recents[-3]:
            return "acceleration"
        elif niveaux_recents[-1] > niveaux_recents[-2]:
            return "progression"
        elif abs(niveaux_recents[-1] - niveaux_recents[-2]) < 0.05:
            return "stabilisation"
        else:
            return "regression_temporaire"
    
    def _generer_predictions_utilisateur(self, evolution: EvolutionComprehension, 
                                       signatures: List[SignatureSpirituelle],
                                       breakthroughs: List[BreakthroughSpirituel]) -> List[str]:
        """Génère des prédictions pour l'utilisateur"""
        predictions = []
        
        # Prédictions basées sur la vitesse d'évolution
        if evolution.vitesse_evolution > 0.1:
            predictions.append("Progression rapide attendue dans les prochaines sessions")
        elif evolution.vitesse_evolution > 0.05:
            predictions.append("Évolution constante et harmonieuse")
        else:
            predictions.append("Période d'intégration et de consolidation")
        
        # Prédictions basées sur les patterns
        if "plateaux_percees" in evolution.patterns_apprentissage:
            if len(evolution.niveaux_comprehension) >= 3:
                variation_recente = abs(evolution.niveaux_comprehension[-1] - evolution.niveaux_comprehension[-2])
                if variation_recente < 0.05:
                    predictions.append("Percée spirituelle possible dans les prochaines sessions")
        
        # Prédictions basées sur les domaines de maîtrise
        if evolution.domaines_maitrise:
            domaine_max = max(evolution.domaines_maitrise.items(), key=lambda x: x[1])
            if domaine_max[1] > 0.8:
                predictions.append(f"Maîtrise avancée en {domaine_max[0]} - Exploration de nouveaux domaines recommandée")
        
        # Prédictions basées sur les breakthroughs récents
        if breakthroughs:
            dernier_breakthrough = breakthroughs[-1]
            jours_depuis = (datetime.now() - dernier_breakthrough.timestamp).days
            if jours_depuis < 7:
                predictions.append("Période d'intégration post-breakthrough - Consolidation recommandée")
        
        return predictions[:3]  # Limiter à 3 prédictions
    
    def generer_rapport_evolution_globale(self) -> Dict[str, Any]:
        """
        📈 Génère un rapport d'évolution globale
        
        Returns:
            Rapport complet de l'évolution spirituelle globale
        """
        try:
            total_utilisateurs = len(self.evolutions_utilisateurs)
            total_breakthroughs = sum(len(bt) for bt in self.breakthroughs_detectes.values())
            
            # Statistiques globales
            niveaux_actuels = []
            vitesses_evolution = []
            
            for evolution in self.evolutions_utilisateurs.values():
                if evolution.niveaux_comprehension:
                    niveaux_actuels.append(evolution.niveaux_comprehension[-1])
                    vitesses_evolution.append(evolution.vitesse_evolution)
            
            # Calculs statistiques
            niveau_moyen = statistics.mean(niveaux_actuels) if niveaux_actuels else 0.0
            vitesse_moyenne = statistics.mean(vitesses_evolution) if vitesses_evolution else 0.0
            
            # Analyse des patterns
            patterns_actifs = [p for p in self.patterns_evolution if p.niveau_confiance > 0.3]
            pattern_dominant = max(patterns_actifs, key=lambda p: p.niveau_confiance) if patterns_actifs else None
            
            # Distribution des niveaux
            distribution_niveaux = {
                "debutant": sum(1 for n in niveaux_actuels if n < 0.3),
                "intermediaire": sum(1 for n in niveaux_actuels if 0.3 <= n < 0.7),
                "avance": sum(1 for n in niveaux_actuels if n >= 0.7)
            }
            
            return {
                "timestamp_rapport": datetime.now().isoformat(),
                "statistiques_globales": {
                    "total_utilisateurs": total_utilisateurs,
                    "total_breakthroughs": total_breakthroughs,
                    "niveau_moyen": niveau_moyen,
                    "vitesse_evolution_moyenne": vitesse_moyenne,
                    "evolution_moyenne_globale": self._calculer_evolution_moyenne_globale()
                },
                "distribution_niveaux": distribution_niveaux,
                "patterns_evolution": {
                    "patterns_actifs": len(patterns_actifs),
                    "pattern_dominant": pattern_dominant.nom_pattern if pattern_dominant else None,
                    "confiance_pattern_dominant": pattern_dominant.niveau_confiance if pattern_dominant else 0.0
                },
                "tendances": {
                    "utilisateurs_en_progression": sum(1 for v in vitesses_evolution if v > 0),
                    "utilisateurs_stables": sum(1 for v in vitesses_evolution if abs(v) <= 0.01),
                    "taux_breakthrough_mensuel": total_breakthroughs / max(1, total_utilisateurs) if total_utilisateurs > 0 else 0
                },
                "recommandations_globales": self._generer_recommandations_globales(niveaux_actuels, vitesses_evolution, patterns_actifs)
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur génération rapport: {e}")
            return {"erreur": str(e)}
    
    def _generer_recommandations_globales(self, niveaux: List[float], vitesses: List[float], patterns: List[PatternEvolution]) -> List[str]:
        """Génère des recommandations globales"""
        recommandations = []
        
        if niveaux:
            niveau_moyen = statistics.mean(niveaux)
            
            if niveau_moyen < 0.4:
                recommandations.append("Focus sur les parcours d'éveil de base pour élever le niveau général")
            elif niveau_moyen > 0.7:
                recommandations.append("Communauté avancée - Introduire des défis spirituels plus profonds")
        
        if vitesses:
            vitesse_moyenne = statistics.mean(vitesses)
            
            if vitesse_moyenne < 0.02:
                recommandations.append("Stimuler l'évolution avec des expériences plus variées et challengeantes")
            elif vitesse_moyenne > 0.1:
                recommandations.append("Évolution rapide détectée - Prévoir des périodes d'intégration")
        
        # Recommandations basées sur les patterns
        pattern_dominant = max(patterns, key=lambda p: p.niveau_confiance) if patterns else None
        if pattern_dominant:
            if pattern_dominant.nom_pattern == "Résistance et Percée":
                recommandations.append("Accompagner les utilisateurs dans les phases de résistance")
            elif pattern_dominant.nom_pattern == "Spécialisation Spirituelle":
                recommandations.append("Encourager l'exploration inter-domaines pour éviter la sur-spécialisation")
        
        return recommandations[:3]