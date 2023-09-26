import json

import requests


url = "https://programsandcourses.anu.edu.au/data/CourseSearch/GetCourses?AppliedFilter=FilterByCourses&Source=&ShowAll=true&PageIndex=0&MaxPageSize=10&PageSize=Infinity&SortColumn=&SortDirection=&InitailSearchRequestedFromExternalPage=false&SearchText=&SelectedYear=2022&Careers%5B0%5D=&Careers%5B1%5D=&Careers%5B2%5D=&Careers%5B3%5D=&Sessions%5B0%5D=&Sessions%5B1%5D=&Sessions%5B2%5D=&Sessions%5B3%5D=&Sessions%5B4%5D=&Sessions%5B5%5D=&DegreeIdentifiers%5B0%5D=&DegreeIdentifiers%5B1%5D=&DegreeIdentifiers%5B2%5D=&FilterByMajors=&FilterByMinors=&FilterBySpecialisations=&CollegeName=All+Colleges&ModeOfDelivery=All+Modes"

# Generic url for all the courses at ANU
link = "https://programsandcourses.anu.edu.au/2022/course/"

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


def process_session(session_name):
    if session_name == 'First Semester':
        return 'Semester 1'
    elif session_name == 'Second Semester':
        return 'Semester 2'
    elif session_name == 'Spring Session':
        return 'Spring'
    elif session_name == 'Summer Session':
        return 'Summer'
    elif session_name == 'Autumn Session':
        return 'Autumn'
    elif session_name == 'Winter Session':
        return 'Winter'
    else:
        raise Exception(f"Unknown Session Code {session_name}")


plain_data = requests.get(url, headers=headers).text

# load the plain data as json data (it is a dict)
json_data = json.loads(plain_data)

# print out to see what it look like
# print(json_data)

# course item list
items = json_data['Items']
print(f"total courses entries: {len(items)}")

# set of added courses, for validate uniqueness
visited_course = set()
# course list
courses = []

for course_data in items:
    course_code = course_data['CourseCode']
    # check if the course already been added (probably should not happen)
    if course_code in visited_course:
        print(f'Duplicated course {course_code}, skipped. ')
        continue

    course_session = course_data['Session']
    if course_session == '':
        # bad data...why a course can without session?
        print(f'Course {course_code} missing session, skipped. ')
        continue
    # print(course_session)

    # the dictionary for store a processed course data
    course = dict()
    # data: according to the specification
    course['id'] = "ANU-" + course_code
    course['code'] = course_code
    course['university'] = "ANU"  # always ANU for this script
    course['career'] = course_data['Career']
    course['name'] = course_data['Name']
    course['sessions'] = [process_session(s) for s in course_session.split('/')]
    course['default_icon'] = "public_rounded"
    course['units'] = float(course_data['Units'])
    course['delivery'] = course_data['ModeOfDelivery']
    course['url'] = f"{link}{course_code}"  # url to course, did not get used at the moment?
    courses.append(course)
    visited_course.add(course_code)
    print('+', course_code)
    # print(course_data)

print(f"total processed courses: {len(courses)}")

output = dict()
output['Courses'] = courses

# write output
with open('courses_data.json', 'w') as json_file:
    json.dump(output, json_file, indent=2)
print('Task Complete')
