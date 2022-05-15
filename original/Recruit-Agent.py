import re
import time

import requests
from bs4 import BeautifulSoup, Tag
from requests import Response

url = "https://next.rikunabi.com/tech_soft/lst_jb0505040000/crn{}.html"
base = "https://next.rikunabi.com"


def request(crn: int):
    r: Response = requests.get(url=url.format(crn))

    _soup: BeautifulSoup = BeautifulSoup(r.content, "html.parser")
    soup: list[Tag] = _soup.select(".rnn-jobOfferList__item")
    _soup_dict = {}

    for t in soup:
        _title_soup = t.select(".js-abScreen__title a")
        _income_soup = t.select(".js-abScreen__income td")
        # print(_title_soup)
        # print(_income_soup)
        _soup_dict[_title_soup[0]] = _income_soup[0] if _income_soup else None

    for i, k in enumerate(_soup_dict, 0):
        # print(k)
        print(f"{crn + i}\n |- Company: {k.text.strip()}\n |- Income: {_soup_dict[k].text.strip() if _soup_dict[k] else '未記入'}\n L_ URL: {base}{re.sub(r'&list_disp_no=[0-9]+&leadtc=n_ichiran_cst_bakuten_ttl', '', k['href'].strip())}")
        print()


if __name__ == "__main__":
    for i in range(25):
        request(crn=(i * 50 + 1))
        time.sleep(5)
        print("-" * 50)
