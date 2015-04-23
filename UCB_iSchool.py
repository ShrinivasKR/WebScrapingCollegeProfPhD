__author__ = 'Shrinivas'

from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen('http://www.ischool.berkeley.edu/people/faculty') as response:
   html = response.read()
soup = BeautifulSoup(html)

#print(soup.prettify())
#print(soup.find_all('strong'))
for link in soup.find_all('a'):
    if "people/faculty/officehours" in link.get('href'):
        pass
    elif "people/faculty/" in link.get('href'):
       print(link.get('href'))
