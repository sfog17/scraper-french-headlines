import re
from typing import List
from bs4 import BeautifulSoup, element
from scraper import Scraper, format_title


class OuestFranceScraper(Scraper):
    def __init__(self, debug_mode: bool = True) -> None:
        super().__init__(debug_mode)
        self.name = "ouestfrance"
        self.url = "https://www.ouest-france.fr"

    def split_headlines(self, soup: BeautifulSoup) -> List[element.Tag]:
        tags = soup.find_all("article", attrs={"class": True})
        # exclude adds
        regex = re.compile(r"www.ouestfrance-(auto|emploi|immo).com")
        tags_headline = [t for t in tags if not regex.search(str(t))]
        return tags_headline

    def parse_premium(self, tag: element.Tag) -> bool:
        is_premium = True if tag.find(attrs={"class": "su-icon"}) else False
        return is_premium

    def parse_title(self, tag: element.Tag) -> str:
        span = tag.find("span", attrs={"class": "su-title"})
        if span:
            unwanted_text = span.find("i")
            if unwanted_text:
                unwanted_text.extract()
            unwanted_text_bis = span.find("span")
            if unwanted_text_bis:
                unwanted_text_bis.extract()
            title = format_title(span.text)
        else:
            title = format_title(tag.find("a").text)
        return title
