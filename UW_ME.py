__author__ = 'Shrinivas'

from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen('https://www.me.washington.edu/research/faculty.html') as response:
   html = response.read()
soup = BeautifulSoup(html)

#print(soup.prettify())
#print(soup.find_all('strong'))
for link in soup.find_all('a'):
    print(link.get('href'))