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