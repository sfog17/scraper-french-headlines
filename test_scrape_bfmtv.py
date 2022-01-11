from scrape_bfmtv import BfmTvScraper
from scraper import Headline
from utils import query_from_file, split_article, TEST_DIR


def test_split_articles():
    split_article(html_name="bfmtv", scraper=BfmTvScraper(), num_articles=91)


def test_scrape_headline_title():
    headline = query_from_file(TEST_DIR.joinpath("bfmtv_title.html")).find("a")
    expected = Headline(
        title="EN DIRECT - Plus de 3500 patients hospitalisés en soins critiques",
        url="https://www.bfmtv.com/sante/en-direct-variant-omicron-le-masque-redevient-obligatoire-en-exterieur-a-paris-des-vendredi_LN-202112300028.html",
        premium=False,
        picture=True,
    )
    assert BfmTvScraper().parse_headline(headline) == expected


def test_scrape_headline_article():
    headline = query_from_file(TEST_DIR.joinpath("bfmtv_article.html")).find("a")
    expected = Headline(
        title="""Coupe de France: "Le père Noël est passé avant l’heure", comment Chauvigny se prépare avant l’OM""",
        url="https://rmcsport.bfmtv.com/football/coupe-de-france/coupe-de-france-le-pere-noel-est-passe-avant-l-heure-comment-chauvigny-se-prepare-avant-l-om_AV-202112300203.html",
        premium=False,
        picture=True,
    )
    assert BfmTvScraper().parse_headline(headline) == expected


def test_scrape_headline_article2():
    headline = query_from_file(TEST_DIR.joinpath("bfmtv_article2.html")).find("a")
    expected = Headline(
        title=(
            "Covid-19: à Paris, le taux d'incidence dépasse les 2000 cas pour 100.000"
            " habitants"
        ),
        url="https://www.bfmtv.com/paris/covid-19-a-paris-le-taux-d-incidence-depasse-les-2000-pour-100-000-habitants_AN-202112290335.html",
        premium=False,
        picture=False,
    )
    assert BfmTvScraper().parse_headline(headline) == expected
