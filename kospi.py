#네이버 증시 페이지에 대신 접속을 해서, 현재 코스피지수를 가져오는 프로그램

import requests
import bs4


# 이 주소로 요청을 보내면 응답으로 html 파일이 도착할 것
html = requests.get('https://finance.naver.com/sise/sise_index.nhn?code=KOSPI')
#print(html.text)로 html 응답받고 지움
soup = bs4.BeautifulSoup(html.text, 'html.parser')
# html text를 내가 보기 좋게 접근할 수 있도록 변경!
kospi = soup.select_one("#now_value")
# css selector로 내가 원하는 태그를 가져오겠다.
print(kospi.text)



##now_value
# pip install bs4 콘솔에 설치
# pip install requests 콘솔에 설치
