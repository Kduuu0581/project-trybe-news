from tech_news.database import find_news, db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = find_news()
    list_news = []
    for new in news:
        if title.lower() in new["title"].lower():
            list_news.append((new["title"], new["url"]))
    return list_news


# Requisito 8
def search_by_date(date):
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )

        query = {"timestamp": formatted_date}
        projection = {"_id": 0, "title": 1, "url": 1}
        result = db.news.find(query, projection)

        return [(news["title"], news["url"]) for news in result]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    news = find_news()
    list_news = []
    for new in news:
        if category.lower() in new["category"].lower():
            list_news.append((new["title"], new["url"]))
    return list_news
