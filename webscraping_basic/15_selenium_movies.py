import requests
from bs4 import BeautifulSoup
url = "https://play.google.com/store/movies?utm_source=apac_med&utm_medium=hasem&utm_content=Aug2118&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-kr-1003227-med-hasem-py-Evergreen-Aug2118-Sitelink-BKWS%7cONSEM_kwid_43700009359644016_creativeid_416407016592_device_c&gclid=Cj0KCQjwr-SSBhC9ARIsANhzu1628PUTnk_H6C4JkEtyECTAiaBgAJUCsSLts7PETADf1tVm0jXsM4oaAtVtEALw_wcB&gclsrc=aw.ds"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
headers = {"User-Agent":user_agent, "Accept-Language":"ko-KR,ko"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("a", attrs={"class":"Si6A0c ZD8Cqc"})
print(len(movies))

# with open('movie.html', "w", encoding="utf8") as f:
#     f.write(soup.prettify())

for movie in movies:
    if movie:
        title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
        print(title)
