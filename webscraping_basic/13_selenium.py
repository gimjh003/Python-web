'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome() # "./chromedriver.exe"
browser.get("http://naver.com")
elem = browser.find_element_by_class_name("link_login")
elem.click()
browser.back()
elem = browser.find_element_by_id("query")
elem.send_keys("My first selenium")
elem.send_keys(Keys.ENTER)
elem = browser.find_elements_by_tag_name("a")
for e in elem:
    e.get_attribute("href")
    
browser.get("http://daum.net")
elem = browser.find_element_by_name("q")
elem.send_keys("My first selenium")
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
elem.click()
browser.quit() # close 메소드는 탭을 닫는 것, quit은 전체 종료
'''
from selenium import webdriver
import time

browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe")
# 1. 네이버 이동
browser.get("http://naver.com")
# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()
# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")
# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
time.sleep(3)
# 5. id 를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")
# 6. html 정보 출력
print(browser.page_source)
# 7. 브라우저 종료
browser.quit()