import os
import re
import numbers
import requests
from BeautifulSoup import BeautifulSoup

#User input
url = ''
while(True):
    try:
        text = raw_input('\nEnter the English text you would like converted to spanish!\n')
        urlText = ''
        for char in text:
            if (char == ' '):
                urlText = urlText + '%20'
            if (char != ' '):
                urlText = urlText + char
        url = 'http://www.spanishdict.com/translate/' + urlText
    except:
        print('Unable to translate!');
    break;

#Web Scraping
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
box = soup.find('div', {'class': 'mt-info-text'})

print ('Translation: ' + str(box))


