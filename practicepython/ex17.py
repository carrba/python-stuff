#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

httpsite = input("Enter site, e.g. http://bbc.com.uk ")


r = requests.get(httpsite)
soup = BeautifulSoup(r.text, 'html.parser')

paras = soup.find_all('p')

for para in paras:
    print(para.text)
