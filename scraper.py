import csv
import datetime
import logging
import re
from dataclasses import dataclass, fields, asdict
from pathlib import Path
from typing import List
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup, element


@dataclass
class Headline:
    premium: bool  # If the article is behind a paywall
    picture: bool  # If the article has a picture
    title: str  # Title of the article
    url: str  # URL of the article


def format_title(x: str) -> str:
    x = x.strip()
    x = x.replace("\n", " ")
    x = x.replace("\xa0", " ")  # Normalise non-breaking space
    return re.sub(" +", " ", x)


class Scraper:
    name: str
    url: str
    out_dir: Path  # Output directory
    max_headlines: int
    debug_mode: bool  # If yes, output intermediary html files
    headlines: List[Headline]

    def __init__(self, debug_mode: bool) -> None:
        self.out_dir = Path("data")
        self.debug_mode = debug_mode
        self.headlines = []
        self.out_dir.mkdir(exist_ok=True)
        self.max_headlines = 50

    def retrieve_webpage(self) -> BeautifulSoup:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(
            options=options,
            executable_path=ChromeDriverManager(log_level=logging.WARNING).install(),
        )
        driver.get(self.url)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, "html.parser")
        return soup

    def split_headlines(self, soup: BeautifulSoup) -> List[element.Tag]:
        tags_headline = soup.find_all("article")
        return tags_headline

    def parse_headline(self, tag: element.Tag) -> Headline:
        logging.debug(tag)
        is_premium = self.parse_premium(tag)
        has_picture = self.parse_picture(tag)
        url = self.parse_url(tag)
        title = self.parse_title(tag)
        headline = Headline(
            title=title, url=url, premium=is_premium, picture=has_picture
        )
        return headline

    def parse_premium(self, tag: element.Tag) -> bool:
        is_premium = False
        return is_premium

    def parse_picture(self, tag: element.Tag) -> bool:
        has_picture = True if tag.find("img") else False
        return has_picture

    def parse_url(self, tag: element.Tag) -> str:
        if a := tag.find("a"):
            link = a["href"]
        else:
            link = tag["href"]
        if link.startswith("/"):
            link = self.url + link
        return link

    def parse_title(self, tag: element.Tag) -> str:
        if tag.find("span"):
            tag.span.extract()
        title = format_title(tag.text)
        return title

    def output_to_csv(self):

        # Warn if no headlines
        if len(self.headlines) == 0:
            logging.warning(f"{self.name} - Found no headlines")

        # File to output
        utc_now = datetime.datetime.now(datetime.timezone.utc)
        timestamp = utc_now.strftime("%Y-%m-%dT%H-%M%SZ")
        out_file = self.out_dir / f"{timestamp}_{self.name}.csv"
        logging.info(
            f"{self.name} - Output top {self.max_headlines} headlines to {out_file.absolute()}"
        )

        with open(out_file, "w", newline="", encoding="utf-8") as f_out:
            csv_writer = csv.DictWriter(
                f_out,
                fieldnames=[f.name for f in fields(Headline)],
                quoting=csv.QUOTE_ALL,
            )
            csv_writer.writeheader()
            for headline in self.headlines[: self.max_headlines]:
                csv_writer.writerow(asdict(headline))

    def scrape(self, max_headlines: int = 50):
        # Set max headlines to output
        self.max_headlines = max_headlines

        # Retrieve page
        logging.info(f"{self.name} - Retrieve webpage {self.url}")
        soup = self.retrieve_webpage()
        if self.debug_mode:
            html_out = self.out_dir / f"headlines-{self.name}.html"
            # utf-8 html_out avoid mismatches with locale Windows encoding
            with html_out.open("w", encoding="utf-8") as f_out:
                output = soup.prettify()
                f_out.write(output)

        # Split into tags
        logging.info(f"{self.name} - Split into tags")
        tags_headline = self.split_headlines(soup)
        if self.debug_mode:
            tags_out = self.out_dir / f"headlines-{self.name}-split.html"
            with tags_out.open("w", encoding="utf-8") as f_out:
                f_out.write("\n----\n".join([tag.prettify() for tag in tags_headline]))

        # Parse
        logging.info(f"{self.name} - Parse headlines from tags")
        for tag in tags_headline:
            self.headlines.append(self.parse_headline(tag))
        logging.info(f"{self.name} - Headlines parsed: {len(self.headlines)}")

        # Output to CSV
        self.output_to_csv()
