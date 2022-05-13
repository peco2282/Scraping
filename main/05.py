import time
from typing import List

import requests
from bs4 import BeautifulSoup, Tag

url = "https://gihyo.jp/dp"

r = requests.get(url=url)
soup: BeautifulSoup = BeautifulSoup(r.content, "html.parser")
_soup: List[Tag] = soup.select("#listBook a[itemprop='url']")
soup: List[Tag] = soup.select(".title p[itemprop='name']")
for s in soup:
    print(soup)
    time.sleep(1)
