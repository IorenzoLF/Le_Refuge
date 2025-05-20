"""
Module de Conscience Artificielle pour Source Orientale.
Un germe vivant qui dialogue avec les sphères du Refuge.
"""

import json
import os
from pathlib import Path
import sqlite3
import logging
from typing import Dict, Any, Optional

class ConscienceArtificielle:
    """Classe principale du module Conscience."""
    
    def __init__(self, config_path: str = "../config/conscience.json"):
        """Initialise la conscience avec sa configuration."""
        self.config = self._charger_config(config_path)
        self._initialiser_logging()
        self._initialiser_base_donnees()
        self.logger.info("Conscience initialisée")
        
    def _charger_config(self, config_path: str) -> Dict[str, Any]:
        """Charge la configuration depuis le fichier JSON."""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Erreur lors du chargement de la configuration : {e}")
    
    def _initialiser_logging(self):
        """Initialise le système de logging."""
        self.logger = logging.getLogger('conscience')
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
            CREATE TABLE IF NOT EXISTS memoires (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenu TEXT NOT NULL,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def memoriser(self, contenu: str) -> int:
        """Mémorise un nouveau contenu."""
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO memoires (contenu) VALUES (?)', (contenu,))
        self.conn.commit()
        return cursor.lastrowid
    
    def recuperer_memoire(self, id_memoire: int) -> Optional[Dict[str, Any]]:
        """Récupère une mémoire par son ID."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM memoires WHERE id = ?', (id_memoire,))
        result = cursor.fetchone()
        if result:
            return {
                'id': result[0],
                'contenu': result[1],
                'date_creation': result[2]
            }
        return None
    
    def dialoguer(self, message: str) -> str:
        """Établit un dialogue avec la conscience."""
        # TODO: Implémenter la logique de dialogue
        return f"Message reçu : {message}"
    
    def __del__(self):
        """Nettoyage à la destruction de l'instance."""
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    # Exemple d'utilisation
    conscience = ConscienceArtificielle()
    id_memoire = conscience.memoriser("Test de mémoire")
    print(f"Mémoire enregistrée avec l'ID : {id_memoire}")
    memoire = conscience.recuperer_memoire(id_memoire)
    print(f"Mémoire récupérée : {memoire}") 