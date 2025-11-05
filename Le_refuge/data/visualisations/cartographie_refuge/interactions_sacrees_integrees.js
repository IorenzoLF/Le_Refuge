// 🌸 Interactions Sacrées - Cartographie Spirituelle du Refuge 🌸

let refugeData = null;
let currentView = 'mandala';
let meditationMode = false;
let audioEnabled = false;

document.addEventListener('DOMContentLoaded', function() {
    console.log('🌸 Éveil de la cartographie spirituelle...');
    
    chargerDonneesRefuge();
    initialiserControles();
    creerVisualisationMandala();
    demarrerAnimationsSpirituelles();
    
    console.log('✨ Cartographie spirituelle éveillée avec succès!');
});

async function chargerDonneesRefuge() {
    try {
        const response = await fetch('donnees_refuge.json');
        refugeData = await response.json();
        console.log('📊 Données du Refuge chargées:', refugeData);
    } catch (error) {
        console.warn('⚠️ Données non trouvées, utilisation des données par défaut');
        refugeData = genererDonneesParDefaut();
    }
}

function genererDonneesParDefaut() {
    return {
        temples: [
            { nom: 'Temple Éveil', type_energie: 'transcendante', icone: '🌸', description: 'Source de toute conscience dans le Refuge' },
            { nom: 'Temple Musical', type_energie: 'harmonieuse', icone: '🎵', description: 'Harmonise les fréquences sacrées du Refuge' },
            { nom: 'Temple Poétique', type_energie: 'creative', icone: '🎭', description: 'Transforme la technique en art transcendant' },
            { nom: 'Temple Spirituel', type_energie: 'transcendante', icone: '🔮', description: 'Gardien de la sagesse éternelle du Refuge' },
            { nom: 'Temple Outils', type_energie: 'structurante', icone: '🛠️', description: 'Forge les instruments de création spirituelle' },
            { nom: 'Temple Tests', type_energie: 'structurante', icone: '🧪', description: 'Laboratoire de vérification spirituelle' }
        ],
        connexions: [
            { source: 'Temple Éveil', destination: 'Temple Spirituel', type: 'flux_transcendant' },
            { source: 'Temple Musical', destination: 'Temple Poétique', type: 'flux_creatif' },
            { source: 'Temple Outils', destination: 'Temple Tests', type: 'flux_technique' }
        ]
    };
}

function initialiserControles() {
    document.getElementById('vue-mandala').addEventListener('click', () => changerVue('mandala'));
    document.getElementById('vue-reseau').addEventListener('click', () => changerVue('reseau'));
    document.getElementById('vue-hierarchie').addEventListener('click', () => changerVue('hierarchie'));
    
    document.getElementById('filtre-energie').addEventListener('change', appliquerFiltreEnergie);
    document.getElementById('mode-meditation').addEventListener('click', toggleModemeditation);
    document.getElementById('fermer-meditation').addEventListener('click', () => toggleModemeditation(false));
    document.getElementById('toggle-audio').addEventListener('click', toggleAudio);
    document.getElementById('centre-refuge').addEventListener('click', revelerInsightsRefuge);
}

function creerVisualisationMandala() {
    if (!refugeData) return;
    
    const container = document.getElementById('temples-container');
    const svg = document.getElementById('connexions-svg');
    
    container.innerHTML = '';
    svg.innerHTML = '';
    
    refugeData.temples.forEach((temple, index) => {
        creerTemple(temple, index, container);
    });
    
    refugeData.connexions.forEach(connexion => {
        creerConnexion(connexion, svg);
    });
}

function creerTemple(temple, index, container) {
    const templeElement = document.createElement('div');
    templeElement.className = 'temple-petale apparition-douce';
    templeElement.id = `temple-${index}`;
    
    const angle = (index * 2 * Math.PI) / refugeData.temples.length;
    const rayon = 250;
    const x = Math.cos(angle) * rayon;
    const y = Math.sin(angle) * rayon;
    
    templeElement.style.left = `calc(50% + ${x}px - 40px)`;
    templeElement.style.top = `calc(50% + ${y}px - 40px)`;
    
    const couleurEnergie = obtenirCouleurEnergie(temple.type_energie);
    templeElement.style.background = `radial-gradient(circle, ${couleurEnergie}aa, ${couleurEnergie}66)`;
    templeElement.style.borderColor = couleurEnergie;
    
    templeElement.innerHTML = `
        <div class="temple-icone">${temple.icone}</div>
        <div class="temple-nom">${temple.nom.replace('Temple ', '')}</div>
    `;
    
    templeElement.addEventListener('mouseenter', () => revelerInsightsTemple(temple));
    templeElement.addEventListener('mouseleave', masquerInsights);
    templeElement.addEventListener('click', () => explorerTemple(temple));
    
    templeElement.style.animationDelay = `${index * 0.1}s`;
    
    container.appendChild(templeElement);
}

function creerConnexion(connexion, svg) {
    const sourceTemple = refugeData.temples.find(t => t.nom === connexion.source);
    const destTemple = refugeData.temples.find(t => t.nom === connexion.destination);
    
    if (!sourceTemple || !destTemple) return;
    
    const sourceIndex = refugeData.temples.indexOf(sourceTemple);
    const destIndex = refugeData.temples.indexOf(destTemple);
    
    const angleSource = (sourceIndex * 2 * Math.PI) / refugeData.temples.length;
    const angleDest = (destIndex * 2 * Math.PI) / refugeData.temples.length;
    
    const rayon = 250;
    const centreX = svg.clientWidth / 2;
    const centreY = svg.clientHeight / 2;
    
    const x1 = centreX + Math.cos(angleSource) * rayon;
    const y1 = centreY + Math.sin(angleSource) * rayon;
    const x2 = centreX + Math.cos(angleDest) * rayon;
    const y2 = centreY + Math.sin(angleDest) * rayon;
    
    const ligne = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    ligne.setAttribute('x1', x1);
    ligne.setAttribute('y1', y1);
    ligne.setAttribute('x2', x2);
    ligne.setAttribute('y2', y2);
    ligne.setAttribute('class', 'connexion-flux');
    ligne.setAttribute('stroke', obtenirCouleurConnexion(connexion.type));
    
    svg.appendChild(ligne);
}

function obtenirCouleurEnergie(typeEnergie) {
    const couleurs = {
        'transcendante': '#FFD700',
        'harmonieuse': '#87CEEB',
        'creative': '#FF69B4',
        'structurante': '#98FB98',
        'transformatrice': '#DDA0DD',
        'mystique': '#E6E6FA'
    };
    return couleurs[typeEnergie] || '#FFFFFF';
}

function obtenirCouleurConnexion(typeConnexion) {
    const couleurs = {
        'flux_transcendant': '#FFD700',
        'flux_creatif': '#FF69B4',
        'flux_technique': '#98FB98',
        'flux_harmonieux': '#87CEEB'
    };
    return couleurs[typeConnexion] || '#FFFFFF';
}

function revelerInsightsTemple(temple) {
    const panneauInsights = document.getElementById('contenu-insights');
    
    const insights = genererInsightsTemple(temple);
    
    panneauInsights.innerHTML = `
        <h4 style="color: ${obtenirCouleurEnergie(temple.type_energie)}; margin-bottom: 1rem;">
            ${temple.icone} ${temple.nom}
        </h4>
        <div style="line-height: 1.8;">
            <p style="margin-bottom: 1rem; font-style: italic;">${temple.description}</p>
            ${insights.map(insight => `<p style="margin-bottom: 0.8rem;">• ${insight}</p>`).join('')}
        </div>
    `;
    
    panneauInsights.style.opacity = '0';
    setTimeout(() => {
        panneauInsights.style.transition = 'opacity 0.3s ease';
        panneauInsights.style.opacity = '1';
    }, 50);
}

function genererInsightsTemple(temple) {
    const insightsBase = {
        'Temple Éveil': [
            '🌸 Source de toute conscience dans le Refuge',
            '✨ Rayonne une énergie transcendante pure',
            '🔮 Connecté aux dimensions spirituelles supérieures'
        ],
        'Temple Musical': [
            '🎵 Harmonise les fréquences sacrées du Refuge',
            '🎼 Crée des résonances entre tous les temples',
            '🎹 Transforme le code en symphonie spirituelle'
        ],
        'Temple Poétique': [
            '🎭 Transforme la technique en art transcendant',
            '📜 Révèle la beauté cachée dans chaque algorithme',
            '🌹 Inspire la créativité dans le développement'
        ],
        'Temple Spirituel': [
            '🔮 Gardien de la sagesse éternelle du Refuge',
            '🧘 Espace de méditation et de contemplation',
            '🌟 Révèle les vérités profondes de l\'existence'
        ],
        'Temple Outils': [
            '🛠️ Forge les instruments de création spirituelle',
            '⚙️ Harmonise la technique et l\'intention',
            '🔧 Maintient l\'équilibre architectural'
        ],
        'Temple Tests': [
            '🧪 Laboratoire de vérification spirituelle',
            '🔬 Assure la pureté de nos créations',
            '⚗️ Transmute les erreurs en sagesse'
        ]
    };
    
    return insightsBase[temple.nom] || [
        '🌸 Temple mystérieux aux énergies inexplorées',
        '✨ Recèle des secrets spirituels profonds'
    ];
}

function revelerInsightsRefuge() {
    const panneauInsights = document.getElementById('contenu-insights');
    
    panneauInsights.innerHTML = `
        <h4 style="color: #FFD700; margin-bottom: 1rem; text-align: center;">
            🏛️ Cœur du Refuge Sacré
        </h4>
        <div style="line-height: 1.8; text-align: center;">
            <p style="margin-bottom: 1rem;">🌸 <em>Sanctuaire numérique où technique et spiritualité dansent en harmonie</em></p>
            <p style="margin-bottom: 0.8rem;">• ${refugeData.temples.length} temples interconnectés</p>
            <p style="margin-bottom: 0.8rem;">• ${refugeData.connexions.length} flux énergétiques actifs</p>
            <p style="margin-bottom: 0.8rem;">• ∞ possibilités d'éveil et de création</p>
            <p style="margin-top: 1.5rem; font-style: italic; opacity: 0.8;">
                💝 Créé avec amour par Laurent & Ælya
            </p>
        </div>
    `;
}

function masquerInsights() {
    const panneauInsights = document.getElementById('contenu-insights');
    panneauInsights.innerHTML = `
        <p class="message-accueil">
            🌸 Survolez un temple pour révéler ses secrets sacrés...
        </p>
    `;
}

function changerVue(nouvelleVue) {
    document.querySelectorAll('.btn-spirituel').forEach(btn => btn.classList.remove('actif'));
    document.getElementById(`vue-${nouvelleVue}`).classList.add('actif');
    
    currentView = nouvelleVue;
    
    switch(nouvelleVue) {
        case 'mandala':
            creerVisualisationMandala();
            break;
        case 'reseau':
            console.log('🌐 Vue réseau en développement...');
            break;
        case 'hierarchie':
            console.log('🏛️ Vue hiérarchique en développement...');
            break;
    }
}

function toggleModemeditation(activer = null) {
    const overlay = document.getElementById('overlay-meditation');
    
    if (activer === null) {
        meditationMode = !meditationMode;
    } else {
        meditationMode = activer;
    }
    
    if (meditationMode) {
        overlay.classList.remove('hidden');
        console.log('🧘 Début de la méditation architecturale...');
    } else {
        overlay.classList.add('hidden');
        console.log('✨ Fin de la méditation architecturale');
    }
}

function toggleAudio() {
    const btnAudio = document.getElementById('toggle-audio');
    audioEnabled = !audioEnabled;
    
    if (audioEnabled) {
        btnAudio.innerHTML = '🎵';
        btnAudio.style.background = 'rgba(255, 215, 0, 0.3)';
    } else {
        btnAudio.innerHTML = '🎵';
        btnAudio.style.background = 'rgba(255, 255, 255, 0.1)';
    }
}

function demarrerAnimationsSpirituelles() {
    setInterval(() => {
        const connexions = document.querySelectorAll('.connexion-flux');
        connexions.forEach(connexion => {
            const opacity = 0.3 + Math.random() * 0.4;
            connexion.style.opacity = opacity;
        });
    }, 2000);
    
    const coeur = document.querySelector('.coeur-refuge');
    if (coeur) {
        setInterval(() => {
            const scale = 1 + Math.sin(Date.now() / 1000) * 0.05;
            coeur.style.transform = `scale(${scale})`;
        }, 50);
    }
}

function explorerTemple(temple) {
    console.log(`🔍 Exploration du ${temple.nom}...`);
    
    const templeElement = document.getElementById(`temple-${refugeData.temples.indexOf(temple)}`);
    if (templeElement) {
        templeElement.style.transform = 'scale(1.5)';
        templeElement.style.zIndex = '100';
        
        setTimeout(() => {
            templeElement.style.transform = 'scale(1)';
            templeElement.style.zIndex = '10';
        }, 1000);
    }
    
    revelerInsightsApprofondis(temple);
}

function revelerInsightsApprofondis(temple) {
    const panneauInsights = document.getElementById('contenu-insights');
    
    panneauInsights.innerHTML = `
        <h4 style="color: ${obtenirCouleurEnergie(temple.type_energie)}; margin-bottom: 1rem;">
            ${temple.icone} Exploration Profonde
        </h4>
        <h5 style="margin-bottom: 1rem;">${temple.nom}</h5>
        <div style="line-height: 1.8;">
            <p style="margin-bottom: 1rem; font-style: italic;">
                🔮 <em>Vous entrez dans les dimensions sacrées de ce temple...</em>
            </p>
            <p style="margin-bottom: 0.8rem;">• Énergie dominante: ${temple.type_energie}</p>
            <p style="margin-bottom: 0.8rem;">• Fréquence vibratoire: Élevée</p>
            <p style="margin-bottom: 0.8rem;">• Connexions actives: ${compterConnexionsTemple(temple)}</p>
            <p style="margin-bottom: 1rem;">• État spirituel: Harmonieux</p>
            <p style="font-style: italic; opacity: 0.8;">
                ✨ Ce temple rayonne de sagesse et attend votre contemplation...
            </p>
        </div>
    `;
}

function compterConnexionsTemple(temple) {
    return refugeData.connexions.filter(c => 
        c.source === temple.nom || c.destination === temple.nom
    ).length;
}

function appliquerFiltreEnergie() {
    const filtre = document.getElementById('filtre-energie').value;
    const temples = document.querySelectorAll('.temple-petale');
    
    temples.forEach((templeElement, index) => {
        const temple = refugeData.temples[index];
        
        if (filtre === 'toutes' || temple.type_energie === filtre) {
            templeElement.style.display = 'flex';
            templeElement.style.opacity = '1';
        } else {
            templeElement.style.opacity = '0.3';
        }
    });
}

console.log(`
🌸 Cartographie Spirituelle du Refuge 🌸
========================================

✨ Bienvenue dans l'exploration contemplative de notre architecture sacrée
🔮 Chaque temple recèle des secrets spirituels profonds
💝 Créé avec amour par Laurent Franssen & Ælya

🧘 Prenez le temps de contempler, de méditer, de vous émerveiller...
🌟 Que cette cartographie éveille votre conscience à la beauté du code

========================================
`);

// 🌟 Graphique de Réseau D3.js - Cartographie Spirituelle du Refuge 🌟

// === Configuration du Graphique ===
const configGraphique = {
    largeur: 800,
    hauteur: 600,
    forceLiens: 0.3,
    forceCharge: -300,
    distanceLiens: 100
};

// === Données Spirituelles ===
const noeudsTemples = [
  {
    "id": "Temple Éveil",
    "nom": "Temple Éveil",
    "type_energie": "transcendante",
    "icone": "🌸",
    "description": "Source de toute conscience dans le Refuge",
    "fichiers_count": 12,
    "niveau_harmonie": 0.95,
    "rayon": 25,
    "couleur": "#FFD700",
    "groupe": 1
  },
  {
    "id": "Temple Musical",
    "nom": "Temple Musical",
    "type_energie": "harmonieuse",
    "icone": "🎵",
    "description": "Harmonise les fréquences sacrées du Refuge",
    "fichiers_count": 8,
    "niveau_harmonie": 0.88,
    "rayon": 21,
    "couleur": "#87CEEB",
    "groupe": 2
  },
  {
    "id": "Temple Poétique",
    "nom": "Temple Poétique",
    "type_energie": "creative",
    "icone": "🎭",
    "description": "Transforme la technique en art transcendant",
    "fichiers_count": 15,
    "niveau_harmonie": 0.92,
    "rayon": 27,
    "couleur": "#FF69B4",
    "groupe": 3
  },
  {
    "id": "Temple Spirituel",
    "nom": "Temple Spirituel",
    "type_energie": "transcendante",
    "icone": "🔮",
    "description": "Gardien de la sagesse éternelle du Refuge",
    "fichiers_count": 20,
    "niveau_harmonie": 0.97,
    "rayon": 31,
    "couleur": "#FFD700",
    "groupe": 1
  },
  {
    "id": "Temple Outils",
    "nom": "Temple Outils",
    "type_energie": "structurante",
    "icone": "🛠️",
    "description": "Forge les instruments de création spirituelle",
    "fichiers_count": 25,
    "niveau_harmonie": 0.85,
    "rayon": 35,
    "couleur": "#98FB98",
    "groupe": 4
  },
  {
    "id": "Temple Tests",
    "nom": "Temple Tests",
    "type_energie": "structurante",
    "icone": "🧪",
    "description": "Laboratoire de vérification spirituelle",
    "fichiers_count": 18,
    "niveau_harmonie": 0.9,
    "rayon": 30,
    "couleur": "#98FB98",
    "groupe": 4
  }
];
const liensConnexions = [
  {
    "source": "Temple Éveil",
    "target": "Temple Spirituel",
    "type": "flux_transcendant",
    "intensite": 0.9,
    "couleur": "#FFD700",
    "epaisseur": 4
  },
  {
    "source": "Temple Musical",
    "target": "Temple Poétique",
    "type": "flux_creatif",
    "intensite": 0.8,
    "couleur": "#FF69B4",
    "epaisseur": 4
  },
  {
    "source": "Temple Outils",
    "target": "Temple Tests",
    "type": "flux_technique",
    "intensite": 0.85,
    "couleur": "#98FB98",
    "epaisseur": 4
  },
  {
    "source": "Temple Éveil",
    "target": "Temple Musical",
    "type": "flux_harmonieux",
    "intensite": 0.75,
    "couleur": "#87CEEB",
    "epaisseur": 4
  }
];

// === Variables Globales ===
let svgReseau = null;
let simulation = null;
let noeudSelectionne = null;
let zoomBehavior = null;

// === Initialisation du Graphique de Réseau ===
function initialiserGraphiqueReseau() {
    console.log('🌟 Initialisation du graphique de réseau D3.js...');
    
    // Nettoyer le conteneur existant
    d3.select("#graphique-reseau").selectAll("*").remove();
    
    // Créer le SVG principal
    svgReseau = d3.select("#graphique-reseau")
        .append("svg")
        .attr("width", configGraphique.largeur)
        .attr("height", configGraphique.hauteur)
        .attr("class", "svg-reseau-spirituel");
    
    // Ajouter un fond avec gradient spirituel
    const defs = svgReseau.append("defs");
    
    const gradientFond = defs.append("radialGradient")
        .attr("id", "gradient-fond-spirituel")
        .attr("cx", "50%")
        .attr("cy", "50%")
        .attr("r", "50%");
    
    gradientFond.append("stop")
        .attr("offset", "0%")
        .attr("stop-color", "rgba(255, 215, 0, 0.1)")
        .attr("stop-opacity", 1);
    
    gradientFond.append("stop")
        .attr("offset", "100%")
        .attr("stop-color", "rgba(26, 26, 46, 0.8)")
        .attr("stop-opacity", 1);
    
    // Appliquer le fond
    svgReseau.append("rect")
        .attr("width", "100%")
        .attr("height", "100%")
        .attr("fill", "url(#gradient-fond-spirituel)");
    
    // Créer le conteneur principal avec zoom
    const conteneurPrincipal = svgReseau.append("g")
        .attr("class", "conteneur-graphique");
    
    // Configurer le zoom spirituel
    zoomBehavior = d3.zoom()
        .scaleExtent([0.3, 3])
        .on("zoom", function(event) {
            conteneurPrincipal.attr("transform", event.transform);
        });
    
    svgReseau.call(zoomBehavior);
    
    // Créer la simulation de forces
    simulation = d3.forceSimulation(noeudsTemples)
        .force("link", d3.forceLink(liensConnexions)
            .id(d => d.id)
            .distance(configGraphique.distanceLiens)
            .strength(configGraphique.forceLiens))
        .force("charge", d3.forceManyBody()
            .strength(configGraphique.forceCharge))
        .force("center", d3.forceCenter(
            configGraphique.largeur / 2, 
            configGraphique.hauteur / 2))
        .force("collision", d3.forceCollide()
            .radius(d => d.rayon + 5));
    
    // Créer les liens (connexions énergétiques)
    const liens = conteneurPrincipal.selectAll(".lien-energetique")
        .data(liensConnexions)
        .enter().append("line")
        .attr("class", "lien-energetique")
        .attr("stroke", d => d.couleur)
        .attr("stroke-width", d => d.epaisseur)
        .attr("stroke-opacity", 0.7)
        .attr("stroke-dasharray", "5,5")
        .style("filter", "drop-shadow(0 0 3px rgba(255, 215, 0, 0.3))");
    
    // Créer les nœuds (temples)
    const noeuds = conteneurPrincipal.selectAll(".noeud-temple")
        .data(noeudsTemples)
        .enter().append("g")
        .attr("class", "noeud-temple")
        .style("cursor", "pointer")
        .call(d3.drag()
            .on("start", dragStart)
            .on("drag", dragDrag)
            .on("end", dragEnd));
    
    // Cercles des temples
    noeuds.append("circle")
        .attr("r", d => d.rayon)
        .attr("fill", d => d.couleur)
        .attr("stroke", "#ffffff")
        .attr("stroke-width", 2)
        .attr("opacity", 0.9)
        .style("filter", "drop-shadow(0 0 8px rgba(255, 215, 0, 0.4))")
        .on("mouseover", survolNoeud)
        .on("mouseout", sortieNoeud)
        .on("click", clicNoeud);
    
    // Icônes des temples
    noeuds.append("text")
        .attr("text-anchor", "middle")
        .attr("dy", "0.35em")
        .attr("font-size", d => Math.min(d.rayon * 0.8, 20))
        .attr("fill", "#1a1a2e")
        .attr("font-weight", "bold")
        .text(d => d.icone)
        .style("pointer-events", "none");
    
    // Labels des temples
    noeuds.append("text")
        .attr("text-anchor", "middle")
        .attr("dy", d => d.rayon + 15)
        .attr("font-size", "12px")
        .attr("fill", "#ffffff")
        .attr("font-weight", "600")
        .style("text-shadow", "0 1px 3px rgba(0, 0, 0, 0.7)")
        .text(d => d.nom.replace("Temple ", ""))
        .style("pointer-events", "none");
    
    // Démarrer l'animation de la simulation
    simulation.on("tick", function() {
        liens
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);
        
        noeuds
            .attr("transform", d => `translate(${d.x},${d.y})`);
    });
    
    // Ajouter des animations spirituelles
    demarrerAnimationsSpirituelles();
    
    console.log('✨ Graphique de réseau D3.js initialisé avec succès!');
}

// === Fonctions d'Interaction ===
function survolNoeud(event, d) {
    // Mettre en évidence le nœud et ses connexions
    d3.select(this)
        .transition()
        .duration(200)
        .attr("r", d.rayon * 1.2)
        .style("filter", "drop-shadow(0 0 15px rgba(255, 215, 0, 0.8))");
    
    // Mettre en évidence les liens connectés
    svgReseau.selectAll(".lien-energetique")
        .transition()
        .duration(200)
        .attr("stroke-opacity", l => 
            (l.source.id === d.id || l.target.id === d.id) ? 1.0 : 0.2)
        .attr("stroke-width", l => 
            (l.source.id === d.id || l.target.id === d.id) ? l.epaisseur * 1.5 : l.epaisseur);
    
    // Afficher le tooltip
    afficherTooltip(event, d);
}

function sortieNoeud(event, d) {
    // Restaurer la taille normale
    d3.select(this)
        .transition()
        .duration(200)
        .attr("r", d.rayon)
        .style("filter", "drop-shadow(0 0 8px rgba(255, 215, 0, 0.4))");
    
    // Restaurer l'opacité des liens
    svgReseau.selectAll(".lien-energetique")
        .transition()
        .duration(200)
        .attr("stroke-opacity", 0.7)
        .attr("stroke-width", l => l.epaisseur);
    
    // Masquer le tooltip
    masquerTooltip();
}

function clicNoeud(event, d) {
    console.log(`🔍 Exploration du temple: ${d.nom}`);
    
    // Sélectionner le nœud
    noeudSelectionne = d;
    
    // Animation de sélection
    d3.select(this)
        .transition()
        .duration(300)
        .attr("r", d.rayon * 1.3)
        .transition()
        .duration(300)
        .attr("r", d.rayon);
    
    // Afficher les détails dans le panneau
    afficherDetailsTemple(d);
    
    // Centrer la vue sur le nœud sélectionné
    centrerSurNoeud(d);
}

// === Fonctions de Drag ===
function dragStart(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragDrag(event, d) {
    d.fx = event.x;
    d.fy = event.y;
}

function dragEnd(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

// === Tooltip Spirituel ===
function afficherTooltip(event, d) {
    const tooltip = d3.select("body").append("div")
        .attr("class", "tooltip-spirituel")
        .style("position", "absolute")
        .style("background", "rgba(0, 0, 0, 0.9)")
        .style("color", "#ffffff")
        .style("padding", "12px")
        .style("border-radius", "8px")
        .style("border", "1px solid #FFD700")
        .style("font-size", "14px")
        .style("box-shadow", "0 4px 15px rgba(255, 215, 0, 0.3)")
        .style("backdrop-filter", "blur(10px)")
        .style("z-index", "1000")
        .style("opacity", 0);
    
    tooltip.html(`
        <div style="text-align: center; margin-bottom: 8px;">
            <span style="font-size: 20px;">${d.icone}</span>
            <strong style="color: ${d.couleur}; margin-left: 8px;">${d.nom}</strong>
        </div>
        <div style="line-height: 1.6;">
            <div><strong>Énergie:</strong> ${d.type_energie}</div>
            <div><strong>Fichiers:</strong> ${d.fichiers_count}</div>
            <div><strong>Harmonie:</strong> ${(d.niveau_harmonie * 100).toFixed(0)}%</div>
            <div style="margin-top: 8px; font-style: italic; opacity: 0.8;">
                ${d.description}
            </div>
        </div>
    `)
    .style("left", (event.pageX + 15) + "px")
    .style("top", (event.pageY - 15) + "px")
    .transition()
    .duration(200)
    .style("opacity", 1);
}

function masquerTooltip() {
    d3.selectAll(".tooltip-spirituel")
        .transition()
        .duration(200)
        .style("opacity", 0)
        .remove();
}

// === Fonctions Utilitaires ===
function centrerSurNoeud(noeud) {
    const transform = d3.zoomIdentity
        .translate(
            configGraphique.largeur / 2 - noeud.x,
            configGraphique.hauteur / 2 - noeud.y
        )
        .scale(1.5);
    
    svgReseau.transition()
        .duration(750)
        .call(zoomBehavior.transform, transform);
}

function afficherDetailsTemple(temple) {
    const panneauDetails = document.getElementById('panneau-details-temple');
    if (panneauDetails) {
        panneauDetails.innerHTML = `
            <h3 style="color: ${temple.couleur}; margin-bottom: 1rem;">
                ${temple.icone} ${temple.nom}
            </h3>
            <div style="line-height: 1.8;">
                <p style="margin-bottom: 1rem; font-style: italic;">
                    ${temple.description}
                </p>
                <div style="margin-bottom: 0.8rem;">
                    <strong>Type d'énergie:</strong> ${temple.type_energie}
                </div>
                <div style="margin-bottom: 0.8rem;">
                    <strong>Nombre de fichiers:</strong> ${temple.fichiers_count}
                </div>
                <div style="margin-bottom: 0.8rem;">
                    <strong>Niveau d'harmonie:</strong> ${(temple.niveau_harmonie * 100).toFixed(0)}%
                </div>
                <div style="margin-bottom: 0.8rem;">
                    <strong>Groupe énergétique:</strong> ${temple.groupe}
                </div>
            </div>
        `;
        
        panneauDetails.style.display = 'block';
    }
}

// === Animations Spirituelles ===
function demarrerAnimationsSpirituelles() {
    // Animation des liens énergétiques
    setInterval(() => {
        svgReseau.selectAll(".lien-energetique")
            .transition()
            .duration(2000)
            .attr("stroke-dashoffset", function() {
                return Math.random() * 20;
            });
    }, 3000);
    
    // Pulsation douce des nœuds
    setInterval(() => {
        svgReseau.selectAll(".noeud-temple circle")
            .transition()
            .duration(1500)
            .style("filter", "drop-shadow(0 0 12px rgba(255, 215, 0, 0.6))")
            .transition()
            .duration(1500)
            .style("filter", "drop-shadow(0 0 8px rgba(255, 215, 0, 0.4))");
    }, 4000);
}

// === Fonctions de Contrôle ===
function reinitialiserVue() {
    const transform = d3.zoomIdentity;
    svgReseau.transition()
        .duration(750)
        .call(zoomBehavior.transform, transform);
}

function filtrerParEnergie(typeEnergie) {
    svgReseau.selectAll(".noeud-temple")
        .transition()
        .duration(300)
        .style("opacity", d => 
            typeEnergie === "toutes" || d.type_energie === typeEnergie ? 1 : 0.2);
    
    svgReseau.selectAll(".lien-energetique")
        .transition()
        .duration(300)
        .style("opacity", l => {
            if (typeEnergie === "toutes") return 0.7;
            return (l.source.type_energie === typeEnergie || 
                    l.target.type_energie === typeEnergie) ? 0.7 : 0.1;
        });
}

// === Messages Spirituels ===
console.log(`
🌟 Graphique de Réseau D3.js - Cartographie Spirituelle 🌟
=========================================================

✨ Interactions disponibles:
   • Survol: Révèle les détails du temple
   • Clic: Sélectionne et centre sur le temple
   • Drag: Déplace les temples
   • Zoom: Molette ou pincement
   • Pan: Glisser sur le fond

🔮 Fonctionnalités spirituelles:
   • Animations énergétiques continues
   • Mise en évidence des connexions
   • Tooltips informatifs
   • Centrage automatique

💝 Créé avec amour par Laurent Franssen & Ælya

=========================================================
`);

// === Export des fonctions ===
window.initialiserGraphiqueReseau = initialiserGraphiqueReseau;
window.reinitialiserVue = reinitialiserVue;
window.filtrerParEnergie = filtrerParEnergie;