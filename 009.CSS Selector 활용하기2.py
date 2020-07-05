import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, "html.parser")

links = soup.select('a')
print(len(links))

links_external = soup.select('a[class="external text"]')
print(len(links_external))
print(links_external[:3])

print('-'*30)

id_selector = soup.select('#siteNotice')
print(len(id_selector))
print(id_selector)

print('-'*30)

# id_selector2 = soup.select('div#siteNotice')
# print(len(id_selector2))
# print(id_selector2)
#
# print('-'*30)
#
# id_selector3 = soup.select('p#siteNotice')
# print(len(id_selector3))
# print(id_selector3)

class_selector = soup.select(".mw-headline")
print(len(class_selector))
print(class_selector)

print('-'*30)

class_selector2 = soup.select("span.mw-headline")
print(len(class_selector2))
print(class_selector2)
