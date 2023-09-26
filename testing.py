from encodings import utf_8
import json

with open('degree_data_p.json', 'r', encoding="utf_8") as file:
    data = json.load(file)

file.close()
 
with open('degree_data_pp.json', 'w') as file:
    json.dump(data, file, indent=2)