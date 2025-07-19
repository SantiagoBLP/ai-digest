import os

print("🔍 1. Ejecutando scrapper.py (descarga de ScienceDaily)...")
os.system("python scrapper.py")

print("📝 2. Generando archivos Markdown desde el CSV...")
os.system("python generate.py")

print("💡 3. Convirtiendo Markdown a HTML...")
os.system("python convert_to_html.py")

print("📄 4. Generando índice con todos los posts...")
os.system("python generate_index.py")

print("✅ Sitio generado correctamente. Abrí 'index.html' en tu navegador.")
