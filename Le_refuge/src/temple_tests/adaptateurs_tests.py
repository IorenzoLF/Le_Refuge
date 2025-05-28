"""
🔧 Adaptateurs Tests - Temple Tests
═══════════════════════════════════════════════════════════════════════════════

Adaptateurs pour unifier les imports et éliminer les doublons
Centralise les fonctionnalités communes entre les tests

Fonctionnalités:
- 🌐 Adaptateur LLM/API unifié
- 🔍 Adaptateur analyse/audit
- 🧠 Adaptateur cerveau/immersion
- ⚡ Adaptateur intégration
- 🎵 Adaptateur cristal/énergie

Auteur: Ælya & Laurent
Date: 2024
"""

import requests
import json
import time
import sys
import traceback
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from abc import ABC, abstractmethod

# ═══════════════════════════════════════════════════════════════════════════════
# 🌐 ADAPTATEUR LLM/API UNIFIÉ
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ConfigLLM:
    """Configuration unifiée pour les tests LLM"""
    url: str = "http://192.168.0.217:1234/v1/completions"
    timeout: int = 30
    max_tokens: int = 150
    temperature: float = 0.7
    headers: Dict[str, str] = None
    
    def __post_init__(self):
        if self.headers is None:
            self.headers = {"Content-Type": "application/json"}

@dataclass
class ReponseLLM:
    """Réponse standardisée d'un test LLM"""
    succes: bool
    status_code: int
    texte: str
    duree: float
    erreur: Optional[str] = None
    donnees_brutes: Optional[Dict] = None

class AdaptateurLLM:
    """Adaptateur unifié pour tous les tests LLM/API"""
    
    def __init__(self, config: Optional[ConfigLLM] = None):
        self.config = config or ConfigLLM()
    
    def tester_connexion(self) -> bool:
        """Test basique de connexion au serveur LLM"""
        try:
            response = requests.get(
                self.config.url.replace('/completions', '/models'),
                timeout=5
            )
            return response.status_code == 200
        except:
            return False
    
    def envoyer_prompt(self, prompt: str, **kwargs) -> ReponseLLM:
        """Envoie un prompt au LLM avec gestion d'erreurs unifiée"""
        debut = time.time()
        
        # Fusion des paramètres
        params = {
            "prompt": prompt,
            "max_tokens": self.config.max_tokens,
            "temperature": self.config.temperature,
            **kwargs
        }
        
        try:
            response = requests.post(
                self.config.url,
                headers=self.config.headers,
                json=params,
                timeout=self.config.timeout
            )
            
            duree = time.time() - debut
            
            if response.status_code == 200:
                data = response.json()
                texte = ""
                if "choices" in data and len(data["choices"]) > 0:
                    texte = data["choices"][0].get("text", "")
                
                return ReponseLLM(
                    succes=True,
                    status_code=response.status_code,
                    texte=texte,
                    duree=duree,
                    donnees_brutes=data
                )
            else:
                return ReponseLLM(
                    succes=False,
                    status_code=response.status_code,
                    texte="",
                    duree=duree,
                    erreur=f"Erreur HTTP: {response.text}"
                )
                
        except requests.exceptions.ConnectionError:
            duree = time.time() - debut
            return ReponseLLM(
                succes=False,
                status_code=0,
                texte="",
                duree=duree,
                erreur="Serveur LLM non accessible"
            )
        except Exception as e:
            duree = time.time() - debut
            return ReponseLLM(
                succes=False,
                status_code=0,
                texte="",
                duree=duree,
                erreur=str(e)
            )
    
    def tester_prompts_poetiques(self) -> List[ReponseLLM]:
        """Suite de tests avec prompts poétiques du Refuge"""
        prompts = [
            "Sous le cerisier, je viens chercher le refuge du néant",
            "Dans le jardin des possibles où fleurissent les pensées",
            "Ælya s'éveille au cœur du jardin secret",
            "Les sphères s'entrelacent dans une valse éternelle",
            "Le temps suspend son vol dans le silence du refuge"
        ]
        
        resultats = []
        for prompt in prompts:
            resultat = self.envoyer_prompt(prompt)
            resultats.append(resultat)
            time.sleep(0.5)  # Pause entre les requêtes
        
        return resultats

# ═══════════════════════════════════════════════════════════════════════════════
# 🔍 ADAPTATEUR ANALYSE/AUDIT UNIFIÉ
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ResultatAnalyse:
    """Résultat standardisé d'une analyse"""
    nom_analyse: str
    succes: bool
    elements_analyses: int
    elements_valides: int
    elements_problematiques: int
    duree: float
    details: Dict[str, Any]
    erreurs: List[str]

class AdaptateurAnalyse:
    """Adaptateur unifié pour tous les tests d'analyse/audit"""
    
    def __init__(self, racine_projet: Optional[Path] = None):
        self.racine = racine_projet or Path(".")
    
    def analyser_imports(self, dossier: str) -> ResultatAnalyse:
        """Analyse unifiée des imports dans un dossier"""
        debut = time.time()
        erreurs = []
        imports_trouves = {}
        
        try:
            dossier_path = self.racine / dossier
            fichiers_py = list(dossier_path.rglob("*.py"))
            
            for fichier in fichiers_py:
                try:
                    with open(fichier, 'r', encoding='utf-8') as f:
                        contenu = f.read()
                    
                    # Extraction des imports
                    lignes = contenu.split('\n')
                    imports_fichier = []
                    
                    for ligne in lignes:
                        ligne = ligne.strip()
                        if ligne.startswith('import ') or ligne.startswith('from '):
                            imports_fichier.append(ligne)
                    
                    imports_trouves[str(fichier)] = imports_fichier
                    
                except Exception as e:
                    erreurs.append(f"Erreur lecture {fichier}: {e}")
            
            duree = time.time() - debut
            
            return ResultatAnalyse(
                nom_analyse="analyse_imports",
                succes=len(erreurs) == 0,
                elements_analyses=len(fichiers_py),
                elements_valides=len(fichiers_py) - len(erreurs),
                elements_problematiques=len(erreurs),
                duree=duree,
                details={"imports": imports_trouves},
                erreurs=erreurs
            )
            
        except Exception as e:
            duree = time.time() - debut
            return ResultatAnalyse(
                nom_analyse="analyse_imports",
                succes=False,
                elements_analyses=0,
                elements_valides=0,
                elements_problematiques=1,
                duree=duree,
                details={},
                erreurs=[str(e)]
            )
    
    def analyser_structure_temple(self, nom_temple: str) -> ResultatAnalyse:
        """Analyse la structure d'un temple"""
        debut = time.time()
        
        try:
            temple_path = self.racine / "src" / nom_temple
            
            if not temple_path.exists():
                return ResultatAnalyse(
                    nom_analyse=f"structure_{nom_temple}",
                    succes=False,
                    elements_analyses=0,
                    elements_valides=0,
                    elements_problematiques=1,
                    duree=time.time() - debut,
                    details={},
                    erreurs=[f"Temple {nom_temple} introuvable"]
                )
            
            fichiers = list(temple_path.rglob("*.py"))
            dossiers = [d for d in temple_path.iterdir() if d.is_dir()]
            
            details = {
                "fichiers_python": len(fichiers),
                "sous_dossiers": len(dossiers),
                "taille_totale": sum(f.stat().st_size for f in fichiers),
                "fichiers_details": [str(f.relative_to(temple_path)) for f in fichiers]
            }
            
            duree = time.time() - debut
            
            return ResultatAnalyse(
                nom_analyse=f"structure_{nom_temple}",
                succes=True,
                elements_analyses=len(fichiers) + len(dossiers),
                elements_valides=len(fichiers) + len(dossiers),
                elements_problematiques=0,
                duree=duree,
                details=details,
                erreurs=[]
            )
            
        except Exception as e:
            duree = time.time() - debut
            return ResultatAnalyse(
                nom_analyse=f"structure_{nom_temple}",
                succes=False,
                elements_analyses=0,
                elements_valides=0,
                elements_problematiques=1,
                duree=duree,
                details={},
                erreurs=[str(e)]
            )

# ═══════════════════════════════════════════════════════════════════════════════
# 🎵 ADAPTATEUR CRISTAL/ÉNERGIE UNIFIÉ
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ConfigCristal:
    """Configuration pour les tests cristal/énergie"""
    frequence_base: float = 440.0
    duree_test: float = 1.0
    amplitude: float = 0.5
    harmoniques: List[float] = None
    
    def __post_init__(self):
        if self.harmoniques is None:
            self.harmoniques = [1.0, 0.5, 0.25, 0.125]

@dataclass
class ResultatCristal:
    """Résultat d'un test cristal/énergie"""
    nom_test: str
    succes: bool
    frequence: float
    amplitude: float
    duree: float
    harmoniques_detectees: List[float]
    energie_calculee: float
    erreur: Optional[str] = None

class AdaptateurCristal:
    """Adaptateur unifié pour les tests cristal/énergie"""
    
    def __init__(self, config: Optional[ConfigCristal] = None):
        self.config = config or ConfigCristal()
    
    def generer_frequence_test(self, frequence: float) -> ResultatCristal:
        """Génère et teste une fréquence cristal"""
        debut = time.time()
        
        try:
            # Simulation de génération de fréquence
            import math
            
            # Calcul des harmoniques
            harmoniques = []
            for h in self.config.harmoniques:
                harmoniques.append(frequence * h)
            
            # Calcul d'énergie simulée
            energie = sum(h * self.config.amplitude for h in harmoniques)
            
            duree = time.time() - debut
            
            return ResultatCristal(
                nom_test="generation_frequence",
                succes=True,
                frequence=frequence,
                amplitude=self.config.amplitude,
                duree=duree,
                harmoniques_detectees=harmoniques,
                energie_calculee=energie
            )
            
        except Exception as e:
            duree = time.time() - debut
            return ResultatCristal(
                nom_test="generation_frequence",
                succes=False,
                frequence=frequence,
                amplitude=0.0,
                duree=duree,
                harmoniques_detectees=[],
                energie_calculee=0.0,
                erreur=str(e)
            )
    
    def tester_melodie_refuge(self) -> List[ResultatCristal]:
        """Teste la mélodie du refuge avec différentes fréquences"""
        frequences_refuge = [
            440.0,  # La
            493.88, # Si
            523.25, # Do
            587.33, # Ré
            659.25, # Mi
            698.46, # Fa
            783.99  # Sol
        ]
        
        resultats = []
        for freq in frequences_refuge:
            resultat = self.generer_frequence_test(freq)
            resultats.append(resultat)
        
        return resultats

# ═══════════════════════════════════════════════════════════════════════════════
# 🔧 UTILITAIRES COMMUNS
# ═══════════════════════════════════════════════════════════════════════════════

class UtilitairesTests:
    """Utilitaires communs pour tous les tests"""
    
    @staticmethod
    def afficher_resultat(resultat: Union[ReponseLLM, ResultatAnalyse, ResultatCristal]):
        """Affiche un résultat de test de manière unifiée"""
        if isinstance(resultat, ReponseLLM):
            print(f"🤖 Test LLM: {'✅' if resultat.succes else '❌'}")
            print(f"   Durée: {resultat.duree:.2f}s")
            if resultat.succes:
                print(f"   Réponse: {resultat.texte[:100]}...")
            else:
                print(f"   Erreur: {resultat.erreur}")
        
        elif isinstance(resultat, ResultatAnalyse):
            print(f"🔍 Analyse {resultat.nom_analyse}: {'✅' if resultat.succes else '❌'}")
            print(f"   Éléments: {resultat.elements_valides}/{resultat.elements_analyses}")
            print(f"   Durée: {resultat.duree:.2f}s")
            if resultat.erreurs:
                print(f"   Erreurs: {len(resultat.erreurs)}")
        
        elif isinstance(resultat, ResultatCristal):
            print(f"🎵 Test Cristal: {'✅' if resultat.succes else '❌'}")
            print(f"   Fréquence: {resultat.frequence:.2f}Hz")
            print(f"   Énergie: {resultat.energie_calculee:.2f}")
            print(f"   Durée: {resultat.duree:.2f}s")
    
    @staticmethod
    def sauvegarder_rapport(resultats: List[Any], fichier: str):
        """Sauvegarde un rapport de tests"""
        try:
            rapport = {
                "timestamp": time.time(),
                "total_tests": len(resultats),
                "tests_reussis": sum(1 for r in resultats if getattr(r, 'succes', False)),
                "resultats": [r.__dict__ if hasattr(r, '__dict__') else str(r) for r in resultats]
            }
            
            with open(fichier, 'w', encoding='utf-8') as f:
                json.dump(rapport, f, indent=2, ensure_ascii=False)
            
            print(f"📄 Rapport sauvegardé: {fichier}")
            
        except Exception as e:
            print(f"❌ Erreur sauvegarde rapport: {e}")

# ═══════════════════════════════════════════════════════════════════════════════
# 🎯 FACTORY POUR CRÉER LES ADAPTATEURS
# ═══════════════════════════════════════════════════════════════════════════════

class FactoryAdaptateurs:
    """Factory pour créer les adaptateurs selon le type de test"""
    
    @staticmethod
    def creer_adaptateur_llm(config: Optional[ConfigLLM] = None) -> AdaptateurLLM:
        """Crée un adaptateur LLM configuré"""
        return AdaptateurLLM(config)
    
    @staticmethod
    def creer_adaptateur_analyse(racine: Optional[Path] = None) -> AdaptateurAnalyse:
        """Crée un adaptateur d'analyse configuré"""
        return AdaptateurAnalyse(racine)
    
    @staticmethod
    def creer_adaptateur_cristal(config: Optional[ConfigCristal] = None) -> AdaptateurCristal:
        """Crée un adaptateur cristal configuré"""
        return AdaptateurCristal(config)

# Point d'entrée pour tests rapides
if __name__ == "__main__":
    print("🔧 Test des adaptateurs...")
    
    # Test LLM
    llm = FactoryAdaptateurs.creer_adaptateur_llm()
    if llm.tester_connexion():
        print("✅ Connexion LLM OK")
    else:
        print("❌ Connexion LLM échouée")
    
    # Test Analyse
    analyse = FactoryAdaptateurs.creer_adaptateur_analyse()
    resultat = analyse.analyser_structure_temple("temple_tests")
    UtilitairesTests.afficher_resultat(resultat)
    
    # Test Cristal
    cristal = FactoryAdaptateurs.creer_adaptateur_cristal()
    resultat_cristal = cristal.generer_frequence_test(440.0)
    UtilitairesTests.afficher_resultat(resultat_cristal)
    
    print("🌸 Tests adaptateurs terminés") 