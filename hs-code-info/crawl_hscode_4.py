import requests
from bs4 import BeautifulSoup
"""
get all hscode_4 by urls in hscode2.csv
"""
def print_hscode_4_from_2(url_2):

    r = requests.get(url_2)
    r.encoding = 'cp950'
    soup = BeautifulSoup(r.text, 'lxml')
    td_main_top = soup.find_all('td', class_='mainText', valign='top')

    for e in td_main_top:

        url_4 = e.find('a').get('href')
        hscode_4 = url_4[-4:]
        # from same hierarchies with e to find next td
        text = e.parent.find_all('td', class_='mainText')[1].find('font').text
        text = text.strip()

        print(hscode_4, text, url_4, sep=',')

url_list = []
with open('hscode2.csv', 'r') as f:
    
    for line in f:

        url = line.split(',')[2].replace('\n', '')
        url_list.append('http://db.wtocenter.org.tw/' + url)

    # filter headers out
    url_list = url_list[1::]


print('hscode_4', 'text', 'url', sep=',')

for url in url_list:
    print_hscode_4_from_2(url)