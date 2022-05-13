import requests
from bs4 import BeautifulSoup
url = "https://qiita.com/advent-calendar/2016/crawler"
r = requests.get(url=url)
soup = BeautifulSoup(r.content, "html.parser")
soup_con = soup.select(".adventCalendarCalendar_comment a")
soup_auth = soup.select(".adventCalendarCalendar_author a")
print(soup)
for i in range(len(soup_con)):
    print(f"Author: {soup_auth[i]['href'].replace('/', '')}, Url:  {soup_con[i]['href']}, Title: {soup_con[i].text}")

# print()
# print(soup.select("body"))
