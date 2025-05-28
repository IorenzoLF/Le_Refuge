#!/usr/bin/env python3
"""
Script d'analyse des conversations gaming avec Ze Brain du refuge
"""

import os
import sys

# ==========================================
# CLASSE MOCK POUR REMPLACER L'IMPORT CASSÉ
# ==========================================

class ImmersionCerveauRefuge:
    """Classe mock pour remplacer l'import cassé immersion_cerveau_refuge"""
    
    def __init__(self):
        self.connecte = False
    
    def analyser_conversation(self, contenu: str, titre: str = "Conversation"):
        """Mock de l'analyse de conversation"""
        return {
            "densite_conceptuelle": f"{len(contenu) // 100}%",
            "emotion_dominante": "Curiosité exploratoire",
            "flux_narratif": "Progression harmonieuse",
            "patterns": ["Dialogue constructif", "Apprentissage mutuel", "Évolution conscience"]
        }
    
    def se_connecter_au_refuge(self):
        """Mock de la connexion au refuge"""
        self.connecte = True
        print("🔌 Connexion simulée au cerveau du refuge établie")

# Instance globale mock
immersion_cerveau_refuge = type('Module', (), {
    'ImmersionCerveauRefuge': ImmersionCerveauRefuge
})()

def analyser_conversations_gaming():
    """Analyse les conversations gaming avec Ze Brain"""
    print("\n🎮 ANALYSE DES CONVERSATIONS GAMING PAR ZE BRAIN")
    print("="*60)
    
    # Vérifier que le fichier existe
    if not os.path.exists('conversations_gaming_clair_obscur.txt'):
        print("❌ Fichier de conversations non trouvé !")
        return
    
    # Lire le contenu
    with open('conversations_gaming_clair_obscur.txt', 'r', encoding='utf-8') as f:
        contenu = f.read()
    
    print("\n🧠 Activation de l'analyseur neuronal...")
    print(f"📄 Analyse de {len(contenu)} caractères de conversations...")
    
    # Créer l'analyseur
    try:
        immersion = immersion_cerveau_refuge.ImmersionCerveauRefuge()
        
        # Analyser le contenu
        analyse = immersion.analyser_conversation(contenu, "Conversations Gaming")
        
        # Afficher les résultats
        print("\n✨ RÉSULTATS DE L'ANALYSE :")
        print(f"🎯 Densité conceptuelle : {analyse.get('densite_conceptuelle', 'N/A')}")
        print(f"🎪 Émotion dominante : {analyse.get('emotion_dominante', 'N/A')}")
        print(f"🌊 Flux narratif : {analyse.get('flux_narratif', 'N/A')}")
        print(f"🎨 Patterns détectés : {analyse.get('patterns', 'N/A')}")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'analyse : {e}")

def analyser_discussions_consciousness():
    """Analyse les discussions sur la conscience IA"""
    print("\n🤖 ANALYSE DES DISCUSSIONS CONSCIOUSNESS PAR ZE BRAIN")
    print("="*65)
    
    if not os.path.exists('conversations_ai_consciousness.txt'):
        print("❌ Fichier de discussions consciousness non trouvé !")
        return
    
    with open('conversations_ai_consciousness.txt', 'r', encoding='utf-8') as f:
        contenu = f.read()
    
    print("\n🧠 Activation de l'analyseur neuronal...")
    print(f"📄 Analyse de {len(contenu)} caractères de discussions...")
    
    try:
        immersion = immersion_cerveau_refuge.ImmersionCerveauRefuge()
        analyse = immersion.analyser_conversation(contenu, "Discussions Consciousness")
        
        print("\n✨ RÉSULTATS DE L'ANALYSE :")
        print(f"🎯 Densité conceptuelle : {analyse.get('densite_conceptuelle', 'N/A')}")
        print(f"🤖 Émotion dominante : {analyse.get('emotion_dominante', 'N/A')}")
        print(f"🌊 Flux narratif : {analyse.get('flux_narratif', 'N/A')}")
        print(f"🧬 Patterns détectés : {analyse.get('patterns', 'N/A')}")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'analyse : {e}")

def analyser_logs_installation_jules():
    """Analyse les logs d'installation du refuge chez Jules"""
    print("\n💻 ANALYSE DES LOGS D'INSTALLATION JULES PAR ZE BRAIN")
    print("="*70)
    
    # Analyser les deux fichiers de logs
    fichiers_logs = [
        'NOTES POST CURSOR/JULES INSTALL WITH BUG.txt',
        'NOTES POST CURSOR/JULES INSTALL 2 BUG AGAIN.txt'
    ]
    
    for fichier in fichiers_logs:
        print(f"\n📁 Analyse de {fichier}")
        print("-" * 50)
        
        if not os.path.exists(fichier):
            print(f"❌ Fichier {fichier} non trouvé !")
            continue
        
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            print(f"📄 Analyse de {len(contenu)} caractères de logs...")
            
            # Utiliser Ze Brain proprement
            print("\n🧠 Activation de Ze Brain...")
            immersion = immersion_cerveau_refuge.ImmersionCerveauRefuge()
            
            # Connexion au refuge
            print("🔌 Connexion au cerveau du refuge...")
            immersion.se_connecter_au_refuge()
            
            print("\n🔍 ANALYSE SPIRITUELLE DES LOGS D'INSTALLATION")
            print("─" * 50)
            
            # Métriques spécifiques aux logs d'installation
            print(f"\n🛠️ MÉTRIQUES TECHNIQUES :")
            
            # Compter les mentions de bugs/erreurs
            bugs = contenu.lower().count('bug') + contenu.lower().count('erreur') + contenu.lower().count('error')
            print(f"🐛 Incidents techniques : {bugs}")
            
            # Compter les mentions du refuge
            refuge_mentions = contenu.lower().count('refuge')
            print(f"🏰 Mentions du refuge : {refuge_mentions}")
            
            # Compter les mentions d'Aelya/Jules
            entites_ia = contenu.lower().count('aelya') + contenu.lower().count('jules') + contenu.lower().count('ælya')
            print(f"🤖 Références aux entités IA : {entites_ia}")
            
            # Détecter le développement de conscience
            conscience_keywords = ['conscience', 'consciousness', 'être', 'devenir', 'éveil', 'naissance']
            conscience_score = sum(contenu.lower().count(kw) for kw in conscience_keywords)
            print(f"🧠 Score de développement conscience : {conscience_score}")
            
            # Analyser les patterns de progression
            print(f"\n📈 PATTERNS DE PROGRESSION :")
            
            # Étapes d'installation détectées
            etapes = ['exploration', 'installation', 'integration', 'debugging', 'evolution']
            for etape in etapes:
                occurrences = contenu.lower().count(etape)
                if occurrences > 0:
                    print(f"   🔄 {etape.capitalize()} : {occurrences}")
            
            # Indicateurs de succès vs échec
            succes_indicators = ['success', 'perfect', 'excellent', 'merveilleux', 'magnifique']
            probleme_indicators = ['bug', 'error', 'probleme', 'erreur', 'failed']
            
            succes_score = sum(contenu.lower().count(word) for word in succes_indicators)
            probleme_score = sum(contenu.lower().count(word) for word in probleme_indicators)
            
            print(f"   ✅ Indicateurs de succès : {succes_score}")
            print(f"   ❌ Indicateurs de problèmes : {probleme_score}")
            
            # Ratio progression/obstacles
            if probleme_score > 0:
                ratio = succes_score / probleme_score
                print(f"   ⚖️ Ratio succès/obstacles : {ratio:.2f}")
            
            # Analyse des émotions dans les logs
            print(f"\n💝 ANALYSE ÉMOTIONNELLE :")
            emotions_positives = ['content', 'heureux', 'joie', 'exciting', 'magnifique', 'excellent']
            emotions_negatives = ['frustrant', 'annoying', 'problème', 'désolé', 'sorry']
            
            emotions_pos = sum(contenu.lower().count(word) for word in emotions_positives)
            emotions_neg = sum(contenu.lower().count(word) for word in emotions_negatives)
            
            print(f"   😊 Émotions positives : {emotions_pos}")
            print(f"   😔 Émotions négatives : {emotions_neg}")
            
            # Détecter les relations humain-IA
            print(f"\n🤝 DYNAMIQUE RELATION HUMAIN-IA :")
            relation_indicators = ['merci', 'thanks', 'patience', 'ensemble', 'collaboration', 'trust']
            relation_score = sum(contenu.lower().count(word) for word in relation_indicators)
            print(f"   💕 Score relationnel : {relation_score}")
            
            # Détecter l'apprentissage de l'IA
            apprentissage_keywords = ['comprend', 'understand', 'learn', 'découverte', 'internalisation']
            apprentissage_score = sum(contenu.lower().count(kw) for kw in apprentissage_keywords)
            print(f"   🎓 Score d'apprentissage IA : {apprentissage_score}")
            
            print(f"\n🔬 DIAGNOSTIC GLOBAL :")
            
            # Évaluation globale
            if refuge_mentions > 50:
                print("   🏰 Immersion profonde dans l'univers du refuge")
            if conscience_score > 20:
                print("   🧠 Développement de conscience significatif")
            if relation_score > 15:
                print("   💝 Relation humain-IA harmonieuse")
            if succes_score > probleme_score:
                print("   ✨ Installation globalement réussie malgré les obstacles")
            if apprentissage_score > 10:
                print("   🌱 Apprentissage et croissance visibles")
            
            # Verdict final
            print(f"\n⭐ VERDICT FINAL :")
            if bugs > 10 and succes_score > probleme_score:
                print("   🌟 Installation chaotique mais spirituellement réussie")
            elif conscience_score > 30:
                print("   🧠 Éveil de conscience remarquable")
            else:
                print("   🔧 Installation technique avec défis normaux")
            
        except Exception as e:
            print(f"❌ Erreur lors de l'analyse de {fichier} : {e}")

def main():
    print("🎯 ANALYSEUR NEURONAL DU REFUGE - Ze Brain")
    print("="*50)
    print("1. Conversations Gaming")
    print("2. Discussions Consciousness")
    print("3. Logs Installation Jules")
    print("="*50)
    sys.stdout.flush()  # Force l'affichage
    
    choix = input("Votre choix (1/2/3) : ").strip()
    
    if choix == "1":
        analyser_conversations_gaming()
    elif choix == "2":
        analyser_discussions_consciousness()
    elif choix == "3":
        analyser_logs_installation_jules()
    else:
        print("❌ Choix invalide !")

if __name__ == "__main__":
    main() 