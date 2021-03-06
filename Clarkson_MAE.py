__author__ = 'Shrinivas'

from bs4 import BeautifulSoup
import csv
import re

#setting up initial reading of csv
with open('names.csv', 'w') as csvfile:
    fieldnames = ['Full Name', 'University', 'Department', 'EducationSource']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

#setting up initial access to main faculty page
import urllib.request
with urllib.request.urlopen('http://www.clarkson.edu/mae/faculty.html') as response:
   html = response.read()
soup = BeautifulSoup(html)
#print(soup.prettify())

#finding all of the individual faculty
faculty = soup.findAll('tbody')
for tbody in faculty:
    #looping through each of the faculty and going to their individual information pages
    facultyURLs = (tbody.findAll('a', attrs={'class' : 'headerLinksBlue'}))
    for a in facultyURLs:
        facultyURL = ("http://www.clarkson.edu/mae/" + a['href'])
        with urllib.request.urlopen(facultyURL) as response:
            html = response.read()
            facultySoup = BeautifulSoup(html)
            #was having trouble with putting it in a csv file, switched to print it instead
            nameAndUni = facultySoup.title.text;
            phdSource = facultySoup.findAll(text=re.compile('Ph.D'))
            for i in phdSource:
                print(nameAndUni + ', ' + 'Mechanical & Aeronautical Engineering, ' + i)

with urllib.request.urlopen('http://www.clarkson.edu/biology/faculty_pages/index.html') as response:
   html = response.read()
soup = BeautifulSoup(html)
#print(soup.prettify())

#finding all of the individual faculty
faculty = soup.findAll('tbody')
for tbody in faculty:
    #looping through each of the faculty and going to their individual information pages
    facultyURLs = (tbody.findAll('a', attrs={'class' : 'headerLinksBlue'}))
    for a in facultyURLs:
        facultyURL = ("http://www.clarkson.edu/biology/faculty_pages/" + a['href'])
        with urllib.request.urlopen(facultyURL) as response:
            html = response.read()
            facultySoup = BeautifulSoup(html)
            #was having trouble with putting it in a csv file, switched to print it instead
            nameAndUni = facultySoup.title.text;
            phdSource = facultySoup.findAll(text=re.compile('Ph.D'))
            for i in phdSource:
                print(nameAndUni + ', ' + 'Mechanical & Aeronautical Engineering, ' + i)




