from selenium import webdriver
import time

driver = webdriver.Chrome("./selenium/chromedriver")
driver.implicitly_wait(3)
driver.get("http://ecos.bok.or.kr/jsp/vis/keystat/#/key")
driver.implicitly_wait(3)

excel_download = driver.find_element_by_css_selector('img[alt="download"]')
driver.implicitly_wait(3)

excel_download.click()
time.sleep(5)
driver.close()

