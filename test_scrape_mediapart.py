from scrape_mediapart import MediapartScraper
from scraper import Headline
from utils import query_from_file, split_article, TEST_DIR


def test_split_articles():
    split_article(
        html_name="mediapart", scraper=MediapartScraper(), num_articles=72
    )


def test_scrape_headline():
    headline = query_from_file(TEST_DIR.joinpath("mediapart_article.html"))
    expected = Headline(
        title="Au studio photo de Louis Vuitton, trois salariés seulement et une armée d’« indépendants »",
        url="https://www.mediapart.fr/journal/economie/070122/au-studio-photo-de-louis-vuitton-trois-salaries-seulement-et-une-armee-d-autoentrepreneurs",
        premium=True,
        picture=True,
    )
    assert MediapartScraper().parse_headline(headline) == expected
