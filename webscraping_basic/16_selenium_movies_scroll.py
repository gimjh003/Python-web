import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://play.google.com/store/movies"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
headers = {"User-Agent":user_agent, "Accept-Language":"ko-KR,ko"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe")
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

movies = soup.find_all("a", attrs={"class":"Si6A0c ZD8Cqc"})

for movie in movies:
    if movie:
        title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
        print(title)
