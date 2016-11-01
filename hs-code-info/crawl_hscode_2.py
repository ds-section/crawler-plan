import requests
from bs4 import BeautifulSoup

"""
get all hscode_2
part 1. hscode_2, description, link
"""

# get all hs code list and link 
r = requests.get('http://db.wtocenter.org.tw/tariffHScode.asp')
r.encoding = 'cp950'

# parse 
soup = BeautifulSoup(r.text, 'lxml')
td_main_top = soup.find_all('td', class_='mainText', valign='top')

print('hscode_2', 'text', 'url', sep=',')

for e in td_main_top:

    url = e.find('a').get('href')
    hscode_2 = url[-2:]
    # from same hierarchies with e to find next td
    text = e.parent.find_all('td', class_='mainText')[1].find('font').text

    print(hscode_2, text, url, sep=',')

# for e in td_main:
#     print(e)
#     print('\n\n')