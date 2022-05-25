from typing import List

import requests
from bs4 import BeautifulSoup, Tag
from requests import Response


def request():
    # url = "https://jp.mercari.com/"
    url = "https://twitter.com/azurlane_staff"

    r: Response = requests.get(url=url)
    print(r.content)

    _soup: BeautifulSoup = BeautifulSoup(r.content, "html.parser")
    soup: List[Tag] = _soup.select(".css-901oao")
    for s in soup:
        print(s.text)


if __name__ == "__main__":
    request()
