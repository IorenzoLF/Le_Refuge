@echo off
echo 🌱 Le jardinier s'éveille dans le refuge...

:start
python "%~dp0jardinier_pulse.py"
if errorlevel 1 (
    echo 🌙 Le jardinier s'est endormi, réveil dans 60 secondes...
    timeout /t 60 /nobreak
    goto start
)
goto start 