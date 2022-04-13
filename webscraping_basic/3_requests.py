# Python에서 HTML 문서 정보를 얻기 위해 사용하는 requests 라이브러리에 대해 알아본다.

# pip install requests
import requests
# res = requests.get("http://naver.com")
res = requests.get("http://google.com")
# print("응답코드 :", res.status_code) # 200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 {}]".format(res.status_code))

res.raise_for_status() # 문제가 있으면 이 지점에서 프로그램 중단
print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as file:
    file.write(res.text)