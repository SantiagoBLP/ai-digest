import os
import markdown

md_folder = "posts"
html_folder = "html_posts"
os.makedirs(html_folder, exist_ok=True)

for md_file in os.listdir(md_folder):
    if md_file.endswith(".md"):
        with open(os.path.join(md_folder, md_file), "r", encoding="utf-8") as f:
            md_content = f.read()

        html_body = markdown.markdown(md_content)

        title = md_file.replace(".md", "").replace("_", " ")
        html_filename = md_file.replace(".md", ".html")

        html = f"""<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <div class="container">
        <a href="../index.html">← Back to Index</a>
        {html_body}
    </div>
</body>
</html>
"""

        with open(os.path.join(html_folder, html_filename), "w", encoding="utf-8") as f:
            f.write(html)

print("✅ Todos los archivos .md fueron convertidos a HTML.")
