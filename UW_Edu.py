__author__ = 'Shrinivas'

from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen('https://education.uw.edu/people') as response:
    html = response.read()
soup = BeautifulSoup(html)
faculty = soup.findAll('td', attrs={'class': 'views-field views-field-user'})
for td in faculty:
    facultyURL = ("https://education.uw.edu" + td.find('a')['href'])
    print(facultyURL)
    with urllib.request.urlopen(facultyURL) as response:
        html = response.read()
        facultySoup = BeautifulSoup(html)
        education = facultySoup.findAll('div', attrs={'class' : 'field-field-person-education'})
        for res in education:
            print(res.text)

