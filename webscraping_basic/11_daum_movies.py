import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class":"thumb_img"})
for year in range(2015, 2020):
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    images = soup.find_all("img", attrs={"class":"thumb_img"})
    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f: # 텍스트가 아닌 바이너리 : wb
            f.write(image_res.content)

        if idx>=4:
            break