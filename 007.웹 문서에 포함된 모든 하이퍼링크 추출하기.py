import requests, re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, "html.parser")

links = soup.find_all("a")
print("Link Count : ", len(links))
print(links[:3])
print("------------------------------------")

links_wiki = soup.find_all(name="a", href=re.compile("/wiki/"), limit=3)
print(links_wiki)
print("------------------------------------")

links_external = soup.find_all(name="a", attrs={"class": "external text"}, limit=3)
print(links_external)
