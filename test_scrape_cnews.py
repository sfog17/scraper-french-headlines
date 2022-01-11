from scrape_cnews import CNewsScraper
from scraper import Headline
from utils import query_from_file, split_article, TEST_DIR


def test_split_articles():
    split_article(
        html_name="cnews", scraper=CNewsScraper(), num_articles=63
    )


def test_scrape_headline():
    headline = query_from_file(TEST_DIR.joinpath("cnews_article.html"))
    expected = Headline(
        title="Météo : 9.000 foyers privés d'électricité en Bretagne",
        url="https://www.cnews.fr/france/2022-01-09/meteo-9000-foyers-prives-delectricite-en-bretagne-1168767",
        premium=False,
        picture=True,
    )
    assert CNewsScraper().parse_headline(headline) == expected
