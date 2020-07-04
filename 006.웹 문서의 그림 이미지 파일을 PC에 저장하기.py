import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
# print(type(resp))
html_src = resp.text

soup = BeautifulSoup(html_src, "html.parser")

filename_img = "Seoul-Metro-2004-20070722.jpg"
target_img = soup.find(name="img", attrs={"alt": filename_img})
# print(type(target_img))
target_img_src = target_img.get("src")
# print(target_img_src)

target_img_resp = requests.get("http:" + target_img_src)
out_file_path = "./output/" + filename_img

with open(out_file_path, "wb") as out_file:
    out_file.write(target_img_resp.content)
    print("Saved Image.")
