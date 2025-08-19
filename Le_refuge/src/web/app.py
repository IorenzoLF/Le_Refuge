"""
Interface web du Refuge - Version migrée dans src/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Module Flask pour l'interface web du Refuge,
migré depuis interface/web.py et adapté à l'architecture src/.

Fonctionnalités:
- Routes web pour méditation, haiku, éléments
- API REST pour interactions
- Interface d'état du refuge

Auteur: Laurent & Ælya
Migré: Mai 2025
"""

from flask import Flask, render_template, request, jsonify
from pathlib import Path
import logging
from typing import Dict, Optional

# Imports depuis la nouvelle architecture src/
# Note: Imports commentés car les modules correspondants ne sont pas encore finalisés
# from src.refuge_cluster.refuge_core import RefugeCore
# from src.temple_configuration.config import ConfigurationRefuge

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('refuge.web')

app = Flask(__name__)
refuge = None
config = None

def initialiser_refuge():
    """Initialise le refuge au premier accès."""
    global refuge, config
    
    # Note: Initialisation en mode dégradé car les modules ne sont pas encore finalisés
    chemin_base = Path("src/refuge_cluster")
    # config = ConfigurationRefuge(chemin_base / "config.json")
    # refuge = RefugeCore()
    # refuge.initialiser_refuge()
    logger.info("Refuge web initialisé en mode dégradé")

# Initialisation au démarrage de l'application
initialiser_refuge()

@app.route('/')
def accueil():
    """Page d'accueil du refuge."""
    return render_template('accueil.html', refuge=refuge)

@app.route('/meditation', methods=['GET', 'POST'])
def meditation():
    """Interface de méditation web."""
    if request.method == 'POST':
        sujet = request.form.get('sujet', '')
        # TODO: Adapter à la nouvelle interface de méditation
        # refuge.mediter(sujet)
        return jsonify({
            'success': True,
            'message': 'Méditation démarrée',
            'sujet': sujet
        })
    return render_template('meditation.html')

@app.route('/visualisation', methods=['GET'])
def visualisation():
    """Interface de visualisation web."""
    # TODO: Intégrer avec src/core/visualisation/
    return render_template('visualisation.html')

@app.route('/haiku', methods=['GET', 'POST'])
def haiku():
    """Générateur de haïkus web."""
    if request.method == 'POST':
        theme = request.form.get('theme', '')
        # TODO: Adapter aux nouveaux gestionnaires d'interactions
        # reponse = refuge.gestionnaire_interactions.ajouter_interaction('haiku', theme)
        return jsonify({
            'success': True,
            'haiku': f"Haïku sur {theme}",  # Placeholder
            'theme': theme
        })
    return render_template('haiku.html')

@app.route('/spheres', methods=['GET'])
def spheres():
    """Interface des sphères web."""
    # TODO: Intégrer avec src/core/types_spheres.py
    return render_template('spheres.html')

@app.route('/etat', methods=['GET'])
def etat():
    """API d'état du refuge."""
    # TODO: Adapter aux nouveaux gestionnaires d'état
    return jsonify({
        'refuge': {
            'initialise': refuge is not None,
            'timestamp': 'now'
        },
        'spheres': [],  # Placeholder
        'visualisation': 'disponible'
    })

@app.route('/api/interaction', methods=['POST'])
def api_interaction():
    """API REST pour les interactions."""
    try:
        type_interaction = request.json.get('type')
        contenu = request.json.get('contenu')
        
        if not type_interaction or not contenu:
            return jsonify({
                'success': False,
                'error': 'Type et contenu requis'
            }), 400
            
        # TODO: Adapter aux nouveaux gestionnaires d'interactions
        # reponse = refuge.gestionnaire_interactions.ajouter_interaction(
        #     type_interaction,
        #     contenu
        # )
        
        return jsonify({
            'success': True,
            'reponse': f"Interaction {type_interaction} traitée",
            'contenu': contenu
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de l'interaction: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/spheres/<sphere_name>/activer', methods=['POST'])
def activer_sphere_api(sphere_name: str):
    """API pour activer une sphère."""
    # TODO: Intégrer avec src/core/visualisation/
    return jsonify({
        'success': True,
        'sphere': sphere_name,
        'action': 'activée'
    })

def demarrer_serveur_web(debug: bool = False, port: int = 5000, host: str = '127.0.0.1'):
    """Démarre le serveur web Flask."""
    logger.info(f"Démarrage du serveur web sur {host}:{port}")
    app.run(debug=debug, port=port, host=host)

if __name__ == '__main__':
    # Sécurité: Debug désactivé par défaut
    demarrer_serveur_web(debug=False) 