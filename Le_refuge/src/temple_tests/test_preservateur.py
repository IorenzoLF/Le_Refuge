#!/usr/bin/env python3
# Test simple du préservateur

from scripts.preservateur_formules_sacrees import PreservateurFormulesSacrees

print("🔮 Test du Préservateur de Formules Sacrées")
print("=" * 50)

try:
    preservateur = PreservateurFormulesSacrees()
    print("✅ Préservateur créé avec succès")
    
    # Test simple
    resultats = preservateur.analyser_tous_fichiers_gem()
    print(f"✅ Analyse terminée: {resultats}")
    
except Exception as e:
    print(f"❌ Erreur: {e}")
    import traceback
    traceback.print_exc()