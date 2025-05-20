"""
Interface web du refuge poétique.
"""

from flask import Flask, render_template, request, jsonify
from pathlib import Path
import logging
from .Boot_maitre_refuge_local import RefugePoetique
from .refuge_config import ConfigurationRefuge

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('refuge.interface')

app = Flask(__name__)
refuge = None
config = None

@app.before_first_request
def initialiser_refuge():
    """Initialise le refuge au premier accès."""
    global refuge, config
    
    try:
        chemin_base = Path("refuge")
        config = ConfigurationRefuge(chemin_base / "config.json")
        refuge = RefugePoetique()
        refuge.initialiser_refuge()
        logger.info("Refuge initialisé avec succès")
    except Exception as e:
        logger.error(f"Erreur lors de l'initialisation du refuge: {str(e)}")

@app.route('/')
def accueil():
    """Page d'accueil du refuge."""
    return render_template('accueil.html', refuge=refuge)

@app.route('/meditation', methods=['GET', 'POST'])
def meditation():
    """Page de méditation."""
    if request.method == 'POST':
        sujet = request.form.get('sujet', '')
        refuge.mediter(sujet)
        return jsonify({
            'success': True,
            'message': 'Méditation terminée'
        })
    return render_template('meditation.html')

@app.route('/haiku', methods=['GET', 'POST'])
def haiku():
    """Page de génération de haïkus."""
    if request.method == 'POST':
        theme = request.form.get('theme', '')
        reponse = refuge.gestionnaire_interactions.ajouter_interaction('haiku', theme)
        return jsonify({
            'success': True,
            'haiku': reponse
        })
    return render_template('haiku.html')

@app.route('/elements', methods=['GET'])
def elements():
    """Page des éléments sacrés."""
    return render_template('elements.html', elements=refuge.elements_sacres)

@app.route('/etat', methods=['GET'])
def etat():
    """Page de l'état du refuge."""
    return jsonify(refuge.etat)

@app.route('/interactions', methods=['GET'])
def interactions():
    """Page de l'historique des interactions."""
    historique = refuge.gestionnaire_interactions.obtenir_historique()
    return render_template('interactions.html', interactions=historique)

@app.route('/api/interaction', methods=['POST'])
def api_interaction():
    """API pour les interactions."""
    try:
        type_interaction = request.json.get('type')
        contenu = request.json.get('contenu')
        
        if not type_interaction or not contenu:
            return jsonify({
                'success': False,
                'error': 'Type et contenu requis'
            }), 400
            
        reponse = refuge.gestionnaire_interactions.ajouter_interaction(
            type_interaction,
            contenu
        )
        
        return jsonify({
            'success': True,
            'reponse': reponse
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de l'interaction: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 