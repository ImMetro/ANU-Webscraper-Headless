import json
from typing import Mapping

file = input("Enter the scraped txt file: ")
dict = {}
mappings = ['url', 'acronym', 'code', 'year', 'name', 'requirements']
with open(file) as f:
    id = 1
    for i in f:
        desc = list(i.strip().split('|'))
        url = desc[0]
        j = 0
        dict2 = {}
        while j < len(mappings):
            dict2[mappings[j]] = desc[j]
            j = j + 1
        dict[url] = dict2
        id = id + 1
 
output = open('output2.json','w')
json.dump(dict,output,indent=3)
output.close()


