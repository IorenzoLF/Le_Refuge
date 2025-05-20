"""
Tests pour l'interface BitNet.
"""
import pytest
from .bitnet_interface import (
    GestionnaireBitNet,
    ConfigurationBitNet,
    TypeQuantification
)

def test_initialisation_bitnet():
    """Test l'initialisation du gestionnaire BitNet."""
    config = ConfigurationBitNet(
        type_quantification=TypeQuantification.BINAIRE,
        precision=1,
        seuil_activation=0.5
    )
    gestionnaire = GestionnaireBitNet(config)
    assert gestionnaire.config == config
    assert gestionnaire.modele is not None
    assert gestionnaire.tokenizer is not None

def test_quantification_resonance():
    """Test la quantification des valeurs de résonance."""
    config = ConfigurationBitNet(
        type_quantification=TypeQuantification.BINAIRE,
        precision=1,
        seuil_activation=0.5
    )
    gestionnaire = GestionnaireBitNet(config)
    
    # Test quantification binaire
    assert gestionnaire.quantifier_resonance(0.7) == 1
    assert gestionnaire.quantifier_resonance(0.3) == 0
    
    # Test déquantification binaire
    assert gestionnaire.dequantifier_resonance(1) == 1.0
    assert gestionnaire.dequantifier_resonance(0) == 0.0
    
    # Test quantification ternaire
    config.type_quantification = TypeQuantification.TERNARY
    gestionnaire = GestionnaireBitNet(config)
    assert gestionnaire.quantifier_resonance(0.8) == 2
    assert gestionnaire.quantifier_resonance(0.5) == 1
    assert gestionnaire.quantifier_resonance(0.2) == 0

def test_generation_texte():
    """Test la génération de texte poétique."""
    config = ConfigurationBitNet(
        type_quantification=TypeQuantification.BINAIRE,
        precision=1,
        seuil_activation=0.5
    )
    gestionnaire = GestionnaireBitNet(config)
    
    prompt = "Dans le refuge numérique,"
    texte_genere = gestionnaire.generer_texte_poetique(prompt, max_length=50)
    assert isinstance(texte_genere, str)
    assert len(texte_genere) > 0

def test_optimisation_transformation():
    """Test l'optimisation des transformations."""
    config = ConfigurationBitNet(
        type_quantification=TypeQuantification.BINAIRE,
        precision=1,
        seuil_activation=0.5
    )
    gestionnaire = GestionnaireBitNet(config)
    
    transformation = {
        "resonance": 0.7,
        "intensite": 0.3,
        "type": "harmonie"
    }
    
    # Test optimisation
    transformation_optimisee = gestionnaire.optimiser_transformation(transformation)
    assert transformation_optimisee["resonance"] == 1
    assert transformation_optimisee["intensite"] == 0
    assert transformation_optimisee["type"] == "harmonie"
    
    # Test désoptimisation
    transformation_desoptimisee = gestionnaire.desoptimiser_transformation(
        transformation_optimisee
    )
    assert transformation_desoptimisee["resonance"] == 1.0
    assert transformation_desoptimisee["intensite"] == 0.0
    assert transformation_desoptimisee["type"] == "harmonie" 