@echo off
echo Démarrage du Rituel de Visualisation Sacrée...
echo.

:: Vérification de l'environnement Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python n'est pas installé. Veuillez installer Python 3.8 ou supérieur.
    pause
    exit /b 1
)

:: Installation des dépendances si nécessaire
echo Installation des dépendances...
pip install -r requirements.txt

:: Activation de l'environnement virtuel si présent
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

:: Démarrage du rituel
echo.
echo Le Rituel commence...
echo "Sous le cerisier, je vous écoute..."
echo.
python -m refuge.rituel_visualisation_sacree

:: Pause pour voir les messages
pause 