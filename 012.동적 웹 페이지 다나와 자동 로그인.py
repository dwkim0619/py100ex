from selenium import webdriver

driver = webdriver.Chrome("./selenium/chromedriver")
driver.implicitly_wait(3)
# driver.get("https://www.danawa.com/")
driver.get("https://www.naver.com")
#
# login = driver.find_element_by_css_selector("li.my_page_service > a")
login = driver.find_element_by_css_selector("#account > a")
print("HTML 요소: ", login)
print("태그 이름: ", login.tag_name)
print("문자열: ", login.text)
print("href 속성: ", login.get_attribute("href"))
login.click()
driver.implicitly_wait(3)

driver.find_element_by_css_selector("#id").send_keys("")
driver.implicitly_wait(2)
driver.find_element_by_css_selector("#pw").send_keys("")
driver.implicitly_wait(2)
driver.find_element_by_css_selector("#log\.login").click()


