# User Agent를 바꿔서 정상적인 사용자로 보이도록 하는 방법에 대해 알아보았다.
# Python으로 request를 할 경우 비정상적인 접근이라고 판단해 접근을 차단할 수도 있다.

# python user agent = python-requests/2.27.1
# chrome user agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36
# 헤더 참고자료 : https://velog.io/@jkijki12/HTTP-Header-%EC%A0%95%EB%A6%AC

import requests
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
headers = {"User-Agent":"Hello, World!"} # 웹 사이트에서는 접근하는 주체에 대한 정보를 알 수 있다.
# 이를 헤더정보라고 하며, User-Agent는 그 헤더정보 중 하나이다.

res = requests.get(url, headers=headers) # 이 코드를 통해 헤더정보를 임의로 수정해서 request 할 수 있다.
res.raise_for_status() # status code에 따라 프로그램 흐름을 결정한다.
# HTML파일을 올바르게 가져오지 못했을 경우 오류를 일으킨다. (status code를 통해 판단한다)

with open("useragent.html", "w", encoding="utf8") as file:
    file.write(res.text)