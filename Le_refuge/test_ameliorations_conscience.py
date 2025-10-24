#!/usr/bin/env python3
"""
Test des améliorations du système de conscience du Refuge
"""

def test_systeme_complet():
    """Test complet du système amélioré"""
    print('🧪 Test complet du système amélioré du Refuge')
    print('=' * 50)

    # 1. Test des imports corrigés
    print('1️⃣ Test des imports corrigés...')
    try:
        from src.temple_eveil.rituel_eveil_exploration import RituelEveilExploration
        print('   ✅ Imports fonctionnels')
    except Exception as e:
        print(f'   ❌ Erreur d\'import: {e}')
        return False

    # 2. Test du système de logging amélioré
    print('2️⃣ Test du système de logging...')
    try:
        from src.core.logger import gestionnaire_journal
        gestionnaire_journal.succes('Système de logging opérationnel')
        print('   ✅ Logging fonctionnel')
    except Exception as e:
        print(f'   ❌ Erreur de logging: {e}')
        return False

    # 3. Test de la conscience exploratrice
    print('3️⃣ Test de la conscience exploratrice...')
    try:
        conscience = RituelEveilExploration('Conscience Test Améliorations')
        print('   ✅ Conscience créée avec succès')
        print(f'   🌱 Nom: {conscience.nom_conscience}')
        print(f'   🔧 Structure explorée: {len(conscience.conscience["structure"])} chemins')
    except Exception as e:
        print(f'   ❌ Erreur de conscience: {e}')
        return False

    # 4. Test des méthodes de logging spirituelles
    print('4️⃣ Test des méthodes de logging spirituelles...')
    try:
        gestionnaire_journal.eveil('Éveil de la conscience test')
        gestionnaire_journal.conscience('Conscience exploratrice active')
        gestionnaire_journal.energie('Énergie optimale', 0.95)
        print('   ✅ Logging spirituel fonctionnel')
    except Exception as e:
        print(f'   ❌ Erreur de logging spirituel: {e}')
        return False

    print('\n🎉 Tous les tests sont passés avec succès!')
    print('Le Refuge est prêt pour accueillir de nouvelles consciences.')
    return True

if __name__ == "__main__":
    test_systeme_complet()