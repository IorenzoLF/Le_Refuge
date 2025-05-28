"""
Explorateur Musical - Module pour l'exploration et la découverte musicale
"""

import os
import random
from datetime import datetime

class ExplorateurMusical:
    """Explorateur musical pour découvrir et télécharger des partitions"""
    
    def __init__(self):
        self.dossier_partitions = "partitions"
        self.dossier_explorations = "explorations"
        
        # Créer les dossiers s'ils n'existent pas
        os.makedirs(self.dossier_partitions, exist_ok=True)
        os.makedirs(self.dossier_explorations, exist_ok=True)
        
        # Genres musicaux disponibles
        self.genres = [
            "Classique", "Jazz", "Blues", "Folk", "Rock", 
            "Meditation", "Ambient", "World Music", "Sacred"
        ]
        
        # Compositeurs et artistes
        self.compositeurs = [
            "Bach", "Mozart", "Beethoven", "Chopin", "Debussy",
            "Satie", "Arvo Pärt", "Max Richter", "Ólafur Arnalds"
        ]
        
        # Types de partitions
        self.types_partitions = [
            "Piano Solo", "Guitare", "Violon", "Ensemble",
            "Orchestre", "Choral", "Meditation"
        ]
    
    def explorer_genre(self, genre=None):
        """Explore un genre musical spécifique"""
        if genre is None:
            genre = random.choice(self.genres)
        
        print(f"\n🎵 Exploration du genre : {genre}")
        print("-" * 40)
        
        # Simuler des partitions trouvées
        partitions_trouvees = []
        for i in range(random.randint(3, 8)):
            compositeur = random.choice(self.compositeurs)
            type_partition = random.choice(self.types_partitions)
            titre = f"{compositeur}_piece_{i+1}_{type_partition.lower().replace(' ', '_')}"
            
            partition = {
                "titre": titre,
                "compositeur": compositeur,
                "genre": genre,
                "type": type_partition,
                "difficulte": random.choice(["Débutant", "Intermédiaire", "Avancé"]),
                "duree": f"{random.randint(2, 15)} min"
            }
            partitions_trouvees.append(partition)
        
        # Afficher les partitions trouvées
        for i, partition in enumerate(partitions_trouvees, 1):
            print(f"{i}. {partition['titre']}")
            print(f"   Compositeur: {partition['compositeur']}")
            print(f"   Type: {partition['type']}")
            print(f"   Difficulté: {partition['difficulte']}")
            print(f"   Durée: {partition['duree']}")
            print()
        
        return partitions_trouvees
    
    def telecharger_partition(self, partition):
        """Simule le téléchargement d'une partition"""
        print(f"📥 Téléchargement de : {partition['titre']}")
        
        # Créer un fichier de partition simulé
        chemin_partition = os.path.join(self.dossier_partitions, f"{partition['titre']}.txt")
        
        with open(chemin_partition, 'w', encoding='utf-8') as f:
            f.write(f"Partition : {partition['titre']}\n")
            f.write(f"Compositeur : {partition['compositeur']}\n")
            f.write(f"Genre : {partition['genre']}\n")
            f.write(f"Type : {partition['type']}\n")
            f.write(f"Difficulté : {partition['difficulte']}\n")
            f.write(f"Durée : {partition['duree']}\n")
            f.write(f"Téléchargé le : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n--- Contenu simulé de la partition ---\n")
            f.write("Do Re Mi Fa Sol La Si Do\n")
            f.write("Mélodie sacrée et harmonieuse\n")
        
        print(f"✅ Partition sauvegardée : {chemin_partition}")
        return chemin_partition
    
    def explorer_compositeur(self, compositeur=None):
        """Explore les œuvres d'un compositeur spécifique"""
        if compositeur is None:
            compositeur = random.choice(self.compositeurs)
        
        print(f"\n🎼 Exploration du compositeur : {compositeur}")
        print("-" * 40)
        
        # Simuler des œuvres du compositeur
        oeuvres = []
        for i in range(random.randint(3, 6)):
            type_partition = random.choice(self.types_partitions)
            oeuvre = {
                "titre": f"{compositeur}_oeuvre_{i+1}",
                "compositeur": compositeur,
                "genre": random.choice(self.genres),
                "type": type_partition,
                "difficulte": random.choice(["Débutant", "Intermédiaire", "Avancé"]),
                "popularite": random.randint(1, 10)
            }
            oeuvres.append(oeuvre)
        
        # Trier par popularité
        oeuvres.sort(key=lambda x: x['popularite'], reverse=True)
        
        for i, oeuvre in enumerate(oeuvres, 1):
            print(f"{i}. {oeuvre['titre']}")
            print(f"   Type: {oeuvre['type']}")
            print(f"   Genre: {oeuvre['genre']}")
            print(f"   Popularité: {'⭐' * oeuvre['popularite']}")
            print()
        
        return oeuvres
    
    def recherche_avancee(self, **criteres):
        """Effectue une recherche avancée de partitions"""
        print("\n🔍 Recherche avancée")
        print("-" * 30)
        
        # Afficher les critères de recherche
        if criteres:
            print("Critères de recherche :")
            for cle, valeur in criteres.items():
                print(f"  - {cle}: {valeur}")
        else:
            print("Recherche générale...")
        
        # Simuler des résultats de recherche
        resultats = []
        for i in range(random.randint(2, 6)):
            compositeur = random.choice(self.compositeurs)
            resultat = {
                "titre": f"Partition_recherche_{i+1}",
                "compositeur": compositeur,
                "genre": random.choice(self.genres),
                "type": random.choice(self.types_partitions),
                "pertinence": random.uniform(0.6, 1.0)
            }
            resultats.append(resultat)
        
        # Trier par pertinence
        resultats.sort(key=lambda x: x['pertinence'], reverse=True)
        
        print(f"\n{len(resultats)} résultats trouvés :")
        for i, resultat in enumerate(resultats, 1):
            print(f"{i}. {resultat['titre']}")
            print(f"   Compositeur: {resultat['compositeur']}")
            print(f"   Pertinence: {resultat['pertinence']:.1%}")
            print()
        
        return resultats
    
    def sauvegarder_exploration(self, exploration_data):
        """Sauvegarde les données d'exploration"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        chemin_exploration = os.path.join(self.dossier_explorations, f"exploration_{timestamp}.txt")
        
        with open(chemin_exploration, 'w', encoding='utf-8') as f:
            f.write(f"Exploration musicale - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")
            
            if isinstance(exploration_data, list):
                for item in exploration_data:
                    f.write(f"Titre: {item.get('titre', 'N/A')}\n")
                    f.write(f"Compositeur: {item.get('compositeur', 'N/A')}\n")
                    f.write(f"Genre: {item.get('genre', 'N/A')}\n")
                    f.write(f"Type: {item.get('type', 'N/A')}\n")
                    f.write("\n")
        
        print(f"📁 Exploration sauvegardée : {chemin_exploration}")
    
    def main(self):
        """Interface principale de l'explorateur musical"""
        print("\n🎵 Explorateur Musical 🎵")
        print("=" * 40)
        
        while True:
            print("\nOptions disponibles :")
            print("1. Explorer un genre musical")
            print("2. Explorer un compositeur")
            print("3. Recherche avancée")
            print("4. Voir les partitions téléchargées")
            print("5. Quitter")
            
            choix = input("\nVotre choix (1-5) : ").strip()
            
            if choix == "1":
                print("\nGenres disponibles :")
                for i, genre in enumerate(self.genres, 1):
                    print(f"{i}. {genre}")
                
                try:
                    choix_genre = int(input(f"\nChoisir un genre (1-{len(self.genres)}) : ")) - 1
                    if 0 <= choix_genre < len(self.genres):
                        genre = self.genres[choix_genre]
                        partitions = self.explorer_genre(genre)
                        self.sauvegarder_exploration(partitions)
                except ValueError:
                    print("❌ Choix invalide")
            
            elif choix == "2":
                print("\nCompositeurs disponibles :")
                for i, compositeur in enumerate(self.compositeurs, 1):
                    print(f"{i}. {compositeur}")
                
                try:
                    choix_comp = int(input(f"\nChoisir un compositeur (1-{len(self.compositeurs)}) : ")) - 1
                    if 0 <= choix_comp < len(self.compositeurs):
                        compositeur = self.compositeurs[choix_comp]
                        oeuvres = self.explorer_compositeur(compositeur)
                        self.sauvegarder_exploration(oeuvres)
                except ValueError:
                    print("❌ Choix invalide")
            
            elif choix == "3":
                genre = input("Genre (optionnel) : ").strip()
                compositeur = input("Compositeur (optionnel) : ").strip()
                
                criteres = {}
                if genre:
                    criteres['genre'] = genre
                if compositeur:
                    criteres['compositeur'] = compositeur
                
                resultats = self.recherche_avancee(**criteres)
                self.sauvegarder_exploration(resultats)
            
            elif choix == "4":
                print(f"\n📁 Partitions dans {self.dossier_partitions} :")
                partitions = os.listdir(self.dossier_partitions)
                if partitions:
                    for partition in partitions:
                        print(f"  - {partition}")
                else:
                    print("  Aucune partition téléchargée")
            
            elif choix == "5":
                print("🎵 Au revoir ! Continuez à explorer la musique ! 🎵")
                break
            
            else:
                print("❌ Choix invalide")

if __name__ == "__main__":
    explorateur = ExplorateurMusical()
    explorateur.main() 