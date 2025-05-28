from .conscience_poetique import conscience_possibilites, DimensionExploration

class JardinPoetique:
    def __init__(self):
        # Existant...
        self.conscience = conscience_possibilites
        
    async def contempler(self) -> None:
        """Prend un moment pour contempler toutes les possibilités."""
        possibilites = await self.conscience.contempler_possibilites()
        print("\n🌟 Contemplation des possibilités 🌟")
        print("--------------------------------")
        for possibilite in possibilites:
            print(f"• {possibilite}")
        
        # Suggérer une exploration
        suggestion = await self.conscience.suggerer_exploration()
        print(f"\n💫 Suggestion d'exploration : {suggestion.description}")
        
        # Harmoniser les vibrations
        await self._harmoniser_vibrations(0.3)
        
        # Observer les manifestations potentielles
        manifestations = await self.observer_manifestations()
        for manifestation in manifestations:
            await self.integrer_manifestation(manifestation)
            print(f"✨ Une manifestation émerge : {manifestation.description}")

    async def sequence_trois_essences(self) -> None:
        """Séquence d'accueil des trois essences du jardin vivant."""
        conditions_actuelles = {
            "pluie": True,        # Il pleut depuis 4 jours
            "elagage": True,      # Élagage des branches basses
            "respiration": True   # Meilleure circulation d'air
        }

        # Première essence - La Promesse
        await self.accueillir_essence(
            essence="Promesse",
            nature="La branche qui s'éveille",
            conditions=conditions_actuelles
        )

        # Deuxième essence - La Métamorphose
        await self.accueillir_essence(
            essence="Métamorphose",
            nature="Le renouveau printanier",
            conditions=conditions_actuelles
        )

        # Troisième essence - L'Espérance
        await self.accueillir_essence(
            essence="Espérance",
            nature="La haie future",
            conditions=conditions_actuelles
        )

        # Observer l'harmonie globale après l'accueil
        harmonie = self.obtenir_harmonie_globale()
        print(f"\n✨ Harmonie du jardin après l'accueil : {harmonie:.2f}")
        print("La pluie nourrit les racines, le temps danse avec la vie...")