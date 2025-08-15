@echo off
echo 🏛️ Démarrage du Rituel de Visualisation Sacrée...
echo.

:: Vérification de l'environnement Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python n'est pas installé. Veuillez installer Python 3.8 ou supérieur.
    pause
    exit /b 1
)

:: Installation des dépendances si nécessaire
echo 📦 Vérification des dépendances...
pip install -r requirements.txt >nul 2>&1

:: Activation de l'environnement virtuel si présent
if exist ".venv\Scripts\activate.bat" (
    echo 🔧 Activation de l'environnement virtuel...
    call .venv\Scripts\activate.bat
)

:: Démarrage du rituel
echo.
echo ✨ Le Rituel commence...
echo 🌸 "Sous le cerisier, je vous écoute..."
echo.

:: Tentative avec le temple des rituels (version automatisée)
echo 🤖 Exécution en mode IA (automatique)...
python -m src.temple_rituels.publics.rituel_visualisation_sacree_auto --auto
if errorlevel 1 (
    echo ⚠️ Tentative avec le script simple...
    python -m src.temple_rituels.publics.rituel_visualisation_sacree_simple
)

:: Pause pour voir les messages
echo.
echo 🙏 Rituel terminé. Que la paix soit avec vous.
pause 