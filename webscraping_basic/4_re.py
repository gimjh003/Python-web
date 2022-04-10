# 정규식 = 정해진 형태를 의미하는 식

import re # 정규식 라이브러리

# ca?e
p = re.compile("ca.e") # p == pattern

# 정규식 (일부)
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)

def print_match(m): # 매칭된 값을 통해 어떠한 값을 얻을 수 있는 함수들
    if m:
        print("m.group() :", m.group()) # group : 일치하는 문자열 반환 (ex : careless -> care)
        print("m.string :", m.string) # string : 입력받은 문자열 (ex : careless -> careless)
        print("m.start() :", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() :", m.end()) # 일치하는 문자열의 끝 index+1
        print("m.span() :", m.span()) # 일치하는 문자열의 시작 index & 끝 index+1
    else:
        print("매칭되지 않음")

m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인 (실행결과 : care)
print(m.group()) # 매치되지 않으면 에러가 발생
# print_match(m)

lst = p.findall("careless cafe") # findall : 정규식에 일치하는 모든 것을 리스트 형태로 반환 ['care', 'cafe']
print(lst)

m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m) # 실행결과 : care

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식 (w3school -> python -> regular expression | python re search)
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)