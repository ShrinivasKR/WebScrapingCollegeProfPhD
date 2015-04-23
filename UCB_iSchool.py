__author__ = 'Shrinivas'

from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen('http://www.ischool.berkeley.edu/people/faculty') as response:
   html = response.read()
soup = BeautifulSoup(html)

faculty = soup.findAll('td', attrs={'class' : 'person-col-1'})
for td in faculty:
    print(td.find('a')['href'])

