from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv  

# url = input('Type your URL: ')
url = 'https://en.wikipedia.org/wiki/BMW_3_Series_(E90)'
file_name = input('Choose .csv file name: ')
content = []

soup = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'html.parser')

table = soup.find_all('table')[1]

rows = table.find_all('tr')

for row in rows:
    items = row.find_all('td')
    titles = rows[0].find('th')
    print(rows[0])
    print(titles)
    content.append(titles)

    with open (f'{file_name}.csv', 'w') as f:
        writer = csv.writer(f)

        writer.writerow(content[0])
        writer.writerows(content[1:])

print(items)