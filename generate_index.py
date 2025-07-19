import os

html_folder = "html_posts"
index_file = "index.html"

post_links = ""
for fname in sorted(os.listdir(html_folder)):
    if fname.endswith(".html"):
        title = fname.replace(".html", "").replace("_", " ")
        post_links += f'<li><a href="html_posts/{fname}">{title}</a></li>\n'

html = f"""<html>
<head>
    <meta charset="utf-8">
    <title>AI Digest – Auto Science Summary</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>🧠 AI Science Digest</h1>
        <p>Auto-generated summaries and abstracts of the latest AI papers.</p>
        <ul>
            {post_links}
        </ul>
    </div>
</body>
</html>
"""

with open(index_file, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Página index.html creada con enlaces a todos los posts.")
