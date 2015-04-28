__author__ = 'Shrinivas'

from bs4 import BeautifulSoup
import urllib.request
import csv
import re

#setting up initial reading of csv
with open('names.csv', 'w') as csvfile:
    fieldnames = ['Full Name', 'University', 'Department', 'EducationSource']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

#setting up initial access to main faculty page

with urllib.request.urlopen('http://www.ischool.berkeley.edu/people/faculty') as response:
   html = response.read()
soup = BeautifulSoup(html)

#finding all of the individual faculty
faculty = soup.findAll('td', attrs={'class' : 'person-col-1'})
for td in faculty:
    #looping through each of the faculty and going to their individual information pages
    facultyURL = ("http://www.ischool.berkeley.edu" + td.find('a')['href'])
    #print(facultyURL)
    with urllib.request.urlopen(facultyURL) as response:
        html = response.read()
        facultySoup = BeautifulSoup(html)
        #was having trouble with putting it in a csv file, switched to print it instead
        nameAndDepartment = facultySoup.title.text;
        print(nameAndDepartment)
        education = facultySoup.findAll('div', attrs={'class' : 'field-field-person-education'})
        for res in education:
            print(res.text)
            #writer.writerow({'Full Name': 'Baked', 'University': 'UC Berkeley', 'Department': 'iSchool', 'EducationSource': 'okay'})
            print("EducationSource:" + res.text)

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
    facultyURLs = (tbody.findAll('a'))
    for a in facultyURLs:
        name = a.text
        facultyURL = ("http://www.clarkson.edu/biology/faculty_pages/" + a['href'])
        if "html" in facultyURL:
            with urllib.request.urlopen(facultyURL) as response:
                html = response.read()
                facultySoup = BeautifulSoup(html)
                #was having trouble with putting it in a csv file, switched to print it instead
                nameAndUni = facultySoup.title.text;
                phdSource = facultySoup.findAll(text=re.compile('Ph.D'))
                for i in phdSource:
                    print(nameAndUni + ', ' + name + ', ' + 'Biology, ' + i)

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

with urllib.request.urlopen('http://www.clarkson.edu/business/faculty/index.html') as response:
    html = response.read()
soup = BeautifulSoup(html)
# print(soup.prettify())

#finding all of the individual faculty
faculty = soup.findAll('tbody')
for tbody in faculty:
    #looping through each of the faculty and going to their individual information pages
    facultyURLs = (tbody.findAll('a'))
    for a in facultyURLs:
        name = a.text
        facultyURL = ("http://www.clarkson.edu/business/faculty/" + a['href'])
        if "html" in facultyURL:
            with urllib.request.urlopen(facultyURL) as response:
                html = response.read()
                facultySoup = BeautifulSoup(html)
                #was having trouble with putting it in a csv file, switched to print it instead
                nameAndUni = facultySoup.title.text;
                phdSource = facultySoup.findAll(text=re.compile('Ph.D'))
                for i in phdSource:
                    print(nameAndUni + ', ' + name + ', ' + 'Business, ' + i)

with urllib.request.urlopen('http://www.clarkson.edu/physics/faculty.html') as response:
    html = response.read()
soup = BeautifulSoup(html)
#print(soup.prettify())

#finding all of the individual faculty
faculty = soup.findAll('tbody')
for tbody in faculty:
    #looping through each of the faculty and going to their individual information pages
    facultyURLs = (tbody.findAll('a'))
    for a in facultyURLs:
        name = a.text
        facultyURL = ("http://www.clarkson.edu/physics/" + a['href'])
        if "html" in facultyURL:
            with urllib.request.urlopen(facultyURL) as response:
                html = response.read()
                facultySoup = BeautifulSoup(html)
                #was having trouble with putting it in a csv file, switched to print it instead
                nameAndUni = facultySoup.title.text;
                phdSource = facultySoup.findAll(text=re.compile('Ph.D'))
                for i in phdSource:
                    print(nameAndUni + ', ' + name + ', ' + 'Physics, ' + i)

with urllib.request.urlopen('http://www.clarkson.edu/camp/faculty/index.html') as response:
    html = response.read()
soup = BeautifulSoup(html)
#print(soup.prettify())

#finding all of the individual faculty
faculty = soup.findAll('tbody')
for tbody in faculty:
    #looping through each of the faculty and going to their individual information pages
    facultyURLs = (tbody.findAll('a'))
    for a in facultyURLs:
        name = a.text
        if "http" not in a['href']:
            facultyURL = ("http://www.clarkson.edu/camp/faculty/" + a['href'])
        else:
            facultyURL = a['href']
        if "html" in facultyURL:
            with urllib.request.urlopen(facultyURL) as response:
                html = response.read()
                facultySoup = BeautifulSoup(html)
                #was having trouble with putting it in a csv file, switched to print it instead
                nameAndUni = facultySoup.title.text;
                phdSource = facultySoup.findAll(text=re.compile('Ph.D'))
                for i in phdSource:
                    print(nameAndUni + ', ' + name + ', ' + 'Camp, ' + i)