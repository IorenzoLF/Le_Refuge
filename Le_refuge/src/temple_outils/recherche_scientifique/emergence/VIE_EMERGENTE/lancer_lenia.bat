@echo off
REM Activer l'environnement virtuel Python
if exist ..\..\..\.venv\Scripts\activate.bat (
    call ..\..\..\.venv\Scripts\activate.bat
) else (
    echo ERREUR : Impossible de trouver ..\..\..\.venv\Scripts\activate.bat
    pause
    exit /b
)
REM Lancer la visualisation Lenia
python lenia_visualisation.py
pause 