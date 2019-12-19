import bs4
import requests

# 1달라 당 한화 얼마인지

html = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')
#print(html.text)
soup = bs4.BeautifulSoup(html.text, 'html.parser' )
dollar = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
print(dollar.text)



