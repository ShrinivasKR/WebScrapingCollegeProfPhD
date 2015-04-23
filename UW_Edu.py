__author__ = 'Shrinivas'

from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen('https://education.uw.edu/people') as response:
    html = response.read()
soup = BeautifulSoup(html)
print(soup.prettify())
faculty = soup.findAll('td', attrs={'class': 'views-field views-field-field-last-name-1'})
for td in faculty:
    print("https://education.uw.edu" + td.find('a')['href'])

