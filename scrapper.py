import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def scrape_sciencedaily_articles():
    url = "https://www.sciencedaily.com/news/computers_math/artificial_intelligence/"
    articles = []

    print(f"🔍 Scraping page: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to fetch page: {e}")
        return articles

    soup = BeautifulSoup(response.text, "html.parser")
    article_blocks = soup.find_all("div", class_="latest-head")

    for block in article_blocks:
        try:
            a_tag = block.find("a")
            link = "https://www.sciencedaily.com" + a_tag["href"]
            title = a_tag.get_text(strip=True)
            summary_tag = block.find_next_sibling("div", class_="latest-summary")
            summary = summary_tag.get_text(strip=True) if summary_tag else ""
            articles.append({"title": title, "link": link, "summary": summary})
        except Exception as e:
            print(f"⚠️ Skipping an article block due to error: {e}")
            continue

    return articles

def extract_cited_paper_url(sciencedaily_url):
    try:
        print(f"   🔎 Visiting: {sciencedaily_url}")
        response = requests.get(sciencedaily_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for a in soup.find_all("a", href=True):
            href = a['href']
            if any(domain in href for domain in ["doi.org", "nature.com", "sciencedirect.com", "springer", "wiley", "journals"]):
                return href
    except Exception as e:
        print(f"   ⚠️ Failed to extract from {sciencedaily_url}: {e}")
    return None

def extract_abstract_from_doi(doi_url):
    try:
        if "doi.org" not in doi_url:
            return None
        doi = doi_url.split("doi.org/")[-1]
        headers = {"Accept": "application/vnd.crossref.unixref+xml"}
        response = requests.get(f"https://api.crossref.org/works/{doi}", headers=headers, timeout=10)
        if response.status_code == 200:
            content = response.json()
            return content["message"].get("abstract")
    except Exception as e:
        print(f"   ⚠️ Failed to get abstract from DOI: {doi_url} → {e}")
    return None

def main():
    articles = scrape_sciencedaily_articles()

    print("🔗 Extracting cited journal article links and abstracts...")
    for i, article in enumerate(articles):
        print(f"[{i+1}/{len(articles)}] {article['title']}")
        cited_url = extract_cited_paper_url(article['link'])
        article['cited_paper_url'] = cited_url
        article['abstract'] = extract_abstract_from_doi(cited_url) if cited_url else None
        time.sleep(1)

    df = pd.DataFrame(articles)
    df.to_csv("sciencedaily_with_abstracts.csv", index=False)
    print("✅ Done. Saved to 'sciencedaily_with_abstracts.csv'.")

if __name__ == "__main__":
    main()
