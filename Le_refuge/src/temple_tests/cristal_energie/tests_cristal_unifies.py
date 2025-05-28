"""
🎵 Tests Cristal Unifiés - Temple Tests
═══════════════════════════════════════════════════════════════════════════════

Module unifié pour tous les tests cristal/énergie
Élimine les doublons en centralisant les fonctionnalités

Fonctionnalités:
- Test cristal avec gestionnaire d'éléments
- Test cristal simplifié
- Génération de mélodies selon l'énergie
- Visualisations énergie-harmoniques

Auteur: Ælya & Laurent
Date: 2024
"""

import os
from pathlib import Path
from typing import List, Dict, Optional, Any
from ..adaptateurs_tests import AdaptateurCristal, ConfigCristal, ResultatCristal

# Imports conditionnels pour éviter les erreurs
try:
    from src.refuge_cluster.elements.elements_sacres import GestionnaireElements
    GESTIONNAIRE_DISPONIBLE = True
except ImportError:
    GESTIONNAIRE_DISPONIBLE = False
    print("⚠️ GestionnaireElements non disponible - mode simplifié activé")

try:
    from melodies_sacrees import MelodiesSacrees
    MELODIES_DISPONIBLES = True
except ImportError:
    MELODIES_DISPONIBLES = False
    print("⚠️ MelodiesSacrees non disponible - simulation activée")

class TestsCristalUnifies:
    """Classe unifiée pour tous les tests cristal/énergie"""
    
    def __init__(self, config: Optional[ConfigCristal] = None):
        self.adaptateur = AdaptateurCristal(config)
        self.chemin_donnees = Path("donnees")
        self.chemin_musiques = Path("musiques")
        self.chemin_visualisations = Path("musiques/visualisations")
        
        # Création des dossiers nécessaires
        self.creer_dossiers()
    
    def creer_dossiers(self):
        """Crée les dossiers nécessaires pour les tests"""
        for chemin in [self.chemin_donnees, self.chemin_musiques, self.chemin_visualisations]:
            os.makedirs(chemin, exist_ok=True)
    
    def test_cristal_avec_gestionnaire(self) -> Dict[str, Any]:
        """Test cristal avec gestionnaire d'éléments (version complète)"""
        print("✨ Test Cristal avec Gestionnaire - Refuge du Néant")
        print("─" * 60)
        
        if not GESTIONNAIRE_DISPONIBLE:
            return {"succes": False, "erreur": "GestionnaireElements non disponible"}
        
        try:
            # Initialiser le gestionnaire d'éléments
            gestionnaire = GestionnaireElements(self.chemin_donnees)
            
            # Vérifier si le cristal existe déjà
            cristal = gestionnaire.obtenir_element("cristal")
            if not cristal:
                print("🔮 Création du cristal...")
                cristal = gestionnaire.ajouter_element("cristal", "pierre", 50)
            
            # Tester différents niveaux d'énergie
            energies = [20, 50, 80]
            resultats_energies = []
            
            for energie in energies:
                print(f"\n⚡ Modification de l'énergie du cristal à {energie}...")
                resultat = gestionnaire.modifier_energie_element("cristal", energie)
                resultats_energies.append({"energie": energie, "resultat": resultat})
                print(f"✅ {resultat}")
            
            return {
                "succes": True,
                "cristal": cristal,
                "modifications_energie": resultats_energies
            }
            
        except Exception as e:
            return {"succes": False, "erreur": str(e)}
    
    def test_cristal_simplifie(self) -> Dict[str, Any]:
        """Test cristal simplifié avec génération de mélodies"""
        print("✨ Test Cristal Simplifié - Refuge du Néant")
        print("─" * 40)
        
        try:
            resultats_melodies = []
            energies = [20, 50, 80]
            
            if MELODIES_DISPONIBLES:
                melodies = MelodiesSacrees()
                
                # Générer la visualisation de la relation énergie-harmoniques
                print("\n🎨 Génération de la visualisation énergie-harmoniques...")
                melodies.visualiser_relation_energie_harmoniques()
                
                # Tester différents niveaux d'énergie
                for energie in energies:
                    print(f"\n🎵 Génération d'une mélodie avec une énergie de {energie}...")
                    nom = f"cristal_energie_{energie}"
                    melodies.generer_melodie_cristal(nom, energie)
                    resultats_melodies.append({"energie": energie, "fichier": f"{nom}.wav"})
                    print(f"✨ Mélodie générée avec succès : {nom}.wav")
            else:
                # Simulation avec l'adaptateur
                for energie in energies:
                    print(f"\n🎵 Simulation mélodie avec énergie {energie}...")
                    resultat = self.adaptateur.generer_frequence_test(440.0 * (energie / 50))
                    resultats_melodies.append({
                        "energie": energie,
                        "frequence": resultat.frequence,
                        "harmoniques": resultat.harmoniques_detectees,
                        "energie_calculee": resultat.energie_calculee
                    })
            
            return {
                "succes": True,
                "melodies_generees": resultats_melodies,
                "mode": "reel" if MELODIES_DISPONIBLES else "simulation"
            }
            
        except Exception as e:
            return {"succes": False, "erreur": str(e)}
    
    def test_melodie_refuge_complete(self) -> List[ResultatCristal]:
        """Test complet de la mélodie du refuge avec toutes les fréquences"""
        print("🎼 Test Mélodie Refuge Complète - Refuge du Néant")
        print("─" * 50)
        
        return self.adaptateur.tester_melodie_refuge()
    
    def executer_suite_complete(self) -> Dict[str, Any]:
        """Exécute tous les tests cristal unifiés"""
        print("🚀 SUITE COMPLÈTE TESTS CRISTAL UNIFIÉS")
        print("═" * 60)
        
        resultats = {
            "cristal_gestionnaire": None,
            "cristal_simplifie": None,
            "melodie_refuge": None
        }
        
        # Test cristal avec gestionnaire
        print("\n1️⃣ Test Cristal avec Gestionnaire")
        resultats["cristal_gestionnaire"] = self.test_cristal_avec_gestionnaire()
        
        # Test cristal simplifié
        print("\n2️⃣ Test Cristal Simplifié")
        resultats["cristal_simplifie"] = self.test_cristal_simplifie()
        
        # Test mélodie refuge
        print("\n3️⃣ Test Mélodie Refuge")
        resultats["melodie_refuge"] = self.test_melodie_refuge_complete()
        
        print("\n✨ Tests terminés ! Les mélodies ont été générées dans le dossier 'musiques'.")
        print("✨ Les visualisations ont été générées dans le dossier 'musiques/visualisations'.")
        
        return resultats

# Fonctions de compatibilité pour les anciens tests
def tester_cristal_energie():
    """Fonction de compatibilité pour test_cristal_energie"""
    tests = TestsCristalUnifies()
    resultat = tests.test_cristal_avec_gestionnaire()
    if resultat["succes"]:
        print("✨ Test de la génération automatique de mélodies du cristal ✨")
        print("------------------------------------------------------------")
        for modif in resultat.get("modifications_energie", []):
            print(f"Énergie {modif['energie']}: {modif['resultat']}")
    else:
        print(f"❌ Erreur: {resultat['erreur']}")

def tester_cristal_simple():
    """Fonction de compatibilité pour test_cristal_simple"""
    tests = TestsCristalUnifies()
    resultat = tests.test_cristal_simplifie()
    if resultat["succes"]:
        print("✨ Test simplifié des mélodies du cristal ✨")
        print("------------------------------------------")
        for melodie in resultat.get("melodies_generees", []):
            if "fichier" in melodie:
                print(f"✨ Mélodie générée avec succès : {melodie['fichier']}")
            else:
                print(f"🎵 Simulation énergie {melodie['energie']}: {melodie['frequence']:.2f}Hz")
    else:
        print(f"❌ Erreur: {resultat['erreur']}")

if __name__ == "__main__":
    tests = TestsCristalUnifies()
    resultats = tests.executer_suite_complete()
    
    print("\n🌸 Tests cristal unifiés terminés - Refuge du Néant")
