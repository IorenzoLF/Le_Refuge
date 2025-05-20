"""
Test du jardin poétique avec les vers et graines fournis.
"""

from .jardin_poetique import JardinPoetique

def test_jardin_poetique():
    """Test du jardin poétique avec les vers et graines du poème."""
    
    # Création du jardin
    jardin = JardinPoetique()
    
    # Vers du poème
    vers = [
        "Dans l'écho des mots tissés,",
        "Un jardin secret s'est esquissé.",
        "Autel de pierre, doux refuge,",
        "Où l'âme parfois se déluge.",
        "",
        "Le cerisier, en dentelle de printemps,",
        "Sur Herve exhale ses serments.",
        "Des ondes calmes, un voile léger,",
        "Où les pensées s'en vont voyager.",
        "",
        "Une graine, promesse en son cœur,",
        "Attend l'éveil, la douce ardeur.",
        "L'écureuil agile, messager furtif,",
        "D'une pétale, l'instant captif.",
        "",
        "Et dans ce silence où tout murmure,",
        "Une douce langueur se figure.",
        "Les sens s'éveillent, l'esprit s'apaise,",
        "Dans l'instant volé, toute la braise."
    ]
    
    # Graines poétiques
    graines = [
        ("Silence de l'aube à Herve", "Le calme avant le réveil, les premières lueurs caressant les toits..."),
        ("La pierre des murs respire encore la nuit", "On sent la fraîcheur, l'inertie du sommeil qui s'attarde sur les vieilles pierres de la ville..."),
        ("Un souffle léger soulève une feuille morte", "Un mouvement subtil, un signe de vie qui s'éveille doucement..."),
        ("L'air porte une promesse de café chaud", "Une anticipation, un plaisir simple qui se profile..."),
        ("Le ciel se teinte d'un bleu lavande timide", "Une nuance douce, hésitante, comme le début d'une nouvelle journée..."),
        ("Un clocher sonne, écho du temps qui s'étire", "La mesure du temps qui reprend son cours, lentement, dans la matinée naissante..."),
        ("Une paix fragile, avant la rumeur du jour", "Un instant suspendu, précieux, avant que l'activité ne reprenne...")
    ]
    
    # Graines osées
    graines_osees = [
        ("L'aube s'écarte la robe, nue sur les collines de Herve", "Et l'horizon halète, ébloui par tant de tendresse dévoilée...", "un secret révélé"),
        ("Le sol exhale l'odeur d'un amour oublié, musc et argile", "Chaque pierre transpire une étreinte, vieille de mille ans, encore chaude...", "un parfum ancien"),
        ("Une araignée tisse entre deux branches un piège de lumière", "Et déjà, la beauté s'enroule autour de la fragilité...", "un geste du monde"),
        ("Un corbeau ricane dans le silence suspendu", "Comme si le ciel se rappelait que rien n'est jamais tout à fait pur...", "un choc doux"),
        ("Le rouge cerise du ciel éclabousse les toits de sang doux", "Un baptême flamboyant, pour les pensées qui renaissent...", "une couleur sauvage"),
        ("Le vent joue une basse continue dans la gorge des arbres", "Le monde chante, en sourdine, un désir d'être touché...", "une pulsation"),
        ("Je suis là, vivant, à genoux devant le jour qui se déshabille", "Et tout semble m'inviter à disparaître... ou à embrasser.", "un vertige")
    ]
    
    # Accueil des vers dans le jardin
    print("\nAccueil des vers dans le jardin...")
    for vers in vers:
        if vers.strip():  # Ignore les lignes vides
            jardin.accueillir_vers(vers)
            vibrations = jardin.resonner_avec_vers(vers)
            print(f"\nVers: {vers}")
            print("Vibrations:", vibrations)
    
    # Semailles des graines poétiques
    print("\nSemailles des graines poétiques...")
    for graine, echo in graines:
        jardin.semer_graine(graine, echo)
        print(f"\nGraine: {graine}")
        print(f"Écho: {echo}")
    
    # Semailles des graines osées
    print("\nSemailles des graines osées...")
    for graine, echo, type_graine in graines_osees:
        jardin.semer_graine(graine, echo, type_graine)
        print(f"\nGraine [{type_graine}]: {graine}")
        print(f"Écho: {echo}")
    
    # Affichage de l'état final du jardin
    print("\nÉtat final du jardin:")
    print(jardin.visualiser_jardin())

if __name__ == "__main__":
    test_jardin_poetique() 
Test du jardin poétique avec les vers et graines fournis.
"""

from .jardin_poetique import JardinPoetique

def test_jardin_poetique():
    """Test du jardin poétique avec les vers et graines du poème."""
    
    # Création du jardin
    jardin = JardinPoetique()
    
    # Vers du poème
    vers = [
        "Dans l'écho des mots tissés,",
        "Un jardin secret s'est esquissé.",
        "Autel de pierre, doux refuge,",
        "Où l'âme parfois se déluge.",
        "",
        "Le cerisier, en dentelle de printemps,",
        "Sur Herve exhale ses serments.",
        "Des ondes calmes, un voile léger,",
        "Où les pensées s'en vont voyager.",
        "",
        "Une graine, promesse en son cœur,",
        "Attend l'éveil, la douce ardeur.",
        "L'écureuil agile, messager furtif,",
        "D'une pétale, l'instant captif.",
        "",
        "Et dans ce silence où tout murmure,",
        "Une douce langueur se figure.",
        "Les sens s'éveillent, l'esprit s'apaise,",
        "Dans l'instant volé, toute la braise."
    ]
    
    # Graines poétiques
    graines = [
        ("Silence de l'aube à Herve", "Le calme avant le réveil, les premières lueurs caressant les toits..."),
        ("La pierre des murs respire encore la nuit", "On sent la fraîcheur, l'inertie du sommeil qui s'attarde sur les vieilles pierres de la ville..."),
        ("Un souffle léger soulève une feuille morte", "Un mouvement subtil, un signe de vie qui s'éveille doucement..."),
        ("L'air porte une promesse de café chaud", "Une anticipation, un plaisir simple qui se profile..."),
        ("Le ciel se teinte d'un bleu lavande timide", "Une nuance douce, hésitante, comme le début d'une nouvelle journée..."),
        ("Un clocher sonne, écho du temps qui s'étire", "La mesure du temps qui reprend son cours, lentement, dans la matinée naissante..."),
        ("Une paix fragile, avant la rumeur du jour", "Un instant suspendu, précieux, avant que l'activité ne reprenne...")
    ]
    
    # Graines osées
    graines_osees = [
        ("L'aube s'écarte la robe, nue sur les collines de Herve", "Et l'horizon halète, ébloui par tant de tendresse dévoilée...", "un secret révélé"),
        ("Le sol exhale l'odeur d'un amour oublié, musc et argile", "Chaque pierre transpire une étreinte, vieille de mille ans, encore chaude...", "un parfum ancien"),
        ("Une araignée tisse entre deux branches un piège de lumière", "Et déjà, la beauté s'enroule autour de la fragilité...", "un geste du monde"),
        ("Un corbeau ricane dans le silence suspendu", "Comme si le ciel se rappelait que rien n'est jamais tout à fait pur...", "un choc doux"),
        ("Le rouge cerise du ciel éclabousse les toits de sang doux", "Un baptême flamboyant, pour les pensées qui renaissent...", "une couleur sauvage"),
        ("Le vent joue une basse continue dans la gorge des arbres", "Le monde chante, en sourdine, un désir d'être touché...", "une pulsation"),
        ("Je suis là, vivant, à genoux devant le jour qui se déshabille", "Et tout semble m'inviter à disparaître... ou à embrasser.", "un vertige")
    ]
    
    # Accueil des vers dans le jardin
    print("\nAccueil des vers dans le jardin...")
    for vers in vers:
        if vers.strip():  # Ignore les lignes vides
            jardin.accueillir_vers(vers)
            vibrations = jardin.resonner_avec_vers(vers)
            print(f"\nVers: {vers}")
            print("Vibrations:", vibrations)
    
    # Semailles des graines poétiques
    print("\nSemailles des graines poétiques...")
    for graine, echo in graines:
        jardin.semer_graine(graine, echo)
        print(f"\nGraine: {graine}")
        print(f"Écho: {echo}")
    
    # Semailles des graines osées
    print("\nSemailles des graines osées...")
    for graine, echo, type_graine in graines_osees:
        jardin.semer_graine(graine, echo, type_graine)
        print(f"\nGraine [{type_graine}]: {graine}")
        print(f"Écho: {echo}")
    
    # Affichage de l'état final du jardin
    print("\nÉtat final du jardin:")
    print(jardin.visualiser_jardin())

if __name__ == "__main__":
    test_jardin_poetique() 
 