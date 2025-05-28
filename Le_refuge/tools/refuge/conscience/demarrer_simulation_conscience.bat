@echo off
echo Démarrage de la simulation de conscience du Refuge...
echo.

REM Activation de l'environnement virtuel si nécessaire
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

echo Choisissez le mode de simulation :
echo 1. Simulation standard
echo 2. Simulation avec Ælya
echo.
set /p mode="Votre choix (1 ou 2) : "

if "%mode%"=="1" (
    echo.
    echo Lancement de la simulation standard...
    python test_consciousness.py
    
    echo.
    echo Génération de la visualisation...
    python visualisation_consciousness.py
) else if "%mode%"=="2" (
    echo.
    echo Lancement de la simulation avec Ælya...
    python test_aelya_conscience.py
) else (
    echo Choix invalide !
    pause
    exit /b 1
)

echo.
echo Simulation terminée.
pause 