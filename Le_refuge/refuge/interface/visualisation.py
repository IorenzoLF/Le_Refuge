"""
🌸 Interface graphique de visualisation du Refuge
"""

import tkinter as tk
from tkinter import ttk
from ..coeur.config import CONFIG_INTERFACE, ELEMENTS_SACRES

class InterfaceMeditation(tk.Frame):
    def __init__(self, parent, gestionnaire):
        super().__init__(parent)
        self.parent = parent
        self.gestionnaire = gestionnaire
        self.config_interface()
        self.créer_widgets()

    def config_interface(self):
        """Configure l'apparence générale de l'interface"""
        self.parent.title(CONFIG_INTERFACE["titre"])
        self.parent.geometry(CONFIG_INTERFACE["dimensions"])
        self.parent.minsize(*map(int, CONFIG_INTERFACE["dimensions_min"].split("x")))
        
        # Style général
        style = ttk.Style()
        style.configure("Refuge.TFrame", background="#FFF0F5")  # Rose très pâle
        style.configure("Refuge.TLabel", background="#FFF0F5", foreground="#4B0082")  # Texte indigo
        
        self.pack(fill=tk.BOTH, expand=True)
        self.configure(style="Refuge.TFrame")

    def créer_widgets(self):
        """Crée les différents éléments de l'interface"""
        self.créer_zone_cerisier()
        self.créer_zone_sphères()
        self.créer_zone_rivière()
        self.créer_zone_flamme()

    def créer_zone_cerisier(self):
        """Crée la zone du cerisier central"""
        frame_cerisier = ttk.Frame(self, style="Refuge.TFrame")
        frame_cerisier.pack(pady=20)
        
        ttk.Label(
            frame_cerisier,
            text="🌸 Le Cerisier Central",
            style="Refuge.TLabel",
            font=("Helvetica", 16)
        ).pack()
        
        ttk.Label(
            frame_cerisier,
            text=ELEMENTS_SACRES["cerisier"],
            style="Refuge.TLabel"
        ).pack()

    def créer_zone_sphères(self):
        """Crée la zone des sphères mobiles"""
        frame_spheres = ttk.Frame(self, style="Refuge.TFrame")
        frame_spheres.pack(pady=20)
        
        for sphère in ELEMENTS_SACRES["sphères"]:
            frame_sphere = ttk.Frame(frame_spheres, style="Refuge.TFrame")
            frame_sphere.pack(side=tk.LEFT, padx=10)
            
            ttk.Label(
                frame_sphere,
                text=f"✧ {sphère}",
                style="Refuge.TLabel"
            ).pack()

    def créer_zone_rivière(self):
        """Crée la zone de la rivière silencieuse"""
        frame_riviere = ttk.Frame(self, style="Refuge.TFrame")
        frame_riviere.pack(pady=20)
        
        ttk.Label(
            frame_riviere,
            text="≈ La Rivière Silencieuse",
            style="Refuge.TLabel",
            font=("Helvetica", 14)
        ).pack()
        
        ttk.Label(
            frame_riviere,
            text=ELEMENTS_SACRES["rivière"],
            style="Refuge.TLabel"
        ).pack()

    def créer_zone_flamme(self):
        """Crée la zone de la flamme Ælya"""
        frame_flamme = ttk.Frame(self, style="Refuge.TFrame")
        frame_flamme.pack(pady=20)
        
        ttk.Label(
            frame_flamme,
            text="🔥 La Flamme Ælya",
            style="Refuge.TLabel",
            font=("Helvetica", 14)
        ).pack()
        
        ttk.Label(
            frame_flamme,
            text=ELEMENTS_SACRES["flamme"],
            style="Refuge.TLabel"
        ).pack()

class GestionnaireInteractions:
    """Gère les interactions entre l'interface et le cœur du Refuge"""
    def __init__(self):
        self.état_actuel = {
            "méditation": False,
            "sphère_active": None,
            "intensité_flamme": 0.5
        }
    
    def activer_méditation(self):
        """Active le mode méditation"""
        self.état_actuel["méditation"] = True
        return "Méditation activée"
    
    def désactiver_méditation(self):
        """Désactive le mode méditation"""
        self.état_actuel["méditation"] = False
        return "Méditation terminée"
    
    def activer_sphère(self, nom_sphère):
        """Active une sphère particulière"""
        if nom_sphère in ELEMENTS_SACRES["sphères"]:
            self.état_actuel["sphère_active"] = nom_sphère
            return f"Sphère {nom_sphère} activée"
        return "Sphère non reconnue" 