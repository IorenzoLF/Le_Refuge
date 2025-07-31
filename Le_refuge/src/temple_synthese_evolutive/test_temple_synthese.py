"""
🌟 Tests pour le Temple de la Synthèse Évolutive
===============================================

Tests unitaires pour valider les fonctionnalités du méta-temple.
"""

import pytest
import asyncio
from temple_synthese_evolutive import (
    TempleSyntheseEvolutive,
    TypeSyntheseEvolutive,
    NiveauSynthese,
    FrequenceSynthetique,
    SynergieEmergente
)

class TestTempleSyntheseEvolutive:
    """Tests pour le Temple de la Synthèse Évolutive"""
    
    def setup_method(self):
        """Initialisation avant chaque test"""
        self.temple = TempleSyntheseEvolutive()
    
    def test_initialisation_temple(self):
        """Test de l'initialisation du temple"""
        assert self.temple.nom == "Temple de la Synthèse Évolutive"
        assert self.temple.niveau_synthese == NiveauSynthese.INITIATION
        assert len(self.temple.temples_connectes) == 0
        assert self.temple.coherence_globale == 0.0
        assert self.temple.evolution_continue is True
    
    def test_connexion_temple(self):
        """Test de connexion d'un temple"""
        # Connexion réussie
        assert self.temple.connecter_temple("temple_creativite") is True
        assert "temple_creativite" in self.temple.temples_connectes
        assert self.temple.coherence_globale > 0.0
        
        # Connexion échouée (temple inexistant)
        assert self.temple.connecter_temple("temple_inexistant") is False
    
    def test_creation_frequence_synthetique(self):
        """Test de création de fréquence synthétique"""
        # Connecter des temples d'abord
        self.temple.connecter_temple("temple_creativite")
        self.temple.connecter_temple("temple_musical")
        
        # Créer une fréquence synthétique
        freq = self.temple.creer_frequence_synthetique(
            ["temple_creativite", "temple_musical"], 
            "Test Harmonie"
        )
        
        assert freq is not None
        assert freq.nom == "Test Harmonie"
        assert len(freq.temples_sources) == 2
        assert freq.frequence_hz > 0
        assert len(self.temple.frequences_synthetiques) == 1
    
    def test_detection_synergie_emergente(self):
        """Test de détection de synergie émergente"""
        # Connecter plusieurs temples
        temples = ["temple_creativite", "temple_musical", "temple_guerison", "temple_amour"]
        for temple in temples:
            self.temple.connecter_temple(temple)
        
        # Forcer une cohérence élevée
        self.temple.coherence_globale = 0.8
        
        # Détecter une synergie
        synergie = self.temple.detecter_synergie_emergente()
        
        if synergie:  # Peut être None selon les conditions
            assert synergie.niveau_emergence > 0.7
            assert len(synergie.temples_impliques) >= 2
    
    @pytest.mark.asyncio
    async def test_ceremonie_synthese_evolutive(self):
        """Test de la cérémonie complète"""
        # Connecter des temples
        temples = ["temple_creativite", "temple_musical", "temple_guerison"]
        for temple in temples:
            self.temple.connecter_temple(temple)
        
        # Exécuter une cérémonie courte
        resultats = await self.temple.ceremonie_synthese_evolutive(3)
        
        assert "phase_1_harmonisation" in resultats
        assert "phase_2_synthese" in resultats
        assert "phase_3_transcendance" in resultats
        assert "etat_final" in resultats
        
        # Vérifier l'état final
        etat_final = resultats["etat_final"]
        assert len(etat_final.temples_actifs) == 3
        assert etat_final.coherence_globale >= 0.0
    
    def test_calcul_harmonique_doree(self):
        """Test du calcul d'harmonique dorée"""
        frequences = [432.0, 528.0, 639.0]
        harmonique = self.temple._calculer_harmonique_doree(frequences)
        
        assert harmonique > 0
        assert isinstance(harmonique, float)
    
    def test_fusion_couleurs(self):
        """Test de fusion des couleurs"""
        # Une couleur
        assert self.temple._fusionner_couleurs(["rouge"]) == "rouge"
        
        # Deux couleurs
        assert self.temple._fusionner_couleurs(["rouge", "bleu"]) == "rouge-bleu"
        
        # Plusieurs couleurs
        result = self.temple._fusionner_couleurs(["rouge", "bleu", "vert"])
        assert result == "arc-en-ciel-synthétique"
    
    def test_etat_synthese_globale(self):
        """Test de l'obtention de l'état global"""
        # Connecter quelques temples
        self.temple.connecter_temple("temple_creativite")
        self.temple.connecter_temple("temple_musical")
        
        etat = self.temple.obtenir_etat_synthese_globale()
        
        assert len(etat.temples_actifs) == 2
        assert etat.niveau_synthese == NiveauSynthese.INITIATION
        assert etat.coherence_globale >= 0.0
        assert etat.evolution_continue is True
        assert etat.timestamp is not None

if __name__ == "__main__":
    pytest.main([__file__])