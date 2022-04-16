from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.headless = True

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
browser = webdriver.Chrome('./webscraping_basic/chromedriver.exe', options=options)
browser.get("http://daum.net")
elem = browser.find_element_by_class_name("tf_keyword")
elem.send_keys("서울 매물")
elem.send_keys(Keys.ENTER)
url = browser.current_url
headers = {"User-Agent":user_agent}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

list_place = soup.find("ol", attrs={"class":"list_place"})
places = list_place.find_all("li")

for idx, place in enumerate(places):
    print("=========== 매물 {} ============".format(idx+1))
    info = place.get_text().split()
    name = f"{info[1][4:]} {info[2]}"
    type = info[1][1:3]
    price = info[3]
    area = info[5]
    floor = info[7]
    address = " ".join(info[10:])
    print(f"장소 : {name}")
    print(f"유형 : {type}")
    print(f"가격 : {price}")
    print(f"면적 : {area}")
    print(f"층 : {floor}")
    print(f"주소 : {address}")