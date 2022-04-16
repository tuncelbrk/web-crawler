import urllib
from urllib.request import urlopen

import certifi
import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup, NavigableString, Tag


def download_url(url):
    return requests.get(url).text


def get_linked_urls(url, html):
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('div', class_='entry-content')
    extracted = data.pop()
    if extracted is not None:
        save_to_file(extracted, "../recepts.txt")

    # if soup.find_all('div', class_='icerik-card-box'):

    for link in soup.find_all('a'):
        path = link.get('href')
        if path and path.startswith('/'):
            path = urljoin(url, path)
        yield path


class Scraper:

    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):
        html = download_url(url)
        for url in get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)


def get_page(url):
    """Scrapes a URL and returns the HTML source.

    Args:
        url (string): Fully qualified URL of a page.

    Returns:
        soup (string): HTML source of scraped page.
    """

    response = urllib.request.urlopen(urllib.request.Request(url,
                                                             headers={'User-Agent': 'Mozilla'}), cafile=certifi.where())
    soup = BeautifulSoup(response,
                         'html.parser',
                         from_encoding=response.info().get_param('charset'))

    return soup


def save_to_file(data, receipt_file):
    with open(receipt_file, 'a') as the_file:

        for span in data.contents:
            if "<p>" in str(span) and "<img" not in str(span):

                the_file.write(str(span))


if __name__ == '__main__':
    Scraper(urls=['https://www.ardaninmutfagi.com/yemek-tarifleri/soslar/bbq-sos-yer-fistigi-sosu']).run()
