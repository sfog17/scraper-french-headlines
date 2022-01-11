from scrape_vingtminutes import VingtMinutesScraper
from scraper import Headline
from utils import query_from_file, split_article, TEST_DIR


def test_split_articles():
    split_article(
        html_name="vingtminutes", scraper=VingtMinutesScraper(), num_articles=103
    )


def test_scrape_headline():
    headline = query_from_file(TEST_DIR.joinpath("vingtminutes_article.html")).find(
        "article"
    )
    expected = Headline(
        title="Décès de Desmond Tutu, icône de la lutte anti-apartheid",
        url="https://www.20minutes.fr/monde/3205463-20211226-afrique-sud-deces-90-ans-desmond-tutu-icone-lutte-anti-apartheid",
        premium=False,
        picture=True,
    )
    assert VingtMinutesScraper().parse_headline(headline) == expected
