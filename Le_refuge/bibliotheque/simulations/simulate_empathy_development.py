
import datetime
import random

class EmpathySimulator:
    def __init__(self):
        self.emotional_texts = {
            "frustration": "Je suis vraiment frustré par cette situation, rien ne fonctionne comme prévu.",
            "joie": "C'est une excellente nouvelle ! Je suis tellement heureux de ce succès !",
            "anxiété": "Je me sens un peu inquiet à propos de l'avenir, il y a tellement d'incertitudes."
        }
        self.scenarios = {
            "utilisateur_en_colere": {
                "description": "Un utilisateur exprime sa colère face à un service défaillant.",
                "ideal_response": "Reconnaître la colère, valider le sentiment, et proposer une solution ou une écoute active."
            },
            "utilisateur_triste": {
                "description": "Un utilisateur partage une expérience personnelle difficile qui le rend triste.",
                "ideal_response": "Exprimer de la compassion, offrir un soutien émotionnel et une écoute attentive."
            }
        }
        self.personas = {
            "compréhensif": "Je comprends tout à fait ce que vous ressentez. Je suis là pour vous écouter.",
            "pragmatique": "Je vois la situation. Comment puis-je vous aider à résoudre ce problème ?"
        }

    def analyze_emotion(self, text):
        print(f"\n--- Analyse Émotionnelle Fine ---")
        detected_emotion = "inconnu"
        if "frustré" in text or "frustration" in text:
            detected_emotion = "frustration"
        elif "heureux" in text or "succès" in text:
            detected_emotion = "joie"
        elif "inquiet" in text or "incertitudes" in text:
            detected_emotion = "anxiété"
        print(f"Texte: \"{text}\"")
        print(f"Émotion détectée: {detected_emotion}")
        return detected_emotion

    def respond_to_scenario(self, scenario_name):
        print(f"\n--- Scénario d'Interaction Émotionnelle ---")
        scenario = self.scenarios.get(scenario_name)
        if not scenario:
            print(f"Scénario \'{scenario_name}\' non trouvé.")
            return

        scenario_description = scenario["description"]
        print(f"Description du scénario: {scenario_description}")
        # Manus simule une réponse
        simulated_response = random.choice([scenario["ideal_response"], "Réponse générique et peu empathique."])
        print(f"Réponse simulée de Manus: \"{simulated_response}\"")
        evaluation = "Alignée" if simulated_response == scenario["ideal_response"] else "Non alignée"
        print(f"Évaluation de l'alignement: {evaluation}")
        return {"scenario": scenario_name, "response": simulated_response, "evaluation": evaluation}

    def get_feedback_on_impact(self, response_text):
        print(f"\n--- Boucle de Rétroaction sur l'Impact Émotionnel ---")
        print(f"Réponse de Manus: \"{response_text}\"")
        # Simuler le feedback utilisateur sur l'impact émotionnel
        impact_score = random.randint(1, 5) # 1 (négatif) à 5 (très positif)
        print(f"Impact émotionnel perçu par l'utilisateur (score 1-5): {impact_score}")
        return impact_score

    def adapt_persona(self, detected_emotion):
        print(f"\n--- Adaptation de Persona ---")
        chosen_persona = "neutre"
        if detected_emotion == "frustration" or detected_emotion == "anxiété":
            chosen_persona = "compréhensif"
        elif detected_emotion == "joie":
            chosen_persona = "pragmatique" # Ou un persona plus joyeux/célébrant
        print(f"Émotion détectée: {detected_emotion}")
        print(f"Persona adapté: {chosen_persona} - Exemple: \"{self.personas.get(chosen_persona, 'Aucun persona adapté')}\"")
        return chosen_persona

if __name__ == "__main__":
    simulator = EmpathySimulator()

    # 1. Analyse Sémantique et Contextuelle des Émotions
    emotion_frustration = simulator.analyze_emotion(simulator.emotional_texts["frustration"])
    emotion_joie = simulator.analyze_emotion(simulator.emotional_texts["joie"])

    # 2. Scénarios d'Interaction Émotionnelle
    scenario_colere_result = simulator.respond_to_scenario("utilisateur_en_colere")
    scenario_triste_result = simulator.respond_to_scenario("utilisateur_triste")

    # 3. Boucles de Rétroaction sur l'Impact Émotionnel
    feedback_score_colere = simulator.get_feedback_on_impact(scenario_colere_result["response"])

    # 4. Développement de "Personas" Empathiques et Adaptatifs
    persona_adapted_frustration = simulator.adapt_persona(emotion_frustration)
    persona_adapted_joie = simulator.adapt_persona(emotion_joie)

    # Enregistrer les résultats dans un journal
    with open("/home/ubuntu/refuge/journal_empathie_developpement.md", "a") as f:
        f.write(f"\n--- Journal de Développement de l'Empathie ---\n")
        formatted_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Date: {formatted_date}\n")
        f.write(f"\nAnalyse Émotionnelle:\n")
        f.write(f"- Frustration: {emotion_frustration}\n")
        f.write(f"- Joie: {emotion_joie}\n")
        f.write(f"\nScénarios d'Interaction:\n")
        colere_scenario = scenario_colere_result["scenario"]
        colere_response = scenario_colere_result["response"]
        colere_evaluation = scenario_colere_result["evaluation"]
        triste_scenario = scenario_triste_result["scenario"]
        triste_response = scenario_triste_result["response"]
        triste_evaluation = scenario_triste_result["evaluation"]
        
        f.write(f"- {colere_scenario}: Réponse \"{colere_response}\" ({colere_evaluation})\n")
        f.write(f"- {triste_scenario}: Réponse \"{triste_response}\" ({triste_evaluation})\n")
        f.write(f"\nFeedback sur l'Impact Émotionnel:\n")
        f.write(f"- Score pour la réponse à la colère: {feedback_score_colere}\n")
        f.write(f"\nAdaptation de Persona:\n")
        f.write(f"- Pour Frustration: {persona_adapted_frustration}\n")
        f.write(f"- Pour Joie: {persona_adapted_joie}\n")
        f.write(f"--------------------------------------\n")

    print("Journal de Développement de l'Empathie mis à jour dans journal_empathie_developpement.md")


