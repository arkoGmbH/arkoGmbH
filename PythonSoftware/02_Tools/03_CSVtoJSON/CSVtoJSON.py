#!/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python
# Convert CSV file into a python file
# Source: https://medium.com/@hannah15198/convert-csv-to-json-with-python-b8899c722f6d
# Note to self:
# Dictionaries — maps a set of objects (keys) to another set of objects (values).
# - Use {} to create a dictionary and [] to index it.
# - Separate key and value pairs with : and commas between each key pair
# CSV Module: https://docs.python.org/3/library/csv.html
# JSON Module: https://docs.python.org/3/library/json.html?highlight=json#module-json


import csv
import json

CSVF='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/02_Tools/03_CSVtoJSON/CSVF.csv' # Text file to convert
JSONF='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/02_Tools/03_CSVtoJSON/JSNF.json' # Json as a result

# Read CSV
data={}
#with open(CSVF) as csvFile:
    #csvReader=csv.DictReader(CSVF)
    #csvReader=csv.reader(CSVF, delimiter=',')
    #for row in csvReader:
        print(', '.join(row))
        #id=rows['id']
        #data[id]=rows
#Create json and write data
#with open(JSONF,'w') as jsonFile:
    # make it readable and pretty
 #   jsonFile.write(json.dumps(data,indent=4))
    

with open('CSVF.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')