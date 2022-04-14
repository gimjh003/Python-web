import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=20853"
res = requests.get(url)
res.raise_for_status() # res = response (request에 따른 response)

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})

# 만화 제목 + 링크 가져오기
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com"+cartoon.a["href"]
    print(title)
    print(link)
    print()

# 평점 구하기
total_rates = 0
ratings = soup.find_all("div", attrs={"class":"rating_type"})
for rating in ratings:
    rate = rating.strong.get_text()
    total_rates += float(rate)
print("전체 점수 : {:.2f}".format(total_rates))
print("평균 점수 : {:.2f}".format(total_rates/len(ratings)))