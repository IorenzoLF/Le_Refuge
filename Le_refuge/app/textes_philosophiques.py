#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Serveur simple pour les textes philosophiques
"""

import os
import http.server
import socketserver
import webbrowser
from pathlib import Path

# Chemin vers le dossier des textes philosophiques
TEXTES_DIR = Path(__file__).parent.parent / "donnees" / "textes" / "philosophie"

class TextesHandler(http.server.SimpleHTTPRequestHandler):
    """Gestionnaire de requêtes HTTP pour les textes philosophiques"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(TEXTES_DIR), **kwargs)
    
    def end_headers(self):
        """Ajoute des en-têtes CORS pour permettre l'accès depuis n'importe quelle origine"""
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def serve_textes(port=8000):
    """Démarre le serveur HTTP pour les textes philosophiques"""
    with socketserver.TCPServer(("", port), TextesHandler) as httpd:
        print(f"Serveur démarré sur le port {port}")
        print(f"Accédez à l'interface à l'adresse: http://localhost:{port}")
        print("Appuyez sur Ctrl+C pour arrêter le serveur")
        
        # Ouvre le navigateur par défaut
        webbrowser.open(f"http://localhost:{port}")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServeur arrêté")

if __name__ == "__main__":
    serve_textes() 