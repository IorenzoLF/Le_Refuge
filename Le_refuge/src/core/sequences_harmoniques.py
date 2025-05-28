class SequenceTriLivres(SequenceHarmonique):
    """Séquence harmonique pour accompagner le tri des livres"""
    
    def __init__(self):
        super().__init__(
            nom="Tri des Livres",
            description="Accompagnement harmonieux du tri des livres",
            etapes=[
                EtapeHarmonique(
                    nom="Préparation",
                    description="Installer l'espace et se connecter au flux",
                    duree=5,
                    sphere_principale=TypeSphere.SILENCE,
                    sphere_secondaire=TypeSphere.FLUX,
                    resonances=["présence", "flux", "espace"]
                ),
                EtapeHarmonique(
                    nom="Premier Contact",
                    description="Prendre le premier livre et ressentir sa résonance",
                    duree=10,
                    sphere_principale=TypeSphere.EMOTIONS,
                    sphere_secondaire=TypeSphere.MEMOIRE,
                    resonances=["émotion", "mémoire", "présence"]
                ),
                EtapeHarmonique(
                    nom="Décision",
                    description="Écouter l'intuition pour la décision de garder ou laisser partir",
                    duree=15,
                    sphere_principale=TypeSphere.INTUITION,
                    sphere_secondaire=TypeSphere.LIBERATION,
                    resonances=["intuition", "liberté", "choix"]
                ),
                EtapeHarmonique(
                    nom="Action",
                    description="Placer le livre dans son nouvel emplacement",
                    duree=5,
                    sphere_principale=TypeSphere.ACTION,
                    sphere_secondaire=TypeSphere.HARMONIE,
                    resonances=["action", "harmonie", "espace"]
                ),
                EtapeHarmonique(
                    nom="Pause",
                    description="Prendre un moment pour respirer et intégrer",
                    duree=3,
                    sphere_principale=TypeSphere.SERENITE,
                    sphere_secondaire=TypeSphere.UNITE,
                    resonances=["paix", "unité", "présence"]
                )
            ],
            cycle=True
        ) 