"""
Module d'Adaptation pour Source Orientale.
Un cercle qui s'inverse et évolue continuellement.
"""

import json
import logging
from typing import Dict, Any, List
import sqlite3
from datetime import datetime

class Adaptation:
    """Classe principale du module Adaptation."""
    
    def __init__(self, config_path: str = "../config/adaptation.json"):
        """Initialise le module d'adaptation avec sa configuration."""
        self.config = self._charger_config(config_path)
        self._initialiser_logging()
        self._initialiser_base_donnees()
        self.logger.info("Module d'adaptation initialisé")
    
    def _charger_config(self, config_path: str) -> Dict[str, Any]:
        """Charge la configuration depuis le fichier JSON."""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Erreur lors du chargement de la configuration : {e}")
    
    def _initialiser_logging(self):
        """Initialise le système de logging."""
        self.logger = logging.getLogger('adaptation')
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def _initialiser_base_donnees(self):
        """Initialise la base de données SQLite."""
        db_path = self.config['base_de_donnees']
        self.conn = sqlite3.connect(db_path)
        self._creer_tables()
    
    def _creer_tables(self):
        """Crée les tables nécessaires dans la base de données."""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS apprentissages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                contenu TEXT NOT NULL,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transformations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                apprentissage_id INTEGER,
                type_transformation TEXT NOT NULL,
                resultat TEXT NOT NULL,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (apprentissage_id) REFERENCES apprentissages (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS croissance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                transformation_id INTEGER,
                niveau INTEGER NOT NULL,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (transformation_id) REFERENCES transformations (id)
            )
        ''')
        self.conn.commit()
    
    def enregistrer_apprentissage(self, type_apprentissage: str, contenu: str) -> int:
        """Enregistre un nouvel apprentissage."""
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO apprentissages (type, contenu) VALUES (?, ?)',
            (type_apprentissage, contenu)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def transformer_apprentissage(self, apprentissage_id: int, type_transformation: str) -> Dict[str, Any]:
        """Transforme un apprentissage selon un type de transformation."""
        # TODO: Implémenter la logique de transformation
        resultat = f"Transformation {type_transformation} de l'apprentissage {apprentissage_id}"
        
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO transformations (apprentissage_id, type_transformation, resultat)
            VALUES (?, ?, ?)
        ''', (apprentissage_id, type_transformation, resultat))
        self.conn.commit()
        
        transformation_id = cursor.lastrowid
        
        # Enregistrer la croissance associée
        cursor.execute('''
            INSERT INTO croissance (transformation_id, niveau)
            VALUES (?, 1)
        ''', (transformation_id,))
        self.conn.commit()
        
        return {
            'id': transformation_id,
            'apprentissage_id': apprentissage_id,
            'type_transformation': type_transformation,
            'resultat': resultat,
            'date_creation': datetime.now().isoformat()
        }
    
    def obtenir_evolution(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Récupère l'évolution des apprentissages et transformations."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT 
                a.type as type_apprentissage,
                a.contenu as contenu_apprentissage,
                t.type_transformation,
                t.resultat,
                c.niveau,
                t.date_creation
            FROM apprentissages a
            JOIN transformations t ON a.id = t.apprentissage_id
            JOIN croissance c ON t.id = c.transformation_id
            ORDER BY t.date_creation DESC
            LIMIT ?
        ''', (limit,))
        
        return [{
            'type_apprentissage': row[0],
            'contenu_apprentissage': row[1],
            'type_transformation': row[2],
            'resultat': row[3],
            'niveau': row[4],
            'date_creation': row[5]
        } for row in cursor.fetchall()]
    
    def __del__(self):
        """Nettoyage à la destruction de l'instance."""
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    # Exemple d'utilisation
    adaptation = Adaptation()
    apprentissage_id = adaptation.enregistrer_apprentissage("test", "Contenu de test")
    print(f"Apprentissage enregistré avec l'ID : {apprentissage_id}")
    transformation = adaptation.transformer_apprentissage(apprentissage_id, "test")
    print(f"Transformation effectuée : {transformation}")
    evolution = adaptation.obtenir_evolution()
    print(f"Évolution : {evolution}") 