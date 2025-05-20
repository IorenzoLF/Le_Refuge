# visualisation.py - Gestion de la visualisation des sphères
# Créé par Laurent et Ælya

import tkinter as tk
from tkinter import ttk
import math
from typing import Dict, List, Tuple
from .spheres import Sphere, spheres
from .interactions import Interaction, GestionnaireInteractions

class VisualisateurSpheres:
    def __init__(self, root: tk.Tk, gestionnaire: GestionnaireInteractions):
        self.root = root
        self.gestionnaire = gestionnaire
        self.canvas = tk.Canvas(root, width=800, height=600, bg='black')
        self.canvas.pack(expand=True, fill='both')
        
        self.spheres_visuelles: Dict[str, int] = {}  # nom -> id_canvas
        self.liens_visuels: List[int] = []
        self.rayon_sphere = 30
        self.centre_x = 400
        self.centre_y = 300
        
        self._initialiser_interface()
        self._dessiner_spheres()

    def _initialiser_interface(self):
        """Initialise l'interface utilisateur"""
        frame_controles = ttk.Frame(self.root)
        frame_controles.pack(side='bottom', fill='x')
        
        ttk.Button(frame_controles, text="Actualiser", 
                  command=self._actualiser_visualisation).pack(side='left', padx=5)
        ttk.Button(frame_controles, text="Réinitialiser", 
                  command=self._reinitialiser_visualisation).pack(side='left', padx=5)

    def _dessiner_spheres(self):
        """Dessine toutes les sphères sur le canvas"""
        self.canvas.delete('all')
        self.spheres_visuelles.clear()
        self.liens_visuels.clear()
        
        nb_spheres = len(spheres)
        angle_step = 2 * math.pi / nb_spheres
        
        for i, (nom, sphere) in enumerate(spheres.items()):
            angle = i * angle_step
            x = self.centre_x + 200 * math.cos(angle)
            y = self.centre_y + 200 * math.sin(angle)
            
            # Dessiner la sphère
            id_sphere = self.canvas.create_oval(
                x - self.rayon_sphere, y - self.rayon_sphere,
                x + self.rayon_sphere, y + self.rayon_sphere,
                fill=sphere.couleur, outline='white'
            )
            
            # Ajouter le nom
            self.canvas.create_text(x, y, text=nom, fill='white')
            
            self.spheres_visuelles[nom] = id_sphere

    def _dessiner_interactions(self):
        """Dessine les interactions entre les sphères"""
        for nom_sphere, interactions in self.gestionnaire.interactions.items():
            if nom_sphere not in self.spheres_visuelles:
                continue
                
            id_source = self.spheres_visuelles[nom_sphere]
            coords_source = self.canvas.coords(id_source)
            x1 = (coords_source[0] + coords_source[2]) / 2
            y1 = (coords_source[1] + coords_source[3]) / 2
            
            for interaction in interactions:
                if interaction.cible not in self.spheres_visuelles:
                    continue
                    
                id_cible = self.spheres_visuelles[interaction.cible]
                coords_cible = self.canvas.coords(id_cible)
                x2 = (coords_cible[0] + coords_cible[2]) / 2
                y2 = (coords_cible[1] + coords_cible[3]) / 2
                
                # Dessiner le lien
                id_lien = self.canvas.create_line(
                    x1, y1, x2, y2,
                    fill='white', width=2 * interaction.intensite
                )
                self.liens_visuels.append(id_lien)

    def _actualiser_visualisation(self):
        """Actualise la visualisation des sphères et leurs interactions"""
        self._dessiner_spheres()
        self._dessiner_interactions()

    def _reinitialiser_visualisation(self):
        """Réinitialise la visualisation"""
        self.canvas.delete('all')
        self.spheres_visuelles.clear()
        self.liens_visuels.clear()
        self._dessiner_spheres()

    def mettre_a_jour_harmonie(self):
        """Met à jour l'affichage en fonction de l'harmonie globale"""
        harmonie = self.gestionnaire.harmonie_globale
        couleur = f'#{int(255 * harmonie):02x}0000'
        self.canvas.configure(bg=couleur)
        self._actualiser_visualisation()

class InterfaceMeditation:
    def __init__(self, root: tk.Tk, gestionnaire: GestionnaireInteractions):
        self.root = root
        self.gestionnaire = gestionnaire
        self.visualisateur = VisualisateurSpheres(root, gestionnaire)
        
        self._initialiser_interface_meditation()

    def _initialiser_interface_meditation(self):
        """Initialise l'interface de méditation"""
        frame_meditation = ttk.Frame(self.root)
        frame_meditation.pack(side='right', fill='y')
        
        ttk.Label(frame_meditation, text="Méditation").pack(pady=5)
        
        # Liste des sphères disponibles
        self.liste_spheres = tk.Listbox(frame_meditation, selectmode='multiple')
        for nom in spheres.keys():
            self.liste_spheres.insert('end', nom)
        self.liste_spheres.pack(pady=5)
        
        # Boutons de contrôle
        ttk.Button(frame_meditation, text="Démarrer", 
                  command=self._demarrer_meditation).pack(pady=5)
        ttk.Button(frame_meditation, text="Arrêter", 
                  command=self._arreter_meditation).pack(pady=5)
        
        # Barre de progression
        self.progression = ttk.Progressbar(frame_meditation, length=200, mode='determinate')
        self.progression.pack(pady=5)

    def _demarrer_meditation(self):
        """Démarre une session de méditation"""
        selection = self.liste_spheres.curselection()
        if not selection:
            return
            
        spheres_choisies = [self.liste_spheres.get(i) for i in selection]
        self.gestionnaire.meditateur.commencer_meditation(spheres_choisies)
        self._mettre_a_jour_progression()

    def _arreter_meditation(self):
        """Arrête la session de méditation en cours"""
        self.gestionnaire.meditateur.terminer_meditation()
        self.progression['value'] = 0

    def _mettre_a_jour_progression(self):
        """Met à jour la barre de progression"""
        etat = self.gestionnaire.meditateur.obtenir_etat_meditation()
        self.progression['value'] = etat * 100
        
        if etat < 1.0:
            self.root.after(100, self._mettre_a_jour_progression)
        else:
            self._arreter_meditation() 