import requests

url = "https://programsandcourses.anu.edu.au/data/CourseSearch/GetCourses?AppliedFilter=FilterByCourses&Source=&ShowAll=true&PageIndex=0&MaxPageSize=10&PageSize=Infinity&SortColumn=&SortDirection=&InitailSearchRequestedFromExternalPage=false&SearchText=&SelectedYear=2022&Careers%5B0%5D=&Careers%5B1%5D=&Careers%5B2%5D=&Careers%5B3%5D=&Sessions%5B0%5D=&Sessions%5B1%5D=&Sessions%5B2%5D=&Sessions%5B3%5D=&Sessions%5B4%5D=&Sessions%5B5%5D=&DegreeIdentifiers%5B0%5D=&DegreeIdentifiers%5B1%5D=&DegreeIdentifiers%5B2%5D=&FilterByMajors=&FilterByMinors=&FilterBySpecialisations=&CollegeName=All+Colleges&ModeOfDelivery=All+Modes"

headers = {
    "Host": "programsandcourses.anu.edu.au",
    "Connection": "keep-alive",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/84.0.4316.21",
    "Accept" : "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "Request-Id": "|S37FI.qO1H2",
    "sec-ch-ua-platform": "Windows",
    "Request-Context": "appId=cid-v1:775546e6-6a6e-4c3e-b8cf-c1782ef85af8",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://programsandcourses.anu.edu.au/catalogue",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9"
}

courses = []

x = requests.get(url, headers=headers).text

x = x.strip()
x = x.replace("}", "")
x = x.split("{")


with open ("anu courses.txt", 'w') as file:
    for i in range(len(x)):
        file.write(x[i] + "\n")

file.close()

#Used to store the course codes in a list instead of a .txt
courses = []

## Course Codes
with open("Anu course codes.txt", 'w') as cc:
    for i in range (len(x)):
        a = x[i][14:23]
        a = a.replace('"',"")
        cc.write(a + "\n")
        courses.append(a)

cc.close()

courses = courses[2:]

#Generic url for all the courses at ANU
link = "https://programsandcourses.anu.edu.au/2022/course/"

#Making of all the links to the courses at ANU
course_links = []
with open("course links.txt", "w") as file:
    for i in range(len(courses)):
        a = link + courses[i]
        course_links.append(a)
        file.write(a + "\n")

file.close()

