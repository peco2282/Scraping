import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20171124102832/https://www.mizuhobank.co.jp/rate/interest.html"

r = requests.get(url=url)
soup = BeautifulSoup(r.content, "html.parser")
soup_table = soup.select_one("table[summary=\"外貨普通預金金利・為替相場\"]")
# print(soup_table)
for tr in soup_table.select("tr"):
    cell1, cell2 = tr.select('*')
    print(cell1.string.strip(), cell2.string.strip())

