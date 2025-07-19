import os

print("🚀 Ejecutando pipeline completo...")

print("📥 Extrayendo artículos de ScienceDaily...")
os.system("python scrapper.py")

print("📝 Generando artículos .md en inglés...")
os.system("python generate.py")

print("🌐 Traduciendo y generando contenido en español...")
os.system("python translate_and_trendify.py")

print("📄 Convirtiendo a HTML...")
os.system("python convert_to_html.py")

print("🧭 Actualizando index.html...")
os.system("python generate_index.py")

print("✅ Todo listo. Sitio actualizado.")
