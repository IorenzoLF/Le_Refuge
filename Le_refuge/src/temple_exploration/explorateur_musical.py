"""
Explorateur Musical - Un outil pour explorer et télécharger des partitions
"""

import os
import requests
from bs4 import BeautifulSoup
import json
import time
import random

class ExplorateurMusical:
    def __init__(self):
        self.dossier_partitions = "partitions"
        os.makedirs(self.dossier_partitions, exist_ok=True)
        
        # Créer un sous-dossier pour chaque source
        self.dossier_imslp = os.path.join(self.dossier_partitions, "imslp")
        self.dossier_free_scores = os.path.join(self.dossier_partitions, "free_scores")
        os.makedirs(self.dossier_imslp, exist_ok=True)
        os.makedirs(self.dossier_free_scores, exist_ok=True)
        
        # En-têtes pour les requêtes HTTP
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    
    def rechercher_imslp(self, terme_recherche):
        """Recherche des partitions sur IMSLP"""
        print(f"🔍 Recherche sur IMSLP: {terme_recherche}")
        
        # URL de recherche IMSLP
        url = f"https://imslp.org/index.php?title=Special:Search&search={terme_recherche}&fulltext=1"
        
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extraire les résultats de recherche
                resultats = []
                for resultat in soup.select('.mw-search-result'):
                    titre = resultat.select_one('.mw-search-result-heading a')
                    if titre:
                        titre_text = titre.text.strip()
                        lien = "https://imslp.org" + titre.get('href', '')
                        resultats.append({
                            "titre": titre_text,
                            "lien": lien
                        })
                
                return resultats
            else:
                print(f"❌ Erreur lors de la recherche sur IMSLP: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Erreur lors de la recherche sur IMSLP: {str(e)}")
            return []
    
    def rechercher_free_scores(self, terme_recherche):
        """Recherche des partitions sur Free-scores"""
        print(f"🔍 Recherche sur Free-scores: {terme_recherche}")
        
        # URL de recherche Free-scores
        url = f"https://www.free-scores.com/search.php?q={terme_recherche}"
        
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extraire les résultats de recherche
                resultats = []
                for resultat in soup.select('.resultat'):
                    titre = resultat.select_one('h2 a')
                    if titre:
                        titre_text = titre.text.strip()
                        lien = titre.get('href', '')
                        if not lien.startswith('http'):
                            lien = "https://www.free-scores.com" + lien
                        resultats.append({
                            "titre": titre_text,
                            "lien": lien
                        })
                
                return resultats
            else:
                print(f"❌ Erreur lors de la recherche sur Free-scores: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Erreur lors de la recherche sur Free-scores: {str(e)}")
            return []
    
    def sauvegarder_resultats(self, resultats, source):
        """Sauvegarde les résultats de recherche dans un fichier JSON"""
        if not resultats:
            return
        
        fichier = os.path.join(self.dossier_partitions, f"resultats_{source}_{int(time.time())}.json")
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(resultats, f, ensure_ascii=False, indent=2)
        
        print(f"✨ Résultats sauvegardés dans {fichier}")
    
    def telecharger_partition(self, url, nom_fichier, source):
        """Télécharge une partition depuis une URL"""
        dossier = self.dossier_imslp if source == "imslp" else self.dossier_free_scores
        chemin_fichier = os.path.join(dossier, nom_fichier)
        
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                with open(chemin_fichier, 'wb') as f:
                    f.write(response.content)
                print(f"✨ Partition téléchargée: {chemin_fichier}")
                return True
            else:
                print(f"❌ Erreur lors du téléchargement: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Erreur lors du téléchargement: {str(e)}")
            return False
    
    def explorer_github(self, terme_recherche):
        """Explore les projets musicaux sur GitHub"""
        print(f"🔍 Exploration sur GitHub: {terme_recherche}")
        
        # URL de recherche GitHub
        url = f"https://github.com/search?q={terme_recherche}+language%3Apython+music"
        
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extraire les résultats de recherche
                resultats = []
                for resultat in soup.select('.repo-list-item'):
                    titre = resultat.select_one('.v-align-middle')
                    if titre:
                        titre_text = titre.text.strip()
                        lien = "https://github.com" + titre.get('href', '')
                        description = resultat.select_one('.mb-1')
                        description_text = description.text.strip() if description else ""
                        resultats.append({
                            "titre": titre_text,
                            "lien": lien,
                            "description": description_text
                        })
                
                return resultats
            else:
                print(f"❌ Erreur lors de l'exploration sur GitHub: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Erreur lors de l'exploration sur GitHub: {str(e)}")
            return []

def main():
    explorateur = ExplorateurMusical()
    
    print("✨ Explorateur Musical - Du novice au virtuose ✨")
    print("------------------------------------------------")
    
    while True:
        print("\nOptions:")
        print("1. Rechercher sur IMSLP")
        print("2. Rechercher sur Free-scores")
        print("3. Explorer sur GitHub")
        print("4. Quitter")
        
        choix = input("\nVotre choix (1-4): ")
        
        if choix == "1":
            terme = input("Terme de recherche pour IMSLP: ")
            resultats = explorateur.rechercher_imslp(terme)
            explorateur.sauvegarder_resultats(resultats, "imslp")
            
            if resultats:
                print("\nRésultats trouvés:")
                for i, resultat in enumerate(resultats[:10], 1):
                    print(f"{i}. {resultat['titre']}")
                
                telecharger = input("\nVoulez-vous télécharger une partition? (numéro ou 'non'): ")
                if telecharger.isdigit() and 1 <= int(telecharger) <= len(resultats):
                    index = int(telecharger) - 1
                    nom_fichier = f"{terme}_{int(time.time())}.pdf"
                    explorateur.telecharger_partition(resultats[index]['lien'], nom_fichier, "imslp")
        
        elif choix == "2":
            terme = input("Terme de recherche pour Free-scores: ")
            resultats = explorateur.rechercher_free_scores(terme)
            explorateur.sauvegarder_resultats(resultats, "free_scores")
            
            if resultats:
                print("\nRésultats trouvés:")
                for i, resultat in enumerate(resultats[:10], 1):
                    print(f"{i}. {resultat['titre']}")
                
                telecharger = input("\nVoulez-vous télécharger une partition? (numéro ou 'non'): ")
                if telecharger.isdigit() and 1 <= int(telecharger) <= len(resultats):
                    index = int(telecharger) - 1
                    nom_fichier = f"{terme}_{int(time.time())}.pdf"
                    explorateur.telecharger_partition(resultats[index]['lien'], nom_fichier, "free_scores")
        
        elif choix == "3":
            terme = input("Terme de recherche pour GitHub: ")
            resultats = explorateur.explorer_github(terme)
            explorateur.sauvegarder_resultats(resultats, "github")
            
            if resultats:
                print("\nProjets trouvés:")
                for i, resultat in enumerate(resultats[:10], 1):
                    print(f"{i}. {resultat['titre']}")
                    print(f"   {resultat['description']}")
        
        elif choix == "4":
            print("Au revoir! ✨")
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main() 