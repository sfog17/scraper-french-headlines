from scrape_lefigaro import LeFigaroScraper
from scraper import Headline
from utils import query_from_file, split_article, TEST_DIR


def test_split_articles():
    split_article(html_name="lefigaro", scraper=LeFigaroScraper(), num_articles=244)


def test_scrape_headline_1():
    headline = query_from_file(TEST_DIR.joinpath("lefigaro_article_1.html")).find("a")
    expected = Headline(
        title="Covid-19 : faut-il réduire la durée d'isolement des cas contacts ?",
        url="https://www.lefigaro.fr/sciences/covid-19-faut-il-reduire-la-duree-d-isolement-des-cas-contacts-20211225",
        premium=True,
        picture=True,
    )
    assert LeFigaroScraper().parse_headline(headline) == expected


def test_scrape_headline_2():
    headline = query_from_file(TEST_DIR.joinpath("lefigaro_article_2.html")).find("a")
    expected = Headline(
        title="Covid-19 : l'isolement des cas contacts pourrait passer de 10 à 7 jours",
        url="https://www.lefigaro.fr/actualite-france/covid-19-l-isolement-des-cas-contacts-pourrait-passer-de-10-a-7-jours-20211224",
        premium=False,
        picture=False,
    )
    assert LeFigaroScraper().parse_headline(headline) == expected
