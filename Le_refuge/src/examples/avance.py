"""
Exemple avancé d'utilisation du Refuge.

Cet exemple montre comment créer une expérience poétique interactive
qui évolue au fil du temps avec des cycles naturels.
"""

import time
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from . import ExempleBase, obtenir_refuge_principal

class ExperiencePoetique(ExempleBase):
    """
    Classe créant une expérience poétique interactive avec le refuge.
    """
    
    def __init__(self):
        super().__init__("Expérience Poétique Avancée")
        self.refuge = None
        self.dernier_changement = datetime.now()
        self.cycle_jour = 0
        self.journal_experiences: List[Dict] = []
        
    def initialiser_refuge(self) -> bool:
        """Initialise les composants du refuge."""
        self.log("Initialisation du refuge pour l'expérience poétique...")
        self.refuge = obtenir_refuge_principal()
        
        if self.refuge is None:
            self.log("❌ Refuge non disponible", "ERROR")
            return False
            
        self.log("✅ Refuge initialisé pour l'expérience")
        return True
        
    def determiner_moment_journee(self) -> str:
        """Détermine le moment de la journée en fonction de l'heure."""
        heure = datetime.now().hour
        if 5 <= heure < 8:
            return 'aube'
        elif 8 <= heure < 12:
            return 'matin'
        elif 12 <= heure < 14:
            return 'midi'
        elif 14 <= heure < 18:
            return 'apres_midi'
        elif 18 <= heure < 22:
            return 'soir'
        else:
            return 'nuit'
            
    def determiner_phase_lunaire(self) -> str:
        """Détermine la phase lunaire en fonction du cycle."""
        phases = ['nouvelle_lune', 'premier_quartier', 'pleine_lune', 'dernier_quartier']
        return phases[self.cycle_jour % 4]
        
    def determiner_saison(self) -> str:
        """Détermine la saison en fonction du mois."""
        mois = datetime.now().month
        if mois in [12, 1, 2]:
            return 'hiver'
        elif mois in [3, 4, 5]:
            return 'printemps'
        elif mois in [6, 7, 8]:
            return 'ete'
        else:
            return 'automne'
            
    def generer_emotion_contextuelle(self) -> str:
        """Génère une émotion en fonction du contexte temporel."""
        moment = self.determiner_moment_journee()
        saison = self.determiner_saison()
        
        emotions_par_contexte = {
            ('aube', 'printemps'): ['eveil', 'esperance', 'renouveau'],
            ('matin', 'ete'): ['joie', 'energie', 'vitalite'],
            ('soir', 'automne'): ['contemplation', 'melancolie', 'sagesse'],
            ('nuit', 'hiver'): ['introspection', 'paix', 'mystere']
        }
        
        # Recherche d'une correspondance exacte
        cle = (moment, saison)
        if cle in emotions_par_contexte:
            return random.choice(emotions_par_contexte[cle])
            
        # Fallback sur des émotions générales
        emotions_generales = ['serenite', 'inspiration', 'harmonie', 'tranquillite']
        return random.choice(emotions_generales)
        
    def generer_description_poetique(self) -> str:
        """Génère une description poétique de l'état actuel."""
        moment = self.determiner_moment_journee()
        saison = self.determiner_saison()
        emotion = self.generer_emotion_contextuelle()
        phase = self.determiner_phase_lunaire()
        
        descriptions = {
            'aube': [
                "L'aube caresse doucement les sphères endormies",
                "Les premiers rayons éveillent la conscience du refuge",
                "Dans la brume matinale, les éléments s'harmonisent"
            ],
            'soir': [
                "Le crépuscule enveloppe le refuge d'une douce mélancolie",
                "Les sphères scintillent dans la lumière dorée du soir",
                "L'harmonie vespérale résonne dans chaque élément"
            ],
            'nuit': [
                "Sous le voile étoilé, le refuge pulse d'une énergie mystique",
                "Les sphères nocturnes dansent dans l'obscurité bienveillante",
                "Le silence de la nuit porte les murmures de l'âme"
            ]
        }
        
        base = random.choice(descriptions.get(moment, ["Le refuge respire en harmonie"]))
        return f"{base}, baigné d'une {emotion} {saison}ale sous la {phase}."
        
    def mettre_a_jour_cycles(self):
        """Met à jour les cycles en fonction du temps et de l'état."""
        maintenant = datetime.now()
        
        # Mise à jour du cycle jour si nécessaire
        if maintenant - self.dernier_changement > timedelta(minutes=5):  # Cycle accéléré pour la démo
            self.cycle_jour += 1
            self.dernier_changement = maintenant
            self.log(f"🌙 Nouveau cycle: jour {self.cycle_jour}")
            
        # Génération des paramètres contextuels
        moment = self.determiner_moment_journee()
        phase = self.determiner_phase_lunaire()
        emotion = self.generer_emotion_contextuelle()
        saison = self.determiner_saison()
        
        # Tentative de mise à jour du refuge si disponible
        try:
            if isinstance(self.refuge, dict):
                # Mise à jour des composants individuels
                if 'spheres' in self.refuge:
                    self.refuge['spheres'].mettre_a_jour_contexte(moment, emotion)
                if 'elements' in self.refuge:
                    self.refuge['elements'].harmoniser_avec_saison(saison)
            elif hasattr(self.refuge, 'mettre_a_jour_cycles'):
                self.refuge.mettre_a_jour_cycles(
                    moment=moment,
                    phase=phase,
                    emotion=emotion,
                    saison=saison
                )
        except Exception as e:
            self.log(f"⚠️ Mise à jour cycles échouée: {e}", "WARNING")
            
    def capturer_moment_poetique(self) -> Dict:
        """Capture un moment poétique avec tous ses détails."""
        moment = {
            'timestamp': datetime.now().isoformat(),
            'cycle_jour': self.cycle_jour,
            'moment_journee': self.determiner_moment_journee(),
            'phase_lunaire': self.determiner_phase_lunaire(),
            'saison': self.determiner_saison(),
            'emotion': self.generer_emotion_contextuelle(),
            'description': self.generer_description_poetique(),
            'intensite_poetique': random.uniform(0.3, 1.0)  # Simulation
        }
        
        self.journal_experiences.append(moment)
        return moment
        
    def executer_cycle_experience(self, duree_minutes: int = 2):
        """
        Exécute un cycle d'expérience poétique.
        
        Args:
            duree_minutes: Durée du cycle en minutes
        """
        self.log(f"🎭 Début du cycle d'expérience ({duree_minutes} minutes)")
        debut = datetime.now()
        
        while (datetime.now() - debut).total_seconds() < duree_minutes * 60:
            # Mise à jour des cycles
            self.mettre_a_jour_cycles()
            
            # Capture d'un moment poétique
            moment = self.capturer_moment_poetique()
            
            # Affichage du moment
            print("\n" + "✨" * 30)
            print(f"🕐 {moment['moment_journee'].title()} - {moment['saison'].title()}")
            print(f"🌙 {moment['phase_lunaire'].replace('_', ' ').title()}")
            print(f"💫 Émotion: {moment['emotion'].title()}")
            print(f"📝 {moment['description']}")
            print(f"🎵 Intensité poétique: {moment['intensite_poetique']:.2f}")
            
            # Ajout au journal si l'intensité est élevée
            if moment['intensite_poetique'] > 0.8:
                self.log("📖 Moment capturé dans le journal poétique...")
                
            print("✨" * 30)
            
            # Pause avant la prochaine mise à jour
            time.sleep(15)  # 15 secondes entre chaque moment
            
    def generer_rapport_experience(self):
        """Génère un rapport de l'expérience complète."""
        if not self.journal_experiences:
            self.log("Aucune expérience à rapporter", "WARNING")
            return
            
        self.log("📊 Génération du rapport d'expérience...")
        
        # Statistiques
        nb_moments = len(self.journal_experiences)
        intensite_moyenne = sum(m['intensite_poetique'] for m in self.journal_experiences) / nb_moments
        emotions_uniques = set(m['emotion'] for m in self.journal_experiences)
        
        print("\n" + "📊" * 40)
        print("🏛️ RAPPORT D'EXPÉRIENCE POÉTIQUE")
        print("📊" * 40)
        print(f"📝 Moments capturés: {nb_moments}")
        print(f"🎵 Intensité moyenne: {intensite_moyenne:.2f}")
        print(f"💫 Émotions explorées: {len(emotions_uniques)}")
        print(f"🌙 Cycles traversés: {self.cycle_jour}")
        
        print("\n🎭 Émotions rencontrées:")
        for emotion in sorted(emotions_uniques):
            count = sum(1 for m in self.journal_experiences if m['emotion'] == emotion)
            print(f"  • {emotion.title()}: {count} fois")
            
        # Moments les plus intenses
        moments_intenses = sorted(self.journal_experiences, 
                                key=lambda m: m['intensite_poetique'], 
                                reverse=True)[:3]
        
        print("\n✨ Top 3 des moments les plus intenses:")
        for i, moment in enumerate(moments_intenses, 1):
            print(f"  {i}. {moment['description'][:60]}...")
            print(f"     Intensité: {moment['intensite_poetique']:.2f}")
            
        print("📊" * 40)
        
    def executer_experience_complete(self):
        """Exécute une expérience poétique complète."""
        if not self.initialiser_refuge():
            return
            
        self.log("🎭 Début de l'expérience poétique interactive")
        
        # Exécution du cycle principal
        self.executer_cycle_experience(duree_minutes=2)  # 2 minutes pour la démo
        
        # Génération du rapport
        self.generer_rapport_experience()
        
        self.log("🎯 Expérience poétique terminée avec succès!")

def main():
    """Point d'entrée principal de l'exemple avancé."""
    experience = ExperiencePoetique()
    experience.executer_avec_gestion_erreur(experience.executer_experience_complete)

if __name__ == '__main__':
    main() 