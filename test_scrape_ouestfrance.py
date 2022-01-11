from scrape_ouestfrance import OuestFranceScraper
from scraper import Headline
from utils import query_from_file, split_article, TEST_DIR


def test_split_articles():
    split_article(
        html_name="ouestfrance", scraper=OuestFranceScraper(), num_articles=267
    )


def test_scrape_headline():
    headline = query_from_file(TEST_DIR.joinpath("ouestfrance_article.html")).find(
        "article"
    )
    expected = Headline(
        title=(
            "Arnold Schwarzenegger offre 25 mini-maisons aux vétérans sans-abris de Los"
            " Angeles"
        ),
        url="https://www.ouest-france.fr/monde/etats-unis/arnold-schwarzenegger-offre-25-mini-maisons-aux-veterans-sans-abris-de-los-angeles-41ac3626-5275-406d-9d81-f1e2abef0154",
        premium=False,
        picture=True,
    )
    assert OuestFranceScraper().parse_headline(headline) == expected


def test_scrape_headline2():
    headline = query_from_file(TEST_DIR.joinpath("ouestfrance_article2.html")).find(
        "article"
    )
    expected = Headline(
        title=(
            "Dacia, premier vendeur de véhicules neufs aux particuliers en France en"
            " 2021"
        ),
        url="https://www.ouest-france.fr/economie/automobile/dacia-premier-vendeur-de-vehicules-neufs-aux-particuliers-en-france-en-2021-65407c3c-67c9-11ec-8fe6-75ff3f7dbad0",
        premium=False,
        picture=False,
    )
    assert OuestFranceScraper().parse_headline(headline) == expected


def test_scrape_headline3():
    headline = query_from_file(TEST_DIR.joinpath("ouestfrance_article3.html")).find(
        "article"
    )
    expected = Headline(
        title=(
            "VIDÉO. Covid-19 : les jauges sanitaires ne s'appliquent pas aux meetings"
            " politiques"
        ),
        url="https://www.ouest-france.fr/sante/virus/coronavirus/video-covid-19-les-jauges-sanitaires-ne-s-appliquent-pas-aux-meetings-politiques-2e86bebd-2121-4b68-b9f0-f7bff4709c0b",
        premium=False,
        picture=True,
    )
    assert OuestFranceScraper().parse_headline(headline) == expected


def test_scrape_headline_prem():
    headline = query_from_file(
        TEST_DIR.joinpath("ouestfrance_article_premium.html")
    ).find("article")
    expected = Headline(
        title=(
            "Covid-19. Sa fille reçoit une dose du vaccin Moderna par erreur, le père"
            " va porter plainte"
        ),
        url="https://www.ouest-france.fr/normandie/avranches-50300/pres-d-avranches-au-centre-de-ponts-une-fillette-recoit-une-dose-du-vaccin-moderna-par-erreur-4885ed94-64cb-11ec-8f86-070a54080f2e",
        premium=True,
        picture=True,
    )
    assert OuestFranceScraper().parse_headline(headline) == expected
