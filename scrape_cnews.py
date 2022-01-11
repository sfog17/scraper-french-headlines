import re
from bs4 import BeautifulSoup, element
from scraper import Scraper, format_title
from typing import List


class CNewsScraper(Scraper):
    def __init__(self, debug_mode: bool = True) -> None:
        super().__init__(debug_mode)
        self.name = "cnews"
        self.url = "https://www.cnews.fr"

    def split_headlines(self, soup: BeautifulSoup) -> List[element.Tag]:
        tags_headline = []
        blocks = soup.find_all("div", attrs={"class": "dm-block"})
        for b in blocks:
            for t in b.find_all("a", attrs={"href": True}):
                if t.find(attrs={"class": re.compile(r"title")}):
                    tags_headline.append(t)
        return tags_headline

    def parse_title(self, tag: element.Tag) -> str:
        tag_title = tag.find(attrs={"class": re.compile(r"title")})
        title = format_title(tag_title.text)
        return title
