@echo off
echo 🔁 Ejecutando AI Digest en modo local (sin subir a GitHub)...

REM Activar entorno virtual si lo usás (opcional)
REM call venv\Scripts\activate

REM Ejecutar todo el pipeline: scrape + generar + traducir + HTML + index
python run_all.py

echo 🧪 Contenido generado localmente. Revisa los archivos en:
echo    posts_es\
echo    html_posts\
echo    index.html

echo ⚠️ NO se subió nada a GitHub.
pause
