#!/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python
# Convert CSV file into a python file
# Source: https://medium.com/@hannah15198/convert-csv-to-json-with-python-b8899c722f6d
# Note to self:
# Dictionaries — maps a set of objects (keys) to another set of objects (values).
# - Use {} to create a dictionary and [] to index it.
# - Separate key and value pairs with : and commas between each key pair
# CSV Module: https://docs.python.org/3/library/csv.html
# JSON Module: https://docs.python.org/3/library/json.html?highlight=json#module-json
# Nested dictionary access elements: https://www.programiz.com/python-programming/nested-dictionary


import csv
import json
from collections import OrderedDict




CSVF='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/02_Tools/03_CSVtoJSON/CSVF.txt' # Text file to convert
JSNF='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/02_Tools/03_CSVtoJSON/JSNF.json' # Json as a result

# Read CSV
# data={}
#with open(CSVF) as csvFile:
    #csvReader=csv.DictReader(CSVF)
    #csvReader=csv.reader(CSVF, delimiter=',')
    #for row in csvReader:
        #print(', '.join(row))
        #id=rows['id']
        #data[id]=rows

data={}
UniqueHeaderName='name' #Unique header name from which the values will be used as a key for the dictionary
with open(CSVF, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        #print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        data[line_count]=row
        old_key=line_count
        new_key=data[line_count][UniqueHeaderName]
        data[new_key] = data[old_key] # Assign a new key to the old key
        del data[old_key]                # Delete the old key
        line_count += 1 
    print(f'Processed {line_count} lines.')

# Change the dictionary key from the row number to the desired uniqueHeader one

#d = {'x':1, 'y':2, 'z':3}
#d1 = {'x':'a', 'y':'b', 'z':'c'}

#data((d1[key], value) for (key, value) in d.items())


#data.move_to_end('a')
#Create json and write data
with open(JSNF,'w') as jsonFile:
    # make it readable and pretty
    jsonFile.write(json.dumps(data,indent=4))


# Read the json file (notice that it has a nested dictionary inside on the basis of the row number)
with open(JSNF) as json_file:
    redata = json.load(json_file)
    for p in redata:
        print('Name: ' + redata[p]['name'])
        print('Bday: ' + redata[p]['birthday month'])
        print('')