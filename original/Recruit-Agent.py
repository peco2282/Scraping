from pprint import pprint

import requests
from bs4 import BeautifulSoup

url = "https://next.rikunabi.com/tech_soft/lst_jb0505040000"
base = "https://next.rikunabi.com"
r = requests.get(url=url)

soup = BeautifulSoup(r.content, "html.parser")
soup = soup.select(".rnn-jobOfferList__item")
_soup_dict = {}

for t in soup:
    _title_soup = t.select(".js-abScreen__title a")
    _income_soup = t.select(".js-abScreen__income td")
    # print(_title_soup)
    # print(_income_soup)
    _soup_dict[_title_soup[0]] = _income_soup[0] if _income_soup else None

for i, k in enumerate(_soup_dict, 1):
    # print(k)
    print(f"{i}\n |- Company: {k.text.strip()}\n |- Income: {_soup_dict[k].text.strip() if _soup_dict[k] else '未記入'}\n L_ URL: {base}{k['href'].strip()}")
    print()

# empty_soup = []
# empty_income = []
#
# for t in soup:
#     _soup = t.select(".rnn-textLl a")
#     _income = t.select(".js-abScreen__income td")
#     if _soup:
#         empty_soup.append(_soup[0])
#
#     if _income:
#         empty_income.append(_income[0])
#
#
# empty_soup = list(dict.fromkeys(empty_soup))
# for i in range(len(empty_soup)):
#     print(f"{base}{empty_soup[i]['href']} : {empty_soup[i].text}\n"
#           f"                   {empty_income[i].text.split()}")

