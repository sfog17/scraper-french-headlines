import re
from typing import List
from bs4 import BeautifulSoup, element
from scraper import Scraper, format_title


class LeParisienScraper(Scraper):
    def __init__(self, debug_mode: bool = True) -> None:
        super().__init__(debug_mode)
        self.name = "leparisien"
        self.url = "https://www.leparisien.fr"

    def split_headlines(self, soup: BeautifulSoup) -> List[element.Tag]:
        tags_headline = []
        regex = re.compile(r"story-preview|SectionFeedVertical")
        tags = soup.find_all("div", attrs={"class": regex})
        for t in tags:
            if "story-preview" in t["class"]:
                tags_headline.append(t)
            else:
                tags_headline.extend(t.find_all("li"))

        return tags_headline

    def parse_url(self, tag: element.Tag) -> str:
        link = tag.find("a")["href"]
        if link.startswith("//www"):
            link = link.replace("//www", "https://www")
        elif link.startswith("/"):
            link = self.url + link
        return link

    def parse_premium(self, tag: element.Tag) -> bool:
        is_premium = True if tag.find("span", attrs={"class": "abo"}) else False
        return is_premium

    def parse_title(self, tag: element.Tag) -> str:
        if tag.find(attrs={"class": "story-headline"}):
            tag_title = tag.find(attrs={"class": "story-headline"}).text
        elif tag.find(attrs={"class": "story-headline-highlight"}):
            tag_title = tag.find(attrs={"class": "story-headline-highlight"}).text
        else:
            tag_title = tag.text
        title = format_title(tag_title)
        return title
