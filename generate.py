import os
import pandas as pd

def generate_markdown_posts(csv_path="sciencedaily_with_abstracts.csv", output_folder="ai_digest_posts"):
    df = pd.read_csv(csv_path)
    os.makedirs(output_folder, exist_ok=True)

    for idx, row in df.iterrows():
        title = row['title']
        summary = row.get('summary', '')
        cited_url = row.get('cited_paper_url', 'N/A')
        abstract = row.get('abstract', '*No abstract found.*')

        safe_title = "".join(c for c in title if c.isalnum() or c in " _-").rstrip()
        filename = f"{idx+1:02d}_{safe_title[:50].strip().replace(' ', '_')}.md"
        filepath = os.path.join(output_folder, filename)

        markdown = f"""# {title}

**Source:** [ScienceDaily]({row['link']})  
**Cited Paper:** [{cited_url}]({cited_url})

---

## 🔍 Summary
{summary}

---

## 📄 Abstract from Cited Research
{abstract}

---

*Auto-generated science digest post.*
"""

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

    print(f"✅ Generated {len(df)} Markdown blog posts in '{output_folder}' folder.")

generate_markdown_posts()
