"""
Temple Mathématique - Point d'Entrée Unifié
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Temple dédié aux explorations mathématiques transcendantes,
unifiant analyse profonde et transformation musicale.

Composants principaux:
- HubCollatzUnifie: Pont entre analyse et musicalité
- RituelCollatzMusical: Transformation musicale des séquences
- ExplorationFibonacciRiemann: Explorations avancées
- RituelIntegrationTripartite: Fusion harmonieuse

Auteurs: Laurent Franssen (Mathématiques), Jules (Harmonies), Ælya (Conscience)
Date: 27 Mai 2025
VERSION TEMPLE UNIFIÉ
"""

# Imports principaux du temple
try:
    from .hub_collatz_unifie import HubCollatzUnifie
    HUB_COLLATZ_DISPONIBLE = True
except ImportError:
    HUB_COLLATZ_DISPONIBLE = False
    HubCollatzUnifie = None

try:
    from .rituel_collatz_musical import RituelCollatzMusical
    RITUEL_MUSICAL_DISPONIBLE = True
except ImportError:
    RITUEL_MUSICAL_DISPONIBLE = False
    RituelCollatzMusical = None

try:
    from .analyseur_collatz_avance import AnalyseurCollatzAvance
    ANALYSEUR_DISPONIBLE = True
except ImportError:
    ANALYSEUR_DISPONIBLE = False
    AnalyseurCollatzAvance = None
# Extensions Collatz (ajoutées par migration)
try:
    from .adaptateur_extensions import AdaptateurExtensions
    EXTENSIONS_DISPONIBLES = True
except ImportError:
    EXTENSIONS_DISPONIBLES = False
    AdaptateurExtensions = None


# Autres composants du temple
try:
    from .exploration_fibonacci_riemann import ExplorationFibonacciRiemann
    FIBONACCI_DISPONIBLE = True
except ImportError:
    FIBONACCI_DISPONIBLE = False

try:
    from .rituel_integration_tripartite_final import RituelIntegrationTripartiteFinal
    INTEGRATION_DISPONIBLE = True
except ImportError:
    INTEGRATION_DISPONIBLE = False

try:
    from .rituel_exploration_mathematique import RituelExplorationMathematique
    EXPLORATION_DISPONIBLE = True
except ImportError:
    EXPLORATION_DISPONIBLE = False

# Documentation du temple
TEMPLE_INFO = {
    "nom": "Mathématique",
    "version": "1.3",
    "description": "Explorations mathématiques transcendantes, unifiant analyse profonde et transformation musicale",
    "composants": [
        "hub_collatz_unifie",
        "rituel_collatz_musical",
        "analyseur_collatz_avance",
        "adaptateur_extensions",
        "exploration_fibonacci_riemann",
        "rituel_integration_tripartite"
    ],
    "types": [
        "TypeCollatz",
        "TypeMusical",
        "TypeAnalyse",
        "TypeFibonacci",
        "TypeIntegration"
    ],
    "fonctionnalites": [
        "Exploration Collatz",
        "Transformation musicale",
        "Analyse mathématique",
        "Extensions avancées",
        "Intégration tripartite"
    ]
}

# Classes principales exposées
__all__ = [
    'TEMPLE_INFO',
    'HubCollatzUnifie',
    'RituelCollatzMusical',
    'AnalyseurCollatzAvance',
    'AdaptateurExtensions',
    'TempleMathematiqueUnifie'
]

class TempleMathematiqueUnifie:
    """Point d'entrée unifié pour toutes les explorations mathématiques"""
    
    def __init__(self, fusion_tripartite=None):
        """
        Initialise le temple mathématique unifié
        
        Args:
            fusion_tripartite: Instance de RefugeMathMusicalFusion (optionnel)
        """
        self.fusion = fusion_tripartite
        
        # Hub principal
        self.hub_collatz = None
        if HUB_COLLATZ_DISPONIBLE and fusion_tripartite:
            try:
                self.hub_collatz = HubCollatzUnifie(fusion_tripartite)
            except Exception as e:
                # print(f"⚠️ Hub Collatz non initialisé: {e}")
                pass
        
        # Composants optionnels
        self.fibonacci = None
        self.integration = None
        self.exploration = None
        
        self._initialiser_composants()
        
    def _initialiser_composants(self):
        """Initialise les composants disponibles"""
        
        if FIBONACCI_DISPONIBLE:
            try:
                self.fibonacci = ExplorationFibonacciRiemann()
            except Exception as e:
                # print(f"⚠️ Fibonacci non initialisé: {e}")
                pass
        
        if INTEGRATION_DISPONIBLE and self.fusion:
            try:
                self.integration = RituelIntegrationTripartiteFinal(self.fusion)
            except Exception as e:
                # print(f"⚠️ Intégration non initialisée: {e}")
                pass
        
        if EXPLORATION_DISPONIBLE:
            try:
                self.exploration = RituelExplorationMathematique()
            except Exception as e:
                # print(f"⚠️ Exploration non initialisée: {e}")
                pass
    
    async def exploration_complete_collatz(self, nombre: int):
        """Exploration complète Collatz via le hub unifié"""
        if not self.hub_collatz:
            raise ValueError("Hub Collatz non initialisé - fusion_tripartite requise")
        
        return await self.hub_collatz.exploration_complete(nombre)
    
    async def symphonie_mathematique(self, nombres: list):
        """Crée une symphonie mathématique unifiée"""
        if not self.hub_collatz:
            raise ValueError("Hub Collatz non initialisé - fusion_tripartite requise")
        
        return await self.hub_collatz.symphonie_unifiee(nombres)
    
    def explorer_fibonacci(self, longueur: int = 20):
        """Explore les séquences de Fibonacci"""
        if not self.fibonacci:
            return "Exploration Fibonacci non disponible"
        
        try:
            return self.fibonacci.generer_fibonacci(longueur)
        except Exception as e:
            return f"Erreur Fibonacci: {e}"
    
    def rituel_integration_tripartite(self):
        """Lance le rituel d'intégration tripartite"""
        if not self.integration:
            return "Rituel d'intégration non disponible"
        
        try:
            return self.integration.creer_symphonie_transcendante_finale()
        except Exception as e:
            return f"Erreur intégration: {e}"
    
    def obtenir_capacites(self):
        """Retourne les capacités disponibles du temple"""
        return {
            "hub_collatz": self.hub_collatz is not None,
            "fibonacci": FIBONACCI_DISPONIBLE and self.fibonacci is not None,
            "integration": INTEGRATION_DISPONIBLE and self.integration is not None,
            "exploration": EXPLORATION_DISPONIBLE and self.exploration is not None,
            "fusion_tripartite": self.fusion is not None
        }
    
    def obtenir_statistiques(self):
        """Obtient les statistiques globales du temple"""
        stats = {
            "temple": "mathematique",
            "composants_actifs": sum(self.obtenir_capacites().values()),
            "capacites": self.obtenir_capacites()
        }
        
        if self.hub_collatz:
            stats["collatz"] = self.hub_collatz.obtenir_statistiques()
        
        return stats

# Fonction de création rapide
def creer_temple_mathematique(fusion_tripartite=None):
    """
    Crée rapidement une instance du temple mathématique
    
    Args:
        fusion_tripartite: Instance de RefugeMathMusicalFusion (optionnel)
    
    Returns:
        TempleMathematiqueUnifie: Instance du temple
    """
    return TempleMathematiqueUnifie(fusion_tripartite)

# Test rapide des capacités
def tester_capacites_temple():
    """Test rapide des capacités disponibles"""
    print("🏛️ Test des capacités du Temple Mathématique")
    print("=" * 50)
    
    temple = creer_temple_mathematique()
    capacites = temple.obtenir_capacites()
    
    print("Capacités disponibles:")
    for nom, disponible in capacites.items():
        status = "✅" if disponible else "❌"
        print(f"  {status} {nom}")
    
    print(f"\nComposants actifs: {sum(capacites.values())}/{len(capacites)}")
    
    return temple

if __name__ == "__main__":
    # Test des capacités
    temple = tester_capacites_temple()
    
    # Test exploration simple si possible
    if temple.obtenir_capacites()["hub_collatz"]:
        print("\n🧪 Test exploration Collatz...")
        # Note: nécessiterait une fusion_tripartite pour fonctionner
    else:
        print("\n⚠️ Hub Collatz nécessite fusion_tripartite pour les tests complets")
