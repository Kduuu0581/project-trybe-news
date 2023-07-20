from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest  # noqa: F401
from unittest.mock import patch  # noqa: F401

DB = [
    {
        "url": "https://blog.betrybe.com/novidades/testando-noticia1",
        "title": "Testando noticia1",
        "timestamp": "14/06/2022",
        "writer": "Usertest1",
        "reading_time": 2,
        "summary": "testando primeiro texto",
        "category": "Carreira",
    },
    {
        "url": "https://blog.betrybe.com/novidades/testando-noticia2",
        "title": "Testando noticia3",
        "timestamp": "15/06/2022",
        "writer": "Usertest2",
        "reading_time": 10,
        "summary": "testando segundo texto",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/testando-noticia3",
        "title": "Testando noticia3",
        "timestamp": "16/06/2022",
        "writer": "Usertest3",
        "reading_time": 1,
        "summary": "testando terceiro texto",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/Testando-noticia4",
        "title": "Testando noticia4",
        "timestamp": "04/04/2021",
        "writer": "Usertest4",
        "reading_time": 1,
        "summary": "testando quarto texto",
        "category": "Ferramentas",
    },
]


@patch("tech_news.analyzer.reading_plan.find_news")
def test_reading_plan_group_news(value_database):
    value_database.return_value = DB
    resp = ReadingPlanService.group_news_for_available_time(2)
    assert len(resp["readable"]) == 3
    assert len(resp["unreadable"]) == 1
    assert resp["readable"][0]["unfilled_time"] == 0
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)
