from selenium import webdriver
from bs4 import BeautifulSoup
import time

item_found = 0
while not item_found:
    keyword = ""
    while len(keyword) == 0:
        keyword = str(input("검색할 항목을 입력하세요 : "))

    driver = webdriver.Chrome("./selenium/chromedriver")
    driver.implicitly_wait(3)
    driver.get("http://ecos.bok.or.kr/jsp/vis/keystat/#/key")
    time.sleep(5)

    items1 = driver.find_elements_by_css_selector('a[class="ng-binding"]')
    items2 = driver.find_elements_by_css_selector('a[class="a-c1-list ng-binding"]')
    items3 = driver.find_elements_by_css_selector('a[class="a-c4-list ng-binding"]')
    driver.implicitly_wait(3)

    items = items1[1:] + items2 + items3

    for idx, item in enumerate(items):
        if keyword in item.text:
            print("검색어 '%s'에 매칭되는 '%s' 통계지표를 검색 중..." % (keyword, item.text))
            item.click()
            item_found = 1
            time.sleep(5)
            break
        elif idx == (len(items) -1):
            print("검색어 '%s'에 대한 통계지표가 존재하지 않습니다..." % keyword)
            driver.close()
            continue
        else:
            pass

    html_src = driver.page_source
    soup = BeautifulSoup(html_src, "html.parser")
    driver.close()

    table_items =soup.find_all('td', {'class': 'ng-binding'})
    date = [t.text for i, t in enumerate(table_items) if i % 3 == 0]
    value = [t.text for i, t in enumerate(table_items) if i % 3 == 1]
    change = [t.text for i, t in enumerate(table_items) if i % 3 == 2]

    result_file = open('./output/bok_statistics_%s.csv' % keyword, 'w')
    for i in range(len(date)):
        result_file.write("%s, %s, %s" % (date[i], value[i].replace(',', ''), change[i].replace(',', '')))
        result_file.write('\n')
    result_file.close()

    print(date, value, change)