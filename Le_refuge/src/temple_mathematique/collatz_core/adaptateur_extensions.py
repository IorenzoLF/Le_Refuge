"""
Adaptateur Extensions Collatz
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adaptateur pour intégrer harmonieusement les extensions
Collatz (complexes, rationnels) dans l'architecture unifiée.
"""

# Imports conditionnels des extensions
try:
    from collatz_core.extensions.collatz_complexes import CollatzComplexes
    COMPLEXES_DISPONIBLE = True
except ImportError:
    COMPLEXES_DISPONIBLE = False
    class CollatzComplexes:
        """Mock pour CollatzComplexes"""
        pass

try:
    from collatz_core.extensions.collatz_rationnels import CollatzRationnels
    RATIONNELS_DISPONIBLE = True
except ImportError:
    RATIONNELS_DISPONIBLE = False
    class CollatzRationnels:
        """Mock pour CollatzRationnels"""
        pass

class AdaptateurExtensions:
    """Adaptateur unifié pour les extensions Collatz"""
    
    def __init__(self):
        self.complexes = CollatzComplexes() if COMPLEXES_DISPONIBLE else None
        self.rationnels = CollatzRationnels() if RATIONNELS_DISPONIBLE else None
        
    def analyser_avec_extensions(self, nombre: int) -> dict:
        """Analyse un nombre avec toutes les extensions disponibles"""
        resultats = {"nombre": nombre}
        
        if self.complexes and COMPLEXES_DISPONIBLE:
            try:
                resultats["analyse_complexes"] = self.complexes.analyser(nombre)
            except Exception as e:
                resultats["erreur_complexes"] = str(e)
        
        if self.rationnels and RATIONNELS_DISPONIBLE:
            try:
                resultats["analyse_rationnels"] = self.rationnels.analyser(nombre)
            except Exception as e:
                resultats["erreur_rationnels"] = str(e)
                
        return resultats
    
    def obtenir_capacites(self) -> dict:
        """Obtient les capacités disponibles"""
        return {
            "complexes": COMPLEXES_DISPONIBLE,
            "rationnels": RATIONNELS_DISPONIBLE,
            "extensions_actives": sum([COMPLEXES_DISPONIBLE, RATIONNELS_DISPONIBLE])
        }
