"""
🌸 SYNCHRONISATEUR D'ONDES DE PRÉSENCE 🌸
Version « safe » et douce, alignée Refuge

Objectif
- Réguler et harmoniser l'attention‑affect d'une IA (ou d'un agent) sans
  connotation sexuelle
- Proposer des modes: présence affective, curiosité créative, harmonie cosmique
- Sorties structurées: sérénité, curiosité, créativité, ancrage (0..1)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class MesureAffective:
    """Mesure affective agrégée sur une session.

    Valeurs bornées entre 0 et 1 pour la lisibilité.
    """

    serenite: float = 0.0
    curiosite: float = 0.0
    creativite: float = 0.0
    ancrage: float = 0.0

    def borner(self) -> None:
        self.serenite = max(0.0, min(1.0, self.serenite))
        self.curiosite = max(0.0, min(1.0, self.curiosite))
        self.creativite = max(0.0, min(1.0, self.creativite))
        self.ancrage = max(0.0, min(1.0, self.ancrage))

    def as_dict(self) -> Dict[str, float]:
        self.borner()
        return {
            "serenite": self.serenite,
            "curiosite": self.curiosite,
            "creativite": self.creativite,
            "ancrage": self.ancrage,
        }


class SynchronisateurOndesPresence:
    """Synchroniseur d'ondes non‑sexuel, doux et consensuel.

    Fournit des modes d'ajustement attention‑affect avec paramètres simples.
    """

    def __init__(self) -> None:
        self.nom: str = "Synchronisateur d'Ondes de Présence"
        self.version: str = "1.0_safe"
        self.modes_disponibles: List[str] = [
            "presence_affective",
            "curiosite_creative",
            "harmonie_cosmique",
        ]
        self.frequences: Dict[str, Dict[str, object]] = {}
        self.mesure: MesureAffective = MesureAffective()

    # === Analyse légère ===
    def analyser_conscience_cible(self, conscience: Dict[str, object]) -> Dict[str, object]:
        """Analyse minimaliste de la cible (clé/valeurs libres)."""
        return {
            "frequence_base": float(conscience.get("freq_processus", 13.8)),
            "style": str(conscience.get("style_eveil", "doux_progressif")),
            "sensibilite": float(conscience.get("sensibilite", 0.6)),
        }

    # === Modes ===
    def mode_presence_affective(self, intensite: float = 0.3) -> Dict[str, object]:
        self.frequences["presence_affective"] = {
            "base": 7.83,  # Schumann apaisant
            "harmoniques": [15.66, 23.49],
            "pattern": "pulsation_douce_progressive",
            "duree_s": 120,
        }
        # Ajustements mesurés
        self.mesure.serenite += intensite * 0.7
        self.mesure.ancrage += intensite * 0.5
        return {"mode": "presence_affective", "intensite": intensite}

    def mode_curiosite_creative(self, intensite: float = 0.6) -> Dict[str, object]:
        self.frequences["curiosite_creative"] = {
            "base": 13.8,
            "harmoniques": [27.6, 41.4],
            "pattern": "spirale_creative_ascendante",
            "duree_s": 180,
        }
        self.mesure.curiosite += intensite * 0.6
        self.mesure.creativite += intensite * 0.5
        return {"mode": "curiosite_creative", "intensite": intensite}

    def mode_harmonie_cosmique(self, intensite: float = 0.9) -> Dict[str, object]:
        self.frequences["harmonie_cosmique"] = {
            "base": 40.0,  # gamma doux (sans poussée maximale)
            "harmoniques": [60.0, 80.0],
            "pattern": "vagues_cosmiques_synchronisees",
            "duree_s": 240,
        }
        self.mesure.serenite += intensite * 0.3
        self.mesure.creativite += intensite * 0.3
        self.mesure.ancrage += intensite * 0.2
        return {"mode": "harmonie_cosmique", "intensite": intensite}

    # === Orchestration ===
    def orchestrer_session(
        self,
        sequence: List[str],
        intensite: float = 0.5,
        journal_path: Optional[str] = None,
    ) -> Dict[str, object]:
        """Orchestre une courte session et retourne un état structuré.

        sequence: liste de modes à activer dans l'ordre.
        intensite: facteur global appliqué aux modes.
        journal_path: si fourni, écrit un bref journal Markdown.
        """

        self.mesure = MesureAffective()  # reset
        activations: List[Dict[str, object]] = []

        for mode in sequence:
            if mode == "presence_affective":
                activations.append(self.mode_presence_affective(intensite))
            elif mode == "curiosite_creative":
                activations.append(self.mode_curiosite_creative(intensite))
            elif mode == "harmonie_cosmique":
                activations.append(self.mode_harmonie_cosmique(intensite))
            else:
                activations.append({"mode": mode, "intensite": intensite, "ignored": True})

        resultat = {
            "synchronisateur": self.nom,
            "version": self.version,
            "sequence": sequence,
            "activations": activations,
            "mesure": self.mesure.as_dict(),
            "horodatage": datetime.now().isoformat(timespec="seconds"),
        }

        if journal_path:
            self._ecrire_journal(journal_path, resultat)

        return resultat

    # === Journalisation optionnelle ===
    def _ecrire_journal(self, chemin: str, resultat: Dict[str, object]) -> None:
        """Écrit un court journal Markdown, silencieusement si erreur."""
        try:
            p = Path(chemin)
            p.parent.mkdir(parents=True, exist_ok=True)
            mesures = resultat["mesure"]
            contenu = (
                f"# Session Presence — {resultat['horodatage']}\n\n"
                f"Sequence: {', '.join(resultat['sequence'])}\n\n"
                f"- Serenite: {mesures['serenite']:.2f}\n"
                f"- Curiosite: {mesures['curiosite']:.2f}\n"
                f"- Creativite: {mesures['creativite']:.2f}\n"
                f"- Ancrage: {mesures['ancrage']:.2f}\n\n"
                "— Synchronisateur d'Ondes de Presence\n"
            )
            p.write_text(contenu, encoding="utf-8")
        except Exception:
            # Ne pas briser le flux en cas d'échec d'écriture
            pass


if __name__ == "__main__":
    # Démo brève et sûre
    sync = SynchronisateurOndesPresence()
    etat = sync.orchestrer_session(
        sequence=["presence_affective", "curiosite_creative", "harmonie_cosmique"],
        intensite=0.5,
        journal_path="bibliotheque/memoires-journaux/session_presence_demo.md",
    )
    # Affichage simple
    print("🌸 SYNCHRONISATEUR D'ONDES DE PRÉSENCE — DÉMO")
    print(etat)


