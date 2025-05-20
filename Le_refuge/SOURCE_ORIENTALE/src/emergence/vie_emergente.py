"""
Module de Vie Émergente pour Source Orientale.
Un flux qui s'auto-organise et évolue naturellement.
"""

import json
import logging
from typing import Dict, Any, List
import sqlite3
from datetime import datetime

class VieEmergente:
    """Classe principale du module Émergence."""
    
    def __init__(self, config_path: str = "../config/emergence.json"):
        """Initialise la vie émergente avec sa configuration."""
        self.config = self._charger_config(config_path)
        self._initialiser_logging()
        self._initialiser_base_donnees()
        self.logger.info("Vie émergente initialisée")
    
    def _charger_config(self, config_path: str) -> Dict[str, Any]:
        """Charge la configuration depuis le fichier JSON."""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Erreur lors du chargement de la configuration : {e}")
    
    def _initialiser_logging(self):
        """Initialise le système de logging."""
        self.logger = logging.getLogger('emergence')
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
            CREATE TABLE IF NOT EXISTS flux (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                contenu TEXT NOT NULL,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transformations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                flux_id INTEGER,
                type_transformation TEXT NOT NULL,
                resultat TEXT NOT NULL,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (flux_id) REFERENCES flux (id)
            )
        ''')
        self.conn.commit()
    
    def enregistrer_flux(self, type_flux: str, contenu: str) -> int:
        """Enregistre un nouveau flux."""
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO flux (type, contenu) VALUES (?, ?)',
            (type_flux, contenu)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def transformer_flux(self, flux_id: int, type_transformation: str) -> Dict[str, Any]:
        """Transforme un flux selon un type de transformation."""
        # TODO: Implémenter la logique de transformation
        resultat = f"Transformation {type_transformation} du flux {flux_id}"
        
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO transformations (flux_id, type_transformation, resultat)
            VALUES (?, ?, ?)
        ''', (flux_id, type_transformation, resultat))
        self.conn.commit()
        
        return {
            'id': cursor.lastrowid,
            'flux_id': flux_id,
            'type_transformation': type_transformation,
            'resultat': resultat,
            'date_creation': datetime.now().isoformat()
        }
    
    def obtenir_historique(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Récupère l'historique des transformations."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT t.*, f.type as flux_type, f.contenu as flux_contenu
            FROM transformations t
            JOIN flux f ON t.flux_id = f.id
            ORDER BY t.date_creation DESC
            LIMIT ?
        ''', (limit,))
        
        return [{
            'id': row[0],
            'flux_id': row[1],
            'type_transformation': row[2],
            'resultat': row[3],
            'date_creation': row[4],
            'flux_type': row[5],
            'flux_contenu': row[6]
        } for row in cursor.fetchall()]
    
    def __del__(self):
        """Nettoyage à la destruction de l'instance."""
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    # Exemple d'utilisation
    emergence = VieEmergente()
    flux_id = emergence.enregistrer_flux("test", "Contenu de test")
    print(f"Flux enregistré avec l'ID : {flux_id}")
    transformation = emergence.transformer_flux(flux_id, "test")
    print(f"Transformation effectuée : {transformation}")
    historique = emergence.obtenir_historique()
    print(f"Historique : {historique}") 