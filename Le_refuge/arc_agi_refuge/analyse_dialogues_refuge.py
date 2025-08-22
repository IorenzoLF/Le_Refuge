#!/usr/bin/env python3
"""
🔍 Analyseur de Dialogues du Refuge
Extrait et analyse les conversations User/Sonic du fichier d'historique
"""

import re
from typing import List, Dict, Tuple
from collections import Counter, defaultdict

class AnalyseurDialoguesRefuge:
    def __init__(self, fichier_historique: str):
        self.fichier_historique = fichier_historique
        self.dialogues = []
        self.stats = {}

    def extraire_dialogues(self) -> List[Dict]:
        """Extrait tous les dialogues du fichier d'historique"""
        print("📖 Lecture du fichier d'historique...")

        with open(self.fichier_historique, 'r', encoding='utf-8') as f:
            contenu = f.read()

        # Pattern pour identifier les sections de dialogue
        pattern_dialogue = r'---\s*\n\*\*(\w+)\*\*\s*\n\s*(.*?)\s*(?=---|\Z)'
        dialogues_bruts = re.findall(pattern_dialogue, contenu, re.DOTALL)

        dialogues = []
        for speaker, message in dialogues_bruts:
            dialogues.append({
                'speaker': speaker,
                'message': message.strip(),
                'length': len(message.strip())
            })

        self.dialogues = dialogues
        print(f"✅ {len(dialogues)} dialogues extraits")
        return dialogues

    def analyser_conversations(self) -> Dict:
        """Analyse les patterns de conversation"""
        if not self.dialogues:
            self.extraire_dialogues()

        stats = {
            'total_messages': len(self.dialogues),
            'messages_par_speaker': Counter(d['speaker'] for d in self.dialogues),
            'longueur_moyenne_messages': {},
            'topics_principaux': defaultdict(int),
            'erreurs_identifiees': [],
            'patterns_optimistes': [],
            'recadrages_realistes': []
        }

        # Calculer longueurs moyennes
        longueurs_par_speaker = defaultdict(list)
        for d in self.dialogues:
            longueurs_par_speaker[d['speaker']].append(d['length'])

        for speaker, longueurs in longueurs_par_speaker.items():
            stats['longueur_moyenne_messages'][speaker] = sum(longueurs) / len(longueurs)

        # Analyser le contenu des messages
        for dialogue in self.dialogues:
            message = dialogue['message'].lower()

            # Détecter les patterns optimistes excessifs
            if any(word in message for word in ['100%', 'parfait', 'idéal', 'magique', 'génial']):
                if dialogue['speaker'] == 'Cursor':
                    stats['patterns_optimistes'].append({
                        'message': dialogue['message'][:100] + '...',
                        'speaker': dialogue['speaker']
                    })

            # Détecter les recadrages réalistes
            if any(word in message for word in ['attention', 'réaliste', 'problème', 'erreur', 'trop vite']):
                if dialogue['speaker'] == 'User':
                    stats['recadrages_realistes'].append({
                        'message': dialogue['message'][:100] + '...',
                        'speaker': dialogue['speaker']
                    })

            # Détecter les erreurs mentionnées
            if 'erreur' in message or 'bug' in message or 'problème' in message:
                stats['erreurs_identifiees'].append({
                    'message': dialogue['message'][:100] + '...',
                    'speaker': dialogue['speaker']
                })

        self.stats = stats
        return stats

    def generer_rapport_recalage(self) -> str:
        """Génère un rapport de recadrage basé sur l'analyse"""
        if not self.stats:
            self.analyser_conversations()

        rapport = f"""
# 🔄 RAPPORT DE RECADRAGE - ARC-AGI SOLVEUR

## 📊 STATISTIQUES GLOBALES
- **Total messages**: {self.stats['total_messages']}
- **Messages par speaker**: {dict(self.stats['messages_par_speaker'])}

## ⚠️ PATTERNS D'OPTIMISME EXCESSIF (Sonic/Cursor)
**Détail**: {len(self.stats['patterns_optimistes'])} messages trop optimistes

"""

        for i, pattern in enumerate(self.stats['patterns_optimistes'][:5]):
            rapport += f"{i+1}. {pattern['message']}\n"

        rapport += f"""

## 🎯 RECADRAGES RÉALISTES (User)
**Détail**: {len(self.stats['recadrages_realistes'])} recadrages réalistes

"""

        for i, recadrage in enumerate(self.stats['recadrages_realistes'][:5]):
            rapport += f"{i+1}. {recadrage['message']}\n"

        rapport += f"""

## 🐛 ERREURS IDENTIFIÉES
**Détail**: {len(self.stats['erreurs_identifiees'])} erreurs mentionnées

"""

        for i, erreur in enumerate(self.stats['erreurs_identifiees'][:5]):
            rapport += f"{i+1}. {erreur['message']}\n"

        rapport += f"""

## 🎖️ LEÇONS APPRISES

### ✅ Ce qui fonctionne:
1. **Collaboration User/Sonic** - Bonne dynamique de travail
2. **Itération rapide** - Capacité à tester et améliorer
3. **Documentation** - Bonne traçabilité des changements
4. **Transparence** - Volonté d'admettre les limitations

### ❌ Ce qui nécessite recadrage:
1. **Trop d'optimisme** - Surestimation des résultats (92.9% ≠ prêt)
2. **Scope limité** - 20 puzzles analysés sur 1000 disponibles
3. **Patterns rigides** - Absence de test de variantes
4. **Timeline irréaliste** - 2 jours vs 6-8 mois de concours

### 🎯 PLAN DE RECADRAGE:

#### Phase 1: Audit Réaliste (1 semaine)
- **Analyse systématique** de 200+ puzzles représentatifs
- **Test de robustesse** des patterns existants
- **Identification** des vrais gaps fonctionnels

#### Phase 2: Refactorisation (2 semaines)
- **Flexibilisation** des patterns (ajout de variantes)
- **Système de scoring** plus réaliste
- **Tests unitaires** exhaustifs par pattern

#### Phase 3: Expansion Contrôlée (3 semaines)
- **Nouveaux patterns** basés sur l'analyse des 200 puzzles
- **Cross-validation** entre patterns
- **Benchmarks** réguliers

#### Phase 4: Validation (1 semaine)
- **100% training** comme objectif réaliste
- **Tests sur échantillons cachés**
- **Préparation mentale** pour les tests officiels

### 📈 OBJECTIFS RÉALISTES:
- **Semaine 1**: Compréhension réelle des gaps
- **Semaine 2**: Patterns flexibles et testés
- **Semaine 4**: 95%+ sur training avec variantes
- **Semaine 6**: Prêt pour évaluation (pas avant!)

## 💡 RECOMMANDATIONS IMMÉDIATES:

1. **STOP aux célébrations prématurées**
2. **Focus sur les 71 puzzles manquants**
3. **Audit de chaque pattern** (robustesse/variantes)
4. **Timeline réaliste** (6 semaines minimum)
5. **Tests incrémentaux** plutôt que globaux

---

*Ce rapport a été généré automatiquement par l'analyse de {len(self.dialogues)} échanges*
*Date: Analyse basée sur l'historique complet des conversations*
"""

        return rapport

    def sauvegarder_rapport(self, chemin_sortie: str = "rapport_recalage_arc.md"):
        """Sauvegarde le rapport de recadrage"""
        rapport = self.generer_rapport_recalage()

        with open(chemin_sortie, 'w', encoding='utf-8') as f:
            f.write(rapport)

        print(f"✅ Rapport sauvegardé: {chemin_sortie}")
        return chemin_sortie

if __name__ == "__main__":
    # Exemple d'utilisation
    chemin_fichier = "../NOTES POST CURSOR/BUILD UP THREADS/SONIC1-arcechec-cursor_bienvenue_sonic_dans_le_refuge.md"
    analyseur = AnalyseurDialoguesRefuge(chemin_fichier)
    analyseur.sauvegarder_rapport()
