#!/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python
# Convert CSV file into a python file
# Source: https://medium.com/@hannah15198/convert-csv-to-json-with-python-b8899c722f6d

import csv
import json

CSVF='MyCSVFile.txt' # Text file to convert
JSONF='MyConverted.json' # Json as a result

# Read CSV
data={}
with open(CSVF) as csvFile:
    csvReader=csv.DictReader(CSVF)
    for rows in csvReader:
        id=rows['id']
        data[id]=rows
#Create json and write data
with open(JSONF,'w') as jsonFile:
    # make it readable and pretty
    jsonFile.write(json.dumps(data,indent=4))
    

