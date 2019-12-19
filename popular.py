#네이버 실시간 검색어 중 1위가 무엇인지 정답 고르기
import requests
import bs4

html = requests.get('https://www.naver.com/')
soup = bs4.BeautifulSoup(html.text, 'html.parser')

keywords = soup.select('span.ah_k')

#for keyword in keywords:
#   print(keyword.text)
# 키워드 안에 문자들만 출력

# 배열[0:n] -> 배열의 0번째 인덱스부터 n-1번째 인덱스들의 요소를 가져와서 배열로 만든다.
real_keywords = keywords[0:20]
real_real_keywords = [keyword.text for keyword in real_keywords]
problem = sorted(real_real_keywords)
#가나다순 정렬로 무엇이 키워드인지 모름

print('아래의 보기 중에서 1위를 고르세요')
print(problem)
answer = input('당신이 입력한 답 : ')
if answer == real_real_keywords[0]:
    print('정답입니다!')
else:
    print('오답입니다!')

# numbers = [i for i in range(0,101)]
# print(numbers)
# [0,1,2,3,4,.....,100]
# 또는 
# numbers = []
# for i in range(0,101):
#       numbers.append(i)
#print(numbers)