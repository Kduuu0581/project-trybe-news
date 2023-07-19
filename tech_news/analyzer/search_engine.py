from tech_news.database import find_news


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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
