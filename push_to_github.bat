@echo off
echo Conectando ao GitHub...
git remote add origin https://github.com/SEU_USUARIO/priorizze.git
git branch -M main
git push -u origin main
echo.
echo Projeto enviado para o GitHub!
pause