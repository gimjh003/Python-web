import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
url = "https://play.google.com/store/movies"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
headers = {"User-Agent":user_agent, "Accept-Language":"ko-KR,ko"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe", options=options)
browser.maximize_window()

# 페이지 이동
browser.get(url)

# 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")

# 화면 가장 아래로 스크롤 내리기
interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height

browser.get_screenshot_as_file("google_movie.png")
movies = soup.find_all("a", attrs={"class":"Si6A0c ZD8Cqc"})

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    price = movie.find("span")
    prices = price.find_all("span")
    if len(prices) < 2:
        continue
    else:
        link = "http://play.google.com"+movie["href"]
        print(f"제목 : {title}")
        print(f"할인 전 금액 : {prices[1].get_text()}")
        print(f"할인 후 금액 : {prices[3].get_text()}")
        print(f"링크 : {link}")
        print("-"*100)
    
browser.quit()