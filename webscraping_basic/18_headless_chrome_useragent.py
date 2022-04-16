import requests
from bs4 import BeautifulSoup
from selenium import webdriver
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")
headers = {"User-Agent":user_agent, "Accept-Language":"ko-KR,ko"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe", options=options)
browser.maximize_window()

browser.get(url)
detected_value = browser.find_element_by_id("detected_value").text
print(detected_value)