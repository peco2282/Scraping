import time
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20190404030952/https://www.apple.com/jp/itunes/charts/free-apps/"
base = "https://web.archive.org/"

r = requests.get(url=url)
# print(r.content)
soup = BeautifulSoup(r.content, "html.parser")
soup = soup.select(".section-content img")
for t in soup:
    img = base + t["src"]
    print(img[-68:])
    with urlopen(url=img) as _img:
        data = _img.read()
        with open(file=f"images/{t['alt']}.png", mode="wb") as f:
            f.write(data)

        # time.sleep()
