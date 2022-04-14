import requests
import re
from bs4 import BeautifulSoup

for i in range(1,  6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())
    for item in items:
        if item.find(attrs={"class":"ad_badge_text"}):
            continue
        name = item.find("div", attrs={"class":"name"}).get_text() # 이름
        # 애플 제품 제외
        if "Apple" in name:
            continue
        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
        # 평점 (rating)
        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class":"rating"}) # 평점
        if rate: rate = rate.get_text()
        else: continue
        # 평점 수 (rating-total-count)
        rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
        if rate_cnt: rate_cnt = rate_cnt.get_text()[1:-1] # (리뷰수) 를 그냥 숫자만
        else : continue
        # 평점 4.5 이상, 리뷰 50개 이상
        if float(rate) >= 4.5 and int(rate_cnt)>=100:
            link = item.find("a", attrs={"class":"search-product-link"})["href"]
            print("상품 : {}\n가격 : {}\n평점 : {} ({})\n바로가기 : {}\n{}".format(name, price, rate, rate_cnt, "https://www.coupang.com"+link, "-"*77))