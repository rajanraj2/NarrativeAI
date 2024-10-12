import requests

# Set up your NewsAPI key
NEWS_API_KEY = ''

def get_news(keyword, page_size=20):
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={NEWS_API_KEY}&pageSize={page_size}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    
    news = []
    for article in articles:
        news.append({
            'title': article['title'],
            'description': article['description'],
            'url': article['url']
        })
    return news

# Example Usage
news_articles = get_news('technology')
for article in news_articles:
    print(article['title'], article['url'])
    print()
