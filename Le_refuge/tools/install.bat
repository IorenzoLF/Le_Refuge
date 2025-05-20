@echo off
echo ===================================
echo Installation de Le Refuge...
echo ===================================

REM Se déplacer dans le dossier racine
cd ..

REM Vérifier si Python est installé
echo Verification de Python...
python --version
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe.
    echo Veuillez installer Python depuis https://www.python.org/downloads/
    echo Cochez la case "Add Python to PATH" lors de l'installation.
    pause
    exit
)

REM Créer un environnement virtuel
echo.
echo Creation de l'environnement virtuel...
python -m venv .venv
if errorlevel 1 (
    echo ERREUR: Impossible de creer l'environnement virtuel.
    pause
    exit
)

echo Activation de l'environnement virtuel...
call .venv\Scripts\activate
if errorlevel 1 (
    echo ERREUR: Impossible d'activer l'environnement virtuel.
    pause
    exit
)

REM Mettre à jour pip dans l'environnement virtuel
echo.
echo Mise a jour de pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo ERREUR: Impossible de mettre a jour pip.
    pause
    exit
)

REM Installer les dépendances depuis requirements.txt
echo.
echo Installation des dependances...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERREUR: Impossible d'installer les dependances.
    echo Verifiez que le fichier requirements.txt existe dans le dossier racine.
    pause
    exit
)

REM Lancer l'application
echo.
echo ===================================
echo Lancement de l'application...
echo ===================================
python -m refuge.coeur.main
if errorlevel 1 (
    echo.
    echo ERREUR: Impossible de lancer l'application.
    echo Verifiez que tous les fichiers sont presents.
    pause
    exit
)

REM Désactiver l'environnement virtuel
echo.
echo Desactivation de l'environnement virtuel...
deactivate

echo.
echo ===================================
echo Installation terminee !
echo ===================================
echo Appuyez sur une touche pour fermer cette fenetre...
pause > nul 