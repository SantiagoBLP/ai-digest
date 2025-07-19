@echo off
echo ===============================
echo 🚀 AI Digest Deployment Script
echo ===============================

:: Paso 1: Navegar al directorio del proyecto
cd /d %~dp0

:: Paso 2: Confirmar que estamos en un repositorio Git
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo ❌ No es un repositorio Git. Inicializa primero con git init
    pause
    exit /b 1
)

:: Paso 3: Añadir y hacer commit de todos los cambios
echo 📝 Añadiendo cambios...
git add .

echo 💬 Escribiendo commit...
git commit -m "🔄 Actualización automática de artículos y contenido generado"

:: Paso 4: Hacer pull seguro con rebase
echo 🔄 Haciendo pull con rebase para evitar conflictos...
git pull origin main --rebase

:: Paso 5: Hacer push al repositorio remoto
echo 📤 Subiendo cambios a GitHub...
git push origin main

:: Confirmación final
echo ✅ Despliegue completado exitosamente.
pause
