'''
Ex18-2-beautfulsoup.py

beautfulsoup
    HTML, XML 등의 마크업 언어를 파싱하는 라이브러리
    ex) <html>텍스트</html>

beautfulsoup 설치방법
pip install beautifulsoup4

'''

import requests
from bs4 import BeautifulSoup

url = 'http://news.nate.com/rank'
param = {'min': 'n1000'}
response = requests.get(url, params=param)
html = response.text

print(html)

soup = BeautifulSoup(html, 'html.parser')
tit_list = soup.find_all('h2')
for tit in tit_list:
    print(tit.text.strip())