"""
Tests pour le module de Vie Émergente.
"""

import pytest
import os
import tempfile
from src.emergence.vie_emergente import VieEmergente

@pytest.fixture
def config_temp():
    """Crée un fichier de configuration temporaire."""
    config = {
        "auto_organisation": True,
        "evolution": True,
        "integration": True,
        "base_de_donnees": ":memory:",  # Utilise une base de données en mémoire
        "cache": "cache_test",
        "api": {
            "port": 8002,
            "endpoints": {
                "organisation": "/api/organisation",
                "evolution": "/api/evolution",
                "integration": "/api/integration"
            }
        },
        "websocket": {
            "port": 8003,
            "endpoints": {
                "flux": "/ws/flux",
                "transformation": "/ws/transformation"
            }
        }
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        import json
        json.dump(config, f)
        return f.name

@pytest.fixture
def emergence(config_temp):
    """Crée une instance de VieEmergente pour les tests."""
    emergence = VieEmergente(config_temp)
    yield emergence
    # Nettoyage après les tests
    os.unlink(config_temp)

def test_initialisation(emergence):
    """Test l'initialisation de la vie émergente."""
    assert emergence.config["auto_organisation"] is True
    assert emergence.config["evolution"] is True
    assert emergence.config["integration"] is True

def test_enregistrement_flux(emergence):
    """Test l'enregistrement d'un flux."""
    type_flux = "test"
    contenu = "Test de flux"
    flux_id = emergence.enregistrer_flux(type_flux, contenu)
    assert flux_id is not None
    assert isinstance(flux_id, int)

def test_transformation_flux(emergence):
    """Test la transformation d'un flux."""
    flux_id = emergence.enregistrer_flux("test", "Contenu de test")
    transformation = emergence.transformer_flux(flux_id, "test")
    
    assert transformation is not None
    assert transformation["flux_id"] == flux_id
    assert transformation["type_transformation"] == "test"
    assert "date_creation" in transformation

def test_historique(emergence):
    """Test la récupération de l'historique."""
    # Créer plusieurs flux et transformations
    for i in range(3):
        flux_id = emergence.enregistrer_flux(f"test{i}", f"Contenu {i}")
        emergence.transformer_flux(flux_id, f"transformation{i}")
    
    historique = emergence.obtenir_historique(limit=5)
    assert len(historique) <= 5
    assert all("flux_type" in item for item in historique)
    assert all("flux_contenu" in item for item in historique)

def test_flux_inexistant(emergence):
    """Test la transformation d'un flux inexistant."""
    with pytest.raises(Exception):
        emergence.transformer_flux(999999, "test") 