from bs4 import BeautifulSoup
import requests

html = requests.get('https://climatempo.com.br/').content

soup = BeautifulSoup(html, 'html.parser')

print(soup.a.string)
print(soup.p.string)
print(soup.li.string)
