from bs4 import BeautifulSoup, element
from scraper import Scraper, format_title
from typing import List


class MediapartScraper(Scraper):
    def __init__(self, debug_mode: bool = True) -> None:
        super().__init__(debug_mode)
        self.name = "mediapart"
        self.url = "https://www.mediapart.fr"

    def split_headlines(self, soup: BeautifulSoup) -> List[element.Tag]:
        tags_headline = soup.find_all("div", attrs={"class": "teaser__container"})
        return tags_headline

    def parse_premium(self, tag: element.Tag) -> bool:
        is_premium = True
        return is_premium

    def parse_title(self, tag: element.Tag) -> str:
        tag_title = tag.find(attrs={"class": "teaser__title"})
        title = format_title(tag_title.text)
        return title
