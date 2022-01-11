from typing import List
from bs4 import BeautifulSoup, element
from scraper import Scraper, format_title


class BfmTvScraper(Scraper):
    def __init__(self, debug_mode: bool = True) -> None:
        super().__init__(debug_mode)
        self.name = "bfmtv"
        self.url = "https://www.bfmtv.com"

    def split_headlines(self, soup: BeautifulSoup) -> List[element.Tag]:
        tags_headline = []
        main = soup.find("main")
        for tag in main.find_all("a"):
            if tag["href"][-4:] == "html" and not tag.find(
                # Exclude News 24/7
                "div",
                attrs={"class": "content_item_time"},
            ):
                tags_headline.append(tag)

        return tags_headline

    def parse_title(self, tag: element.Tag) -> str:
        if tag.find(attrs={"class": "quote_text"}):
            quote = tag.find(attrs={"class": "quote_text"}).text
            author = tag.find(attrs={"class": "quote_author_description"}).text
            title = format_title(quote + ". " + author)
        elif tag_title := tag.find(attrs={"class": "title_une_item"}):
            title = format_title(tag_title.text)
        elif tag_title := tag.find(attrs={"class": "content_item_title"}):
            title = format_title(tag_title.text)
        else:
            title = format_title(tag.text)
        return title
