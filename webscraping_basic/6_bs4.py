import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력 
# print(soup.a.attrs) # a element 의 속성 정보를 출력 (딕셔너리)
# print(soup.a.attrs["href"]) # same as print(soup.a["href"]) / a element의 href 속성 '값' 정보를 출력

# attribute = element에게 추가 정보를 제공
# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # soup.a처럼 처음 발견되는 element를 가져옴, 차이점이라면 조건을 붙일 수 있음 (예: class 어트리뷰트 겂이 "Nbtn_upload"인 a element)
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element를 찾아달라는 뜻이다. (태그를 지정하지 않아도 가능)

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a) # li element 내부에 있는 a element를 가져옴
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li") # 형제 태그를 찾을 때에도 조건 설정 가능
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="")
print(webtoon)