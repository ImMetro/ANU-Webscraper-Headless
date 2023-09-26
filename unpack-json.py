import json

f = open('degree_data.json')
data = json.load(f)
f.close()

with open('degree_data_processed.json', 'w') as file:
    json.dump(data['Degrees'], file, indent=2) 

file.close()

print("Completed")