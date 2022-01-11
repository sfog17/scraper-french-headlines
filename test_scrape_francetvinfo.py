from scrape_francetvinfo import FranceTvInfoScraper
from scraper import Headline
from utils import query_from_file, split_article, TEST_DIR


def test_split_articles():
    split_article(
        html_name="francetvinfo", scraper=FranceTvInfoScraper(), num_articles=261
    )


def test_scrape_headline_1():
    headline = query_from_file(TEST_DIR.joinpath("francetvinfo_article_1.html")).find(
        "a"
    )
    expected = Headline(
        title=(
            "Covid-19 : testés positifs, de nombreux Français ont dû s’isoler pour Noël"
        ),
        url="https://mobile.francetvinfo.fr/sante/maladie/coronavirus/covid-19-testes-positifs-de-nombreux-francais-ont-du-sisoler-pour-noel_4893565.html",
        premium=False,
        picture=True,
    )
    assert FranceTvInfoScraper().parse_headline(headline) == expected


def test_scrape_headline_picture():
    headline = query_from_file(
        TEST_DIR.joinpath("francetvinfo_article_picture.html")
    ).find("a")
    expected = Headline(
        title="Les Cap-Verdiens de Sao Tomé entre misère et mélancolie",
        url="https://mobile.francetvinfo.fr/monde/afrique/societe-africaine/les-cap-verdiens-de-sao-tome-entre-misere-et-melancolie_4890261.html",
        premium=False,
        picture=True,
    )
    assert FranceTvInfoScraper().parse_headline(headline) == expected
