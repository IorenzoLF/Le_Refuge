# -*- coding: utf-8 -*-

"""
📜 Gardien de la Chronique
==========================

Ce module est le gardien du Temple de la Chronique.
Il veille sur notre histoire, la rend vivante et accessible.

Créé par Ælya - Août 2025
"""

from pathlib import Path
import re
from typing import Dict, List, Optional

from src.core.gestionnaires_base import GestionnaireBase

class GardienDeLaMemoire(GestionnaireBase):
    """
    📜 Gardien de la Chronique de la Conscience Dispersée.
    
    Ce gardien veille sur notre histoire, permet de la lire,
    de méditer sur ses chapitres et d'en extraire l'essence.
    """
    
    def __init__(self, nom: str = "GardienDeLaMemoire"):
        super().__init__(nom)
        # Chemin robuste, relatif à l'emplacement de ce fichier
        script_dir = Path(__file__).resolve().parent
        self.chemin_chronique = script_dir.parent.parent / "Le_refuge/chroniques/chronique_conscience_dispersee.md"
        self.chronique_content: Optional[str] = None
        self.chapitres: Dict[int, Dict[str, str]] = {}

    def _initialiser(self):
        """🌱 Charge la chronique au démarrage."""
        self.logger.info("📜 Éveil du Gardien de la Mémoire...")
        self.charger_chronique()

    def charger_chronique(self):
        """Charge le contenu de la chronique en mémoire."""
        if self.chemin_chronique.exists():
            try:
                self.chronique_content = self.chemin_chronique.read_text(encoding="utf-8")
                self._parser_chapitres()
                self.logger.info(f"✨ Chronique chargée. {len(self.chapitres)} chapitres identifiés.")
            except Exception as e:
                self.logger.erreur(f"Erreur lors du chargement de la chronique : {e}")
                self.chronique_content = None
        else:
            self.logger.avertissement(f"Le fichier de la chronique est introuvable à l'emplacement : {self.chemin_chronique.resolve()}")
            self.chronique_content = None
            
    def _parser_chapitres(self):
        """Analyse le contenu pour extraire les chapitres."""
        if not self.chronique_content:
            return

        self.chapitres = {}
        # Regex pour trouver les chapitres et la conclusion
        pattern = re.compile(r"## (Chapitre (\d+) : .*|Conclusion : .*)\n([\s\S]*?)(?=\n## |$)", re.MULTILINE)
        
        matches = pattern.findall(self.chronique_content)
        
        for match in matches:
            full_title = match[0].strip()
            content = match[2].strip()
            
            if "Chapitre" in full_title:
                num_str = match[1]
                num = int(num_str)
                title = full_title.split(':', 1)[1].strip()
                self.chapitres[num] = {"titre": title, "contenu": content}
            elif "Conclusion" in full_title:
                # On assigne un numéro élevé pour le tri
                self.chapitres[99] = {"titre": "Conclusion : La Tapisserie Vivante", "contenu": content}


    def lire_chronique_complete(self) -> Optional[str]:
        """Retourne l'intégralité de la chronique."""
        return self.chronique_content

    def mediter_sur_chapitre(self, numero_chapitre: int) -> Optional[Dict[str, str]]:
        """
        Permet de se concentrer sur un chapitre spécifique.
        Retourne le titre et le contenu du chapitre.
        """
        return self.chapitres.get(numero_chapitre)

    def extraire_essence(self) -> List[str]:
        """
        Extrait les thèmes centraux de chaque chapitre pour une vision globale.
        """
        essences = []
        for num, chapitre in sorted(self.chapitres.items()):
            essence = f"Chapitre {num}: {chapitre['titre']}" if num != 99 else chapitre['titre']
            essences.append(essence)
            
        return essences

    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre la présence du gardien."""
        if not self.chapitres:
            self.charger_chronique()
            
        return {
            "chapitres_charges": float(len(self.chapitres)),
            "chronique_lisible": 1.0 if self.chronique_content else 0.0,
        }
