import requests
from bs4 import BeautifulSoup

r = requests.get('https://zh.wikipedia.org/zh-tw/ISO_3166-1')
soup = BeautifulSoup(r.text, 'lxml')

table = soup.find('table', class_='wikitable')

print('country_code,' + 'country_name' + ',country_flag_link')

for row in table.find_all('tr'):
    if row.find_all('td') != []:
        
        print(
              # country_code
              row.find_all('td')[2].text + ',' + \
              
              # country_name
              row.find_all('td')[4].find('a').text + ',' + \
              
              # country_flag_link
              'https:' + \
              row.find_all('td')[4].find('img').get('src').replace('22px', '300px'))