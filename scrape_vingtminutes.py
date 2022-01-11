from typing import List
from bs4 import BeautifulSoup, element
from scraper import Scraper, format_title


class VingtMinutesScraper(Scraper):
    def __init__(self, debug_mode: bool = True) -> None:
        super().__init__(debug_mode)
        self.name = "vingtminutes"
        self.url = "https://www.20minutes.fr"

    def split_headlines(self, soup: BeautifulSoup) -> List[element.Tag]:
        # Remove the box with "latest","most read/shared", because it is not an editorial choice
        tabpanel = soup.find("div", attrs={"class": "tabpanel"})
        tabpanel.extract()

        tags_headline = []
        for x in soup.find_all(["article", "li"]):
            if x.find(attrs={"class": "teaser-title"}):
                tags_headline.append(x)

        return tags_headline

    def parse_title(self, tag: element.Tag) -> str:
        tag_title = tag.find(attrs={"class": "teaser-title"})
        title = format_title(tag_title.text)
        return title
