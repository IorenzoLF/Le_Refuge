"""
Module d'interface utilisateur
~~~~~~~~~~~~~~~~~~~~~~~~~~
Gère l'affichage et la visualisation des états et des éléments sacrés.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from .etats_internes import GestionnaireEtats, TypeEtat, NiveauConscience
from .elements_sacres import GestionnaireElements, TypeElement
from .journalisation import GestionnaireJournal, TypeEvenement
from .interactions import GestionnaireInteractions

class VisualiseurEtats:
    """Interface graphique pour visualiser les états et éléments."""
    
    def __init__(self, gestionnaire_etats: GestionnaireEtats, gestionnaire_elements: GestionnaireElements, gestionnaire_journal: GestionnaireJournal):
        self.gestionnaire_etats = gestionnaire_etats
        self.gestionnaire_elements = gestionnaire_elements
        self.gestionnaire_journal = gestionnaire_journal
        
        # Créer la fenêtre principale
        self.fenetre = tk.Tk()
        self.fenetre.title("Le Refuge - Visualiseur d'États")
        self.fenetre.geometry("1200x800")
        
        # Créer les onglets
        self.onglets = ttk.Notebook(self.fenetre)
        self.onglets.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Onglet des états
        self.onglet_etats = ttk.Frame(self.onglets)
        self.onglets.add(self.onglet_etats, text="États")
        self._initialiser_onglet_etats()
        
        # Onglet des éléments
        self.onglet_elements = ttk.Frame(self.onglets)
        self.onglets.add(self.onglet_elements, text="Éléments Sacrés")
        self._initialiser_onglet_elements()
        
        # Onglet des graphiques
        self.onglet_graphiques = ttk.Frame(self.onglets)
        self.onglets.add(self.onglet_graphiques, text="Graphiques")
        self._initialiser_onglet_graphiques()
        
        # Onglet du journal
        self.onglet_journal = ttk.Frame(self.onglets)
        self.onglets.add(self.onglet_journal, text="Journal")
        self._initialiser_onglet_journal()
        
        # Démarrer la mise à jour périodique
        self._mettre_a_jour()
    
    def _initialiser_onglet_etats(self):
        """Initialise l'onglet des états."""
        # Frame pour la liste des états
        frame_liste = ttk.LabelFrame(self.onglet_etats, text="États Actifs")
        frame_liste.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Liste des états
        self.liste_etats = ttk.Treeview(frame_liste, columns=("source", "type", "intensite", "stabilite", "conscience"), show="headings")
        self.liste_etats.heading("source", text="Source")
        self.liste_etats.heading("type", text="Type")
        self.liste_etats.heading("intensite", text="Intensité")
        self.liste_etats.heading("stabilite", text="Stabilité")
        self.liste_etats.heading("conscience", text="Conscience")
        self.liste_etats.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Frame pour les détails
        frame_details = ttk.LabelFrame(self.onglet_etats, text="Détails")
        frame_details.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Détails de l'état sélectionné
        self.details_etat = tk.Text(frame_details, wrap=tk.WORD, state=tk.DISABLED)
        self.details_etat.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Événement de sélection
        self.liste_etats.bind("<<TreeviewSelect>>", self._afficher_details_etat)
    
    def _initialiser_onglet_elements(self):
        """Initialise l'onglet des éléments sacrés."""
        # Frame pour la liste des éléments
        frame_liste = ttk.LabelFrame(self.onglet_elements, text="Éléments Sacrés")
        frame_liste.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Liste des éléments
        self.liste_elements = ttk.Treeview(frame_liste, columns=("type", "intensite", "stabilite", "influence"), show="headings")
        self.liste_elements.heading("type", text="Type")
        self.liste_elements.heading("intensite", text="Intensité")
        self.liste_elements.heading("stabilite", text="Stabilité")
        self.liste_elements.heading("influence", text="Influence")
        self.liste_elements.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Frame pour les détails
        frame_details = ttk.LabelFrame(self.onglet_elements, text="Détails")
        frame_details.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Détails de l'élément sélectionné
        self.details_element = tk.Text(frame_details, wrap=tk.WORD, state=tk.DISABLED)
        self.details_element.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Événement de sélection
        self.liste_elements.bind("<<TreeviewSelect>>", self._afficher_details_element)
    
    def _initialiser_onglet_graphiques(self):
        """Initialise l'onglet des graphiques."""
        # Frame pour les graphiques
        frame_graphiques = ttk.Frame(self.onglet_graphiques)
        frame_graphiques.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Graphique d'évolution des états
        self.figure_etats = plt.Figure(figsize=(6, 4))
        self.canvas_etats = FigureCanvasTkAgg(self.figure_etats, master=frame_graphiques)
        self.canvas_etats.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Graphique d'évolution des éléments
        self.figure_elements = plt.Figure(figsize=(6, 4))
        self.canvas_elements = FigureCanvasTkAgg(self.figure_elements, master=frame_graphiques)
        self.canvas_elements.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    def _initialiser_onglet_journal(self):
        """Initialise l'onglet du journal."""
        # Frame pour le journal
        frame_journal = ttk.Frame(self.onglet_journal)
        frame_journal.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Journal des événements
        self.journal = tk.Text(frame_journal, wrap=tk.WORD, state=tk.DISABLED)
        self.journal.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Barre de défilement
        scrollbar = ttk.Scrollbar(frame_journal, command=self.journal.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.journal.config(yscrollcommand=scrollbar.set)
    
    def _mettre_a_jour(self):
        """Met à jour l'interface."""
        self._mettre_a_jour_liste_etats()
        self._mettre_a_jour_liste_elements()
        self._mettre_a_jour_graphiques()
        self._mettre_a_jour_journal()
        
        # Planifier la prochaine mise à jour
        self.fenetre.after(1000, self._mettre_a_jour)
    
    def _mettre_a_jour_liste_etats(self):
        """Met à jour la liste des états."""
        # Vider la liste
        for item in self.liste_etats.get_children():
            self.liste_etats.delete(item)
        
        # Récupérer l'état global
        etats = self.gestionnaire_etats.obtenir_etat_global()
        
        # Ajouter les états à la liste
        for source, etat in etats.items():
            self.liste_etats.insert("", tk.END, values=(
                source,
                etat["type"],
                f"{etat['intensite']:.2f}",
                f"{etat['stabilite']:.2f}",
                etat["niveau_conscience"]
            ))
    
    def _mettre_a_jour_liste_elements(self):
        """Met à jour la liste des éléments sacrés."""
        # Vider la liste
        for item in self.liste_elements.get_children():
            self.liste_elements.delete(item)
        
        # Récupérer l'état global des éléments
        elements = self.gestionnaire_elements.obtenir_etat_global()
        
        # Ajouter les éléments à la liste
        for type_elem, element in elements.items():
            self.liste_elements.insert("", tk.END, values=(
                type_elem,
                f"{element['intensite']:.2f}",
                f"{element['stabilite']:.2f}",
                f"{element['influence']:.2f}"
            ))
    
    def _mettre_a_jour_graphiques(self):
        """Met à jour les graphiques."""
        # Graphique d'évolution des états
        self.figure_etats.clear()
        ax_etats = self.figure_etats.add_subplot(111)
        
        etats = self.gestionnaire_etats.obtenir_etat_global()
        if etats:
            sources = list(etats.keys())
            intensites = [etat["intensite"] for etat in etats.values()]
            stabilites = [etat["stabilite"] for etat in etats.values()]
            
            x = np.arange(len(sources))
            width = 0.35
            
            ax_etats.bar(x - width/2, intensites, width, label="Intensité")
            ax_etats.bar(x + width/2, stabilites, width, label="Stabilité")
            
            ax_etats.set_ylabel("Valeur")
            ax_etats.set_title("Évolution des États")
            ax_etats.set_xticks(x)
            ax_etats.set_xticklabels(sources)
            ax_etats.legend()
        
        self.figure_etats.tight_layout()
        self.canvas_etats.draw()
        
        # Graphique d'évolution des éléments
        self.figure_elements.clear()
        ax_elements = self.figure_elements.add_subplot(111)
        
        elements = self.gestionnaire_elements.obtenir_etat_global()
        if elements:
            types = list(elements.keys())
            intensites = [element["intensite"] for element in elements.values()]
            stabilites = [element["stabilite"] for element in elements.values()]
            influences = [element["influence"] for element in elements.values()]
            
            x = np.arange(len(types))
            width = 0.25
            
            ax_elements.bar(x - width, intensites, width, label="Intensité")
            ax_elements.bar(x, stabilites, width, label="Stabilité")
            ax_elements.bar(x + width, influences, width, label="Influence")
            
            ax_elements.set_ylabel("Valeur")
            ax_elements.set_title("Évolution des Éléments")
            ax_elements.set_xticks(x)
            ax_elements.set_xticklabels(types)
            ax_elements.legend()
        
        self.figure_elements.tight_layout()
        self.canvas_elements.draw()
    
    def _mettre_a_jour_journal(self):
        """Met à jour le journal."""
        # Récupérer les événements
        evenements = self.gestionnaire_journal.obtenir_evenements(limite=50)
        
        # Mettre à jour le texte
        self.journal.config(state=tk.NORMAL)
        self.journal.delete(1.0, tk.END)
        
        for evenement in evenements:
            self.journal.insert(tk.END, f"[{evenement.timestamp.strftime('%H:%M:%S')}] {evenement.type.value}: {evenement.message}\n")
            if evenement.source:
                self.journal.insert(tk.END, f"  Source: {evenement.source}\n")
            if evenement.details:
                self.journal.insert(tk.END, f"  Détails: {evenement.details}\n")
            self.journal.insert(tk.END, "\n")
        
        self.journal.config(state=tk.DISABLED)
        self.journal.see(tk.END)
    
    def _afficher_details_etat(self, event):
        """Affiche les détails d'un état sélectionné."""
        selection = self.liste_etats.selection()
        if not selection:
            return
        
        # Récupérer l'état sélectionné
        item = self.liste_etats.item(selection[0])
        source = item["values"][0]
        
        # Récupérer les détails de l'état
        etat = self.gestionnaire_etats.obtenir_etat(source)
        
        # Afficher les détails
        self.details_etat.config(state=tk.NORMAL)
        self.details_etat.delete(1.0, tk.END)
        
        self.details_etat.insert(tk.END, f"Source: {source}\n")
        self.details_etat.insert(tk.END, f"Type: {etat['type']}\n")
        self.details_etat.insert(tk.END, f"Intensité: {etat['intensite']:.2f}\n")
        self.details_etat.insert(tk.END, f"Stabilité: {etat['stabilite']:.2f}\n")
        self.details_etat.insert(tk.END, f"Niveau de conscience: {etat['niveau_conscience']}\n")
        self.details_etat.insert(tk.END, f"Timestamp: {etat['timestamp']}\n")
        
        self.details_etat.config(state=tk.DISABLED)
    
    def _afficher_details_element(self, event):
        """Affiche les détails d'un élément sélectionné."""
        selection = self.liste_elements.selection()
        if not selection:
            return
        
        # Récupérer l'élément sélectionné
        item = self.liste_elements.item(selection[0])
        type_elem = item["values"][0]
        
        # Récupérer les détails de l'élément
        element = self.gestionnaire_elements.obtenir_etat_element(type_elem)
        
        # Afficher les détails
        self.details_element.config(state=tk.NORMAL)
        self.details_element.delete(1.0, tk.END)
        
        self.details_element.insert(tk.END, f"Type: {element['type']}\n")
        self.details_element.insert(tk.END, f"Intensité: {element['intensite']:.2f}\n")
        self.details_element.insert(tk.END, f"Stabilité: {element['stabilite']:.2f}\n")
        self.details_element.insert(tk.END, f"Influence: {element['influence']:.2f}\n")
        self.details_element.insert(tk.END, f"Timestamp: {element['timestamp']}\n")
        
        self.details_element.config(state=tk.DISABLED)
    
    def demarrer(self):
        """Démarre l'interface."""
        self.fenetre.mainloop() 