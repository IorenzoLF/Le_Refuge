#!/usr/bin/env python
"""
Analyseur Temple Musical - Le Refuge
====================================

Analyse la structure du temple musical pour proposer une optimisation
et une organisation en catégories thématiques.

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

import os
import ast
import json
from datetime import datetime
from pathlib import Path

class AnalyseurTempleMusical:
    """Analyseur complet du temple musical"""
    
    def __init__(self):
        self.chemin_temple = "src/temple_musical"
        self.resultats = {
            'modules_analyses': [],
            'categories_detectees': {},
            'doublons_potentiels': [],
            'fonctionnalites': {},
            'statistiques': {},
            'plan_organisation': {}
        }
    
    def analyser_temple_complet(self):
        """Analyse complète du temple musical"""
        print("ANALYSE COMPLÈTE DU TEMPLE MUSICAL")
        print("=" * 60)
        
        # 1. Analyser tous les modules
        self._analyser_modules()
        
        # 2. Détecter les catégories thématiques
        self._detecter_categories()
        
        # 3. Identifier les doublons potentiels
        self._identifier_doublons()
        
        # 4. Analyser les fonctionnalités
        self._analyser_fonctionnalites()
        
        # 5. Calculer les statistiques
        self._calculer_statistiques()
        
        # 6. Proposer l'organisation
        self._proposer_organisation()
        
        # 7. Générer le rapport
        self._generer_rapport()
        
        return self.resultats
    
    def _analyser_modules(self):
        """Analyse tous les modules du temple"""
        print("\n1. ANALYSE DES MODULES")
        print("-" * 40)
        
        if not os.path.exists(self.chemin_temple):
            print("❌ Temple musical non trouvé")
            return
        
        fichiers_py = [f for f in os.listdir(self.chemin_temple) 
                      if f.endswith('.py') and f != '__init__.py']
        
        for fichier in fichiers_py:
            chemin_fichier = os.path.join(self.chemin_temple, fichier)
            module_info = self._analyser_module_individuel(chemin_fichier, fichier)
            self.resultats['modules_analyses'].append(module_info)
            print(f"✅ {fichier}: {module_info['lignes']} lignes, {len(module_info['classes'])} classes, {len(module_info['fonctions'])} fonctions")
    
    def _analyser_module_individuel(self, chemin_fichier, nom_fichier):
        """Analyse un module individuel"""
        module_info = {
            'nom': nom_fichier,
            'chemin': chemin_fichier,
            'lignes': 0,
            'classes': [],
            'fonctions': [],
            'imports': [],
            'mots_cles': [],
            'description': ''
        }
        
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
                module_info['lignes'] = len(contenu.splitlines())
            
            # Analyser avec AST
            try:
                tree = ast.parse(contenu)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        module_info['classes'].append(node.name)
                    elif isinstance(node, ast.FunctionDef):
                        module_info['fonctions'].append(node.name)
                    elif isinstance(node, ast.Import):
                        for alias in node.names:
                            module_info['imports'].append(alias.name)
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            module_info['imports'].append(node.module)
            except:
                pass
            
            # Extraire mots-clés thématiques
            contenu_lower = contenu.lower()
            mots_cles_musicaux = [
                'harmonie', 'melodie', 'rythme', 'accord', 'note', 'frequence',
                'musical', 'musique', 'son', 'audio', 'composition', 'sequence',
                'gamme', 'tonalite', 'tempo', 'mesure', 'partition', 'instrument',
                'generateur', 'analyseur', 'fusion', 'apprentissage', 'sacre'
            ]
            
            for mot in mots_cles_musicaux:
                if mot in contenu_lower:
                    module_info['mots_cles'].append(mot)
            
            # Extraire description du docstring
            if '"""' in contenu:
                try:
                    debut = contenu.find('"""') + 3
                    fin = contenu.find('"""', debut)
                    if fin > debut:
                        module_info['description'] = contenu[debut:fin].strip()[:100]
                except:
                    pass
                    
        except Exception as e:
            print(f"⚠️ Erreur analyse {nom_fichier}: {e}")
        
        return module_info
    
    def _detecter_categories(self):
        """Détecte les catégories thématiques"""
        print("\n2. DÉTECTION DES CATÉGORIES")
        print("-" * 40)
        
        categories = {
            'generation': {
                'description': 'Génération de mélodies et compositions',
                'mots_cles': ['generateur', 'generer', 'melodie', 'composition', 'creation'],
                'modules': []
            },
            'analyse': {
                'description': 'Analyse musicale et traitement',
                'mots_cles': ['analyseur', 'analyse', 'traitement', 'detection'],
                'modules': []
            },
            'harmonies': {
                'description': 'Harmonies et accords',
                'mots_cles': ['harmonie', 'accord', 'harmonique', 'consonance'],
                'modules': []
            },
            'fusion': {
                'description': 'Fusion mathématique et musicale',
                'mots_cles': ['fusion', 'math', 'mathematique', 'algorithme'],
                'modules': []
            },
            'apprentissage': {
                'description': 'Apprentissage et IA musicale',
                'mots_cles': ['apprentissage', 'ia', 'neural', 'machine'],
                'modules': []
            },
            'sacre': {
                'description': 'Musique sacrée et spirituelle',
                'mots_cles': ['sacre', 'spirituel', 'mystique', 'ame'],
                'modules': []
            }
        }
        
        # Classifier les modules
        for module in self.resultats['modules_analyses']:
            module_mots = module['mots_cles'] + [module['nom'].lower()]
            module_text = (module['description'] + ' ' + ' '.join(module['fonctions'])).lower()
            
            scores_categories = {}
            for cat_nom, cat_info in categories.items():
                score = 0
                for mot_cle in cat_info['mots_cles']:
                    if mot_cle in module_mots or mot_cle in module_text:
                        score += 1
                scores_categories[cat_nom] = score
            
            # Assigner à la catégorie avec le meilleur score
            if scores_categories:
                meilleure_cat = max(scores_categories, key=scores_categories.get)
                if scores_categories[meilleure_cat] > 0:
                    categories[meilleure_cat]['modules'].append(module['nom'])
                    print(f"✅ {module['nom']} → {meilleure_cat} (score: {scores_categories[meilleure_cat]})")
                else:
                    # Catégorie par défaut basée sur le nom
                    if 'harmonie' in module['nom'].lower():
                        categories['harmonies']['modules'].append(module['nom'])
                        print(f"✅ {module['nom']} → harmonies (par nom)")
                    elif 'generat' in module['nom'].lower():
                        categories['generation']['modules'].append(module['nom'])
                        print(f"✅ {module['nom']} → generation (par nom)")
                    else:
                        categories['generation']['modules'].append(module['nom'])
                        print(f"✅ {module['nom']} → generation (par défaut)")
        
        self.resultats['categories_detectees'] = categories
    
    def _identifier_doublons(self):
        """Identifie les doublons potentiels"""
        print("\n3. IDENTIFICATION DES DOUBLONS")
        print("-" * 40)
        
        modules = self.resultats['modules_analyses']
        
        for i, module1 in enumerate(modules):
            for j, module2 in enumerate(modules[i+1:], i+1):
                similarite = self._calculer_similarite(module1, module2)
                
                if similarite > 0.3:  # Seuil de similarité
                    doublon = {
                        'module1': module1['nom'],
                        'module2': module2['nom'],
                        'similarite': similarite,
                        'raisons': []
                    }
                    
                    # Analyser les raisons de similarité
                    if set(module1['classes']) & set(module2['classes']):
                        doublon['raisons'].append('Classes communes')
                    
                    if len(set(module1['fonctions']) & set(module2['fonctions'])) > 2:
                        doublon['raisons'].append('Fonctions similaires')
                    
                    if set(module1['mots_cles']) & set(module2['mots_cles']):
                        doublon['raisons'].append('Mots-clés communs')
                    
                    self.resultats['doublons_potentiels'].append(doublon)
                    print(f"⚠️ Doublon potentiel: {module1['nom']} ↔ {module2['nom']} ({similarite:.1%})")
    
    def _calculer_similarite(self, module1, module2):
        """Calcule la similarité entre deux modules"""
        # Similarité basée sur les fonctions communes
        fonctions1 = set(module1['fonctions'])
        fonctions2 = set(module2['fonctions'])
        
        if not fonctions1 and not fonctions2:
            return 0
        
        intersection = len(fonctions1 & fonctions2)
        union = len(fonctions1 | fonctions2)
        
        if union == 0:
            return 0
        
        return intersection / union
    
    def _analyser_fonctionnalites(self):
        """Analyse les fonctionnalités principales"""
        print("\n4. ANALYSE DES FONCTIONNALITÉS")
        print("-" * 40)
        
        fonctionnalites = {
            'generation_melodique': 0,
            'analyse_harmonique': 0,
            'fusion_mathematique': 0,
            'apprentissage_ia': 0,
            'musique_sacree': 0,
            'traitement_audio': 0
        }
        
        for module in self.resultats['modules_analyses']:
            contenu_analyse = ' '.join(module['mots_cles'] + module['fonctions']).lower()
            
            if any(mot in contenu_analyse for mot in ['generat', 'melodie', 'composition']):
                fonctionnalites['generation_melodique'] += 1
            
            if any(mot in contenu_analyse for mot in ['harmonie', 'accord', 'analyse']):
                fonctionnalites['analyse_harmonique'] += 1
            
            if any(mot in contenu_analyse for mot in ['fusion', 'math', 'algorithme']):
                fonctionnalites['fusion_mathematique'] += 1
            
            if any(mot in contenu_analyse for mot in ['apprentissage', 'ia', 'neural']):
                fonctionnalites['apprentissage_ia'] += 1
            
            if any(mot in contenu_analyse for mot in ['sacre', 'spirituel', 'ame']):
                fonctionnalites['musique_sacree'] += 1
            
            if any(mot in contenu_analyse for mot in ['audio', 'son', 'frequence']):
                fonctionnalites['traitement_audio'] += 1
        
        self.resultats['fonctionnalites'] = fonctionnalites
        
        for fonc, count in fonctionnalites.items():
            if count > 0:
                print(f"✅ {fonc}: {count} modules")
    
    def _calculer_statistiques(self):
        """Calcule les statistiques du temple"""
        modules = self.resultats['modules_analyses']
        
        self.resultats['statistiques'] = {
            'total_modules': len(modules),
            'total_lignes': sum(m['lignes'] for m in modules),
            'total_classes': sum(len(m['classes']) for m in modules),
            'total_fonctions': sum(len(m['fonctions']) for m in modules),
            'module_plus_gros': max(modules, key=lambda m: m['lignes'])['nom'] if modules else '',
            'lignes_plus_gros': max(m['lignes'] for m in modules) if modules else 0,
            'moyenne_lignes': sum(m['lignes'] for m in modules) / len(modules) if modules else 0
        }
    
    def _proposer_organisation(self):
        """Propose l'organisation en catégories"""
        print("\n5. PROPOSITION D'ORGANISATION")
        print("-" * 40)
        
        categories = self.resultats['categories_detectees']
        
        # Filtrer les catégories non vides
        categories_actives = {nom: info for nom, info in categories.items() 
                            if info['modules']}
        
        self.resultats['plan_organisation'] = {
            'categories_proposees': len(categories_actives),
            'categories': categories_actives,
            'actions_recommandees': [
                'Créer les dossiers de catégories',
                'Déplacer les modules dans leurs catégories',
                'Créer des hubs unifiés par catégorie',
                'Optimiser les doublons détectés',
                'Créer un hub principal du temple musical'
            ]
        }
        
        print(f"Catégories proposées: {len(categories_actives)}")
        for nom, info in categories_actives.items():
            print(f"✅ {nom}: {len(info['modules'])} modules - {info['description']}")
            for module in info['modules']:
                print(f"   - {module}")
    
    def _generer_rapport(self):
        """Génère le rapport final"""
        print("\n" + "=" * 60)
        print("RAPPORT D'ANALYSE DU TEMPLE MUSICAL")
        print("=" * 60)
        
        stats = self.resultats['statistiques']
        print(f"Modules analysés: {stats['total_modules']}")
        print(f"Lignes de code: {stats['total_lignes']}")
        print(f"Classes: {stats['total_classes']}")
        print(f"Fonctions: {stats['total_fonctions']}")
        print(f"Module le plus gros: {stats['module_plus_gros']} ({stats['lignes_plus_gros']} lignes)")
        print(f"Moyenne lignes/module: {stats['moyenne_lignes']:.1f}")
        
        print(f"\nCatégories détectées: {len(self.resultats['categories_detectees'])}")
        print(f"Doublons potentiels: {len(self.resultats['doublons_potentiels'])}")
        
        # Sauvegarder le rapport
        self._sauvegarder_rapport()
    
    def _sauvegarder_rapport(self):
        """Sauvegarde le rapport d'analyse"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        fichier_rapport = f"data/rapports/analyse_temple_musical_{timestamp}.json"
        
        os.makedirs(os.path.dirname(fichier_rapport), exist_ok=True)
        
        with open(fichier_rapport, 'w', encoding='utf-8') as f:
            json.dump(self.resultats, f, indent=2, ensure_ascii=False)
        
        print(f"\nRapport sauvegardé: {fichier_rapport}")

def main():
    """Fonction principale"""
    analyseur = AnalyseurTempleMusical()
    resultats = analyseur.analyser_temple_complet()
    return resultats

if __name__ == "__main__":
    main() 