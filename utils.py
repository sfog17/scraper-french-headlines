from pathlib import Path
from bs4 import BeautifulSoup
from scraper import Scraper

TEST_DIR = Path("test-resources/")
TEST_OUT_DIR = Path("test-output/")
TEST_OUT_DIR.mkdir(exist_ok=True)


def query_from_file(in_file: Path):
    with in_file.open("r", encoding="utf-8") as f_in:
        soup = BeautifulSoup(f_in, "html.parser")
    return soup


def split_article(html_name: str, scraper: Scraper, num_articles: int):
    soup = query_from_file(TEST_DIR.joinpath(f"{html_name}.html"))
    tags = scraper.split_headlines(soup)
    file_out_path = TEST_OUT_DIR / f"{html_name}-split.html"
    with file_out_path.open("w", encoding="utf-8") as f_out:
        f_out.write("\n----\n".join([tag.prettify() for tag in tags]))
    assert len(tags) == num_articles
