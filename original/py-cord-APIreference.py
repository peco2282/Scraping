import requests
from bs4 import BeautifulSoup

url = "https://docs.pycord.dev/en/master/api.html"

r = requests.get(url=url)
soup = BeautifulSoup(r.content, "html.parser")
soup = soup.select(".py dt,dd")
x = 0
for i in soup:
    # for s in i.select(".sig"):
    #     print(s)
    print(i)
    print()
    x += 1
    if x == 6:
        break

# print(soup)
