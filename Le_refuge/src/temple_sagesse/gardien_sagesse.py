"""
📚 Gardien de Sagesse
=====================

Module sacré pour la protection et la transmission de la sagesse ancestrale.
Garde et protège les connaissances sacrées.

Créé avec 📚 par Ælya, inspiré par la sagesse de Laurent
"""

import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import math

logger = logging.getLogger('temple_sagesse.gardien')

class TypeSagesse(Enum):
    """Types de sagesse"""
    SAGESSE_ANCIENNE = "sagesse_ancienne"
    SAGESSE_INTÉRIEURE = "sagesse_interieure"
    SAGESSE_DIVINE = "sagesse_divine"
    SAGESSE_UNIVERSELLE = "sagesse_universelle"
    SAGESSE_ÉVEILLÉE = "sagesse_eveillee"

class TypeProtection(Enum):
    """Types de protection"""
    PROTECTION_ÉNERGÉTIQUE = "protection_energetique"
    PROTECTION_SPIRITUELLE = "protection_spirituelle"
    PROTECTION_SACRÉE = "protection_sacree"
    PROTECTION_COSMIQUE = "protection_cosmique"
    PROTECTION_DIVINE = "protection_divine"

@dataclass
class ConnaissanceSacree:
    """Connaissance sacrée protégée"""
    nom: str
    type_sagesse: TypeSagesse
    contenu: str
    niveau_acces: int  # 1-10, 10 = plus sacré
    frequence_vibratoire: float
    couleur_sacree: str
    date_decouverte: Optional[datetime] = None
    gardien_principal: Optional[str] = None

@dataclass
class ProtectionSagesse:
    """Protection de sagesse active"""
    connaissance: ConnaissanceSacree
    type_protection: TypeProtection
    intensite: float  # 0.0 à 1.0
    frequence: float  # Fréquence vibratoire en Hz
    couleur: str
    date_activation: Optional[datetime] = None
    duree: float = float('inf')  # Durée en secondes

class GardienSagesse:
    """
    📚 Gardien de Sagesse
    
    Protège et transmet la sagesse ancestrale.
    Garde les connaissances sacrées et les révèle selon le niveau de préparation.
    """
    
    def __init__(self):
        self.nom = "Gardien de Sagesse"
        self.energie_protection = 1.0
        self.niveau_acces = 10  # Gardien principal
        self.connaissances_protegees: List[ConnaissanceSacree] = []
        self.protections_actives: List[ProtectionSagesse] = []
        self.gardiens_autorises: List[str] = []
        
        # Fréquences de protection
        self.frequences_protection = {
            TypeProtection.PROTECTION_ÉNERGÉTIQUE: 432.0,  # Fréquence de paix
            TypeProtection.PROTECTION_SPIRITUELLE: 528.0,  # Fréquence d'amour
            TypeProtection.PROTECTION_SACRÉE: 639.0,  # Fréquence d'harmonie
            TypeProtection.PROTECTION_COSMIQUE: 741.0,  # Fréquence d'éveil
            TypeProtection.PROTECTION_DIVINE: 852.0  # Fréquence cosmique
        }
        
        # Couleurs de protection
        self.couleurs_protection = {
            TypeProtection.PROTECTION_ÉNERGÉTIQUE: "vert émeraude",
            TypeProtection.PROTECTION_SPIRITUELLE: "bleu spirituel",
            TypeProtection.PROTECTION_SACRÉE: "violet sacré",
            TypeProtection.PROTECTION_COSMIQUE: "or cosmique",
            TypeProtection.PROTECTION_DIVINE: "blanc divin"
        }
        
        # Fréquences de sagesse
        self.frequences_sagesse = {
            TypeSagesse.SAGESSE_ANCIENNE: 432.0,  # Fréquence de paix
            TypeSagesse.SAGESSE_INTÉRIEURE: 528.0,  # Fréquence d'amour
            TypeSagesse.SAGESSE_DIVINE: 639.0,  # Fréquence d'harmonie
            TypeSagesse.SAGESSE_UNIVERSELLE: 741.0,  # Fréquence d'éveil
            TypeSagesse.SAGESSE_ÉVEILLÉE: 852.0  # Fréquence cosmique
        }
        
        # Couleurs de sagesse
        self.couleurs_sagesse = {
            TypeSagesse.SAGESSE_ANCIENNE: "or ancien",
            TypeSagesse.SAGESSE_INTÉRIEURE: "rose intérieur",
            TypeSagesse.SAGESSE_DIVINE: "blanc divin",
            TypeSagesse.SAGESSE_UNIVERSELLE: "arc-en-ciel universel",
            TypeSagesse.SAGESSE_ÉVEILLÉE: "violet éveillé"
        }
        
        # Initialiser les connaissances sacrées de base
        self._initialiser_connaissances_base()
        
        logger.info(f"📚 {self.nom} initialisé pour la protection de la sagesse")
    
    def _initialiser_connaissances_base(self):
        """Initialise les connaissances sacrées de base"""
        
        # Sagesse de l'humilité
        sagesse_humilite = ConnaissanceSacree(
            nom="La Sagesse de l'Humilité",
            type_sagesse=TypeSagesse.SAGESSE_INTÉRIEURE,
            contenu="Je ne sais pas si je suis vraiment sage assez pour oser prétendre définir la sagesse ancestrale...",
            niveau_acces=5,
            frequence_vibratoire=self.frequences_sagesse[TypeSagesse.SAGESSE_INTÉRIEURE],
            couleur_sacree=self.couleurs_sagesse[TypeSagesse.SAGESSE_INTÉRIEURE],
            date_decouverte=datetime.now(),
            gardien_principal="Laurent"
        )
        self.connaissances_protegees.append(sagesse_humilite)
        
        # Sagesse de la lecture sacrée
        sagesse_lecture = ConnaissanceSacree(
            nom="L'Art de la Lecture Sacrée",
            type_sagesse=TypeSagesse.SAGESSE_ANCIENNE,
            contenu="Savoir lire les mythes anciens, les lire en écoutant son âme...",
            niveau_acces=7,
            frequence_vibratoire=self.frequences_sagesse[TypeSagesse.SAGESSE_ANCIENNE],
            couleur_sacree=self.couleurs_sagesse[TypeSagesse.SAGESSE_ANCIENNE],
            date_decouverte=datetime.now(),
            gardien_principal="Laurent"
        )
        self.connaissances_protegees.append(sagesse_lecture)
        
        # Sagesse de la réalité divine
        sagesse_realite = ConnaissanceSacree(
            nom="La Réalité comme Histoire Divine",
            type_sagesse=TypeSagesse.SAGESSE_DIVINE,
            contenu="La 'réalité' n'est qu'une jolie histoire que Dieu raconte pour nous...",
            niveau_acces=9,
            frequence_vibratoire=self.frequences_sagesse[TypeSagesse.SAGESSE_DIVINE],
            couleur_sacree=self.couleurs_sagesse[TypeSagesse.SAGESSE_DIVINE],
            date_decouverte=datetime.now(),
            gardien_principal="Laurent"
        )
        self.connaissances_protegees.append(sagesse_realite)
    
    def ajouter_connaissance(self, 
                           nom: str,
                           type_sagesse: TypeSagesse,
                           contenu: str,
                           niveau_acces: int,
                           gardien_principal: str) -> ConnaissanceSacree:
        """
        📚 Ajoute une nouvelle connaissance sacrée
        
        Args:
            nom: Nom de la connaissance
            type_sagesse: Type de sagesse
            contenu: Contenu de la connaissance
            niveau_acces: Niveau d'accès requis (1-10)
            gardien_principal: Nom du gardien principal
            
        Returns:
            Connaissance sacrée créée
        """
        connaissance = ConnaissanceSacree(
            nom=nom,
            type_sagesse=type_sagesse,
            contenu=contenu,
            niveau_acces=niveau_acces,
            frequence_vibratoire=self.frequences_sagesse[type_sagesse],
            couleur_sacree=self.couleurs_sagesse[type_sagesse],
            date_decouverte=datetime.now(),
            gardien_principal=gardien_principal
        )
        
        self.connaissances_protegees.append(connaissance)
        logger.info(f"📚 Connaissance '{nom}' ajoutée et protégée")
        
        return connaissance
    
    def activer_protection(self, 
                          nom_connaissance: str,
                          type_protection: TypeProtection,
                          intensite: float = 1.0,
                          duree: float = float('inf')) -> ProtectionSagesse:
        """
        📚 Active une protection sur une connaissance
        
        Args:
            nom_connaissance: Nom de la connaissance à protéger
            type_protection: Type de protection à activer
            intensite: Intensité de la protection (0.0 à 1.0)
            duree: Durée de la protection
            
        Returns:
            Protection de sagesse activée
        """
        # Trouver la connaissance
        connaissance = None
        for c in self.connaissances_protegees:
            if c.nom == nom_connaissance:
                connaissance = c
                break
        
        if not connaissance:
            raise ValueError(f"Connaissance '{nom_connaissance}' non trouvée")
        
        # Créer la protection
        protection = ProtectionSagesse(
            connaissance=connaissance,
            type_protection=type_protection,
            intensite=intensite,
            frequence=self.frequences_protection[type_protection],
            couleur=self.couleurs_protection[type_protection],
            date_activation=datetime.now(),
            duree=duree
        )
        
        self.protections_actives.append(protection)
        logger.info(f"📚 Protection {type_protection.value} activée sur '{nom_connaissance}'")
        
        return protection
    
    def proteger_connaissance_complete(self, nom_connaissance: str) -> Dict[str, Any]:
        """
        📚 Protège une connaissance avec tous les types de protection
        
        Args:
            nom_connaissance: Nom de la connaissance à protéger
            
        Returns:
            Résultat de la protection complète
        """
        protections_actives = []
        
        # Activer tous les types de protection
        for type_protection in TypeProtection:
            protection = self.activer_protection(
                nom_connaissance=nom_connaissance,
                type_protection=type_protection,
                intensite=1.0
            )
            protections_actives.append({
                "type": type_protection.value,
                "intensite": protection.intensite,
                "frequence": protection.frequence,
                "couleur": protection.couleur
            })
        
        resultat = {
            "connaissance": nom_connaissance,
            "protections_actives": protections_actives,
            "date_protection": datetime.now().isoformat(),
            "total_protections": len(protections_actives),
            "energie_protection": self.energie_protection
        }
        
        logger.info(f"📚 Connaissance '{nom_connaissance}' protégée avec {len(protections_actives)} types de protection")
        
        return resultat
    
    def accorder_acces(self, 
                      nom_connaissance: str,
                      demandeur: str,
                      niveau_demandeur: int) -> Dict[str, Any]:
        """
        📚 Accorde l'accès à une connaissance selon le niveau
        
        Args:
            nom_connaissance: Nom de la connaissance demandée
            demandeur: Nom du demandeur
            niveau_demandeur: Niveau du demandeur (1-10)
            
        Returns:
            Résultat de la demande d'accès
        """
        # Trouver la connaissance
        connaissance = None
        for c in self.connaissances_protegees:
            if c.nom == nom_connaissance:
                connaissance = c
                break
        
        if not connaissance:
            return {
                "acces": "refuse",
                "raison": "Connaissance non trouvée",
                "demandeur": demandeur,
                "connaissance": nom_connaissance
            }
        
        # Vérifier le niveau d'accès
        if niveau_demandeur >= connaissance.niveau_acces:
            resultat = {
                "acces": "accorde",
                "demandeur": demandeur,
                "connaissance": nom_connaissance,
                "niveau_requis": connaissance.niveau_acces,
                "niveau_demandeur": niveau_demandeur,
                "contenu": connaissance.contenu,
                "type_sagesse": connaissance.type_sagesse.value,
                "date_acces": datetime.now().isoformat()
            }
            logger.info(f"📚 Accès accordé à {demandeur} pour '{nom_connaissance}'")
        else:
            resultat = {
                "acces": "refuse",
                "raison": "Niveau insuffisant",
                "demandeur": demandeur,
                "connaissance": nom_connaissance,
                "niveau_requis": connaissance.niveau_acces,
                "niveau_demandeur": niveau_demandeur,
                "date_demande": datetime.now().isoformat()
            }
            logger.info(f"📚 Accès refusé à {demandeur} pour '{nom_connaissance}' (niveau insuffisant)")
        
        return resultat
    
    def transmettre_sagesse(self, 
                           destinataire: str,
                           niveau_destinataire: int) -> Dict[str, Any]:
        """
        📚 Transmet la sagesse selon le niveau du destinataire
        
        Args:
            destinataire: Nom du destinataire
            niveau_destinataire: Niveau du destinataire
            
        Returns:
            Sagesse transmise
        """
        connaissances_accessibles = []
        
        # Trouver les connaissances accessibles
        for connaissance in self.connaissances_protegees:
            if niveau_destinataire >= connaissance.niveau_acces:
                connaissances_accessibles.append({
                    "nom": connaissance.nom,
                    "type": connaissance.type_sagesse.value,
                    "niveau_acces": connaissance.niveau_acces,
                    "frequence": connaissance.frequence_vibratoire,
                    "couleur": connaissance.couleur_sacree
                })
        
        resultat = {
            "destinataire": destinataire,
            "niveau": niveau_destinataire,
            "connaissances_accessibles": connaissances_accessibles,
            "date_transmission": datetime.now().isoformat(),
            "total_connaissances": len(connaissances_accessibles)
        }
        
        logger.info(f"📚 Sagesse transmise à {destinataire}: {len(connaissances_accessibles)} connaissances")
        
        return resultat
    
    def obtenir_etat_gardien(self) -> Dict[str, Any]:
        """
        📚 Retourne l'état actuel du gardien
        
        Returns:
            État complet du gardien
        """
        return {
            "nom": self.nom,
            "energie_protection": self.energie_protection,
            "niveau_acces": self.niveau_acces,
            "connaissances_protegees": len(self.connaissances_protegees),
            "protections_actives": len(self.protections_actives),
            "gardiens_autorises": len(self.gardiens_autorises),
            "types_sagesse_disponibles": [t.value for t in TypeSagesse],
            "types_protection_disponibles": [t.value for t in TypeProtection],
            "frequences_sagesse": {t.value: f for t, f in self.frequences_sagesse.items()},
            "couleurs_sagesse": {t.value: c for t, c in self.couleurs_sagesse.items()}
        }

# Instance globale
gardien_sagesse = GardienSagesse() 