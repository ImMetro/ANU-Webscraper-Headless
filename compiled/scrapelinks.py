import requests
from bs4 import BeautifulSoup

year = input('What year (e.g. 2018, 2019) did you want the links of')

boiler_link = f'https://programsandcourses.anu.edu.au/{year}'

#Majors
url = 'https://programsandcourses.anu.edu.au/data/MajorSearch/GetMajors?AppliedFilter=FilterByAllSpecializations&Source=&ShowAll=true&PageIndex=0&MaxPageSize=10&PageSize=Infinity&SortColumn=&SortDirection=&InitailSearchRequestedFromExternalPage=false&SearchText=&SelectedYear=2022&Careers%5B0%5D=&Careers%5B1%5D=&Careers%5B2%5D=&Careers%5B3%5D=&Sessions%5B0%5D=&Sessions%5B1%5D=&Sessions%5B2%5D=&Sessions%5B3%5D=&Sessions%5B4%5D=&Sessions%5B5%5D=&DegreeIdentifiers%5B0%5D=&DegreeIdentifiers%5B1%5D=&DegreeIdentifiers%5B2%5D=&FilterByMajors=&FilterByMinors=&FilterBySpecialisations=&CollegeName=All+Colleges&ModeOfDelivery=All+Modes'

x = requests.get(url).text

x = x.strip()
x = x.replace("}", "")
x = x.split("{")
x = x[2:]

for i in x:
    a = i.split('SubPlanCode":"')[1]
    a = a.split('"')[0]
    with open(f'{year} major minor and specialisation links.txt', 'a') as file:
        file.write(boiler_link + '/major/' + a + '\n')
    file.close()

#Minors
url = 'https://programsandcourses.anu.edu.au/data/MinorSearch/GetMinors?AppliedFilter=FilterByAllSpecializations&Source=&ShowAll=true&PageIndex=0&MaxPageSize=10&PageSize=Infinity&SortColumn=&SortDirection=&InitailSearchRequestedFromExternalPage=false&SearchText=&SelectedYear=2022&Careers%5B0%5D=&Careers%5B1%5D=&Careers%5B2%5D=&Careers%5B3%5D=&Sessions%5B0%5D=&Sessions%5B1%5D=&Sessions%5B2%5D=&Sessions%5B3%5D=&Sessions%5B4%5D=&Sessions%5B5%5D=&DegreeIdentifiers%5B0%5D=&DegreeIdentifiers%5B1%5D=&DegreeIdentifiers%5B2%5D=&FilterByMajors=&FilterByMinors=&FilterBySpecialisations=&CollegeName=All+Colleges&ModeOfDelivery=All+Modes'
x = requests.get(url).text

x = x.strip()
x = x.replace("}", "")
x = x.split("{")
x = x[2:]

for i in x:
    a = i.split('SubPlanCode":"')[1]
    a = a.split('"')[0]
    with open(f'{year} major minor and specialisation links.txt', 'a') as file:
        file.write(boiler_link + '/minor/' + a + '\n')
    file.close()

#Specialisations
url = 'https://programsandcourses.anu.edu.au/data/SpecialisationSearch/GetSpecialisations?AppliedFilter=FilterByAllSpecializations&Source=&ShowAll=true&PageIndex=0&MaxPageSize=10&PageSize=Infinity&SortColumn=&SortDirection=&InitailSearchRequestedFromExternalPage=false&SearchText=&SelectedYear=2022&Careers%5B0%5D=&Careers%5B1%5D=&Careers%5B2%5D=&Careers%5B3%5D=&Sessions%5B0%5D=&Sessions%5B1%5D=&Sessions%5B2%5D=&Sessions%5B3%5D=&Sessions%5B4%5D=&Sessions%5B5%5D=&DegreeIdentifiers%5B0%5D=&DegreeIdentifiers%5B1%5D=&DegreeIdentifiers%5B2%5D=&FilterByMajors=&FilterByMinors=&FilterBySpecialisations=&CollegeName=All+Colleges&ModeOfDelivery=All+Modes'
x = requests.get(url).text

x = x.strip()
x = x.replace("}", "")
x = x.split("{")
x = x[2:]

for i in x:
    a = i.split('SubPlanCode":"')[1]
    a = a.split('"')[0]
    with open(f'{year} major minor and specialisation links.txt', 'a') as file:
        file.write(boiler_link + '/specialisation/' + a + '\n')
    file.close()

