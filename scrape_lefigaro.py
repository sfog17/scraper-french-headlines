import re
from typing import List
from bs4 import BeautifulSoup, element
from scraper import Scraper, format_title


class LeFigaroScraper(Scraper):
    def __init__(self, debug_mode: bool = True) -> None:
        super().__init__(debug_mode)
        self.name = "lefigaro"
        self.url = "https://www.lefigaro.fr"

    def split_headlines(self, soup: BeautifulSoup) -> List[element.Tag]:
        homepage = soup.find(attrs={"data-section": "Actu"})
        tags_headline = [x for x in homepage.find_all(attrs={"data-fig-domain": True})]
        return tags_headline

    def parse_premium(self, tag: element.Tag) -> bool:
        is_premium = True if tag.find(attrs={"class": "fig-premium-mark"}) else False
        return is_premium

    def parse_title(self, tag: element.Tag) -> str:
        # Extract title, handle exceptions for article-related content
        regex = re.compile(r"fig-ensemble__title|fig-profile__headline")
        tag_title = tag.find(attrs={"class": regex})
        if tag_title:
            title_raw = tag_title.text
        else:
            title_raw = tag.text

        title = (
            format_title(title_raw)
            .replace(" (article premium)", "")
            .replace(" (article Premium)", "")
            .replace(" (Article Premium)", "")
        )

        return title
