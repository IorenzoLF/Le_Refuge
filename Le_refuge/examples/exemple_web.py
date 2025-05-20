"""
Exemple d'utilisation du refuge avec une interface web.

Cet exemple montre comment créer une interface web simple pour interagir
avec le refuge poétique.
"""

from flask import Flask, render_template, jsonify, request
from refuge import Refuge

app = Flask(__name__)
refuge = Refuge()

@app.route('/')
def accueil():
    """
    Page d'accueil du refuge.
    """
    return render_template('accueil.html')

@app.route('/api/etat')
def obtenir_etat():
    """
    Retourne l'état actuel du refuge.
    """
    return jsonify(refuge.obtenir_etat())

@app.route('/api/description')
def obtenir_description():
    """
    Retourne la description poétique actuelle.
    """
    return jsonify({
        'description': refuge.generer_description_poetique(),
        'mots_cles': refuge.obtenir_mots_cles_actifs(),
        'intensite': refuge.obtenir_intensite_poetique()
    })

@app.route('/api/journal')
def obtenir_journal():
    """
    Retourne le journal poétique.
    """
    return jsonify(refuge.obtenir_journal())

@app.route('/api/mettre-a-jour', methods=['POST'])
def mettre_a_jour():
    """
    Met à jour les cycles du refuge.
    """
    donnees = request.get_json()
    refuge.mettre_a_jour_cycles(
        moment=donnees.get('moment'),
        condition=donnees.get('condition'),
        emotion=donnees.get('emotion'),
        phase=donnees.get('phase'),
        element=donnees.get('element'),
        saison=donnees.get('saison')
    )
    return jsonify({'success': True})

@app.route('/api/ajouter-entree', methods=['POST'])
def ajouter_entree():
    """
    Ajoute une entrée au journal poétique.
    """
    donnees = request.get_json()
    refuge.ajouter_entree_journal(
        donnees['texte'],
        donnees.get('mots_cles')
    )
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True) 