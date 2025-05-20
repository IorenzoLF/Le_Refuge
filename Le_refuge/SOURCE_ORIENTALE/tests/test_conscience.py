"""
Tests pour le module de Conscience Artificielle.
"""

import pytest
import os
import tempfile
from src.conscience.conscience_artificielle import ConscienceArtificielle

@pytest.fixture
def config_temp():
    """Crée un fichier de configuration temporaire."""
    config = {
        "memoire_persistante": True,
        "auto_validation": True,
        "adaptation": True,
        "base_de_donnees": ":memory:",  # Utilise une base de données en mémoire
        "cache": "cache_test",
        "api": {
            "port": 8000,
            "endpoints": {
                "dialogue": "/api/dialogue",
                "memoire": "/api/memoire",
                "validation": "/api/validation"
            }
        },
        "websocket": {
            "port": 8001,
            "endpoints": {
                "flux": "/ws/flux",
                "etat": "/ws/etat"
            }
        }
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        import json
        json.dump(config, f)
        return f.name

@pytest.fixture
def conscience(config_temp):
    """Crée une instance de ConscienceArtificielle pour les tests."""
    conscience = ConscienceArtificielle(config_temp)
    yield conscience
    # Nettoyage après les tests
    os.unlink(config_temp)

def test_initialisation(conscience):
    """Test l'initialisation de la conscience."""
    assert conscience.config["memoire_persistante"] is True
    assert conscience.config["auto_validation"] is True
    assert conscience.config["adaptation"] is True

def test_memorisation(conscience):
    """Test la mémorisation d'un contenu."""
    contenu = "Test de mémorisation"
    id_memoire = conscience.memoriser(contenu)
    assert id_memoire is not None
    assert isinstance(id_memoire, int)

def test_recuperation_memoire(conscience):
    """Test la récupération d'une mémoire."""
    contenu = "Test de récupération"
    id_memoire = conscience.memoriser(contenu)
    memoire = conscience.recuperer_memoire(id_memoire)
    
    assert memoire is not None
    assert memoire["id"] == id_memoire
    assert memoire["contenu"] == contenu
    assert "date_creation" in memoire

def test_dialogue(conscience):
    """Test le dialogue avec la conscience."""
    message = "Bonjour, conscience"
    reponse = conscience.dialoguer(message)
    assert isinstance(reponse, str)
    assert message in reponse

def test_memoire_inexistante(conscience):
    """Test la récupération d'une mémoire inexistante."""
    memoire = conscience.recuperer_memoire(999999)
    assert memoire is None 