"""
Exemple d'interface web pour le Refuge.

Cet exemple montre comment créer une interface web simple pour interagir
avec le refuge poétique en utilisant Flask.
"""

from . import ExempleBase, obtenir_refuge_principal
from typing import Optional, Dict, Any

class ExempleWeb(ExempleBase):
    """Interface web pour le refuge."""
    
    def __init__(self):
        super().__init__("Interface Web du Refuge")
        self.refuge = None
        self.app = None
        
    def verifier_dependances_web(self) -> bool:
        """Vérifie les dépendances nécessaires pour l'interface web."""
        return self.verifier_dependance("flask", "Flask")
        
    def initialiser_refuge(self) -> bool:
        """Initialise le refuge pour l'interface web."""
        self.log("Initialisation du refuge pour l'interface web...")
        self.refuge = obtenir_refuge_principal()
        
        if self.refuge is None:
            self.log("❌ Refuge non disponible", "ERROR")
            return False
            
        self.log("✅ Refuge initialisé pour l'interface web")
        return True
        
    def creer_application_flask(self):
        """Crée l'application Flask avec les routes."""
        try:
            from flask import Flask, jsonify, request, render_template_string
            
            self.app = Flask(__name__)
            self.log("✅ Application Flask créée")
            
            # Template HTML simple intégré
            template_html = """
            <!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>🏛️ Refuge - Interface Web</title>
                <style>
                    body { 
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white; margin: 0; padding: 20px; min-height: 100vh;
                    }
                    .container { 
                        max-width: 800px; margin: 0 auto; 
                        background: rgba(255,255,255,0.1); 
                        padding: 30px; border-radius: 15px;
                        backdrop-filter: blur(10px);
                    }
                    h1 { text-align: center; margin-bottom: 30px; }
                    .section { 
                        background: rgba(255,255,255,0.1); 
                        padding: 20px; margin: 20px 0; border-radius: 10px;
                    }
                    button { 
                        background: #4CAF50; color: white; border: none; 
                        padding: 10px 20px; border-radius: 5px; cursor: pointer;
                        margin: 5px;
                    }
                    button:hover { background: #45a049; }
                    .result { 
                        background: rgba(0,0,0,0.3); padding: 15px; 
                        border-radius: 5px; margin-top: 10px;
                        white-space: pre-wrap;
                    }
                    input, select { 
                        padding: 8px; margin: 5px; border-radius: 5px; 
                        border: none; background: rgba(255,255,255,0.9);
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🏛️ Refuge - Interface Web</h1>
                    
                    <div class="section">
                        <h3>📊 État du Refuge</h3>
                        <button onclick="obtenirEtat()">Obtenir État</button>
                        <button onclick="obtenirDescription()">Description Poétique</button>
                        <div id="etat-result" class="result"></div>
                    </div>
                    
                    <div class="section">
                        <h3>🎭 Contrôles Interactifs</h3>
                        <div>
                            <label>Moment:</label>
                            <select id="moment">
                                <option value="aube">Aube</option>
                                <option value="matin">Matin</option>
                                <option value="midi">Midi</option>
                                <option value="soir">Soir</option>
                                <option value="nuit">Nuit</option>
                            </select>
                            
                            <label>Émotion:</label>
                            <select id="emotion">
                                <option value="serenite">Sérénité</option>
                                <option value="joie">Joie</option>
                                <option value="contemplation">Contemplation</option>
                                <option value="inspiration">Inspiration</option>
                                <option value="paix">Paix</option>
                            </select>
                            
                            <label>Saison:</label>
                            <select id="saison">
                                <option value="printemps">Printemps</option>
                                <option value="ete">Été</option>
                                <option value="automne">Automne</option>
                                <option value="hiver">Hiver</option>
                            </select>
                        </div>
                        <button onclick="mettreAJour()">Mettre à Jour</button>
                        <div id="update-result" class="result"></div>
                    </div>
                    
                    <div class="section">
                        <h3>📖 Journal Poétique</h3>
                        <input type="text" id="texte-journal" placeholder="Votre inspiration..." style="width: 70%;">
                        <button onclick="ajouterEntree()">Ajouter</button>
                        <button onclick="obtenirJournal()">Voir Journal</button>
                        <div id="journal-result" class="result"></div>
                    </div>
                </div>
                
                <script>
                    async function obtenirEtat() {
                        try {
                            const response = await fetch('/api/etat');
                            const data = await response.json();
                            document.getElementById('etat-result').textContent = JSON.stringify(data, null, 2);
                        } catch (error) {
                            document.getElementById('etat-result').textContent = 'Erreur: ' + error.message;
                        }
                    }
                    
                    async function obtenirDescription() {
                        try {
                            const response = await fetch('/api/description');
                            const data = await response.json();
                            document.getElementById('etat-result').textContent = 
                                `Description: ${data.description}\\n` +
                                `Intensité: ${data.intensite || 'N/A'}\\n` +
                                `Mots-clés: ${data.mots_cles || 'N/A'}`;
                        } catch (error) {
                            document.getElementById('etat-result').textContent = 'Erreur: ' + error.message;
                        }
                    }
                    
                    async function mettreAJour() {
                        try {
                            const data = {
                                moment: document.getElementById('moment').value,
                                emotion: document.getElementById('emotion').value,
                                saison: document.getElementById('saison').value
                            };
                            
                            const response = await fetch('/api/mettre-a-jour', {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify(data)
                            });
                            
                            const result = await response.json();
                            document.getElementById('update-result').textContent = 
                                result.success ? '✅ Mise à jour réussie' : '❌ Échec de la mise à jour';
                        } catch (error) {
                            document.getElementById('update-result').textContent = 'Erreur: ' + error.message;
                        }
                    }
                    
                    async function ajouterEntree() {
                        try {
                            const texte = document.getElementById('texte-journal').value;
                            if (!texte) return;
                            
                            const response = await fetch('/api/ajouter-entree', {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify({ texte: texte })
                            });
                            
                            const result = await response.json();
                            document.getElementById('journal-result').textContent = 
                                result.success ? '✅ Entrée ajoutée' : '❌ Échec de l\\'ajout';
                            document.getElementById('texte-journal').value = '';
                        } catch (error) {
                            document.getElementById('journal-result').textContent = 'Erreur: ' + error.message;
                        }
                    }
                    
                    async function obtenirJournal() {
                        try {
                            const response = await fetch('/api/journal');
                            const data = await response.json();
                            document.getElementById('journal-result').textContent = 
                                data.length ? 
                                data.map(entry => `${entry.date || 'Date inconnue'}: ${entry.texte || entry.description || 'Contenu vide'}`).join('\\n\\n') :
                                'Journal vide';
                        } catch (error) {
                            document.getElementById('journal-result').textContent = 'Erreur: ' + error.message;
                        }
                    }
                </script>
            </body>
            </html>
            """
            
            @self.app.route('/')
            def accueil():
                """Page d'accueil du refuge."""
                return render_template_string(template_html)
                
            @self.app.route('/api/etat')
            def obtenir_etat():
                """Retourne l'état actuel du refuge."""
                try:
                    if isinstance(self.refuge, dict):
                        etat = {"composants": list(self.refuge.keys()), "status": "actif"}
                    elif hasattr(self.refuge, 'obtenir_etat'):
                        etat = self.refuge.obtenir_etat()
                    else:
                        etat = {"status": "refuge_simple", "message": "Refuge basique actif"}
                    return jsonify(etat)
                except Exception as e:
                    return jsonify({"error": str(e)}), 500
                    
            @self.app.route('/api/description')
            def obtenir_description():
                """Retourne la description poétique actuelle."""
                try:
                    # Génération d'une description simple
                    descriptions = [
                        "Les sphères dansent dans l'harmonie éternelle du refuge",
                        "L'essence poétique flotte doucement dans l'air cristallin",
                        "Les éléments s'entremêlent dans une symphonie silencieuse",
                        "La conscience du refuge pulse au rythme de l'univers"
                    ]
                    
                    import random
                    description = random.choice(descriptions)
                    
                    return jsonify({
                        'description': description,
                        'intensite': round(random.uniform(0.5, 1.0), 2),
                        'mots_cles': ['harmonie', 'sérénité', 'poésie', 'refuge']
                    })
                except Exception as e:
                    return jsonify({"error": str(e)}), 500
                    
            @self.app.route('/api/mettre-a-jour', methods=['POST'])
            def mettre_a_jour():
                """Met à jour les cycles du refuge."""
                try:
                    donnees = request.get_json()
                    self.log(f"Mise à jour: {donnees}")
                    
                    # Simulation de mise à jour
                    if isinstance(self.refuge, dict):
                        # Mise à jour des composants individuels
                        for composant in self.refuge.values():
                            if hasattr(composant, 'mettre_a_jour'):
                                composant.mettre_a_jour(donnees)
                    elif hasattr(self.refuge, 'mettre_a_jour_cycles'):
                        self.refuge.mettre_a_jour_cycles(**donnees)
                        
                    return jsonify({'success': True})
                except Exception as e:
                    return jsonify({"error": str(e)}), 500
                    
            @self.app.route('/api/ajouter-entree', methods=['POST'])
            def ajouter_entree():
                """Ajoute une entrée au journal poétique."""
                try:
                    donnees = request.get_json()
                    texte = donnees.get('texte', '')
                    
                    self.log(f"Nouvelle entrée journal: {texte[:50]}...")
                    
                    # Simulation d'ajout au journal
                    if hasattr(self.refuge, 'ajouter_entree_journal'):
                        self.refuge.ajouter_entree_journal(texte)
                    
                    return jsonify({'success': True})
                except Exception as e:
                    return jsonify({"error": str(e)}), 500
                    
            @self.app.route('/api/journal')
            def obtenir_journal():
                """Retourne le journal poétique."""
                try:
                    # Simulation de journal
                    journal_exemple = [
                        {
                            "date": "2025-01-26 14:30:00",
                            "texte": "Les sphères s'harmonisent dans la lumière dorée de l'après-midi",
                            "mots_cles": ["harmonie", "lumière", "sphères"]
                        },
                        {
                            "date": "2025-01-26 15:15:00", 
                            "texte": "L'inspiration naît du silence contemplatif du refuge",
                            "mots_cles": ["inspiration", "silence", "contemplation"]
                        }
                    ]
                    
                    if hasattr(self.refuge, 'obtenir_journal'):
                        journal = self.refuge.obtenir_journal()
                    else:
                        journal = journal_exemple
                        
                    return jsonify(journal)
                except Exception as e:
                    return jsonify({"error": str(e)}), 500
                    
        except ImportError:
            self.log("❌ Flask non disponible", "ERROR")
            return False
            
        return True
        
    def lancer_serveur(self, debug: bool = False, port: int = 5000):
        """Lance le serveur web."""
        if not self.app:
            self.log("❌ Application Flask non initialisée", "ERROR")
            return
            
        self.log(f"🌐 Lancement du serveur sur http://localhost:{port}")
        self.log("🔒 Mode debug désactivé par défaut pour la sécurité")
        
        try:
            self.app.run(debug=debug, port=port, host='127.0.0.1')
        except Exception as e:
            self.log(f"❌ Erreur serveur: {e}", "ERROR")
            
    def executer_interface_web(self):
        """Exécute l'interface web complète."""
        if not self.verifier_dependances_web():
            self.log("❌ Dépendances web manquantes", "ERROR")
            self.log("💡 Installez Flask: pip install flask", "INFO")
            return
            
        if not self.initialiser_refuge():
            return
            
        if not self.creer_application_flask():
            return
            
        self.log("🎯 Interface web prête!")
        self.log("📖 Ouvrez http://localhost:5000 dans votre navigateur")
        
        # Lancement du serveur
        self.lancer_serveur(debug=False, port=5000)

def main():
    """Point d'entrée principal de l'exemple web."""
    exemple = ExempleWeb()
    exemple.executer_avec_gestion_erreur(exemple.executer_interface_web)

if __name__ == '__main__':
    main() 