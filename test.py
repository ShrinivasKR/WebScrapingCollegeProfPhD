__author__ = 'Shrinivas'

with open('names.csv', 'w') as csvfile:
    fieldnames = ['Full Name', 'University', 'Department', 'EducationSource']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()