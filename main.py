import logging
from scrape_lemonde import LeMondeScraper
from scrape_francetvinfo import FranceTvInfoScraper
from scrape_lefigaro import LeFigaroScraper
from scrape_vingtminutes import VingtMinutesScraper
from scrape_leparisien import LeParisienScraper
from scrape_ouestfrance import OuestFranceScraper
from scrape_bfmtv import BfmTvScraper
from scrape_mediapart import MediapartScraper
from scrape_cnews import CNewsScraper

logging.basicConfig(level=logging.INFO)


def run():
    scrapers = [
        LeMondeScraper(),
        FranceTvInfoScraper(),
        LeFigaroScraper(),
        OuestFranceScraper(),
        VingtMinutesScraper(),
        LeParisienScraper(),
        BfmTvScraper(),
        MediapartScraper(),
        CNewsScraper()
    ]

    for scr in scrapers:
        try:
            scr.scrape(max_headlines=50)
        except Exception as err:
            logging.warning(f"Failed to scrape {scr.name} at {scr.url}")
            logging.warning(err, exc_info=True)


if __name__ == "__main__":
    run()
