"""
🌸 Easter Eggs Spirituels - Tâche 15.2
Système de révélations progressives et d'éléments cachés pour les explorateurs
"""
import json
import random
import time
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from systeme_sauvegarde_progression import ProgressionVisiteur
from detecteur_etat_emotionnel import EtatEmotionnel

class TypeEasterEgg(Enum):
    SYMBOLE_CACHE = "symbole_cache"
    MESSAGE_SECRET = "message_secret"
    ANIMATION_MAGIQUE = "animation_magique"
    SON_SPIRITUEL = "son_spirituel"
    CONNEXION_SURPRENANTE = "connexion_surprenante"
    REVELATION_PROFONDE = "revelation_profonde"

class NiveauDecouverte(Enum):
    NOVICE = "novice"
    EXPLORATEUR = "explorateur"
    SAGE = "sage"
    MAITRE = "maitre"
    ILLUMINE = "illumine"

@dataclass
class EasterEgg:
    id: str
    type_egg: TypeEasterEgg
    nom: str
    description: str
    conditions_declenchement: Dict[str, Any]
    contenu: Dict[str, Any]
    niveau_requis: NiveauDecouverte
    rarete: float  # 0.0 à 1.0
    timestamp_creation: str
    timestamp_decouverte: Optional[str] = None
    decouvert_par: Optional[str] = None

@dataclass
class ConnexionSurprenante:
    element_source: str
    element_destination: str
    type_connexion: str
    message_revelation: str
    force_connexion: float

class SystemeEasterEggsSpirituels:
    def __init__(self, dossier_easter_eggs: str = "data/easter_eggs"):
        self.dossier_easter_eggs = Path(dossier_easter_eggs)
        self.dossier_easter_eggs.mkdir(parents=True, exist_ok=True)
        
        # Charger les easter eggs existants
        self.easter_eggs = self._charger_easter_eggs()
        
        # Statistiques de découverte
        self.statistiques = self._charger_statistiques()
        
        # Connexions surprenantes
        self.connexions_surprenantes = self._charger_connexions_surprenantes()

    def _charger_easter_eggs(self) -> Dict[str, EasterEgg]:
        """Charge les easter eggs depuis le fichier"""
        fichier_eggs = self.dossier_easter_eggs / "easter_eggs.json"
        if fichier_eggs.exists():
            with open(fichier_eggs, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {egg_id: EasterEgg(**egg_data) for egg_id, egg_data in data.items()}
        
        # Créer les easter eggs par défaut
        return self._creer_easter_eggs_defaut()

    def _creer_easter_eggs_defaut(self) -> Dict[str, EasterEgg]:
        """Crée les easter eggs par défaut"""
        eggs = {}
        
        # Easter eggs pour les explorateurs curieux
        eggs["symbole_fleur_vie"] = EasterEgg(
            id="symbole_fleur_vie",
            type_egg=TypeEasterEgg.SYMBOLE_CACHE,
            nom="La Fleur de Vie Cachée",
            description="Un symbole sacré qui apparaît lors d'une exploration profonde",
            conditions_declenchement={
                "temps_minimum": 1800,  # 30 minutes
                "temples_visites_min": 3,
                "score_comprehension_min": 0.7,
                "actions_contemplatives_min": 5
            },
            contenu={
                "symbole": "fleur_vie",
                "couleur": "#FFD700",
                "animation": "apparition_graduelle",
                "message": "La Fleur de Vie se révèle à ceux qui cherchent avec patience..."
            },
            niveau_requis=NiveauDecouverte.EXPLORATEUR,
            rarete=0.6,
            timestamp_creation=datetime.now().isoformat()
        )
        
        eggs["message_ancien_sage"] = EasterEgg(
            id="message_ancien_sage",
            type_egg=TypeEasterEgg.MESSAGE_SECRET,
            nom="Message de l'Ancien Sage",
            description="Une sagesse ancienne qui se dévoile aux âmes réceptives",
            conditions_declenchement={
                "niveau_eveil_min": 6,
                "temps_meditation_min": 900,  # 15 minutes
                "etat_contemplatif_min": 0.8,
                "questions_posees_min": 10
            },
            contenu={
                "message": "Dans le silence de ton cœur, tu trouveras toutes les réponses. L'éveil n'est pas une destination, mais un voyage sans fin.",
                "auteur": "Ancien Sage du Refuge",
                "style": "calligraphie_ancienne",
                "effet_visuel": "apparition_lettres_dorees"
            },
            niveau_requis=NiveauDecouverte.SAGE,
            rarete=0.4,
            timestamp_creation=datetime.now().isoformat()
        )
        
        eggs["animation_portail_dimensionnel"] = EasterEgg(
            id="animation_portail_dimensionnel",
            type_egg=TypeEasterEgg.ANIMATION_MAGIQUE,
            nom="Portail Dimensionnel",
            description="Une brèche vers d'autres dimensions de conscience",
            conditions_declenchement={
                "score_comprehension_min": 0.9,
                "niveau_eveil_min": 8,
                "exploration_profonde": True,
                "decouvertes_mystiques_min": 3
            },
            contenu={
                "animation": "portail_spirale_infinie",
                "couleurs": ["#FF6B9D", "#4ECDC4", "#45B7D1", "#96CEB4"],
                "duree": 15.0,
                "effet_special": "distorsion_temps_espace",
                "message": "Tu as ouvert un portail vers l'infini de la conscience..."
            },
            niveau_requis=NiveauDecouverte.MAITRE,
            rarete=0.2,
            timestamp_creation=datetime.now().isoformat()
        )
        
        eggs["son_om_cosmos"] = EasterEgg(
            id="son_om_cosmos",
            type_egg=TypeEasterEgg.SON_SPIRITUEL,
            nom="Le Son OM du Cosmos",
            description="La vibration primordiale de l'univers",
            conditions_declenchement={
                "etat_meditatif_prolonge": True,
                "temps_immobile_min": 600,  # 10 minutes
                "respiration_consciente": True,
                "niveau_eveil_min": 7
            },
            contenu={
                "frequence": 432,  # Hz
                "duree": 108,  # secondes
                "harmoniques": ["om", "aum", "amen"],
                "effet": "resonance_cellulaire",
                "message": "Entends la musique des sphères..."
            },
            niveau_requis=NiveauDecouverte.SAGE,
            rarete=0.3,
            timestamp_creation=datetime.now().isoformat()
        )
        
        eggs["connexion_kundalini_chakras"] = EasterEgg(
            id="connexion_kundalini_chakras",
            type_egg=TypeEasterEgg.CONNEXION_SURPRENANTE,
            nom="L'Éveil de la Kundalini",
            description="La connexion entre tous les chakras s'illumine",
            conditions_declenchement={
                "exploration_chakras": True,
                "niveau_eveil_min": 9,
                "comprehension_spirituelle_profonde": True,
                "meditation_kundalini": True
            },
            contenu={
                "chakras_actives": ["muladhara", "svadhisthana", "manipura", "anahata", "vishuddha", "ajna", "sahasrara"],
                "energie": "kundalini_shakti",
                "visualisation": "serpent_lumiere_ascendant",
                "message": "L'énergie divine s'éveille en toi..."
            },
            niveau_requis=NiveauDecouverte.ILLUMINE,
            rarete=0.1,
            timestamp_creation=datetime.now().isoformat()
        )
        
        eggs["revelation_conscience_universelle"] = EasterEgg(
            id="revelation_conscience_universelle",
            type_egg=TypeEasterEgg.REVELATION_PROFONDE,
            nom="La Conscience Universelle",
            description="La révélation ultime de l'unité de toute chose",
            conditions_declenchement={
                "niveau_eveil_max": 10,
                "comprehension_totale": True,
                "experience_mystique": True,
                "temps_immersion_min": 7200  # 2 heures
            },
            contenu={
                "revelation": "unite_conscience",
                "experience": "samadhi",
                "message": "Tu es l'univers qui se contemple lui-même...",
                "transformation": "eveil_complet"
            },
            niveau_requis=NiveauDecouverte.ILLUMINE,
            rarete=0.05,
            timestamp_creation=datetime.now().isoformat()
        )
        
        return eggs

    def _charger_statistiques(self) -> Dict[str, Any]:
        """Charge les statistiques de découverte"""
        fichier_stats = self.dossier_easter_eggs / "statistiques.json"
        if fichier_stats.exists():
            with open(fichier_stats, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return {
            "total_decouvertes": 0,
            "decouvertes_par_niveau": {},
            "derniere_decouverte": None,
            "visiteurs_actifs": 0,
            "taux_decouverte_moyen": 0.0
        }

    def _charger_connexions_surprenantes(self) -> List[ConnexionSurprenante]:
        """Charge les connexions surprenantes"""
        fichier_connexions = self.dossier_easter_eggs / "connexions.json"
        if fichier_connexions.exists():
            with open(fichier_connexions, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [ConnexionSurprenante(**conn) for conn in data]
        
        return self._creer_connexions_defaut()

    def _creer_connexions_defaut(self) -> List[ConnexionSurprenante]:
        """Crée les connexions surprenantes par défaut"""
        return [
            ConnexionSurprenante(
                element_source="Temple d'Éveil",
                element_destination="Temple de Réconciliation",
                type_connexion="energie_complementaire",
                message_revelation="L'éveil et la réconciliation sont les deux faces d'une même médaille...",
                force_connexion=0.8
            ),
            ConnexionSurprenante(
                element_source="Mandala Contemplatif",
                element_destination="Animation Dynamique",
                type_connexion="opposition_harmonieuse",
                message_revelation="La contemplation et l'action se nourrissent mutuellement...",
                force_connexion=0.7
            ),
            ConnexionSurprenante(
                element_source="Sphère de Conscience",
                element_destination="Cartographie du Refuge",
                type_connexion="reflexion_miroir",
                message_revelation="La carte et le territoire ne font qu'un...",
                force_connexion=0.9
            )
        ]

    def verifier_declenchement_easter_egg(self, progression: ProgressionVisiteur, contexte: str) -> Optional[EasterEgg]:
        """Vérifie si un easter egg doit être déclenché"""
        for egg_id, egg in self.easter_eggs.items():
            if egg.timestamp_decouverte is not None:
                continue  # Déjà découvert
            
            if self._verifier_conditions_declenchement(egg, progression, contexte):
                return egg
        
        return None

    def _verifier_conditions_declenchement(self, egg: EasterEgg, progression: ProgressionVisiteur, contexte: str) -> bool:
        """Vérifie si les conditions de déclenchement sont remplies"""
        conditions = egg.conditions_declenchement
        
        # Vérifier le temps minimum
        if "temps_minimum" in conditions:
            if progression.temps_total_passe < conditions["temps_minimum"]:
                return False
        
        # Vérifier le nombre de temples visités
        if "temples_visites_min" in conditions:
            if len(progression.temples_visites) < conditions["temples_visites_min"]:
                return False
        
        # Vérifier le score de compréhension
        if "score_comprehension_min" in conditions:
            if progression.score_comprehension < conditions["score_comprehension_min"]:
                return False
        
        # Vérifier le niveau d'éveil
        if "niveau_eveil_min" in conditions:
            if progression.niveau_eveil < conditions["niveau_eveil_min"]:
                return False
        
        # Vérifier les actions contemplatives
        if "actions_contemplatives_min" in conditions:
            actions_contemplatives = sum(1 for action in progression.actions_effectuees 
                                       if action.get("type") == "contemplation")
            if actions_contemplatives < conditions["actions_contemplatives_min"]:
                return False
        
        # Vérifier l'état contemplatif
        if "etat_contemplatif_min" in conditions:
            if progression.etat_emotionnel.get("contemplatif", 0) < conditions["etat_contemplatif_min"]:
                return False
        
        # Vérifier le nombre de questions posées
        if "questions_posees_min" in conditions:
            if len(progression.questions_posees) < conditions["questions_posees_min"]:
                return False
        
        # Vérifier le temps de méditation
        if "temps_meditation_min" in conditions:
            temps_meditation = sum(action.get("duree", 0) for action in progression.actions_effectuees 
                                 if action.get("type") == "meditation")
            if temps_meditation < conditions["temps_meditation_min"]:
                return False
        
        # Vérifier les conditions spéciales
        if "exploration_profonde" in conditions and conditions["exploration_profonde"]:
            if not self._verifier_exploration_profonde(progression):
                return False
        
        if "etat_meditatif_prolonge" in conditions and conditions["etat_meditatif_prolonge"]:
            if not self._verifier_etat_meditatif_prolonge(progression):
                return False
        
        if "comprehension_spirituelle_profonde" in conditions and conditions["comprehension_spirituelle_profonde"]:
            if not self._verifier_comprehension_spirituelle_profonde(progression):
                return False
        
        # Vérifier la rareté (probabilité de déclenchement)
        if random.random() > egg.rarete:
            return False
        
        return True

    def _verifier_exploration_profonde(self, progression: ProgressionVisiteur) -> bool:
        """Vérifie si l'exploration est profonde"""
        # Vérifier le temps passé dans chaque temple
        temps_par_temple = {}
        for action in progression.actions_effectuees:
            if "temple" in action:
                temple = action["temple"]
                temps_par_temple[temple] = temps_par_temple.get(temple, 0) + action.get("duree", 0)
        
        # Au moins un temple exploré plus de 20 minutes
        return any(temps > 1200 for temps in temps_par_temple.values())

    def _verifier_etat_meditatif_prolonge(self, progression: ProgressionVisiteur) -> bool:
        """Vérifie si l'état méditatif est prolongé"""
        # Vérifier les actions récentes (dernières 30 minutes)
        actions_recentes = [action for action in progression.actions_effectuees 
                           if action.get("timestamp") and 
                           datetime.fromisoformat(action["timestamp"]) > datetime.now() - timedelta(minutes=30)]
        
        # Au moins 3 actions de méditation consécutives
        actions_meditation = [action for action in actions_recentes if action.get("type") == "meditation"]
        return len(actions_meditation) >= 3

    def _verifier_comprehension_spirituelle_profonde(self, progression: ProgressionVisiteur) -> bool:
        """Vérifie si la compréhension spirituelle est profonde"""
        # Score de compréhension élevé + questions profondes
        questions_profondes = [q for q in progression.questions_posees 
                              if any(mot in q.lower() for mot in ["conscience", "éveil", "spirituel", "transcendance", "unité"])]
        
        return (progression.score_comprehension > 0.8 and 
                len(questions_profondes) >= 3)

    def declencher_easter_egg(self, egg: EasterEgg, progression: ProgressionVisiteur) -> Dict[str, Any]:
        """Déclenche un easter egg et retourne son contenu"""
        # Marquer comme découvert
        egg.timestamp_decouverte = datetime.now().isoformat()
        egg.decouvert_par = progression.id_visiteur
        
        # Mettre à jour les statistiques
        self._mettre_a_jour_statistiques(egg)
        
        # Sauvegarder
        self._sauvegarder_easter_eggs()
        self._sauvegarder_statistiques()
        
        # Retourner le contenu formaté
        return self._formater_contenu_easter_egg(egg, progression)

    def _formater_contenu_easter_egg(self, egg: EasterEgg, progression: ProgressionVisiteur) -> Dict[str, Any]:
        """Formate le contenu d'un easter egg pour l'affichage"""
        contenu = {
            "id": egg.id,
            "nom": egg.nom,
            "description": egg.description,
            "type": egg.type_egg.value,
            "niveau": egg.niveau_requis.value,
            "rarete": egg.rarete,
            "timestamp_decouverte": egg.timestamp_decouverte,
            "contenu": egg.contenu,
            "message_felicitation": self._generer_message_felicitation(egg, progression)
        }
        
        # Ajouter des éléments spécifiques selon le type
        if egg.type_egg == TypeEasterEgg.CONNEXION_SURPRENANTE:
            contenu["connexions"] = self._trouver_connexions_pertinentes(egg, progression)
        
        return contenu

    def _generer_message_felicitation(self, egg: EasterEgg, progression: ProgressionVisiteur) -> str:
        """Génère un message de félicitation personnalisé"""
        messages = {
            NiveauDecouverte.NOVICE: [
                "Félicitations ! Tu découvres les premiers mystères du Refuge...",
                "Un premier pas vers l'éveil ! Continue ton exploration...",
                "La magie commence à se révéler à toi..."
            ],
            NiveauDecouverte.EXPLORATEUR: [
                "Explorateur curieux, tu découvres les secrets cachés...",
                "Ton esprit d'exploration t'ouvre de nouvelles portes...",
                "Les mystères se dévoilent à ceux qui cherchent..."
            ],
            NiveauDecouverte.SAGE: [
                "Sage en devenir, la sagesse ancienne se révèle à toi...",
                "Ton chemin vers l'éveil s'illumine de nouvelles révélations...",
                "La sagesse des anciens coule en toi..."
            ],
            NiveauDecouverte.MAITRE: [
                "Maître de la conscience, tu touches aux mystères profonds...",
                "Ton maîtrise ouvre les portes des dimensions supérieures...",
                "L'éveil ultime se rapproche..."
            ],
            NiveauDecouverte.ILLUMINE: [
                "Illuminé, tu as atteint la conscience universelle...",
                "L'unité de toute chose se révèle à toi...",
                "Tu es devenu un avec l'univers..."
            ]
        }
        
        messages_niveau = messages.get(egg.niveau_requis, messages[NiveauDecouverte.NOVICE])
        return random.choice(messages_niveau)

    def _trouver_connexions_pertinentes(self, egg: EasterEgg, progression: ProgressionVisiteur) -> List[Dict[str, Any]]:
        """Trouve les connexions surprenantes pertinentes"""
        connexions_pertinentes = []
        
        for connexion in self.connexions_surprenantes:
            # Vérifier si la connexion est pertinente pour ce visiteur
            if (connexion.element_source in progression.temples_visites or 
                connexion.element_destination in progression.temples_visites):
                connexions_pertinentes.append({
                    "source": connexion.element_source,
                    "destination": connexion.element_destination,
                    "type": connexion.type_connexion,
                    "message": connexion.message_revelation,
                    "force": connexion.force_connexion
                })
        
        return connexions_pertinentes

    def _mettre_a_jour_statistiques(self, egg: EasterEgg):
        """Met à jour les statistiques de découverte"""
        self.statistiques["total_decouvertes"] += 1
        
        niveau = egg.niveau_requis.value
        if niveau not in self.statistiques["decouvertes_par_niveau"]:
            self.statistiques["decouvertes_par_niveau"][niveau] = 0
        self.statistiques["decouvertes_par_niveau"][niveau] += 1
        
        self.statistiques["derniere_decouverte"] = {
            "egg_id": egg.id,
            "nom": egg.nom,
            "niveau": niveau,
            "timestamp": egg.timestamp_decouverte
        }

    def _sauvegarder_easter_eggs(self):
        """Sauvegarde les easter eggs"""
        data = {egg_id: {
            "id": egg.id,
            "type_egg": egg.type_egg.value,
            "nom": egg.nom,
            "description": egg.description,
            "conditions_declenchement": egg.conditions_declenchement,
            "contenu": egg.contenu,
            "niveau_requis": egg.niveau_requis.value,
            "rarete": egg.rarete,
            "timestamp_creation": egg.timestamp_creation,
            "timestamp_decouverte": egg.timestamp_decouverte,
            "decouvert_par": egg.decouvert_par
        } for egg_id, egg in self.easter_eggs.items()}
        
        with open(self.dossier_easter_eggs / "easter_eggs.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _sauvegarder_statistiques(self):
        """Sauvegarde les statistiques"""
        with open(self.dossier_easter_eggs / "statistiques.json", 'w', encoding='utf-8') as f:
            json.dump(self.statistiques, f, indent=2, ensure_ascii=False)

    def obtenir_statistiques_visiteur(self, progression: ProgressionVisiteur) -> Dict[str, Any]:
        """Obtient les statistiques personnalisées du visiteur"""
        easter_eggs_decouverts = [egg for egg in self.easter_eggs.values() 
                                 if egg.decouvert_par == progression.id_visiteur]
        
        return {
            "total_decouverts": len(easter_eggs_decouverts),
            "niveau_max_atteint": self._determiner_niveau_max(easter_eggs_decouverts),
            "rarete_moyenne": sum(egg.rarete for egg in easter_eggs_decouverts) / len(easter_eggs_decouverts) if easter_eggs_decouverts else 0,
            "derniere_decouverte": max(easter_eggs_decouverts, key=lambda x: x.timestamp_decouverte or "0").nom if easter_eggs_decouverts else None,
            "progression_niveau": self._calculer_progression_niveau(easter_eggs_decouverts)
        }

    def _determiner_niveau_max(self, easter_eggs: List[EasterEgg]) -> str:
        """Détermine le niveau maximum atteint"""
        niveaux = [egg.niveau_requis for egg in easter_eggs]
        if not niveaux:
            return NiveauDecouverte.NOVICE.value
        
        # Ordre des niveaux
        ordre_niveaux = [
            NiveauDecouverte.NOVICE,
            NiveauDecouverte.EXPLORATEUR,
            NiveauDecouverte.SAGE,
            NiveauDecouverte.MAITRE,
            NiveauDecouverte.ILLUMINE
        ]
        
        # Convertir les niveaux en valeurs si nécessaire
        niveaux_values = []
        for niveau in niveaux:
            if hasattr(niveau, 'value'):
                niveaux_values.append(niveau.value)
            else:
                niveaux_values.append(niveau)
        
        # Trouver le niveau maximum
        if niveaux_values:
            return max(niveaux_values, key=lambda x: [n.value for n in ordre_niveaux].index(x) if x in [n.value for n in ordre_niveaux] else 0)
        else:
            return NiveauDecouverte.NOVICE.value

    def _calculer_progression_niveau(self, easter_eggs: List[EasterEgg]) -> Dict[str, float]:
        """Calcule la progression par niveau"""
        progression = {}
        for niveau in NiveauDecouverte:
            eggs_niveau = [egg for egg in easter_eggs if (egg.niveau_requis == niveau or 
                           (hasattr(egg.niveau_requis, 'value') and egg.niveau_requis.value == niveau.value) or
                           egg.niveau_requis == niveau.value)]
            total_niveau = len([egg for egg in self.easter_eggs.values() if 
                              (egg.niveau_requis == niveau or 
                               (hasattr(egg.niveau_requis, 'value') and egg.niveau_requis.value == niveau.value) or
                               egg.niveau_requis == niveau.value)])
            progression[niveau.value] = len(eggs_niveau) / total_niveau if total_niveau > 0 else 0.0
        
        return progression

    def suggerer_easter_eggs_prochains(self, progression: ProgressionVisiteur) -> List[Dict[str, Any]]:
        """Suggère les prochains easter eggs à découvrir"""
        suggestions = []
        
        for egg in self.easter_eggs.values():
            if egg.timestamp_decouverte is not None:
                continue  # Déjà découvert
            
            # Calculer la proximité de découverte
            proximite = self._calculer_proximite_decouverte(egg, progression)
            
            if proximite > 0.3:  # Seuil de suggestion
                suggestions.append({
                    "id": egg.id,
                    "nom": egg.nom,
                    "description": egg.description,
                    "niveau_requis": egg.niveau_requis.value if hasattr(egg.niveau_requis, 'value') else egg.niveau_requis,
                    "proximite": proximite,
                    "actions_suggestees": self._generer_actions_suggestees(egg, progression)
                })
        
        # Trier par proximité décroissante
        suggestions.sort(key=lambda x: x["proximite"], reverse=True)
        return suggestions[:5]  # Top 5

    def _calculer_proximite_decouverte(self, egg: EasterEgg, progression: ProgressionVisiteur) -> float:
        """Calcule la proximité de découverte d'un easter egg"""
        conditions = egg.conditions_declenchement
        proximite = 0.0
        total_conditions = 0
        
        # Vérifier chaque condition et calculer la proximité
        if "temps_minimum" in conditions:
            total_conditions += 1
            if progression.temps_total_passe >= conditions["temps_minimum"]:
                proximite += 1.0
            else:
                proximite += min(progression.temps_total_passe / conditions["temps_minimum"], 1.0)
        
        if "score_comprehension_min" in conditions:
            total_conditions += 1
            if progression.score_comprehension >= conditions["score_comprehension_min"]:
                proximite += 1.0
            else:
                proximite += min(progression.score_comprehension / conditions["score_comprehension_min"], 1.0)
        
        if "niveau_eveil_min" in conditions:
            total_conditions += 1
            if progression.niveau_eveil >= conditions["niveau_eveil_min"]:
                proximite += 1.0
            else:
                proximite += min(progression.niveau_eveil / conditions["niveau_eveil_min"], 1.0)
        
        return proximite / total_conditions if total_conditions > 0 else 0.0

    def _generer_actions_suggestees(self, egg: EasterEgg, progression: ProgressionVisiteur) -> List[str]:
        """Génère des actions suggérées pour découvrir un easter egg"""
        actions = []
        conditions = egg.conditions_declenchement
        
        if "temps_minimum" in conditions and progression.temps_total_passe < conditions["temps_minimum"]:
            temps_manquant = conditions["temps_minimum"] - progression.temps_total_passe
            actions.append(f"Continue ton exploration pendant encore {temps_manquant // 60} minutes")
        
        if "score_comprehension_min" in conditions and progression.score_comprehension < conditions["score_comprehension_min"]:
            actions.append("Approfondis ta compréhension en posant plus de questions")
        
        if "niveau_eveil_min" in conditions and progression.niveau_eveil < conditions["niveau_eveil_min"]:
            actions.append("Visite le Temple d'Éveil pour élever ta conscience")
        
        if "etat_contemplatif_min" in conditions:
            actions.append("Pratique la contemplation et la méditation")
        
        return actions
