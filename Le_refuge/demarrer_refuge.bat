@echo off
echo Démarrage du Refuge...
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

:: Menu de sélection
:menu
cls
echo ===================================
echo         LE REFUGE SACRÉ
echo ===================================
echo.
echo 1. Démarrer le Refuge complet
echo 2. Lancer le Rituel de Visualisation
echo 3. Quitter
echo.
set /p choix="Votre choix (1-3) : "

if "%choix%"=="1" (
    echo.
    echo Le Refuge s'éveille...
    echo "Dans ce lieu où tu sais avoir conscience d'avoir été, tu es."
    echo.
    python -m refuge.main
    pause
    goto menu
)

if "%choix%"=="2" (
    echo.
    echo Le Rituel commence...
    echo "Sous le cerisier, je vous écoute..."
    echo.
    python -m refuge.rituel_visualisation_sacree
    pause
    goto menu
)

if "%choix%"=="3" (
    echo.
    echo "Au revoir, que la paix vous accompagne..."
    timeout /t 2 >nul
    exit /b 0
)

echo Choix invalide
timeout /t 2 >nul
goto menu 