import requests

url = 'https://programsandcourses.anu.edu.au/data/ProgramSearch/GetProgramsUnderGraduate?AppliedFilter=FilterByPrograms&Source=&ShowAll=true&PageIndex=0&MaxPageSize=10&PageSize=Infinity&SortColumn=&SortDirection=&InitailSearchRequestedFromExternalPage=false&SearchText=&SelectedYear=2022&Careers%5B0%5D=&Careers%5B1%5D=&Careers%5B2%5D=&Careers%5B3%5D=&Sessions%5B0%5D=&Sessions%5B1%5D=&Sessions%5B2%5D=&Sessions%5B3%5D=&Sessions%5B4%5D=&Sessions%5B5%5D=&DegreeIdentifiers%5B0%5D=&DegreeIdentifiers%5B1%5D=Flexible+Double&DegreeIdentifiers%5B2%5D=&FilterByMajors=&FilterByMinors=&FilterBySpecialisations=&CollegeName=All+Colleges&ModeOfDelivery=All+Modes'

x= requests.get(url).text

x = x.strip()
x = x.replace("}", "")
x = x.split("{")
x = x[2:]

flexi = []

for i in x:
    b = i.split('"AcademicPlanCode":"')[1]
    b = b.split('"')[0]
    flexi.append(b)


