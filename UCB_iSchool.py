__author__ = 'Shrinivas'

from bs4 import BeautifulSoup
import csv
with open('names.csv', 'w') as csvfile:
    fieldnames = ['Full Name', 'University', 'Department', 'where they got their PhD']
import urllib.request
with urllib.request.urlopen('http://www.ischool.berkeley.edu/people/faculty') as response:
   html = response.read()
soup = BeautifulSoup(html)

faculty = soup.findAll('td', attrs={'class' : 'person-col-1'})
for td in faculty:
    facultyURL = ("http://www.ischool.berkeley.edu" + td.find('a')['href'])
    print(facultyURL)
    with urllib.request.urlopen(facultyURL) as response:
        html = response.read()
        facultySoup = BeautifulSoup(html)
        education = facultySoup.findAll('div', attrs={'class' : 'field-field-person-education'})
        for res in education:
            print(res.text)


writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

writer.writeheader()
writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
