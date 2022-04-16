from crawler.robots import to_dataframe
from crawler.scraper import get_page
from utils.helper import read_url_file


def display_robots(url):
    print(f"__url = {url}")
    robots = get_page(url)
    robots_data = to_dataframe(robots)
    print(robots_data)


lines = read_url_file("../urls.txt")
for line in lines:
    url = f"{line}/robots.txt"
    display_robots(url)
