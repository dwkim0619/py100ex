# https://news.google.com
# https://news.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&hl=ko&gl=KR&ceid=KR%3Ako

import requests
from bs4 import BeautifulSoup

base_url = "https://news.google.com"
search_url = base_url + "/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&hl=ko&gl=KR&ceid=KR%3Ako"

resp = requests.get(search_url)
html_src = resp.text
soup = BeautifulSoup(html_src, "html.parser")

news_items = soup.select('div[class="xrnccd"]')
for item in news_items:
    link = item.find('a', attrs={"class": "VDXfz"}).get("href")
    news_link = base_url + link
    # print(news_link)

    news_title = item.find('a', attrs={"class": "DY5T1d"}).getText()
    print("[" + news_title + "]" + "(" + news_link + ")")

    news_content = item.find('span', attrs={"class": "xBbh9"}).getText()
    print(news_content)

    news_agency = item.find('a', attrs={"class": "wEwyrc AVN2gc uQIVzc Sksgp"}).text
    # print(news_agency)

    news_reporting = item.find('time', attrs={"class": "WW6dff uQIVzc Sksgp"})
    news_reporting_datetime = news_reporting.get("datetime").split("T")
    news_reporting_date = news_reporting_datetime[0]
    news_reporting_time = news_reporting_datetime[1][:-1]
    print(news_agency + ' ' + news_reporting_date + ' ' + news_reporting_time)