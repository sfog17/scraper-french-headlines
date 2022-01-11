import logging
from typing import List
from bs4 import BeautifulSoup, element
from scraper import Scraper, format_title


class FranceTvInfoScraper(Scraper):
    def __init__(self, debug_mode: bool = True) -> None:
        super().__init__(debug_mode)
        self.name = "francetvinfo"
        self.url = "https://mobile.francetvinfo.fr"

    def split_headlines(self, soup: BeautifulSoup) -> List[element.Tag]:
        content = soup.find("div", "content")
        tags_headline = []
        # Headers
        for a in content.find_all("a", attrs={"class": "flowItem"}, recursive=False):
            if a.find("p"):
                tags_headline.append(a)
        logging.debug(tags_headline)
        # Others
        for section in content.find_all("section"):
            for x in section.find_all("article"):
                if x.find("p"):
                    tags_headline.append(x.find("a"))

        return tags_headline

    def parse_title(self, tag: element.Tag) -> str:
        if tag.find("span"):
            tag.span.extract()
        title = format_title(tag.text)
        if title == "":
            title = format_title(tag.find("img")["alt"])

        return title
