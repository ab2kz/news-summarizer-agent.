from news_fetcher import fetch_top_headlines
from summarizer import summarize_article
import json

def main():
    print("Fetching news...")
    articles = fetch_top_headlines()

    summarized_news = []
    for article in articles:
        summary = summarize_article(article['title'] + ". " + article['description'] if article['description'] else article['title'])
        summarized_news.append({
            "title": article['title'],
            "url": article['url'],
            "summary": summary
        })

    with open("news_summary.json", "w", encoding="utf-8") as f:
        json.dump(summarized_news, f, indent=4, ensure_ascii=False)

    print("Summarized news saved to news_summary.json")

if __name__ == "__main__":
    main()