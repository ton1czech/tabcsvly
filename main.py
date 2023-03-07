from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = input('Type your URL: ')
num = int(input('What table (number): '))
file_name = input('Choose .csv file name: ')

soup = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'html.parser')

table = str(soup.find_all('table')[num])

df = pd.read_html("".join(table))[0]

df.to_csv(f'{file_name}.csv', index=False)