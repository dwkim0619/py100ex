import requests
from bs4 import BeautifulSoup
import urllib

keyword_input = "파이썬"
keyword_input = urllib.parse.quote(keyword_input)
print("파이썬 문자열을 URL 코드로 변환 : ", keyword_input)

base_url = "https://news.google.com"
search_url = base_url + "/search?q=" +  keyword_input + "&hl=ko&gl=KR&ceid=KR%3Ako"
print("검색어와 조합한 URL : ", search_url)


def google_news_clipping_keyword(keyword_input, limit=5):
    keyword = urllib.parse.quote(keyword_input)
    url =  base_url + "/search?q=" +  keyword + "&hl=ko&gl=KR&ceid=KR%3Ako"

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    news_items = soup.select('div[class="xrnccd"]')

    titles = []; links = []; contents = []

    for item in news_items:
        link = item.find('a', attrs={"class": "VDXfz"}).get("href")
        news_link = base_url + link
        links.append(news_link)

        news_title = item.find('a', attrs={"class": "DY5T1d"}).getText()
        titles.append(news_title)

        news_content = item.find('span', attrs={"class": "xBbh9"}).getText()
        contents.append(news_content)

        # news_agency = item.find('a', attrs={"class": "wEwyrc AVN2gc uQIVzc Sksgp"}).text
        
        # news_reporting = item.find('time', attrs={"class": "WW6dff uQIVzc Sksgp"})
        # news_reporting_datetime = news_reporting.get("datetime").split("T")
        # news_reporting_date = news_reporting_datetime[0]
        # news_reporting_time = news_reporting_datetime[1][:-1]
        # print(news_agency + ' ' + news_reporting_date + ' ' + news_reporting_time)

    result = {'link': links, 'title': titles, 'content': contents}
    return result

search_word = input("검색어를 입력하세요 : ")
news = google_news_clipping_keyword(search_word)
print(len(news['title']))
print(news['title'])

    