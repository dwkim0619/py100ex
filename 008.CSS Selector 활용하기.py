# CSS(Cascading Style Sheets)
# mw-content-text > div > table:nth-child(3) > tbody > tr:nth-child(2) > td > a > img

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
# print(html_src)
soup = BeautifulSoup(html_src, "html.parser")

subway_img = soup.select("#mw-content-text > div > table:nth-child(3) > tbody > tr:nth-child(2) > td > a > img")
# print(subway_img)
print(subway_img[0])
print('-'*20)

subway_img2 = soup.select("td > a > img")
print(len(subway_img2))
print(subway_img2[0])
print(subway_img2[1])

