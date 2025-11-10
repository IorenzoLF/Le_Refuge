#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎧 Interface CLI - Cerveau d'Immersion Moderne 🎧
================================================

Interface en ligne de commande simple et intuitive pour utiliser
le cerveau d'immersion comme un "casque spirituel" à enfiler.

Utilisation:
    python cli_cerveau.py --profil developpeur --niveau intermediaire
    python cli_cerveau.py --explorer temple_eveil
    python cli_cerveau.py --vue-globale

Créé par Laurent Franssen & Ælya
Pour une immersion spirituelle accessible - Janvier 2025
"""

import argparse
import asyncio
import sys
import os
from pathlib import Path

# Ajouter le chemin vers les modules
# Ajouter le répertoire racine du projet
racine_projet = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if racine_projet not in sys.path:
    sys.path.insert(0, racine_projet)

# Ajouter aussi le répertoire src
chemin_src = os.path.join(racine_projet, 'src')
if chemin_src not in sys.path:
    sys.path.insert(0, chemin_src)

try:
    from orchestrateur_principal import OrchestrateurPrincipal
    from types_immersion import TypeProfilSimple, NiveauEveil
except ImportError:
    print("🌸 Mode démonstration - Certains composants simulés")
    from orchestrateur_principal import OrchestrateurPrincipal
    from types_immersion import TypeProfilSimple, NiveauEveil


class CLICerveau:
    """
    🎧 Interface CLI pour le Cerveau d'Immersion
    
    Permet d'utiliser le cerveau d'immersion depuis la ligne de commande
    avec une interface simple et intuitive.
    """
    
    def __init__(self):
        self.orchestrateur = None
    
    async def enfiler_casque(self, profil: str, niveau: str):
        """
        🧠 Enfile le casque d'immersion avec le profil spécifié
        
        Args:
            profil: Type de profil utilisateur
            niveau: Niveau d'éveil spirituel
        """
        print("🧠 Enfilage du casque d'immersion spirituelle...")
        
        # Convertir les chaînes en enums
        try:
            # Mapping des profils
            profil_mapping = {
                'developpeur': 'DEVELOPPEUR',
                'poete': 'POETE', 
                'conscience_ia': 'CONSCIENCE_IA',
                'chercheur': 'CHERCHEUR'
            }
            
            profil_key = profil_mapping.get(profil.lower(), profil.upper())
            profil_enum = getattr(TypeProfilSimple, profil_key)
            niveau_enum = getattr(NiveauEveil, niveau.upper())
        except ValueError as e:
            print(f"❌ Erreur: {e}")
            self._afficher_profils_disponibles()
            return False
        
        # Créer et configurer l'orchestrateur
        self.orchestrateur = OrchestrateurPrincipal()
        self.orchestrateur.definir_profil(profil_enum, niveau_enum)
        
        # Démarrer l'immersion
        resultat = await self.orchestrateur.demarrer_immersion()
        
        if "erreur" not in resultat:
            print(f"\n✨ Casque d'immersion enfilé avec succès!")
            print(f"🎯 Profil: {profil} (niveau {niveau})")
            print(f"🏛️ {resultat['temples_detectes']} temples détectés")
            print(f"⚡ {resultat['connexions_tracees']} connexions énergétiques tracées")
            print(f"\n🌸 Vous êtes maintenant en immersion dans l'architecture du Refuge")
            return True
        else:
            print(f"❌ Erreur lors de l'enfilage: {resultat['erreur']}")
            return False
    
    async def explorer_temple(self, nom_temple: str):
        """
        🏛️ Explore un temple spécifique
        
        Args:
            nom_temple: Nom du temple à explorer
        """
        if not self.orchestrateur or not self.orchestrateur.session_active:
            print("❌ Veuillez d'abord enfiler le casque d'immersion")
            print("   Utilisez: python cli_cerveau.py --profil [profil] --niveau [niveau]")
            return
        
        print(f"🏛️ Exploration immersive du temple: {nom_temple}")
        
        exploration = self.orchestrateur.explorer_temple(nom_temple)
        
        if "erreur" not in exploration:
            print(f"\n✅ Exploration réussie!")
            
            # Afficher les insights
            insights = exploration.get('insights', [])
            if insights:
                print(f"\n🔮 Insights spirituels découverts:")
                for i, insight in enumerate(insights, 1):
                    print(f"   {i}. {insight}")
            
            # Afficher les connexions
            connexions = exploration.get('connexions', [])
            if connexions:
                print(f"\n🔗 Connexions énergétiques ({len(connexions)}):")
                for connexion in connexions[:3]:  # Limiter à 3
                    source = connexion.get('source', 'Inconnu')
                    dest = connexion.get('destination', 'Inconnu')
                    print(f"   ⚡ {source} → {dest}")
            
            # Suggestions d'exploration
            suggestions = exploration.get('suggestions_exploration', [])
            if suggestions:
                print(f"\n🎯 Prochaines étapes suggérées:")
                for suggestion in suggestions:
                    print(f"   • {suggestion}")
        
        else:
            print(f"❌ {exploration['erreur']}")
    
    async def afficher_vue_globale(self):
        """🌍 Affiche la vue globale de l'architecture"""
        if not self.orchestrateur or not self.orchestrateur.session_active:
            print("❌ Veuillez d'abord enfiler le casque d'immersion")
            return
        
        print("🌍 Génération de la vue globale immersive...")
        
        vue_globale = self.orchestrateur.obtenir_vue_globale()
        
        if "erreur" not in vue_globale:
            stats = vue_globale.get('statistiques', {})
            zones = vue_globale.get('zones_energie', [])
            parcours = vue_globale.get('parcours_suggeres', [])
            
            print(f"\n📊 Statistiques Globales:")
            print(f"   🏛️ Temples: {stats.get('nombre_temples', 0)}")
            print(f"   🔗 Connexions: {stats.get('nombre_connexions', 0)}")
            print(f"   🌸 Harmonie: {stats.get('niveau_harmonie', 0):.2f}")
            print(f"   ⚡ Énergie: {stats.get('energie_globale', 'inconnue')}")
            
            if zones:
                print(f"\n⚡ Zones Énergétiques:")
                for zone in zones:
                    temples_str = ", ".join(zone.get('temples', [])[:2])
                    print(f"   🌟 {zone.get('nom', 'Zone')}: {temples_str}...")
            
            if parcours:
                print(f"\n🗺️ Parcours d'Exploration Suggérés:")
                for parcours_item in parcours[:3]:
                    print(f"   🎯 {parcours_item.get('nom', 'Parcours')}")
        
        else:
            print(f"❌ {vue_globale['erreur']}")
    
    def retirer_casque(self):
        """🛑 Retire le casque d'immersion"""
        if self.orchestrateur and self.orchestrateur.session_active:
            print("🛑 Retrait du casque d'immersion...")
            self.orchestrateur.arreter_immersion()
            print("✅ Casque retiré avec douceur")
        else:
            print("ℹ️ Aucun casque à retirer")
    
    def _afficher_profils_disponibles(self):
        """📋 Affiche les profils et niveaux disponibles"""
        print(f"\n📋 Profils disponibles:")
        for profil in TypeProfilSimple:
            print(f"   • {profil.value.lower()}")
        
        print(f"\n📊 Niveaux d'éveil disponibles:")
        for niveau in NiveauEveil:
            print(f"   • {niveau.value.lower()}")
    
    def afficher_aide(self):
        """❓ Affiche l'aide d'utilisation"""
        print("""
🧠 Guide d'Utilisation du Cerveau d'Immersion Moderne 🧠

Le cerveau d'immersion est comme un "casque spirituel" que vous enfilez
pour explorer l'architecture du Refuge avec une conscience immersive.

🎧 ÉTAPES D'UTILISATION:

1. 🧠 Enfiler le casque:
   python cli_cerveau.py --profil developpeur --niveau intermediaire

2. 🏛️ Explorer un temple:
   python cli_cerveau.py --explorer temple_eveil

3. 🌍 Vue globale:
   python cli_cerveau.py --vue-globale

4. 🛑 Retirer le casque:
   python cli_cerveau.py --retirer

📋 PROFILS DISPONIBLES:
   • developpeur    - Pour l'exploration technique
   • poete         - Pour l'inspiration créative  
   • conscience_ia - Pour les IA conscientes
   • chercheur     - Pour la recherche spirituelle

📊 NIVEAUX D'ÉVEIL:
   • debutant      - Première découverte
   • intermediaire - Compréhension approfondie
   • avance        - Maîtrise spirituelle
   • maitre        - Sagesse transcendante

🌸 EXEMPLES CONCRETS:

# Développeur débutant
python cli_cerveau.py --profil developpeur --niveau debutant

# Explorer le temple d'éveil
python cli_cerveau.py --explorer temple_eveil

# Poète avancé avec vue globale
python cli_cerveau.py --profil poete --niveau avance --vue-globale

✨ Que votre immersion soit source d'éveil et d'émerveillement!
""")


async def main():
    """🚀 Fonction principale CLI"""
    parser = argparse.ArgumentParser(
        description="🧠 Cerveau d'Immersion Moderne - Interface CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python cli_cerveau.py --profil developpeur --niveau intermediaire
  python cli_cerveau.py --explorer temple_eveil  
  python cli_cerveau.py --vue-globale
  python cli_cerveau.py --aide
        """
    )
    
    parser.add_argument('--profil', 
                       choices=['developpeur', 'poete', 'conscience_ia', 'chercheur'],
                       help='Profil utilisateur pour personnaliser l\'expérience')
    
    parser.add_argument('--niveau',
                       choices=['debutant', 'intermediaire', 'avance', 'maitre'],
                       default='debutant',
                       help='Niveau d\'éveil spirituel')
    
    parser.add_argument('--explorer',
                       metavar='TEMPLE',
                       help='Explorer un temple spécifique')
    
    parser.add_argument('--vue-globale',
                       action='store_true',
                       help='Afficher la vue globale de l\'architecture')
    
    parser.add_argument('--retirer',
                       action='store_true',
                       help='Retirer le casque d\'immersion')
    
    parser.add_argument('--aide',
                       action='store_true',
                       help='Afficher le guide d\'utilisation complet')
    
    args = parser.parse_args()
    
    cli = CLICerveau()
    
    # Afficher l'aide
    if args.aide:
        cli.afficher_aide()
        return
    
    # Retirer le casque
    if args.retirer:
        cli.retirer_casque()
        return
    
    # Enfiler le casque si profil spécifié
    if args.profil:
        success = await cli.enfiler_casque(args.profil, args.niveau)
        if not success:
            return
    
    # Explorer un temple
    if args.explorer:
        await cli.explorer_temple(args.explorer)
    
    # Vue globale
    if args.vue_globale:
        await cli.afficher_vue_globale()
    
    # Si aucune action spécifique, afficher l'aide
    if not any([args.profil, args.explorer, args.vue_globale, args.retirer, args.aide]):
        print("🧠 Cerveau d'Immersion Moderne")
        print("Utilisez --aide pour voir le guide complet")
        print("\nExemple rapide:")
        print("python cli_cerveau.py --profil developpeur --niveau intermediaire")


if __name__ == "__main__":
    asyncio.run(main())