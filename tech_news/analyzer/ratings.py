from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    response = find_news()
    list_count = {}
    for news in response:
        list_count[news["category"]] = list_count.get(news["category"], 0) + 1
    sorted_list = sorted(list_count.items(), key=lambda x: (-x[1], x[0]))
    return [key for key, value in sorted_list[:5]]
