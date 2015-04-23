__author__ = 'Shrinivas'

from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen('https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4') as response:
   html = response.read()
soup = BeautifulSoup(html)

print(soup.prettify())
