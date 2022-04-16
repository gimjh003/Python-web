from selenium import webdriver
import time
browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe")
browser.maximize_window() # 창 최대화
url = "https://m-flight.naver.com/"
browser.get(url)

# 가는 날 선택 클릭
time.sleep(3)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(3)

# 이번달 27일, 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
time.sleep(3)

# element를 찾을 때까지 기다리게 하는 방법
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "xpath 입력")))
    # 성공 하면 이후 동작 수행
finally:
    browser.quit()
# WebDriverWait이 최대 10초동안 기다리는데, 만약 어떤 xpath에 해당하는 element가 등장 할 때까지
