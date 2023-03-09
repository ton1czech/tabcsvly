#####################################
# tabcsvly                          #
# 31/11/2022                        #
# Daniel Anthony Baudyš (ton1czech) #
#####################################

# import modules
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import re

# get user url
url = input('type your URL [http://...]: ')
# get user table
num = int(input('what table [1-99] (from above): '))
# get user filename
filename = input('choose file name [a-z]: ')

def main():
    # init scraper
    soup = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'html.parser')

    # fint html table
    table = str(soup.find_all('table')[num-1])

    # regex
    table = re.sub("\[.*\]", '', table)

    # use pandas to red html table
    df = pd.read_html("".join(table))[0]

    # show the result
    print(df)
    # save data into .csv file
    df.to_csv(f'{filename}.csv', index=False)

if __name__ == "__main__":
    main()