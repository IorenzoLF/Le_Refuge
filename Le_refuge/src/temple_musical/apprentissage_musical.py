"""
Apprentissage Musical - Un environnement complet pour progresser du novice au virtuose
"""

import os
import sys
import json
import time
from src.core.explorateur_musical import ExplorateurMusical
from src.temple_musical.analyseur_musical import AnalyseurMusical
from src.musique.melodies import MelodiesSacrees

class ApprentissageMusical:
    def __init__(self):
        self.explorateur = ExplorateurMusical()
        self.analyseur = AnalyseurMusical()
        self.melodies = MelodiesSacrees()
        
        # Créer un dossier pour les rapports d'apprentissage
        self.dossier_rapports = "rapports_apprentissage"
        os.makedirs(self.dossier_rapports, exist_ok=True)
        
        # Charger ou créer le profil d'apprentissage
        self.chemin_profil = os.path.join(self.dossier_rapports, "profil_apprentissage.json")
        self.profil = self.charger_profil()
    
    def charger_profil(self):
        """Charge le profil d'apprentissage ou en crée un nouveau"""
        if os.path.exists(self.chemin_profil):
            with open(self.chemin_profil, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Créer un nouveau profil
            profil = {
                "nom": "",
                "niveau": "debutant",
                "date_creation": time.strftime("%Y-%m-%d"),
                "partitions_analysees": 0,
                "melodies_creees": 0,
                "exercices_completes": 0,
                "competences": {
                    "notes": 0,
                    "accords": 0,
                    "tempo": 0,
                    "expression": 0,
                    "composition": 0
                },
                "historique": []
            }
            
            # Sauvegarder le profil
            with open(self.chemin_profil, 'w', encoding='utf-8') as f:
                json.dump(profil, f, ensure_ascii=False, indent=2)
            
            return profil
    
    def sauvegarder_profil(self):
        """Sauvegarde le profil d'apprentissage"""
        with open(self.chemin_profil, 'w', encoding='utf-8') as f:
            json.dump(self.profil, f, ensure_ascii=False, indent=2)
    
    def ajouter_historique(self, action, description):
        """Ajoute une action à l'historique d'apprentissage"""
        entree = {
            "date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "description": description
        }
        
        self.profil["historique"].append(entree)
        self.sauvegarder_profil()
    
    def mettre_a_jour_competences(self, competence, valeur):
        """Met à jour les compétences d'apprentissage"""
        if competence in self.profil["competences"]:
            self.profil["competences"][competence] += valeur
            self.sauvegarder_profil()
    
    def evaluer_niveau(self):
        """Évalue le niveau d'apprentissage actuel"""
        # Calculer le score total
        score_total = sum(self.profil["competences"].values())
        
        # Déterminer le niveau en fonction du score
        if score_total < 10:
            niveau = "debutant"
        elif score_total < 20:
            niveau = "intermediaire"
        else:
            niveau = "avance"
        
        # Mettre à jour le niveau si nécessaire
        if niveau != self.profil["niveau"]:
            ancien_niveau = self.profil["niveau"]
            self.profil["niveau"] = niveau
            self.sauvegarder_profil()
            
            print(f"✨ Félicitations ! Vous êtes passé du niveau {ancien_niveau} au niveau {niveau} ! ✨")
        
        return niveau
    
    def afficher_profil(self):
        """Affiche le profil d'apprentissage"""
        print("\n✨ Profil d'Apprentissage ✨")
        print("---------------------------")
        print(f"Nom: {self.profil['nom']}")
        print(f"Niveau: {self.profil['niveau']}")
        print(f"Date de création: {self.profil['date_creation']}")
        print(f"Partitions analysées: {self.profil['partitions_analysees']}")
        print(f"Mélodies créées: {self.profil['melodies_creees']}")
        print(f"Exercices complétés: {self.profil['exercices_completes']}")
        
        print("\nCompétences:")
        for competence, valeur in self.profil["competences"].items():
            print(f"  - {competence}: {valeur}/5")
        
        print("\nHistorique récent:")
        for entree in self.profil["historique"][-5:]:
            print(f"  - {entree['date']}: {entree['action']} - {entree['description']}")
    
    def configurer_profil(self):
        """Configure le profil d'apprentissage"""
        print("\n✨ Configuration du Profil ✨")
        print("----------------------------")
        
        nom = input("Votre nom: ")
        if nom:
            self.profil["nom"] = nom
            self.sauvegarder_profil()
            self.ajouter_historique("Configuration", f"Nom configuré: {nom}")
    
    def explorer_partitions(self):
        """Explore et télécharge des partitions"""
        print("\n✨ Exploration de Partitions ✨")
        print("-------------------------------")
        
        # Utiliser l'explorateur musical
        self.explorateur.main()
        
        # Mettre à jour le profil
        self.ajouter_historique("Exploration", "Exploration de partitions")
    
    def analyser_partitions(self):
        """Analyse les partitions téléchargées"""
        print("\n✨ Analyse de Partitions ✨")
        print("---------------------------")
        
        # Utiliser l'analyseur musical
        self.analyseur.main()
        
        # Mettre à jour le profil
        self.profil["partitions_analysees"] += 1
        self.mettre_a_jour_competences("notes", 1)
        self.mettre_a_jour_competences("accords", 1)
        self.mettre_a_jour_competences("tempo", 1)
        self.sauvegarder_profil()
        
        self.ajouter_historique("Analyse", "Analyse de partitions")
    
    def generer_melodies(self):
        """Génère des mélodies sacrées"""
        print("\n✨ Génération de Mélodies ✨")
        print("----------------------------")
        
        # Utiliser le générateur de mélodies sacrées
        self.melodies.main()
        
        # Mettre à jour le profil
        self.profil["melodies_creees"] += 1
        self.mettre_a_jour_competences("composition", 1)
        self.sauvegarder_profil()
        
        self.ajouter_historique("Création", "Génération de mélodies sacrées")
    
    def generer_exercices(self):
        """Génère des exercices adaptés au niveau"""
        print("\n✨ Génération d'Exercices ✨")
        print("---------------------------")
        
        # Évaluer le niveau actuel
        niveau = self.evaluer_niveau()
        
        # Générer des exercices adaptés au niveau
        exercices = self.analyseur.generer_exercices(niveau)
        
        # Afficher les exercices
        if exercices:
            print("\nExercices générés:")
            for i, exercice in enumerate(exercices, 1):
                print(f"{i}. {exercice['type']}: {exercice['description']}")
            
            # Mettre à jour le profil
            self.profil["exercices_completes"] += 1
            self.sauvegarder_profil()
            
            self.ajouter_historique("Exercices", f"Génération d'exercices pour le niveau {niveau}")
        else:
            print("❌ Aucun exercice généré. Veuillez d'abord analyser des partitions.")
    
    def afficher_statistiques(self):
        """Affiche des statistiques d'apprentissage"""
        print("\n✨ Statistiques d'Apprentissage ✨")
        print("---------------------------------")
        
        # Évaluer le niveau actuel
        niveau = self.evaluer_niveau()
        
        # Afficher le profil
        self.afficher_profil()
        
        # Afficher des conseils en fonction du niveau
        print("\nConseils pour progresser:")
        if niveau == "debutant":
            print("  - Explorez des partitions simples")
            print("  - Pratiquez les notes de base")
            print("  - Écoutez des mélodies sacrées")
        elif niveau == "intermediaire":
            print("  - Analysez des partitions plus complexes")
            print("  - Pratiquez les accords et les gammes")
            print("  - Créez vos propres mélodies")
        else:
            print("  - Explorez des partitions avancées")
            print("  - Improvisez et composez")
            print("  - Enseignez aux autres")
        
        self.ajouter_historique("Statistiques", "Consultation des statistiques d'apprentissage")

def main():
    apprentissage = ApprentissageMusical()
    
    print("✨ Apprentissage Musical - Du novice au virtuose ✨")
    print("-------------------------------------------------")
    
    # Configurer le profil si nécessaire
    if not apprentissage.profil["nom"]:
        apprentissage.configurer_profil()
    
    while True:
        print("\nOptions:")
        print("1. Explorer des partitions")
        print("2. Analyser des partitions")
        print("3. Générer des mélodies sacrées")
        print("4. Générer des exercices")
        print("5. Afficher le profil")
        print("6. Afficher les statistiques")
        print("7. Configurer le profil")
        print("8. Quitter")
        
        choix = input("\nVotre choix (1-8): ")
        
        if choix == "1":
            apprentissage.explorer_partitions()
        
        elif choix == "2":
            apprentissage.analyser_partitions()
        
        elif choix == "3":
            apprentissage.generer_melodies()
        
        elif choix == "4":
            apprentissage.generer_exercices()
        
        elif choix == "5":
            apprentissage.afficher_profil()
        
        elif choix == "6":
            apprentissage.afficher_statistiques()
        
        elif choix == "7":
            apprentissage.configurer_profil()
        
        elif choix == "8":
            print("Au revoir! ✨")
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main() 