from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = input('type your URL [http://...]: ')
num = int(input('what table [1-99] (from above): '))
file_name = input('choose file name [a-z]: ')

soup = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'html.parser')

table = str(soup.find_all('table')[num-1])

df = pd.read_html("".join(table))[0]

df.to_csv(f'{file_name}.csv', index=False)