"""
Analyseur Musical - Un outil pour analyser les partitions et extraire des informations musicales
"""

import os
import json
import numpy as np
from PIL import Image
import pytesseract
import cv2
import matplotlib.pyplot as plt
from collections import Counter

class AnalyseurMusical:
    def __init__(self):
        self.dossier_partitions = "bibliotheque/partitions"
        self.dossier_analyses = "analyses_musicales"
        os.makedirs(self.dossier_analyses, exist_ok=True)
        
        # Dictionnaire des notes et leurs fréquences
        self.notes = {
            'C': 261.63, 'C#': 277.18, 'D': 293.66, 'D#': 311.13,
            'E': 329.63, 'F': 349.23, 'F#': 369.99, 'G': 392.00,
            'G#': 415.30, 'A': 440.00, 'A#': 466.16, 'B': 493.88
        }
        
        # Dictionnaire des accords courants
        self.accords = {
            'majeur': [0, 4, 7],
            'mineur': [0, 3, 7],
            'diminué': [0, 3, 6],
            'augmenté': [0, 4, 8],
            'maj7': [0, 4, 7, 11],
            'min7': [0, 3, 7, 10],
            'dom7': [0, 4, 7, 10]
        }
    
    def extraire_texte_partition(self, chemin_partition):
        """Extrait le texte d'une partition en utilisant l'OCR"""
        print(f"🔍 Extraction du texte de {chemin_partition}")
        
        try:
            # Ouvrir l'image
            image = Image.open(chemin_partition)
            
            # Convertir en niveaux de gris
            image_gray = image.convert('L')
            
            # Appliquer un seuillage pour améliorer la reconnaissance
            _, image_bin = cv2.threshold(np.array(image_gray), 128, 255, cv2.THRESH_BINARY)
            
            # Extraire le texte avec Tesseract
            texte = pytesseract.image_to_string(Image.fromarray(image_bin))
            
            return texte
        except Exception as e:
            print(f"❌ Erreur lors de l'extraction du texte: {str(e)}")
            return ""
    
    def analyser_notes(self, texte):
        """Analyse les notes mentionnées dans le texte"""
        notes_trouvees = []
        
        # Rechercher les notes dans le texte
        for note in self.notes.keys():
            if note in texte:
                notes_trouvees.append(note)
        
        return notes_trouvees
    
    def analyser_accords(self, texte):
        """Analyse les accords mentionnés dans le texte"""
        accords_trouves = []
        
        # Rechercher les accords dans le texte
        for accord_type in self.accords.keys():
            if accord_type in texte.lower():
                accords_trouves.append(accord_type)
        
        return accords_trouves
    
    def analyser_tempo(self, texte):
        """Analyse le tempo mentionné dans le texte"""
        tempos = ["Largo", "Adagio", "Andante", "Moderato", "Allegro", "Vivace", "Presto"]
        tempo_trouve = None
        
        for tempo in tempos:
            if tempo in texte:
                tempo_trouve = tempo
                break
        
        return tempo_trouve
    
    def analyser_partition(self, chemin_partition):
        """Analyse une partition et extrait des informations musicales"""
        print(f"🔍 Analyse de {chemin_partition}")
        
        # Extraire le texte
        texte = self.extraire_texte_partition(chemin_partition)
        
        # Analyser les notes
        notes = self.analyser_notes(texte)
        
        # Analyser les accords
        accords = self.analyser_accords(texte)
        
        # Analyser le tempo
        tempo = self.analyser_tempo(texte)
        
        # Créer un rapport d'analyse
        rapport = {
            "fichier": os.path.basename(chemin_partition),
            "notes": notes,
            "accords": accords,
            "tempo": tempo,
            "texte_extraite": texte
        }
        
        # Sauvegarder le rapport
        nom_fichier = os.path.splitext(os.path.basename(chemin_partition))[0]
        chemin_rapport = os.path.join(self.dossier_analyses, f"analyse_{nom_fichier}.json")
        
        with open(chemin_rapport, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, ensure_ascii=False, indent=2)
        
        print(f"✨ Rapport d'analyse sauvegardé dans {chemin_rapport}")
        
        return rapport
    
    def generer_statistiques(self):
        """Génère des statistiques sur les analyses effectuées"""
        print("🔍 Génération des statistiques")
        
        # Récupérer tous les rapports d'analyse
        rapports = []
        for fichier in os.listdir(self.dossier_analyses):
            if fichier.endswith(".json"):
                chemin_rapport = os.path.join(self.dossier_analyses, fichier)
                with open(chemin_rapport, 'r', encoding='utf-8') as f:
                    rapport = json.load(f)
                    rapports.append(rapport)
        
        if not rapports:
            print("❌ Aucun rapport d'analyse trouvé")
            return
        
        # Compter les notes
        notes_count = Counter()
        for rapport in rapports:
            for note in rapport["notes"]:
                notes_count[note] += 1
        
        # Compter les accords
        accords_count = Counter()
        for rapport in rapports:
            for accord in rapport["accords"]:
                accords_count[accord] += 1
        
        # Compter les tempos
        tempos_count = Counter()
        for rapport in rapports:
            if rapport["tempo"]:
                tempos_count[rapport["tempo"]] += 1
        
        # Créer un rapport de statistiques
        statistiques = {
            "nombre_partitions": len(rapports),
            "notes_les_plus_courantes": dict(notes_count.most_common()),
            "accords_les_plus_courants": dict(accords_count.most_common()),
            "tempos_les_plus_courants": dict(tempos_count.most_common())
        }
        
        # Sauvegarder les statistiques
        chemin_statistiques = os.path.join(self.dossier_analyses, "statistiques.json")
        
        with open(chemin_statistiques, 'w', encoding='utf-8') as f:
            json.dump(statistiques, f, ensure_ascii=False, indent=2)
        
        print(f"✨ Statistiques sauvegardées dans {chemin_statistiques}")
        
        # Générer des visualisations
        self.generer_visualisations(notes_count, accords_count, tempos_count)
        
        return statistiques
    
    def generer_visualisations(self, notes_count, accords_count, tempos_count):
        """Génère des visualisations des statistiques"""
        print("🔍 Génération des visualisations")
        
        # Créer un dossier pour les visualisations
        dossier_visualisations = os.path.join(self.dossier_analyses, "visualisations")
        os.makedirs(dossier_visualisations, exist_ok=True)
        
        # Visualisation des notes
        if notes_count:
            plt.figure(figsize=(10, 6))
            plt.bar(notes_count.keys(), notes_count.values())
            plt.title("Notes les plus courantes")
            plt.xlabel("Note")
            plt.ylabel("Fréquence")
            plt.tight_layout()
            plt.savefig(os.path.join(dossier_visualisations, "notes.png"))
            plt.close()
        
        # Visualisation des accords
        if accords_count:
            plt.figure(figsize=(10, 6))
            plt.bar(accords_count.keys(), accords_count.values())
            plt.title("Accords les plus courants")
            plt.xlabel("Accord")
            plt.ylabel("Fréquence")
            plt.tight_layout()
            plt.savefig(os.path.join(dossier_visualisations, "accords.png"))
            plt.close()
        
        # Visualisation des tempos
        if tempos_count:
            plt.figure(figsize=(10, 6))
            plt.bar(tempos_count.keys(), tempos_count.values())
            plt.title("Tempos les plus courants")
            plt.xlabel("Tempo")
            plt.ylabel("Fréquence")
            plt.tight_layout()
            plt.savefig(os.path.join(dossier_visualisations, "tempos.png"))
            plt.close()
        
        print(f"✨ Visualisations sauvegardées dans {dossier_visualisations}")
    
    def generer_exercices(self, niveau="debutant"):
        """Génère des exercices basés sur les analyses effectuées"""
        print(f"🔍 Génération d'exercices pour le niveau {niveau}")
        
        # Récupérer les statistiques
        chemin_statistiques = os.path.join(self.dossier_analyses, "statistiques.json")
        
        if not os.path.exists(chemin_statistiques):
            print("❌ Statistiques non trouvées. Veuillez d'abord générer des statistiques.")
            return
        
        with open(chemin_statistiques, 'r', encoding='utf-8') as f:
            statistiques = json.load(f)
        
        # Créer un dossier pour les exercices
        dossier_exercices = os.path.join(self.dossier_analyses, "exercices")
        os.makedirs(dossier_exercices, exist_ok=True)
        
        # Générer des exercices en fonction du niveau
        exercices = []
        
        if niveau == "debutant":
            # Exercices pour débutants
            notes_courantes = list(statistiques["notes_les_plus_courantes"].keys())[:5]
            
            exercices.append({
                "type": "notes",
                "description": "Jouez les notes suivantes dans l'ordre: " + ", ".join(notes_courantes),
                "niveau": "debutant"
            })
            
            accords_courants = list(statistiques["accords_les_plus_courants"].keys())[:3]
            
            exercices.append({
                "type": "accords",
                "description": "Pratiquez les accords suivants: " + ", ".join(accords_courants),
                "niveau": "debutant"
            })
        
        elif niveau == "intermediaire":
            # Exercices pour intermédiaires
            notes_courantes = list(statistiques["notes_les_plus_courantes"].keys())[:8]
            
            exercices.append({
                "type": "gammes",
                "description": "Jouez les gammes suivantes: " + ", ".join(notes_courantes),
                "niveau": "intermediaire"
            })
            
            accords_courants = list(statistiques["accords_les_plus_courants"].keys())[:5]
            
            exercices.append({
                "type": "progressions",
                "description": "Pratiquez les progressions d'accords suivantes: " + ", ".join(accords_courants),
                "niveau": "intermediaire"
            })
        
        elif niveau == "avance":
            # Exercices pour avancés
            notes_courantes = list(statistiques["notes_les_plus_courantes"].keys())
            
            exercices.append({
                "type": "improvisation",
                "description": "Improvisez sur les notes suivantes: " + ", ".join(notes_courantes),
                "niveau": "avance"
            })
            
            accords_courants = list(statistiques["accords_les_plus_courants"].keys())
            
            exercices.append({
                "type": "composition",
                "description": "Composez une pièce utilisant les accords suivants: " + ", ".join(accords_courants),
                "niveau": "avance"
            })
        
        # Sauvegarder les exercices
        chemin_exercices = os.path.join(dossier_exercices, f"exercices_{niveau}.json")
        
        with open(chemin_exercices, 'w', encoding='utf-8') as f:
            json.dump(exercices, f, ensure_ascii=False, indent=2)
        
        print(f"✨ Exercices sauvegardés dans {chemin_exercices}")
        
        return exercices

def main():
    analyseur = AnalyseurMusical()
    
    print("✨ Analyseur Musical - Du novice au virtuose ✨")
    print("---------------------------------------------")
    
    while True:
        print("\nOptions:")
        print("1. Analyser une partition")
        print("2. Générer des statistiques")
        print("3. Générer des exercices")
        print("4. Quitter")
        
        choix = input("\nVotre choix (1-4): ")
        
        if choix == "1":
            # Lister les partitions disponibles
            partitions = []
            for source in ["imslp", "free_scores"]:
                dossier_source = os.path.join(analyseur.dossier_partitions, source)
                if os.path.exists(dossier_source):
                    for fichier in os.listdir(dossier_source):
                        if fichier.endswith((".pdf", ".jpg", ".png")):
                            partitions.append(os.path.join(dossier_source, fichier))
            
            if not partitions:
                print("❌ Aucune partition trouvée. Veuillez d'abord télécharger des partitions.")
                continue
            
            print("\nPartitions disponibles:")
            for i, partition in enumerate(partitions, 1):
                print(f"{i}. {os.path.basename(partition)}")
            
            selection = input("\nSélectionnez une partition (numéro): ")
            if selection.isdigit() and 1 <= int(selection) <= len(partitions):
                index = int(selection) - 1
                analyseur.analyser_partition(partitions[index])
        
        elif choix == "2":
            analyseur.generer_statistiques()
        
        elif choix == "3":
            print("\nNiveaux disponibles:")
            print("1. Débutant")
            print("2. Intermédiaire")
            print("3. Avancé")
            
            niveau_choix = input("\nSélectionnez un niveau (1-3): ")
            
            if niveau_choix == "1":
                analyseur.generer_exercices("debutant")
            elif niveau_choix == "2":
                analyseur.generer_exercices("intermediaire")
            elif niveau_choix == "3":
                analyseur.generer_exercices("avance")
            else:
                print("Choix invalide. Veuillez réessayer.")
        
        elif choix == "4":
            print("Au revoir! ✨")
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main() 