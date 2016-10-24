import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.globaltradealert.org/measure')
print(r.status_code)

soup = BeautifulSoup(r.text, 'lxml')

views_row = soup.find_all('div', class_='views-row')


for row in views_row:
    print(row.find('div').find('h2').text.strip())

# for a in soup.find_all('a'):
#     print(a.get('href'))