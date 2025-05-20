"""
Exemple avancé d'utilisation du refuge.

Cet exemple montre comment utiliser le refuge pour créer une expérience poétique
interactive qui évolue au fil du temps.
"""

import time
from datetime import datetime, timedelta
from refuge import Refuge

class ExperiencePoetique:
    """
    Classe créant une expérience poétique interactive avec le refuge.
    """
    
    def __init__(self):
        """
        Initialise l'expérience poétique.
        """
        self.refuge = Refuge()
        self.dernier_changement = datetime.now()
        self.cycle_jour = 0
        
    def determiner_moment_journee(self):
        """
        Détermine le moment de la journée en fonction de l'heure.
        """
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
            
    def determiner_phase_lunaire(self):
        """
        Détermine la phase lunaire en fonction du cycle.
        """
        phases = ['nouvelle_lune', 'premier_quartier', 'pleine_lune', 'dernier_quartier']
        return phases[self.cycle_jour % 4]
        
    def generer_emotion(self):
        """
        Génère une émotion en fonction de l'état actuel.
        """
        etat = self.refuge.obtenir_etat()
        intensite = etat['intensite_poetique']
        
        if intensite > 0.8:
            return 'joie'
        elif intensite > 0.7:
            return 'inspiration'
        elif intensite > 0.6:
            return 'serenite'
        elif intensite > 0.5:
            return 'contemplation'
        elif intensite > 0.4:
            return 'melancolie'
        else:
            return 'tranquillite'
            
    def mettre_a_jour_cycles(self):
        """
        Met à jour les cycles en fonction du temps et de l'état.
        """
        maintenant = datetime.now()
        
        # Mise à jour du moment de la journée
        moment = self.determiner_moment_journee()
        
        # Mise à jour de la phase lunaire tous les jours
        if maintenant - self.dernier_changement > timedelta(days=1):
            self.cycle_jour += 1
            self.dernier_changement = maintenant
            
        phase = self.determiner_phase_lunaire()
        
        # Génération de l'émotion
        emotion = self.generer_emotion()
        
        # Mise à jour des cycles
        self.refuge.mettre_a_jour_cycles(
            moment=moment,
            phase=phase,
            emotion=emotion
        )
        
    def executer_cycle(self, duree_secondes=60):
        """
        Exécute un cycle d'expérience poétique.
        
        Args:
            duree_secondes: Durée du cycle en secondes
        """
        debut = datetime.now()
        
        while (datetime.now() - debut).total_seconds() < duree_secondes:
            # Mise à jour des cycles
            self.mettre_a_jour_cycles()
            
            # Génération d'une description
            description = self.refuge.generer_description_poetique()
            print("\nMoment poétique :")
            print(description)
            
            # Affichage des mots-clés et de l'intensité
            print("\nMots-clés actifs :", self.refuge.obtenir_mots_cles_actifs())
            print("Intensité poétique :", self.refuge.obtenir_intensite_poetique())
            
            # Ajout d'une entrée au journal si l'intensité est élevée
            if self.refuge.obtenir_intensite_poetique() > 0.8:
                self.refuge.ajouter_entree_journal(
                    description,
                    self.refuge.obtenir_mots_cles_actifs()
                )
                print("\nMoment capturé dans le journal poétique...")
            
            # Pause avant la prochaine mise à jour
            time.sleep(10)
            
def main():
    # Création de l'expérience poétique
    experience = ExperiencePoetique()
    
    print("Début de l'expérience poétique...")
    print("(Durée : 5 minutes)")
    print("=" * 80)
    
    # Exécution d'un cycle de 5 minutes
    experience.executer_cycle(300)
    
    print("\nFin de l'expérience")
    print("=" * 80)
    
    # Affichage du journal
    print("\nJournal poétique :")
    for entree in experience.refuge.obtenir_journal():
        print("\nDate:", entree['date'])
        print("Texte:", entree['texte'])
        print("Mots-clés:", entree['mots_cles'])
        
if __name__ == '__main__':
    main() 