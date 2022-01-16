from scrape_leparisien import LeParisienScraper
from scraper import Headline
from utils import query_from_file, split_article, TEST_DIR


def test_split_articles():
    split_article(html_name="leparisien", scraper=LeParisienScraper(), num_articles=112)


def test_scrape_headline():
    headline = query_from_file(TEST_DIR.joinpath("leparisien_article.html"))
    expected = Headline(
        title="Un homme soupçonné de féminicide en Espagne arrêté en Charente-Maritime",
        url="https://www.leparisien.fr/faits-divers/un-homme-soupconne-de-feminicide-en-espagne-arrete-en-charente-maritime-11-01-2022-YFMFVTSD7VGUDK7FE23553EYJA.php",
        premium=False,
        picture=False,
    )
    assert LeParisienScraper().parse_headline(headline) == expected


def test_scrape_headline_prem():
    headline = query_from_file(TEST_DIR.joinpath("leparisien_article_prem.html")).find(
        "div"
    )
    expected = Headline(
        title=(
            "Passe vaccinal : les nouveaux vaccinés pourraient l’obtenir avant même"
            " leur 2e dose"
        ),
        url="https://www.leparisien.fr/societe/sante/passe-vaccinal-les-nouveaux-vaccines-pourraient-lobtenir-avant-meme-leur-2e-dose-25-12-2021-I3FJAXWRMRFPVAGR6LJVJSIX2U.php",
        premium=True,
        picture=True,
    )
    assert LeParisienScraper().parse_headline(headline) == expected


def test_scrape_headline_prem2():
    headline = query_from_file(TEST_DIR.joinpath("leparisien_article_prem2.html")).find(
        "div"
    )
    expected = Headline(
        title=(
            "«C’est allé trop loin» : après la mort de MavaChou, les regrets d’une"
            " communauté toxique"
        ),
        url="https://www.leparisien.fr/societe/cest-alle-trop-loin-apres-la-mort-de-mavachou-les-regrets-dune-communaute-toxique-24-12-2021-EWNTEHCOYZCJ3IXZ6JDGLPS5JM.php",
        premium=True,
        picture=True,
    )
    assert LeParisienScraper().parse_headline(headline) == expected


def test_scrape_headline_prem_short():
    headline = query_from_file(
        TEST_DIR.joinpath("leparisien_article_prem_short.html")
    )
    expected = Headline(
        title=(
            "Un milliard de doses de vaccin distribuées, mais... Pourquoi Covax laisse"
            " un goût amer aux pays pauvres"
        ),
        url="https://www.leparisien.fr/societe/sante/un-milliard-de-doses-de-vaccin-distribuees-mais-pourquoi-covax-laisse-un-gout-amer-aux-pays-pauvres-16-01-2022-IEF5FNZWT5HYLJMZGQ47F36T7I.php",
        premium=True,
        picture=False,
    )
    assert LeParisienScraper().parse_headline(headline) == expected
