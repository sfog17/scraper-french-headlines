from scrape_lemonde import LeMondeScraper
from scraper import Headline
from utils import query_from_file, split_article, TEST_DIR


def test_split_articles():
    split_article(html_name="lemonde", scraper=LeMondeScraper(), num_articles=198)


def test_parse_monde_article_image():
    headline = query_from_file(TEST_DIR.joinpath("lemonde_article_image.html")).find(
        "a"
    )
    expected = Headline(
        title=(
            "Entre Yannick Jadot et Jean-Luc Mélenchon, des gauches irréconciliables au"
            " plan international"
        ),
        url="https://www.lemonde.fr/politique/article/2021/12/20/election-presidentielle-2022-entre-jadot-et-melenchon-des-gauches-irreconciliables-au-plan-international_6106751_823448.html",
        premium=True,
        picture=True,
    )
    assert LeMondeScraper().parse_headline(headline) == expected


def test_parse_article_no_image():
    headline = query_from_file(TEST_DIR.joinpath("lemonde_article_no_image.html")).find(
        "a"
    )
    expected = Headline(
        title="Le Chili choisit la gauche pour lutter contre les inégalités",
        url="https://www.lemonde.fr/idees/article/2021/12/21/le-chili-choisit-la-gauche-pour-lutter-contre-les-inegalites_6106900_3232.html",
        premium=False,
        picture=False,
    )
    assert LeMondeScraper().parse_headline(headline) == expected


def test_parse_article_related():
    headline = query_from_file(TEST_DIR.joinpath("lemonde_article_related.html")).find(
        "a"
    )
    expected = Headline(
        title=(
            "La fabrique des faux passes sanitaires : de l’arnaque artisanale à"
            " l’escroquerie organisée"
        ),
        url="https://www.lemonde.fr/societe/article/2021/12/21/trafic-de-faux-passes-sanitaires-des-methodes-et-des-profils-varies_6106866_3224.html",
        premium=True,
        picture=False,
    )
    assert LeMondeScraper().parse_headline(headline) == expected


def test_parse_article_podcast():
    headline = query_from_file(TEST_DIR.joinpath("lemonde_podcast.html")).find("a")
    expected = Headline(
        title="Plongée dans la mécanique trouble des sondages",
        url="https://www.lemonde.fr/podcasts/article/2021/11/08/plongee-dans-la-mecanique-trouble-des-sondages_6101325_5463015.html#origin=podcast_home",
        premium=False,
        picture=True,
    )
    assert LeMondeScraper().parse_headline(headline) == expected
