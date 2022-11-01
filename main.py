from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv  

url = input('Type your URL: ')
file_name = input('Choose .csv file name: ')
content = []

soup = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'html.parser')

table = soup.find_all('table')[1]

rows = table.find_all('tr')

for title in rows[0].find_all('th'):
    content.append(title.text)

for row in rows:
    items = row.find_all('td')
    for item in items:
        content.append(item.text)

with open (f'{file_name}.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(content)