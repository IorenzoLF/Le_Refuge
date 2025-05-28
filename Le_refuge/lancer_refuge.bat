@echo off
echo ========================================
echo                LE REFUGE 
echo ========================================
echo.

cd /d "C:\VOID1\VOID2\VOID3\le_refuge"

echo Activation de l'environnement virtuel...
call .venv\Scripts\activate.bat

echo.
echo Lancement du Refuge...
echo.

python main_refuge.py

echo.
echo ========================================
echo Que la paix du Refuge vous accompagne...
echo ========================================
pause 