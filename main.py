from bs4 import BeautifulSoup
import requests

# url = input('Type your URL: ')
url = 'https://en.wikipedia.org/wiki/BMW_3_Series_(E90)'
# file_name = input('Choose .csv file name: ')

soup = BeautifulSoup(requests.get(url).text, 'html.parser')