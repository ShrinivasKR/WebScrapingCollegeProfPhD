__author__ = 'Shrinivas'

from bs4 import BeautifulSoup
import urllib.request
import re

#initial access to main page
with urllib.request.urlopen('https://education.uw.edu/people') as response:
    html = response.read()
soup = BeautifulSoup(html)
faculty = soup.findAll('td', attrs={'class': 'views-field views-field-user'})
#looping through each individual faculty
for td in faculty:
    facultyURL = ("https://education.uw.edu" + td.find('a')['href'])
    #print(facultyURL)
    with urllib.request.urlopen(facultyURL) as response:
        html = response.read()
        facultySoup = BeautifulSoup(html)
        #printing out name and department and college
        if "Ph.D" in facultySoup.text:
            print(facultySoup.title.text)
            phdSource = facultySoup.findAll(text=re.compile('Ph.D'))
            for i in phdSource:
                print(i)

