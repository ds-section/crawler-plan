import requests
from bs4 import BeautifulSoup

print('http://www.tradingeconomics.com/country-list/manufacturing-pmi' + '\n')

r = requests.get('http://www.tradingeconomics.com/country-list/manufacturing-pmi')
soup = BeautifulSoup(r.text, 'lxml')


# Manufacturing PMI (monthly)
# country, last_value, last_update_time, previous_value, highest_value, lowest_value

data_table_row = soup.find_all('tr', class_='datatable-row')

for row in data_table_row:

    country = row.find_all('td')[0].find('a').text.strip()
    last_value = row.find_all('td')[1].text.strip()
    last_update_time = row.find_all('td')[2].find('span').text.strip()
    # market_trend = row.find_all('td')[3].find('span').get('class')[0]
    previous_value = row.find_all('td')[4].text.strip()
    highest_value = row.find_all('td')[5].text.strip()
    lowest_value = row.find_all('td')[6].text.strip()

    print('country:', country)
    print('last_value:', last_value)
    print('last_update_time:', last_update_time)
    # print(market_trend)
    print('previous_value:', previous_value)
    print('highest_value:', highest_value)
    print('lowest_value:', lowest_value)
    print()

# print(type(data_table_row))