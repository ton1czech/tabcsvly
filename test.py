from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/tables"

html_code = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_code, 'html.parser')

first_table = soup.find('table')
rows = first_table.findAll('tr')[1:]
last_names = []
for row in rows:
    names = row.find_all('td')[2]

    last_names.append(names.get_text())

print(last_names)