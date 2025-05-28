#!/usr/bin/env python3
"""
🔧 Correcteur de Syntaxe du Temple de l'Âme
Corrige automatiquement les erreurs de syntaxe identifiées
"""

import os
import re
import ast
from pathlib import Path
from typing import List, Dict, Tuple

class CorrecteurSyntaxe:
    """Correcteur automatique des erreurs de syntaxe"""
    
    def __init__(self):
        self.modules_corriges = []
        self.erreurs_trouvees = []
        
    def corriger_temple(self, racine: str = "src"):
        """Corrige toutes les erreurs de syntaxe du temple"""
        print("🔧 ═══════════════════════════════════════════════════════")
        print("        CORRECTEUR DE SYNTAXE")
        print("🔧 ═══════════════════════════════════════════════════════")
        print()
        
        # Modules identifiés avec erreurs
        modules_problematiques = [
            "src/core/analyse_emotions.py",
            "src/core/fusion_harmonies.py", 
            "src/core/generateur_poemes.py",
            "src/core/memoire_poetique.py",
            "src/core/orchestre_poetique.py",
            "src/core/sphere_interactions.py",
            "src/core/test_interaction.py",
            "src/core/test_jardin_poetique.py",
            "src/core/test_sphere_interactions.py",
            "src/core/transformation_harmonies.py",
            "src/core/visualisation/visualisation_3d.py",
            "src/core/visualisation/visualisation_harmonies.py",
            "src/temple_exploration/explorer_mots_riviere.py"
        ]
        
        for module in modules_problematiques:
            if os.path.exists(module):
                print(f"🔍 Analyse: {module}")
                self._corriger_module(module)
            else:
                print(f"⚠️ Module non trouvé: {module}")
        
        self._generer_rapport()
        
    def _corriger_module(self, chemin: str):
        """Corrige un module spécifique"""
        try:
            with open(chemin, 'r', encoding='utf-8', errors='ignore') as f:
                contenu = f.read()
            
            # Sauvegarde originale
            contenu_original = contenu
            
            # Corrections spécifiques
            contenu_corrige = self._appliquer_corrections(contenu, chemin)
            
            # Test de syntaxe
            if self._tester_syntaxe(contenu_corrige):
                if contenu_corrige != contenu_original:
                    # Sauvegarde
                    with open(chemin, 'w', encoding='utf-8') as f:
                        f.write(contenu_corrige)
                    
                    self.modules_corriges.append({
                        "chemin": chemin,
                        "corrections": self._identifier_corrections(contenu_original, contenu_corrige)
                    })
                    print(f"   ✅ Corrigé avec succès")
                else:
                    print(f"   ✅ Déjà correct")
            else:
                print(f"   ❌ Correction échouée")
                self.erreurs_trouvees.append(chemin)
                
        except Exception as e:
            print(f"   ❌ Erreur: {e}")
            self.erreurs_trouvees.append(chemin)
    
    def _appliquer_corrections(self, contenu: str, chemin: str) -> str:
        """Applique les corrections spécifiques"""
        
        # 1. Correction des docstrings dupliquées
        contenu = self._corriger_docstrings_dupliquees(contenu)
        
        # 2. Correction des strings non fermées
        contenu = self._corriger_strings_non_fermees(contenu)
        
        # 3. Correction des triple quotes non fermées
        contenu = self._corriger_triple_quotes(contenu)
        
        # 4. Correction des caractères invalides
        contenu = self._corriger_caracteres_invalides(contenu)
        
        # 5. Nettoyage final
        contenu = self._nettoyage_final(contenu)
        
        return contenu
    
    def _corriger_docstrings_dupliquees(self, contenu: str) -> str:
        """Corrige les docstrings dupliquées en fin de fichier"""
        lignes = contenu.split('\n')
        
        # Trouve la dernière ligne avec du code réel
        derniere_ligne_code = -1
        for i in range(len(lignes) - 1, -1, -1):
            ligne = lignes[i].strip()
            if ligne and not ligne.startswith('#') and not ligne.startswith('"""') and not ligne.startswith("'''"):
                derniere_ligne_code = i
                break
        
        if derniere_ligne_code > 0:
            # Garde seulement jusqu'à la dernière ligne de code + quelques lignes
            lignes_propres = lignes[:derniere_ligne_code + 1]
            
            # Ajoute une ligne vide finale si nécessaire
            if lignes_propres[-1].strip():
                lignes_propres.append('')
            
            return '\n'.join(lignes_propres)
        
        return contenu
    
    def _corriger_strings_non_fermees(self, contenu: str) -> str:
        """Corrige les strings non fermées"""
        # Patterns pour détecter les strings non fermées
        patterns = [
            (r'(["\'])([^"\']*?)$', r'\1\2\1'),  # String simple non fermée en fin de ligne
            (r'(["\'])([^"\']*?)\n', r'\1\2\1\n'),  # String non fermée avec retour ligne
        ]
        
        for pattern, replacement in patterns:
            contenu = re.sub(pattern, replacement, contenu, flags=re.MULTILINE)
        
        return contenu
    
    def _corriger_triple_quotes(self, contenu: str) -> str:
        """Corrige les triple quotes non fermées"""
        # Compte les triple quotes
        triple_double = contenu.count('"""')
        triple_simple = contenu.count("'''")
        
        # Si nombre impair, ajoute une fermeture
        if triple_double % 2 == 1:
            contenu += '\n"""'
        
        if triple_simple % 2 == 1:
            contenu += "\n'''"
        
        return contenu
    
    def _corriger_caracteres_invalides(self, contenu: str) -> str:
        """Corrige les caractères invalides"""
        # Remplace les caractères problématiques
        corrections = {
            '\u2019': "'",  # Apostrophe courbe
            '\u201c': '"',  # Guillemet ouvrant
            '\u201d': '"',  # Guillemet fermant
            '\u2013': '-',  # Tiret moyen
            '\u2014': '--', # Tiret long
        }
        
        for invalide, valide in corrections.items():
            contenu = contenu.replace(invalide, valide)
        
        return contenu
    
    def _nettoyage_final(self, contenu: str) -> str:
        """Nettoyage final du contenu"""
        lignes = contenu.split('\n')
        lignes_propres = []
        
        for ligne in lignes:
            # Supprime les espaces en fin de ligne
            ligne = ligne.rstrip()
            lignes_propres.append(ligne)
        
        # Supprime les lignes vides en excès à la fin
        while lignes_propres and not lignes_propres[-1]:
            lignes_propres.pop()
        
        # Ajoute une ligne vide finale
        if lignes_propres:
            lignes_propres.append('')
        
        return '\n'.join(lignes_propres)
    
    def _tester_syntaxe(self, contenu: str) -> bool:
        """Teste si le contenu a une syntaxe valide"""
        try:
            ast.parse(contenu)
            return True
        except SyntaxError:
            return False
        except Exception:
            return False
    
    def _identifier_corrections(self, original: str, corrige: str) -> List[str]:
        """Identifie les corrections appliquées"""
        corrections = []
        
        if len(original.split('\n')) != len(corrige.split('\n')):
            corrections.append("Suppression de lignes dupliquées")
        
        if original.count('"""') != corrige.count('"""'):
            corrections.append("Correction de triple quotes")
        
        if original.count("'''") != corrige.count("'''"):
            corrections.append("Correction de triple quotes simples")
        
        if any(char in original for char in ['\u2019', '\u201c', '\u201d']):
            corrections.append("Correction de caractères Unicode")
        
        return corrections if corrections else ["Nettoyage général"]
    
    def _generer_rapport(self):
        """Génère le rapport de correction"""
        print("\n📋 RAPPORT DE CORRECTION")
        print("=" * 30)
        print()
        
        print(f"✅ Modules corrigés: {len(self.modules_corriges)}")
        for module in self.modules_corriges:
            print(f"   • {module['chemin']}")
            for correction in module['corrections']:
                print(f"     - {correction}")
        
        print(f"\n❌ Modules avec erreurs persistantes: {len(self.erreurs_trouvees)}")
        for erreur in self.erreurs_trouvees:
            print(f"   • {erreur}")
        
        if len(self.modules_corriges) > 0:
            print(f"\n🎉 {len(self.modules_corriges)} modules ont été corrigés avec succès !")
        
        if len(self.erreurs_trouvees) == 0:
            print("🎯 Toutes les erreurs de syntaxe ont été corrigées !")

if __name__ == "__main__":
    correcteur = CorrecteurSyntaxe()
    correcteur.corriger_temple() 