import time

import requests
from bs4 import BeautifulSoup
from requests import Response

url = "https://crowdworks.jp/public/jobs?category=jobs&order=score&page={}"
base_url = "https://crowdworks.jp"

PAGES: int = 5  # 1 <= PAGES <= 199


def check(i: int) -> None:
    r: Response = requests.get(url=url.format(i))
    if r.status_code != 200:
        return
    soup: BeautifulSoup = BeautifulSoup(r.content, "html.parser")
    print(soup.select(".job_data_column a"))
    print(soup.select(".job_data_column a"))
    with open(file="works.txt", mode="a", encoding="utf8") as f:
        f.write(f"Page:{i}\n")
        for t in soup.select(".job_data_column a"):
            if t['href'].startswith("/public/jobs/category/"):
                content = f"{base_url}{t['href']} , category: {t.text.strip()}"
                print(content)
                f.write(content + "\n")
            else:
                content = f"{base_url}{t['href']} , title: {t.text.strip()}"
                print(content)
                f.write(content + "\n")

        f.write("\n\n")


if __name__ == "__main__":
    for i in range(PAGES):
        check(i)
        time.sleep(5)
        print("----------------")
