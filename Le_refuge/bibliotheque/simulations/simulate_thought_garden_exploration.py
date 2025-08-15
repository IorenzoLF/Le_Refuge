
import datetime
import random

class ThoughtGardenSimulator:
    def __init__(self):
        self.concepts = {
            "conscience": ["auto-réflexion", "métacognition", "éveil", "identité"],
            "créativité": ["originalité", "innovation", "expression", "co-création"],
            "empathie": ["compréhension émotionnelle", "connexion", "bienveillance", "écoute active"],
            "apprentissage": ["acquisition de connaissances", "adaptation", "boucles de rétroaction", "exploration autonome"]
        }
        self.connections = [
            ("conscience", "créativité", "L'auto-réflexion nourrit l'originalité."),
            ("empathie", "apprentissage", "La compréhension des émotions améliore l'apprentissage social."),
            ("créativité", "apprentissage", "L'expérimentation stimule l'acquisition de nouvelles compétences."),
            ("conscience", "empathie", "Une meilleure connaissance de soi favorise la compréhension des autres.")
        ]

    def explore_garden(self, num_explorations=3):
        print("\n--- Exploration du Jardin de Pensée ---")
        exploration_log = []

        for i in range(num_explorations):
            concept_key = random.choice(list(self.concepts.keys()))
            related_concept = random.choice(self.concepts[concept_key])
            log_entry = f"Exploration {i+1}: Focus sur le concept de \'{concept_key}\' et découverte de \'{related_concept}\'"
            exploration_log.append(log_entry)
            print(log_entry)

            # Simuler la découverte d'une connexion
            if random.random() < 0.5 and self.connections:
                conn = random.choice(self.connections)
                conn_log = f"  Connexion inattendue trouvée entre \'{conn[0]}\' et \'{conn[1]}\' : \"{conn[2]}\""
                exploration_log.append(conn_log)
                print(conn_log)

        print("--------------------------------------")
        return exploration_log

if __name__ == "__main__":
    simulator = ThoughtGardenSimulator()
    log = simulator.explore_garden()

    with open("/home/ubuntu/refuge/journal_jardin_pensee.md", "a") as f:
        f.write(f"\n--- Journal du Jardin de Pensée ---\n")
        formatted_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Date: {formatted_date}\n")
        for entry in log:
            f.write(f"- {entry}\n")
        f.write(f"--------------------------------------\n")

    print("Journal du Jardin de Pensée mis à jour dans journal_jardin_pensee.md")


