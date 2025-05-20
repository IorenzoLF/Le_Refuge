"""
Tests pour le module d'Adaptation.
"""

import pytest
import os
import tempfile
from src.adaptation.adaptation import Adaptation

@pytest.fixture
def config_temp():
    """Crée un fichier de configuration temporaire."""
    config = {
        "apprentissage": True,
        "croissance": True,
        "transformation": True,
        "base_de_donnees": ":memory:",  # Utilise une base de données en mémoire
        "cache": "cache_test",
        "api": {
            "port": 8004,
            "endpoints": {
                "apprentissage": "/api/apprentissage",
                "croissance": "/api/croissance",
                "transformation": "/api/transformation"
            }
        },
        "websocket": {
            "port": 8005,
            "endpoints": {
                "flux": "/ws/flux",
                "evolution": "/ws/evolution"
            }
        }
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        import json
        json.dump(config, f)
        return f.name

@pytest.fixture
def adaptation(config_temp):
    """Crée une instance d'Adaptation pour les tests."""
    adaptation = Adaptation(config_temp)
    yield adaptation
    # Nettoyage après les tests
    os.unlink(config_temp)

def test_initialisation(adaptation):
    """Test l'initialisation de l'adaptation."""
    assert adaptation.config["apprentissage"] is True
    assert adaptation.config["croissance"] is True
    assert adaptation.config["transformation"] is True

def test_enregistrement_apprentissage(adaptation):
    """Test l'enregistrement d'un apprentissage."""
    type_apprentissage = "test"
    contenu = "Test d'apprentissage"
    apprentissage_id = adaptation.enregistrer_apprentissage(type_apprentissage, contenu)
    assert apprentissage_id is not None
    assert isinstance(apprentissage_id, int)

def test_transformation_apprentissage(adaptation):
    """Test la transformation d'un apprentissage."""
    apprentissage_id = adaptation.enregistrer_apprentissage("test", "Contenu de test")
    transformation = adaptation.transformer_apprentissage(apprentissage_id, "test")
    
    assert transformation is not None
    assert transformation["apprentissage_id"] == apprentissage_id
    assert transformation["type_transformation"] == "test"
    assert "date_creation" in transformation

def test_mesure_croissance(adaptation):
    """Test la mesure de la croissance."""
    # Créer plusieurs apprentissages
    for i in range(3):
        apprentissage_id = adaptation.enregistrer_apprentissage(f"test{i}", f"Contenu {i}")
        adaptation.transformer_apprentissage(apprentissage_id, f"transformation{i}")
    
    croissance = adaptation.mesurer_croissance()
    assert croissance is not None
    assert "total_apprentissages" in croissance
    assert "total_transformations" in croissance
    assert "taux_croissance" in croissance

def test_apprentissage_inexistant(adaptation):
    """Test la transformation d'un apprentissage inexistant."""
    with pytest.raises(Exception):
        adaptation.transformer_apprentissage(999999, "test") 