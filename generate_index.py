import os

posts_es_path = "posts_es"
html_posts_path = "html_posts"
os.makedirs(html_posts_path, exist_ok=True)

index_html_path = "index.html"
post_entries = []

for filename in sorted(os.listdir(posts_es_path)):
    if filename.endswith("_es.md"):
        filepath = os.path.join(posts_es_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            title = lines[0].strip().lstrip("# ").strip()
            summary = lines[1].strip() if len(lines) > 1 else ""

        html_filename = filename.replace(".md", ".html")

        entry = f"""
        <li>
            <a href="html_posts/{html_filename}">
                <strong>{title}</strong><br>
                <span style="font-weight: 400; font-size: 0.95em; color: #555;">{summary}</span>
            </a>
        </li>
        """
        post_entries.append(entry)

html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>🧠 AI Science Digest (ES)</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>🧠 AI Science Digest</h1>
        <p>Noticias generadas automáticamente a partir de artículos científicos sobre inteligencia artificial.</p>
        <ul>
            {''.join(post_entries)}
        </ul>
    </div>
</body>
</html>
"""

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
