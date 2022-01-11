from typing import List
from bs4 import BeautifulSoup, element
from scraper import Scraper, format_title


class LeMondeScraper(Scraper):
    def __init__(self, debug_mode: bool = True) -> None:
        super().__init__(debug_mode)
        self.name = "lemonde"
        self.url = "https://www.lemonde.fr"

    def split_headlines(self, soup: BeautifulSoup) -> List[element.Tag]:
        homepage = soup.find_all("section", "zone")
        tags_headline = []
        for page in homepage:
            for div in page.find_all("div", ["article", "podcast-area"]):
                for a in div.find_all("a"):
                    tags_headline.append(a)
        return tags_headline

    def parse_premium(self, tag: element.Tag) -> bool:
        is_premium = True if tag.find("span", "sr-only") else False
        return is_premium

    def parse_title(self, tag: element.Tag) -> str:
        if title_tag := tag.find(attrs={"class": "article__title"}):
            title = format_title(title_tag.text)
        elif title_tag := tag.find(attrs={"class": "podcast-area__title"}):
            title = format_title(title_tag.text)
        else:
            if tag.find("span"):
                tag.span.extract()  # Remove potential tags for paid articles
            title = format_title(tag.text)

        return title
