import os
import json

students = {}

for file_name in os.listdir ("students"):

    file = open (f"students/{file_name}", encoding = "utf-8")
    info = file.read ()
    
    start_in = info.find ('Start') + 5
    end_in = info.find ('End')

    info = info [start_in: end_in]
    
    dicts = info.split ('\n')

    while '' in dicts:
        dicts.remove ('')
    
    for d in range (len (dicts)):

        dicts [d] = tuple (dicts [d].split (': '))

    real_dict = {}

    for d_ in range (3, len (dicts)):

        real_dict [dicts[d_][0]] = dicts[d_][1]

    students [dicts [1][1] + ' ' + dicts [0][1] + ' ' + dicts [2][1]] = real_dict

print (students)

with open ('students1.json', 'w', encoding = 'utf-8') as js_file:

    json.dump (students, js_file, ensure_ascii = False, indent = 4)