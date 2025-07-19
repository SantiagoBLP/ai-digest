import os
import openai

# Leer la clave API desde un archivo local
with open('api_keys/openai_key.txt', 'r') as f:
    openai.api_key = f.read().strip()

input_folder = "posts"
output_folder = "posts_es"
os.makedirs(output_folder, exist_ok=True)

def translate_and_adapt(text):
    prompt = f"""Traduce al español el siguiente texto técnico y redacta una noticia clara, fluida y atractiva para una audiencia general:
---
{text}
---
Responde solo con la noticia en español, sin encabezado ni introducción adicional.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un periodista experto en inteligencia artificial y ciencia."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1200
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"❌ Error al traducir: {e}")
        return None

for filename in os.listdir(input_folder):
    if filename.endswith(".md"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".md", "_es.md"))

        with open(input_path, "r", encoding="utf-8") as infile:
            content = infile.read()

        translated = translate_and_adapt(content)

        if translated:
            with open(output_path, "w", encoding="utf-8") as outfile:
                outfile.write(translated)
            print(f"✅ Traducido: {filename} → {output_path}")
        else:
            print(f"⚠️ Falló la traducción de: {filename}")
